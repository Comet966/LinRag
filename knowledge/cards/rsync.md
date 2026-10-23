## rsync

在本地或远程目录之间增量同步文件。

### 常用参数

- `-a`：归档模式，等价 `-rlptgoD`。
- `-n`：试运行，只打印不修改。
- `-v`：显示同步的文件清单。
- `--delete`：删除目标端多余文件，有风险。
- `-P`：保留断点并显示进度。
- `--exclude=PAT`：排除匹配的路径。

### 常用例子

**1. 干跑：源目录尾不加斜杠**

```bash
rsync -avn /data/project /backup/
```

**2. 干跑：源目录尾加斜杠**

```bash
rsync -avn /data/project/ /backup/project/
```

**3. 干跑确认删除范围**

```bash
rsync -avn --delete /data/project/ /backup/
```
