## docker logout

移除 Docker 保存的指定镜像仓库登录信息。

### 常用参数

- `SERVER`：可选的镜像仓库主机名。
- `--help`：显示帮助。

### 常用例子

**1. 退出 Docker Hub 登录**

```bash
docker logout
```

**2. 退出指定私有镜像仓库**

```bash
docker logout registry.example.com
```
