## traceroute

追踪数据包到目标经过的每跳网关和延迟。

### 常用参数

- `-n`：不解析域名，直接显示 IP。
- `-m N`：最大跳数，默认 30。
- `-w N`：等待响应的秒数。
- `-I`：改用 ICMP Echo 探测。
- `-T`：改用 TCP SYN 探测。

### 常用例子

**1. 不解析域名追踪路径**

```bash
traceroute -n example.com
```

**2. 用 TCP 探测 443 端口**

```bash
traceroute -T -p 443 -n example.com
```

**3. 限制跳数并缩短等待**

```bash
traceroute -n -m 15 -w 2 example.com
```
