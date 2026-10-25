## git diff

比较工作区、暂存区或指定提交之间的差异。

### 常用参数

- `--staged`：比较暂存区与 HEAD。
- `--stat`：显示文件变更统计。
- `--name-only`：只列出变化路径。
- `--check`：检查新增的空白格式问题。

### 常用例子

**1. 查看尚未暂存的修改**

```bash
git diff
```

**2. 查看准备提交的差异**

```bash
git diff --staged
```

**3. 比较两个分支**

```bash
git diff --stat main..feature/demo
```
