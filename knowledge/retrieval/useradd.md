# useradd 检索说明

## 用途与查询表达

创建新的本地用户账户。适用实现：shadow-utils。

- 怎么新建用户。
- 建用户指定家目录。
- 新用户加入组。
- 创建系统账户。

## 参数与行为

- `-m`：创建家目录。
- `-s SHELL`：指定登录 shell。
- `-g GROUP`：指定主组，需已存在。
- `-G G1,G2`：指定附加组，逗号分隔。
- `-u UID`：指定用户 ID。
- `-r`：创建系统账户。

## 常见任务示例

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

## 边界与易混淆点

useradd 不设密码，新账户无法密码登录；Debian 上 adduser 是交互式封装。
