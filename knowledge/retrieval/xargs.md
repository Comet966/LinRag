# xargs 检索说明

## 用途与查询表达

将标准输入拆成参数，批量传给其他命令。适用实现：GNU findutils。

- 管道输出转命令参数。
- 批量处理查找到的文件。
- 避免文件名空格拆分。

## 参数与行为

- `-0`：按空字符分隔输入，适合任意文件名。
- `-d CHAR`：指定输入分隔符。
- `-n N`：每次最多传入 N 个参数。
- `-P N`：最多并行运行 N 个进程。
- `-r`：输入为空时不执行命令。
- `-I STR`：用每个输入行替换命令参数中的占位符。

## 常见任务示例

**1. 安全传递含空格的文件名，批量统计日志行数**

```bash
find . -type f -name '*.log' -print0 | xargs -0 -r wc -l
```

**2. 把空字符分隔的文件名交给 grep，搜索文件内容**

```bash
find . -type f -name '*.log' -print0 | xargs -0 -r grep -n 'ERROR'
```

**3. 把逐行目录名转换成 mkdir 参数**

```bash
printf '%s\n' build dist | xargs -r -I '{}' mkdir -p '{}'
```

## 边界与易混淆点

默认按空白及引号规则解析输入；文件名传递优先与 find -print0 配合。-n 与 -I 不应随意混用。
