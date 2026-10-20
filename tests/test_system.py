import json
from dataclasses import replace
from pathlib import Path

import httpx
import pytest
from fastapi.testclient import TestClient

from linuxrag.app import create_app
from linuxrag.config import Endpoint, Settings
from linuxrag.corpus import Chunk, read_corpus, split_markdown
from linuxrag.index import Index, build_index, tokenize
from linuxrag.provider import Provider, ProviderError
from linuxrag.rendering import render_markdown


@pytest.fixture
def settings(tmp_path):
    return Settings(data_dir=tmp_path)


@pytest.fixture
def chunks():
    return [
        Chunk(
            "grep",
            "grep",
            "递归搜索",
            "grep -r 递归搜索文件内容，查找匹配的文本。",
            "test",
            "https://github.com/example/docs/blob/revision/grep.md",
            "revision",
            "zh",
            "linux",
            "MIT",
            "Test",
        ),
        Chunk(
            "df",
            "df",
            "磁盘空间",
            "df -h 查看磁盘空间使用情况。",
            "test",
            "https://github.com/example/docs/blob/revision/df.md",
            "revision",
            "zh",
            "linux",
            "MIT",
            "Test",
        ),
    ]


@pytest.fixture
def index(settings, chunks):
    build_index(settings, chunks, {}, lexical_only=True)
    return Index(settings)


def test_split_preserves_fenced_code():
    code = "```sh\n# not a heading\n" + "echo x\n" * 400 + "\n```"
    document = "# grep\n简介\n\n## 示例\n说明\n\n" + code + "\n\n结尾"
    result = split_markdown(document, "grep", limit=100)
    assert sum(code in text for _, text in result) == 1
    assert all(text.count("```") % 2 == 0 for _, text in result)
    assert all("命令：grep" in text for _, text in result)


def test_tokenization_preserves_options():
    tokens = tokenize("grep -r --ignore-case 如何递归搜索文件")
    assert {"grep", "-r", "--ignore-case", "递归"} <= set(tokens)


def test_repeated_build_is_idempotent(settings, chunks):
    first = build_index(settings, chunks, {}, lexical_only=True)
    second = build_index(settings, chunks, {}, lexical_only=True)
    assert first["generation"] != second["generation"]
    assert len(Index(settings).rows) == 2


def test_lexical_search_and_no_results(index):
    assert index.search("grep -r")["results"][0]["command"] == "grep"
    assert index.search("磁盘空间")["results"][0]["command"] == "df"
    assert index.search("zzzznonexistent")["results"] == []
    assert index.search("grep")["mode"] == "lexical"


def test_api_validation_health_and_empty(settings, index):
    with TestClient(create_app(settings, index)) as client:
        assert client.get("/").status_code == 200
        assert client.get("/static/app.js").status_code == 200
        health = client.get("/api/health").json()
        assert health["chunks"] == 2 and "chat_ready" not in health
        assert "api_key" not in json.dumps(health)
        assert client.post("/api/search", json={"query": " ", "top_k": 0}).status_code == 422
        assert (
            client.post("/api/search", json={"query": "grep", "top_k": 1}).json()["results"][0]["command"]
            == "grep"
        )
        assert client.post("/api/ask", json={"query": "grep"}).status_code == 404
    with TestClient(create_app(replace(settings, data_dir=settings.data_dir / "empty"))) as client:
        assert not client.get("/api/health").json()["index_ready"]
        assert client.post("/api/search", json={"query": "grep"}).json()["results"] == []


def mock_provider():
    def handle(request):
        assert request.url.path.endswith("/embeddings")
        data = json.loads(request.content)
        return httpx.Response(
            200,
            json={
                "data": [
                    {"index": i, "embedding": [1, 0] if "grep" in text else [0, 1]}
                    for i, text in enumerate(data["input"])
                ]
            },
        )

    return Provider(transport=httpx.MockTransport(handle))


def configured(settings):
    endpoint = Endpoint("https://provider.example/v1", "secret", "test-model")
    return replace(settings, embed=endpoint)


def test_changed_model_falls_back(settings, chunks):
    settings = configured(settings)
    build_index(settings, chunks, {}, provider=mock_provider())
    other = replace(settings, embed=replace(settings.embed, model="different"))
    index = Index(other, mock_provider())
    assert not index.vector_ready
    assert index.search("grep")["mode"] == "lexical"
    assert index.search("grep")["warnings"]


def test_timeouts_keep_evidence(settings, chunks):
    settings = configured(settings)
    build_index(settings, chunks, {}, provider=mock_provider())

    def timeout(request):
        raise httpx.ReadTimeout("secret-url", request=request)

    result = Index(settings, Provider(transport=httpx.MockTransport(timeout))).search("grep")
    assert result["mode"] == "lexical" and result["results"]
    assert "secret" not in json.dumps(result)


def test_failed_build_preserves_previous_generation(settings, chunks):
    settings = configured(settings)
    build_index(settings, chunks, {}, lexical_only=True)
    before = (settings.data_dir / "CURRENT").read_text()
    provider = Provider(transport=httpx.MockTransport(lambda r: httpx.Response(401, text="secret")))
    with pytest.raises(ProviderError, match="HTTP 401"):
        build_index(settings, chunks, {}, provider=provider)
    assert (settings.data_dir / "CURRENT").read_text() == before
    assert len(Index(settings).rows) == 2


def test_bad_embedding_dimensions(settings, chunks):
    settings = configured(settings)
    build_index(settings, chunks, {}, provider=mock_provider())

    def response(request):
        return httpx.Response(200, json={"data": [{"index": 0, "embedding": [1, 0, 0]}]})

    index = Index(settings, Provider(transport=httpx.MockTransport(response)))
    result = index.search("grep")
    assert result["mode"] == "lexical"
    assert "维度" in result["warnings"][0]


@pytest.mark.parametrize(
    "data", [[], [{"index": 0, "embedding": [0, 0]}], [{"index": 1, "embedding": [1, 0]}]]
)
def test_invalid_vectors(data):
    provider = Provider(transport=httpx.MockTransport(lambda r: httpx.Response(200, json={"data": data})))
    with pytest.raises(ProviderError):
        provider.embeddings(Endpoint("https://provider.example", "secret", "m"), ["test"])


def test_html_safety():
    result = render_markdown("<script>alert(1)</script>\n\n[x](javascript:alert(1))")
    assert "<script>" not in result
    assert 'href="javascript:' not in result


def test_corrupt_index_has_actionable_health(settings):
    settings.data_dir.mkdir(exist_ok=True)
    (settings.data_dir / "CURRENT").write_text("../../bad")
    with TestClient(create_app(settings)) as client:
        assert client.get("/api/health").json()["error"]
        assert client.post("/api/search", json={"query": "grep"}).json()["results"] == []


def test_hybrid_search_with_existing_vector_index(settings, chunks):
    settings = configured(settings)
    provider = mock_provider()
    build_index(settings, chunks, {}, provider=provider)
    with TestClient(create_app(settings, Index(settings, provider))) as client:
        result = client.post("/api/search", json={"query": "grep -r"}).json()
        assert result["mode"] == "hybrid"
        assert result["results"][0]["semantic_score"] == 1
        assert "html" in result["results"][0]
        assert "answer" not in result
        assert "/api/ask" not in client.get("/openapi.json").json()["paths"]


def test_search_renders_markdown(settings, chunks):
    source = "# 标题\n\n- 示例\n\n```sh\ngrep -r test .\n```\n\n| 参数 | 含义 |\n| --- | --- |\n| -r | 递归 |"
    chunks = [replace(chunks[0], text=source)]
    build_index(settings, chunks, {}, lexical_only=True)
    with TestClient(create_app(settings)) as client:
        row = client.post("/api/search", json={"query": "grep"}).json()["results"][0]
        assert row["text"] == source
        for markup in ("<h1>", "<ul>", '<code class="language-sh">', "<table>"):
            assert markup in row["html"]


def test_option_case_and_numeric_option():
    tokens = tokenize("ls -a -A -1 grep -f -F")
    assert {"-a", "-A", "-1", "-f", "-F"} <= set(tokens)


def test_parent_card_is_returned_once(settings, chunks):
    card = "## grep\n\n展示说明，不包含检索用语。"
    children = [
        replace(chunks[0], id=f"grep-{i}", text=f"独特检索词 日志 {i}", card_text=card) for i in range(30)
    ]
    build_index(settings, children + [chunks[1]], {}, lexical_only=True)
    index = Index(settings)
    rows = index.search("独特检索词")["results"]
    assert len(rows) == 1
    assert rows[0]["text"] == card
    assert "独特检索词" in rows[0]["matched_text"]
    assert rows[0]["command_id"] == "grep"
    assert index.metadata["commands"] == 2
    assert index.metadata["chunks"] == 31


def test_candidate_limit_counts_commands_not_chunks(settings, chunks):
    many = [replace(chunks[0], id=f"a-{i}", text="shared token", card_text="card") for i in range(30)]
    other = replace(chunks[1], text="shared token other", card_text="df card")
    build_index(settings, many + [other], {}, lexical_only=True)
    assert {r["command"] for r in Index(settings).search("shared")["results"]} == {"grep", "df"}


def test_repeated_fragments_do_not_inflate_rrf(settings, chunks):
    one = replace(chunks[0], text="shared", card_text="card")
    build_index(settings, [one], {}, lexical_only=True)
    score = Index(settings).search("shared")["results"][0]["score"]
    build_index(settings, [replace(one, id=f"{i}") for i in range(30)], {}, lexical_only=True)
    assert Index(settings).search("shared")["results"][0]["score"] == score


def test_embeddings_receive_only_retrieval_text(settings, chunks):
    inputs = []

    class FakeProvider:
        def embeddings(self, endpoint, texts):
            import numpy as np

            inputs.extend(texts)
            return np.array([[1.0, 0.0] for _ in texts])

    child = replace(chunks[0], card_text="DISPLAY_ONLY")
    build_index(configured(settings), [child], {}, provider=FakeProvider())
    assert inputs == [child.text]
    assert "DISPLAY_ONLY" not in inputs


def test_curated_corpus_is_complete_and_mapped():
    chunks, sources = read_corpus(Path("knowledge"))
    assert len({c.command for c in chunks}) == 50
    assert len(chunks) == 200
    assert len({c.id for c in chunks}) == len(chunks)
    assert set(sources) == {"linux-command"}
    for chunk in chunks:
        assert chunk.card_text.startswith(f"## {chunk.command}\n")
        assert f"命令：{chunk.command}" in chunk.text
        assert "适用实现：" in chunk.text


def test_full_corpus_lexical_smoke(settings):
    chunks, sources = read_corpus(Path("knowledge"))
    build_index(settings, chunks, sources, lexical_only=True)
    index = Index(settings)
    cases = [
        ("日志轮转后继续监控", "tail"),
        ("磁盘还剩多少空间", "df"),
        ("用户属于哪些组", "id"),
        ("查程序的 PID", "pgrep"),
        ("统计重复行次数", "uniq"),
        ("远程登录服务器", "ssh"),
        ("创建多级目录", "mkdir"),
        ("which -a", "which"),
    ]
    for query, expected in cases:
        result = index.search(query, mode="lexical")
        assert expected in {r["command"] for r in result["results"]}, query
        assert len({r["command"] for r in result["results"]}) == len(result["results"])
