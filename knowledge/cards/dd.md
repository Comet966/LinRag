## dd

按块复制文件或设备，写错会覆盖数据。

### 常用参数

- `if=FILE`：输入文件或设备。
- `of=FILE`：输出文件或设备，会覆盖。
- `bs=SIZE`：块大小，常用 `4M`。
- `count=N`：复制的块数。
- `status=progress`：显示进度。

### 常用例子

**1. 生成 100 MiB 测试文件**

```bash
dd if=/dev/zero of=/tmp/dd-test.img bs=1M count=100
```

**2. 备份设备到镜像（核对设备名）**

```bash
sudo dd if=/dev/sdX of=/tmp/disk.img bs=4M
```

**3. 恢复到设备（`of=` 务必核对）**

```bash
sudo dd if=/tmp/disk.img of=/dev/sdX bs=4M
```
