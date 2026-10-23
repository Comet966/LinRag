## md5sum

计算或核对文件的 MD5 摘要。

### 常用参数

- `-c`：按清单核对摘要。
- `--quiet`：只输出校验失败项。
- `--status`：不输出，只用退出码。
- `-b`：以二进制模式读取。
- `--tag`：输出 BSD 风格摘要。

### 常用例子

**1. 生成校验和清单**

```bash
md5sum app.tar.gz > app.tar.gz.md5
```

**2. 按清单核对文件**

```bash
md5sum -c app.tar.gz.md5
```

**3. 只显示失败项**

```bash
md5sum -c --quiet app.tar.gz.md5
```
