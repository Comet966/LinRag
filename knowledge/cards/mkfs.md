## mkfs

在设备上创建文件系统，会清空数据。

### 常用参数

- `-t TYPE`：指定文件系统类型。
- `-V`：显示将执行的命令。
- `-L LABEL`：设置卷标（ext 系列）。
- `-n`：只演练不写入（ext 系列）。
- `-F`：强制创建，慎用（ext 系列）。

### 常用例子

**1. 在占位分区创建 ext4**

```bash
sudo mkfs -t ext4 /dev/sdX1
```

**2. 只演练不写入（ext 系列）**

```bash
sudo mkfs.ext4 -n /dev/sdX1
```
