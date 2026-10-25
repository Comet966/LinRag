## pip show

显示已安装 Python 包的元数据和安装位置。

### 常用参数

- `-f`：列出该包记录的已安装文件。
- `--help`：显示帮助。

### 常用例子

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
