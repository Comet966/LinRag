## docker build

根据 Dockerfile 和构建上下文构建镜像。

### 常用参数

- `-t NAME:TAG`：设置镜像名称和标签。
- `-f FILE`：指定 Dockerfile。
- `--no-cache`：不复用构建缓存。
- `--build-arg KEY=VALUE`：传入构建参数。

### 常用例子

**1. 构建当前目录镜像**

```bash
docker build -t demo:local .
```

**2. 使用指定 Dockerfile**

```bash
docker build -f Dockerfile.dev -t demo:dev .
```

**3. 不复用缓存重新构建**

```bash
docker build --no-cache -t demo:clean .
```
