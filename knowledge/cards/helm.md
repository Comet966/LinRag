## helm

使用 Chart 管理 Kubernetes 应用的模板与发布。

### 常用参数

- `--namespace NAME`：设置操作命名空间。
- `--kube-context NAME`：选择 kubeconfig 上下文。
- `--help`：显示帮助。

### 常用例子

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
