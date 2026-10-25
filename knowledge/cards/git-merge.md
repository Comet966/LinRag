## git merge

把其他分支的历史合并到当前分支。

### 常用参数

- `--ff-only`：仅允许快进合并。
- `--no-ff`：禁用快进并建立合并提交。
- `--abort`：尝试中止正在进行的合并。

### 常用例子

**1. 仅在能够快进时合并更新**

```bash
git merge --ff-only origin/main
```

**2. 将功能分支合并到当前分支**

```bash
git merge feature/demo
```

**3. 冲突后中止当前合并**

```bash
git merge --abort
```
