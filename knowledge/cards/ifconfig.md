## ifconfig

查看和临时配置网络接口。

### 常用参数

- `-a`：显示所有接口，含未启用的。
- `IFACE`：只显示指定接口信息。
- `IFACE up`：启用指定接口。
- `IFACE down`：关闭指定接口。
- `netmask MASK`：设置子网掩码。
- `mtu N`：设置最大传输单元。
- `-s`：显示接口收发统计摘要。

### 常用例子

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
