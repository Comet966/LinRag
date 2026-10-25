# npm list 检索说明

## 用途与查询表达

显示项目已安装依赖的树状关系。适用实现：npm CLI。

- 查看 npm 依赖树。
- 列出 Node 全局包。
- 检查 npm 缺失依赖。

## 参数与行为

- `--depth N`：限制展示深度。
- `--all`：显示完整依赖树。
- `--json`：输出 JSON。
- `--global`：查看全局依赖。

## 常见任务示例

**1. 查看直接依赖**

```bash
npm list --depth 0
```

**2. 查看全局安装包**

```bash
npm list --global --depth 0
```

**3. 以 JSON 检查依赖树**

```bash
npm list --json
```

## 边界与易混淆点

别名为 npm ls；缺失、无效或多余依赖可能导致非零退出，命令本身不负责修复安装。
