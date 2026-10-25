## git log

查看提交历史及各提交的改动。

### 常用参数

- `--oneline`：每条提交显示一行。
- `--graph`：显示分支图。
- `--all`：查看所有引用可达的提交。
- `-n N`：限制提交数量。
- `-p`：显示补丁。

### 常用例子

**1. 查看最近十条提交**

```bash
git log -n 10 --oneline
```

**2. 查看各分支的提交图**

```bash
git log --graph --oneline --all
```

**3. 查看指定文件的改动历史**

```bash
git log -p -- README.md
```
