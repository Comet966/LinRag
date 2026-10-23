# traceroute 检索说明

## 用途与查询表达

追踪数据包到目标经过的每跳网关和延迟。适用实现：traceroute。

- 到某站走哪条线路。
- 哪一跳开始变慢。
- 星号行是什么意思。
- TCP 探测怎么追踪。

## 参数与行为

- `-n`：不解析域名，直接显示 IP。
- `-m N`：最大跳数，默认 30。
- `-w N`：等待响应的秒数。
- `-I`：改用 ICMP Echo 探测。
- `-T`：改用 TCP SYN 探测。

## 常见任务示例

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

## 边界与易混淆点

Linux 默认用 UDP 探测，Windows tracert 与 `-I` 用 ICMP，路径可能不同；`-T` 和 `-I` 需 root。
