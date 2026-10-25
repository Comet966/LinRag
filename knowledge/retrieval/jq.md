# jq 检索说明

## 用途与查询表达

解析、筛选和转换 JSON 数据。适用实现：jq 1.7+ 基础选项。

- 格式化 JSON。
- 提取 JSON 字段。
- 命令行解析接口响应。

## 参数与行为

- `-r`：直接输出字符串而不带 JSON 引号。
- `-c`：紧凑输出 JSON。
- `-s`：将输入的多个 JSON 值收集为数组。
- `--arg NAME VALUE`：绑定字符串变量。

## 常见任务示例

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

## 边界与易混淆点

过滤表达式使用单引号避免 shell 展开；-r 适用于字符串输出，不等于对任意数据做 JSON 校验。
