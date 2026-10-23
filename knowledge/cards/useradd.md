## useradd

创建新的本地用户账户。

### 常用参数

- `-m`：创建家目录。
- `-s SHELL`：指定登录 shell。
- `-g GROUP`：指定主组，需已存在。
- `-G G1,G2`：指定附加组，逗号分隔。
- `-u UID`：指定用户 ID。
- `-r`：创建系统账户。

### 常用例子

**1. 创建普通用户**

```bash
sudo useradd -m -s /bin/bash alice
```

**2. 创建并加入附加组**

```bash
sudo useradd -m -G developers,docker bob
```

**3. 创建不可登录服务账户**

```bash
sudo useradd -r -s /usr/sbin/nologin svcapp
```
