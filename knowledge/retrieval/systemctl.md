# systemctl 检索说明

## 用途与查询表达

查询和管理 systemd 服务及其他单元。适用实现：systemd。

- 服务启动失败。
- 查看服务运行状态。
- 设置开机启动。
- 重启服务。

## 参数与行为

- `status UNIT`：查看单元状态。
- `start UNIT`：立即启动单元。
- `stop UNIT`：立即停止单元。
- `restart UNIT`：重启单元。
- `enable UNIT`：配置开机等目标激活时启动，不立即启动。
- `--now`：配合 enable 或 disable 同时启动或停止。
- `--user`：操作当前用户的服务管理器。
- `--no-pager`：不使用分页器。

## 常见任务示例

**1. 查看服务状态，单元名称以发行版实际配置为准**

```bash
systemctl --no-pager status sshd.service
```

**2. 立即启动指定服务（可能需要管理员权限）**

```bash
systemctl start nginx.service
```

**3. 设置开机启动并立即启动服务（可能需要管理员权限）**

```bash
systemctl enable --now nginx.service
```

**4. 查看当前用户的服务状态**

```bash
systemctl --user --no-pager status my-app.service
```

## 边界与易混淆点

status、start、enable 等是子命令。enable 与 start 不同；部分系统 SSH 单元名是 ssh.service。仅适用于 systemd。
