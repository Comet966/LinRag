## sed

按行处理文本，可替换、筛选或删除内容。

### 常用参数

- `-n`：关闭每行自动输出。
- `-e SCRIPT`：添加一段处理脚本。
- `-f FILE`：从文件读取脚本。
- `-E`：使用扩展正则表达式。
- `-i[SUFFIX]`：直接修改文件，可用后缀保留备份。

### 常用例子

**1. 把每行全部 old 替换成 new 后输出**

```bash
sed 's/old/new/g' notes.txt
```

**2. 仅打印第 10 到第 20 行**

```bash
sed -n '10,20p' app.log
```

**3. 修改文件内容，并保留 .bak 备份**

```bash
sed -i.bak 's/old/new/g' notes.txt
```

**4. 过滤以 # 开头的注释行后输出**

```bash
sed '/^#/d' config.conf
```
