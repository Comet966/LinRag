## split

按大小或行数把大文件切成多块。

### 常用参数

- `-b SIZE`：按字节大小切分。
- `-l N`：按行数切分。
- `-n N`：切成 N 个大致等大的块。
- `-d`：后缀用数字而非字母。
- `-a N`：设置后缀长度。
- `--verbose`：每生成一块打印信息。

### 常用例子

**1. 每 10MB 切一块，数字后缀**

```bash
split -b 10M -d /tmp/big.log /tmp/part_
```

**2. 每 1000 行切一块**

```bash
split -l 1000 /tmp/big.log /tmp/chunk_
```
