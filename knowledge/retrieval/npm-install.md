# npm install 检索说明

## 用途与查询表达

安装 Node.js 项目依赖或添加指定软件包。适用实现：npm CLI。

- 安装 npm 依赖。
- 添加 JavaScript 开发依赖。
- npm install 和 ci 区别。

## 参数与行为

- `--save-dev`：记录为开发依赖。
- `--global`：安装到全局环境。
- `--ignore-scripts`：不执行依赖安装生命周期脚本。
- `--package-lock-only`：只更新锁文件而不安装依赖。

## 常见任务示例

**1. 按项目清单安装依赖**

```bash
npm install
```

**2. 添加一个开发依赖**

```bash
npm install --save-dev typescript
```

**3. 安装时禁用生命周期脚本**

```bash
npm install --ignore-scripts
```

## 边界与易混淆点

通常会修改 node_modules，指定包时还可能修改 package.json 和锁文件；默认可能执行脚本，仅在可信项目中安装。
