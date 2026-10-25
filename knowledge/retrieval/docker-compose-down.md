# docker compose down 检索说明

## 用途与查询表达

停止并删除 Compose 项目的服务容器与网络。适用实现：Docker Compose 插件（docker compose）。

- 停止并删除 Compose 应用。
- compose down 和 stop 区别。
- 删除 Compose 数据卷。

## 参数与行为

- `--remove-orphans`：删除同项目中未定义的服务容器。
- `--volumes`：同时删除声明的命名卷和附加匿名卷。
- `--timeout SECONDS`：指定停止超时。

## 常见任务示例

**1. 执行前核对项目容器**

```bash
docker compose ps -a
```

**2. 执行前核对配置**

```bash
docker compose config --quiet
```

**3. 查看停止和移除帮助**

```bash
docker compose down --help
```

## 边界与易混淆点

例子仅用于执行前检查；down 默认不删除数据卷，--volumes 会删除部分卷数据，外部卷和外部网络不会由 down 删除。
