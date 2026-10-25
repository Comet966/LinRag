## kubectl logs

读取 Pod 容器的标准输出与标准错误日志。

### 常用参数

- `-f`：持续跟踪。
- `-c NAME`：指定容器。
- `--previous`：读取上一实例的容器日志。
- `--tail N`：限定末尾行数。
- `--since DURATION`：限定最近时长。

### 常用例子

**1. 查看指定 Pod 的最近日志**

```bash
kubectl logs demo-web -n demo --tail=100
```

**2. 跟踪 Pod 中某个容器的日志**

```bash
kubectl logs -f demo-web -n demo -c web
```

**3. 查看重启前一实例的日志**

```bash
kubectl logs demo-web -n demo --previous
```
