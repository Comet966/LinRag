# hwclock 检索说明

## 用途与查询表达

读取与设置主板硬件时钟。适用实现：util-linux。

- 查看硬件时钟。
- 系统时间不对。
- 同步硬件时钟。
- 硬件时间差几秒。

## 参数与行为

- `--show`：显示硬件时钟的日期与时间。
- `-s`：把系统时钟设为硬件时间。
- `-w`：把硬件时钟设为系统时间。
- `-u`：按 UTC 解释硬件时钟。
- `-l`：按本地时间解释硬件时钟。
- `--adjust`：按 adjtime 记录校正漂移。

## 常见任务示例

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

## 边界与易混淆点

`hwclock` 读写主板 RTC，不直接改系统时间；systemd 系统多用 `timedatectl`。
