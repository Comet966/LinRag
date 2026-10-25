# docker info 检索说明

## 用途与查询表达

查看 Docker Engine 的系统配置和资源信息。适用实现：Docker CLI / Docker Engine。

- 查看 Docker 存储驱动。
- Docker 系统信息。
- 检查容器引擎配置。

## 参数与行为

- `--format FORMAT`：设置输出格式。
- `--help`：显示帮助。

## 常见任务示例

**1. 查看引擎信息**

```bash
docker info
```

**2. 读取存储驱动**

```bash
docker info --format '{{.Driver}}'
```

**3. 读取运行中的容器数**

```bash
docker info --format '{{.ContainersRunning}}'
```

## 边界与易混淆点

显示当前上下文连接的 Engine；系统信息可能含主机名、镜像仓库和代理配置。
