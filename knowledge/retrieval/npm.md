# npm 检索说明

## 用途与查询表达

管理 Node.js 项目的软件包、依赖和脚本。适用实现：npm CLI。

- Node.js 包管理。
- npm 常用命令。
- 查看 JavaScript 项目脚本。

## 参数与行为

- `--version`：显示 npm 版本。
- `--help`：显示帮助。
- `--prefix DIR`：在指定目录运行相关命令。

## 常见任务示例

**1. 查看 npm 版本**

```bash
npm --version
```

**2. 查看可用命令**

```bash
npm --help
```

**3. 查看当前项目定义的脚本**

```bash
npm run
```

## 边界与易混淆点

npm 通常随 Node.js 分发；项目可能要求特定 Node/npm 版本，操作前检查 package.json 和现有锁文件。
