## pip install

向 Python 环境安装软件包或项目依赖。

### 常用参数

- `-r FILE`：从需求文件安装。
- `-e PATH`：以可编辑方式安装本地项目。
- `--upgrade`：升级指定包及必要依赖。
- `--dry-run`：解析安装计划但不安装。

### 常用例子

**1. 在虚拟环境中安装需求文件**

```bash
.venv/bin/python -m pip install -r requirements.txt
```

**2. 可编辑安装当前项目**

```bash
.venv/bin/python -m pip install -e .
```

**3. 预览一个包的安装计划**

```bash
.venv/bin/python -m pip install --dry-run requests
```
