## dig

查询 DNS 记录并显示解析报文。

### 常用参数

- `+short`：只输出精简结果。
- `@SERVER`：向指定 DNS 服务器查询。
- `-t TYPE`：指定查询类型。
- `-x IP`：反向解析 PTR 记录。
- `+noall +answer`：只显示应答段。
- `+trace`：逐级跟踪解析过程。

### 常用例子

**1. 查 A 记录，只看结果**

```bash
dig +short example.com
```

**2. 指定服务器查 MX**

```bash
dig @8.8.8.8 example.com MX +short
```

**3. 反查 IP 对应域名**

```bash
dig -x 192.0.2.1 +short
```
