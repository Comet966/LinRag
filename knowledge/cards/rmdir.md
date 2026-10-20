## rmdir

删除空目录。

### 常用参数

- `-p`：依次尝试删除指定目录及其空父目录。
- `-v`：显示删除的目录。
- `--ignore-fail-on-non-empty`：忽略目录非空导致的失败。

### 常用例子

**1. 删除一个空文件夹**

```bash
rmdir empty-dir
```

**2. 删除空目录，并继续删除空的父目录**

```bash
rmdir -p work/cache/empty
```
