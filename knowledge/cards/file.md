## file

判断文件类型。

### 常用参数

- `-b`：只输出类型，不显示文件名。
- `-i`：输出 MIME 类型和编码。
- `--mime-type`：只输出 MIME 类型。
- `-L`：跟随符号链接。
- `-z`：查看压缩包内部类型。
- `-0`：NUL 分隔输出。

### 常用例子

**1. 判断文件类型**

```bash
file README.md archive.tar.gz
```

**2. 只看 MIME 类型**

```bash
file -b --mime-type upload.bin
```

**3. 批量识别文件**

```bash
find . -maxdepth 1 -type f -print0 | xargs -0 file
```
