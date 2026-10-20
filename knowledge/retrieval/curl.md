# curl 检索说明

## 用途与查询表达

通过 URL 传输数据，常用于 HTTP 请求和下载。适用实现：curl。

- 发 HTTP 请求。
- 下载接口结果。
- 查看响应头。
- 请求重定向。
- API 调试。

## 参数与行为

- `-L`：跟随重定向。
- `-o FILE`：把响应体写入指定文件。
- `-O`：以 URL 中的文件名保存。
- `-I`：发送 HEAD 请求，仅取响应头。
- `-i`：在输出中包含响应头。
- `-f`：HTTP 错误状态通常返回失败且不输出响应体。
- `-s`：隐藏进度及错误信息。
- `-S`：配合 -s 仍显示错误。
- `-H HEADER`：添加请求头。
- `-d DATA`：发送请求数据，HTTP 默认使用 POST。

## 常见任务示例

**1. 跟随重定向并保存网页**

```bash
curl -fL -o page.html https://example.com/
```

**2. 发送 HEAD 请求查看 HTTP 响应头**

```bash
curl -I https://example.com/
```

**3. 发送 JSON 数据到示例 API（替换为实际服务地址）**

```bash
curl -H 'Content-Type: application/json' -d '{"name":"demo"}' https://api.example.com/items
```

**4. 安静获取响应，同时保留错误提示**

```bash
curl -fsS https://example.com/
```

## 边界与易混淆点

默认将响应体输出到终端。-I 发送 HEAD，-i 在普通响应中附带头；-o 指定本地名，-O 使用远程名。
