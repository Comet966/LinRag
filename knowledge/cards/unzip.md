## unzip

查看或解压 ZIP 压缩包。

### 常用参数

- `-l`：列出压缩包中的文件。
- `-t`：测试归档完整性。
- `-d DIR`：指定解压目录。
- `-n`：不覆盖已存在的文件。
- `-o`：覆盖已有文件且不询问。
- `-q`：减少输出。

### 常用例子

**1. 解压到指定目录，保留已有文件**

```bash
unzip -n project.zip -d extracted/
```

**2. 只列出 ZIP 中的文件，不解压**

```bash
unzip -l project.zip
```
