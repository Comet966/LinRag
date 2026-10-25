# kubectl apply 检索说明

## 用途与查询表达

根据资源清单创建或更新 Kubernetes 对象。适用实现：kubectl / Kubernetes。

- 校验 Kubernetes YAML。
- 应用 K8s 部署清单。
- Kustomize 部署预览。

## 参数与行为

- `-f FILE`：读取清单文件或目录。
- `-k DIR`：读取 Kustomize 目录。
- `--dry-run=server`：请求服务器校验而不持久化对象。
- `--dry-run=client`：在客户端生成结果而不提交变更。

## 常见任务示例

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

## 边界与易混淆点

本卡片示例只预检；client 模式仍可能查询集群发现或校验信息，不保证离线。去掉 dry-run 会实际修改资源，server 预检也需要访问目标集群。
