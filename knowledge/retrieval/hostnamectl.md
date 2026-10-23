# hostnamectl 检索说明

## 用途与查询表达

查看或设置系统主机名等设置。适用实现：systemd。

- 查看当前主机名。
- 改主机名要重启吗。
- 永久改主机名。
- 静态和临时主机名。

## 参数与行为

- `--static`：只输出静态主机名。
- `--pretty`：只输出易读主机名。
- `--transient`：只输出临时主机名。
- `-H user@host`：操作远程主机。
- `-M 容器名`：在本地容器内操作。
- `--no-ask-password`：不提示输密码。

## 常见任务示例

**1. 查看当前主机名设置**

```bash
hostnamectl status
```

**2. 只看静态主机名**

```bash
hostnamectl --static
```

**3. 永久改名，需 root**

```bash
sudo hostnamectl set-hostname web01
```

## 边界与易混淆点

`set-hostname` 需 root，且立即永久生效；只想临时改名改用 `hostname` 命令。
