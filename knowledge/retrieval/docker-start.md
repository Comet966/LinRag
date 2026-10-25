# docker start 检索说明

## 用途与查询表达

启动已经存在但停止的容器。适用实现：Docker CLI / Docker Engine。

- 重新启动已停止容器。
- 恢复已有容器。
- start 与 run 区别。

## 参数与行为

- `-a`：连接容器输出。
- `-i`：连接标准输入。

## 常见任务示例

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

## 边界与易混淆点

沿用创建时的镜像、端口和挂载配置，不通过 start 修改这些配置；run 会创建新容器。
