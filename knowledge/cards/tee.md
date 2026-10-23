## tee

同时输出到终端和文件。

### 常用参数

- `-a`：追加而不是覆盖。
- `-i`：忽略 Ctrl+C 中断。
- `-p`：诊断非管道写错误。
- `文件...`：可同时写多个文件。
- `--output-error=模式`：设置写错误行为。

### 常用例子

**1. 保存目录列表**

```bash
ls -l /var/log | tee /tmp/log-list.txt
```

**2. 追加编译日志**

```bash
make 2>&1 | tee -a build.log
```

**3. sudo 写配置文件**

```bash
printf 'listen=8080\n' | sudo tee /etc/myapp.conf
```
