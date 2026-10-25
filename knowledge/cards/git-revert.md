## git revert

通过新增反向提交撤销已有提交的改动。

### 常用参数

- `--no-commit`：应用反向改动但暂不提交。
- `--continue`：解决冲突后继续。
- `--abort`：中止撤销过程。

### 常用例子

**1. 撤销最近一次提交并编辑说明**

```bash
git revert HEAD
```

**2. 先生成反向改动再检查**

```bash
git revert --no-commit HEAD
```

**3. 冲突后取消撤销过程**

```bash
git revert --abort
```
