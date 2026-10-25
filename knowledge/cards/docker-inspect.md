## docker inspect

读取容器或其他 Docker 对象的详细配置。

### 常用参数

- `--type TYPE`：限定对象类型。
- `--format FORMAT`：按模板输出。
- `--size`：查看容器文件系统大小信息。

### 常用例子

**1. 查看指定容器详情**

```bash
docker inspect --type container demo-web
```

**2. 只看挂载配置**

```bash
docker inspect --format '{{json .Mounts}}' demo-web
```

**3. 查看容器状态**

```bash
docker inspect --format '{{.State.Status}}' demo-web
```
