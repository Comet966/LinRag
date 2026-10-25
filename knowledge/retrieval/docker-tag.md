# docker tag 检索说明

## 用途与查询表达

为已有镜像增加一个本地名称或标签。适用实现：Docker CLI / Docker Engine。

- Docker 镜像改标签。
- 为镜像添加仓库前缀。
- 推送前设置镜像名称。

## 参数与行为

- `SOURCE_IMAGE`：源镜像名称或 ID。
- `TARGET_IMAGE`：目标仓库名称及标签。

## 常见任务示例

**1. 为镜像增加版本标签**

```bash
docker tag demo:local demo:v1
```

**2. 增加目标仓库标签**

```bash
docker tag demo:local registry.example.com/team/demo:v1
```

**3. 增加开发标签**

```bash
docker tag demo:v1 demo:dev
```

## 边界与易混淆点

tag 创建本地名称，不复制镜像层、不上传镜像，也不删除旧标签。
