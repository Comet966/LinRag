## jq

解析、筛选和转换 JSON 数据。

### 常用参数

- `-r`：直接输出字符串而不带 JSON 引号。
- `-c`：紧凑输出 JSON。
- `-s`：将输入的多个 JSON 值收集为数组。
- `--arg NAME VALUE`：绑定字符串变量。

### 常用例子

**1. 格式化 JSON 文件**

```bash
jq '.' data.json
```

**2. 读取配置中的字符串字段**

```bash
jq -r '.name' package.json
```

**3. 输出每个项目的名称**

```bash
jq -r '.items[].name' data.json
```
