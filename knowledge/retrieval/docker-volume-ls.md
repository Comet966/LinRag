# docker volume ls 检索说明

## 用途与查询表达

列出 Docker 管理的数据卷。适用实现：Docker CLI / Docker Engine。

- 查看 Docker 数据卷。
- 查未使用的数据卷。
- 列出持久化存储。

## 参数与行为

- `--filter FILTER`：按属性筛选。
- `--format FORMAT`：设置输出格式。
- `-q`：只输出卷名。

## 常见任务示例

**1. 列出数据卷**

```bash
docker volume ls
```

**2. 查看当前未被容器引用的卷**

```bash
docker volume ls --filter dangling=true
```

**3. 只列出卷名**

```bash
docker volume ls -q
```

## 边界与易混淆点

dangling 表示当前未被容器引用，不代表其中没有需要保留的数据；此命令不会删除数据卷。
