# helm list 检索说明

## 用途与查询表达

列出命名空间或集群内的 Helm 发布记录。适用实现：Helm 3/4 基础操作。

- 列出 Helm 发布。
- 查看已安装 Chart。
- Helm release 列表。

## 参数与行为

- `-n NAMESPACE`：指定命名空间。
- `-A`：查看所有命名空间。
- `-o FORMAT`：设置 json 或 yaml 输出。
- `--filter REGEXP`：按名称正则筛选。

## 常见任务示例

**1. 查看命名空间中的发布**

```bash
helm list -n demo
```

**2. 查看所有命名空间的发布**

```bash
helm list -A
```

**3. 按名称筛选并输出 JSON**

```bash
helm list -n demo --filter '^demo-' -o json
```

## 边界与易混淆点

结果按状态等条件筛选，通常不是所有历史记录；发布记录和实际资源健康状态需要分别检查。
