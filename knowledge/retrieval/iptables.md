# iptables 检索说明

## 用途与查询表达

查看和配置 netfilter 过滤规则。适用实现：iptables。

- 查看现有防火墙规则。
- 规则加了不生效。
- 重启后规则全没了。
- 和 nft 什么关系。

## 参数与行为

- `-t TABLE`：指定表，默认 filter。
- `-L`：列出链上的规则。
- `-n`：不把 IP 和端口解析成名称。
- `-v`：显示计数器等详细信息。
- `--line-numbers`：列出规则序号。
- `-S`：以命令形式打印规则。

## 常见任务示例

**1. 只读查看全部规则与计数**

```bash
iptables -L -n -v
```

**2. 带序号查看 INPUT 链**

```bash
iptables -L INPUT -n -v --line-numbers
```

**3. 以命令形式导出便于比对**

```bash
iptables -S
```

## 边界与易混淆点

规则自上而下匹配，命中即停；重启会丢，需 `iptables-save`；新版 iptables 多是 nftables 前端。
