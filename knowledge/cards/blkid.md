## blkid

查看块设备的 UUID 和类型。

### 常用参数

- `-s TAG`：只显示指定字段。
- `-o value`：只输出字段值。
- `-o list`：表格列出设备信息。
- `-L LABEL`：按标签查设备。
- `-U UUID`：按 UUID 查设备。
- `-p`：低层直接探测设备。

### 常用例子

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
