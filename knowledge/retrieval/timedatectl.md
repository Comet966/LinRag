# timedatectl 检索说明

## 用途与查询表达

查看和设置系统时间、时区与 NTP。适用实现：systemd。

- 修改系统时区。
- 系统时间不准。
- 看 NTP 是否同步。
- 列出时区列表。

## 参数与行为

- `-p`：只显示指定名称的属性
- `-a`：显示所有属性，含空值
- `--value`：只打印属性值
- `--no-pager`：不调用分页器
- `-H`：在远程主机上操作
- `-M`：在本地容器内操作

## 常见任务示例

**1. 查看当前时间与时区状态**

```bash
timedatectl status
```

**2. 列出所有可选时区**

```bash
timedatectl list-timezones
```

**3. 只读查看 NTP 同步属性**

```bash
timedatectl show -p NTP -p NTPSynchronized
```

## 边界与易混淆点

设置时间和时区要 root，容器内常被拒绝；`set-time` 与 NTP 同开时会冲突，先 `set-ntp` 关闭。
