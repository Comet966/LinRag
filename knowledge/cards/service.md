## service

以 SysV 脚本方式管理服务状态。

### 常用参数

- `--status-all`：列出所有服务的状态。
- `status`：查询服务当前运行状态。
- `start`：启动指定服务。
- `stop`：停止指定服务。
- `restart`：重启服务，会短暂中断。
- `reload`：重载配置，不中断服务。

### 常用例子

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
