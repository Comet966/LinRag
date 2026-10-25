# git reflog 检索说明

## 用途与查询表达

查看本地引用曾经指向的提交记录。适用实现：Git 2.23+。

- 找回误删提交。
- 查看 reset 前的 HEAD。
- 找回变基前的提交。

## 参数与行为

- `show REF`：显示指定引用日志。
- `--all`：显示所有引用日志。
- `--date=iso`：使用 ISO 日期格式。

## 常见任务示例

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

## 边界与易混淆点

记录只属于本地且可能过期；reflog 是查找线索，不保证永久保存或恢复已清理的对象。
