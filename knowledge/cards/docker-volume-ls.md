## docker volume ls

列出 Docker 管理的数据卷。

### 常用参数

- `--filter FILTER`：按属性筛选。
- `--format FORMAT`：设置输出格式。
- `-q`：只输出卷名。

### 常用例子

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
