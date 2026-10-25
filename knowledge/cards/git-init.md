## git init

在目录中初始化 Git 仓库。

### 常用参数

- `-b NAME`：指定初始分支名。
- `--bare`：创建没有工作区的裸仓库。
- `--quiet`：减少输出。

### 常用例子

**1. 在新目录创建 main 分支仓库**

```bash
git init -b main project
```

**2. 初始化当前目录**

```bash
git init .
```

**3. 创建供推送使用的裸仓库**

```bash
git init --bare project.git
```
