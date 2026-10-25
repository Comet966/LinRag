# git commit 检索说明

## 用途与查询表达

将暂存区内容保存为一个本地提交。适用实现：Git 2.23+。

- 提交代码。
- 保存暂存区。
- 修改最近一次提交说明。

## 参数与行为

- `-m MESSAGE`：指定提交说明。
- `--amend`：修改最近一次提交。
- `--only`：只提交指定路径。
- `--dry-run`：预览提交范围。

## 常见任务示例

**1. 预览将提交的文件**

```bash
git commit --dry-run
```

**2. 提交已暂存的改动**

```bash
git commit -m 'Update documentation'
```

**3. 仅提交指定的已跟踪文件**

```bash
git commit --only README.md -m 'Update README'
```

## 边界与易混淆点

commit 不会自动推送；--amend 改写提交历史，已共享提交不应随意修改。
