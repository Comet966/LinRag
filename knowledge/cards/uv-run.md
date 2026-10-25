## uv run

在项目环境或指定环境中运行命令或 Python 脚本。

### 常用参数

- `--locked`：锁文件过期时拒绝更新。
- `--frozen`：不更新和检查锁文件。
- `--no-sync`：不执行环境同步。
- `--with PACKAGE`：运行时额外提供依赖。

### 常用例子

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
