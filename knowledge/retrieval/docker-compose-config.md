# docker compose config 检索说明

## 用途与查询表达

解析、合并和校验 Compose 配置。适用实现：Docker Compose 插件（docker compose）。

- 校验 Compose 配置。
- 查看展开后的配置。
- 列出 Compose 服务名称。

## 参数与行为

- `-q`：仅校验，不打印配置。
- `--services`：列出服务名。
- `--images`：列出镜像名称。
- `--no-interpolate`：不进行环境变量插值。

## 常见任务示例

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

## 边界与易混淆点

不启动服务；完整输出会解析环境变量且可能包含敏感值，默认示例优先使用 quiet 或仅列出名称。
