## docker images

列出本地镜像及其标签和大小。

### 常用参数

- `-a`：显示全部镜像。
- `-q`：只输出镜像 ID。
- `--digests`：显示镜像摘要。
- `--filter FILTER`：按条件筛选。

### 常用例子

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
