## git checkout

切换分支或从指定版本恢复文件。

### 常用参数

- `-b NAME`：创建并切换分支。
- `--detach`：检出提交而不附着分支。
- `--`：将分支或选项与文件路径分隔。

### 常用例子

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
