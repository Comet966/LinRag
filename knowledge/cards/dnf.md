## dnf

Fedora、RHEL 8+ 的包管理器。

### 常用参数

- `install 包名`：安装包及依赖。
- `remove 包名`：卸载包。
- `upgrade`：升级全部或指定包。
- `provides 路径`：查文件所属包。
- `history`：查看并回滚事务。
- `check-update`：检查可升级的包。
- `clean all`：清理缓存。

### 常用例子

**1. 安装 nginx**

```bash
sudo dnf install -y nginx
```

**2. 查文件所属包**

```bash
dnf provides /usr/sbin/sshd
```

**3. 查看可升级的包**

```bash
dnf check-update
```
