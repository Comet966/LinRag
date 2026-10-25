## helm install

从 Chart 创建一个新的 Helm 发布。

### 常用参数

- `-f FILE`：读取 values 文件。
- `--set KEY=VALUE`：覆盖配置值。
- `--namespace NAME`：指定命名空间。
- `--create-namespace`：创建缺失命名空间。
- `--dry-run=client`：只模拟安装而不执行集群变更。

### 常用例子

**1. 本地模拟安装 Chart**

```bash
helm install demo-web ./chart --dry-run=client
```

**2. 使用开发配置模拟安装**

```bash
helm install demo-web ./chart -f values-dev.yaml --dry-run=client
```

**3. 覆盖副本数模拟安装**

```bash
helm install demo-web ./chart --set replicaCount=2 --dry-run=client
```
