# docker stop 检索说明

## 用途与查询表达

请求运行中的容器停止并等待退出。适用实现：Docker CLI / Docker Engine。

- 停止 Docker 容器。
- 优雅停止容器。
- 调整容器停止超时。

## 参数与行为

- `--timeout SECONDS`：设置强制终止前等待时间。
- `--signal SIGNAL`：指定先发送的信号。

## 常见任务示例

**1. 停止已核对名称的容器**

```bash
docker stop demo-web
```

**2. 给应用三十秒退出**

```bash
docker stop --timeout 30 demo-web
```

**3. 停止两个指定容器**

```bash
docker stop demo-web demo-worker
```

## 边界与易混淆点

会中断容器提供的服务；等待超时后可能发送 SIGKILL，停止不等于删除。
