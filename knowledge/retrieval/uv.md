# uv 检索说明

## 用途与查询表达

管理 Python 项目、依赖、虚拟环境和工具。适用实现：uv 项目工作流。

- uv Python 项目管理。
- 查看 uv 工具用法。
- uv 和 pip 区别。

## 参数与行为

- `--version`：显示版本。
- `--help`：显示帮助。
- `--offline`：禁用网络访问。

## 常见任务示例

**1. 查看 uv 版本**

```bash
uv --version
```

**2. 查看命令帮助**

```bash
uv --help
```

**3. 在项目环境中运行 Python**

```bash
uv run python --version
```

## 边界与易混淆点

不同子命令管理的环境和清单范围不同；uv run/sync 可能自动创建环境并检查锁文件，offline 仍需本地所需资源齐全。
