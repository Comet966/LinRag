## awk

按记录和字段处理文本，适合筛选、计算和报表。

### 常用参数

- `-F FS`：指定字段分隔符，可为正则表达式。
- `-v NAME=VALUE`：执行程序前设置变量。
- `-f FILE`：从文件读取 awk 程序。

### 常用例子

**1. 按冒号分列并输出第一列**

```bash
awk -F ':' '{print $1}' /etc/passwd
```

**2. 将第二列的数值求和**

```bash
awk '{total += $2} END {print total}' sales.txt
```

**3. 筛选第三列数值大于 100 的记录**

```bash
awk '$3 > 100 {print $1, $3}' metrics.txt
```

**4. 输出行号和每行字段数**

```bash
awk '{print NR, NF}' report.txt
```
