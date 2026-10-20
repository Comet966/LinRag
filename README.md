# LinuxRag

简洁的 Linux 命令搜索网站：输入命令名、参数或中文任务，回车搜索。默认聚焦输入栏，`/` 或 `⌘/Ctrl + K` 返回输入栏。只使用 embedding 检索，不使用问答模型。

## 当前进度：等待知识库审核

旧知识库及向量索引已删除。第一批 50 个常用命令已整理为展示和检索两层，**尚未向量化，也未启动验收服务**。已有 `.env` 保留，无需覆盖。

请先打开 [知识库审核目录](knowledge/REVIEW.md)，检查展示说明、常用参数、例子，以及检索文本是否覆盖你的表达习惯。

```bash
uv run linuxrag validate
```

该命令只检查本地语料，不调用模型、不写索引。当前应显示 50 个命令、200 个检索片段。

## 数据位置与维护

| 位置 | 用途 |
| --- | --- |
| `knowledge/cards/*.md` | 用户看到的完整命令卡片，每个命令一个文件 |
| `knowledge/retrieval/*.md` | 实际检索文本，按章节切分后送入 embedding |
| `knowledge/raw/linux-command/*.md` | 50 份上游 Markdown，仅供追溯，不参与索引 |
| `knowledge/manifest.json` | 命令标识、文件映射、实现范围、来源和原文摘要 |
| `knowledge/sources.lock.json` | 固定上游版本 |
| `knowledge/licenses/` | 原始许可声明 |

直接编辑 Markdown 即可维护内容；修改参数时同步修改展示和检索两个文件，然后运行校验。增加命令需同时更新 manifest。审核完成后，每次修改语料都需要重建索引并重启服务。原始 Markdown 不应直接修改，更新来源需同步记录版本和摘要。

## 审核通过后再执行

以下是后续第 3、4 步，现在不需要运行。

1. 安装依赖：`uv sync --python 3.12`。
2. 确认 `.env` 中的 `EMBED_BASE_URL`、`EMBED_API_KEY`、`EMBED_MODEL`；保留已有配置，不要覆盖密钥。地址包含 API 前缀但不包含 `/embeddings`。
3. `uv run linuxrag build`：完整向量化检索层，并构建关键词索引。
4. `uv run linuxrag serve`：打开 <http://127.0.0.1:8000> 验收。

`build` 和后续语义查询会调用模型服务。更换模型或地址后需重建。`build --lexical-only` 可用于关键词模式，但不能代表向量检索效果。新索引完成后才原子更新 `data/CURRENT`，失败不会覆盖此前可用索引。

## 检索方式

每个检索片段保留命令名、简介和适用实现。BM25 和向量检索各按最佳片段召回最多 20 个不同命令，再以 RRF 融合命令排名，提升显式命令名匹配。多个片段不会重复贡献同一通道的融合分数。最终每个命令只返回一张展示卡片。参数大小写保留，例如 `-a` 与 `-A`。

索引位于 `data/indexes/<generation>/`：SQLite 的 `cards` 表保存展示 Markdown，`chunks` 表保存检索片段及 command_id；其中 payload.text 是实际 embedding 输入。`vectors.npy` 保存对应向量；manifest 记录模型签名、语料摘要、命令数、片段数和来源。每份索引复制许可证。

- `GET /api/health`：索引状态、命令数、片段数和向量状态。
- `POST /api/search`：输入 query 和可选 top_k；结果的 text/html 是展示卡片，matched_text 是召回片段，command_id 是稳定命令标识。
- Markdown 禁用原始 HTML 和危险链接。系统不执行文档中的命令。

## 开发验证

```bash
uv run pytest -q
uv run ruff check linuxrag tests
```

单元测试使用临时目录和模拟 embedding，不调用真实模型。`eval/cases.json` 是旧范围的评测题；其中超出本次 50 个命令的题不用于判断本轮覆盖率。真实混合检索效果留待完成向量化后验收。

来源及改写说明见 [第三方声明](THIRD_PARTY_NOTICES.md)。
