## chgrp

修改文件或目录的所属用户组。

### 常用参数

- `-R`：递归处理子目录与文件。
- `-v`：逐个显示处理结果。
- `-c`：只在确有更改时输出。
- `-f`：不显示错误信息。
- `-h`：只改符号链接本身。
- `--reference=RFILE`：组改为参考文件的组。

### 常用例子

**1. 改单个文件的所属组**

```bash
chgrp www-data index.html
```

**2. 递归改整棵目录树**

```bash
chgrp -R www-data /var/www
```

**3. 参照另一个文件同步组**

```bash
chgrp --reference=ref.txt a.txt
```
