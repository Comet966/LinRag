# pip show 检索说明

## 用途与查询表达

显示已安装 Python 包的元数据和安装位置。适用实现：pip（示例通过 Python 3 调用）。

- Python 包安装在哪里。
- 查看 pip 包版本和依赖。
- 查看包包含的文件。

## 参数与行为

- `-f`：列出该包记录的已安装文件。
- `--help`：显示帮助。

## 常见任务示例

**1. 查看 requests 包信息**

```bash
python3 -m pip show requests
```

**2. 查看包记录的安装文件**

```bash
python3 -m pip show -f requests
```

**3. 同时查看多个包**

```bash
python3 -m pip show requests httpx
```

## 边界与易混淆点

只查询当前解释器环境中已安装的软件包，不会查询远程包的最新信息。
