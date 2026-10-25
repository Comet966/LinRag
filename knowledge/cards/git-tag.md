## git tag

列出或创建提交的标签。

### 常用参数

- `-l PATTERN`：按模式列出标签。
- `-a NAME`：创建附注标签。
- `-m MESSAGE`：指定附注内容。
- `--points-at REV`：列出指向某提交的标签。

### 常用例子

**1. 列出版本标签**

```bash
git tag -l 'v*'
```

**2. 为当前提交创建附注标签**

```bash
git tag -a v1.0.0 -m 'Release 1.0.0'
```

**3. 查看指向 HEAD 的标签**

```bash
git tag --points-at HEAD
```
