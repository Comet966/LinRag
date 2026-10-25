# 知识库审核目录

当前收录 **295 个命令**。本目录依据 `manifest.json` 与实际 Markdown 文件整理，按命令名排序。其中 Linux 基础命令 200 个，Git 28 个，Docker 25 个，Docker Compose 10 个，以及 jq、ripgrep、Python/pip、npm、uv、kubectl、Helm 共 32 个条目；子命令分别建卡。

- **展示卡片**：命令用途、常用参数和 2–4 个使用示例。
- **检索文本**：任务表达、参数行为、示例和适用边界，用于关键词检索与向量化。
- **上游原文**：固定版本的来源文档，仅供追溯，不参与索引。

## 审核说明

检查用途、参数和示例是否准确，展示卡片与检索文本是否一致，并注意不同实现和发行版的差异。示例中的路径、用户、PID 和主机需要按实际环境替换；文档不代表已经在 Linux 上逐条执行验证。

修改内容后运行 `uv run linrag validate` 检查语料结构、文件映射与来源摘要。该命令不调用模型，也不验证命令的实际运行效果。

整理依据与校验边界见 [CURATION.md](CURATION.md)，来源版本见 [sources.lock.json](sources.lock.json)。审核状态以 `manifest.json` 中的 `review` 字段为准，目前全部为 `pending_user_review`。

## 命令目录

| 命令 | 用途 | 适用实现 | 展示卡片 | 检索文本 | 上游原文 |
| --- | --- | --- | --- | --- | --- |
| `7z` | 高压缩比归档工具，支持多种格式。 | p7zip | [卡片](cards/7z.md) | [检索](retrieval/7z.md) | [原文](raw/linux-command/7z.md) |
| `apt-get` | Debian/Ubuntu 包管理工具。 | APT | [卡片](cards/apt-get.md) | [检索](retrieval/apt-get.md) | [原文](raw/linux-command/apt-get.md) |
| `ar` | 创建、查看或展开静态库归档。 | binutils | [卡片](cards/ar.md) | [检索](retrieval/ar.md) | [原文](raw/linux-command/ar.md) |
| `arch` | 显示当前主机的硬件架构名称。 | GNU coreutils | [卡片](cards/arch.md) | [检索](retrieval/arch.md) | [原文](raw/linux-command/arch.md) |
| `arp` | 查看和修改内核的 ARP 缓存表。 | net-tools | [卡片](cards/arp.md) | [检索](retrieval/arp.md) | [原文](raw/linux-command/arp.md) |
| `at` | 在指定时间执行一次性任务。 | at | [卡片](cards/at.md) | [检索](retrieval/at.md) | [原文](raw/linux-command/at.md) |
| `atq` | 列出当前用户待执行的 at 任务。 | at | [卡片](cards/atq.md) | [检索](retrieval/atq.md) | [原文](raw/linux-command/atq.md) |
| `atrm` | 删除排队中的 at 任务。 | at | [卡片](cards/atrm.md) | [检索](retrieval/atrm.md) | [原文](raw/linux-command/atrm.md) |
| `awk` | 按记录和字段处理文本，适合筛选、计算和报表。 | POSIX awk subset | [卡片](cards/awk.md) | [检索](retrieval/awk.md) | [原文](raw/linux-command/awk.md) |
| `axel` | 多线程分段下载，支持断点续传。 | axel | [卡片](cards/axel.md) | [检索](retrieval/axel.md) | [原文](raw/linux-command/axel.md) |
| `basename` | 取路径中的文件名。 | GNU coreutils | [卡片](cards/basename.md) | [检索](retrieval/basename.md) | [原文](raw/linux-command/basename.md) |
| `batch` | 系统空闲时执行一次性任务。 | at | [卡片](cards/batch.md) | [检索](retrieval/batch.md) | [原文](raw/linux-command/batch.md) |
| `bg` | Bash 内建，把暂停的作业放回后台。 | Bash 内建 | [卡片](cards/bg.md) | [检索](retrieval/bg.md) | [原文](raw/linux-command/bg.md) |
| `blkid` | 查看块设备的 UUID 和类型。 | util-linux | [卡片](cards/blkid.md) | [检索](retrieval/blkid.md) | [原文](raw/linux-command/blkid.md) |
| `bzip2` | 压缩成 bz2 格式的归档文件。 | bzip2 | [卡片](cards/bzip2.md) | [检索](retrieval/bzip2.md) | [原文](raw/linux-command/bzip2.md) |
| `cal` | 显示月历或年历，默认本月。 | util-linux | [卡片](cards/cal.md) | [检索](retrieval/cal.md) | [原文](raw/linux-command/cal.md) |
| `cat` | 连接文件并把内容输出到标准输出。 | GNU coreutils | [卡片](cards/cat.md) | [检索](retrieval/cat.md) | [原文](raw/linux-command/cat.md) |
| `cd` | 切换当前 shell 的工作目录。 | Bash builtin | [卡片](cards/cd.md) | [检索](retrieval/cd.md) | [原文](raw/linux-command/cd.md) |
| `chage` | 查看和修改账号密码有效期。 | shadow-utils | [卡片](cards/chage.md) | [检索](retrieval/chage.md) | [原文](raw/linux-command/chage.md) |
| `chattr` | 修改 ext 系文件系统的属性位。 | e2fsprogs | [卡片](cards/chattr.md) | [检索](retrieval/chattr.md) | [原文](raw/linux-command/chattr.md) |
| `chgrp` | 修改文件或目录的所属用户组。 | GNU coreutils | [卡片](cards/chgrp.md) | [检索](retrieval/chgrp.md) | [原文](raw/linux-command/chgrp.md) |
| `chmod` | 修改文件或目录的访问权限。 | GNU coreutils | [卡片](cards/chmod.md) | [检索](retrieval/chmod.md) | [原文](raw/linux-command/chmod.md) |
| `chown` | 修改文件或目录的所有者及所属组。 | GNU coreutils | [卡片](cards/chown.md) | [检索](retrieval/chown.md) | [原文](raw/linux-command/chown.md) |
| `chsh` | 更改用户登录时使用的 shell。 | shadow-utils | [卡片](cards/chsh.md) | [检索](retrieval/chsh.md) | [原文](raw/linux-command/chsh.md) |
| `cmp` | 逐字节比较，报首个差异位置。 | GNU diffutils | [卡片](cards/cmp.md) | [检索](retrieval/cmp.md) | [原文](raw/linux-command/cmp.md) |
| `cp` | 复制文件或目录。 | GNU coreutils | [卡片](cards/cp.md) | [检索](retrieval/cp.md) | [原文](raw/linux-command/cp.md) |
| `cpio` | 建立或还原归档包，可与 find 配合。 | GNU cpio | [卡片](cards/cpio.md) | [检索](retrieval/cpio.md) | [原文](raw/linux-command/cpio.md) |
| `crontab` | 管理定时任务，字段为分时日月周。 | cronie / Vixie cron | [卡片](cards/crontab.md) | [检索](retrieval/crontab.md) | [原文](raw/linux-command/crontab.md) |
| `csplit` | 按内容匹配把大文件切成多份。 | GNU coreutils | [卡片](cards/csplit.md) | [检索](retrieval/csplit.md) | [原文](raw/linux-command/csplit.md) |
| `curl` | 通过 URL 传输数据，常用于 HTTP 请求和下载。 | curl | [卡片](cards/curl.md) | [检索](retrieval/curl.md) | [原文](raw/linux-command/curl.md) |
| `cut` | 按字段、字节或字符位置提取每行内容。 | GNU coreutils | [卡片](cards/cut.md) | [检索](retrieval/cut.md) | [原文](raw/linux-command/cut.md) |
| `date` | 显示或设置系统日期和时间。 | GNU coreutils | [卡片](cards/date.md) | [检索](retrieval/date.md) | [原文](raw/linux-command/date.md) |
| `dd` | 按块复制文件或设备，写错会覆盖数据。 | GNU coreutils | [卡片](cards/dd.md) | [检索](retrieval/dd.md) | [原文](raw/linux-command/dd.md) |
| `df` | 显示文件系统的容量和可用空间。 | GNU coreutils | [卡片](cards/df.md) | [检索](retrieval/df.md) | [原文](raw/linux-command/df.md) |
| `diff` | 逐行比较文本文件并显示差异。 | GNU diffutils | [卡片](cards/diff.md) | [检索](retrieval/diff.md) | [原文](raw/linux-command/diff.md) |
| `dig` | 查询 DNS 记录并显示解析报文。 | BIND utils | [卡片](cards/dig.md) | [检索](retrieval/dig.md) | [原文](raw/linux-command/dig.md) |
| `dirname` | 取路径中的目录部分。 | GNU coreutils | [卡片](cards/dirname.md) | [检索](retrieval/dirname.md) | [原文](raw/linux-command/dirname.md) |
| `dmesg` | 读取内核环形缓冲区消息。 | util-linux | [卡片](cards/dmesg.md) | [检索](retrieval/dmesg.md) | [原文](raw/linux-command/dmesg.md) |
| `dnf` | Fedora、RHEL 8+ 的包管理器。 | DNF | [卡片](cards/dnf.md) | [检索](retrieval/dnf.md) | [原文](raw/linux-command/dnf.md) |
| `docker` | 管理镜像、容器、网络和数据卷的命令行工具。 | Docker CLI / Docker Engine | [卡片](cards/docker.md) | [检索](retrieval/docker.md) | [原文](raw/docker-cli/docker.md) |
| `docker build` | 根据 Dockerfile 和构建上下文构建镜像。 | Docker CLI / Docker Engine | [卡片](cards/docker-build.md) | [检索](retrieval/docker-build.md) | [原文](raw/docker-cli/docker-build.md) |
| `docker compose` | 使用 Compose 文件管理多容器应用。 | Docker Compose 插件（docker compose） | [卡片](cards/docker-compose.md) | [检索](retrieval/docker-compose.md) | [原文](raw/docker-compose/docker-compose.md) |
| `docker compose build` | 根据 Compose 配置构建服务镜像。 | Docker Compose 插件（docker compose） | [卡片](cards/docker-compose-build.md) | [检索](retrieval/docker-compose-build.md) | [原文](raw/docker-compose/docker-compose-build.md) |
| `docker compose config` | 解析、合并和校验 Compose 配置。 | Docker Compose 插件（docker compose） | [卡片](cards/docker-compose-config.md) | [检索](retrieval/docker-compose-config.md) | [原文](raw/docker-compose/docker-compose-config.md) |
| `docker compose down` | 停止并删除 Compose 项目的服务容器与网络。 | Docker Compose 插件（docker compose） | [卡片](cards/docker-compose-down.md) | [检索](retrieval/docker-compose-down.md) | [原文](raw/docker-compose/docker-compose-down.md) |
| `docker compose exec` | 在已运行的 Compose 服务容器中执行命令。 | Docker Compose 插件（docker compose） | [卡片](cards/docker-compose-exec.md) | [检索](retrieval/docker-compose-exec.md) | [原文](raw/docker-compose/docker-compose-exec.md) |
| `docker compose logs` | 查看 Compose 服务的日志输出。 | Docker Compose 插件（docker compose） | [卡片](cards/docker-compose-logs.md) | [检索](retrieval/docker-compose-logs.md) | [原文](raw/docker-compose/docker-compose-logs.md) |
| `docker compose ps` | 查看 Compose 项目的服务容器状态。 | Docker Compose 插件（docker compose） | [卡片](cards/docker-compose-ps.md) | [检索](retrieval/docker-compose-ps.md) | [原文](raw/docker-compose/docker-compose-ps.md) |
| `docker compose pull` | 拉取 Compose 服务引用的镜像。 | Docker Compose 插件（docker compose） | [卡片](cards/docker-compose-pull.md) | [检索](retrieval/docker-compose-pull.md) | [原文](raw/docker-compose/docker-compose-pull.md) |
| `docker compose run` | 为某个 Compose 服务创建一次性任务容器。 | Docker Compose 插件（docker compose） | [卡片](cards/docker-compose-run.md) | [检索](retrieval/docker-compose-run.md) | [原文](raw/docker-compose/docker-compose-run.md) |
| `docker compose up` | 创建并启动 Compose 应用的服务容器。 | Docker Compose 插件（docker compose） | [卡片](cards/docker-compose-up.md) | [检索](retrieval/docker-compose-up.md) | [原文](raw/docker-compose/docker-compose-up.md) |
| `docker cp` | 在容器与宿主机之间复制文件或目录。 | Docker CLI / Docker Engine | [卡片](cards/docker-cp.md) | [检索](retrieval/docker-cp.md) | [原文](raw/docker-cli/docker-cp.md) |
| `docker exec` | 在已经运行的容器中执行新进程。 | Docker CLI / Docker Engine | [卡片](cards/docker-exec.md) | [检索](retrieval/docker-exec.md) | [原文](raw/docker-cli/docker-exec.md) |
| `docker images` | 列出本地镜像及其标签和大小。 | Docker CLI / Docker Engine | [卡片](cards/docker-images.md) | [检索](retrieval/docker-images.md) | [原文](raw/docker-cli/docker-images.md) |
| `docker info` | 查看 Docker Engine 的系统配置和资源信息。 | Docker CLI / Docker Engine | [卡片](cards/docker-info.md) | [检索](retrieval/docker-info.md) | [原文](raw/docker-cli/docker-info.md) |
| `docker inspect` | 读取容器或其他 Docker 对象的详细配置。 | Docker CLI / Docker Engine | [卡片](cards/docker-inspect.md) | [检索](retrieval/docker-inspect.md) | [原文](raw/docker-cli/docker-inspect.md) |
| `docker login` | 登录镜像仓库并保存认证信息。 | Docker CLI / Docker Engine | [卡片](cards/docker-login.md) | [检索](retrieval/docker-login.md) | [原文](raw/docker-cli/docker-login.md) |
| `docker logout` | 移除 Docker 保存的指定镜像仓库登录信息。 | Docker CLI / Docker Engine | [卡片](cards/docker-logout.md) | [检索](retrieval/docker-logout.md) | [原文](raw/docker-cli/docker-logout.md) |
| `docker logs` | 读取容器标准输出与标准错误的日志。 | Docker CLI / Docker Engine | [卡片](cards/docker-logs.md) | [检索](retrieval/docker-logs.md) | [原文](raw/docker-cli/docker-logs.md) |
| `docker network ls` | 列出 Docker 网络。 | Docker CLI / Docker Engine | [卡片](cards/docker-network-ls.md) | [检索](retrieval/docker-network-ls.md) | [原文](raw/docker-cli/docker-network-ls.md) |
| `docker ps` | 列出容器及运行状态。 | Docker CLI / Docker Engine | [卡片](cards/docker-ps.md) | [检索](retrieval/docker-ps.md) | [原文](raw/docker-cli/docker-ps.md) |
| `docker pull` | 从镜像仓库拉取镜像到本地。 | Docker CLI / Docker Engine | [卡片](cards/docker-pull.md) | [检索](retrieval/docker-pull.md) | [原文](raw/docker-cli/docker-pull.md) |
| `docker push` | 将本地镜像上传到目标镜像仓库。 | Docker CLI / Docker Engine | [卡片](cards/docker-push.md) | [检索](retrieval/docker-push.md) | [原文](raw/docker-cli/docker-push.md) |
| `docker restart` | 停止并重新启动已有容器。 | Docker CLI / Docker Engine | [卡片](cards/docker-restart.md) | [检索](retrieval/docker-restart.md) | [原文](raw/docker-cli/docker-restart.md) |
| `docker rm` | 删除已有容器及其可写层。 | Docker CLI / Docker Engine | [卡片](cards/docker-rm.md) | [检索](retrieval/docker-rm.md) | [原文](raw/docker-cli/docker-rm.md) |
| `docker rmi` | 删除本地镜像或取消镜像标签。 | Docker CLI / Docker Engine | [卡片](cards/docker-rmi.md) | [检索](retrieval/docker-rmi.md) | [原文](raw/docker-cli/docker-rmi.md) |
| `docker run` | 从镜像创建并启动一个新容器。 | Docker CLI / Docker Engine | [卡片](cards/docker-run.md) | [检索](retrieval/docker-run.md) | [原文](raw/docker-cli/docker-run.md) |
| `docker start` | 启动已经存在但停止的容器。 | Docker CLI / Docker Engine | [卡片](cards/docker-start.md) | [检索](retrieval/docker-start.md) | [原文](raw/docker-cli/docker-start.md) |
| `docker stats` | 查看容器的 CPU、内存和网络资源统计。 | Docker CLI / Docker Engine | [卡片](cards/docker-stats.md) | [检索](retrieval/docker-stats.md) | [原文](raw/docker-cli/docker-stats.md) |
| `docker stop` | 请求运行中的容器停止并等待退出。 | Docker CLI / Docker Engine | [卡片](cards/docker-stop.md) | [检索](retrieval/docker-stop.md) | [原文](raw/docker-cli/docker-stop.md) |
| `docker system df` | 查看 Docker 对象的磁盘占用及可回收空间。 | Docker CLI / Docker Engine | [卡片](cards/docker-system-df.md) | [检索](retrieval/docker-system-df.md) | [原文](raw/docker-cli/docker-system-df.md) |
| `docker tag` | 为已有镜像增加一个本地名称或标签。 | Docker CLI / Docker Engine | [卡片](cards/docker-tag.md) | [检索](retrieval/docker-tag.md) | [原文](raw/docker-cli/docker-tag.md) |
| `docker version` | 显示 Docker 客户端和服务端版本。 | Docker CLI / Docker Engine | [卡片](cards/docker-version.md) | [检索](retrieval/docker-version.md) | [原文](raw/docker-cli/docker-version.md) |
| `docker volume ls` | 列出 Docker 管理的数据卷。 | Docker CLI / Docker Engine | [卡片](cards/docker-volume-ls.md) | [检索](retrieval/docker-volume-ls.md) | [原文](raw/docker-cli/docker-volume-ls.md) |
| `dpkg` | 操作本地 deb 包和包数据库。 | dpkg | [卡片](cards/dpkg.md) | [检索](retrieval/dpkg.md) | [原文](raw/linux-command/dpkg.md) |
| `du` | 估算文件和目录占用的磁盘空间。 | GNU coreutils | [卡片](cards/du.md) | [检索](retrieval/du.md) | [原文](raw/linux-command/du.md) |
| `echo` | 输出字符串或变量值。 | Bash 内建 / GNU coreutils | [卡片](cards/echo.md) | [检索](retrieval/echo.md) | [原文](raw/linux-command/echo.md) |
| `env` | 显示环境变量，或在指定环境中运行命令。 | GNU coreutils | [卡片](cards/env.md) | [检索](retrieval/env.md) | [原文](raw/linux-command/env.md) |
| `ethtool` | 查看和设置网卡链路与卸载参数。 | ethtool | [卡片](cards/ethtool.md) | [检索](retrieval/ethtool.md) | [原文](raw/linux-command/ethtool.md) |
| `fdisk` | 查看和修改分区表，写盘可能丢数据。 | util-linux | [卡片](cards/fdisk.md) | [检索](retrieval/fdisk.md) | [原文](raw/linux-command/fdisk.md) |
| `fg` | Bash 内建，把作业切到前台运行。 | Bash 内建 | [卡片](cards/fg.md) | [检索](retrieval/fg.md) | [原文](raw/linux-command/fg.md) |
| `file` | 判断文件类型。 | file | [卡片](cards/file.md) | [检索](retrieval/file.md) | [原文](raw/linux-command/file.md) |
| `find` | 按名称、类型、时间等条件递归查找文件。 | GNU findutils | [卡片](cards/find.md) | [检索](retrieval/find.md) | [原文](raw/linux-command/find.md) |
| `fmt` | 把文本段落重排到指定列宽。 | GNU coreutils | [卡片](cards/fmt.md) | [检索](retrieval/fmt.md) | [原文](raw/linux-command/fmt.md) |
| `fold` | 按指定宽度把每行折成多行。 | GNU coreutils | [卡片](cards/fold.md) | [检索](retrieval/fold.md) | [原文](raw/linux-command/fold.md) |
| `free` | 显示系统内存与交换空间使用情况。 | procps-ng | [卡片](cards/free.md) | [检索](retrieval/free.md) | [原文](raw/linux-command/free.md) |
| `fsck` | 检查并修复文件系统错误。 | util-linux | [卡片](cards/fsck.md) | [检索](retrieval/fsck.md) | [原文](raw/linux-command/fsck.md) |
| `gdb` | 命令行调试器，可断点单步查值。 | GDB | [卡片](cards/gdb.md) | [检索](retrieval/gdb.md) | [原文](raw/linux-command/gdb.md) |
| `getfacl` | 查看文件和目录的访问控制列表。 | acl | [卡片](cards/getfacl.md) | [检索](retrieval/getfacl.md) | [原文](raw/linux-command/getfacl.md) |
| `git` | 分布式版本控制工具，用于管理代码历史、分支和协作。 | Git 2.23+ | [卡片](cards/git.md) | [检索](retrieval/git.md) | [原文](raw/git/git.adoc) |
| `git add` | 把文件内容或删除操作写入暂存区。 | Git 2.23+ | [卡片](cards/git-add.md) | [检索](retrieval/git-add.md) | [原文](raw/git/git-add.adoc) |
| `git blame` | 逐行显示文件内容最后修改的提交和作者。 | Git 2.23+ | [卡片](cards/git-blame.md) | [检索](retrieval/git-blame.md) | [原文](raw/git/git-blame.adoc) |
| `git branch` | 列出、创建或管理本地分支。 | Git 2.23+ | [卡片](cards/git-branch.md) | [检索](retrieval/git-branch.md) | [原文](raw/git/git-branch.adoc) |
| `git checkout` | 切换分支或从指定版本恢复文件。 | Git 2.23+ | [卡片](cards/git-checkout.md) | [检索](retrieval/git-checkout.md) | [原文](raw/git/git-checkout.adoc) |
| `git cherry-pick` | 将指定提交的改动应用为当前分支的新提交。 | Git 2.23+ | [卡片](cards/git-cherry-pick.md) | [检索](retrieval/git-cherry-pick.md) | [原文](raw/git/git-cherry-pick.adoc) |
| `git clean` | 预览或删除工作区中的未跟踪文件。 | Git 2.23+ | [卡片](cards/git-clean.md) | [检索](retrieval/git-clean.md) | [原文](raw/git/git-clean.adoc) |
| `git clone` | 克隆远程或本地仓库并建立工作副本。 | Git 2.23+ | [卡片](cards/git-clone.md) | [检索](retrieval/git-clone.md) | [原文](raw/git/git-clone.adoc) |
| `git commit` | 将暂存区内容保存为一个本地提交。 | Git 2.23+ | [卡片](cards/git-commit.md) | [检索](retrieval/git-commit.md) | [原文](raw/git/git-commit.adoc) |
| `git config` | 读取和设置 Git 配置项。 | Git | [卡片](cards/git-config.md) | [检索](retrieval/git-config.md) | [原文](raw/git/git-config.adoc) |
| `git diff` | 比较工作区、暂存区或指定提交之间的差异。 | Git 2.23+ | [卡片](cards/git-diff.md) | [检索](retrieval/git-diff.md) | [原文](raw/git/git-diff.adoc) |
| `git fetch` | 从远程下载对象并更新远程跟踪引用。 | Git 2.23+ | [卡片](cards/git-fetch.md) | [检索](retrieval/git-fetch.md) | [原文](raw/git/git-fetch.adoc) |
| `git init` | 在目录中初始化 Git 仓库。 | Git 2.23+ | [卡片](cards/git-init.md) | [检索](retrieval/git-init.md) | [原文](raw/git/git-init.adoc) |
| `git log` | 查看提交历史及各提交的改动。 | Git 2.23+ | [卡片](cards/git-log.md) | [检索](retrieval/git-log.md) | [原文](raw/git/git-log.adoc) |
| `git merge` | 把其他分支的历史合并到当前分支。 | Git 2.23+ | [卡片](cards/git-merge.md) | [检索](retrieval/git-merge.md) | [原文](raw/git/git-merge.adoc) |
| `git pull` | 获取远程更新并整合到当前分支。 | Git 2.23+ | [卡片](cards/git-pull.md) | [检索](retrieval/git-pull.md) | [原文](raw/git/git-pull.adoc) |
| `git push` | 把本地引用和提交发送到远程仓库。 | Git 2.23+ | [卡片](cards/git-push.md) | [检索](retrieval/git-push.md) | [原文](raw/git/git-push.adoc) |
| `git rebase` | 将当前分支的提交重新应用到新的基底。 | Git 2.23+ | [卡片](cards/git-rebase.md) | [检索](retrieval/git-rebase.md) | [原文](raw/git/git-rebase.adoc) |
| `git reflog` | 查看本地引用曾经指向的提交记录。 | Git 2.23+ | [卡片](cards/git-reflog.md) | [检索](retrieval/git-reflog.md) | [原文](raw/git/git-reflog.adoc) |
| `git remote` | 管理远程仓库地址和跟踪配置。 | Git 2.23+ | [卡片](cards/git-remote.md) | [检索](retrieval/git-remote.md) | [原文](raw/git/git-remote.adoc) |
| `git reset` | 调整暂存区，或将当前分支移动到指定提交。 | Git 2.23+ | [卡片](cards/git-reset.md) | [检索](retrieval/git-reset.md) | [原文](raw/git/git-reset.adoc) |
| `git restore` | 从暂存区或指定提交恢复工作区和暂存区文件。 | Git 2.23+ | [卡片](cards/git-restore.md) | [检索](retrieval/git-restore.md) | [原文](raw/git/git-restore.adoc) |
| `git revert` | 通过新增反向提交撤销已有提交的改动。 | Git 2.23+ | [卡片](cards/git-revert.md) | [检索](retrieval/git-revert.md) | [原文](raw/git/git-revert.adoc) |
| `git show` | 显示某个 Git 对象及提交的详细内容。 | Git 2.23+ | [卡片](cards/git-show.md) | [检索](retrieval/git-show.md) | [原文](raw/git/git-show.adoc) |
| `git stash` | 临时保存和恢复尚未提交的工作。 | Git 2.23+ | [卡片](cards/git-stash.md) | [检索](retrieval/git-stash.md) | [原文](raw/git/git-stash.adoc) |
| `git status` | 查看工作区、暂存区和分支的当前状态。 | Git 2.23+ | [卡片](cards/git-status.md) | [检索](retrieval/git-status.md) | [原文](raw/git/git-status.adoc) |
| `git switch` | 切换工作分支，或创建新分支后切换。 | Git 2.23+ | [卡片](cards/git-switch.md) | [检索](retrieval/git-switch.md) | [原文](raw/git/git-switch.adoc) |
| `git tag` | 列出或创建提交的标签。 | Git 2.23+ | [卡片](cards/git-tag.md) | [检索](retrieval/git-tag.md) | [原文](raw/git/git-tag.adoc) |
| `grep` | 搜索文本中匹配模式的行。 | GNU grep | [卡片](cards/grep.md) | [检索](retrieval/grep.md) | [原文](raw/linux-command/grep.md) |
| `groups` | 打印用户所属的组名列表。 | GNU coreutils | [卡片](cards/groups.md) | [检索](retrieval/groups.md) | [原文](raw/linux-command/groups.md) |
| `gzip` | 压缩或解压单个文件，默认替换原文件。 | gzip | [卡片](cards/gzip.md) | [检索](retrieval/gzip.md) | [原文](raw/linux-command/gzip.md) |
| `halt` | 停止系统，现代 systemd 下即关机。 | systemd | [卡片](cards/halt.md) | [检索](retrieval/halt.md) | [原文](raw/linux-command/halt.md) |
| `head` | 显示文件开头的部分内容。 | GNU coreutils | [卡片](cards/head.md) | [检索](retrieval/head.md) | [原文](raw/linux-command/head.md) |
| `helm` | 使用 Chart 管理 Kubernetes 应用的模板与发布。 | Helm 3/4 基础操作 | [卡片](cards/helm.md) | [检索](retrieval/helm.md) | [原文](raw/helm/helm.go) |
| `helm install` | 从 Chart 创建一个新的 Helm 发布。 | Helm 3/4 基础操作 | [卡片](cards/helm-install.md) | [检索](retrieval/helm-install.md) | [原文](raw/helm/helm-install.go) |
| `helm list` | 列出命名空间或集群内的 Helm 发布记录。 | Helm 3/4 基础操作 | [卡片](cards/helm-list.md) | [检索](retrieval/helm-list.md) | [原文](raw/helm/helm-list.go) |
| `helm template` | 在本地渲染 Chart 为 Kubernetes YAML。 | Helm 3/4 基础操作 | [卡片](cards/helm-template.md) | [检索](retrieval/helm-template.md) | [原文](raw/helm/helm-template.go) |
| `helm upgrade` | 用新的 Chart 或配置更新已有 Helm 发布。 | Helm 3/4 基础操作 | [卡片](cards/helm-upgrade.md) | [检索](retrieval/helm-upgrade.md) | [原文](raw/helm/helm-upgrade.go) |
| `host` | 查询域名的 DNS 记录与反向解析。 | BIND utils | [卡片](cards/host.md) | [检索](retrieval/host.md) | [原文](raw/linux-command/host.md) |
| `hostname` | 显示或临时设置主机名。 | hostname | [卡片](cards/hostname.md) | [检索](retrieval/hostname.md) | [原文](raw/linux-command/hostname.md) |
| `hostnamectl` | 查看或设置系统主机名。 | systemd | [卡片](cards/hostnamectl.md) | [检索](retrieval/hostnamectl.md) | [原文](raw/linux-command/hostnamectl.md) |
| `htop` | 交互式进程查看器，可动态排序。 | htop | [卡片](cards/htop.md) | [检索](retrieval/htop.md) | [原文](raw/linux-command/htop.md) |
| `hwclock` | 读取与设置主板硬件时钟。 | util-linux | [卡片](cards/hwclock.md) | [检索](retrieval/hwclock.md) | [原文](raw/linux-command/hwclock.md) |
| `id` | 显示用户 ID、组 ID 以及所属组。 | GNU coreutils | [卡片](cards/id.md) | [检索](retrieval/id.md) | [原文](raw/linux-command/id.md) |
| `ifconfig` | 查看和临时配置网络接口。 | net-tools | [卡片](cards/ifconfig.md) | [检索](retrieval/ifconfig.md) | [原文](raw/linux-command/ifconfig.md) |
| `iftop` | 实时查看网卡各连接的流量。 | iftop | [卡片](cards/iftop.md) | [检索](retrieval/iftop.md) | [原文](raw/linux-command/iftop.md) |
| `insmod` | 把指定内核模块文件加载进内核。 | kmod | [卡片](cards/insmod.md) | [检索](retrieval/insmod.md) | [原文](raw/linux-command/insmod.md) |
| `install` | 复制文件并设定权限属主，或建目录。 | GNU coreutils | [卡片](cards/install.md) | [检索](retrieval/install.md) | [原文](raw/linux-command/install.md) |
| `iostat` | 查看磁盘 I/O 与 CPU 的使用情况。 | sysstat | [卡片](cards/iostat.md) | [检索](retrieval/iostat.md) | [原文](raw/linux-command/iostat.md) |
| `ip` | 查看和配置网络接口、地址和路由。 | iproute2 | [卡片](cards/ip.md) | [检索](retrieval/ip.md) | [原文](raw/linux-command/ip.md) |
| `iptables` | 查看和配置 netfilter 过滤规则。 | iptables | [卡片](cards/iptables.md) | [检索](retrieval/iptables.md) | [原文](raw/linux-command/iptables.md) |
| `jobs` | 列出当前 shell 的作业状态。 | Bash 内建 | [卡片](cards/jobs.md) | [检索](retrieval/jobs.md) | [原文](raw/linux-command/jobs.md) |
| `join` | 按共同字段合并两个已排序文本。 | GNU coreutils | [卡片](cards/join.md) | [检索](retrieval/join.md) | [原文](raw/linux-command/join.md) |
| `journalctl` | 查询和跟踪 systemd 日志。 | systemd | [卡片](cards/journalctl.md) | [检索](retrieval/journalctl.md) | [原文](raw/linux-command/journalctl.md) |
| `jq` | 解析、筛选和转换 JSON 数据。 | jq 1.7+ 基础选项 | [卡片](cards/jq.md) | [检索](retrieval/jq.md) | [原文](raw/jq/jq.yml) |
| `kill` | 向进程发送信号，默认请求正常终止。 | Bash / Linux kill common subset | [卡片](cards/kill.md) | [检索](retrieval/kill.md) | [原文](raw/linux-command/kill.md) |
| `killall` | 按进程名向一组同名进程发信号。 | psmisc | [卡片](cards/killall.md) | [检索](retrieval/killall.md) | [原文](raw/linux-command/killall.md) |
| `kubectl` | 访问和管理 Kubernetes 集群资源的命令行工具。 | kubectl / Kubernetes | [卡片](cards/kubectl.md) | [检索](retrieval/kubectl.md) | [原文](raw/kubectl/kubectl.md) |
| `kubectl apply` | 根据资源清单创建或更新 Kubernetes 对象。 | kubectl / Kubernetes | [卡片](cards/kubectl-apply.md) | [检索](retrieval/kubectl-apply.md) | [原文](raw/kubectl/kubectl-apply.go) |
| `kubectl describe` | 查看资源详情、状态和关联事件的可读摘要。 | kubectl / Kubernetes | [卡片](cards/kubectl-describe.md) | [检索](retrieval/kubectl-describe.md) | [原文](raw/kubectl/kubectl-describe.go) |
| `kubectl exec` | 在 Kubernetes Pod 的运行中容器内执行命令。 | kubectl / Kubernetes | [卡片](cards/kubectl-exec.md) | [检索](retrieval/kubectl-exec.md) | [原文](raw/kubectl/kubectl-exec.go) |
| `kubectl get` | 列出 Kubernetes 资源或读取指定资源。 | kubectl / Kubernetes | [卡片](cards/kubectl-get.md) | [检索](retrieval/kubectl-get.md) | [原文](raw/kubectl/kubectl-get.go) |
| `kubectl logs` | 读取 Pod 容器的标准输出与标准错误日志。 | kubectl / Kubernetes | [卡片](cards/kubectl-logs.md) | [检索](retrieval/kubectl-logs.md) | [原文](raw/kubectl/kubectl-logs.go) |
| `kubectl rollout status` | 等待并查看某个工作负载的滚动发布状态。 | kubectl / Kubernetes | [卡片](cards/kubectl-rollout-status.md) | [检索](retrieval/kubectl-rollout-status.md) | [原文](raw/kubectl/kubectl-rollout-status.go) |
| `last` | 查看用户登录和系统重启历史。 | util-linux | [卡片](cards/last.md) | [检索](retrieval/last.md) | [原文](raw/linux-command/last.md) |
| `ldd` | 列出程序或库依赖的共享库。 | glibc | [卡片](cards/ldd.md) | [检索](retrieval/ldd.md) | [原文](raw/linux-command/ldd.md) |
| `less` | 分页浏览文本，支持前后翻页和搜索。 | less | [卡片](cards/less.md) | [检索](retrieval/less.md) | [原文](raw/linux-command/less.md) |
| `ln` | 为文件建立硬链接或符号链接。 | GNU coreutils | [卡片](cards/ln.md) | [检索](retrieval/ln.md) | [原文](raw/linux-command/ln.md) |
| `locate` | 从索引数据库快速查找文件路径。 | plocate / mlocate | [卡片](cards/locate.md) | [检索](retrieval/locate.md) | [原文](raw/linux-command/locate.md) |
| `ls` | 列出目录中的文件和子目录。 | GNU coreutils | [卡片](cards/ls.md) | [检索](retrieval/ls.md) | [原文](raw/linux-command/ls.md) |
| `lsattr` | 查看文件的 ext 文件系统属性标志。 | e2fsprogs | [卡片](cards/lsattr.md) | [检索](retrieval/lsattr.md) | [原文](raw/linux-command/lsattr.md) |
| `lsblk` | 树状列出块设备与分区。 | util-linux | [卡片](cards/lsblk.md) | [检索](retrieval/lsblk.md) | [原文](raw/linux-command/lsblk.md) |
| `lscpu` | 显示 CPU 架构和拓扑信息。 | util-linux | [卡片](cards/lscpu.md) | [检索](retrieval/lscpu.md) | [原文](raw/linux-command/lscpu.md) |
| `lsmod` | 列出已加载的内核模块。 | kmod | [卡片](cards/lsmod.md) | [检索](retrieval/lsmod.md) | [原文](raw/linux-command/lsmod.md) |
| `lsof` | 列出进程打开的文件，包括网络套接字。 | lsof | [卡片](cards/lsof.md) | [检索](retrieval/lsof.md) | [原文](raw/linux-command/lsof.md) |
| `ltrace` | 跟踪进程对库函数的调用。 | ltrace | [卡片](cards/ltrace.md) | [检索](retrieval/ltrace.md) | [原文](raw/linux-command/ltrace.md) |
| `make` | 按依赖关系增量构建或干跑预览。 | GNU Make | [卡片](cards/make.md) | [检索](retrieval/make.md) | [原文](raw/linux-command/make.md) |
| `md5sum` | 计算或核对文件的 MD5 摘要。 | GNU coreutils | [卡片](cards/md5sum.md) | [检索](retrieval/md5sum.md) | [原文](raw/linux-command/md5sum.md) |
| `mkdir` | 创建目录。 | GNU coreutils | [卡片](cards/mkdir.md) | [检索](retrieval/mkdir.md) | [原文](raw/linux-command/mkdir.md) |
| `mkfs` | 在设备上创建文件系统，会清空数据。 | util-linux | [卡片](cards/mkfs.md) | [检索](retrieval/mkfs.md) | [原文](raw/linux-command/mkfs.md) |
| `mkswap` | 建立交换区，会覆盖设备原有内容。 | util-linux | [卡片](cards/mkswap.md) | [检索](retrieval/mkswap.md) | [原文](raw/linux-command/mkswap.md) |
| `mktemp` | 安全创建临时文件或目录。 | GNU coreutils | [卡片](cards/mktemp.md) | [检索](retrieval/mktemp.md) | [原文](raw/linux-command/mktemp.md) |
| `modinfo` | 查看内核模块的描述与参数。 | kmod | [卡片](cards/modinfo.md) | [检索](retrieval/modinfo.md) | [原文](raw/linux-command/modinfo.md) |
| `modprobe` | 按依赖关系加载或卸载内核模块。 | kmod | [卡片](cards/modprobe.md) | [检索](retrieval/modprobe.md) | [原文](raw/linux-command/modprobe.md) |
| `mount` | 把设备挂载到挂载点。 | util-linux | [卡片](cards/mount.md) | [检索](retrieval/mount.md) | [原文](raw/linux-command/mount.md) |
| `mpstat` | 按 CPU 查看利用率与中断统计。 | sysstat | [卡片](cards/mpstat.md) | [检索](retrieval/mpstat.md) | [原文](raw/linux-command/mpstat.md) |
| `mtr` | 边探测边统计各跳链路质量。 | mtr | [卡片](cards/mtr.md) | [检索](retrieval/mtr.md) | [原文](raw/linux-command/mtr.md) |
| `mv` | 移动文件或目录，也可用于重命名。 | GNU coreutils | [卡片](cards/mv.md) | [检索](retrieval/mv.md) | [原文](raw/linux-command/mv.md) |
| `nc` | TCP/UDP 连接、监听与端口探测。 | netcat-openbsd | [卡片](cards/nc.md) | [检索](retrieval/nc.md) | [原文](raw/linux-command/nc.md) |
| `nethogs` | 按进程实时查看网络带宽占用。 | nethogs | [卡片](cards/nethogs.md) | [检索](retrieval/nethogs.md) | [原文](raw/linux-command/nethogs.md) |
| `netstat` | 查看网络连接、监听端口与路由表。 | net-tools | [卡片](cards/netstat.md) | [检索](retrieval/netstat.md) | [原文](raw/linux-command/netstat.md) |
| `nice` | 以指定调度优先级运行命令。 | GNU coreutils | [卡片](cards/nice.md) | [检索](retrieval/nice.md) | [原文](raw/linux-command/nice.md) |
| `nl` | 给文本加上行号后输出。 | GNU coreutils | [卡片](cards/nl.md) | [检索](retrieval/nl.md) | [原文](raw/linux-command/nl.md) |
| `nmap` | 探测主机开放端口和服务版本。 | nmap | [卡片](cards/nmap.md) | [检索](retrieval/nmap.md) | [原文](raw/linux-command/nmap.md) |
| `nohup` | 退出终端后仍运行命令。 | GNU coreutils | [卡片](cards/nohup.md) | [检索](retrieval/nohup.md) | [原文](raw/linux-command/nohup.md) |
| `npm` | 管理 Node.js 项目的软件包、依赖和脚本。 | npm CLI | [卡片](cards/npm.md) | [检索](retrieval/npm.md) | [原文](raw/npm/npm.md) |
| `npm ci` | 根据现有锁文件执行干净的项目依赖安装。 | npm CLI | [卡片](cards/npm-ci.md) | [检索](retrieval/npm-ci.md) | [原文](raw/npm/npm-ci.md) |
| `npm install` | 安装 Node.js 项目依赖或添加指定软件包。 | npm CLI | [卡片](cards/npm-install.md) | [检索](retrieval/npm-install.md) | [原文](raw/npm/npm-install.md) |
| `npm list` | 显示项目已安装依赖的树状关系。 | npm CLI | [卡片](cards/npm-list.md) | [检索](retrieval/npm-list.md) | [原文](raw/npm/npm-list.md) |
| `npm outdated` | 检查项目依赖的已装、允许和最新版本。 | npm CLI | [卡片](cards/npm-outdated.md) | [检索](retrieval/npm-outdated.md) | [原文](raw/npm/npm-outdated.md) |
| `npm run` | 列出或执行 package.json 中定义的项目脚本。 | npm CLI | [卡片](cards/npm-run.md) | [检索](retrieval/npm-run.md) | [原文](raw/npm/npm-run.md) |
| `nslookup` | 按域名或 IP 查询 DNS 记录。 | BIND utils | [卡片](cards/nslookup.md) | [检索](retrieval/nslookup.md) | [原文](raw/linux-command/nslookup.md) |
| `objdump` | 查看目标文件和可执行文件结构。 | binutils | [卡片](cards/objdump.md) | [检索](retrieval/objdump.md) | [原文](raw/linux-command/objdump.md) |
| `parted` | 磁盘分区与调整分区大小的工具。 | parted | [卡片](cards/parted.md) | [检索](retrieval/parted.md) | [原文](raw/linux-command/parted.md) |
| `passwd` | 修改用户密码并管理锁定状态。 | shadow-utils | [卡片](cards/passwd.md) | [检索](retrieval/passwd.md) | [原文](raw/linux-command/passwd.md) |
| `paste` | 把多个文件按列并排合并。 | GNU coreutils | [卡片](cards/paste.md) | [检索](retrieval/paste.md) | [原文](raw/linux-command/paste.md) |
| `pgrep` | 按名称或条件查找进程并输出 PID。 | procps-ng | [卡片](cards/pgrep.md) | [检索](retrieval/pgrep.md) | [原文](raw/linux-command/pgrep.md) |
| `pidstat` | 按进程监控 CPU、内存与磁盘 IO。 | sysstat | [卡片](cards/pidstat.md) | [检索](retrieval/pidstat.md) | [原文](raw/linux-command/pidstat.md) |
| `ping` | 用 ICMP 测试到目标主机的连通性。 | iputils | [卡片](cards/ping.md) | [检索](retrieval/ping.md) | [原文](raw/linux-command/ping.md) |
| `pip` | 安装和管理指定 Python 环境中的软件包。 | pip（示例通过 Python 3 调用） | [卡片](cards/pip.md) | [检索](retrieval/pip.md) | [原文](raw/pip/pip.rst) |
| `pip check` | 检查已安装包的依赖是否缺失或版本不兼容。 | pip（示例通过 Python 3 调用） | [卡片](cards/pip-check.md) | [检索](retrieval/pip-check.md) | [原文](raw/pip/pip-check.rst) |
| `pip freeze` | 按 requirements 格式输出当前环境的软件包版本。 | pip（示例通过 Python 3 调用） | [卡片](cards/pip-freeze.md) | [检索](retrieval/pip-freeze.md) | [原文](raw/pip/pip-freeze.rst) |
| `pip install` | 向 Python 环境安装软件包或项目依赖。 | pip（示例通过 Python 3 调用） | [卡片](cards/pip-install.md) | [检索](retrieval/pip-install.md) | [原文](raw/pip/pip-install.rst) |
| `pip list` | 列出 Python 环境中已经安装的软件包。 | pip（示例通过 Python 3 调用） | [卡片](cards/pip-list.md) | [检索](retrieval/pip-list.md) | [原文](raw/pip/pip-list.rst) |
| `pip show` | 显示已安装 Python 包的元数据和安装位置。 | pip（示例通过 Python 3 调用） | [卡片](cards/pip-show.md) | [检索](retrieval/pip-show.md) | [原文](raw/pip/pip-show.rst) |
| `pkill` | 按进程名或匹配模式查找并发送信号。 | procps-ng | [卡片](cards/pkill.md) | [检索](retrieval/pkill.md) | [原文](raw/linux-command/pkill.md) |
| `poweroff` | 关闭 Linux 系统并写入关机记录。 | systemd | [卡片](cards/poweroff.md) | [检索](retrieval/poweroff.md) | [原文](raw/linux-command/poweroff.md) |
| `printf` | 按格式串格式化输出。 | Bash 内建 / GNU coreutils | [卡片](cards/printf.md) | [检索](retrieval/printf.md) | [原文](raw/linux-command/printf.md) |
| `ps` | 显示进程的当前快照。 | procps-ng | [卡片](cards/ps.md) | [检索](retrieval/ps.md) | [原文](raw/linux-command/ps.md) |
| `pstree` | 以树状图显示进程的父子派生关系。 | psmisc | [卡片](cards/pstree.md) | [检索](retrieval/pstree.md) | [原文](raw/linux-command/pstree.md) |
| `pwd` | 显示当前工作目录的绝对路径。 | Bash / GNU coreutils | [卡片](cards/pwd.md) | [检索](retrieval/pwd.md) | [原文](raw/linux-command/pwd.md) |
| `python3` | 运行 Python 3 程序、模块或交互解释器。 | Python 3 | [卡片](cards/python3.md) | [检索](retrieval/python3.md) | [原文](raw/python/python3.rst) |
| `realpath` | 把相对路径和符号链接解析成绝对路径。 | GNU coreutils | [卡片](cards/realpath.md) | [检索](retrieval/realpath.md) | [原文](raw/linux-command/realpath.md) |
| `reboot` | 重启系统，需 root 权限。 | systemd | [卡片](cards/reboot.md) | [检索](retrieval/reboot.md) | [原文](raw/linux-command/reboot.md) |
| `rename` | 按字面串批量替换文件名。 | util-linux | [卡片](cards/rename.md) | [检索](retrieval/rename.md) | [原文](raw/linux-command/rename.md) |
| `renice` | 调整运行中进程的调度优先级。 | util-linux | [卡片](cards/renice.md) | [检索](retrieval/renice.md) | [原文](raw/linux-command/renice.md) |
| `rev` | 把每行内容按字符反序输出。 | util-linux | [卡片](cards/rev.md) | [检索](retrieval/rev.md) | [原文](raw/linux-command/rev.md) |
| `rg` | 快速递归搜索文件内容，默认遵循忽略规则。 | ripgrep | [卡片](cards/rg.md) | [检索](retrieval/rg.md) | [原文](raw/ripgrep/rg.md) |
| `rm` | 删除文件；指定递归选项后可删除目录。 | GNU coreutils | [卡片](cards/rm.md) | [检索](retrieval/rm.md) | [原文](raw/linux-command/rm.md) |
| `rmdir` | 删除空目录。 | GNU coreutils | [卡片](cards/rmdir.md) | [检索](retrieval/rmdir.md) | [原文](raw/linux-command/rmdir.md) |
| `rmmod` | 从内核中卸载已加载的模块。 | kmod | [卡片](cards/rmmod.md) | [检索](retrieval/rmmod.md) | [原文](raw/linux-command/rmmod.md) |
| `route` | 查看和设置内核静态路由表。 | net-tools | [卡片](cards/route.md) | [检索](retrieval/route.md) | [原文](raw/linux-command/route.md) |
| `rpm` | 直接操作 RPM 包和本地数据库。 | RPM | [卡片](cards/rpm.md) | [检索](retrieval/rpm.md) | [原文](raw/linux-command/rpm.md) |
| `rsync` | 在本地或远程目录之间增量同步文件。 | rsync | [卡片](cards/rsync.md) | [检索](retrieval/rsync.md) | [原文](raw/linux-command/rsync.md) |
| `sar` | 采样并报告系统资源使用统计。 | sysstat | [卡片](cards/sar.md) | [检索](retrieval/sar.md) | [原文](raw/linux-command/sar.md) |
| `scp` | 在本地与远程主机之间复制文件。 | OpenSSH | [卡片](cards/scp.md) | [检索](retrieval/scp.md) | [原文](raw/linux-command/scp.md) |
| `sed` | 按行处理文本，可替换、筛选或删除内容。 | GNU sed | [卡片](cards/sed.md) | [检索](retrieval/sed.md) | [原文](raw/linux-command/sed.md) |
| `seq` | 按指定增量打印一串数字。 | GNU coreutils | [卡片](cards/seq.md) | [检索](retrieval/seq.md) | [原文](raw/linux-command/seq.md) |
| `service` | 以 SysV 脚本方式管理服务状态。 | initscripts（systemd 兼容） | [卡片](cards/service.md) | [检索](retrieval/service.md) | [原文](raw/linux-command/service.md) |
| `setfacl` | 设置文件的访问控制列表 ACL。 | acl | [卡片](cards/setfacl.md) | [检索](retrieval/setfacl.md) | [原文](raw/linux-command/setfacl.md) |
| `setsid` | 在新会话中运行程序，脱离当前终端。 | util-linux | [卡片](cards/setsid.md) | [检索](retrieval/setsid.md) | [原文](raw/linux-command/setsid.md) |
| `sftp` | 通过 SSH 加密地交互传输文件。 | OpenSSH | [卡片](cards/sftp.md) | [检索](retrieval/sftp.md) | [原文](raw/linux-command/sftp.md) |
| `sha256sum` | 计算或核对文件的 SHA-256 摘要。 | GNU coreutils | [卡片](cards/sha256sum.md) | [检索](retrieval/sha256sum.md) | [原文](raw/linux-command/sha256sum.md) |
| `shuf` | 随机打乱输入行或抽取若干行。 | GNU coreutils | [卡片](cards/shuf.md) | [检索](retrieval/shuf.md) | [原文](raw/linux-command/shuf.md) |
| `shutdown` | 安排关机或重启，并通知登录用户。 | systemd | [卡片](cards/shutdown.md) | [检索](retrieval/shutdown.md) | [原文](raw/linux-command/shutdown.md) |
| `sort` | 对文本行排序。 | GNU coreutils | [卡片](cards/sort.md) | [检索](retrieval/sort.md) | [原文](raw/linux-command/sort.md) |
| `split` | 按大小或行数把大文件切成多块。 | GNU coreutils | [卡片](cards/split.md) | [检索](retrieval/split.md) | [原文](raw/linux-command/split.md) |
| `ss` | 查看套接字连接和监听端口。 | iproute2 | [卡片](cards/ss.md) | [检索](retrieval/ss.md) | [原文](raw/linux-command/ss.md) |
| `ssh` | 通过加密连接登录远程主机或执行命令。 | OpenSSH | [卡片](cards/ssh.md) | [检索](retrieval/ssh.md) | [原文](raw/linux-command/ssh.md) |
| `ssh-copy-id` | 把本机公钥装到远端账户的授权列表。 | OpenSSH | [卡片](cards/ssh-copy-id.md) | [检索](retrieval/ssh-copy-id.md) | [原文](raw/linux-command/ssh-copy-id.md) |
| `ssh-keygen` | 生成、查看和管理 SSH 密钥对。 | OpenSSH | [卡片](cards/ssh-keygen.md) | [检索](retrieval/ssh-keygen.md) | [原文](raw/linux-command/ssh-keygen.md) |
| `stat` | 显示文件详细状态信息。 | GNU coreutils | [卡片](cards/stat.md) | [检索](retrieval/stat.md) | [原文](raw/linux-command/stat.md) |
| `strace` | 跟踪进程的系统调用与信号。 | strace | [卡片](cards/strace.md) | [检索](retrieval/strace.md) | [原文](raw/linux-command/strace.md) |
| `strings` | 在二进制文件中查找可打印字符串。 | binutils | [卡片](cards/strings.md) | [检索](retrieval/strings.md) | [原文](raw/linux-command/strings.md) |
| `su` | 切换到其他用户身份。 | util-linux | [卡片](cards/su.md) | [检索](retrieval/su.md) | [原文](raw/linux-command/su.md) |
| `sudo` | 以其他用户身份执行命令。 | sudo | [卡片](cards/sudo.md) | [检索](retrieval/sudo.md) | [原文](raw/linux-command/sudo.md) |
| `swapoff` | 关闭指定交换分区或交换文件。 | util-linux | [卡片](cards/swapoff.md) | [检索](retrieval/swapoff.md) | [原文](raw/linux-command/swapoff.md) |
| `swapon` | 启用交换区并查看其使用情况。 | util-linux | [卡片](cards/swapon.md) | [检索](retrieval/swapon.md) | [原文](raw/linux-command/swapon.md) |
| `sync` | 把内存缓冲区数据强制写入磁盘。 | GNU coreutils | [卡片](cards/sync.md) | [检索](retrieval/sync.md) | [原文](raw/linux-command/sync.md) |
| `sysctl` | 查看与临时修改内核运行参数。 | procps-ng | [卡片](cards/sysctl.md) | [检索](retrieval/sysctl.md) | [原文](raw/linux-command/sysctl.md) |
| `systemctl` | 查询和管理 systemd 服务及其他单元。 | systemd | [卡片](cards/systemctl.md) | [检索](retrieval/systemctl.md) | [原文](raw/linux-command/systemctl.md) |
| `tac` | 按行倒序输出文件内容。 | GNU coreutils | [卡片](cards/tac.md) | [检索](retrieval/tac.md) | [原文](raw/linux-command/tac.md) |
| `tail` | 显示文件末尾内容，也可持续跟踪新增内容。 | GNU coreutils | [卡片](cards/tail.md) | [检索](retrieval/tail.md) | [原文](raw/linux-command/tail.md) |
| `tar` | 将多个文件打包，或列出、解开归档。 | GNU tar | [卡片](cards/tar.md) | [检索](retrieval/tar.md) | [原文](raw/linux-command/tar.md) |
| `tcpdump` | 抓取并分析网络接口上的数据包。 | tcpdump | [卡片](cards/tcpdump.md) | [检索](retrieval/tcpdump.md) | [原文](raw/linux-command/tcpdump.md) |
| `tee` | 同时输出到终端和文件。 | GNU coreutils | [卡片](cards/tee.md) | [检索](retrieval/tee.md) | [原文](raw/linux-command/tee.md) |
| `telnet` | 远程登录主机或探测端口连通性。 | telnet | [卡片](cards/telnet.md) | [检索](retrieval/telnet.md) | [原文](raw/linux-command/telnet.md) |
| `time` | 统计命令耗时与 CPU 占用。 | Bash 内建 / GNU time | [卡片](cards/time.md) | [检索](retrieval/time.md) | [原文](raw/linux-command/time.md) |
| `timedatectl` | 查看和设置系统时间、时区与 NTP。 | systemd | [卡片](cards/timedatectl.md) | [检索](retrieval/timedatectl.md) | [原文](raw/linux-command/timedatectl.md) |
| `tmux` | 终端复用器，管理多个会话。 | tmux | [卡片](cards/tmux.md) | [检索](retrieval/tmux.md) | [原文](raw/linux-command/tmux.md) |
| `top` | 交互查看进程和 CPU、内存等资源使用情况。 | procps-ng | [卡片](cards/top.md) | [检索](retrieval/top.md) | [原文](raw/linux-command/top.md) |
| `touch` | 创建空文件，或更新已有文件的时间戳。 | GNU coreutils | [卡片](cards/touch.md) | [检索](retrieval/touch.md) | [原文](raw/linux-command/touch.md) |
| `tr` | 按字符集转换、压缩或删除输入字符。 | GNU coreutils | [卡片](cards/tr.md) | [检索](retrieval/tr.md) | [原文](raw/linux-command/tr.md) |
| `traceroute` | 追踪数据包到目标经过的每跳网关和延迟。 | traceroute | [卡片](cards/traceroute.md) | [检索](retrieval/traceroute.md) | [原文](raw/linux-command/traceroute.md) |
| `tree` | 以树状图列出目录及其子目录内容。 | tree | [卡片](cards/tree.md) | [检索](retrieval/tree.md) | [原文](raw/linux-command/tree.md) |
| `ulimit` | 查看或设置当前 shell 的资源上限。 | Bash 内建 | [卡片](cards/ulimit.md) | [检索](retrieval/ulimit.md) | [原文](raw/linux-command/ulimit.md) |
| `umount` | 卸载已挂载的文件系统。 | util-linux | [卡片](cards/umount.md) | [检索](retrieval/umount.md) | [原文](raw/linux-command/umount.md) |
| `uname` | 显示内核和系统信息。 | GNU coreutils | [卡片](cards/uname.md) | [检索](retrieval/uname.md) | [原文](raw/linux-command/uname.md) |
| `uniq` | 处理相邻的重复文本行。 | GNU coreutils | [卡片](cards/uniq.md) | [检索](retrieval/uniq.md) | [原文](raw/linux-command/uniq.md) |
| `unlink` | 删除单个文件，且不经过回收站。 | GNU coreutils | [卡片](cards/unlink.md) | [检索](retrieval/unlink.md) | [原文](raw/linux-command/unlink.md) |
| `unrar` | 从 rar 压缩包里列表或解压文件。 | unrar | [卡片](cards/unrar.md) | [检索](retrieval/unrar.md) | [原文](raw/linux-command/unrar.md) |
| `unzip` | 查看或解压 ZIP 压缩包。 | Info-ZIP UnZip | [卡片](cards/unzip.md) | [检索](retrieval/unzip.md) | [原文](raw/linux-command/unzip.md) |
| `uptime` | 查看运行时间和系统平均负载。 | procps-ng | [卡片](cards/uptime.md) | [检索](retrieval/uptime.md) | [原文](raw/linux-command/uptime.md) |
| `useradd` | 创建新的本地用户账户。 | shadow-utils | [卡片](cards/useradd.md) | [检索](retrieval/useradd.md) | [原文](raw/linux-command/useradd.md) |
| `userdel` | 删除用户账户及其家目录。 | shadow-utils | [卡片](cards/userdel.md) | [检索](retrieval/userdel.md) | [原文](raw/linux-command/userdel.md) |
| `usermod` | 修改已有用户的属性和组。 | shadow-utils | [卡片](cards/usermod.md) | [检索](retrieval/usermod.md) | [原文](raw/linux-command/usermod.md) |
| `users` | 打印当前登录本机的用户名列表。 | GNU coreutils | [卡片](cards/users.md) | [检索](retrieval/users.md) | [原文](raw/linux-command/users.md) |
| `uv` | 管理 Python 项目、依赖、虚拟环境和工具。 | uv 项目工作流 | [卡片](cards/uv.md) | [检索](retrieval/uv.md) | [原文](raw/uv/uv.md) |
| `uv add` | 向项目清单添加依赖并更新项目环境。 | uv 项目工作流 | [卡片](cards/uv-add.md) | [检索](retrieval/uv-add.md) | [原文](raw/uv/uv-add.md) |
| `uv lock` | 解析项目依赖并创建或更新 uv.lock。 | uv 项目工作流 | [卡片](cards/uv-lock.md) | [检索](retrieval/uv-lock.md) | [原文](raw/uv/uv-lock.md) |
| `uv run` | 在项目环境或指定环境中运行命令或 Python 脚本。 | uv 项目工作流 | [卡片](cards/uv-run.md) | [检索](retrieval/uv-run.md) | [原文](raw/uv/uv-run.md) |
| `uv sync` | 将项目环境同步为锁文件和依赖组要求的状态。 | uv 项目工作流 | [卡片](cards/uv-sync.md) | [检索](retrieval/uv-sync.md) | [原文](raw/uv/uv-sync.md) |
| `vmstat` | 报告进程、内存、IO 与 CPU 概况。 | procps-ng | [卡片](cards/vmstat.md) | [检索](retrieval/vmstat.md) | [原文](raw/linux-command/vmstat.md) |
| `w` | 显示登录用户及其正在执行的命令。 | procps-ng | [卡片](cards/w.md) | [检索](retrieval/w.md) | [原文](raw/linux-command/w.md) |
| `wait` | 等待后台进程或作业结束后返回。 | Bash 内建 | [卡片](cards/wait.md) | [检索](retrieval/wait.md) | [原文](raw/linux-command/wait.md) |
| `watch` | 周期性执行命令并刷新输出。 | procps-ng | [卡片](cards/watch.md) | [检索](retrieval/watch.md) | [原文](raw/linux-command/watch.md) |
| `wc` | 统计文件的行数、单词数、字节数等。 | GNU coreutils | [卡片](cards/wc.md) | [检索](retrieval/wc.md) | [原文](raw/linux-command/wc.md) |
| `wget` | 从网络下载文件，支持续传和批量下载。 | GNU Wget | [卡片](cards/wget.md) | [检索](retrieval/wget.md) | [原文](raw/linux-command/wget.md) |
| `which` | 在 PATH 中查找可执行命令的位置。 | GNU which | [卡片](cards/which.md) | [检索](retrieval/which.md) | [原文](raw/linux-command/which.md) |
| `who` | 列出当前登录的用户和终端。 | GNU coreutils | [卡片](cards/who.md) | [检索](retrieval/who.md) | [原文](raw/linux-command/who.md) |
| `whoami` | 显示当前有效用户的名称。 | GNU coreutils | [卡片](cards/whoami.md) | [检索](retrieval/whoami.md) | [原文](raw/linux-command/whoami.md) |
| `xargs` | 将标准输入拆成参数，批量传给其他命令。 | GNU findutils | [卡片](cards/xargs.md) | [检索](retrieval/xargs.md) | [原文](raw/linux-command/xargs.md) |
| `xz` | 高压缩率压缩单个文件，默认替换原文件。 | xz-utils | [卡片](cards/xz.md) | [检索](retrieval/xz.md) | [原文](raw/linux-command/xz.md) |
| `yes` | 反复输出同一字符串，默认输出 y。 | GNU coreutils | [卡片](cards/yes.md) | [检索](retrieval/yes.md) | [原文](raw/linux-command/yes.md) |
| `yum` | RHEL 旧版本的 RPM 包管理器。 | YUM | [卡片](cards/yum.md) | [检索](retrieval/yum.md) | [原文](raw/linux-command/yum.md) |
| `zip` | 创建或更新 ZIP 压缩包。 | Info-ZIP Zip | [卡片](cards/zip.md) | [检索](retrieval/zip.md) | [原文](raw/linux-command/zip.md) |
