# git pull 检索说明

## 用途与查询表达

获取远程更新并整合到当前分支。适用实现：Git 2.23+。

- 拉取远程更新。
- 同步当前分支。
- pull 与 fetch 区别。

## 参数与行为

- `--ff-only`：只允许快进整合。
- `--rebase`：通过变基整合。
- `--no-rebase`：通过合并整合。

## 常见任务示例

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

## 边界与易混淆点

pull 包含 fetch 和整合；分叉时 --ff-only 会拒绝操作，--rebase 可能改写本地提交。
