## helm list

列出命名空间或集群内的 Helm 发布记录。

### 常用参数

- `-n NAMESPACE`：指定命名空间。
- `-A`：查看所有命名空间。
- `-o FORMAT`：设置 json 或 yaml 输出。
- `--filter REGEXP`：按名称正则筛选。

### 常用例子

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
