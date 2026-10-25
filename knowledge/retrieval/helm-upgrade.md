# helm upgrade 检索说明

## 用途与查询表达

用新的 Chart 或配置更新已有 Helm 发布。适用实现：Helm 3/4 基础操作。

- 升级 Helm 应用。
- Helm upgrade install。
- 预览 Chart 更新。

## 参数与行为

- `--install`：发布不存在时转为安装。
- `-f FILE`：读取 values 文件。
- `--set KEY=VALUE`：覆盖配置值。
- `--reuse-values`：合并复用上次发布值。
- `--dry-run=client`：只模拟升级。

## 常见任务示例

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

## 边界与易混淆点

去掉 dry-run 会修改资源并可能触发 hooks；values 的复用与重置会影响结果，升级前核对目标发布和最终配置。
