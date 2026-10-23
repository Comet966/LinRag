## unlink

删除单个文件，且不经过回收站。

### 常用参数

- `--help`：显示帮助信息。
- `--version`：显示版本号。
- `--`：结束选项解析。
- `FILE`：要删除的那一个文件。
- 不接受多文件或目录，无递归。

### 常用例子

**1. 删除 /tmp 测试文件**

```bash
unlink /tmp/demo-old.log
```

**2. 先确认路径再删除**

```bash
ls -l /tmp/demo.tmp && unlink /tmp/demo.tmp
```
