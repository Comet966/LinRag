## sftp

通过 SSH 加密地交互传输文件。

### 常用参数

- `-b FILE`：按批处理文件执行命令。
- `-P PORT`：指定远端 SSH 端口。
- `-C`：传输时启用压缩。
- `-o OPT`：传入 ssh 配置选项。
- `-F FILE`：指定 ssh 配置文件。
- `-v`：输出详细调试信息。

### 常用例子

**1. 连上远端主机进入交互模式**

```bash
sftp user@host.example.com
```

**2. 用批处理文件批量下载**

```bash
sftp -b /tmp/sftp_batch.txt user@host.example.com
```
