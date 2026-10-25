## docker compose

使用 Compose 文件管理多容器应用。

### 常用参数

- `-f FILE`：指定 Compose 文件。
- `-p NAME`：指定项目名。
- `--profile NAME`：启用指定配置档。
- `--help`：显示帮助。

### 常用例子

**1. 查看 Compose 插件版本**

```bash
docker compose version
```

**2. 查看子命令帮助**

```bash
docker compose --help
```

**3. 核对指定配置文件**

```bash
docker compose -f compose.yaml config --quiet
```
