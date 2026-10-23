## ping

用 ICMP 测试到目标主机的连通性。

### 常用参数

- `-c N`：发 N 个包后退出。
- `-i SEC`：设置发包间隔秒数。
- `-W SEC`：单包回应超时秒数。
- `-w SEC`：本次总超时秒数。
- `-I IFACE`：指定出口接口。
- `-n`：只输出数字地址。
- `-q`：只输出统计摘要。

### 常用例子

**1. 测连通性，发 4 个包**

```bash
ping -c 4 example.com
```

**2. 限制总耗时**

```bash
ping -c 5 -w 3 example.com
```

**3. 只看结尾统计**

```bash
ping -q -c 10 example.com
```
