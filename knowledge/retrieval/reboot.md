# reboot 检索说明

## 用途与查询表达

重启系统，是 `systemctl` 的封装。适用实现：systemd。

- 重启服务器。
- 安全重启机器。
- 重启前发通知。
- 演练一次重启。

## 参数与行为

- `-f`：不再停服务，立即强制重启。
- `-w`：只写 wtmp 记录，不真重启。
- `-d`：不写 wtmp 登录记录。
- `--no-wall`：重启前不向用户发广播。
- `--no-sync`：重启前不刷写磁盘缓存。
- `--help`：显示帮助后退出。

## 常见任务示例

**1. 仅写记录，不真正重启**

```bash
reboot -w
```

**2. 演练重启且不广播**

```bash
reboot -w --no-wall
```

**3. 查看全部可用选项**

```bash
reboot --help
```

## 边界与易混淆点

systemd 版是 `systemctl reboot` 的符号链接，需 root；`-w` 只写 wtmp，用来演练。
