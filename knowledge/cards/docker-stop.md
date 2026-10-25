## docker stop

请求运行中的容器停止并等待退出。

### 常用参数

- `--timeout SECONDS`：设置强制终止前等待时间。
- `--signal SIGNAL`：指定先发送的信号。

### 常用例子

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
