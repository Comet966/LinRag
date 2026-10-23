# usermod 检索说明

## 用途与查询表达

修改已有用户的属性和组。适用实现：shadow-utils。

- 把用户加到组。
- 修改用户名。
- 锁定某个账户。
- 用户加组不生效。

## 参数与行为

- `-aG GROUP`：追加附加组，保留原有组。
- `-G GROUP`：重设附加组，会覆盖原值。
- `-l NAME`：修改登录名。
- `-d DIR`：修改家目录路径。
- `-m`：配合 `-d` 迁移家目录内容。
- `-L`：锁定密码。
- `-U`：解除密码锁定。

## 常见任务示例

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

## 边界与易混淆点

`-G` 不带 `-a` 会覆盖原有附加组；`-l` 改名不改家目录。
