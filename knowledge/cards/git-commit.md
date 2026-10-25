## git commit

将暂存区内容保存为一个本地提交。

### 常用参数

- `-m MESSAGE`：指定提交说明。
- `--amend`：修改最近一次提交。
- `--only`：只提交指定路径。
- `--dry-run`：预览提交范围。

### 常用例子

**1. 预览将提交的文件**

```bash
git commit --dry-run
```

**2. 提交已暂存的改动**

```bash
git commit -m 'Update documentation'
```

**3. 仅提交指定的已跟踪文件**

```bash
git commit --only README.md -m 'Update README'
```
