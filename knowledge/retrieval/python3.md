# python3 检索说明

## 用途与查询表达

运行 Python 3 程序、模块或交互解释器。适用实现：Python 3。

- 运行 Python 脚本。
- 创建 Python 虚拟环境。
- Python 检查 JSON。

## 参数与行为

- `-V`：显示解释器版本。
- `-m MODULE`：按模块名运行。
- `-c CODE`：运行给定代码。
- `-u`：使用无缓冲的标准输出和错误。

## 常见任务示例

**1. 查看 Python 版本**

```bash
python3 -V
```

**2. 在新目录创建虚拟环境**

```bash
python3 -m venv .venv-demo
```

**3. 格式化并检查 JSON**

```bash
python3 -m json.tool data.json
```

## 边界与易混淆点

python3 的版本和可用模块取决于本机安装；venv 会创建目录，不会自动激活环境，部分系统需另装 venv 支持。
