## mkswap

建立交换区，会覆盖设备原有内容。

### 常用参数

- `-c`：建立前检查坏块，较慢。
- `-f`：跳过尺寸检查强制建立。
- `-L LABEL`：设置交换区卷标。
- `-U UUID`：指定交换区 UUID。
- `-p SIZE`：指定页大小（字节）。

### 常用例子

**1. 在占位分区建交换区（有风险）**

```bash
mkswap /dev/sdXN
```

**2. 为交换文件设置卷标**

```bash
mkswap -L swap1 /swapfile1
```

**3. 建立前先检查坏块**

```bash
mkswap -c /dev/sdXN
```
