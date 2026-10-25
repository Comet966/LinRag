# kubectl 检索说明

## 用途与查询表达

访问和管理 Kubernetes 集群资源的命令行工具。适用实现：kubectl / Kubernetes。

- Kubernetes 常用命令。
- 检查 kubectl 连接哪个集群。
- 查看 kubeconfig 上下文。

## 参数与行为

- `--context NAME`：选择 kubeconfig 上下文。
- `--namespace NAME`：指定命名空间。
- `--kubeconfig FILE`：指定配置文件。

## 常见任务示例

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

## 边界与易混淆点

多数子命令依赖可访问的集群及 RBAC 权限；操作前核对上下文与命名空间，客户端与服务端版本也需兼容。
