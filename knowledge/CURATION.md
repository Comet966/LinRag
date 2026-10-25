# 整理与验证说明

当前共 295 个命令条目：原有 200 个 Linux 基础命令，加上 28 个 Git、25 个 Docker、10 个 Docker Compose 和 32 个常用软件工具条目。子命令分别建卡，例如 `git status`、`docker run`、`docker compose up`，不合并成一张冗长的工具手册。每张卡片保持一句话用途、常用参数和 2–4 个例子；检索层保持用途与查询表达、参数与行为、常见任务示例、边界与易混淆点四个章节。

新增条目的官方原文分别保存在 `raw/git/`、`raw/docker-cli/`、`raw/docker-compose/`；`manifest.json` 记录每张卡片的固定提交链接与摘要，`sources.lock.json` 固定各来源版本，`licenses/` 保留原始许可。多级命令使用完整空格分隔的命令名作为标识，文件名以连字符连接；例如标识为 `git status`，文件名为 `git-status.md`。

## 补充核对依据

以下上游手册页面用于核对部分易错事实，未整页导入知识库：

- [ls](https://man7.org/linux/man-pages/man1/ls.1.html)：长格式与单列。
- [grep](https://man7.org/linux/man-pages/man1/grep.1.html)：固定字符串、上下文。
- [tail](https://man7.org/linux/man-pages/man1/tail.1.html)：描述符与按名称跟踪。
- [cp](https://man7.org/linux/man-pages/man1/cp.1.html)、[rm](https://man7.org/linux/man-pages/man1/rm.1.html)：属性与交互删除。
- [sort](https://man7.org/linux/man-pages/man1/sort.1.html)、[cut](https://man7.org/linux/man-pages/man1/cut.1.html)：排序键与字符处理的版本差异。
- [find](https://man7.org/linux/man-pages/man1/find.1.html)、[xargs](https://man7.org/linux/man-pages/man1/xargs.1.html)：时间和文件名分隔。
- [scp](https://man7.org/linux/man-pages/man1/scp.1.html)：端口选项大小写。
- [ss](https://man7.org/linux/man-pages/man8/ss.8.html)、[ip](https://man7.org/linux/man-pages/man8/ip.8.html)：套接字和网络对象。
- [systemctl](https://man7.org/linux/man-pages/man1/systemctl.1.html)：启用和启动的区别。
- [ps](https://man7.org/linux/man-pages/man1/ps.1.html)、[pgrep](https://man7.org/linux/man-pages/man1/pgrep.1.html)：选项风格与命令匹配。
- [curl](https://curl.se/docs/manpage.html)：响应头、输出和错误处理。
- [less](https://man7.org/linux/man-pages/man1/less.1.html)、[Bash](https://man7.org/linux/man-pages/man1/bash.1.html)：交互阅读及内建命令。

## 校验边界

全部例子通过 bash 语法检查，但没有实际执行。第二批和第三批涉及磁盘、内核、网络和权限变更的命令只保留只读或占位符示例，并在检索层写明风险边界。回归测试以临时索引和模拟 embedding 验证卡片映射、命令合并、向量化输入与参数大小写。没有调用真实模型，没有创建生产索引。这不等于 Linux 实际运行验证或真实语义检索效果评测。目前等待用户审核。

## Git、Docker 与 Compose 的整理边界

- 以固定版本的官方文档为依据，用中文重写用途、常用参数和任务表达，不直接采用旧教程中的过时选项。Git 的 switch/restore 面向 2.23+，Compose 面向 `docker compose` 插件；具体选项是否可用仍取决于本机版本。
- 区分工作区与暂存区、fetch 与 pull、reset 与 revert、容器与镜像、run 与 start/exec、Compose run 与 exec。显式指定子命令的查询优先对应子命令卡片。
- Git clean、Docker rm/rmi、Compose down 的例子只提供执行前检查；删除、强推、改写历史、挂载和发布镜像等行为的影响在检索层注明。其他写入型例子也需要先确认仓库、容器和配置范围。
- 示例中的仓库地址、分支、提交、镜像、容器和服务名需要按环境替换。本文档不承诺执行成功，也未实际运行这些修改型命令。
- 本轮扩充不自动替换生产索引。新增条目审核后需重新向量化并重启服务，旧索引仍只包含此前的命令。

## 常用软件工具的整理范围

本批新增 32 个条目：jq、ripgrep、Python 3 各 1 个，pip 6 个、npm 6 个、uv 5 个、kubectl 7 个、Helm 5 个。卡片与检索层继续采用前述格式，保留参数解释、不同任务例子和行为边界。

- pip 示例优先使用 `python3 -m pip`，安装型例子指向已有虚拟环境；freeze 是环境快照，不是完整依赖锁文件。
- npm 区分 install、ci 和 run；注明 ci 清理 node_modules、锁文件一致性和生命周期脚本行为。
- uv 区分 locked、frozen、no-sync 的含义及锁文件、清单、环境三者的变化范围。
- kubectl 以命名空间和上下文限定目标，apply 示例只预检；Helm install/upgrade 示例只模拟，template 仅本地渲染。预检不保证离线，也不能代替真实目标集群验证。
- 本批固定官方文档、指南或包含帮助文本及选项定义的命令源码作为来源。`raw/` 保留原始格式（Markdown、YAML、RST 或 Go），不将这些文件直接送入检索。
- jq 的文档采用 CC BY 3.0，不能按 jq 可执行程序的 MIT 许可处理；上游 COPYING 与其许可链接保留在许可证和 NOTICE 文件中。其他来源保留各自许可。新增中文内容为整理和改写，未得到上游作者背书。
- 本批示例仅检查 shell 语法，不安装软件、不访问集群、不执行项目脚本。新增内容审核后再重建生产索引。
