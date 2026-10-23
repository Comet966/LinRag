## setfacl

设置文件的访问控制列表 ACL。

### 常用参数

- `-m RULE`：添加或修改一条 ACL 规则。
- `-x RULE`：删除指定用户或组的规则。
- `-b`：删除所有扩展 ACL 规则。
- `-d`：设置目录默认规则，供新文件继承。
- `-R`：递归处理目录下所有文件。
- `--test`：只测试，不写入任何更改。

### 常用例子

**1. 给用户 alice 加读写权限**

```bash
setfacl -m u:alice:rw /tmp/demo.txt
```

**2. 查看 ACL 是否生效**

```bash
getfacl /tmp/demo.txt
```

**3. 删掉 alice 的规则并核对**

```bash
setfacl -x u:alice /tmp/demo.txt
```
