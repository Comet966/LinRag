# docker restart 检索说明

## 用途与查询表达

停止并重新启动已有容器。适用实现：Docker CLI / Docker Engine。

- 重启 Docker 容器。
- 容器重启超时。
- 重启 Web 服务。

## 参数与行为

- `--timeout SECONDS`：设置停止阶段等待时间。
- `--signal SIGNAL`：指定停止信号。

## 常见任务示例

**1. 重启指定容器**

```bash
docker restart demo-web
```

**2. 给容器三十秒退出再启动**

```bash
docker restart --timeout 30 demo-web
```

**3. 重启两个指定容器**

```bash
docker restart demo-web demo-worker
```

## 边界与易混淆点

会造成服务短暂中断；不会根据新的 Dockerfile、镜像标签或 Compose 文件重新创建容器。
