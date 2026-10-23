## sudo

以其他用户身份执行命令。

### 常用参数

- `-u USER`：以指定用户身份执行。
- `-i`：启动登录 shell，加载完整环境。
- `-s`：启动 shell，保留当前环境。
- `-l`：列出可执行的 sudo 命令。
- `-k`：作废已缓存的密码。
- `-v`：刷新密码缓存有效期。

### 常用例子

**1. 以 root 重启服务**

```bash
sudo systemctl restart nginx
```

**2. 查看自己的 sudo 权限**

```bash
sudo -l
```

**3. 进入 root 登录 shell**

```bash
sudo -i
```
