## chmod

修改文件或目录的访问权限。

### 常用参数

- `-R`：递归修改目录及内容。
- `-v`：显示处理信息。
- `-c`：只报告实际改变的权限。
- `--reference=FILE`：使用参考文件的权限。

### 常用例子

**1. 给文件所有者增加执行权限**

```bash
chmod u+x script.sh
```

**2. 将文件权限设为仅属主可读写**

```bash
chmod 600 secrets.conf
```

**3. 为属主增加目录访问权限**

```bash
chmod u+x private/
```
