# helm template 检索说明

## 用途与查询表达

在本地渲染 Chart 为 Kubernetes YAML。适用实现：Helm 3/4 基础操作。

- 本地渲染 Helm 模板。
- 查看 Chart 生成的 YAML。
- 不用安装预览 Helm 资源。

## 参数与行为

- `-f FILE`：读取 values 文件。
- `--set KEY=VALUE`：覆盖配置值。
- `--namespace NAME`：设置渲染用命名空间。
- `--debug`：显示诊断信息。

## 常见任务示例

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

## 边界与易混淆点

默认本地渲染不安装资源，也不代表清单已通过目标集群 API 校验；模板结果可能包含 Secret，避免直接公开。
