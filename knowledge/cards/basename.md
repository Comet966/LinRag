## basename

取路径中的文件名。

### 常用参数

- `路径`：要处理的路径名。
- `后缀`：可选，从结果去掉。
- `-a`：多个路径一起处理。
- `-s 后缀`：指定要去掉的后缀。
- `-z`：用 NUL 分隔输出。

### 常用例子

**1. 取路径的文件名**

```bash
basename /var/log/syslog
```

**2. 去掉 .csv 后缀**

```bash
basename /home/alice/report.csv .csv
```

**3. 批量去掉后缀**

```bash
basename -s .log -a /var/log/app.log /var/log/error.log
```
