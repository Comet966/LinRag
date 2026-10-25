## docker info

查看 Docker Engine 的系统配置和资源信息。

### 常用参数

- `--format FORMAT`：设置输出格式。
- `--help`：显示帮助。

### 常用例子

**1. 查看引擎信息**

```bash
docker info
```

**2. 读取存储驱动**

```bash
docker info --format '{{.Driver}}'
```

**3. 读取运行中的容器数**

```bash
docker info --format '{{.ContainersRunning}}'
```
