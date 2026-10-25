## docker compose up

创建并启动 Compose 应用的服务容器。

### 常用参数

- `-d`：在后台运行。
- `--build`：启动前构建镜像。
- `--no-deps`：不启动依赖服务。
- `--wait`：等待服务达到运行或健康状态。

### 常用例子

**1. 后台启动配置中的服务**

```bash
docker compose up -d
```

**2. 构建并后台启动**

```bash
docker compose up -d --build
```

**3. 启动 web 而不启动依赖**

```bash
docker compose up -d --no-deps web
```
