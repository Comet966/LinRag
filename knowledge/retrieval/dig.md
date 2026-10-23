# dig 检索说明

## 用途与查询表达

查询 DNS 记录并显示解析报文。适用实现：BIND utils。

- 域名解析到哪个 IP。
- 换 DNS 服务器再查。
- 怎么查 MX 记录。
- 怎么反查 IP 域名。

## 参数与行为

- `+short`：只输出精简结果。
- `@SERVER`：向指定 DNS 服务器查询。
- `-t TYPE`：指定查询类型。
- `-x IP`：反向解析 PTR 记录。
- `+noall +answer`：只显示应答段。
- `+trace`：逐级跟踪解析过程。

## 常见任务示例

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

## 边界与易混淆点

dig 输出完整报文，脚本取值用 `+short`，指定服务器用 `@`，nslookup 输出更粗糙。
