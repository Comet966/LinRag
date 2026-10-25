# pip list 检索说明

## 用途与查询表达

列出 Python 环境中已经安装的软件包。适用实现：pip（示例通过 Python 3 调用）。

- 查看 Python 已安装包。
- 列出可升级依赖。
- pip 包列表 JSON。

## 参数与行为

- `--format FORMAT`：指定 columns、freeze 或 json 输出。
- `--outdated`：列出有新版本的包。
- `--local`：在可访问全局包的虚拟环境中只列本地包。

## 常见任务示例

**1. 查看安装的软件包**

```bash
python3 -m pip list
```

**2. 输出 JSON 包列表**

```bash
python3 -m pip list --format json
```

**3. 检查可升级的包**

```bash
python3 -m pip list --outdated
```

## 边界与易混淆点

outdated 通常需要访问包索引；list 展示安装状态，不等于可以重现环境的完整依赖锁文件。
