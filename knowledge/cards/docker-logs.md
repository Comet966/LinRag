## docker logs

读取容器标准输出与标准错误的日志。

### 常用参数

- `-f`：持续跟踪。
- `--tail N`：只显示末尾 N 行。
- `--since TIME`：只读取指定时间之后的日志。
- `-t`：显示时间戳。

### 常用例子

**1. 查看最后一百行日志**

```bash
docker logs --tail 100 demo-web
```

**2. 持续跟踪日志**

```bash
docker logs -f demo-web
```

**3. 查看最近十分钟带时间戳的日志**

```bash
docker logs --since 10m -t demo-web
```
