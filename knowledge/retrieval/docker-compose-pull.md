# docker compose pull 检索说明

## 用途与查询表达

拉取 Compose 服务引用的镜像。适用实现：Docker Compose 插件（docker compose）。

- 更新 Compose 镜像。
- 拉取服务依赖镜像。
- 下载多容器项目镜像。

## 参数与行为

- `--include-deps`：包括所选服务的依赖。
- `--policy POLICY`：选择 missing 或 always 拉取策略。
- `--quiet`：减少进度输出。

## 常见任务示例

**1. 拉取项目服务镜像**

```bash
docker compose pull
```

**2. 拉取 web 及其依赖镜像**

```bash
docker compose pull --include-deps web
```

**3. 按始终拉取策略更新镜像**

```bash
docker compose pull --policy always
```

## 边界与易混淆点

只拉取镜像，不自动重新创建或启动现有服务容器；项目中仅构建的服务可能需要使用 build。
