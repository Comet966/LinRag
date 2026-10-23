# setfacl 检索说明

## 用途与查询表达

设置文件 ACL 规则。适用实现：acl。

- 给用户单独授权。
- 查看文件 ACL。
- 删除 ACL 规则。
- 目录默认 ACL。

## 参数与行为

- `-m RULE`：添加或修改一条 ACL 规则。
- `-x RULE`：删除指定用户或组的规则。
- `-b`：删除所有扩展 ACL 规则。
- `-d`：设置目录默认规则，供新文件继承。
- `-R`：递归处理目录下所有文件。
- `--test`：只测试，不写入任何更改。

## 常见任务示例

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

## 边界与易混淆点

ls -l 权限末尾带 + 说明有 ACL；-b 清扩展规则，-x 只删单条，改完用 getfacl 复核。
