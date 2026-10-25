# pip 检索说明

## 用途与查询表达

安装和管理指定 Python 环境中的软件包。适用实现：pip（示例通过 Python 3 调用）。

- Python 包管理工具。
- pip 对应哪个 Python。
- 查看 pip 版本。

## 参数与行为

- `--version`：显示版本及所属环境路径。
- `--help`：显示帮助。
- `--isolated`：忽略环境变量和用户配置。

## 常见任务示例

**1. 查看当前解释器的 pip**

```bash
python3 -m pip --version
```

**2. 查看 pip 命令帮助**

```bash
python3 -m pip --help
```

**3. 检查当前环境的依赖兼容性**

```bash
python3 -m pip check
```

## 边界与易混淆点

示例优先采用 python3 -m pip，避免 pip 可执行文件绑定到其他解释器；虚拟环境中的解释器需按实际路径选择。
