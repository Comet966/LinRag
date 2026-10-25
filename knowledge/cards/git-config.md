## git config

读取和设置 Git 配置项。

### 常用参数

- `--global`：操作当前用户的全局配置。
- `--local`：操作当前仓库配置。
- `--get KEY`：读取指定配置项。
- `--show-origin`：显示配置来源。

### 常用例子

**1. 查看当前提交者姓名**

```bash
git config --get user.name
```

**2. 设置当前用户的提交者姓名**

```bash
git config --global user.name "Your Name"
```

**3. 检查配置的来源文件**

```bash
git config --list --show-origin
```
