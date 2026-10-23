# poweroff 检索说明

## 用途与查询表达

关闭系统并写入关机记录。适用实现：systemd。

- 怎么安全关机。
- 关机记录在哪查。
- 关机前不发广播。
- 和 halt 有何差别。

## 参数与行为

- `--help`：显示帮助并退出。
- `-w`：只写 wtmp 记录，不关机。
- `-d`：不写 wtmp 记录。
- `-f`：强制关机，不联系 init。
- `-p`：断电关机，poweroff 默认。
- `--no-wall`：不向所有终端广播。

## 常见任务示例

**1. 查看选项而不关机**

```bash
poweroff --help
```

**2. 阅读手册了解行为**

```bash
man poweroff
```

## 边界与易混淆点

systemd 下它会经 systemctl 停服务再关机，需 root；`-f` 不联系 init，`-w` 只记日志不关机。
