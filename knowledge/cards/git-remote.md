## git remote

管理远程仓库地址和跟踪配置。

### 常用参数

- `-v`：显示远程地址。
- `add NAME URL`：添加远程。
- `get-url NAME`：显示指定远程 URL。
- `set-url NAME URL`：修改远程 URL。

### 常用例子

**1. 查看远程仓库地址**

```bash
git remote -v
```

**2. 读取 origin 的地址**

```bash
git remote get-url origin
```

**3. 为新仓库添加远程**

```bash
git remote add origin https://example.com/team/project.git
```
