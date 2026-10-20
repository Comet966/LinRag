# env 检索说明

## 用途与查询表达

显示环境变量，或在指定环境中运行命令。适用实现：GNU coreutils。

- 临时设置环境变量。
- 清空环境执行程序。
- 查看环境变量。

## 参数与行为

- `-i`：以空环境开始。
- `-u NAME`：移除指定环境变量。
- `NAME=VALUE`：为本次执行设置变量。

## 常见任务示例

**1. 用指定语言环境运行一次 date**

```bash
env LANG=C date
```

**2. 从子命令的环境中移除代理变量**

```bash
env -u HTTPS_PROXY -u https_proxy curl -I https://example.com/
```

## 边界与易混淆点

NAME=VALUE 是赋值操作数，不是选项；只影响子命令及其子进程，不改变父 shell。
