# git cherry-pick 检索说明

## 用途与查询表达

将指定提交的改动应用为当前分支的新提交。适用实现：Git 2.23+。

- 挑选单个提交。
- 把修复移到另一个分支。
- 继续 cherry-pick。

## 参数与行为

- `-x`：在提交说明中记录来源。
- `--no-commit`：应用改动但暂不提交。
- `--continue`：冲突解决后继续。
- `--abort`：中止操作。

## 常见任务示例

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

## 边界与易混淆点

将 COMMIT_ID 替换为已核对的提交；会创建新历史，依赖前置提交的改动可能无法独立应用。
