## strace

跟踪进程的系统调用与信号。

### 常用参数

- `-f`：跟随 fork 出的子进程。
- `-p PID`：附加到已运行的进程。
- `-e trace=SET`：只跟踪指定系统调用。
- `-o FILE`：结果写入文件而非 stderr。
- `-c`：统计调用次数与耗时。
- `-T`：显示每次调用耗时。
- `-s N`：限制字符串显示长度。

### 常用例子

**1. 统计命令的系统调用耗时**

```bash
strace -c /bin/true
```

**2. 只看文件相关的系统调用**

```bash
strace -e trace=file ls /tmp
```
