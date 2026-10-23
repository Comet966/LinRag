## mount

把设备挂载到挂载点。

### 常用参数

- `-t TYPE`：指定文件系统类型。
- `-o ro`：以只读方式挂载。
- `-o remount`：用新选项重新挂载。
- `-o loop`：把镜像文件当块设备挂载。
- `-a`：挂载 fstab 中所有未挂载项。
- `-U UUID`：按 UUID 挂载。

### 常用例子

**1. 挂载 U 盘分区**

```bash
sudo mount /dev/sdb1 /mnt/usb
```

**2. 只读挂载 ISO 镜像**

```bash
sudo mount -o loop,ro /tmp/image.iso /mnt/iso
```

**3. 重新挂载为只读**

```bash
sudo mount -o remount,ro /
```
