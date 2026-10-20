## chown

修改文件或目录的所有者及所属组。

### 常用参数

- `-R`：递归处理目录及内容。
- `-h`：修改符号链接本身的属主而非目标。
- `-v`：显示处理信息。
- `-c`：只报告实际改变。
- `--reference=FILE`：使用参考文件的属主和组。

### 常用例子

**1. 将文件属主和组设为指定用户与组**

```bash
chown alice:developers report.txt
```

**2. 只修改文件所属组，保持属主不变**

```bash
chown :developers report.txt
```
