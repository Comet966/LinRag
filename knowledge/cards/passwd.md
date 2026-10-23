## passwd

修改用户密码并管理锁定状态。

### 常用参数

- `passwd`：修改当前用户自己的密码。
- `passwd USER`：root 修改指定用户密码。
- `-l`：锁定密码，禁止密码登录。
- `-u`：解除密码锁定。
- `-e`：让密码立即过期。
- `-S`：查看密码状态。

### 常用例子

**1. 修改自己的密码**

```bash
passwd
```

**2. root 设置指定用户密码**

```bash
sudo passwd alice
```

**3. 查看密码是否被锁定**

```bash
sudo passwd -S alice
```
