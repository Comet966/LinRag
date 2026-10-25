# docker logout 检索说明

## 用途与查询表达

移除 Docker 保存的指定镜像仓库登录信息。适用实现：Docker CLI / Docker Engine。

- 退出 Docker 登录。
- 移除本机镜像仓库凭据。
- 注销 Docker Hub。

## 参数与行为

- `SERVER`：可选的镜像仓库主机名。
- `--help`：显示帮助。

## 常见任务示例

**1. 退出 Docker Hub 登录**

```bash
docker logout
```

**2. 退出指定私有镜像仓库**

```bash
docker logout registry.example.com
```

## 边界与易混淆点

移除客户端保存的认证信息，不会停止容器，也不等于在服务器上撤销访问令牌；后续访问受限仓库需要重新认证。
