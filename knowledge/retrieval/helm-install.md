# helm install 检索说明

## 用途与查询表达

从 Chart 创建一个新的 Helm 发布。适用实现：Helm 3/4 基础操作。

- 安装 Helm Chart。
- 预览 Helm 安装清单。
- 通过 values 配置应用。

## 参数与行为

- `-f FILE`：读取 values 文件。
- `--set KEY=VALUE`：覆盖配置值。
- `--namespace NAME`：指定命名空间。
- `--create-namespace`：创建缺失命名空间。
- `--dry-run=client`：只模拟安装而不执行集群变更。

## 常见任务示例

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

## 边界与易混淆点

例子仅模拟安装，输出可能包含 Secret；去掉 dry-run 会创建集群资源，Chart hooks 也可能执行任务。检查本机版本对 dry-run 模式的支持。
