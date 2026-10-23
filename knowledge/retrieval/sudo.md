# sudo 检索说明

## 用途与查询表达

以其他用户身份执行命令。适用实现：sudo。

- 怎么用 sudo。
- 查看 sudo 权限。
- 切到 root 环境。
- sudo 重定向失败。

## 参数与行为

- `-u USER`：以指定用户身份执行。
- `-i`：启动登录 shell，加载完整环境。
- `-s`：启动 shell，保留当前环境。
- `-l`：列出可执行的 sudo 命令。
- `-k`：作废已缓存的密码。
- `-v`：刷新密码缓存有效期。

## 常见任务示例

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

## 边界与易混淆点

sudo 用本人密码，su 用目标用户密码；改 sudoers 必须用 visudo。
