## wget

从网络下载文件，支持续传和批量下载。

### 常用参数

- `-O FILE`：将下载内容写入指定文件。
- `-c`：尝试继续未完成的下载。
- `-P DIR`：指定保存目录。
- `-i FILE`：从文件读取 URL 列表。
- `-q`：减少输出。
- `--limit-rate=RATE`：限制下载速率。

### 常用例子

**1. 下载网页并指定本地文件名**

```bash
wget -O page.html https://example.com/
```

**2. 尝试继续下载未完成且远端未改变的文件**

```bash
wget -c https://example.com/archive.tar.gz
```

**3. 按文本文件中的 URL 列表批量下载**

```bash
wget -i urls.txt -P downloads/
```
