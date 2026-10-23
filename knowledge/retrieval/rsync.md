# rsync 检索说明

## 用途与查询表达

在本地或远程目录之间增量同步文件。适用实现：rsync。

- 备份目录到另一块盘。
- 尾斜杠有什么区别。
- 先看会同步哪些文件。
- 同步时删掉多余文件。

## 参数与行为

- `-a`：归档模式，等价 `-rlptgoD`。
- `-n`：试运行，只打印不修改。
- `-v`：显示同步的文件清单。
- `--delete`：删除目标端多余文件，有风险。
- `-P`：保留断点并显示进度。
- `--exclude=PAT`：排除匹配的路径。

## 常见任务示例

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

## 边界与易混淆点

源目录加 `/` 只同步内容，不加则连目录本身放入目标；`--delete` 会删目标端多余文件，须先 `-n` 干跑。
