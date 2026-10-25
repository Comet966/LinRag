# git push 检索说明

## 用途与查询表达

把本地引用和提交发送到远程仓库。适用实现：Git 2.23+。

- 上传代码。
- 首次推送分支。
- 推送 Git 标签。

## 参数与行为

- `-u`：成功推送后设置上游。
- `--dry-run`：预览推送。
- `--tags`：推送本地标签。
- `--force-with-lease`：在租约条件满足时强制更新。

## 常见任务示例

**1. 预览 main 的推送**

```bash
git push --dry-run origin main
```

**2. 首次推送功能分支并设置上游**

```bash
git push -u origin feature/demo
```

**3. 推送一个明确的版本标签**

```bash
git push origin v1.0.0
```

## 边界与易混淆点

会修改远程仓库；先核对目标和差异，强推即使使用 --force-with-lease 仍可能覆盖共享历史。
