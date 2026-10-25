## uv add

向项目清单添加依赖并更新项目环境。

### 常用参数

- `--dev`：加入 dev 依赖组。
- `--group NAME`：加入指定依赖组。
- `--optional EXTRA`：加入可选依赖。
- `--no-sync`：不立即同步环境。

### 常用例子

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
