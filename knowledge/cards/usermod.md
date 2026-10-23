## usermod

修改已有用户的属性和组。

### 常用参数

- `-aG GROUP`：追加附加组，保留原有组。
- `-G GROUP`：重设附加组，会覆盖原值。
- `-l NAME`：修改登录名。
- `-d DIR`：修改家目录路径。
- `-m`：配合 `-d` 迁移家目录内容。
- `-L`：锁定密码。
- `-U`：解除密码锁定。

### 常用例子

**1. 追加到 docker 组**

```bash
sudo usermod -aG docker alice
```

**2. 修改家目录并迁移**

```bash
sudo usermod -d /data/alice -m alice
```

**3. 锁定账户密码**

```bash
sudo usermod -L alice
```
