# gdb 检索说明

## 用途与查询表达

命令行调试器，可设断点、单步和查值。适用实现：GDB。

- 怎么用 gdb 调试。
- 加断点单步执行。
- 查看变量和栈。
- 程序崩溃看栈。

## 参数与行为

- `-q`：不打印版本等开场信息。
- `-batch`：执行完命令后退出。
- `-ex CMD`：执行一条 GDB 命令。
- `-cd DIR`：切换调试工作目录。
- `-s FILE`：指定读取的符号表。
- `-p PID`：附加到运行中的进程。

## 常见任务示例

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

## 边界与易混淆点

`-batch` 配 `-ex` 可做只读脚本化调试；要行级调试须编译加 `-g`，否则只能看汇编。
