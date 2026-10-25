## git reset

调整暂存区，或将当前分支移动到指定提交。

### 常用参数

- `--soft`：只移动 HEAD，保留暂存区和工作区。
- `--mixed`：移动 HEAD 并重置暂存区，保留工作区。
- `--hard`：同时重置 HEAD、暂存区和工作区。

### 常用例子

**1. 取消单个文件暂存**

```bash
git reset HEAD -- README.md
```

**2. 撤回最近一次本地提交但保留暂存内容**

```bash
git reset --soft HEAD~1
```

**3. 撤回本地提交并保留工作区修改**

```bash
git reset --mixed HEAD~1
```
