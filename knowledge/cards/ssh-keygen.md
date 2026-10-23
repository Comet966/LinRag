## ssh-keygen

生成、查看和管理 SSH 密钥对。

### 常用参数

- `-t TYPE`：指定密钥类型，如 ed25519。
- `-b BITS`：指定密钥位数。
- `-C TEXT`：为公钥添加注释。
- `-f FILE`：指定密钥保存路径。
- `-N PASS`：设置或置空口令。
- `-l`：显示公钥指纹。
- `-y`：从私钥导出公钥。

### 常用例子

**1. 生成测试密钥到 /tmp**

```bash
ssh-keygen -t ed25519 -f /tmp/demo_key -N ''
```

**2. 查看公钥指纹确认类型**

```bash
ssh-keygen -lf /tmp/demo_key.pub
```
