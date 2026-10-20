# 命令知识库 Markdown 数据源调研

## 结论

找到较接近目标排版的新来源 `liuzi6612/linux-manual`，但没有确认一个能不经整理就同时满足中文、简短说明、独立参数说明、末尾例子、全面覆盖且质量稳定的现成库。

建议先整理已有 linux-command 为命令卡片，用 linux-manual 补充结构参考，tldr 提供少量常用示例。入库单位是完整命令，不再把章节直接当成用户看到的结果。当前阶段只生成 5 份格式样本，不修改语料下载配置、服务、现有 SQLite 或向量索引。

## 候选来源

| 来源 | 原始格式和结构 | 适用性 |
| --- | --- | --- |
| [linux-manual](https://github.com/liuzi6612/linux-manual) | 单一 README.md；仓库自述 112 个条目；许多命令按说明、参数表、示例组织；仓库标注 MIT | 新找到的最接近目标的来源，但需按命令拆分、删减冗余、核查错误和平台差异 |
| [linux-command](https://github.com/jaywcjlove/linux-command) | command/*.md；每命令一文件；MIT | 适合作为主要候选原料，覆盖较广，但需去重、精简并纠错 |
| [tldr-pages](https://github.com/tldr-pages/tldr) | 每命令一个 Markdown；简述和多个例子；页面 CC BY 4.0 | 适合补充例子，不提供独立、完整的参数字典，不适合单独满足目标结构 |

旧地址 `xjh22222228/linux-manual` 当前重定向到 `liuzi6612/linux-manual`。linux-manual 的 LICENSE 单独页面本次未成功取得；许可标注来自仓库主页，正式接入时还需固定提交并保存许可全文。

## 本地语料检查

固定 linux-command 提交：`cd17682d612e6fdfaff29261c11ffbc3f951f41d`。

本地统计 621 份命令 Markdown，其中 573 份出现“选项/参数”标题、485 份出现“实例/示例/例子”标题。这是标题级统计，不代表内容已通过审核。ls 原文 429 行，grep 256 行，tar 549 行，find 738 行，pwd 95 行；直接展示全文不能满足简洁目标。

当前按章节切分并展示的方式，还会让一个命令在结果中出现多次。更换数据源并不能单独解决这个问题。

## 抽查发现

- linux-manual 的 rmdir 条目写有 `-i`，GNU rmdir 手册未提供该选项；不要照搬。参考：https://man7.org/linux/man-pages/man1/rmdir.1.html
- 本地 linux-command 的 grep 参数表含 `--revert-match` 和 `--fixed-regexp`；规范拼写应为 `--invert-match`、`--fixed-strings`。参考：https://man7.org/linux/man-pages/man1/grep.1.html
- 本地 tail 文档含 `--line`、`--sleep-interal` 等拼写，应核对为 `--lines`、`--sleep-interval`。参考：https://man7.org/linux/man-pages/man1/tail.1.html
- `ls -l` 是详细列表，`ls -1` 才是每行一个文件名。参考：https://man7.org/linux/man-pages/man1/ls.1.html
- pwd 的 shell 内建与 GNU 外部实现不能把默认行为混成一个结论；样本保留明确的 -L、-P 行为，来源元数据标注实现范围。

## 建议的整理规则

1. 保留下载的原始 Markdown；派生卡片与原文分目录存放，保留来源提交与许可。
2. 一命令一文件，一句话说明，参数按短选项/长选项及所需值逐项解释，末尾只放一个代表性例子。
3. 默认做常用参数卡片，避免把长手册完整搬过来；不把多个组合选项误拆为无依据的单项解释。
4. 自动抽取只处理明确结构；缺失或歧义条目标记待审核，不补造参数和例子，不直接取前 N 行充当摘要。
5. 依据 GNU/Linux 的具体实现核对内容。上游手册是事实校验依据，不替代用户要求的 Markdown 原始数据。
6. 同一命令不同来源先合并校验后形成一张卡片；真正不同的实现分别标注。子命令可单独建卡，但不得误并入根命令。
7. 新库建立后，结果按命令去重，返回完整卡片。向量需基于新文本重新生成，但本阶段没有触发任何 embedding 调用。

## 当前交付

初期五份样本已由首批 50 个命令替代。当前审核入口为 `knowledge/REVIEW.md`，展示卡片位于 `knowledge/cards/`，检索文档位于 `knowledge/retrieval/`；本页其余内容保留为数据源选择记录。
