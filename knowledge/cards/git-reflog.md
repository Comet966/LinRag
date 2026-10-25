## git reflog

查看本地引用曾经指向的提交记录。

### 常用参数

- `show REF`：显示指定引用日志。
- `--all`：显示所有引用日志。
- `--date=iso`：使用 ISO 日期格式。

### 常用例子

**1. 查看 HEAD 移动记录**

```bash
git reflog
```

**2. 查看 main 分支引用日志**

```bash
git reflog show main
```

**3. 显示全部引用日志的时间**

```bash
git reflog --all --date=iso
```
