# file 检索说明

## 用途与查询表达

根据内容判断文件类型。适用实现：file。

- 查看文件类型。
- 判断文件编码。
- file 看 MIME。
- 批量识别文件。

## 参数与行为

- `-b`：只输出类型，不显示文件名。
- `-i`：输出 MIME 类型和编码。
- `--mime-type`：只输出 MIME 类型。
- `-L`：跟随符号链接。
- `-z`：查看压缩包内部类型。
- `-0`：NUL 分隔输出。

## 常见任务示例

**1. 判断文件类型**

```bash
file README.md archive.tar.gz
```

**2. 只看 MIME 类型**

```bash
file -b --mime-type upload.bin
```

**3. 批量识别文件**

```bash
find . -maxdepth 1 -type f -print0 | xargs -0 file
```

## 边界与易混淆点

file 靠魔数推断，可能误判；默认不跟随符号链接，需用 -L。
