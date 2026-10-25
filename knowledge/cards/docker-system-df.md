## docker system df

查看 Docker 对象的磁盘占用及可回收空间。

### 常用参数

- `-v`：显示更详细的对象占用。
- `--format FORMAT`：设置输出格式。

### 常用例子

**1. 查看 Docker 总体磁盘用量**

```bash
docker system df
```

**2. 查看镜像与容器占用详情**

```bash
docker system df -v
```
