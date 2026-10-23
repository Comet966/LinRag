# yum 检索说明

## 用途与查询表达

RHEL 旧版本的 RPM 包管理器。适用实现：YUM。

- 安装软件包。
- 查找包来源。
- 升级系统软件。
- 清理 yum 缓存。

## 参数与行为

- `install 包名`：安装包及其依赖。
- `remove 包名`：卸载包。
- `update`：升级全部或指定包。
- `search 关键字`：搜索软件包。
- `provides 路径`：查文件所属包。
- `check-update`：检查可升级的包。
- `clean all`：清理缓存。

## 常见任务示例

**1. 安装 httpd**

```bash
sudo yum install -y httpd
```

**2. 查命令属于哪个包**

```bash
yum provides /usr/bin/htpasswd
```

**3. 查看可升级的包**

```bash
yum check-update
```

## 边界与易混淆点

用于 RHEL/CentOS 7 及更早版本，新系统用 dnf；与 apt-get 不通用，升级前先评估。
