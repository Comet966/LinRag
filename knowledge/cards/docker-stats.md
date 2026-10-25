## docker stats

查看容器的 CPU、内存和网络资源统计。

### 常用参数

- `--no-stream`：仅输出一次。
- `--all`：包括所有容器。
- `--format FORMAT`：设置输出格式。

### 常用例子

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
