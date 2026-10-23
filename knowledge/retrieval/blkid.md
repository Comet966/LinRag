# blkid 检索说明

## 用途与查询表达

查看块设备的 UUID 和类型。适用实现：util-linux。

- 查看分区 UUID。
- 设备什么文件系统。
- 按标签查设备。
- 脚本取 UUID 值。

## 参数与行为

- `-s TAG`：只显示指定字段。
- `-o value`：只输出字段值。
- `-o list`：表格列出设备信息。
- `-L LABEL`：按标签查设备。
- `-U UUID`：按 UUID 查设备。
- `-p`：低层直接探测设备。

## 常见任务示例

**1. 列出所有设备属性**

```bash
sudo blkid
```

**2. 只取分区 UUID**

```bash
sudo blkid -s UUID -o value /dev/sdb1
```

**3. 按标签查设备**

```bash
sudo blkid -L DATA
```

## 边界与易混淆点

新格式化设备可能读不到，先 partprobe 或加 `-p`；查 UUID 比 lsblk 可靠。
