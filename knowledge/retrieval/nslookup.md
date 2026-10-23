# nslookup 检索说明

## 用途与查询表达

按域名或 IP 查询 DNS 记录。适用实现：BIND utils。

- 查域名的解析结果。
- 用指定服务器查域名。
- 交互模式怎么用。
- 怎么反查 IP 域名。

## 参数与行为

- `域名`：向默认服务器查询。
- `SERVER`：指定 DNS 服务器。
- `-type=TYPE`：指定查询类型。
- `-timeout=N`：设置等待超时秒数。
- `-debug`：显示查询过程。
- `set type=TYPE`：交互模式设类型。

## 常见任务示例

**1. 查默认服务器的解析结果**

```bash
nslookup example.com
```

**2. 指定 DNS 服务器查询**

```bash
nslookup example.com 8.8.8.8
```

**3. 查 MX 记录**

```bash
nslookup -type=MX example.com
```

## 边界与易混淆点

nslookup 输出面向人阅读，脚本取值应改用 dig，指定服务器放末尾而非 `@`。
