# awk 检索说明

## 用途与查询表达

按记录和字段处理文本，适合筛选、计算和报表。适用实现：POSIX awk subset。

- 按列提取文本。
- 字段求和。
- 条件筛选行。
- 统计报表。

## 参数与行为

- `-F FS`：指定字段分隔符，可为正则表达式。
- `-v NAME=VALUE`：执行程序前设置变量。
- `-f FILE`：从文件读取 awk 程序。

## 常见任务示例

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

## 边界与易混淆点

默认按空白划分字段；$0 是整行，$1 是第一列，NF 是字段数，NR 是已读记录数。这里只使用常见可移植语法。
