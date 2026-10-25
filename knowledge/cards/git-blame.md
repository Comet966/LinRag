## git blame

逐行显示文件内容最后修改的提交和作者。

### 常用参数

- `-L START,END`：限定行号范围。
- `-w`：忽略空白差异。
- `--show-email`：显示作者邮箱。

### 常用例子

**1. 查看文件逐行来源**

```bash
git blame README.md
```

**2. 只查看指定行范围**

```bash
git blame -L 10,30 -- README.md
```

**3. 忽略空白变化追溯内容**

```bash
git blame -w -- README.md
```
