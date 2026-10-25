## docker start

启动已经存在但停止的容器。

### 常用参数

- `-a`：连接容器输出。
- `-i`：连接标准输入。

### 常用例子

**1. 启动已有容器**

```bash
docker start demo-web
```

**2. 启动并观察输出**

```bash
docker start -a demo-worker
```

**3. 启动已有交互容器**

```bash
docker start -ai demo-shell
```
