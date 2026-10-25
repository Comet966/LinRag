## docker compose ps

查看 Compose 项目的服务容器状态。

### 常用参数

- `-a`：包括已停止的容器。
- `--services`：只列出服务名。
- `--format FORMAT`：指定输出格式。
- `-q`：只列出容器 ID。

### 常用例子

**1. 查看项目运行状态**

```bash
docker compose ps
```

**2. 包括已经退出的服务**

```bash
docker compose ps -a
```

**3. 以 JSON 查看服务状态**

```bash
docker compose ps --format json
```
