## tcpdump

抓取并分析网络接口上的数据包。

### 常用参数

- `-i`：指定网卡，`any` 表示全部
- `-c`：抓够指定包数后自动停止
- `-n`：不把地址和端口解析成名字
- `-w`：把原始数据包写入文件
- `-r`：从保存的文件里读取数据包
- `-A`：以 ASCII 形式显示报文内容

### 常用例子

**1. 抓 10 个包后自动停止**

```bash
sudo tcpdump -i any -c 10 -n
```

**2. 看 5 个 80 端口报文**

```bash
sudo tcpdump -i any -c 5 -n port 80 -A
```

**3. 存包供离线分析**

```bash
sudo tcpdump -i eth0 -c 100 -w cap.pcap
```
