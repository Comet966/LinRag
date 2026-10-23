## nslookup

按域名或 IP 查询 DNS 记录。

### 常用参数

- `域名`：向默认服务器查询。
- `SERVER`：指定 DNS 服务器。
- `-type=TYPE`：指定查询类型。
- `-timeout=N`：设置等待超时秒数。
- `-debug`：显示查询过程。
- `set type=TYPE`：交互模式设类型。

### 常用例子

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
