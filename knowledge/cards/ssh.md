## ssh

通过加密连接登录远程主机或执行命令。

### 常用参数

- `-p PORT`：指定远程端口。
- `-i FILE`：指定身份密钥文件。
- `-l USER`：指定远程用户名。
- `-L SPEC`：设置本地端口转发。
- `-N`：不执行远程命令，常用于转发。
- `-v`：显示调试信息。

### 常用例子

**1. 连接指定用户和端口的远程主机**

```bash
ssh -p 2222 user@example.com
```

**2. 使用指定私钥登录远程主机**

```bash
ssh -i ~/.ssh/id_ed25519 user@example.com
```

**3. 通过远程主机转发本机 8080 端口到远端本机的 80 端口**

```bash
ssh -N -L 127.0.0.1:8080:127.0.0.1:80 user@example.com
```

**4. 不打开交互 shell，直接查询远端内核版本**

```bash
ssh user@example.com 'uname -r'
```
