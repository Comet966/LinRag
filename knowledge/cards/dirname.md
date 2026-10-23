## dirname

取路径中的目录部分。

### 常用参数

- `路径...`：一个或多个路径。
- `-z`：用 NUL 分隔输出。
- `--`：结束选项解析。
- `--help`：显示帮助。
- `"$(dirname "$0")"`：脚本取自身目录。

### 常用例子

**1. 取文件的目录**

```bash
dirname /var/log/syslog
```

**2. 忽略尾部斜杠**

```bash
dirname /var/log/
```

**3. 脚本取自身目录**

```bash
script_dir=$(dirname "$0")
```
