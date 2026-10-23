# mount 检索说明

## 用途与查询表达

把设备挂载到挂载点。适用实现：util-linux。

- 怎么挂载 U 盘。
- 挂载 ISO 文件。
- 按 UUID 挂载。
- 开机自动挂载。

## 参数与行为

- `-t TYPE`：指定文件系统类型。
- `-o ro`：以只读方式挂载。
- `-o remount`：用新选项重新挂载。
- `-o loop`：把镜像文件当块设备挂载。
- `-a`：挂载 fstab 中所有未挂载项。
- `-U UUID`：按 UUID 挂载。

## 常见任务示例

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

## 边界与易混淆点

设备在前挂载点在后，挂载点须存在；fstab 持久化需手动编辑。
