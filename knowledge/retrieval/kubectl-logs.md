# kubectl logs 检索说明

## 用途与查询表达

读取 Pod 容器的标准输出与标准错误日志。适用实现：kubectl / Kubernetes。

- 查看 K8s 容器日志。
- 排查 Pod 重启前日志。
- 实时跟踪 Pod 日志。

## 参数与行为

- `-f`：持续跟踪。
- `-c NAME`：指定容器。
- `--previous`：读取上一实例的容器日志。
- `--tail N`：限定末尾行数。
- `--since DURATION`：限定最近时长。

## 常见任务示例

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

## 边界与易混淆点

多容器 Pod 应明确 -c；previous 仅适用于仍可获取的上一实例，不是永久历史日志归档。
