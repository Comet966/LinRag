## docker login

登录镜像仓库并保存认证信息。

### 常用参数

- `-u USER`：指定仓库用户名。
- `--password-stdin`：从标准输入读取口令或令牌。
- `--help`：显示帮助。

### 常用例子

**1. 交互登录 Docker Hub**

```bash
docker login
```

**2. 交互登录已获授权的私有仓库**

```bash
docker login registry.example.com
```

**3. 从已设置的环境变量读取令牌**

```bash
printf '%s' "$REGISTRY_TOKEN" | docker login registry.example.com -u "$REGISTRY_USER" --password-stdin
```
