## git cherry-pick

将指定提交的改动应用为当前分支的新提交。

### 常用参数

- `-x`：在提交说明中记录来源。
- `--no-commit`：应用改动但暂不提交。
- `--continue`：冲突解决后继续。
- `--abort`：中止操作。

### 常用例子

**1. 应用指定提交并保留来源说明**

```bash
git cherry-pick -x COMMIT_ID
```

**2. 只应用改动以便检查**

```bash
git cherry-pick --no-commit COMMIT_ID
```

**3. 冲突后取消操作**

```bash
git cherry-pick --abort
```
