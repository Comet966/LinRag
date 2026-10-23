## hwclock

读取与设置主板硬件时钟。

### 常用参数

- `--show`：显示硬件时钟的日期与时间。
- `-s`：把系统时钟设为硬件时间。
- `-w`：把硬件时钟设为系统时间。
- `-u`：按 UTC 解释硬件时钟。
- `-l`：按本地时间解释硬件时钟。
- `--adjust`：按 adjtime 记录校正漂移。

### 常用例子

**1. 读取硬件时钟当前时间**

```bash
hwclock --show
```

**2. 按 UTC 解释后查看硬件时间**

```bash
hwclock --show --utc
```

**3. 用系统时间校准硬件时钟**

```bash
sudo hwclock --systohc --utc
```
