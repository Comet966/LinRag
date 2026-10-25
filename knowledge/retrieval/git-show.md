# git show 检索说明

## 用途与查询表达

显示某个 Git 对象及提交的详细内容。适用实现：Git 2.23+。

- 查看单次提交。
- 读取历史版本文件。
- 查看 HEAD 内容。

## 参数与行为

- `--stat`：显示提交的变更统计。
- `--name-only`：仅列出涉及的路径。
- `--format=FORMAT`：设置提交信息格式。

## 常见任务示例

**1. 查看最近一次提交**

```bash
git show HEAD
```

**2. 查看提交修改了哪些文件**

```bash
git show --stat HEAD
```

**3. 查看某次提交中的文件内容**

```bash
git show HEAD:README.md
```

## 边界与易混淆点

REV:path 读取指定提交中的文件，不改变工作区；对象或路径必须存在。
