# dnf 检索说明

## 用途与查询表达

Fedora、RHEL 8+ 的包管理器。适用实现：DNF。

- 安装软件包。
- 回滚升级操作。
- 查文件所属包。
- 清理 dnf 缓存。

## 参数与行为

- `install 包名`：安装包及依赖。
- `remove 包名`：卸载包。
- `upgrade`：升级全部或指定包。
- `provides 路径`：查文件所属包。
- `history`：查看并回滚事务。
- `check-update`：检查可升级的包。
- `clean all`：清理缓存。

## 常见任务示例

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

## 边界与易混淆点

用于 Fedora 与 RHEL 8+，旧系统仍是 yum；不要与 apt-get 混用，升级前先看 history。
