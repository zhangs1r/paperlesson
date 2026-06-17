# E2Map 论文精读 · 组会报告

> 📖 **E2Map: Experience-and-Emotion Map for Self-Reflective Robot Navigation with Language Models**  
> 面向组会的论文精读教学项目

## 项目简介

本仓库包含对 E2Map 论文的**系统性精读课程**，旨在帮助移动机器人方向的研究者深入理解该论文的核心思想、技术细节和实验验证，并**准备一场完整的组会报告**。

论文的核心贡献是提出**经验-情绪地图（E2Map）**——一种将 LLM 知识与机器人真实经验整合的空间表征，受人类情绪机制启发，使机器人能在随机环境中以**单次经验驱动**的方式自主调整行为。

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

## 快速开始

用浏览器打开课程（在命令行中运行）：

```bash
# Windows
start lessons\0001-paper-overview.html

# 或直接双击 lessons 目录下的 HTML 文件
```

建议按照编号顺序学习（0001 → 0004），每课约 15-20 分钟。

## 课程内容

| 课程 | 内容 | 对应组会 PPT |
|------|------|------------|
| **第1课** 论文全景概览 | 背景、动机、贡献、相关工作对比 | PPT Part I |
| **第2课** E2Map核心技术 | 地图定义、情绪建模、更新机制 | PPT Part II |
| **第3课** 导航系统与实验 | 系统流程、三场景实验、结果分析 | PPT Part III+IV |
| **第4课** 组会报告要点 | PPT 结构、讲解词、QA准备 | PPT 全部 |

## PPT 建议结构（20-25 分钟）

1. **标题 + 大纲**（1页）
2. **背景与动机**（3页，4-5分钟）— LLM 导航现状、随机环境问题、人类情绪启发
3. **方法核心**（5页，7-8分钟）— E2Map 定义、情绪建模、事件处理、地图更新
4. **系统流程**（1页，3-4分钟）— 目标选择→规划→控制→更新
5. **实验分析**（5页，5-6分钟）— 设置、场景、结果、可视化
6. **讨论与总结**（3页，3分钟）— 贡献、局限、个人思考

具体讲解词和 QA 准备见 [第4课](lessons/0004-presentation-guide.html)。

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
