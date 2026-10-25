## docker compose build

根据 Compose 配置构建服务镜像。

### 常用参数

- `--no-cache`：不使用构建缓存。
- `--pull`：尝试拉取较新的基础镜像。
- `--build-arg KEY=VALUE`：设置构建参数。

### 常用例子

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
