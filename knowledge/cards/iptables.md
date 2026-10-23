## iptables

查看和配置 netfilter 过滤规则。

### 常用参数

- `-t TABLE`：指定表，默认 filter。
- `-L`：列出链上的规则。
- `-n`：不把 IP 和端口解析成名称。
- `-v`：显示计数器等详细信息。
- `--line-numbers`：列出规则序号。
- `-S`：以命令形式打印规则。

### 常用例子

**1. 只读查看全部规则与计数**

```bash
iptables -L -n -v
```

**2. 带序号查看 INPUT 链**

```bash
iptables -L INPUT -n -v --line-numbers
```

**3. 以命令形式导出便于比对**

```bash
iptables -S
```
