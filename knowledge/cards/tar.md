## tar

将多个文件打包，或列出、解开归档。

### 常用参数

- `-c`：创建归档。
- `-x`：解开归档。
- `-t`：列出归档内容。
- `-f FILE`：指定归档文件。
- `-z`：通过 gzip 压缩或解压。
- `-j`：通过 bzip2 压缩或解压。
- `-J`：通过 xz 压缩或解压。
- `-v`：显示处理的文件。
- `-C DIR`：切换到指定目录再处理。

### 常用例子

**1. 把项目目录打包并使用 gzip 压缩**

```bash
tar -czf project.tar.gz project/
```

**2. 列出压缩归档中的文件，不解压**

```bash
tar -tzf project.tar.gz
```

**3. 解压到已存在的目标目录**

```bash
tar -xzf project.tar.gz -C extracted/
```

**4. 使用 xz 压缩创建归档**

```bash
tar -cJf project.tar.xz project/
```
