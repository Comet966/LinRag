## cpio

建立或还原归档包，可与 find 配合。

### 常用参数

- `-o`：copy-out，打包成归档。
- `-i`：copy-in，从归档解出文件。
- `-p`：copy-pass，直接复制目录树。
- `-t`：只列出归档内容。
- `-d`：按需创建目标目录。
- `-v`：显示处理的文件名清单。
- `-H FMT`：指定格式，如 newc。

### 常用例子

**1. 打包 etc 下的普通文件**

```bash
find /etc -type f | cpio -ocv > etc.cpio
```

**2. 查看包内文件清单**

```bash
cpio -itv < etc.cpio
```

**3. 解包到当前目录并覆盖**

```bash
cpio -iduv < etc.cpio
```
