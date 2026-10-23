# basename 检索说明

## 用途与查询表达

去掉路径中的目录部分，只留文件名。适用实现：GNU coreutils。

- 从路径取文件名。
- 去掉文件后缀。
- 脚本里取文件名。
- basename 用法。

## 参数与行为

- `路径`：要处理的路径名。
- `后缀`：可选，从结果去掉。
- `-a`：多个路径一起处理。
- `-s 后缀`：指定要去掉的后缀。
- `-z`：用 NUL 分隔输出。

## 常见任务示例

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

## 边界与易混淆点

basename 只切字符串，不查文件；取目录部分用 dirname。
