# git checkout 检索说明

## 用途与查询表达

切换分支或从指定版本恢复文件。适用实现：Git 2.23+。

- 旧版 Git 切换分支。
- checkout 创建分支。
- 分离 HEAD。

## 参数与行为

- `-b NAME`：创建并切换分支。
- `--detach`：检出提交而不附着分支。
- `--`：将分支或选项与文件路径分隔。

## 常见任务示例

**1. 切换已有分支**

```bash
git checkout main
```

**2. 创建并切换分支**

```bash
git checkout -b feature/demo
```

**3. 只读检查某个提交时进入分离 HEAD**

```bash
git checkout --detach HEAD~1
```

## 边界与易混淆点

checkout 同时承担切分支和恢复文件两类操作；新版本可分别用 switch 和 restore，恢复文件可能覆盖未提交内容。
