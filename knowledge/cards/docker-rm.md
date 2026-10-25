## docker rm

删除已有容器及其可写层。

### 常用参数

- `-f`：强制删除运行中的容器。
- `-v`：同时删除关联的匿名数据卷。
- `--help`：显示帮助。

### 常用例子

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
