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
│   ├── 0001-paper-overview.html      # 第1课：论文全景概览
│   ├── 0002-e2map-method-core.html   # 第2课：E2Map核心技术
│   ├── 0003-navigation-experiments.html # 第3课：导航系统与实验分析
│   └── 0004-presentation-guide.html  # 第4课：组会报告组织与讲解
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
start lessons\0001-paper-overview.html   # 第1课
```

## 🏗️ 网站结构

```
├── index.html                         # 🌐 网站主页（课程导航 + 参考 + 笔记）
├── shared/
│   └── theme.css                      # 🎨 全局共享主题样式
├── data/
│   └── lessons.json                   # 📋 课程数据清单（新增课程时编辑此文件）
├── lessons/                           # 📚 精读课程
│   ├── 0001-paper-overview.html       # 第1课：论文全景概览
│   ├── 0002-e2map-method-core.html    # 第2课：E2Map核心技术
│   ├── 0003-navigation-experiments.html # 第3课：导航系统与实验
│   └── 0004-presentation-guide.html   # 第4课：组会报告要点
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

## 📝 如何添加新论文 + 新课

### 场景 A：为当前论文加新课
1. 创建 `lessons/0005-your-lesson.html`，`<head>` 中引用 `<link rel="stylesheet" href="../shared/theme.css">`
2. 编辑 `data/lessons.json`，在 `lessons` 数组中添加新条目（含 `paper: "e2map"` 字段）
3. 同时更新 `index.html` 中的 `SITE_DATA.lessons` 数组
4. 提交推送即可

### 场景 B：添加全新的论文
1. 将新论文的 MD 文件放入 `资料/` 目录
2. 在 `data/lessons.json` 和 `index.html` 的 `SITE_DATA` 中：
   - 修改 `currentPaper` 对象指向新论文
   - 在 `references` 中添加新论文原文的引用
   - 新建该论文对应的 `lessons` 条目
3. 为新课编号时建议用论文前缀，如 `e2map-0001`、`newpaper-0001`
4. 推送后主页自动更新为显示新论文

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
