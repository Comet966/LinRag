# chsh 检索说明

## 用途与查询表达

更改用户登录时使用的 shell。适用实现：shadow-utils。

- 换成 zsh 怎么改。
- 查看可用 shell。
- shell 改了没生效。
- 帮他人改 shell。

## 参数与行为

- `-s SHELL`：指定新的登录 shell。
- `--shell=SHELL`：`-s` 的长选项写法。
- `-l`：列出 /etc/shells 中的 shell。
- `-h`：显示帮助信息。
- `-R DIR`：在指定根目录下操作。

## 常见任务示例

**1. 列出系统可用的 shell**

```bash
chsh -l
```

**2. 把登录 shell 换成 bash**

```bash
chsh -s /bin/bash
```

**3. 为指定用户改 shell**

```bash
chsh -s /bin/zsh alice
```

## 边界与易混淆点

写入 `/etc/passwd`，新 shell 要在 `/etc/shells` 里；当前会话不受影响，重登才生效。
