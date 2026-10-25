# npm ci 检索说明

## 用途与查询表达

根据现有锁文件执行干净的项目依赖安装。适用实现：npm CLI。

- CI 安装 npm 依赖。
- 按 package-lock 精确安装。
- npm ci 锁文件不一致。

## 参数与行为

- `--ignore-scripts`：不执行安装生命周期脚本。
- `--omit=dev`：不将开发依赖安装到磁盘。
- `--no-audit`：安装时不提交审计请求。

## 常见任务示例

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

## 边界与易混淆点

要求 package-lock.json 或 npm-shrinkwrap.json 与清单匹配；会移除已有 node_modules 后安装，不会自动修正锁文件不一致。
