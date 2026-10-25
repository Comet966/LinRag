# pip freeze 检索说明

## 用途与查询表达

按 requirements 格式输出当前环境的软件包版本。适用实现：pip（示例通过 Python 3 调用）。

- 导出 Python 依赖版本。
- 生成 requirements 格式。
- 记录虚拟环境包版本。

## 参数与行为

- `--all`：也包括默认省略的引导工具包。
- `--exclude NAME`：排除指定包。
- `--local`：只输出虚拟环境中的本地安装包。

## 常见任务示例

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

## 边界与易混淆点

freeze 记录已安装状态，不进行依赖求解，也不是跨平台完整锁文件；写入文件前确认不会覆盖已有需求文件。
