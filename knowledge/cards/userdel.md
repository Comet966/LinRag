## userdel

删除用户账户及其家目录。

### 常用参数

- `userdel USER`：只删账户，保留家目录。
- `-r`：同时删除家目录和邮件。
- `-f`：强制删除，即使用户已登录。
- `-R DIR`：在 chroot 目录下操作。
- `-P DIR`：在前缀目录下操作。
- `-Z`：清理 SELinux 用户映射。

### 常用例子

**1. 删除账户保留家目录**

```bash
sudo userdel alice
```

**2. 删除前查残留进程**

```bash
id alice; pgrep -u alice -a
```

**3. 连家目录一起删除**

```bash
sudo userdel -r alice
```
