## tmux

终端复用器，管理多个会话。

### 常用参数

- `new -s 名称`：新建并进入会话。
- `attach -t 名称`：接入已有会话。
- `ls`：列出所有会话。
- `detach`：脱离会话，进程继续运行。
- `split-window -h`：左右分屏。
- `send-keys -t 名称`：向会话发送命令。

### 常用例子

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
