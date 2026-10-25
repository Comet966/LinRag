## git clone

克隆远程或本地仓库并建立工作副本。

### 常用参数

- `--depth N`：限制克隆历史深度。
- `--branch NAME`：检出指定分支或标签。
- `--single-branch`：只克隆选定分支的历史。
- `--recurse-submodules`：初始化并克隆子模块。

### 常用例子

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
