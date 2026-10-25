## npm list

显示项目已安装依赖的树状关系。

### 常用参数

- `--depth N`：限制展示深度。
- `--all`：显示完整依赖树。
- `--json`：输出 JSON。
- `--global`：查看全局依赖。

### 常用例子

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
