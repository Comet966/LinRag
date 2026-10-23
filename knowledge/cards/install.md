## install

复制文件并设定权限属主，或建目录。

### 常用参数

- `-m`：设置目标文件的权限模式。
- `-o`：设置属主，通常需 root。
- `-g`：设置属组。
- `-d`：创建目录，类似 `mkdir -p`。
- `-D`：自动补建目标的父目录。
- `-t`：指定目标目录。
- `-v`：显示处理的每个文件。

### 常用例子

**1. 一次建好多级目录**

```bash
install -d /tmp/demo/conf
```

**2. 复制并设为 755 权限**

```bash
install -m 755 app.sh /tmp/demo/
```

**3. 补建父目录后复制文件**

```bash
install -D -m 644 app.conf /tmp/demo/etc/app.conf
```
