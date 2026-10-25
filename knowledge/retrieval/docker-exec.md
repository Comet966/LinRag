# docker exec 检索说明

## 用途与查询表达

在已经运行的容器中执行新进程。适用实现：Docker CLI / Docker Engine。

- 进入正在运行的容器。
- 在容器中执行命令。
- docker exec 与 run 区别。

## 参数与行为

- `-i`：保持标准输入。
- `-t`：分配伪终端。
- `-u USER`：指定执行用户。
- `-w DIR`：设置容器内工作目录。

## 常见任务示例

**1. 进入运行中容器的 shell**

```bash
docker exec -it demo-web sh
```

**2. 查看容器内部路径**

```bash
docker exec demo-web pwd
```

**3. 以指定用户查看身份**

```bash
docker exec -u 1000 demo-web id
```

## 边界与易混淆点

容器须正在运行且包含目标程序；exec 不创建新容器，在自动化管道中通常不要分配 -t。
