# git config 检索说明

## 用途与查询表达

读取和设置 Git 配置项。适用实现：Git。

- 设置 Git 用户名和邮箱。
- 查看 Git 配置来源。
- 全局配置与仓库配置区别。

## 参数与行为

- `--global`：操作当前用户的全局配置。
- `--local`：操作当前仓库配置。
- `--get KEY`：读取指定配置项。
- `--show-origin`：显示配置来源。

## 常见任务示例

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

## 边界与易混淆点

默认写入当前仓库配置；--global 影响当前用户的其他仓库。不要把凭据直接写入可分享的配置或命令历史。
