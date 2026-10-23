# sftp 检索说明

## 用途与查询表达

通过 SSH 加密传输文件。适用实现：OpenSSH。

- 上传下载文件。
- 远程传文件。
- 批处理传文件。
- sftp 连不上。

## 参数与行为

- `-b FILE`：按批处理文件执行命令。
- `-P PORT`：指定远端 SSH 端口。
- `-C`：传输时启用压缩。
- `-o OPT`：传入 ssh 配置选项。
- `-F FILE`：指定 ssh 配置文件。
- `-v`：输出详细调试信息。

## 常见任务示例

**1. 连上远端主机进入交互模式**

```bash
sftp user@host.example.com
```

**2. 用批处理文件批量下载**

```bash
sftp -b /tmp/sftp_batch.txt user@host.example.com
```

## 边界与易混淆点

-P 是大写端口，-p 保留时间戳；递归要写进 get -r、put -r 子命令。
