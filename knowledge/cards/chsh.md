## chsh

更改用户登录时使用的 shell。

### 常用参数

- `-s SHELL`：指定新的登录 shell。
- `--shell=SHELL`：`-s` 的长选项写法。
- `-l`：列出 /etc/shells 中的 shell。
- `-h`：显示帮助信息。
- `-R DIR`：在指定根目录下操作。

### 常用例子

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
