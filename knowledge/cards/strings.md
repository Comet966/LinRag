## strings

在二进制文件中查找可打印字符串。

### 常用参数

- `-a`：扫描整个文件，不止初始化段
- `-n`：设定最短长度，默认 4 个字符
- `-t`：指定偏移量进制，o、d 或 x
- `-f`：在字符串前显示所属文件名
- `-e`：指定字符编码，如 s、S 或 l

### 常用例子

**1. 列出 /bin/ls 的可打印字符串**

```bash
strings /bin/ls
```

**2. 只输出长度不少于 8 的字符串**

```bash
strings -n 8 /bin/ls
```

**3. 带十六进制偏移过滤 libc**

```bash
strings -t x /bin/ls | grep -i libc
```
