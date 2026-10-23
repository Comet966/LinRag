# tmux 检索说明

## 用途与查询表达

终端复用器，管理多个会话、窗口和窗格。适用实现：tmux。

- 断开 SSH 继续跑。
- 新建和恢复会话。
- 一个终端开多窗口。
- tmux 前缀键是什么。

## 参数与行为

- `new -s 名称`：新建并进入会话。
- `attach -t 名称`：接入已有会话。
- `ls`：列出所有会话。
- `detach`：脱离会话，进程继续运行。
- `split-window -h`：左右分屏。
- `send-keys -t 名称`：向会话发送命令。

## 常见任务示例

**1. 新建 work 会话**

```bash
tmux new -s work
```

**2. 重新接入会话**

```bash
tmux attach -t work
```

**3. 给会话发命令**

```bash
tmux send-keys -t work 'tail -n 20 app.log' Enter
```

## 边界与易混淆点

前缀键默认 Ctrl+b；会话含窗口，窗口再分窗格；detach 不结束进程。
