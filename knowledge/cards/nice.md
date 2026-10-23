## nice

以指定调度优先级运行命令。

### 常用参数

- `-n 值`：设 nice 值，越小优先级越高。
- `-数值`：旧写法，等价于 `-n` 数值。
- `--adjustment=值`：同 `-n`，长选项写法。
- `--help`：显示帮助后退出。
- `--version`：显示版本信息。

### 常用例子

**1. 查看当前的 nice 值**

```bash
nice
```

**2. 以最低优先级做耗时统计**

```bash
nice -n 19 du -sh /var/log
```

**3. 调高优先级需要 root**

```bash
sudo nice -n -5 ps aux
```
