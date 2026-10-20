## xargs

将标准输入拆成参数，批量传给其他命令。

### 常用参数

- `-0`：按空字符分隔输入，适合任意文件名。
- `-d CHAR`：指定输入分隔符。
- `-n N`：每次最多传入 N 个参数。
- `-P N`：最多并行运行 N 个进程。
- `-r`：输入为空时不执行命令。
- `-I STR`：用每个输入行替换命令参数中的占位符。

### 常用例子

**1. 安全传递含空格的文件名，批量统计日志行数**

```bash
find . -type f -name '*.log' -print0 | xargs -0 -r wc -l
```

**2. 把空字符分隔的文件名交给 grep，搜索文件内容**

```bash
find . -type f -name '*.log' -print0 | xargs -0 -r grep -n 'ERROR'
```

**3. 把逐行目录名转换成 mkdir 参数**

```bash
printf '%s\n' build dist | xargs -r -I '{}' mkdir -p '{}'
```
