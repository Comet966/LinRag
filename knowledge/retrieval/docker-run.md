# docker run 检索说明

## 用途与查询表达

从镜像创建并启动一个新容器。适用实现：Docker CLI / Docker Engine。

- 启动新容器。
- Docker 端口映射。
- 进入临时 Alpine 容器。

## 参数与行为

- `-d`：在后台运行。
- `--name NAME`：指定容器名。
- `--rm`：退出后自动移除容器。
- `-it`：保持标准输入并分配终端。
- `-p HOST:CONTAINER`：发布端口。
- `--mount SPEC`：配置挂载。

## 常见任务示例

**1. 运行一次性示例命令**

```bash
docker run --rm alpine:3.21 echo hello
```

**2. 进入临时容器的 shell**

```bash
docker run --rm -it alpine:3.21 sh
```

**3. 仅向回环地址发布 Web 端口**

```bash
docker run -d --name demo-web -p 127.0.0.1:8080:80 nginx:stable
```

## 边界与易混淆点

每次 run 都创建新容器；start 启动已有容器。挂载和权限会影响宿主机，示例端口只绑定回环地址。
