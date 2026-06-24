# PaperLesson · 论文精读课程

> 📖 **面向组会的论文精读与报告准备**  
> 从全景概览到组会讲解，每篇论文一套精读课程。

## 项目简介

本仓库是一个**论文精读教学空间**，旨在帮助移动机器人 / AI 方向的研究者深入理解论文核心思想、技术细节和实验验证，并**准备完整的组会报告**。

目前正在精读：
- **E2Map**: Experience-and-Emotion Map for Self-Reflective Robot Navigation with Language Models

## 仓库结构

```
├── MISSION.md                        # 教学使命 —— 学习目标与路径
├── RESOURCES.md                      # 拓展资源 —— 论文、代码、社区
├── NOTES.md                          # 教学笔记
├── README.md                         # 本文件
├── 资料/                              # 原始论文（双语对照 + 图片资源）
│   ├── E2Map Experience-and-Emotion Map ....md
│   └── E2Map Experience-and-Emotion Map ....assets/
├── lessons/                          # 📚 课程文件（HTML）
│   ├── 0001-论文全景概览.html      # 第1课：论文全景概览
│   ├── 0002-E2Map核心技术.html   # 第2课：E2Map核心技术
│   ├── 0003-导航与实验分析.html # 第3课：导航系统与实验分析
│   └── 0004-组会汇报指南.html  # 第4课：组会报告组织与讲解
├── reference/                        # 📖 参考文档
│   └── glossary.html                 # 术语表（中英对照）
└── learning-records/                 # 📝 学习记录
    └── 0001-e2map-core-insights.md   # 第1篇：核心要点
```

## 📦 快速开始

### 在线浏览（推荐）

直接将项目部署到 GitHub Pages，或打开 **`index.html`** ——这是网站的入口主页，包含课程导航、参考资料和学习记录。

### 本地浏览

直接在浏览器打开主页：

```bash
# Windows
start index.html

# macOS
open index.html

# 或双击 index.html
```

从主页可以链接到所有课程。也可以直接打开单课：

```bash
start lessons\0001-论文全景概览.html   # 第1课
```

## 🏗️ 网站结构

```
├── index.html                         # 🌐 网站主页（课程导航 + 参考 + 笔记）
├── shared/
│   └── theme.css                      # 🎨 全局共享主题样式
├── data/
│   ├── course-catalog.js              # 📋 首页主数据源（collection + lessons）
│   └── lessons.json                   # 📦 旧结构快照，保留作迁移参考
├── lessons/                           # 📚 精读课程
│   ├── 0001-论文全景概览.html       # 第1课：论文全景概览
│   ├── 0002-E2Map核心技术.html    # 第2课：E2Map核心技术
│   ├── 0003-导航与实验分析.html # 第3课：导航系统与实验
│   └── 0004-组会汇报指南.html   # 第4课：组会报告要点
├── reference/
│   └── glossary.html                  # 📖 术语表（中英对照）
├── learning-records/                  # 📝 学习记录
│   └── 0001-e2map-core-insights.md
├── 资料/                              # 原始论文（双语对照 + 图片资源）
├── MISSION.md                         # 教学使命 —— 学习目标与路径
├── RESOURCES.md                       # 拓展资源 —— 论文、代码、社区
├── NOTES.md                           # 教学笔记
└── README.md                          # 本文件
```

## 📝 如何添加新课程

## 📝 开发规范

### 公式渲染
所有课程 HTML 使用 **MathJax v3** 渲染 LaTeX 公式：
- 行内公式：用 `\(...\)` 包裹（如 `\(\mathcal{M} \in \mathcal{R}^{\bar{H} \times \bar{W}}\)`）
- 块级公式：用 `\[...\]` 包裹
- MathJax CDN 已全局引入所有课程和术语表，新课程只需在 `<head>` 中添加相同脚本

### 图片引用
论文原图存放在 `资料/E2Map Experience-and-Emotion Map for Self-Reflective Robot Navigation with Language Models.assets/`，在 HTML 中引用时：
- 使用 URL 编码后的路径（空格 → `%20`）
- 示例：`src="../%E8%B5%84%E6%96%99/E2Map%20...assets/concept.png"`
- 图片需加 `border-radius`、`box-shadow` 和响应式 `max-width` 样式
- 每张图下方配 `<p style="text-align:center">` 格式的图注

### 统一主题
所有页面引用 `shared/theme.css`，使用 CSS 变量系统：
- `var(--paper)` / `var(--ink)` / `var(--accent)` 等色板变量
- `var(--font-serif)` / `var(--font-sans)` / `var(--font-mono)` 字体栈
- 课程页面需添加 `← 返回主页` 导航链接

### 添加新课程
**场景 A：为当前课程块加新课**
1. 创建 `lessons/0005-your-lesson.html`：
   - 引用 `../shared/theme.css`
   - 在 `<head>` 中添加 MathJax 脚本
   - 需要论文图片时引用 `../资料/...assets/` 目录
2. 编辑 `data/course-catalog.js`，在 `lessons` 数组中添加新条目：
   - `id`
   - `path`
   - `paper`（或理解成 collection id，例如 `e2map` / `slambook`）
   - `title` / `subtitle` / `emoji` / `duration` / `tags` / `description`
3. 若课程属于已有来源块，无需修改 `index.html`
4. 提交推送

**场景 B：添加全新的论文块或书本块**
1. 将新论文 / 新书的原始资料放入 `资料/` 目录
2. 创建对应的 `lessons/` 课程 HTML 文件
3. 编辑 `data/course-catalog.js`：
   - 在 `collections` 中新增一个对象，至少包含 `id`、`kind`、`title`、`subtitle`、`description`、`quickOpen`、`meta`
   - 在 `lessons` 中添加该来源下的课程条目，并让每一节课的 `paper` 指向新的 `collection.id`
   - 如有需要，在 `references` / `siteLinks` 中补官方链接或速查页
4. 若希望新块成为首页主线，将 `featuredCollectionId` 改成新的 `id`
5. 推送后主页会自动按来源新增一个完整分块，不需要再改首页结构

## 引用

```bibtex
@article{kim2024e2map,
  title={E2Map: Experience-and-Emotion Map for Self-Reflective Robot Navigation with Language Models},
  author={Kim, Chan and Kim, Keonwoo and Oh, Mintaek and others},
  year={2024}
}
```

## 许可

本仓库仅为教学目的创建。论文版权归原作者所有。
