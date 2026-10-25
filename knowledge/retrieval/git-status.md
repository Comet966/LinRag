# git status 检索说明

## 用途与查询表达

查看工作区、暂存区和分支的当前状态。适用实现：Git 2.23+。

- 查看未提交修改。
- 检查暂存区。
- Git 工作区是否干净。

## 参数与行为

- `-s`：使用简短格式。
- `-b`：显示分支与跟踪信息。
- `--porcelain`：输出适合脚本解析的稳定格式。
- `--untracked-files=all`：列出未跟踪目录下的文件。

## 常见任务示例

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

## 边界与易混淆点

只读取状态；ahead/behind 依据本地远程跟踪引用，需先 fetch 才能反映远程新提交。
