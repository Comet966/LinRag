# npm outdated 检索说明

## 用途与查询表达

检查项目依赖的已装、允许和最新版本。适用实现：npm CLI。

- 查看 npm 过期依赖。
- 比较 current wanted latest。
- 检查 JavaScript 包更新。

## 参数与行为

- `--global`：检查全局包。
- `--json`：输出 JSON。
- `--long`：增加包类型等信息。

## 常见任务示例

**1. 检查当前项目的可升级依赖**

```bash
npm outdated
```

**2. 以 JSON 查看版本差异**

```bash
npm outdated --json
```

**3. 检查全局包的新版本**

```bash
npm outdated --global
```

## 边界与易混淆点

通常访问注册表且不执行升级；wanted 受版本范围约束，latest 是注册表标签，不一定满足项目约束。
