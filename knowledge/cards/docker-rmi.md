## docker rmi

删除本地镜像或取消镜像标签。

### 常用参数

- `-f`：强制删除。
- `--no-prune`：不删除未标记的父镜像。
- `--help`：显示帮助。

### 常用例子

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
