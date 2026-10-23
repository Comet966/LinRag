# tee 检索说明

## 用途与查询表达

从标准输入读数据，同时写到终端和文件。适用实现：GNU coreutils。

- 输出同时存文件。
- tee 追加日志。
- sudo 重定向报错。
- tee 覆盖还是追加。

## 参数与行为

- `-a`：追加而不是覆盖。
- `-i`：忽略 Ctrl+C 中断。
- `-p`：诊断非管道写错误。
- `文件...`：可同时写多个文件。
- `--output-error=模式`：设置写错误行为。

## 常见任务示例

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

## 边界与易混淆点

tee 默认覆盖，追加用 -a；sudo 重定向应写成 sudo tee。
