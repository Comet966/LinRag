## git restore

从暂存区或指定提交恢复工作区和暂存区文件。

### 常用参数

- `-p`：交互选择需要恢复的修改块。
- `--staged`：恢复暂存区。
- `--source=REV`：指定来源提交。
- `--worktree`：恢复工作区。
- `--`：分隔路径。

### 常用例子

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
