# docker ps 检索说明

## 用途与查询表达

列出容器及运行状态。适用实现：Docker CLI / Docker Engine。

- 查看 Docker 容器。
- 列出已退出容器。
- docker container ls。

## 参数与行为

- `-a`：包括已停止的容器。
- `-q`：只显示容器 ID。
- `--filter FILTER`：筛选容器。
- `--format FORMAT`：设置输出格式。

## 常见任务示例

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

## 边界与易混淆点

默认只显示运行中的容器，是 docker container ls 的别名；不会启动或停止容器。
