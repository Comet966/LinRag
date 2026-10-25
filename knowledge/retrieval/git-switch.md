# git switch 检索说明

## 用途与查询表达

切换工作分支，或创建新分支后切换。适用实现：Git 2.23+。

- 切换 Git 分支。
- 创建并切换分支。
- 跟踪远程分支。

## 参数与行为

- `-c NAME`：创建并切换新分支。
- `--track`：设置远程跟踪关系。
- `--detach`：以分离 HEAD 方式检出提交。

## 常见任务示例

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

## 边界与易混淆点

适用于 Git 2.23+；未提交修改与目标冲突时会拒绝切换，不要用丢弃修改选项绕过检查。
