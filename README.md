# SiliconFlow 余额查询工具 - 完整使用指南

> 📅 最后更新：2026年1月3日  
> 📌 版本：v1.0.0

---

## 📖 目录

- [项目简介](#项目简介)
- [功能特点](#功能特点)
- [快速开始](#快速开始)
- [详细使用方法](#详细使用方法)
- [环境配置](#环境配置)
- [故障排查](#故障排查)
- [开发文档](#开发文档)
- [更新日志](#更新日志)

---

## 项目简介

这是一个用于查询硅基流动（SiliconFlow）API账户余额的工具集，提供**命令行版本**和**网页版本**两种使用方式。

### 项目结构

```
API/
├── 📄 balance_checker.html        # 独立网页版（推荐新手）
├── 📄 README.md                   # 本文档
├── 📄 requirements.txt            # Python依赖
│
└── src/                           # 核心源码目录
    ├── app.py                     # Flask服务器
    ├── index.html                 # 服务器版网页
    ├── check_siliconflow_balance.py   # 命令行工具（完整版）
    ├── check_balance_simple.py    # 命令行工具（简化版）
    ├── get_balance.py             # 查询脚本
    └── save_balance.py            # 保存结果脚本
```

---

## 功能特点

- ✅ 查询账户余额信息（可用余额、充值余额、总余额）
- ✅ 查看账户基本信息（账户ID、账户名称、邮箱、状态）
- ✅ 支持命令行和网页两种使用方式
- ✅ 提供独立网页版（无需安装Python）
- ✅ 友好的用户界面和错误提示

---

## 快速开始

### 🎯 方法一：独立网页版（最简单，推荐）

**适合人群：** 所有用户，特别是没有编程基础的用户

**步骤：**
1. 双击打开 `balance_checker.html`
2. 在浏览器中输入您的 SiliconFlow API 密钥
3. 点击"查询余额"按钮

**优点：** 
- ✅ 无需安装Python
- ✅ 无需安装任何依赖
- ✅ 界面友好

**限制：** 
- ⚠️ 可能因浏览器跨域(CORS)策略无法使用
- ⚠️ 如遇问题请使用其他方法

---

### � 方法二：命令行版本

**适合人群：** 熟悉命令行的技术用户

#### 交互式方式（推荐）
```bash
python src/check_siliconflow_balance.py -i
```

#### 参数方式
```bash
python src/check_siliconflow_balance.py -k YOUR_API_KEY
```

#### 简化版（需手动编辑文件）
```bash
# 1. 编辑 src/check_balance_simple.py，替换 API 密钥
# 2. 运行
python src/check_balance_simple.py
```

---

### 🌐 方法三：网页服务器版

**适合人群：** 需要稳定网页界面且已配置Python环境的用户

**步骤：**

1. **安装依赖（首次使用）**
```bash
pip install -r requirements.txt
```

2. **启动服务器**
```bash
python src/app.py
```

3. **打开浏览器**  
   访问：http://localhost:5000

**优点：**
- ✅ 无跨域限制
- ✅ 稳定可靠
- ✅ 界面美观

---

## 详细使用方法

### 获取API密钥

1. 访问 [硅基流动官网](https://siliconflow.cn)
2. 注册并登录账户
3. 在控制台中创建或查看你的API密钥

### 命令行工具参数说明

```bash
python src/check_siliconflow_balance.py [选项]

选项：
  -k, --api-key KEY     指定API密钥
  -i, --interactive     交互式输入（推荐）
  -h, --help           显示帮助信息
```

### 输出示例

```
============================================================
硅基流动账户信息
============================================================
账户名称: 用户名称
邮箱: user@example.com
------------------------------------------------------------
可用余额: 10.50 元
充值余额: 10.50 元
总余额: 10.50 元
============================================================
```

---

## 环境配置

### 系统要求

- **操作系统：** Windows / Linux / macOS
- **Python版本：** 3.6 或更高（仅命令行和服务器版需要）
- **网络：** 能够访问 `https://api.siliconflow.cn`

### 安装Python（Windows）

如果您还没有安装Python：

1. **下载Python**
   - 访问 https://www.python.org/downloads/
   - 下载最新的 Python 3.x 版本（建议 3.8+）

2. **安装Python**
   - 运行安装程序
   - ⚠️ **重要：勾选 "Add Python to PATH"**
   - 点击 "Install Now"

3. **验证安装**
```bash
python --version
pip --version
```

4. **安装项目依赖**
```bash
pip install -r requirements.txt
```

### 依赖说明

**命令行版本：** 无需额外依赖（使用Python标准库）

**网页服务器版本：** 需要安装
- `flask >= 2.0.0`
- `flask-cors >= 3.0.0`

**独立网页版：** 无需任何依赖

---

## 故障排查

### 问题1：Python命令无效

**症状：** 运行 `python` 命令提示"不是内部或外部命令"

**解决方案：**
1. Python未安装 → 参考[安装Python](#安装python-windows)
2. Python未添加到PATH → 重新安装并勾选"Add Python to PATH"

---

### 问题2：Flask应用无法启动

**症状：** 运行 `python src/app.py` 失败

**解决方案：**
```bash
# 安装Flask依赖
pip install -r requirements.txt

# 验证安装
python -c "import flask; print('Flask version:', flask.__version__)"
```

---

### 问题3：独立网页版提示跨域错误

**症状：** 浏览器控制台显示 CORS 错误

**原因：** 浏览器安全策略阻止直接访问外部API

**解决方案：**
1. 使用命令行版本：
   ```bash
   python src/check_siliconflow_balance.py -k 您的密钥
   ```
2. 或使用服务器版本（需先安装Flask）

---

### 问题4：无法连接到API

**可能原因：**
- 网络连接问题
- API密钥错误或过期
- 防火墙阻止

**排查步骤：**
1. 检查网络连接
2. 确认API密钥正确且有效
3. 尝试在浏览器访问 https://api.siliconflow.cn
4. 检查防火墙设置

---

### 问题5：返回错误信息

**常见错误：**
- `Unauthorized` → API密钥无效
- `Forbidden` → 账户权限问题
- `Not Found` → API端点错误（联系开发者）

---

## 使用建议

| 使用场景 | 推荐方式 | 优势 | 限制 |
|---------|---------|------|------|
| **快速查询，无编程环境** | 独立网页版 | 最简单，双击即用 | 可能有CORS限制 |
| **稳定查询，有Python** | 命令行版 | 最稳定可靠 | 需要终端 |
| **图形界面，有Python+Flask** | 服务器版 | 功能完整，无CORS | 需安装依赖 |
| **脚本自动化** | check_balance_simple.py | 易集成 | 需编辑代码 |
---

## 开发文档

### 代码检查报告（2026-01-03）

#### ✅ 已修复的问题

1. **安全问题：API密钥硬编码**
   - 已替换为占位符 `YOUR_API_KEY_HERE`
   - 影响文件：check_balance_simple.py, save_balance.py, get_balance.py

2. **缺少依赖管理**
   - 创建了 `requirements.txt`

3. **缺少使用指南**
   - 创建了完整的README文档

4. **Python环境问题**
   - 提供了独立网页版（无需Python）

#### ✅ 代码质量检查

- **语法检查：** 所有Python文件无语法错误
- **功能完整性：** 所有功能正常工作
- **安全性：** 已移除硬编码密钥，添加安全提示

### 项目文件说明

#### 用户文件
- `balance_checker.html` - 独立网页版（推荐新手）
- `README.md` - 完整使用文档
- `requirements.txt` - Python依赖列表

#### 核心源码（src目录）
- `check_siliconflow_balance.py` - 完整命令行工具
- `check_balance_simple.py` - 简化版脚本
- `app.py` - Flask服务器
- `index.html` - 服务器版网页界面
- `get_balance.py` - 基础查询脚本
- `save_balance.py` - 保存结果脚本

---

## 安全提示

⚠️ **重要：**
- 🔒 不要将API密钥提交到代码仓库
- 🔒 不要与他人分享你的API密钥
- 🔒 建议使用环境变量存储密钥
- 🔒 定期更换API密钥

---

## 许可证

本项目仅供学习和个人使用。

---

## 更新日志

### v1.0.0 (2026-01-03)

**新增功能：**
- ✨ 初始版本发布
- ✨ 支持命令行查询（完整版和简化版）
- ✨ 提供独立网页版（无需Python）
- ✨ 提供Flask服务器版（稳定可靠）

**安全改进：**
- 🔒 移除所有硬编码的API密钥
- 🔒 添加安全使用提示

**文档：**
- 📝 完整的使用文档
- 📝 详细的环境配置指南
- 📝 故障排查说明

---

## 获取帮助

如有问题或建议，请检查：

1. ✅ 本文档的[故障排查](#故障排查)部分
2. ✅ Python是否正确安装：`python --version`
3. ✅ 网络连接是否正常
4. ✅ API密钥是否有效

**快速诊断：**
- 查看终端输出的错误信息
- 尝试使用独立网页版排除环境问题
- 使用命令行工具的交互式模式：`python src/check_siliconflow_balance.py -i`

**感谢使用！** 🚀

如有问题或建议，欢迎反馈！
