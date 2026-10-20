## env

显示环境变量，或在指定环境中运行命令。

### 常用参数

- `-i`：以空环境开始。
- `-u NAME`：移除指定环境变量。
- `NAME=VALUE`：为本次执行设置变量。

### 常用例子

**1. 用指定语言环境运行一次 date**

```bash
env LANG=C date
```

**2. 从子命令的环境中移除代理变量**

```bash
env -u HTTPS_PROXY -u https_proxy curl -I https://example.com/
```
