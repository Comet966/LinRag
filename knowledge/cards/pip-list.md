## pip list

列出 Python 环境中已经安装的软件包。

### 常用参数

- `--format FORMAT`：指定 columns、freeze 或 json 输出。
- `--outdated`：列出有新版本的包。
- `--local`：在可访问全局包的虚拟环境中只列本地包。

### 常用例子

**1. 查看安装的软件包**

```bash
python3 -m pip list
```

**2. 输出 JSON 包列表**

```bash
python3 -m pip list --format json
```

**3. 检查可升级的包**

```bash
python3 -m pip list --outdated
```
