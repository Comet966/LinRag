# docker system df 检索说明

## 用途与查询表达

查看 Docker 对象的磁盘占用及可回收空间。适用实现：Docker CLI / Docker Engine。

- Docker 占用磁盘太大。
- 查看镜像缓存大小。
- 统计可回收空间。

## 参数与行为

- `-v`：显示更详细的对象占用。
- `--format FORMAT`：设置输出格式。

## 常见任务示例

**1. 查看 Docker 总体磁盘用量**

```bash
docker system df
```

**2. 查看镜像与容器占用详情**

```bash
docker system df -v
```

## 边界与易混淆点

只统计并展示，不执行清理；共享层导致各镜像大小不能简单相加，可回收不代表可以无条件删除。
