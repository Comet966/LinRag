## git pull

获取远程更新并整合到当前分支。

### 常用参数

- `--ff-only`：只允许快进整合。
- `--rebase`：通过变基整合。
- `--no-rebase`：通过合并整合。

### 常用例子

**1. 安全地尝试快进更新**

```bash
git pull --ff-only
```

**2. 从指定远程分支快进更新**

```bash
git pull --ff-only origin main
```

**3. 在本地功能分支用变基整合**

```bash
git pull --rebase origin main
```
