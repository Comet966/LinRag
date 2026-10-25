## uv lock

解析项目依赖并创建或更新 uv.lock。

### 常用参数

- `--check`：只检查锁文件是否最新。
- `--upgrade`：允许升级所有锁定依赖。
- `--upgrade-package NAME`：允许升级指定包。

### 常用例子

**1. 生成或刷新锁文件**

```bash
uv lock
```

**2. 检查清单与锁文件一致性**

```bash
uv lock --check
```

**3. 仅为指定包允许升级**

```bash
uv lock --upgrade-package httpx
```
