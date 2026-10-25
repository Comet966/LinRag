# kubectl describe 检索说明

## 用途与查询表达

查看资源详情、状态和关联事件的可读摘要。适用实现：kubectl / Kubernetes。

- 排查 Pod Pending。
- 查看 Pod 调度事件。
- Kubernetes 镜像拉取失败排查。

## 参数与行为

- `-n NAMESPACE`：指定命名空间。
- `-l SELECTOR`：按标签选择资源。
- `--show-events=false`：不显示关联事件。

## 常见任务示例

**1. 排查 Pod 状态与事件**

```bash
kubectl describe pod demo-web -n demo
```

**2. 查看 Deployment 的副本信息**

```bash
kubectl describe deployment demo-web -n demo
```

**3. 按标签查看 Pod 详情**

```bash
kubectl describe pods -n demo -l app=demo-web
```

## 边界与易混淆点

describe 展示资源摘要和事件，不代替容器日志；Pod 名称需要替换为实际名称，事件有保留期限。
