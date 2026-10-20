## scp

在本地与远程主机之间复制文件。

### 常用参数

- `-P PORT`：指定远程端口。
- `-r`：递归复制目录。
- `-p`：保留修改时间、访问时间和权限模式。
- `-i FILE`：指定身份密钥文件。
- `-C`：启用压缩。
- `-v`：显示调试信息。

### 常用例子

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
