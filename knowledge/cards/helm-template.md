## helm template

在本地渲染 Chart 为 Kubernetes YAML。

### 常用参数

- `-f FILE`：读取 values 文件。
- `--set KEY=VALUE`：覆盖配置值。
- `--namespace NAME`：设置渲染用命名空间。
- `--debug`：显示诊断信息。

### 常用例子

**1. 渲染本地 Chart**

```bash
helm template demo-web ./chart
```

**2. 用开发配置渲染**

```bash
helm template demo-web ./chart -f values-dev.yaml
```

**3. 渲染指定命名空间和副本数**

```bash
helm template demo-web ./chart --namespace demo --set replicaCount=2
```
