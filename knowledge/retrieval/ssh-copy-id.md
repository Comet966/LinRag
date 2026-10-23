# ssh-copy-id 检索说明

## 用途与查询表达

把公钥装到远端账户。适用实现：OpenSSH。

- 免密登录配置。
- 安装公钥。
- 复制公钥到远端。
- 仍要输入密码。

## 参数与行为

- `-i FILE`：指定要安装的公钥文件。
- `-p PORT`：指定远端 SSH 端口。
- `-f`：跳过确认直接安装。
- `-n`：试运行，只显示将做的事。
- `-o OPT`：传给 ssh 的选项。
- `-h`：显示帮助。

## 常见任务示例

**1. 安装默认公钥到远端用户**

```bash
ssh-copy-id user@host.example.com
```

**2. 指定公钥文件与端口安装**

```bash
ssh-copy-id -i /tmp/id_demo.pub -p 2222 user@host.example.com
```

## 边界与易混淆点

公钥写进远端 ~/.ssh/authorized_keys；需远端允许密码登录，私钥不要外传。
