## sha256sum

计算或核对文件的 SHA-256 摘要。

### 常用参数

- `-c`：按清单核对摘要。
- `--quiet`：只输出校验失败项。
- `--status`：不输出，只用退出码。
- `-b`：以二进制模式读取。
- `--tag`：输出 BSD 风格摘要。

### 常用例子

**1. 生成 SHA-256 清单**

```bash
sha256sum ubuntu.iso > ubuntu.iso.sha256
```

**2. 按清单核对镜像**

```bash
sha256sum -c ubuntu.iso.sha256
```

**3. 只取摘要值**

```bash
sha256sum ubuntu.iso | cut -d ' ' -f 1
```
