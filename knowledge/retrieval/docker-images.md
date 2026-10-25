# docker images 检索说明

## 用途与查询表达

列出本地镜像及其标签和大小。适用实现：Docker CLI / Docker Engine。

- 查看本地镜像。
- 列出 Docker 镜像大小。
- docker image ls。

## 参数与行为

- `-a`：显示全部镜像。
- `-q`：只输出镜像 ID。
- `--digests`：显示镜像摘要。
- `--filter FILTER`：按条件筛选。

## 常见任务示例

**1. 列出本地镜像**

```bash
docker images
```

**2. 显示本地镜像摘要**

```bash
docker images --digests
```

**3. 筛选某个仓库的镜像**

```bash
docker images --filter 'reference=nginx:*'
```

## 边界与易混淆点

是 docker image ls 的别名；列出的是当前 Engine 的本地镜像，不是远程仓库全部标签。
