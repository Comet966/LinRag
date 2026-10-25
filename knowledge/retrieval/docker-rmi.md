# docker rmi 检索说明

## 用途与查询表达

删除本地镜像或取消镜像标签。适用实现：Docker CLI / Docker Engine。

- 删除本地镜像。
- 移除 Docker 镜像标签。
- docker image rm。

## 参数与行为

- `-f`：强制删除。
- `--no-prune`：不删除未标记的父镜像。
- `--help`：显示帮助。

## 常见任务示例

**1. 删除前核对镜像**

```bash
docker images --digests
```

**2. 查看删除镜像帮助**

```bash
docker rmi --help
```

**3. 检查目标镜像**

```bash
docker image inspect demo:local
```

## 边界与易混淆点

本卡片只提供检查例子；删除标签不一定释放共享层，实际删除可能影响依赖镜像的后续启动。
