# docker version 检索说明

## 用途与查询表达

显示 Docker 客户端和服务端版本。适用实现：Docker CLI / Docker Engine。

- Docker 版本号。
- Docker 客户端服务端是否匹配。
- 查看 Engine 版本。

## 参数与行为

- `--format FORMAT`：设置输出格式。
- `--help`：显示帮助。

## 常见任务示例

**1. 查看客户端和服务端版本**

```bash
docker version
```

**2. 以 JSON 格式查看版本**

```bash
docker version --format '{{json .}}'
```

**3. 仅读取客户端版本字段**

```bash
docker version --format '{{.Client.Version}}'
```

## 边界与易混淆点

完整命令需要连接服务端；docker --version 只输出客户端版本，二者用途不同。
