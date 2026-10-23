## make

按依赖关系增量构建或干跑预览。

### 常用参数

- `-n`：干跑，只打印不执行。
- `-j N`：并行执行 N 个任务。
- `-f FILE`：指定 makefile 文件。
- `-C DIR`：先进入 DIR 再读 makefile。
- `-s`：静默，不打印命令行。
- `-k`：出错后继续处理其它目标。
- `-B`：无条件重建所有目标。

### 常用例子

**1. 干跑查看将执行哪些命令**

```bash
make -n
```

**2. 干跑并指定 makefile**

```bash
make -n -f Makefile.test
```

**3. 干跑：先进目录再构建**

```bash
make -n -C /data/project
```
