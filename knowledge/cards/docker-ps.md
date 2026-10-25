## docker ps

列出容器及运行状态。

### 常用参数

- `-a`：包括已停止的容器。
- `-q`：只显示容器 ID。
- `--filter FILTER`：筛选容器。
- `--format FORMAT`：设置输出格式。

### 常用例子

**1. 列出运行中的容器**

```bash
docker ps
```

**2. 包括已停止容器**

```bash
docker ps -a
```

**3. 查找指定名称的容器**

```bash
docker ps --filter name=demo-web
```
