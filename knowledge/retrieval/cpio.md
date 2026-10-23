# cpio 检索说明

## 用途与查询表达

建立或还原归档包，常与 find 配合。适用实现：GNU cpio。

- cpio 怎么解包。
- 和 tar 有什么区别。
- 用 find 打包。
- 只列出包内文件。

## 参数与行为

- `-o`：copy-out，打包成归档。
- `-i`：copy-in，从归档解出文件。
- `-p`：copy-pass，直接复制目录树。
- `-t`：只列出归档内容。
- `-d`：按需创建目标目录。
- `-v`：显示处理的文件名清单。
- `-H FMT`：指定格式，如 newc。

## 常见任务示例

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

## 边界与易混淆点

与 tar 不同，cpio 从标准输入读文件名列表，需 `find` 喂；`-i` 解包、`-o` 打包。
