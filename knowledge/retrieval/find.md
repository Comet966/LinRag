# find 检索说明

## 用途与查询表达

按名称、类型、时间等条件递归查找文件。适用实现：GNU findutils。

- 按文件名找文件。
- 查找目录。
- 根据修改时间查文件。
- 查找带空格的路径。

## 参数与行为

- `-name PATTERN`：按文件名模式匹配，模式应加引号。
- `-iname PATTERN`：按文件名匹配，忽略大小写。
- `-type f`：只匹配普通文件。
- `-type d`：只匹配目录。
- `-mtime N`：匹配修改时间距今 N 个完整的 24 小时周期。
- `-maxdepth N`：限制遍历深度。
- `-empty`：匹配空的普通文件或空目录。
- `-print0`：以空字符分隔输出路径。

## 常见任务示例

**1. 递归查找当前目录下的日志文件**

```bash
find . -type f -name '*.log'
```

**2. 在两层目录内查找空目录**

```bash
find . -maxdepth 2 -type d -empty
```

**3. 查找过去 24 小时内修改过的普通文件**

```bash
find . -type f -mtime 0
```

**4. 按文件名查找，忽略大小写**

```bash
find . -type f -iname '*.jpg'
```

## 边界与易混淆点

这些是表达式测试和动作，其中 -maxdepth 是全局选项。-mtime +7 表示完整天数大于 7；不是创建时间。
