## docker compose run

为某个 Compose 服务创建一次性任务容器。

### 常用参数

- `--rm`：任务结束后移除容器。
- `--no-deps`：不启动依赖服务。
- `--service-ports`：发布服务配置的端口。
- `-T`：禁用伪终端。

### 常用例子

**1. 执行一次性命令并清理任务容器**

```bash
docker compose run --rm web echo hello
```

**2. 不启动依赖地执行一次性命令**

```bash
docker compose run --rm --no-deps web pwd
```

**3. 为自动化任务禁用终端**

```bash
docker compose run --rm -T web id
```
