## paste

把多个文件按列并排合并。

### 常用参数

- `-d`：指定列间分隔符，默认制表符。
- `-s`：串行处理，每个文件占一行。
- `-z`：以 NUL 作为行分隔符。
- `--help`：显示帮助信息。
- `--version`：显示版本号。

### 常用例子

**1. 两文件按列合并**

```bash
paste a.txt b.txt
```

**2. 用逗号分隔各列**

```bash
paste -d, a.txt b.txt
```

**3. 每个文件合并成一行**

```bash
paste -s a.txt b.txt
```
