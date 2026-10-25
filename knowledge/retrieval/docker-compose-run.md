# docker compose run 检索说明

## 用途与查询表达

为某个 Compose 服务创建一次性任务容器。适用实现：Docker Compose 插件（docker compose）。

- 运行 Compose 一次性任务。
- Compose run 与 exec 区别。
- 执行临时服务命令。

## 参数与行为

- `--rm`：任务结束后移除容器。
- `--no-deps`：不启动依赖服务。
- `--service-ports`：发布服务配置的端口。
- `-T`：禁用伪终端。

## 常见任务示例

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

## 边界与易混淆点

run 创建新容器，exec 在已有服务容器执行；run 默认不发布服务端口，命令可能修改挂载目录或数据库。
