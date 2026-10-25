## git switch

切换工作分支，或创建新分支后切换。

### 常用参数

- `-c NAME`：创建并切换新分支。
- `--track`：设置远程跟踪关系。
- `--detach`：以分离 HEAD 方式检出提交。

### 常用例子

**1. 切换已有 main 分支**

```bash
git switch main
```

**2. 创建开发分支**

```bash
git switch -c feature/demo
```

**3. 从远程跟踪分支创建本地分支**

```bash
git switch --track origin/feature/demo
```
