# git clone 检索说明

## 用途与查询表达

克隆远程或本地仓库并建立工作副本。适用实现：Git 2.23+。

- 下载 Git 仓库。
- 克隆指定分支。
- 浅克隆项目。

## 参数与行为

- `--depth N`：限制克隆历史深度。
- `--branch NAME`：检出指定分支或标签。
- `--single-branch`：只克隆选定分支的历史。
- `--recurse-submodules`：初始化并克隆子模块。

## 常见任务示例

**1. 克隆项目到指定目录**

```bash
git clone https://github.com/Comet966/LinRag.git linrag-demo
```

**2. 浅克隆 main 分支**

```bash
git clone --depth 1 --branch main https://github.com/Comet966/LinRag.git linrag-shallow
```

**3. 克隆时包含子模块**

```bash
git clone --recurse-submodules https://example.com/team/project.git project
```

## 边界与易混淆点

示例仓库地址需要按目标替换；浅克隆缺少部分历史，子模块可能需要额外权限。
