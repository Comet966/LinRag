# docker compose exec 检索说明

## 用途与查询表达

在已运行的 Compose 服务容器中执行命令。适用实现：Docker Compose 插件（docker compose）。

- 进入 Compose 服务容器。
- Compose exec 在脚本中执行。
- 选择服务副本。

## 参数与行为

- `-T`：禁用伪终端。
- `--index N`：选择服务的第 N 个容器。
- `-u USER`：设置执行用户。
- `-w DIR`：设置容器内工作目录。

## 常见任务示例

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

## 边界与易混淆点

服务需已运行；与 docker exec 不同，Compose exec 默认分配终端，脚本中常用 -T。
