## zip

创建或更新 ZIP 压缩包。

### 常用参数

- `-r`：递归包含子目录。
- `-q`：减少输出。
- `-9`：使用最高压缩级别。
- `-u`：更新较新的文件并添加新文件。
- `-x PATTERN`：排除匹配的路径。

### 常用例子

**1. 把项目目录压缩为 ZIP**

```bash
zip -r project.zip project/
```

**2. 压缩目录，同时排除日志文件**

```bash
zip -r project.zip project/ -x '*.log'
```
