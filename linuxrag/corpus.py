import hashlib
import json
import re
from dataclasses import asdict, dataclass
from pathlib import Path


@dataclass(frozen=True)
class Chunk:
    id: str
    command: str
    title: str
    text: str
    source: str
    url: str
    revision: str
    language: str
    platform: str
    license: str
    attribution: str
    card_text: str = ""


def split_markdown(text: str, command: str, limit: int = 1400) -> list[tuple[str, str]]:
    """Split on headings/paragraphs; fenced code is always an indivisible block."""
    sections = []
    title, lines, fence = command, [], None
    for line in text.splitlines():
        marker = re.match(r"^\s*(`{3,}|~{3,})", line)
        heading = re.match(r"^#{1,6}\s+(.+)", line) if fence is None else None
        if heading:
            if lines:
                sections.append((title, "\n".join(lines)))
            title, lines = heading.group(1).strip(), []
            continue
        lines.append(line)
        if marker:
            token = marker.group(1)
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence):
                fence = None
    if lines:
        sections.append((title, "\n".join(lines)))
    chunks = []
    for title, body in sections:
        blocks, block, fence = [], [], None
        for line in body.splitlines():
            marker = re.match(r"^\s*(`{3,}|~{3,})", line)
            if marker:
                token = marker.group(1)
                if fence is None:
                    fence = token
                elif token[0] == fence[0] and len(token) >= len(fence):
                    fence = None
            if not line.strip() and fence is None:
                if block:
                    blocks.append("\n".join(block))
                    block = []
            else:
                block.append(line)
        if block:
            blocks.append("\n".join(block))
        current = ""
        for block in blocks:
            if current and len(current) + len(block) > limit:
                chunks.append((title, f"命令：{command}\n章节：{title}\n\n{current}"))
                current = ""
            current = (current + "\n\n" + block).strip()
        if current:
            chunks.append((title, f"命令：{command}\n章节：{title}\n\n{current}"))
    return chunks


def read_corpus(knowledge_dir: Path) -> tuple[list[Chunk], dict]:
    """Only curated retrieval Markdown is indexed; raw sources are provenance."""
    manifest = json.loads((knowledge_dir / "manifest.json").read_text())
    if manifest.get("schema_version") != 2:
        raise ValueError("知识库版本不受支持。")
    sources = manifest["sources"]
    lock = json.loads((knowledge_dir / "sources.lock.json").read_text())
    if sources != lock:
        raise ValueError("Source manifest differs from sources.lock.json")
    chunks, seen = [], set()

    def read(relative: str) -> str:
        path = (knowledge_dir / relative).resolve()
        if not path.is_relative_to(knowledge_dir.resolve()):
            raise ValueError("知识库路径越界。")
        return path.read_text()

    for entry in manifest["commands"]:
        command = entry["id"]
        if command in seen or not re.fullmatch(r"[a-z][a-z0-9_-]*", command):
            raise ValueError(f"重复或无效的命令标识：{command}")
        seen.add(command)
        card, retrieval = read(entry["card"]), read(entry["retrieval"])
        raw = read(entry["raw"])
        if hashlib.sha256(raw.encode()).hexdigest() != entry["raw_sha256"]:
            raise ValueError(f"{command} 上游原文与固定摘要不一致。")
        if not card.startswith(f"## {command}\n") or card.count("```") not in {4, 6, 8}:
            raise ValueError(f"{command} 卡片需要正确标题和2–4 个示例代码块。")
        if not retrieval.startswith(f"# {command} 检索说明\n"):
            raise ValueError(f"{command} 检索文本标题不一致。")
        if "### 常用参数" not in card or "### 常用例子" not in card:
            raise ValueError(f"{command} 缺少展示章节。")
        summary = card.split("\n\n")[1]
        info = sources[entry["source"]]
        for number, (title, content) in enumerate(split_markdown(retrieval, command)):
            text = f"{command}：{summary}\n适用实现：{entry['implementation']}\n\n{content}"
            identity = f"{command}:{number}:{text}"
            chunks.append(
                Chunk(
                    hashlib.sha256(identity.encode()).hexdigest()[:24],
                    command,
                    title,
                    text,
                    entry["source"],
                    entry["url"],
                    info["revision"],
                    "zh",
                    "linux",
                    info["license"],
                    info["author"],
                    card,
                )
            )
    if not chunks:
        raise ValueError("知识库为空。")
    return chunks, sources


def preserve_licenses(knowledge_dir: Path, target: Path, sources: dict) -> None:
    target.mkdir(parents=True, exist_ok=True)
    for name, info in sources.items():
        dest = target / name
        dest.mkdir(exist_ok=True)
        (dest / "LICENSE.txt").write_bytes((knowledge_dir / "licenses" / f"{name}.txt").read_bytes())
        (dest / "ATTRIBUTION.json").write_text(json.dumps(info, ensure_ascii=False, indent=2))


def chunk_dict(chunk: Chunk) -> dict:
    result = asdict(chunk)
    result.pop("card_text")
    result["command_id"] = chunk.command
    return result
