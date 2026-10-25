## git show

显示某个 Git 对象及提交的详细内容。

### 常用参数

- `--stat`：显示提交的变更统计。
- `--name-only`：仅列出涉及的路径。
- `--format=FORMAT`：设置提交信息格式。

### 常用例子

**1. 查看最近一次提交**

```bash
git show HEAD
```

**2. 查看提交修改了哪些文件**

```bash
git show --stat HEAD
```

**3. 查看某次提交中的文件内容**

```bash
git show HEAD:README.md
```
