## docker cp

在容器与宿主机之间复制文件或目录。

### 常用参数

- `-a`：尽可能保留源文件的用户与组信息。
- `-L`：跟随源符号链接。
- `--help`：显示帮助。

### 常用例子

**1. 从容器复制文件到本地**

```bash
docker cp demo-web:/etc/nginx/nginx.conf ./nginx.conf.copy
```

**2. 复制本地配置到容器临时目录**

```bash
docker cp ./nginx.conf demo-web:/tmp/nginx.conf
```

**3. 从容器复制日志目录**

```bash
docker cp demo-web:/var/log/nginx ./nginx-logs
```
