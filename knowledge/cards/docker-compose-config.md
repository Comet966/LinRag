## docker compose config

解析、合并和校验 Compose 配置。

### 常用参数

- `-q`：仅校验，不打印配置。
- `--services`：列出服务名。
- `--images`：列出镜像名称。
- `--no-interpolate`：不进行环境变量插值。

### 常用例子

**1. 检查 Compose 文件语法与一致性**

```bash
docker compose config --quiet
```

**2. 列出配置中的服务**

```bash
docker compose config --services
```

**3. 列出引用的镜像**

```bash
docker compose config --images
```
