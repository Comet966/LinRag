# git remote 检索说明

## 用途与查询表达

管理远程仓库地址和跟踪配置。适用实现：Git 2.23+。

- 配置 Git 远程地址。
- 查看 origin。
- 更换仓库地址。

## 参数与行为

- `-v`：显示远程地址。
- `add NAME URL`：添加远程。
- `get-url NAME`：显示指定远程 URL。
- `set-url NAME URL`：修改远程 URL。

## 常见任务示例

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

## 边界与易混淆点

add 和 set-url 只更新本地配置，不会创建远程仓库或推送提交。
