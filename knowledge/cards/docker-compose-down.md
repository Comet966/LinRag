## docker compose down

停止并删除 Compose 项目的服务容器与网络。

### 常用参数

- `--remove-orphans`：删除同项目中未定义的服务容器。
- `--volumes`：同时删除声明的命名卷和附加匿名卷。
- `--timeout SECONDS`：指定停止超时。

### 常用例子

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
