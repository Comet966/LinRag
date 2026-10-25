## npm run

列出或执行 package.json 中定义的项目脚本。

### 常用参数

- `--`：把之后的参数传递给脚本。
- `--if-present`：未定义脚本时不因该原因报错。
- `--workspace NAME`：选择工作区。

### 常用例子

**1. 列出可用脚本**

```bash
npm run
```

**2. 执行已定义的构建脚本**

```bash
npm run build
```

**3. 向开发脚本传递参数**

```bash
npm run dev -- --port 3000
```
