## docker run

从镜像创建并启动一个新容器。

### 常用参数

- `-d`：在后台运行。
- `--name NAME`：指定容器名。
- `--rm`：退出后自动移除容器。
- `-it`：保持标准输入并分配终端。
- `-p HOST:CONTAINER`：发布端口。
- `--mount SPEC`：配置挂载。

### 常用例子

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
