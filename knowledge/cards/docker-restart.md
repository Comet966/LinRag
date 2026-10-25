## docker restart

停止并重新启动已有容器。

### 常用参数

- `--timeout SECONDS`：设置停止阶段等待时间。
- `--signal SIGNAL`：指定停止信号。

### 常用例子

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
