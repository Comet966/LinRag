# docker compose logs 检索说明

## 用途与查询表达

查看 Compose 服务的日志输出。适用实现：Docker Compose 插件（docker compose）。

- 查看多容器日志。
- 持续跟踪 Compose 日志。
- 查看指定服务报错。

## 参数与行为

- `-f`：持续跟踪日志。
- `--tail N`：每个容器显示末尾 N 行。
- `--since TIME`：限制日志起始时间。
- `-t`：显示时间戳。

## 常见任务示例

**1. 查看 web 服务最近日志**

```bash
docker compose logs --tail 100 web
```

**2. 跟踪多个服务日志**

```bash
docker compose logs -f web worker
```

**3. 查看近十分钟带时间戳日志**

```bash
docker compose logs --since 10m -t
```

## 边界与易混淆点

日志按服务和容器聚合，不提供任意文件读取；输出可能包含应用凭据。
