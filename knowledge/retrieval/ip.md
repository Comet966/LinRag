# ip 检索说明

## 用途与查询表达

查看和配置网络接口、地址和路由。适用实现：iproute2。

- 查看本机 IP。
- 网卡状态。
- 默认网关。
- 路由表。

## 参数与行为

- `address show`：显示接口 IP 地址。
- `link show`：显示网络接口状态。
- `route show`：显示路由表。
- `-br`：以简洁格式显示。
- `-4`：只处理 IPv4。
- `-6`：只处理 IPv6。

## 常见任务示例

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

## 边界与易混淆点

address、link、route 是对象，show 是操作；示例只查看，不改网络配置。远端看到的公网地址不一定出现在本机接口上。
