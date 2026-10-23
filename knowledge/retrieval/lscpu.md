# lscpu 检索说明

## 用途与查询表达

显示 CPU 架构和拓扑信息。适用实现：util-linux。

- 查看 CPU 信息。
- 查看核心数和线程数。
- 查看 CPU 缓存。
- 查看 NUMA 拓扑。

## 参数与行为

- `-e`：表格显示 CPU 拓扑。
- `-p`：输出可解析格式。
- `-a`：包含离线 CPU。
- `-J`：输出 JSON。
- `-C`：显示缓存信息。

## 常见任务示例

**1. 查看 CPU 架构和缓存**

```bash
lscpu
```

**2. 查看逻辑 CPU 拓扑**

```bash
lscpu -e
```

## 边界与易混淆点

`CPU(s)` 是逻辑 CPU 数；物理核数看 `Core(s) per socket` 和 `Socket(s)`。
