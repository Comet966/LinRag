## docker pull

从镜像仓库拉取镜像到本地。

### 常用参数

- `--platform PLATFORM`：选择目标平台。
- `--all-tags`：拉取仓库内全部标签。
- `--quiet`：减少输出。

### 常用例子

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
