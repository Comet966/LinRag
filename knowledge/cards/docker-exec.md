## docker exec

在已经运行的容器中执行新进程。

### 常用参数

- `-i`：保持标准输入。
- `-t`：分配伪终端。
- `-u USER`：指定执行用户。
- `-w DIR`：设置容器内工作目录。

### 常用例子

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
