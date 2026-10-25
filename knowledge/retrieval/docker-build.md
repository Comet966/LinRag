# docker build 检索说明

## 用途与查询表达

根据 Dockerfile 和构建上下文构建镜像。适用实现：Docker CLI / Docker Engine。

- 构建 Docker 镜像。
- 指定 Dockerfile。
- 镜像构建不用缓存。

## 参数与行为

- `-t NAME:TAG`：设置镜像名称和标签。
- `-f FILE`：指定 Dockerfile。
- `--no-cache`：不复用构建缓存。
- `--build-arg KEY=VALUE`：传入构建参数。

## 常见任务示例

**1. 构建当前目录镜像**

```bash
docker build -t demo:local .
```

**2. 使用指定 Dockerfile**

```bash
docker build -f Dockerfile.dev -t demo:dev .
```

**3. 不复用缓存重新构建**

```bash
docker build --no-cache -t demo:clean .
```

## 边界与易混淆点

构建会执行 Dockerfile 中的指令，先核对构建上下文和脚本；不要用 build-arg 传递敏感凭据。
