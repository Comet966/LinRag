## ip

查看和配置网络接口、地址和路由。

### 常用参数

- `address show`：显示接口 IP 地址。
- `link show`：显示网络接口状态。
- `route show`：显示路由表。
- `-br`：以简洁格式显示。
- `-4`：只处理 IPv4。
- `-6`：只处理 IPv6。

### 常用例子

**1. 简洁列出各接口的 IP 地址**

```bash
ip -br address show
```

**2. 查看 IPv4 路由表和默认网关**

```bash
ip -4 route show
```

**3. 查看网卡链路状态**

```bash
ip -br link show
```
