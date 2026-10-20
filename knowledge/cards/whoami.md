## whoami

显示当前有效用户的名称。

### 常用参数

- `--help`：显示帮助。
- `--version`：显示版本。

### 常用例子

**1. 确认当前命令以哪个用户身份运行**

```bash
whoami
```

**2. 通过 sudo 启动子命令，确认其有效用户（需相应权限）**

```bash
sudo -u alice whoami
```
