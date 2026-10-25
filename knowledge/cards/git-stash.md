## git stash

临时保存和恢复尚未提交的工作。

### 常用参数

- `push -m MESSAGE`：保存并设置说明。
- `-u`：保存时包含未跟踪文件。
- `list`：列出保存记录。
- `apply`：恢复记录但保留该记录。

### 常用例子

**1. 临时保存已跟踪与未跟踪改动**

```bash
git stash push -u -m 'before switching branches'
```

**2. 查看暂存工作列表**

```bash
git stash list
```

**3. 恢复最近记录但不删除记录**

```bash
git stash apply 'stash@{0}'
```
