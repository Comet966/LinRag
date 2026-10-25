## kubectl

访问和管理 Kubernetes 集群资源的命令行工具。

### 常用参数

- `--context NAME`：选择 kubeconfig 上下文。
- `--namespace NAME`：指定命名空间。
- `--kubeconfig FILE`：指定配置文件。

### 常用例子

**1. 查看客户端版本**

```bash
kubectl version --client
```

**2. 核对当前上下文**

```bash
kubectl config current-context
```

**3. 列出配置中的上下文**

```bash
kubectl config get-contexts
```
