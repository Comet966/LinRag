# docker compose 检索说明

## 用途与查询表达

使用 Compose 文件管理多容器应用。适用实现：Docker Compose 插件（docker compose）。

- Docker Compose 常用命令。
- 多容器编排。
- docker-compose 与 docker compose。

## 参数与行为

- `-f FILE`：指定 Compose 文件。
- `-p NAME`：指定项目名。
- `--profile NAME`：启用指定配置档。
- `--help`：显示帮助。

## 常见任务示例

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

## 边界与易混淆点

面向 docker compose 插件；旧版 docker-compose 独立程序的行为和选项可能不同，具体操作分别建卡。
