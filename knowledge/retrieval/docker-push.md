# docker push 检索说明

## 用途与查询表达

将本地镜像上传到目标镜像仓库。适用实现：Docker CLI / Docker Engine。

- 上传 Docker 镜像。
- 推送私有仓库。
- 发布镜像版本。

## 参数与行为

- `--all-tags`：推送该镜像名称下的全部本地标签。
- `--quiet`：减少进度输出。

## 常见任务示例

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

## 边界与易混淆点

最后一个例子仅在目标仓库已授权时使用；会向远程发送镜像内容，推送前确认未包含凭据和私有构建文件。
