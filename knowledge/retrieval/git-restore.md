# git restore 检索说明

## 用途与查询表达

从暂存区或指定提交恢复工作区和暂存区文件。适用实现：Git 2.23+。

- 撤销暂存。
- 保留修改取消 git add。
- 恢复文件版本。

## 参数与行为

- `-p`：交互选择需要恢复的修改块。
- `--staged`：恢复暂存区。
- `--source=REV`：指定来源提交。
- `--worktree`：恢复工作区。
- `--`：分隔路径。

## 常见任务示例

**1. 取消 README 的暂存而保留工作区修改**

```bash
git restore --staged -- README.md
```

**2. 交互选择要恢复的工作区修改**

```bash
git restore -p -- README.md
```

**3. 从 HEAD 恢复暂存区中的指定文件**

```bash
git restore --source=HEAD --staged -- README.md
```

## 边界与易混淆点

Git 2.23+；默认恢复工作区会丢弃未提交修改，--staged 只操作暂存区，不能把它们混为一谈。
