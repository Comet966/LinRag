## kubectl describe

查看资源详情、状态和关联事件的可读摘要。

### 常用参数

- `-n NAMESPACE`：指定命名空间。
- `-l SELECTOR`：按标签选择资源。
- `--show-events=false`：不显示关联事件。

### 常用例子

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
