# LinRag

一个轻量的 Linux 命令RAG搜索网站。

## 功能与亮点

- 支持自然语言快速搜索
- 支持以命令搜索
- 收录 295 个命令条目，覆盖 Linux、Git、Docker、数据处理、包管理和 Kubernetes 工具
- 简洁明了的展示卡片
- 快捷的操作方式
- 向量化语料和展示内容分离实现更精确搜索

## 在线快速体验

[访问 LinRag](https://linrag.cometapi.uno)

项目已上线，当前进度与后续安排见[项目规划](docs/ROADMAP.md)。
## 快速本地构建

需要 Python 3.11+ 和 [uv](https://docs.astral.sh/uv/)。在项目根目录执行：

```bash
uv sync --python 3.12

# 首次配置时执行；已有 .env 则跳过
cp .env.example .env
```

在 `.env` 中填写兼容 OpenAI Embeddings API 的服务配置：

```dotenv
EMBED_BASE_URL=https://your-provider.example/v1
EMBED_API_KEY=your-api-key
EMBED_MODEL=your-embedding-model
```

`EMBED_BASE_URL` 包含服务的 API 前缀，不包含 `/embeddings`。其他可选配置见 [.env.example](.env.example)。

先参考[知识库审核入口](knowledge/REVIEW.md)检查语料，再校验、构建索引并启动服务：

```bash
uv run linrag validate
uv run linrag build
uv run linrag serve
```

打开 <http://127.0.0.1:8000>

构建向量索引及语义查询会调用配置的模型服务。若只需关键词检索，可使用 `uv run linrag build --lexical-only`，无需配置 Embedding 服务。

## 知识库维护

| 路径 | 用途 |
| --- | --- |
| `knowledge/cards/` | 页面展示的命令卡片 |
| `knowledge/retrieval/` | 用于检索和向量化的文本 |
| `knowledge/raw/` | 上游原文，仅供溯源 |
| `knowledge/manifest.json` | 命令信息与来源映射 |
| `knowledge/sources.lock.json` | 固定的上游版本 |

修改内容时同步更新展示层和检索层，新增命令时更新 manifest，然后运行 `validate`。语料或 Embedding 配置变更后，需要重新构建索引并重启服务。索引保存在 `data/`，不纳入版本控制。

整理规则与校验边界见 [CURATION.md](knowledge/CURATION.md)。

## 开发

后端使用 FastAPI，前端使用原生 HTML、CSS 、JS。

```bash
uv run pytest -q
uv run ruff check linrag tests
```

单元测试使用模拟 Embedding，不调用真实模型。建立索引后，可运行检索测试：

```bash
uv run linrag evaluate
```

测试用例位于 `eval/cases.json`，报告默认写入 `data/evaluation.json`；混合检索测试会调用配置的 Embedding 服务。

## 来源

项目源码：[Comet966/LinRag](https://github.com/Comet966/LinRag)。

Linux 基础命令基于 [linux-command](https://github.com/jaywcjlove/linux-command)（MIT）整理；Git、Docker、jq、ripgrep、Python/pip、npm、uv、kubectl 和 Helm 条目依据官方文档或命令源码整理，原文和许可随知识库保存。来源、固定版本和改写说明见[第三方声明](THIRD_PARTY_NOTICES.md)。
