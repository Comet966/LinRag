# uv add 检索说明

## 用途与查询表达

向项目清单添加依赖并更新项目环境。适用实现：uv 项目工作流。

- 向 uv 项目添加依赖。
- 添加 Python 开发依赖组。
- uv 修改 pyproject。

## 参数与行为

- `--dev`：加入 dev 依赖组。
- `--group NAME`：加入指定依赖组。
- `--optional EXTRA`：加入可选依赖。
- `--no-sync`：不立即同步环境。

## 常见任务示例

**1. 添加运行依赖**

```bash
uv add httpx
```

**2. 添加开发依赖**

```bash
uv add --dev pytest
```

**3. 添加依赖但暂不同步环境**

```bash
uv add --no-sync rich
```

## 边界与易混淆点

通常修改 pyproject.toml 和 uv.lock；--no-sync 只跳过环境同步，不等于不解析依赖或不写锁文件。
