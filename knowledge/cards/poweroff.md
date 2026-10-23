## poweroff

关闭 Linux 系统并写入关机记录。

### 常用参数

- `--help`：显示帮助并退出。
- `-w`：只写 wtmp 记录，不关机。
- `-d`：不写 wtmp 记录。
- `-f`：强制关机，不联系 init。
- `-p`：断电关机，poweroff 默认。
- `--no-wall`：不向所有终端广播。

### 常用例子

**1. 查看选项而不关机**

```bash
poweroff --help
```

**2. 阅读手册了解行为**

```bash
man poweroff
```
