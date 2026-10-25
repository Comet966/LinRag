## docker compose exec

在已运行的 Compose 服务容器中执行命令。

### 常用参数

- `-T`：禁用伪终端。
- `--index N`：选择服务的第 N 个容器。
- `-u USER`：设置执行用户。
- `-w DIR`：设置容器内工作目录。

### 常用例子

**1. 进入 web 服务的 shell**

```bash
docker compose exec web sh
```

**2. 在自动化脚本中查看当前路径**

```bash
docker compose exec -T web pwd
```

**3. 在第二个 web 容器查看身份**

```bash
docker compose exec --index 2 web id
```
