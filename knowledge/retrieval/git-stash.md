# git stash 检索说明

## 用途与查询表达

临时保存和恢复尚未提交的工作。适用实现：Git 2.23+。

- 临时保存代码。
- 切分支前保存修改。
- 恢复 stash。

## 参数与行为

- `push -m MESSAGE`：保存并设置说明。
- `-u`：保存时包含未跟踪文件。
- `list`：列出保存记录。
- `apply`：恢复记录但保留该记录。

## 常见任务示例

**1. 临时保存已跟踪与未跟踪改动**

```bash
git stash push -u -m 'before switching branches'
```

**2. 查看暂存工作列表**

```bash
git stash list
```

**3. 恢复最近记录但不删除记录**

```bash
git stash apply 'stash@{0}'
```

## 边界与易混淆点

默认不包含未跟踪文件；-u 不包含被忽略文件，apply 可能冲突，pop 成功时会移除对应记录。
