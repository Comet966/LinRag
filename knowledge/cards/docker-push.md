## docker push

将本地镜像上传到目标镜像仓库。

### 常用参数

- `--all-tags`：推送该镜像名称下的全部本地标签。
- `--quiet`：减少进度输出。

### 常用例子

**1. 查看推送帮助**

```bash
docker push --help
```

**2. 核对待推送标签**

```bash
docker images registry.example.com/team/demo
```

**3. 向已获授权的仓库推送明确标签**

```bash
docker push registry.example.com/team/demo:v1
```
