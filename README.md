# AI Templates

跨项目共享的代码模板库，支持以下内容：

- 代码片段（Snippets）
- 文件模板（Files）
- 项目模板（Projects）
- 配置模板（Configs）

## 仓库结构

```
templates/
├── snippets/                      # 代码片段
│   ├── authentication/            # 认证相关
│   ├── authorization/            # 授权相关
│   ├── database/                 # 数据库相关
│   ├── api/                     # API相关
│   ├── frontend/                # 前端相关
│   ├── backend/                 # 后端相关
│   ├── utils/                   # 工具函数
│   ├── test/                    # 测试相关
│   ├── validation/              # 验证相关
│   └── error-handling/          # 错误处理
├── files/                        # 文件模板
│   ├── config/                  # 配置文件
│   ├── documentation/            # 文档文件
│   ├── scripts/                 # 脚本文件
│   ├── docker/                  # Docker相关
│   ├── env/                     # 环境变量
│   └── readme/                  # README文件
├── projects/                      # 项目模板
│   ├── web/                     # Web应用
│   ├── backend/                 # 后端服务
│   ├── mobile/                  # 移动应用
│   ├── cli/                     # CLI工具
│   ├── library/                 # 库/包
│   └── full-stack/              # 全栈应用
└── configs/                      # 配置模板
    ├── claude/                  # Claude配置
    ├── docker/                  # Docker配置
    ├── kubernetes/             # K8s配置
    ├── ci/                      # CI/CD配置
    ├── deployment/              # 部署配置
    ├── nginx/                   # Nginx配置
    └── postgresql/             # PostgreSQL配置
```

## 使用方式

### 通过code-saver技能使用

```python
# 保存代码片段
Skill("code-saver", save_code(
    code="...",
    filename="jwt-auth.py",
    path="templates/snippets/authentication/"
))

# 获取项目模板
Skill("code-saver", get_template(
    name="web/nextjs-app",
    source="github"
))
```

### 直接使用

```bash
# 克隆仓库
git clone https://github.com/risckee/ai-templates.git

# 获取模板
cp -r ai-templates/templates/projects/web/nextjs-app/ my-project/
```

## 命名规范

### 文件命名

| 类型 | 格式 | 示例 |
|------|------|------|
| 代码片段 | 小写+连字符 | `jwt-auth.py`, `user-service.ts` |
| 文件模板 | 小写+连字符 | `claude-config.template` |
| 项目模板 | 小写+连字符 | `nextjs-app`, `fastapi-backend` |
| 配置模板 | 小写+连字符 | `deployment-config.yml` |

### 提交信息

使用语义化提交信息：

| 类型 | 说明 | 示例 |
|------|------|------|
| feat | 新功能 | `feat: add JWT authentication snippet` |
| fix | 修复 | `fix: correct OAuth2 flow` |
| docs | 文档 | `docs: update README with categories` |

## 分类体系

### Snippets分类

- authentication
- authorization
- database
- api
- frontend
- backend
- utils
- test
- validation
- error-handling

### Files分类

- config
- documentation
- scripts
- docker
- env
- readme

### Projects分类

- web
- backend
- mobile
- cli
- library
- full-stack

### Configs分类

- claude
- docker
- kubernetes
- ci
- deployment
- nginx
- postgresql

## 贡献指南

1. 确定模板类型和分类
2. 按照命名规范创建文件
3. 添加必要的元数据
4. 使用语义化提交信息
5. 更新README（如需要）

## 贡献标准

- ✅ 代码格式规范
- ✅ 包含必要注释
- ✅ 添加使用说明
- ✅ 列出依赖项

## 相关资源

- [Code Saver技能](C:\Users\ryan\.agents\skills\code-saver)
- [元项目](f:\AI项目\元项目)
- [AI助理团队](f:\AI项目\AI助理团队)

---

*更新日期：2026-03-11*
