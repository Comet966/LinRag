# insmod 检索说明

## 用途与查询表达

把指定内核模块文件加载进内核。适用实现：kmod。

- 手动加载模块。
- 加载 ko 文件。
- 装驱动模块。
- 模块加载失败。

## 参数与行为

- `-f`：忽略版本不符，强制加载。
- `-s`：错误信息写入系统日志。
- `-V`：显示版本号。
- `-h`：显示帮助信息。
- `模块文件`：必填，须为 .ko 完整路径。

## 常见任务示例

**1. 查看 insmod 支持的选项**

```bash
insmod -h
```

**2. 查看 insmod 的版本号**

```bash
insmod -V
```

**3. 按完整路径加载一个模块**

```bash
sudo insmod /lib/modules/$(uname -r)/kernel/drivers/md/raid1.ko
```

## 边界与易混淆点

`insmod` 不解决依赖、不认模块名，需 root 和完整路径；日常用 `modprobe`。
