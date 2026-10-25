# docker compose ps 检索说明

## 用途与查询表达

查看 Compose 项目的服务容器状态。适用实现：Docker Compose 插件（docker compose）。

- 查看 Compose 服务状态。
- 列出项目容器。
- Compose 容器退出原因。

## 参数与行为

- `-a`：包括已停止的容器。
- `--services`：只列出服务名。
- `--format FORMAT`：指定输出格式。
- `-q`：只列出容器 ID。

## 常见任务示例

**1. 查看项目运行状态**

```bash
docker compose ps
```

**2. 包括已经退出的服务**

```bash
docker compose ps -a
```

**3. 以 JSON 查看服务状态**

```bash
docker compose ps --format json
```

## 边界与易混淆点

按项目配置和项目名限定范围，不等于列出主机上的全部容器。
