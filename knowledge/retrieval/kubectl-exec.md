# kubectl exec 检索说明

## 用途与查询表达

在 Kubernetes Pod 的运行中容器内执行命令。适用实现：kubectl / Kubernetes。

- 进入 K8s Pod。
- 在 Kubernetes 容器执行命令。
- kubectl exec 双横线。

## 参数与行为

- `-i`：保持标准输入。
- `-t`：分配伪终端。
- `-c NAME`：指定容器。
- `-n NAMESPACE`：指定命名空间。
- `--`：分隔 kubectl 选项和容器命令。

## 常见任务示例

**1. 进入 Pod 指定容器的 shell**

```bash
kubectl exec -it demo-web -n demo -c web -- sh
```

**2. 在容器中查看当前路径**

```bash
kubectl exec demo-web -n demo -- pwd
```

**3. 查看指定容器运行身份**

```bash
kubectl exec demo-web -n demo -c web -- id
```

## 边界与易混淆点

容器必须运行且包含目标程序；容器命令可能修改挂载数据，脚本中不要无条件使用 -t。
