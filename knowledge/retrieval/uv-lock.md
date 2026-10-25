# uv lock 检索说明

## 用途与查询表达

解析项目依赖并创建或更新 uv.lock。适用实现：uv 项目工作流。

- 生成 uv.lock。
- 校验 uv 锁文件。
- 只升级一个锁定依赖。

## 参数与行为

- `--check`：只检查锁文件是否最新。
- `--upgrade`：允许升级所有锁定依赖。
- `--upgrade-package NAME`：允许升级指定包。

## 常见任务示例

**1. 生成或刷新锁文件**

```bash
uv lock
```

**2. 检查清单与锁文件一致性**

```bash
uv lock --check
```

**3. 仅为指定包允许升级**

```bash
uv lock --upgrade-package httpx
```

## 边界与易混淆点

默认尽量保留满足约束的现有版本，不等同于升级全部包；lock 只管理锁文件，不负责把项目环境同步到新版本。
