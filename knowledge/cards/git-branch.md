## git branch

列出、创建或管理本地分支。

### 常用参数

- `-a`：显示本地和远程跟踪分支。
- `-vv`：显示跟踪关系和最近提交。
- `-m NAME`：重命名当前分支。
- `-d NAME`：删除满足合并条件的本地分支。

### 常用例子

**1. 列出全部已知分支**

```bash
git branch -a
```

**2. 检查分支跟踪关系**

```bash
git branch -vv
```

**3. 创建但不切换到新分支**

```bash
git branch feature/demo
```
