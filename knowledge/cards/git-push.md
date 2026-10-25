## git push

把本地引用和提交发送到远程仓库。

### 常用参数

- `-u`：成功推送后设置上游。
- `--dry-run`：预览推送。
- `--tags`：推送本地标签。
- `--force-with-lease`：在租约条件满足时强制更新。

### 常用例子

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
