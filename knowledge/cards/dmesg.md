## dmesg

读取内核环形缓冲区消息。

### 常用参数

- `-T`：时间戳转为可读时间。
- `-l err`：按级别过滤。
- `-w`：持续输出新消息。
- `-H`：分页并显示相对时间。
- `-x`：解码 facility 和级别。

### 常用例子

**1. 查看最近内核消息**

```bash
dmesg -T | tail -n 20
```

**2. 只看错误和警告**

```bash
sudo dmesg -T -l err,warn
```

**3. 排查 USB 设备**

```bash
dmesg -T | grep -i usb
```
