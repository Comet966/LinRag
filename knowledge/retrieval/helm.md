# helm 检索说明

## 用途与查询表达

使用 Chart 管理 Kubernetes 应用的模板与发布。适用实现：Helm 3/4 基础操作。

- Helm Chart 工具。
- Helm 常用命令。
- 查看 Helm 环境。

## 参数与行为

- `--namespace NAME`：设置操作命名空间。
- `--kube-context NAME`：选择 kubeconfig 上下文。
- `--help`：显示帮助。

## 常见任务示例

**1. 查看 Helm 版本**

```bash
helm version
```

**2. 查看客户端环境配置**

```bash
helm env
```

**3. 查看可用命令**

```bash
helm --help
```

## 边界与易混淆点

本轮覆盖 Helm 3/4 的常用基础操作；具体标志和默认行为取决于版本，访问集群前核对上下文与命名空间。
