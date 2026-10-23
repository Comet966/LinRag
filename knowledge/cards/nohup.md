## nohup

退出终端后仍运行命令。

### 常用参数

- `&`：配合 nohup 放后台执行。
- `> 文件 2>&1`：合并标准输出和错误。
- `>> 文件 2>&1`：追加写入日志。
- `$!`：后台进程的 PID。
- `nohup.out`：默认输出文件。

### 常用例子

**1. 后台跑脚本并记日志**

```bash
nohup python3 worker.py > worker.log 2>&1 &
```

**2. 丢弃输出并记 PID**

```bash
nohup ./sync.sh > /dev/null 2>&1 & echo $! > sync.pid
```

**3. 使用默认 nohup.out**

```bash
nohup ./backup.sh &
```
