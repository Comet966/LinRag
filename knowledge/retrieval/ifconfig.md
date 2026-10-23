# ifconfig 检索说明

## 用途与查询表达

查看和临时配置网络接口。适用实现：net-tools。

- 本机网卡 IP 是多少。
- 怎么临时配 IP 地址。
- 查看所有网卡。
- 看网卡 MAC 地址。

## 参数与行为

- `-a`：显示所有接口，含未启用的。
- `IFACE`：只显示指定接口信息。
- `IFACE up`：启用指定接口。
- `IFACE down`：关闭指定接口。
- `netmask MASK`：设置子网掩码。
- `mtu N`：设置最大传输单元。
- `-s`：显示接口收发统计摘要。

## 常见任务示例

**1. 查看所有接口**

```bash
ifconfig -a
```

**2. 查看指定接口信息**

```bash
ifconfig eth0
```

**3. 临时配置地址与掩码**

```bash
ifconfig eth0 192.168.1.50 netmask 255.255.255.0
```

## 边界与易混淆点

ifconfig 属 net-tools，已被 `ip addr`、`ip link` 取代，改的地址重启即失效。
