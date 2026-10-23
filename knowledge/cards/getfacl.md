## getfacl

查看文件和目录的访问控制列表。

### 常用参数

- `-c`：省略注释头，只看条目。
- `-d`：只显示默认 ACL。
- `-R`：递归处理子目录。
- `-t`：表格形式，含默认 ACL。
- `-n`：显示数字 UID 和 GID。
- `-p`：保留路径的前导斜杠。

### 常用例子

**1. 查看文件的 ACL 条目**

```bash
getfacl report.txt
```

**2. 省略注释头只看条目**

```bash
getfacl -c report.txt
```

**3. 递归查看目录 ACL**

```bash
getfacl -R /srv/share
```
