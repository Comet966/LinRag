## git fetch

从远程下载对象并更新远程跟踪引用。

### 常用参数

- `--all`：获取所有已配置远程。
- `--prune`：清理远程已删除分支的本地跟踪引用。
- `--tags`：获取标签。
- `--dry-run`：显示操作但不更新。

### 常用例子

**1. 获取 origin 最新状态**

```bash
git fetch origin
```

**2. 预览获取和清理操作**

```bash
git fetch --dry-run --prune origin
```

**3. 获取全部远程**

```bash
git fetch --all
```
