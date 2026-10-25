# docker rm 检索说明

## 用途与查询表达

删除已有容器及其可写层。适用实现：Docker CLI / Docker Engine。

- 删除停止容器。
- 移除 Docker 容器。
- 删除容器会不会删除卷。

## 参数与行为

- `-f`：强制删除运行中的容器。
- `-v`：同时删除关联的匿名数据卷。
- `--help`：显示帮助。

## 常见任务示例

**1. 先核对停止容器**

```bash
docker ps -a --filter status=exited
```

**2. 查看删除命令帮助**

```bash
docker rm --help
```

**3. 删除前检查指定容器挂载**

```bash
docker inspect --format '{{json .Mounts}}' demo-web
```

## 边界与易混淆点

本卡片例子仅做删除前检查；实际 rm 会丢失容器可写层，-f 会中断运行，-v 可能删除匿名卷数据。
