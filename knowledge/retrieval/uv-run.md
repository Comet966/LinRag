# uv run 检索说明

## 用途与查询表达

在项目环境或指定环境中运行命令或 Python 脚本。适用实现：uv 项目工作流。

- 使用 uv 运行 Python。
- 在项目环境运行测试。
- uv run 不同步环境。

## 参数与行为

- `--locked`：锁文件过期时拒绝更新。
- `--frozen`：不更新和检查锁文件。
- `--no-sync`：不执行环境同步。
- `--with PACKAGE`：运行时额外提供依赖。

## 常见任务示例

**1. 在项目环境运行脚本**

```bash
uv run python app.py
```

**2. 使用最新锁文件约束运行测试**

```bash
uv run --locked pytest -q
```

**3. 在不改变已建环境的情况下运行**

```bash
uv run --no-sync python --version
```

## 边界与易混淆点

默认可能先解析依赖、更新锁文件和同步环境；no-sync 假设环境已可用，不保证依赖与清单一致。
