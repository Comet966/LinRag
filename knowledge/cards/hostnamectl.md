## hostnamectl

查看或设置系统主机名。

### 常用参数

- `--static`：只输出静态主机名。
- `--pretty`：只输出易读主机名。
- `--transient`：只输出临时主机名。
- `-H user@host`：操作远程主机。
- `-M 容器名`：在本地容器内操作。
- `--no-ask-password`：不提示输密码。

### 常用例子

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
