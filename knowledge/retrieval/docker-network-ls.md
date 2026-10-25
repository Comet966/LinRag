# docker network ls 检索说明

## 用途与查询表达

列出 Docker 网络。适用实现：Docker CLI / Docker Engine。

- 查看 Docker 网络。
- 列出 bridge 网络。
- 检查容器网络列表。

## 参数与行为

- `--filter FILTER`：按条件筛选。
- `--format FORMAT`：设置输出格式。
- `-q`：只输出网络 ID。

## 常见任务示例

**1. 列出容器网络**

```bash
docker network ls
```

**2. 筛选 bridge 驱动网络**

```bash
docker network ls --filter driver=bridge
```

**3. 只显示网络 ID**

```bash
docker network ls -q
```

## 边界与易混淆点

此命令列举网络，查看具体连接对象需进一步使用 docker network inspect。
