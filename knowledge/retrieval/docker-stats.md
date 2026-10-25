# docker stats 检索说明

## 用途与查询表达

查看容器的 CPU、内存和网络资源统计。适用实现：Docker CLI / Docker Engine。

- 容器内存占用。
- Docker CPU 使用率。
- 查看容器资源消耗。

## 参数与行为

- `--no-stream`：仅输出一次。
- `--all`：包括所有容器。
- `--format FORMAT`：设置输出格式。

## 常见任务示例

**1. 实时查看容器资源**

```bash
docker stats
```

**2. 读取指定容器的一次统计**

```bash
docker stats --no-stream demo-web
```

**3. 读取所有容器的一次统计**

```bash
docker stats --no-stream --all
```

## 边界与易混淆点

指标来自当前 Engine，内存显示与平台和缓存统计有关，不是应用内部的内存分析器。
