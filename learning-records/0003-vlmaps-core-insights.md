# 0003: VLMaps 完整精读 — Visual Language Maps for Robot Navigation

## 日期

2025 年

## 状态

已完成精读

## 背景

作为 E2Map 的建图基础[9]，VLMaps (ICRA 2023) 是理解 E2Map 工作流的前提。已完成第 6 课完整精读。

## 核心要点

### 论文定位

- **标题**：Visual Language Maps for Robot Navigation
- **作者**：Huang, Mees, Zeng, Burgard (Freiburg / Google Research)
- **发表**：ICRA 2023
- **项目**：https://vlmaps.github.io

### 核心思想

VLMaps = **LSeg 视觉-语言特征** + **3D 重建** → 语言可索引的空间地图

### 关键贡献

1. **开放词汇地标索引**：通过 LSeg 特征与 CLIP 文本空间的余弦相似度，可查询任意物体的位置，无需预定义类别
2. **空间目标导航**：能理解"在沙发和电视之间"、"椅子北方 3 米处"等空间关系指令（基线方法完全做不到）
3. **LLM 代码生成导航**：采用 Socratic 融合，LLM 写 Python 代码调用 17 个导航原语
4. **多形态障碍地图**：同一张 VLMaps 可为不同形态的机器人（地面/空中）生成不同的障碍地图

### 建图 Pipeline

RGB-D 视频 → LSeg 稠密特征提取 → 3D 反投影 + 位姿对齐 → 俯视投影 + 特征平均 → VLMaps (2D 栅格 × d 维特征)

### 导航 Pipeline

自然语言指令 → LLM 生成 Python 代码 → 执行代码（查询 VLMaps 获取物体位置 + 调用导航原语）→ D*/A* 路径规划 → 运动执行

### 实验结果

- **多目标导航**：VLMaps 93% vs CoW 63% vs LM-Nav 70%
- **空间目标导航**：VLMaps 80-100%，基线 0-20%（LM-Nav 完全失败）
- **消融实验**：LSeg > CLIP（稠密特征 vs 全局特征），Codex > GPT-3（代码模型更优）

### 与 E2Map 的关键区别

| 维度 | VLMaps | E2Map |
|------|--------|-------|
| 建图 | 静态（建好后不变） | 动态更新（事件触发） |
| 特征来源 | 预训练 VLM (LSeg) | VLMaps + 自身经验（LLM 评估） |
| 适配环境 | 静态环境 | 动态/随机环境 |
| 学习能力 | ❌ 无 | ✅ 自反思学习 |

### 关键洞察

- VLMaps 成功了，因为它把"建图"和"语言理解"合二为一——而不是像之前的方法那样分别处理
- LSeg 的稠密特征（每像素）是实现精确空间定位的关键；CLIP 的全局特征（整图）远远不够
- VLMaps 的三大局限（重建噪声、物体歧义、动态场景）恰好是 E2Map 改进的起点
- E2Map 继承了 VLMaps 的建图方式，但用"情绪场"赋予了机器人记忆和学习能力

## 后续方向

- 可以在 E2Map 汇报中先讲 VLMaps（5-10 分钟），作为背景铺垫
- 关注 VLMaps 代码仓库的具体实现（特征融合、俯视投影的计算细节）
- 如果时间允许，可以在真实场景中试用 VLMaps 建图流程

## 参考

- 第 6 课：`lessons/0006-VLMaps精读.html`
- 术语表：`reference/glossary.html`（含 VLMaps 相关术语）
- 项目主页：https://vlmaps.github.io
