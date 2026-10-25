# git init 检索说明

## 用途与查询表达

在目录中初始化 Git 仓库。适用实现：Git 2.23+。

- 初始化代码仓库。
- 创建本地 Git 项目。
- 新建 main 分支仓库。

## 参数与行为

- `-b NAME`：指定初始分支名。
- `--bare`：创建没有工作区的裸仓库。
- `--quiet`：减少输出。

## 常见任务示例

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

## 边界与易混淆点

init 创建本地仓库，不设置远程；裸仓库没有用于编辑文件的工作区。
