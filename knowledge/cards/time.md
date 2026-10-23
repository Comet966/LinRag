## time

统计命令耗时与 CPU 占用。

### 常用参数

- `-p`：使用 POSIX 可移植输出格式
- `-f`：自定义输出格式，如 `%E`
- `-o`：把统计结果写入指定文件
- `-a`：配合 `-o` 追加而不覆盖
- `-v`：输出内存等详细资源用量

### 常用例子

**1. 统计一条命令的耗时**

```bash
time ls /usr/bin
```

**2. 外部 time 输出资源详情**

```bash
/usr/bin/time -v sleep 1
```

**3. 把耗时写入文件比较**

```bash
/usr/bin/time -o t.log -f '%E' sleep 1
```
