## npm ci

根据现有锁文件执行干净的项目依赖安装。

### 常用参数

- `--ignore-scripts`：不执行安装生命周期脚本。
- `--omit=dev`：不将开发依赖安装到磁盘。
- `--no-audit`：安装时不提交审计请求。

### 常用例子

**1. 按锁文件执行干净安装**

```bash
npm ci
```

**2. 仅安装非开发依赖**

```bash
npm ci --omit=dev
```

**3. 禁用生命周期脚本安装**

```bash
npm ci --ignore-scripts
```
