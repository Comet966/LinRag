# nohup 检索说明

## 用途与查询表达

让命令忽略挂断信号并继续运行。适用实现：GNU coreutils。

- 退出终端后继续运行。
- nohup 后台跑脚本。
- 关闭 SSH 任务不停。
- 后台 PID 怎么保存。

## 参数与行为

- `&`：配合 nohup 放后台执行。
- `> 文件 2>&1`：合并标准输出和错误。
- `>> 文件 2>&1`：追加写入日志。
- `$!`：后台进程的 PID。
- `nohup.out`：默认输出文件。

## 常见任务示例

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

## 边界与易混淆点

nohup 只忽略 SIGHUP 并重定向输出，不会自动后台，需配合 &。
