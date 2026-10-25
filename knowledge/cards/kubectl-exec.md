## kubectl exec

在 Kubernetes Pod 的运行中容器内执行命令。

### 常用参数

- `-i`：保持标准输入。
- `-t`：分配伪终端。
- `-c NAME`：指定容器。
- `-n NAMESPACE`：指定命名空间。
- `--`：分隔 kubectl 选项和容器命令。

### 常用例子

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
