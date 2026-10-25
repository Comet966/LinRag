## pip freeze

按 requirements 格式输出当前环境的软件包版本。

### 常用参数

- `--all`：也包括默认省略的引导工具包。
- `--exclude NAME`：排除指定包。
- `--local`：只输出虚拟环境中的本地安装包。

### 常用例子

**1. 查看环境版本快照**

```bash
python3 -m pip freeze
```

**2. 包含引导工具包**

```bash
python3 -m pip freeze --all
```

**3. 排除某个工具包**

```bash
python3 -m pip freeze --exclude pip
```
