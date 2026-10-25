# docker cp 检索说明

## 用途与查询表达

在容器与宿主机之间复制文件或目录。适用实现：Docker CLI / Docker Engine。

- 复制容器里的文件。
- 向容器上传配置。
- 容器与本机传文件。

## 参数与行为

- `-a`：尽可能保留源文件的用户与组信息。
- `-L`：跟随源符号链接。
- `--help`：显示帮助。

## 常见任务示例

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

## 边界与易混淆点

支持停止的容器；目标路径必须满足父目录要求，复制可能覆盖同名内容，不是持续同步。
