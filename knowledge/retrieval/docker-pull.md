# docker pull 检索说明

## 用途与查询表达

从镜像仓库拉取镜像到本地。适用实现：Docker CLI / Docker Engine。

- 下载 Docker 镜像。
- 拉取指定架构镜像。
- 更新本地镜像。

## 参数与行为

- `--platform PLATFORM`：选择目标平台。
- `--all-tags`：拉取仓库内全部标签。
- `--quiet`：减少输出。

## 常见任务示例

**1. 拉取指定 Alpine 版本**

```bash
docker pull alpine:3.21
```

**2. 拉取指定平台镜像**

```bash
docker pull --platform linux/amd64 nginx:stable
```

**3. 减少拉取进度输出**

```bash
docker pull --quiet alpine:3.21
```

## 边界与易混淆点

会访问镜像仓库并占用存储；标签可能随时间变化，精确复现应使用已核对的镜像摘要。
