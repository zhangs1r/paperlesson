# PaperLesson · 论文与教材精读课程

> 📖 **面向组会的论文精读与教材系统学习**  
> 从全景概览到组会讲解，每篇论文或每本书一套精读课程。**纯静态 HTML 网站，GitHub Pages 一键部署。**

---

## 项目简介

本仓库是一个**精读教学空间**，涵盖计算机视觉 / 移动机器人方向的论文精读与教材系统学习。所有课程以独立 HTML 页面呈现，通过数据驱动的主页按「分馆 → 来源块 → 课程页」三层结构组织，方便长期扩展。

> ⚡ **想复刻这个项目？** 本项目内置了 [`paperlesson-replicate`](skills/paperlesson-replicate/SKILL.md) AI Agent Skill，你只需告诉 agent 你的领域和风格偏好，它就能：
> 1. 自动生成完整的项目脚手架（主页、主题、数据文件）
> 2. 根据你的领域改写配套的 `/teach` 提示词
> 3. 全局注册 teach skill，后续可用 `/teach` 命令持续生成课程
> 4. 输出 GitHub Pages 部署指南
>
> 在支持 Reasonix 的编辑器中运行 `/paperlesson-replicate` 即可一键复刻。

### 当前涵盖内容

| 来源 | 类型 | 课程范围 | 状态 |
|------|------|----------|------|
| **E2Map** — Experience-and-Emotion Map | 论文精读 | 第 0001–0005 课 | ✅ 已完成 |
| **VLMaps** — Visual Language Maps | 论文精读 | 第 0006 课 | ✅ 已完成 |
| **LSeg** — Language-driven Semantic Segmentation | 论文精读 | 第 0007–0013 课 | ✅ 已完成 |
| **视觉 SLAM 十四讲** — 高翔、张涛 | 教材精读 | 第 0014–0076 课 | ✅ 已完成 |
| **DFusion-SLAM** — Dynamic Environment SLAM | 论文精读 | 第 0077–0082 课 | ✅ 已完成 |

---

## 网站结构

```
.
├── index.html                         # 🌐 网站主页（课程导航）
├── shared/
│   └── theme.css                      # 🎨 全局主题样式（学术出版风）
├── data/
│   ├── course-catalog.js              # 📋 主页数据源（groups + collections + lessons）
│   └── lessons.json                   # 📦 旧结构快照（迁移参考）
├── lessons/                           # 📚 精读课程（HTML）
│   ├── 0001-论文全景概览.html
│   ├── 0002-E2Map核心技术.html
│   ├── ...
│   ├── 0014-第一讲-前言.html
│   ├── 0077-论文全景与问题动机.html
│   └── assets/                        # 课程配套资源
│       ├── slam-course.css            # 课程页专用样式
│       ├── slam-course.js             # 课程页交互脚本
│       └── vlmaps_*.png               # 课程用图
├── reference/                         # 📖 参考资料
│   ├── glossary.html                  # 术语表
│   └── 视觉SLAM后四讲速查.html        # 速查页
├── learning-records/                  # 📝 学习笔记与记录
├── MISSION.md                         # 🎯 教学使命
├── NOTES.md                           # 📓 教学笔记与进度
├── RESOURCES.md                       # 🔗 拓展资源链接
├── skills/                            # ⚡ AI Agent Skills
│   └── paperlesson-replicate/
│       └── SKILL.md                   # 一键复刻本项目的 skill
├── 资料/                              # 原始论文 PDF/MD + 图片 assets
└── .gitignore
```

---

## 🚀 快速开始

### 在线浏览

项目已部署到 GitHub Pages：
```
https://zhangs1r.github.io/paperlesson/
```

### 本地预览

```bash
cd 项目目录
python -m http.server 8000
# 浏览器打开 http://localhost:8000
```

或直接用浏览器打开 `index.html`（注意：直接打开文件时 fetch 可能因跨域限制无法加载数据，推荐用 http.server）。

---

## 技术特色

### 学术出版风设计
- 暖米纸底色 `#F7F4EE` + 赤陶橙点缀 `#CC785C`
- CSS 变量体系（`--paper` / `--ink` / `--accent` 等）
- 衬线标题（Noto Serif SC）+ 无衬线正文（Inter）+ 等宽代码（JetBrains Mono）
- 响应式布局，适配桌面与移动端

### 数据驱动架构
- 所有课程数据集中在 `data/course-catalog.js`，主页自动渲染
- 新增课程只需修改数据文件，无需改动 `index.html`
- 三层结构：**分馆（group）→ 来源块（collection）→ 课程页（lesson）**

### LaTeX 公式渲染
- 所有课程集成 MathJax v3 CDN
- 行内公式：`\(...\)`，块级公式：`\[...\]`

### 交互式学习
- 课后练习使用 `<details>/<summary>` 折叠，点击展开答案
- 课程页底部保留「返回课程馆」和前后课导航

---

## 📝 如何添加新课程

### 场景 A：为已有来源块续课

1. 创建 `lessons/00XX-课程名.html`（序号接当前最大）
   - 引用 `../shared/theme.css` 和 `assets/slam-course.css`
   - `<head>` 中添加 MathJax 脚本
2. 编辑 `data/course-catalog.js`：
   - 在 `lessons` 数组追加新条目（字段：`id`、`path`、`paper`、`title`、`subtitle`、`emoji`、`duration`、`tags`、`description`）
   - 更新对应 collection 的 `meta` 中课程数描述
3. 推送后主页自动更新

### 场景 B：添加全新的论文/教材块

1. 将原始资料放入 `资料/` 目录
2. 创建对应的 `lessons/` 课程 HTML
3. 编辑 `data/course-catalog.js`：
   - 在 `collections` 中新增一个 collection 对象
   - 在 `lessons` 中添加新课程条目（`paper` 指向新 collection id）
   - 如需，更新 `siteLinks` / `references`
4. 若希望新块成为首页主线，修改 `featuredCollectionId`

### 使用 AI Agent 自动生成

本项目内置了 AI agent skill，可用于自动生成课程：

```bash
# 在支持 Reasonix 的编辑器中运行：
/teach "资料/论文或教材路径"
```

详细用法见 [`skills/paperlesson-replicate/SKILL.md`](skills/paperlesson-replicate/SKILL.md)。

---

## 🌐 部署到 GitHub Pages

```bash
# 1. 在 GitHub 创建新仓库（Public）

# 2. 本地推送
git init
git add .
git commit -m "🎉 init: PaperLesson 精读课程"
git branch -M main
git remote add origin https://github.com/你的用户名/你的仓库名.git
git push -u origin main

# 3. 开启 GitHub Pages
# GitHub 仓库 → Settings → Pages → Branch: main, / (root) → Save
# 等待 1-2 分钟后访问：
# https://你的用户名.github.io/仓库名/
```

---

## 开发规范

| 规范 | 要求 |
|------|------|
| 编码 | UTF-8，无 BOM |
| 样式 | 全部通过 `shared/theme.css`，不使用内联样式 |
| 颜色 | 使用 CSS 变量（`var(--ink)`、`var(--accent)` 等），不硬编码 |
| 公式 | MathJax v3，行内 `\(\)`，块级 `\[\]` |
| 图片 | URL 编码路径，加圆角阴影和居中图注 |
| 练习 | `<details>/<summary>` 折叠，默认收起 |
| 导航 | 每页底部「返回课程馆」+ 前后课链接 |

---

## 引用

```bibtex
@article{kim2024e2map,
  title={E2Map: Experience-and-Emotion Map for Self-Reflective Robot Navigation with Language Models},
  author={Kim, Chan and Kim, Keonwoo and Oh, Mintaek and others},
  year={2024}
}
```

---

*PaperLesson · 以教学驱动深度学习*
