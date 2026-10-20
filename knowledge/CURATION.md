# 整理与验证说明

本轮为 50 个命令。每份卡片逐条编辑常用参数、简明说明和2–4 个不同场景的例子，检索文本另加任务表达、行为边界与适用实现。原始 Markdown、来源版本、摘要和许可均保留。

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

全部例子通过 bash 语法检查，但没有实际执行。回归测试以临时索引和模拟 embedding 验证卡片映射、命令合并、向量化输入与参数大小写。没有调用真实模型，没有创建生产索引。这不等于 Linux 实际运行验证或真实语义检索效果评测。目前等待用户审核。
