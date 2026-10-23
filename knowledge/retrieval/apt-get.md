# apt-get 检索说明

## 用途与查询表达

Debian/Ubuntu 包管理工具。适用实现：APT。

- 安装软件包。
- 更新软件源。
- 彻底卸载软件。
- 清理 apt 缓存。

## 参数与行为

- `update`：刷新软件源索引。
- `install 包名`：安装并解决依赖。
- `remove 包名`：卸载，保留配置文件。
- `purge 包名`：卸载并删除配置文件。
- `upgrade`：升级已安装的包。
- `autoremove`：删除无用依赖包。
- `-s`：模拟执行，不实际改动。

## 常见任务示例

**1. 更新索引并安装 nginx**

```bash
sudo apt-get update && sudo apt-get install -y nginx
```

**2. 模拟升级，不实际改动**

```bash
apt-get -s upgrade
```

**3. 彻底卸载并清理**

```bash
sudo apt-get purge nginx
```

## 边界与易混淆点

只用于 Debian/Ubuntu，RHEL 系用 yum 或 dnf；update 只刷索引，安装卸载需 sudo。
