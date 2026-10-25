# docker 检索说明

## 用途与查询表达

管理镜像、容器、网络和数据卷的命令行工具。适用实现：Docker CLI / Docker Engine。

- Docker 常用命令。
- 容器命令帮助。
- 查看 Docker 连接目标。

## 参数与行为

- `--context NAME`：选择 Docker 上下文。
- `--host ENDPOINT`：指定守护进程地址。
- `--help`：显示命令帮助。

## 常见任务示例

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

## 边界与易混淆点

多数操作需要可访问的 Docker Engine；上下文决定操作哪个主机，Docker Desktop 与 Linux Engine 环境有所不同。
