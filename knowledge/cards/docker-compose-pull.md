## docker compose pull

拉取 Compose 服务引用的镜像。

### 常用参数

- `--include-deps`：包括所选服务的依赖。
- `--policy POLICY`：选择 missing 或 always 拉取策略。
- `--quiet`：减少进度输出。

### 常用例子

**1. 拉取项目服务镜像**

```bash
docker compose pull
```

**2. 拉取 web 及其依赖镜像**

```bash
docker compose pull --include-deps web
```

**3. 按始终拉取策略更新镜像**

```bash
docker compose pull --policy always
```
