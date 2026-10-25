# docker compose up 检索说明

## 用途与查询表达

创建并启动 Compose 应用的服务容器。适用实现：Docker Compose 插件（docker compose）。

- 启动 Compose 项目。
- 构建后启动多容器应用。
- 只启动一个服务。

## 参数与行为

- `-d`：在后台运行。
- `--build`：启动前构建镜像。
- `--no-deps`：不启动依赖服务。
- `--wait`：等待服务达到运行或健康状态。

## 常见任务示例

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

## 边界与易混淆点

需在正确项目和配置文件中执行；配置变化可能重建容器，--wait 对健康检查的判断依赖服务配置。
