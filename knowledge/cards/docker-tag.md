## docker tag

为已有镜像增加一个本地名称或标签。

### 常用参数

- `SOURCE_IMAGE`：源镜像名称或 ID。
- `TARGET_IMAGE`：目标仓库名称及标签。

### 常用例子

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
