## kubectl get

列出 Kubernetes 资源或读取指定资源。

### 常用参数

- `-n NAMESPACE`：指定命名空间。
- `-A`：查询所有命名空间。
- `-o FORMAT`：指定 wide、json 或 yaml 等输出。
- `-l SELECTOR`：按标签筛选。
- `-w`：持续观察变化。

### 常用例子

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
