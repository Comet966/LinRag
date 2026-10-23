## yum

RHEL 旧版本的 RPM 包管理器。

### 常用参数

- `install 包名`：安装包及其依赖。
- `remove 包名`：卸载包。
- `update`：升级全部或指定包。
- `search 关键字`：搜索软件包。
- `provides 路径`：查文件所属包。
- `check-update`：检查可升级的包。
- `clean all`：清理缓存。

### 常用例子

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
