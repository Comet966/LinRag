import hashlib
import json
import logging
import re
import sqlite3
import uuid
from collections import Counter, defaultdict
from pathlib import Path

import jieba
import numpy as np

from .config import Endpoint, Settings
from .corpus import Chunk, chunk_dict, preserve_licenses
from .provider import Provider, ProviderError

jieba.setLogLevel(logging.WARNING)
STOP = set(
    "的 了 和 与 在 是 怎么 如何 一个 所有 使用 进行 可以 请 帮 我 想 要 地 得 来 将 中 并 及 或 有 哪些 什么".split()
)


def tokenize(text: str) -> list[str]:
    tokens = re.findall(r"[a-zA-Z0-9_./]+(?:[-+][a-zA-Z0-9_./]+)*|--?[a-zA-Z0-9][a-zA-Z0-9_-]*", text)
    tokens = [token if token.startswith("-") else token.lower() for token in tokens]
    for run in re.findall(r"[\u4e00-\u9fff]+", text):
        tokens.extend(word for word in jieba.lcut(run) if word.strip() and word not in STOP)
    return tokens


def signature(endpoint: Endpoint) -> str:
    return hashlib.sha256(f"{endpoint.base_url.rstrip('/')}|{endpoint.model}".encode()).hexdigest()


def build_index(
    settings: Settings,
    chunks: list[Chunk],
    sources: dict,
    *,
    lexical_only: bool = False,
    provider: Provider | None = None,
    knowledge_dir: Path = Path("knowledge"),
) -> dict:
    if not chunks:
        raise ValueError("不能建立空索引。")
    if not lexical_only and not settings.embed.ready:
        raise ValueError("请配置 EMBED_*，或使用 --lexical-only 建立关键词索引。")
    cards = {}
    for chunk in chunks:
        card = chunk.card_text or chunk.text
        if chunk.command in cards and cards[chunk.command] != card:
            raise ValueError(f"{chunk.command} 的展示卡片内容不一致。")
        cards[chunk.command] = card
    provider = provider or Provider(settings.timeout)
    generation = uuid.uuid4().hex
    target = settings.data_dir / "indexes" / generation
    target.mkdir(parents=True)
    metadata = {
        "schema_version": 2,
        "generation": generation,
        "chunks": len(chunks),
        "commands": len(cards),
        "sources": sources,
        "vector": False,
        "corpus_sha256": hashlib.sha256(
            json.dumps(
                [chunk_dict(c) | {"card_text": c.card_text} for c in chunks],
                ensure_ascii=False,
                sort_keys=True,
            ).encode()
        ).hexdigest(),
    }
    try:
        with sqlite3.connect(target / "corpus.sqlite3") as db:
            db.execute("CREATE TABLE chunks (position INTEGER PRIMARY KEY, id TEXT UNIQUE, payload TEXT)")
            db.execute("CREATE TABLE cards (command_id TEXT PRIMARY KEY, markdown TEXT NOT NULL)")
            db.executemany("INSERT INTO cards VALUES (?, ?)", cards.items())
            db.executemany(
                "INSERT INTO chunks VALUES (?, ?, ?)",
                ((i, c.id, json.dumps(chunk_dict(c), ensure_ascii=False)) for i, c in enumerate(chunks)),
            )
        if not lexical_only:
            batches = []
            for start in range(0, len(chunks), settings.batch_size):
                batches.append(
                    provider.embeddings(
                        settings.embed, [c.text for c in chunks[start : start + settings.batch_size]]
                    )
                )
            try:
                vectors = np.concatenate(batches)
            except ValueError as exc:
                raise ProviderError("不同批次的向量维度不一致。") from exc
            np.save(target / "vectors.npy", vectors, allow_pickle=False)
            metadata.update(
                vector=True, dimensions=vectors.shape[1], embedding_signature=signature(settings.embed)
            )
        preserve_licenses(knowledge_dir, target / "licenses", sources)
        (target / "manifest.json").write_text(json.dumps(metadata, ensure_ascii=False, indent=2))
        # Publish only a complete generation; failed builds leave the last good index available.
        pointer = settings.data_dir / f"current-{generation}.tmp"
        pointer.write_text(generation)
        pointer.replace(settings.data_dir / "CURRENT")
    except (OSError, ValueError, ProviderError):
        (target / "FAILED").touch()
        raise
    return metadata


class Index:
    def __init__(self, settings: Settings, provider: Provider | None = None):
        self.settings = settings
        self.provider = provider or Provider(settings.timeout)
        self.rows = []
        self.metadata = {}
        self.cards = {}
        self.vectors = None
        pointer = settings.data_dir / "CURRENT"
        if not pointer.exists():
            return
        generation = pointer.read_text().strip()
        if not re.fullmatch(r"[a-f0-9]{32}", generation):
            raise ValueError("索引指针无效，请重新建立索引。")
        root = settings.data_dir / "indexes" / generation
        self.metadata = json.loads((root / "manifest.json").read_text())
        if self.metadata.get("schema_version") != 2:
            raise ValueError("旧索引不支持命令卡片，请审核新知识库后重建。")
        with sqlite3.connect(f"{(root / 'corpus.sqlite3').resolve().as_uri()}?mode=ro", uri=True) as db:
            self.cards = dict(db.execute("SELECT command_id, markdown FROM cards"))
            self.rows = [
                json.loads(row[0]) for row in db.execute("SELECT payload FROM chunks ORDER BY position")
            ]
        if any(row["command"] not in self.cards for row in self.rows):
            raise ValueError("检索片段缺少对应的展示卡片。")
        if self.metadata["vector"]:
            self.vectors = np.load(root / "vectors.npy", allow_pickle=False)
            if self.vectors.shape != (len(self.rows), self.metadata["dimensions"]):
                raise ValueError("索引向量与文档数量不匹配，请重建索引。")
        self.postings = defaultdict(list)
        self.lengths = np.zeros(len(self.rows))
        for i, row in enumerate(self.rows):
            tokens = tokenize(f"{row['command']} {row['command']} {row['title']} {row['text']}")
            self.lengths[i] = len(tokens)
            for token, count in Counter(tokens).items():
                self.postings[token].append((i, count))
        self.average_length = max(float(self.lengths.mean()), 1) if self.rows else 1

    @property
    def vector_ready(self) -> bool:
        return (
            self.vectors is not None
            and self.settings.embed.ready
            and self.metadata.get("embedding_signature") == signature(self.settings.embed)
        )

    def lexical_scores(self, query: str) -> np.ndarray:
        scores = np.zeros(len(self.rows))
        for token in set(tokenize(query)):
            entries = self.postings.get(token, [])
            if not entries:
                continue
            idf = np.log(1 + (len(self.rows) - len(entries) + 0.5) / (len(entries) + 0.5))
            for i, count in entries:
                scores[i] += (
                    idf * count * 2.5 / (count + 1.5 * (0.25 + 0.75 * self.lengths[i] / self.average_length))
                )
        return scores

    def search(self, query: str, top_k: int = 6, *, mode: str = "hybrid") -> dict:
        if not self.rows:
            return {"results": [], "mode": "unavailable", "warnings": ["索引为空，请先导入语料并建立索引。"]}
        lexical = self.lexical_scores(query)

        def command_ranking(scores):
            # Each channel contributes once per command, based on its best fragment.
            ranking, seen = [], set()
            for value in np.argsort(-scores, kind="stable"):
                i = int(value)
                command = self.rows[i]["command"]
                if scores[i] <= 0:
                    break
                if command not in seen:
                    ranking.append(i)
                    seen.add(command)
                if len(ranking) >= max(20, top_k):
                    break
            return ranking

        lex_order = command_ranking(lexical)
        rankings, semantic, warnings = [lex_order], None, []
        actual_mode = "lexical"
        if mode == "hybrid" and self.vector_ready:
            try:
                vector = self.provider.embeddings(self.settings.embed, [query])[0]
                if vector.shape[0] != self.vectors.shape[1]:
                    raise ProviderError("查询向量维度已变化，请重建索引。")
                semantic = self.vectors @ vector
                rankings.append(command_ranking(semantic))
                actual_mode = "hybrid"
            except ProviderError as exc:
                warnings.append(str(exc) + " 已使用关键词检索。")
        elif mode == "hybrid":
            warnings.append("向量索引未就绪或模型配置已变化；当前使用关键词检索。配置模型后请重建索引。")
        fused, representatives, semantic_best, lexical_best = defaultdict(float), {}, {}, {}
        for channel, ranking in enumerate(rankings):
            for rank, i in enumerate(ranking, 1):
                command = self.rows[i]["command"]
                fused[command] += 1 / (60 + rank)
                representatives.setdefault(command, i)
                (lexical_best if channel == 0 else semantic_best)[command] = i
        mentioned = set(re.findall(r"[a-zA-Z0-9_]+(?:[-+][a-zA-Z0-9_]+)*", query.lower()))
        for command in fused:
            if command.lower() in mentioned:
                fused[command] += 0.04
        results = []
        for command in sorted(fused, key=lambda c: (-fused[c], c))[:top_k]:
            i = representatives[command]
            row = self.rows[i]
            results.append(
                {
                    **row,
                    "id": command,
                    "command_id": command,
                    "title": command,
                    "text": self.cards[command],
                    "matched_text": row["text"],
                    "matched_chunk_id": row["id"],
                    "citation": len(results) + 1,
                    "score": round(fused[command], 6),
                    "lexical_score": round(float(lexical[lexical_best[command]]), 6)
                    if command in lexical_best
                    else 0.0,
                    "semantic_score": round(float(semantic[semantic_best[command]]), 6)
                    if command in semantic_best
                    else None,
                }
            )
        return {"results": results, "mode": actual_mode, "warnings": warnings}
