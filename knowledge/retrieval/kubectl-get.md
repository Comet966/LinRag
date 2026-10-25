# kubectl get 检索说明

## 用途与查询表达

列出 Kubernetes 资源或读取指定资源。适用实现：kubectl / Kubernetes。

- 查看 K8s Pod。
- 列出 Kubernetes 资源。
- 按命名空间查看服务。

## 参数与行为

- `-n NAMESPACE`：指定命名空间。
- `-A`：查询所有命名空间。
- `-o FORMAT`：指定 wide、json 或 yaml 等输出。
- `-l SELECTOR`：按标签筛选。
- `-w`：持续观察变化。

## 常见任务示例

**1. 查看某命名空间的 Pod**

```bash
kubectl get pods -n demo
```

**2. 跨命名空间查看 Pod 所在节点**

```bash
kubectl get pods -A -o wide
```

**3. 以 YAML 查看指定 Deployment**

```bash
kubectl get deployment demo-web -n demo -o yaml
```

## 边界与易混淆点

读取当前上下文的资源；输出 Secret 或完整 YAML 时可能含敏感配置，不要直接公开。
