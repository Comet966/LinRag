## git status

查看工作区、暂存区和分支的当前状态。

### 常用参数

- `-s`：使用简短格式。
- `-b`：显示分支与跟踪信息。
- `--porcelain`：输出适合脚本解析的稳定格式。
- `--untracked-files=all`：列出未跟踪目录下的文件。

### 常用例子

**1. 查看当前改动**

```bash
git status
```

**2. 简要查看分支和文件状态**

```bash
git status -sb
```

**3. 列出全部未跟踪文件**

```bash
git status --short --untracked-files=all
```
