## git rebase

将当前分支的提交重新应用到新的基底。

### 常用参数

- `-i`：交互整理提交。
- `--continue`：解决冲突后继续。
- `--abort`：中止正在进行的变基。
- `--onto BASE`：指定新的基底。

### 常用例子

**1. 将当前功能分支变基到 main**

```bash
git rebase main
```

**2. 冲突解决并暂存后继续**

```bash
git rebase --continue
```

**3. 取消正在进行的变基**

```bash
git rebase --abort
```
