# tar 检索说明

## 用途与查询表达

将多个文件打包，或列出、解开归档。适用实现：GNU tar。

- 压缩文件夹。
- 创建 tar.gz。
- 解开 tar 归档。
- 查看压缩包文件列表。

## 参数与行为

- `-c`：创建归档。
- `-x`：解开归档。
- `-t`：列出归档内容。
- `-f FILE`：指定归档文件。
- `-z`：通过 gzip 压缩或解压。
- `-j`：通过 bzip2 压缩或解压。
- `-J`：通过 xz 压缩或解压。
- `-v`：显示处理的文件。
- `-C DIR`：切换到指定目录再处理。

## 常见任务示例

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

## 边界与易混淆点

-c、-x、-t 是互斥操作；tar 本身打包，-z 等选择压缩工具。-f 后紧跟归档文件名。
