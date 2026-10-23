# journalctl 检索说明

## 用途与查询表达

查询和跟踪 systemd 日志。适用实现：systemd。

- 查看服务日志。
- 实时跟踪报错。
- 查上次启动日志。
- 清理日志空间。

## 参数与行为

- `-u 单元`：只看指定服务日志。
- `-f`：持续跟踪新日志。
- `--since`：限定起始时间。
- `-b -1`：查看上次启动日志。
- `-p err`：只看错误级日志。
- `-n 20`：只显示最后若干行。

## 常见任务示例

**1. 查看服务今天的日志**

```bash
journalctl -u nginx.service --since today
```

**2. 实时跟踪服务日志**

```bash
journalctl -u ssh.service -f
```

**3. 查上次启动的错误**

```bash
journalctl -p err -b -1
```

## 边界与易混淆点

需 systemd；默认日志在 /run/log/journal，重启即丢，持久化要 /var/log/journal。
