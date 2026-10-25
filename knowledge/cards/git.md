## git

分布式版本控制工具，用于管理代码历史、分支和协作。

### 常用参数

- `-C DIR`：在指定目录执行命令。
- `--version`：显示 Git 版本。
- `--help`：显示帮助。

### 常用例子

**1. 查看安装版本**

```bash
git --version
```

**2. 查看工作区状态**

```bash
git status
```

**3. 在指定仓库查看近期历史**

```bash
git -C project log -5 --oneline
```
