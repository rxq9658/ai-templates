---
type: project
category: web
language: javascript
framework: nextjs
tags: [web, fullstack, react, nextjs, typescript]
created: 2026-03-11
description: Next.js应用脚手架模板
source: templates/projects/web/nextjs-app/
github_url: https://github.com/risckee/ai-templates/tree/main/templates/projects/web/nextjs-app
---

# Next.js应用模板

## 描述

完整的Next.js应用脚手架，包含TypeScript、Tailwind CSS、API路由等现代Web开发所需的基础设施。

## 项目结构

```
nextjs-app/
├── src/
│   ├── app/                    # App Router
│   │   ├── (auth)/
│   │   │   ├── login/
│   │   │   └── register/
│   │   ├── (dashboard)/
│   │   │   └── page.tsx
│   │   ├── api/                # API路由
│   │   ├── layout.tsx
│   │   └── page.tsx
│   ├── components/            # 可复用组件
│   │   ├── ui/
│   │   ├── forms/
│   │   └── layouts/
│   ├── lib/                    # 工具函数
│   │   ├── auth.ts
│   │   ├── db.ts
│   │   └── utils.ts
│   └── types/                # TypeScript类型定义
├── public/                       # 静态资源
├── package.json
├── tsconfig.json
├── next.config.js
├── tailwind.config.js
├── postcss.config.js
├── .eslintrc.json
├── .prettierrc
└── .gitignore
```

## 技术栈

- Next.js 14（App Router）
- React 18
- TypeScript
- Tailwind CSS
- ESLint
- Prettier

## 功能特性

### 核心

- ✅ TypeScript支持
- ✅ App Router路由
- ✅ API路由
- ✅ 环境变量配置
- ✅ 布局系统

### 样式

- ✅ Tailwind CSS配置
- ✅ PostCSS支持
- ✅ 响应式设计

### 开发体验

- ✅ ESLint配置
- ✅ Prettier配置
- ✅ Git忽略文件

## 快速开始

### 1. 安装依赖

```bash
npm install
# 或
pnpm install
# 或
yarn install
```

### 2. 配置环境变量

创建 `.env.local` 文件：

```env
DATABASE_URL=postgresql://user:password@localhost:5432/mydb
NEXTAUTH_SECRET=your-secret-key-here
NEXTAUTH_URL=http://localhost:3000/api/auth
```

### 3. 启动开发服务器

```bash
npm run dev
# 访问 http://localhost:3000
```

### 4. 构建生产版本

```bash
npm run build
npm run start
```

## 开发规范

### 命名约定

- 组件：PascalCase（`UserProfile.tsx`）
- 函数：camelCase（`getUserData`）
- 常量：UPPER_SNAKE_CASE（`MAX_RETRIES`）
- 类型：PascalCase（`UserType`）

### 代码风格

- 使用2空格缩进
- 单引号字符串
- 尾部逗号
- 箭头函数

### 提交规范

```bash
feat: add user authentication feature
fix: resolve login page styling issue
docs: update API documentation
refactor: improve error handling
style: format code with Prettier
test: add unit tests for auth module
```

## 依赖说明

### 核心依赖

```json
{
  "next": "^14.0.0",
  "react": "^18.2.0",
  "react-dom": "^18.2.0",
  "typescript": "^5.3.0"
}
```

### 开发依赖

```json
{
  "@types/node": "^20.0.0",
  "@types/react": "^18.2.0",
  "tailwindcss": "^3.4.0",
  "postcss": "^8.4.0",
  "eslint": "^8.56.0",
  "prettier": "^3.1.0"
}
```

## 部署建议

### Vercel（推荐）

```bash
npm install -g vercel
vercel login
vercel --prod
```

### 其他平台

- **Netlify**: `netlify-cli`
- **AWS Amplify**: `amplify`
- **Railway**: `railway`
- **Render**: `render-cli`

## 扩展建议

### 认证

建议添加：
- NextAuth.js
- Clerk
- Supabase Auth

### 数据库

建议集成：
- Prisma ORM
- Drizzle ORM
- Supabase

### UI组件

建议添加：
- shadcn/ui
- Radix UI
- Headless UI

## 相关

- [[React应用]]
- [[全栈应用]]
- [[TypeScript]]
- [[Tailwind CSS]]
