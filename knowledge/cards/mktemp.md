## mktemp

安全创建临时文件或目录。

### 常用参数

- `-d`：创建临时目录而非文件。
- `-u`：只打印名字不创建，不安全。
- `-p DIR`：在指定目录下创建。
- `-t`：在 $TMPDIR 或 /tmp 下建。
- `--suffix=SUF`：给名字加后缀。
- `-q`：静默，抑制失败提示。

### 常用例子

**1. 创建临时文件并取得路径**

```bash
mktemp
```

**2. 创建临时目录**

```bash
mktemp -d
```

**3. 指定目录、模板与后缀**

```bash
mktemp -p /tmp --suffix=.log build.XXXXXX
```
