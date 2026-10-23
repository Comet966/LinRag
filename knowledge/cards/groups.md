## groups

打印用户所属的组名列表。

### 常用参数

- `--help`：显示帮助信息。
- `--version`：显示版本信息。
- `用户名`：省略时为当前用户。
- `id -Gn`：等价写法，结果相同。
- 其余：不接受其他命令行选项。

### 常用例子

**1. 查看当前用户所属组**

```bash
groups
```

**2. 查询指定用户的组**

```bash
groups alice
```

**3. 与 id -Gn 对照确认**

```bash
groups alice && id -Gn alice
```
