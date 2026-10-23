## timedatectl

查看和设置系统时间、时区与 NTP。

### 常用参数

- `-p`：只显示指定名称的属性
- `-a`：显示所有属性，含空值
- `--value`：只打印属性值
- `--no-pager`：不调用分页器
- `-H`：在远程主机上操作
- `-M`：在本地容器内操作

### 常用例子

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
