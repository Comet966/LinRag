## helm upgrade

用新的 Chart 或配置更新已有 Helm 发布。

### 常用参数

- `--install`：发布不存在时转为安装。
- `-f FILE`：读取 values 文件。
- `--set KEY=VALUE`：覆盖配置值。
- `--reuse-values`：合并复用上次发布值。
- `--dry-run=client`：只模拟升级。

### 常用例子

**1. 模拟用当前 Chart 升级发布**

```bash
helm upgrade demo-web ./chart -n demo --dry-run=client
```

**2. 读取新配置模拟升级**

```bash
helm upgrade demo-web ./chart -n demo -f values-dev.yaml --dry-run=client
```

**3. 模拟不存在时安装或已有时升级**

```bash
helm upgrade --install demo-web ./chart -n demo --dry-run=client
```
