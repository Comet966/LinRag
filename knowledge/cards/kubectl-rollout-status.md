## kubectl rollout status

等待并查看某个工作负载的滚动发布状态。

### 常用参数

- `--timeout DURATION`：限制等待时间。
- `--watch=false`：只读取当前状态。
- `--revision N`：关注指定修订版本。
- `-n NAMESPACE`：指定命名空间。

### 常用例子

**1. 等待 Deployment 发布完成**

```bash
kubectl rollout status deployment/demo-web -n demo --timeout=120s
```

**2. 只读取当前发布状态**

```bash
kubectl rollout status deployment/demo-web -n demo --watch=false
```

**3. 检查 StatefulSet 的发布**

```bash
kubectl rollout status statefulset/demo-db -n demo --timeout=120s
```
