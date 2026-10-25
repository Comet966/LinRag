## docker

管理镜像、容器、网络和数据卷的命令行工具。

### 常用参数

- `--context NAME`：选择 Docker 上下文。
- `--host ENDPOINT`：指定守护进程地址。
- `--help`：显示命令帮助。

### 常用例子

**1. 查看 Docker 命令帮助**

```bash
docker --help
```

**2. 查看客户端与服务端版本**

```bash
docker version
```

**3. 查看已配置的连接上下文**

```bash
docker context ls
```
