## gdb

命令行调试器，可断点单步查值。

### 常用参数

- `-q`：不打印版本等开场信息。
- `-batch`：执行完命令后退出。
- `-ex CMD`：执行一条 GDB 命令。
- `-cd DIR`：切换调试工作目录。
- `-s FILE`：指定读取的符号表。
- `-p PID`：附加到运行中的进程。

### 常用例子

**1. 静默加载被调试程序**

```bash
gdb -q ./a.out
```

**2. 只读列出函数符号**

```bash
gdb -q -batch -ex 'info functions' ./a.out
```

**3. 断在 main 后看调用栈**

```bash
gdb -q -batch -ex 'break main' -ex run -ex bt ./a.out
```
