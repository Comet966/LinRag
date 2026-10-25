## kubectl apply

根据资源清单创建或更新 Kubernetes 对象。

### 常用参数

- `-f FILE`：读取清单文件或目录。
- `-k DIR`：读取 Kustomize 目录。
- `--dry-run=server`：请求服务器校验而不持久化对象。
- `--dry-run=client`：在客户端生成结果而不提交变更。

### 常用例子

**1. 在服务端预检清单**

```bash
kubectl apply --dry-run=server -f deployment.yaml
```

**2. 在客户端生成预览 YAML**

```bash
kubectl apply --dry-run=client -f deployment.yaml -o yaml
```

**3. 预检 Kustomize 目录**

```bash
kubectl apply --dry-run=server -k overlays/dev/
```
