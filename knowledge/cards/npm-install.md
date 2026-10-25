## npm install

安装 Node.js 项目依赖或添加指定软件包。

### 常用参数

- `--save-dev`：记录为开发依赖。
- `--global`：安装到全局环境。
- `--ignore-scripts`：不执行依赖安装生命周期脚本。
- `--package-lock-only`：只更新锁文件而不安装依赖。

### 常用例子

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
