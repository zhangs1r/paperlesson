# 教学笔记

## 学习者偏好

- 移动机器人方向，对定位、规划、控制有基础了解
- 需要完整全流程的组会报告
- 需要在当前会话中一次性完成学习
- 使用中文教学
- GitHub 仓库: https://github.com/zhangs1r/paperlesson.git

## 教学策略

- 每一课程聚焦一个核心概念
- 课程包含直接引用的论文原句 + 中文解释
- 课程附带图片，帮助理解（使用论文中的assets）
- 每课末尾含复习问题
- 可以打开 HTML 浏览器查阅

## 学习进度

- 已完成旧 E2Map / VLMaps 系列（第 1-6 课，已存档）
- 已完成 LSeg 论文精读（第 7-13 课，全新系列）：
  - 第 7 课：论文全景与核心动机（Abstract + Introduction）
  - 第 8 课：相关工作（Related Work）
  - 第 9 课：方法——文本与图像编码器
  - 第 10 课：方法——空间正则化与训练
  - 第 11 课：实验设置与结果分析
  - 第 12 课：消融研究与定性分析
  - 第 13 课：总结与展望
- 已切换至《视觉 SLAM 十四讲》系列（第 14 课起）：
  - 第 14 课：前言（本课）
- 已完成第 6 讲（非线性优化）系列（第 39-45 课）：
  - 第 39 课：状态估计与最小二乘引出
  - 第 40 课：高斯-牛顿法
  - 第 41 课：列文伯格-马夸尔特法
  - 第 42 课：Ceres 实践曲线拟合
  - 第 43 课：图优化理论入门
  - 第 44 课：g2o 实践曲线拟合
  - 第 45 课：章节总结与习题

## LSeg 教学要点备忘

- 论文简称 LSeg (Language-driven Semantic Segmentation)
- 核心创新点：用文本嵌入替代固定分类头
- 关键概念：词-像素相关张量、标签等变性、BottleneckBlock
- 重要结果：FSS-1000 上零样本超越 1-shot 方法是最大亮点
- 失败模式：标签集中无真实类别时的"最接近"问题

## 用户记录的技巧

- **`<details>/<summary>` 折叠面板**：用于"展开查看答案"的课后练习题。HTML 原生标签，无需 JS。示例：`<details><summary>查看答案</summary><p>答案内容</p></details>`

## 视觉 SLAM 十四讲教学要点

- 第 1 讲（前言）已使用 MinerU 将 399 页 PDF 转为 Markdown + 670 张图片
- 后续课程素材均来自转换后的 markdown 文件
- OCR 错误示例：书中原句"那就让我们一起开始这段旅程吧"被识别为"如何佳用大书"
- 公式渲染使用 KaTeX (CDN)，代码块使用 JetBrains Mono

## 已完成课程

### 第九讲 · 实践章：搭建 VO 前端（共 3 课）
- **0060** — VO 框架与五大数据结构（Camera/Frame/MapPoint/Map/Config）
- **0061** — 两两帧 VO 实现与 PnP 优化（0.2→0.3 版递进）
- **0062** — 局部地图改进与章节总结（0.4 版 + 知识图谱 + 全部习题）

### 第十讲 · 后端 1（共 3 课）
- **0063** — 状态估计的贝叶斯框架与卡尔曼滤波器（KF + EKF）
- **0064** — BA 求解与稀疏性边缘化（H 矩阵稀疏结构 + Schur 消元 + Huber 核）
- **0065** — g2o 与 Ceres 实践 BA + 章节总结习题（自定义 Vertex/Edge + AutoDiff + ParameterBlockOrdering）

### OCR 纠正记录
- 第九讲公式 $\mathbf{T}_{cr}$ 被误识别为 $\mathbf { \delta } _ { \mathbf { \mathcal { T } } \nu _ { w } }$，已在 0061 中纠正
- 代码中 Camera 类内参变量名被 OCR 识别为带奇怪下标的格式，已恢复为标准 fx_/fy_/cx_/cy_
- 第十讲公式(10.1)中 $\boldsymbol{x}_k = f(\boldsymbol{x}_{k-1}, \boldsymbol{u}_k) + \boldsymbol{w}_k$ 被 OCR 识别为带多余空格的乱码，已在 0063 中恢复标准 LaTeX
