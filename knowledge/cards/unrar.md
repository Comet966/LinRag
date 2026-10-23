## unrar

从 rar 压缩包里列表或解压文件。

### 常用参数

- `x`：保留包内相对路径解压。
- `e`：解压到当前目录，不保留路径。
- `l`：列出压缩包内文件。
- `t`：测试压缩包是否完好。
- `-o+`：同名文件直接覆盖。
- `-y`：所有询问都回答是。

### 常用例子

**1. 查看包内文件**

```bash
unrar l /tmp/demo.rar
```

**2. 解压到指定目录**

```bash
unrar x /tmp/demo.rar /tmp/demo-out/
```

**3. 先测试能否解压**

```bash
unrar t /tmp/demo.rar
```
