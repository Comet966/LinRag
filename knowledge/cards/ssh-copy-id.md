## ssh-copy-id

把本机公钥装到远端账户的授权列表。

### 常用参数

- `-i FILE`：指定要安装的公钥文件。
- `-p PORT`：指定远端 SSH 端口。
- `-f`：跳过确认直接安装。
- `-n`：试运行，只显示将做的事。
- `-o OPT`：传给 ssh 的选项。
- `-h`：显示帮助。

### 常用例子

**1. 安装默认公钥到远端用户**

```bash
ssh-copy-id user@host.example.com
```

**2. 指定公钥文件与端口安装**

```bash
ssh-copy-id -i /tmp/id_demo.pub -p 2222 user@host.example.com
```
