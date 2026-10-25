# 第三方语料声明

Linux 基础命令部分基于 [jaywcjlove/linux-command](https://github.com/jaywcjlove/linux-command) 的 200 份 Markdown 原文整理，固定提交为 `cd17682d612e6fdfaff29261c11ffbc3f951f41d`。

原文保存在 `knowledge/raw/linux-command/`，原始 MIT 许可全文位于 `knowledge/licenses/linux-command.txt`。保留上游作者和贡献者署名。

处理方式：逐条选取常用参数、纠正说明、改写中文简介和例子，生成独立展示卡片；另写任务表达、参数行为与边界用于检索。改写内容不代表上游原文或上游作者背书。来源链接固定到提交；manifest 逐条记录来源和适用实现。

本轮不包含 tldr-pages 语料。公开分发原文、卡片、检索文本或索引时，请一并保留原始许可证、来源、署名和此处理说明。

## Git、Docker 与 Docker Compose 官方资料

新增 63 张工具与子命令卡片，依据以下固定版本官方文档，用中文重写说明、常用参数、例子和检索表达。原文仅用于溯源，不直接参与检索：

| 来源 | 固定提交 | 原文目录 | 许可与署名 |
| --- | --- | --- | --- |
| [git/git](https://github.com/git/git) | `7e34d8174dcda3435d1404c9a30bef46afe6c13e` | `knowledge/raw/git/` | GPL v2；Git contributors；许可见 `knowledge/licenses/git.txt` |
| [docker/cli](https://github.com/docker/cli) | `6d274590f2f63276a54da8adf475a455d21c1fdd` | `knowledge/raw/docker-cli/` | Apache 2.0；Docker CLI contributors；许可见 `knowledge/licenses/docker-cli.txt` |
| [docker/compose](https://github.com/docker/compose) | `e18ab3d8797716b565e47b32f0ddb60e052fbbb6` | `knowledge/raw/docker-compose/` | Apache 2.0；Docker Compose contributors；许可见 `knowledge/licenses/docker-compose.txt` |

每张卡片对应的原文路径、固定提交链接和摘要均记录在 `manifest.json` 中。原文中的版权声明与 NOTICE 如有则一并保留；整理内容不代表上游作者背书，不将这些来源统一声明为 MIT。分发相关语料及索引时，请同时保留对应来源、署名、许可和处理说明。

## 常用软件工具官方资料

本批新增 32 张卡片，中文内容为用途、选项、任务示例和检索表达的整理与改写。每条对应的固定来源文件和 SHA-256 记录在 manifest；完整版本记录在 sources.lock.json。kubectl 和 Helm 使用含官方帮助文本与参数定义的命令源码，其他工具使用官方文档或指南。原文保持其原始格式，仅供溯源。

| 来源 | 许可 | 固定提交 |
| --- | --- | --- |
| [jq](https://github.com/jqlang/jq) | CC-BY-3.0 | `ac35c7dcbb991fa0f3c3196dd00ca479211e9847` |
| [ripgrep](https://github.com/BurntSushi/ripgrep) | MIT | `6892bc2b7efe5909cbbeec8f757ed2c4c76b1d30` |
| [python](https://github.com/python/cpython) | PSF-2.0 | `ffe13151c0d441884e406507cdc64d22e047fd7d` |
| [pip](https://github.com/pypa/pip) | MIT | `0d09686649a97c2dd304322b191e44eb06ab4d44` |
| [npm](https://github.com/npm/cli) | Artistic-2.0 | `311ff5effbb1f96181c89a1ce6ebfe0c369e1ec1` |
| [uv](https://github.com/astral-sh/uv) | MIT | `6fe4f0f5cfa8322e97af4479cbfb3d53a3ce9596` |
| [kubectl](https://github.com/kubernetes/kubectl) | Apache-2.0 | `a161d6d394d58d485466a0d70d0dfcd870ae058b` |
| [helm](https://github.com/helm/helm) | Apache-2.0 | `2fe5d209e61162bd4b268ba0319c0782b9f49ca1` |

原文位于 `knowledge/raw/<来源>/`，许可位于 `knowledge/licenses/<来源>.txt`。保留上游作者和文件内的版权声明；jq 的 COPYING 另存为 `jq.NOTICE.txt`，其中明确区分程序 MIT 许可与 docs/ 文档 CC BY 3.0 许可，并附许可 URI。Python 的完整 LICENSE 包含历史许可及文档示例的许可说明。ripgrep 与 uv 按上游提供的 MIT 许可选项保存。

分发相关内容及索引时，应保留相应来源、署名、许可与改写说明；不将所有来源统一声明为 MIT，整理内容不代表上游作者背书。
