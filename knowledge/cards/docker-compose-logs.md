## docker compose logs

查看 Compose 服务的日志输出。

### 常用参数

- `-f`：持续跟踪日志。
- `--tail N`：每个容器显示末尾 N 行。
- `--since TIME`：限制日志起始时间。
- `-t`：显示时间戳。

### 常用例子

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
