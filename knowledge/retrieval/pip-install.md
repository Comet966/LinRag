# pip install 检索说明

## 用途与查询表达

向 Python 环境安装软件包或项目依赖。适用实现：pip（示例通过 Python 3 调用）。

- 安装 Python 依赖。
- pip 安装 requirements。
- 可编辑安装 Python 项目。

## 参数与行为

- `-r FILE`：从需求文件安装。
- `-e PATH`：以可编辑方式安装本地项目。
- `--upgrade`：升级指定包及必要依赖。
- `--dry-run`：解析安装计划但不安装。

## 常见任务示例

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

## 边界与易混淆点

前两个例子假设虚拟环境已创建且包含 pip；解析或构建包可能执行构建代码，dry-run 不保证完全不访问网络或不运行准备步骤，避免改动系统环境。
