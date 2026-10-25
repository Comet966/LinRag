# docker logs 检索说明

## 用途与查询表达

读取容器标准输出与标准错误的日志。适用实现：Docker CLI / Docker Engine。

- 查看容器日志。
- 实时跟踪 Docker 日志。
- 筛选最近错误日志。

## 参数与行为

- `-f`：持续跟踪。
- `--tail N`：只显示末尾 N 行。
- `--since TIME`：只读取指定时间之后的日志。
- `-t`：显示时间戳。

## 常见任务示例

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

## 边界与易混淆点

只读取日志驱动可提供的标准输出和错误，不等同于读取容器内任意日志文件；日志可能包含敏感信息。
