# which 检索说明

## 用途与查询表达

在 PATH 中查找可执行命令的位置。适用实现：GNU which。

- 命令安装在哪里。
- 多个 Python 路径。
- 查可执行文件位置。

## 参数与行为

- `-a`：列出 PATH 中所有匹配的可执行文件。

## 常见任务示例

**1. 查看 PATH 中可找到的 python3 路径**

```bash
which -a python3
```

**2. 检查 curl 是否能通过当前 PATH 找到**

```bash
which curl
```

## 边界与易混淆点

which 实现各异；这里采用 GNU which 的 -a。shell 别名、函数和内建命令的解析应结合 type 或 command -v。
