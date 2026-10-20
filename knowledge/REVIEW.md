# 知识库审核入口

第一批 50 个常用命令，当前待你审核，尚未向量化。

- 展示层：一句话说明、常用参数、2–4 个不同场景的常用例子。
- 检索层：用途、自然语言查询、参数行为、示例以及易混淆边界；按章节形成多个检索片段，每个片段始终绑定一个命令。
- `raw/`：保留的上游 Markdown 原文，仅供溯源，不自动送入 embedding。
- `manifest.json`：范围、实现、源文件与固定版本。原文许可位于 `licenses/`。

参数只覆盖常用部分，不承诺穷举。文档已逐项编辑，但当前没有在 Linux 上逐条执行例子；请优先检查说明和检索任务是否符合预期。示例中的路径、用户、PID 和主机可能需要替换。

重点：`ls -l` 与 `-1`、`tail -f` 与 `-F`、`grep -F`、`scp -P` 与 `-p`；`cd` 的路径操作数、`systemctl` 和 `ip` 的子命令已注明。

| 命令 | 展示卡片 | 检索文本 | 上游原文 |
| --- | --- | --- | --- |
| `ls` | [卡片](cards/ls.md) | [检索](retrieval/ls.md) | [原文](raw/linux-command/ls.md) |
| `pwd` | [卡片](cards/pwd.md) | [检索](retrieval/pwd.md) | [原文](raw/linux-command/pwd.md) |
| `cd` | [卡片](cards/cd.md) | [检索](retrieval/cd.md) | [原文](raw/linux-command/cd.md) |
| `mkdir` | [卡片](cards/mkdir.md) | [检索](retrieval/mkdir.md) | [原文](raw/linux-command/mkdir.md) |
| `rmdir` | [卡片](cards/rmdir.md) | [检索](retrieval/rmdir.md) | [原文](raw/linux-command/rmdir.md) |
| `touch` | [卡片](cards/touch.md) | [检索](retrieval/touch.md) | [原文](raw/linux-command/touch.md) |
| `cp` | [卡片](cards/cp.md) | [检索](retrieval/cp.md) | [原文](raw/linux-command/cp.md) |
| `mv` | [卡片](cards/mv.md) | [检索](retrieval/mv.md) | [原文](raw/linux-command/mv.md) |
| `rm` | [卡片](cards/rm.md) | [检索](retrieval/rm.md) | [原文](raw/linux-command/rm.md) |
| `ln` | [卡片](cards/ln.md) | [检索](retrieval/ln.md) | [原文](raw/linux-command/ln.md) |
| `cat` | [卡片](cards/cat.md) | [检索](retrieval/cat.md) | [原文](raw/linux-command/cat.md) |
| `less` | [卡片](cards/less.md) | [检索](retrieval/less.md) | [原文](raw/linux-command/less.md) |
| `head` | [卡片](cards/head.md) | [检索](retrieval/head.md) | [原文](raw/linux-command/head.md) |
| `tail` | [卡片](cards/tail.md) | [检索](retrieval/tail.md) | [原文](raw/linux-command/tail.md) |
| `wc` | [卡片](cards/wc.md) | [检索](retrieval/wc.md) | [原文](raw/linux-command/wc.md) |
| `sort` | [卡片](cards/sort.md) | [检索](retrieval/sort.md) | [原文](raw/linux-command/sort.md) |
| `uniq` | [卡片](cards/uniq.md) | [检索](retrieval/uniq.md) | [原文](raw/linux-command/uniq.md) |
| `cut` | [卡片](cards/cut.md) | [检索](retrieval/cut.md) | [原文](raw/linux-command/cut.md) |
| `grep` | [卡片](cards/grep.md) | [检索](retrieval/grep.md) | [原文](raw/linux-command/grep.md) |
| `find` | [卡片](cards/find.md) | [检索](retrieval/find.md) | [原文](raw/linux-command/find.md) |
| `xargs` | [卡片](cards/xargs.md) | [检索](retrieval/xargs.md) | [原文](raw/linux-command/xargs.md) |
| `sed` | [卡片](cards/sed.md) | [检索](retrieval/sed.md) | [原文](raw/linux-command/sed.md) |
| `awk` | [卡片](cards/awk.md) | [检索](retrieval/awk.md) | [原文](raw/linux-command/awk.md) |
| `tar` | [卡片](cards/tar.md) | [检索](retrieval/tar.md) | [原文](raw/linux-command/tar.md) |
| `zip` | [卡片](cards/zip.md) | [检索](retrieval/zip.md) | [原文](raw/linux-command/zip.md) |
| `unzip` | [卡片](cards/unzip.md) | [检索](retrieval/unzip.md) | [原文](raw/linux-command/unzip.md) |
| `df` | [卡片](cards/df.md) | [检索](retrieval/df.md) | [原文](raw/linux-command/df.md) |
| `du` | [卡片](cards/du.md) | [检索](retrieval/du.md) | [原文](raw/linux-command/du.md) |
| `free` | [卡片](cards/free.md) | [检索](retrieval/free.md) | [原文](raw/linux-command/free.md) |
| `ps` | [卡片](cards/ps.md) | [检索](retrieval/ps.md) | [原文](raw/linux-command/ps.md) |
| `top` | [卡片](cards/top.md) | [检索](retrieval/top.md) | [原文](raw/linux-command/top.md) |
| `kill` | [卡片](cards/kill.md) | [检索](retrieval/kill.md) | [原文](raw/linux-command/kill.md) |
| `pgrep` | [卡片](cards/pgrep.md) | [检索](retrieval/pgrep.md) | [原文](raw/linux-command/pgrep.md) |
| `chmod` | [卡片](cards/chmod.md) | [检索](retrieval/chmod.md) | [原文](raw/linux-command/chmod.md) |
| `chown` | [卡片](cards/chown.md) | [检索](retrieval/chown.md) | [原文](raw/linux-command/chown.md) |
| `id` | [卡片](cards/id.md) | [检索](retrieval/id.md) | [原文](raw/linux-command/id.md) |
| `whoami` | [卡片](cards/whoami.md) | [检索](retrieval/whoami.md) | [原文](raw/linux-command/whoami.md) |
| `uname` | [卡片](cards/uname.md) | [检索](retrieval/uname.md) | [原文](raw/linux-command/uname.md) |
| `date` | [卡片](cards/date.md) | [检索](retrieval/date.md) | [原文](raw/linux-command/date.md) |
| `env` | [卡片](cards/env.md) | [检索](retrieval/env.md) | [原文](raw/linux-command/env.md) |
| `which` | [卡片](cards/which.md) | [检索](retrieval/which.md) | [原文](raw/linux-command/which.md) |
| `ssh` | [卡片](cards/ssh.md) | [检索](retrieval/ssh.md) | [原文](raw/linux-command/ssh.md) |
| `scp` | [卡片](cards/scp.md) | [检索](retrieval/scp.md) | [原文](raw/linux-command/scp.md) |
| `curl` | [卡片](cards/curl.md) | [检索](retrieval/curl.md) | [原文](raw/linux-command/curl.md) |
| `wget` | [卡片](cards/wget.md) | [检索](retrieval/wget.md) | [原文](raw/linux-command/wget.md) |
| `ss` | [卡片](cards/ss.md) | [检索](retrieval/ss.md) | [原文](raw/linux-command/ss.md) |
| `systemctl` | [卡片](cards/systemctl.md) | [检索](retrieval/systemctl.md) | [原文](raw/linux-command/systemctl.md) |
| `lsof` | [卡片](cards/lsof.md) | [检索](retrieval/lsof.md) | [原文](raw/linux-command/lsof.md) |
| `ip` | [卡片](cards/ip.md) | [检索](retrieval/ip.md) | [原文](raw/linux-command/ip.md) |
| `diff` | [卡片](cards/diff.md) | [检索](retrieval/diff.md) | [原文](raw/linux-command/diff.md) |

[整理依据与校验边界](CURATION.md)
