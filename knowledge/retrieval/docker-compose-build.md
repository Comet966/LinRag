# docker compose build 检索说明

## 用途与查询表达

根据 Compose 配置构建服务镜像。适用实现：Docker Compose 插件（docker compose）。

- 构建 Compose 镜像。
- 只构建一个服务。
- Compose 构建刷新基础镜像。

## 参数与行为

- `--no-cache`：不使用构建缓存。
- `--pull`：尝试拉取较新的基础镜像。
- `--build-arg KEY=VALUE`：设置构建参数。

## 常见任务示例

**1. 构建全部配置了 build 的服务**

```bash
docker compose build
```

**2. 只构建 web 服务**

```bash
docker compose build web
```

**3. 更新基础镜像后不复用缓存构建**

```bash
docker compose build --pull --no-cache web
```

## 边界与易混淆点

只构建，不负责启动容器；基础镜像更新和构建指令会影响结果，不要用普通构建参数传递密钥。
