# axel 检索说明

## 用途与查询表达

多连接分段下载，可断点续传。适用实现：axel。

- 多线程下载文件。
- 提高下载速度。
- 下载中断怎么续传。
- 限制下载速度。

## 参数与行为

- `-n N`：用 N 个连接分段下载。
- `-o FILE`：指定保存的文件名。
- `-s RATE`：限速，单位字节每秒。
- `-q`：安静模式，不显示进度。
- `-a`：改用另一种进度显示。
- `-k`：不校验 SSL 证书，有风险。

## 常见任务示例

**1. 十连接下载到指定文件**

```bash
axel -n 10 -o /tmp/file.iso https://example.com/file.iso
```

**2. 限速约 1 MiB 每秒下载**

```bash
axel -s 1048576 -o /tmp/file.iso https://example.com/file.iso
```

**3. 安静模式多连接下载**

```bash
axel -q -n 8 https://example.com/file.iso
```

## 边界与易混淆点

多连接要求服务器支持 Range，否则退回单连接；重跑同一命令即续传。
