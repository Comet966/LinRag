# docker inspect 检索说明

## 用途与查询表达

读取容器或其他 Docker 对象的详细配置。适用实现：Docker CLI / Docker Engine。

- 查看容器配置。
- 查询 Docker 挂载路径。
- 容器状态详情。

## 参数与行为

- `--type TYPE`：限定对象类型。
- `--format FORMAT`：按模板输出。
- `--size`：查看容器文件系统大小信息。

## 常见任务示例

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

## 边界与易混淆点

对象配置可能包含环境变量和凭据；同名对象存在时使用 --type 明确类型。
