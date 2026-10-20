# scp 检索说明

## 用途与查询表达

在本地与远程主机之间复制文件。适用实现：OpenSSH。

- 上传文件到服务器。
- 从服务器下载文件。
- 远程拷贝目录。

## 参数与行为

- `-P PORT`：指定远程端口。
- `-r`：递归复制目录。
- `-p`：保留修改时间、访问时间和权限模式。
- `-i FILE`：指定身份密钥文件。
- `-C`：启用压缩。
- `-v`：显示调试信息。

## 常见任务示例

**1. 把文件复制到远程主机的指定目录**

```bash
scp -P 2222 report.txt user@example.com:/tmp/
```

**2. 把远端日志下载到当前目录**

```bash
scp user@example.com:/var/log/app.log .
```

**3. 递归上传项目目录**

```bash
scp -r project/ user@example.com:/tmp/
```

## 边界与易混淆点

-P 才是端口，-p 保留属性；新版本 OpenSSH 默认使用 SFTP 传输，旧版可能使用传统 SCP 协议。
