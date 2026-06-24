# 资源列表

## 📌 当前精读论文

| 资源 | 链接 | 用途 |
|------|------|------|
| LSeg 论文 (ICLR 2022) | arXiv: https://arxiv.org/abs/2201.03546 | 精读材料 |
| LSeg 代码仓库 | https://github.com/isl-org/lang-seg | 阅读代码实现 |
| CLIP 论文 (ICML 2021) | https://arxiv.org/abs/2103.00020 | LSeg 的文本编码器基础 |
| DPT (Dense Prediction Transformer) | https://arxiv.org/abs/2103.13413 | LSeg 的图像编码器基础 |

## 核心参考文献 (LSeg)

| 文献 | 简介 | 为什么重要 |
|------|------|-----------|
| CLIP, Radford et al., ICML 2021 | 对比学习图文匹配，零样本分类 | LSeg 文本编码器来源 |
| DPT, Ranftl et al., 2021 | Vision Transformer 密集预测 | LSeg 图像编码器架构 |
| ViLD, Gu et al., 2021 | 零样本目标检测，使用 CLIP | 语言驱动检测的先导工作 |
| MDETR, Kamath et al., 2021 | 端到端文本调制目标检测 | 语言驱动检测的代表工作 |
| ZS3Net, Bucher et al., 2019 | 零样本语义分割，Word2Vec嵌入 | LSeg 对比的零样本基线 |
| HSNet, Min et al., 2021 | 超相关网络，小样本分割 | LSeg 对比的少样本基线 |

## 后续发展 (受 LSeg 影响)

| 文献 | 简介 | 与 LSeg 的关系 |
|------|------|-----------|
| OVSeg, 2023 | 开放词汇语义分割 | 扩展 LSeg 的零样本能力 |
| ODISE, 2023 | 扩散模型驱动的开放词汇分割 | 用扩散模型替代传统分割架构 |
| Grounded-SAM, 2023 | Grounding DINO + SAM | 分割基础模型 + 开放词汇 |

## 论文与代码 (已有)

| 资源 | 链接 | 用途 |
|------|------|------|
| E2Map 项目主页 | https://e2map.github.io/ | 论文、视频、代码 |
| E2Map 代码仓库 | https://github.com/ChanKim0610/e2map | 阅读代码实现 |
| 论文原文 (arXiv) | 见项目主页 | 精读材料 |

## 核心参考文献

| 文献 | 简介 | 为什么重要 |
|------|------|-----------|
| [9] VLMaps (ICRA 2023) | Visual Language Maps for Robot Navigation | E2Map 的视觉语言建图基础 |
| [8] Open-vocabulary Queryable Scene | 开放词汇场景表征 | 空间锚定的相关工作 |
| [23] LM-Nav (CoRL 2023) | Robotic Navigation with Large Pre-trained Models | 基线方法之一 |
| [7] VoxPoser (CoRL 2023) | Composable 3D Value Maps | LLM 空间规划的早期工作 |
| [10] Damasio, Feeling & Knowing | 情绪与稳态的神经科学著作 | 本文情绪理论的思想来源 |
| [29] GPT-4o System Card | GPT-4o 技术报告 | 事件描述器使用的模型 |
| [30] Llama 3 Herd of Models | Llama3 模型 | 情绪评估器使用的模型 |

## 背景知识资源

| 资源 | 链接 | 用途 |
|------|------|------|
| ROS Gazebo 教程 | http://gazebosim.org/tutorials | 理解仿真实验环境 |
| D* 算法 | Stentz, 1994 | 路径规划算法（E2Map 所用） |
| MPPI 控制 | Williams et al., 2015 | 模型预测路径积分控制 |
| LSeg | Li et al., ICLR 2022 | 语言驱动的语义分割模型 |
| CLIP | Radford et al., ICML 2021 | 视觉-语言对比学习模型 |
| Weber-Fechner 定律 | Dehaene, 2003 | E2Map 更新规则的理论依据 |

## 社区

- **Reddit**: r/robotics, r/MachineLearning
- **GitHub Discussions**: E2Map 仓库的 Issues/Discussions
- **学术会议**: ICRA, IROS, CoRL 的论文集
