# docker login 检索说明

## 用途与查询表达

登录镜像仓库并保存认证信息。适用实现：Docker CLI / Docker Engine。

- 登录 Docker 镜像仓库。
- 私有仓库认证。
- Docker 使用访问令牌登录。

## 参数与行为

- `-u USER`：指定仓库用户名。
- `--password-stdin`：从标准输入读取口令或令牌。
- `--help`：显示帮助。

## 常见任务示例

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

## 边界与易混淆点

第三个例子要求事先安全设置变量；认证信息可能由凭据助手或本地配置保存，不要使用明文 -p 参数。登录不代表已获得所有仓库权限。
