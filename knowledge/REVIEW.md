# 知识库审核目录

当前收录 **200 个命令**。本目录依据 `manifest.json` 与实际 Markdown 文件整理，按命令名排序。

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
| `grep` | 搜索文本中匹配模式的行。 | GNU grep | [卡片](cards/grep.md) | [检索](retrieval/grep.md) | [原文](raw/linux-command/grep.md) |
| `groups` | 打印用户所属的组名列表。 | GNU coreutils | [卡片](cards/groups.md) | [检索](retrieval/groups.md) | [原文](raw/linux-command/groups.md) |
| `gzip` | 压缩或解压单个文件，默认替换原文件。 | gzip | [卡片](cards/gzip.md) | [检索](retrieval/gzip.md) | [原文](raw/linux-command/gzip.md) |
| `halt` | 停止系统，现代 systemd 下即关机。 | systemd | [卡片](cards/halt.md) | [检索](retrieval/halt.md) | [原文](raw/linux-command/halt.md) |
| `head` | 显示文件开头的部分内容。 | GNU coreutils | [卡片](cards/head.md) | [检索](retrieval/head.md) | [原文](raw/linux-command/head.md) |
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
| `kill` | 向进程发送信号，默认请求正常终止。 | Bash / Linux kill common subset | [卡片](cards/kill.md) | [检索](retrieval/kill.md) | [原文](raw/linux-command/kill.md) |
| `killall` | 按进程名向一组同名进程发信号。 | psmisc | [卡片](cards/killall.md) | [检索](retrieval/killall.md) | [原文](raw/linux-command/killall.md) |
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
| `nslookup` | 按域名或 IP 查询 DNS 记录。 | BIND utils | [卡片](cards/nslookup.md) | [检索](retrieval/nslookup.md) | [原文](raw/linux-command/nslookup.md) |
| `objdump` | 查看目标文件和可执行文件结构。 | binutils | [卡片](cards/objdump.md) | [检索](retrieval/objdump.md) | [原文](raw/linux-command/objdump.md) |
| `parted` | 磁盘分区与调整分区大小的工具。 | parted | [卡片](cards/parted.md) | [检索](retrieval/parted.md) | [原文](raw/linux-command/parted.md) |
| `passwd` | 修改用户密码并管理锁定状态。 | shadow-utils | [卡片](cards/passwd.md) | [检索](retrieval/passwd.md) | [原文](raw/linux-command/passwd.md) |
| `paste` | 把多个文件按列并排合并。 | GNU coreutils | [卡片](cards/paste.md) | [检索](retrieval/paste.md) | [原文](raw/linux-command/paste.md) |
| `pgrep` | 按名称或条件查找进程并输出 PID。 | procps-ng | [卡片](cards/pgrep.md) | [检索](retrieval/pgrep.md) | [原文](raw/linux-command/pgrep.md) |
| `pidstat` | 按进程监控 CPU、内存与磁盘 IO。 | sysstat | [卡片](cards/pidstat.md) | [检索](retrieval/pidstat.md) | [原文](raw/linux-command/pidstat.md) |
| `ping` | 用 ICMP 测试到目标主机的连通性。 | iputils | [卡片](cards/ping.md) | [检索](retrieval/ping.md) | [原文](raw/linux-command/ping.md) |
| `pkill` | 按进程名或匹配模式查找并发送信号。 | procps-ng | [卡片](cards/pkill.md) | [检索](retrieval/pkill.md) | [原文](raw/linux-command/pkill.md) |
| `poweroff` | 关闭 Linux 系统并写入关机记录。 | systemd | [卡片](cards/poweroff.md) | [检索](retrieval/poweroff.md) | [原文](raw/linux-command/poweroff.md) |
| `printf` | 按格式串格式化输出。 | Bash 内建 / GNU coreutils | [卡片](cards/printf.md) | [检索](retrieval/printf.md) | [原文](raw/linux-command/printf.md) |
| `ps` | 显示进程的当前快照。 | procps-ng | [卡片](cards/ps.md) | [检索](retrieval/ps.md) | [原文](raw/linux-command/ps.md) |
| `pstree` | 以树状图显示进程的父子派生关系。 | psmisc | [卡片](cards/pstree.md) | [检索](retrieval/pstree.md) | [原文](raw/linux-command/pstree.md) |
| `pwd` | 显示当前工作目录的绝对路径。 | Bash / GNU coreutils | [卡片](cards/pwd.md) | [检索](retrieval/pwd.md) | [原文](raw/linux-command/pwd.md) |
| `realpath` | 把相对路径和符号链接解析成绝对路径。 | GNU coreutils | [卡片](cards/realpath.md) | [检索](retrieval/realpath.md) | [原文](raw/linux-command/realpath.md) |
| `reboot` | 重启系统，需 root 权限。 | systemd | [卡片](cards/reboot.md) | [检索](retrieval/reboot.md) | [原文](raw/linux-command/reboot.md) |
| `rename` | 按字面串批量替换文件名。 | util-linux | [卡片](cards/rename.md) | [检索](retrieval/rename.md) | [原文](raw/linux-command/rename.md) |
| `renice` | 调整运行中进程的调度优先级。 | util-linux | [卡片](cards/renice.md) | [检索](retrieval/renice.md) | [原文](raw/linux-command/renice.md) |
| `rev` | 把每行内容按字符反序输出。 | util-linux | [卡片](cards/rev.md) | [检索](retrieval/rev.md) | [原文](raw/linux-command/rev.md) |
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
