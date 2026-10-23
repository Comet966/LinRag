# service 检索说明

## 用途与查询表达

管理系统服务脚本。适用实现：initscripts（systemd 兼容）。

- 查询服务状态。
- 启动或停止服务。
- 服务启停报错。
- SysV 脚本服务。

## 参数与行为

- `--status-all`：列出所有服务的状态。
- `status`：查询服务当前运行状态。
- `start`：启动指定服务。
- `stop`：停止指定服务。
- `restart`：重启服务，会短暂中断。
- `reload`：重载配置，不中断服务。

## 常见任务示例

**1. 查看所有服务启停状态**

```bash
service --status-all
```

**2. 查询指定服务状态**

```bash
service ssh status
```

**3. 重载服务配置，不重启进程**

```bash
service ssh reload
```

## 边界与易混淆点

service 只是 SysV 兼容包装，systemd 下转调 systemctl；脚本在 /etc/init.d，名字因发行版而异。
