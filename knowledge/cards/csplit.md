## csplit

按内容匹配把大文件切成多份。

### 常用参数

- `-f PREF`：指定输出文件前缀。
- `-b FMT`：指定后缀格式，如 %02d。
- `-n N`：指定后缀数字位数。
- `-k`：出错时保留已生成文件。
- `-s`：静默，不打印分片大小。
- `-z`：删除长度为 0 的分片。
- `-q`：同 `-s`，不输出大小。

### 常用例子

**1. 按 SERVER 行切分日志**

```bash
csplit -s app.log '/SERVER/' '{*}'
```

**2. 指定前缀与数字后缀**

```bash
csplit -s -f part -b '%02d.log' app.log '/SERVER/' '{*}'
```

**3. 切分后丢弃空分片**

```bash
csplit -s -z app.log '/SERVER/' '{*}'
```
