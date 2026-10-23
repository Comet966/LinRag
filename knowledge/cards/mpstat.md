## mpstat

按 CPU 查看利用率与中断统计。

### 常用参数

- `-P ALL`：每个 CPU 各显示一行。
- `-P 0`：只看 0 号 CPU。
- `-u`：报告 CPU 利用率，默认开。
- `-A`：等价 `-u -P ALL`。
- `-I SUM`：报告中断统计汇总。
- `-o JSON`：以 JSON 格式输出。

### 常用例子

**1. 每 2 秒采样 3 次，按核分行**

```bash
mpstat -P ALL 2 3
```

**2. 只看中断统计**

```bash
mpstat -I SUM 1 2
```

**3. 输出 JSON 便于采集**

```bash
mpstat -o JSON 1 1
```
