## dpkg

操作本地 deb 包和包数据库。

### 常用参数

- `-i 包.deb`：安装本地 deb 包。
- `-r 包名`：卸载，保留配置。
- `-P 包名`：卸载并删除配置。
- `-L 包名`：列出包安装的文件。
- `-S 路径`：反查文件所属包。
- `-l`：列出已安装的包。

### 常用例子

**1. 安装本地 deb 包**

```bash
sudo dpkg -i ./app_1.0_amd64.deb
```

**2. 补齐缺失的依赖**

```bash
sudo apt-get install -f
```

**3. 查文件属于哪个包**

```bash
dpkg -S /usr/sbin/nginx
```
