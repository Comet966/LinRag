## docker version

显示 Docker 客户端和服务端版本。

### 常用参数

- `--format FORMAT`：设置输出格式。
- `--help`：显示帮助。

### 常用例子

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
