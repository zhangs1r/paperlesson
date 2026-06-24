# 学习记录 0007：LSeg 论文精读

## 日期
2026-06-19

## 学习内容
完整精读了 "Language-driven Semantic Segmentation" (ICLR 2022) 论文，共 7 课：

1. **论文全景与核心动机** — 固定标签集问题、LSeg 方案概览
2. **相关工作** — 广义分割脉络、CLIP/ViLD/MDETR 关系
3. **方法：文本与图像编码器** — CLIP 文本编码器、DPT 图像编码器、词-像素内积、对比损失
4. **方法：空间正则化与训练** — 标签等变性、BottleneckBlock/DepthwiseBlock、训练细节
5. **实验设置与结果分析** — PASCAL-5ⁱ、COCO-20ⁱ、FSS-1000 三个基准
6. **消融研究与定性分析** — 消融实验、同义/层级泛化、失败案例
7. **总结与展望** — 全文回顾、贡献与局限、后续影响

## 核心要点

- **核心公式**：$f_{ijk} = I_{ij} \cdot T_k$，用内积替代固定分类头
- **关键约束**：标签等变性（label equivariance）——所有空间操作不能依赖标签输入顺序
- **最大突破**：零样本方法在 FSS-1000 上超越 1-shot 方法（87.8 vs 86.5 mIoU）
- **宝贵代价**：灵活性只付出了 0.38 mIoU（vs DPT）的微小代价

## 技术栈
- CLIP 文本编码器（冻结）
- DPT 密集预测 Transformer（ViT-L/16 或 ResNet101 骨干）
- Depthwise 卷积 + BottleneckBlock 空间正则化

## 后续关注
- OVSeg (2023) — 开放词汇分割扩展
- ODISE / Grounded-SAM — 结合扩散模型/基础模型的开放词汇分割
- 机器人导航中的场景理解应用（见 RESOURCES.md）
