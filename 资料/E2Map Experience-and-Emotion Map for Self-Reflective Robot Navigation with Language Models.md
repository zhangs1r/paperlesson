# E2Map: Experience-and-Emotion Map for Self-Reflective Robot Navigation with Language Models

- Source LaTeX: D:\desktop\学习\obsidian\Note\notebook\论文\latex\E2Map Experience-and-Emotion Map for Self-Reflective Robot Navigation with Language Models\root.tex
- Image assets: ./E2Map Experience-and-Emotion Map for Self-Reflective Robot Navigation with Language Models.assets/
- Format: bilingual paragraph-by-paragraph translation. Each original paragraph is followed by the corresponding Chinese translation.

## 术语约定

| English term | 中文译法 |
|---|---|
| Experience-and-Emotion Map / E2Map | 经验-情绪地图 / E2Map |
| embodied agent | 具身智能体 |
| stochastic environment | 随机环境 |
| one-shot behavior adjustment | 单次经验驱动的行为调整 |
| grounding / spatial grounding | 落地 / 空间锚定 |
| visual-language feature | 视觉-语言特征 |
| large language model (LLM) | 大语言模型（LLM） |
| large multi-modal model (LMM) | 大型多模态模型（LMM） |
| vision-language model (VLM) | 视觉-语言模型（VLM） |
| Visual Language Map (VLMap) | 视觉语言地图（VLMap） |
| goal selector | 目标选择器 |
| event descriptor | 事件描述器 |
| emotion evaluator | 情绪评估器 |
| upsetness | 受挫程度 |
| guiltiness | 内疚程度 |
| affordance | 可供性 |
| homeostasis | 稳态 |

## Title / 标题

**Original**

E2Map: Experience-and-Emotion Map for Self-Reflective Robot Navigation with Language Models

**中文译文**

E2Map：面向基于语言模型的自反思机器人导航的经验-情绪地图

**Original**

Chan Kim, Keonwoo Kim, Mintaek Oh, Hanbi Baek, Jiyang Lee, Donghwi Jung, Soojin Woo, Younkyung Woo, John Tucker, Roya Firoozi, Seung-Woo Seo, Mac Schwager, and Seong-Woo Kim. * indicates equal contribution. Seoul National University; Work done while visiting the Autonomous Robot Intelligence Lab, SNU; Carnegie Mellon University; Stanford University; University of Waterloo. Correspondence to: Seong-Woo Kim, snwoo@snu.ac.kr.

**中文译文**

Chan Kim、Keonwoo Kim、Mintaek Oh、Hanbi Baek、Jiyang Lee、Donghwi Jung、Soojin Woo、Younkyung Woo、John Tucker、Roya Firoozi、Seung-Woo Seo、Mac Schwager 与 Seong-Woo Kim。* 表示共同一作。作者单位包括首尔国立大学、首尔国立大学自主机器人智能实验室访问期间完成的工作、卡内基梅隆大学、斯坦福大学和滑铁卢大学。通讯作者：Seong-Woo Kim，snwoo@snu.ac.kr。

## Abstract / 摘要

**Original**

Large language models (LLMs) have shown significant potential in guiding embodied agents to execute language instructions across a range of tasks, including robotic manipulation and navigation. However, existing methods are primarily designed for static environments and do not leverage the agent's own experiences to refine its initial plans. Given that real-world environments are inherently stochastic, initial plans based solely on LLMs' general knowledge may fail to achieve their objectives, unlike in static scenarios. To address this limitation, this study introduces the Experience-and-Emotion Map (E2Map), which integrates not only LLM knowledge but also the agent's real-world experiences, drawing inspiration from human emotional responses. The proposed methodology enables one-shot behavior adjustments by updating the E2Map based on the agent's experiences. Our evaluation in stochastic navigation environments, including both simulations and real-world scenarios, demonstrates that the proposed method significantly enhances performance in stochastic environments compared to existing LLM-based approaches. Code and supplementary materials are available at https://e2map.github.io/.

**中文译文**

大语言模型（LLMs）在引导具身智能体执行语言指令方面展现出显著潜力，覆盖机器人操作、机器人导航等多类任务。然而，现有方法主要面向静态环境设计，并没有利用智能体自身的经验来修正其初始计划。现实世界环境本质上具有随机性，因此不同于静态场景，仅依赖 LLM 通用知识生成的初始计划可能无法达成目标。为解决这一局限，本文提出经验-情绪地图（Experience-and-Emotion Map，E2Map），它受到人类情绪反应机制启发，不仅整合 LLM 的知识，也整合智能体在真实世界中的经验。该方法根据智能体经验更新 E2Map，从而实现单次经验驱动的行为调整。我们在包含仿真和真实场景的随机导航环境中进行评估，结果表明，与现有基于 LLM 的方法相比，本文方法显著提升了随机环境中的导航性能。代码与补充材料可在 https://e2map.github.io/ 获取。

## 1. Introduction / 引言

**Original**

Large language models (LLMs), pre-trained on Internet-scale data, have emerged as a promising method to encapsulate the world's knowledge distilled in language. These LLMs have demonstrated a variety of capabilities, including interpreting and responding to natural language instructions, performing logical reasoning, and generating code. Leveraging these capabilities, many studies have explored applying the generalizable knowledge of LLMs to embodied agents, enabling them to interact physically in the real world.

**中文译文**

大语言模型（LLMs）在互联网规模数据上预训练，被视为一种很有前景的方式，用语言形式封装和提炼世界知识。这些 LLM 已经展现出多种能力，包括理解并响应自然语言指令、进行逻辑推理以及生成代码。借助这些能力，许多研究开始探索如何将 LLM 的可泛化知识应用到具身智能体上，使其能够在真实世界中进行物理交互。

**Original**

To effectively utilize LLMs' knowledge in enabling embodied agents, it is crucial to ground this knowledge in the real-world environments where the agents operate. Previous studies have proposed methods to decompose language instructions into sequential subtasks, which are then executed using predefined motion primitives [1, 2, 3]. Other research has explored the use of LLMs' code generation capabilities to translate language instructions into executable code for robots, which is then used in conjunction with various APIs [4, 5, 6]. Additionally, some studies have focused on grounding information from LLMs and vision-language models (VLMs) in the spatial contexts where robots operate [7, 8, 9]. For instance, [7] proposed a method for planning by representing language instructions as spatial costs and affordances using LLMs' code-writing capabilities. Furthermore, [8] and [9] introduced methodologies for robot navigation that use maps that allow spatial information queries by language.

**中文译文**

为了让具身智能体有效利用 LLM 的知识，关键在于将这些知识落地到智能体实际运行的真实世界环境中。已有研究提出了将语言指令分解为一系列顺序子任务的方法，并用预定义的运动基元执行这些子任务 [1, 2, 3]。另一些研究探索了利用 LLM 的代码生成能力，将语言指令转换为机器人可执行代码，并结合多种 API 完成任务 [4, 5, 6]。此外，还有研究关注如何把来自 LLM 和视觉-语言模型（VLMs）的信息锚定到机器人运行的空间语境中 [7, 8, 9]。例如，[7] 利用 LLM 的代码编写能力，将语言指令表示为空间代价和可供性，从而进行规划。进一步地，[8] 和 [9] 提出了用于机器人导航的方法，这些方法使用能够通过语言查询空间信息的地图。

![Fig. 1 Concept of E2Map](<E2Map Experience-and-Emotion Map for Self-Reflective Robot Navigation with Language Models.assets/concept.png>)

**Original Caption**

Figure 1. E2Map is a spatial map that captures the agent's emotional responses to its experiences. Our method enables one-shot behavior adjustments in stochastic environments by updating the E2Map through the diverse capabilities of LLMs and LMMs. Since VLM can refer to both the Vision-Language Model and Visual Language Map, we will preferably use LMM for the former and VLMap for the latter.

**中文图注**

图 1. E2Map 是一种空间地图，用于捕获智能体对其经验产生的情绪反应。本文方法借助 LLM 与 LMM 的多样能力更新 E2Map，从而在随机环境中实现单次经验驱动的行为调整。由于 VLM 既可能指视觉-语言模型（Vision-Language Model），也可能指视觉语言地图（Visual Language Map），本文优先用 LMM 表示前者，用 VLMap 表示后者。

**Original**

While these methodologies have successfully demonstrated the use of LLMs with embodied agents, they primarily address static environments and fail to incorporate the agent's own experiences. Given that the real world is inherently stochastic and subject to various uncertainties, initial plans based solely on the general knowledge of LLMs may fall short of achieving their objectives. For example, a robot navigating indoors might unexpectedly collide with a person stepping out from a suddenly opened door, potentially causing it to fall. In such cases, the robot may fail to complete its mission using its initial plan. To increase the success rate in similar future scenarios, it is essential to incorporate these experiences and adjust the robot’s behavior to maintain a safe distance when encountering doors. In summary, to achieve objectives in stochastic environments, the robot must refine its plan based on experience.

**中文译文**

尽管这些方法已经成功展示了 LLM 与具身智能体结合的可行性，但它们主要面向静态环境，并未纳入智能体自身的经验。现实世界本质上具有随机性，并受到各种不确定因素影响，因此仅基于 LLM 通用知识制定的初始计划可能无法完成目标。例如，一个在室内导航的机器人，可能会意外撞上从突然打开的门后走出来的人，甚至因此摔倒。在这种情况下，机器人可能无法依靠初始计划完成任务。为了在未来类似场景中提高成功率，必须将这些经验纳入系统，并调整机器人的行为，使其在遇到门时保持安全距离。总之，要在随机环境中达成目标，机器人必须基于经验修正自身计划。

**Original**

Humans experience emotions in response to stimuli, which influence specific behaviors toward certain objects or situations. According to [10] and [11], emotions play a crucial role in maintaining homeostasis by guiding humans to avoid previously encountered dangers, thus supporting survival. Furthermore, recent research [12] demonstrates that humans integrate emotional experiences into spatial representations for navigation. By using emotions as spatial boundaries to maintain homeostasis, humans can prefer or avoid specific locations based on their experiences during navigation.

**中文译文**

人类会对刺激产生情绪，而情绪会影响其对特定对象或情境的具体行为。根据 [10] 和 [11]，情绪通过引导人类避开曾经遭遇过的危险，在维持稳态方面发挥关键作用，从而支持生存。此外，近期研究 [12] 表明，人类会将情绪经验整合到用于导航的空间表征中。通过将情绪作为维持稳态的空间边界，人类能够基于导航过程中的经验偏好或避开某些特定位置。

**Original**

Inspired by human emotional mechanisms, this study proposes a language-based robot system that utilizes the capabilities of LLMs and large multi-modal models (LMMs) to enable an embodied agent to autonomously adjust its behavior in a one-shot manner. The core component is the Experience-and-Emotion Map (E2Map), which serves as a spatial map that grounds both the general knowledge of LLMs and the agent's emotional responses to experiences. When the agent interacts with a particular object or space, it quantifies its emotional response and integrates this information into the E2Map as shown in Fig. 1. The agent's planning and control module then uses the E2Map as a cost function to guide its actions, allowing for behavior refinement through E2Map updates. The contributions are summarized as follows:

**中文译文**

受人类情绪机制启发，本文提出一种基于语言的机器人系统。该系统利用 LLM 和大型多模态模型（LMMs）的能力，使具身智能体能够以单次经验驱动的方式自主调整自身行为。其核心组件是经验-情绪地图（E2Map）：这是一种空间地图，用于同时锚定 LLM 的通用知识以及智能体对自身经验的情绪反应。当智能体与某一特定物体或空间发生交互时，它会量化自身的情绪反应，并如图 1 所示将该信息整合进 E2Map。随后，智能体的规划与控制模块将 E2Map 作为代价函数来引导行动，使系统能够通过更新 E2Map 来细化行为。本文贡献总结如下：

**Original**

- Inspired by human emotional mechanisms, we propose E2Map, a spatial representation that integrates both the general knowledge of LLMs and the agent's emotional responses to its experiences to facilitate planning.
- We propose a robot system that leverages the E2Map and various LLM capabilities—including code generation, event description, and emotion evaluation—to enable the agent to autonomously adjust its behavior in a one-shot manner based on its experiences.
- We verified that the proposed methodology can autonomously adjust behavior by incorporating its experiences in navigation environments with changing conditions and dynamic objects, demonstrating superior performance over existing LLM-based approaches.

**中文译文**

- 受人类情绪机制启发，我们提出 E2Map：一种空间表征，它同时整合 LLM 的通用知识和智能体对自身经验的情绪反应，以辅助规划。
- 我们提出一种机器人系统，该系统利用 E2Map 以及 LLM 的多种能力，包括代码生成、事件描述和情绪评估，使智能体能够基于自身经验以单次经验驱动的方式自主调整行为。
- 我们验证了所提方法能够在包含条件变化和动态物体的导航环境中纳入经验并自主调整行为，相较于现有基于 LLM 的方法表现出更优性能。

## 2. Related Works / 相关工作

### 2.1 LLM-based Robotics / 基于 LLM 的机器人学

**Original**

Research on using language instructions to control robots has advanced significantly with the development of LLMs. Numerous studies [1, 2, 3, 13, 14, 15, 16, 4, 5, 6, 7, 17] have aimed to leverage the general knowledge embedded in LLMs and the benefits of few-shot prompting, which eliminates the need for additional training. [1, 2, 3] proposed a method that uses LLMs to decompose a given language instruction into a sequence of subtasks and employs predefined motion primitives to execute each subtask. [4, 5, 6] utilized LLMs' capability of code generation to transform language instructions into executable code for robots, using various APIs to carry out tasks. [7] proposed utilizing LLMs to construct affordances and constraints within a 3D voxel map and employing model predictive control (MPC) to compute actions, eliminating the need for predefined motion primitives.

**中文译文**

随着 LLM 的发展，利用语言指令控制机器人的研究取得了显著进展。大量研究 [1, 2, 3, 13, 14, 15, 16, 4, 5, 6, 7, 17] 旨在利用 LLM 内嵌的通用知识，以及少样本提示无需额外训练的优势。[1, 2, 3] 提出使用 LLM 将给定语言指令分解为一系列子任务，并采用预定义运动基元执行各个子任务。[4, 5, 6] 利用 LLM 的代码生成能力，将语言指令转换为机器人可执行代码，并通过各种 API 执行任务。[7] 提出利用 LLM 在三维体素地图中构建可供性与约束，并采用模型预测控制（MPC）计算动作，从而不再依赖预定义运动基元。

**Original**

While these approaches have shown notable success in language-based robotics, they primarily focus on static environments and overlook the integration of the robot's experiences. [17] demonstrated that it is possible to refine a robot's behavior through additional human language instructions, but this refinement does not stem from the robot's own experiences. In contrast, the proposed methodology addresses behavior refinement in stochastic environments by grounding the robot's emotional responses to its own experiences.

**中文译文**

尽管这些方法在基于语言的机器人学中取得了显著成功，但它们主要关注静态环境，并忽视了机器人自身经验的整合。[17] 表明，可以通过额外的人类语言指令来细化机器人行为，但这种细化并非来自机器人自身经验。与之不同，本文方法通过将机器人对自身经验的情绪反应进行空间锚定，来解决随机环境中的行为细化问题。

**Original Caption**

Table 1. Comparison of Existing and Proposed Methods.

**中文表题**

表 1. 现有方法与本文方法的比较。

| Methods | LLM-Based | Spatial Grounding | Behavior Adjustment | Self-Reflection |
|---|---:|---:|---:|---:|
| [1, 2, 3, 4, 5, 6, 18] | ✓ |  |  |  |
| [7, 8, 9] | ✓ | ✓ |  |  |
| [17] | ✓ |  | ✓ |  |
| **Ours** | ✓ | ✓ | ✓ | ✓ |

**中文译表**

| 方法 | 基于 LLM | 空间锚定 | 行为调整 | 自反思 |
|---|---:|---:|---:|---:|
| [1, 2, 3, 4, 5, 6, 18] | ✓ |  |  |  |
| [7, 8, 9] | ✓ | ✓ |  |  |
| [17] | ✓ |  | ✓ |  |
| **本文方法** | ✓ | ✓ | ✓ | ✓ |

### 2.2 Visual-Language Navigation / 视觉-语言导航

**Original**

To demonstrate the ability to achieve one-shot behavior adjustment in stochastic environments, we evaluated the proposed methodology in a mobile robot indoor navigation scenario. Navigation environments involve dynamic objects such as people, which can cause unexpected events, e.g., a person suddenly stepping out of the door.

**中文译文**

为了展示本文方法在随机环境中实现单次经验驱动行为调整的能力，我们在移动机器人室内导航场景中对其进行了评估。导航环境中包含人等动态对象，它们可能引发意外事件，例如有人突然从门后走出。

**Original**

Visual-language navigation (VLN), which uses a robot's visual input to execute given language instructions, has been extensively researched to date. Early research used methods to map language instructions and visual input to discrete [19, 20], or continuous actions [21, 22]. However, these methods are data-intensive, which raises concerns about the cost of data collection. To address these problems, research has emerged that uses foundation models [18, 23, 8, 9]. [23] proposed a topological graph-based navigation approach using three different foundation models. [18] demonstrated object navigation using open-vocabulary object detector based on CLIP [24] and exploration techniques. [8] proposed creating a prebuilt spatial map that stores visual-language features of objects, while [9] suggested generating maps by storing pixel-level visual-language features of spaces. By grounding language instructions into these maps, both approaches demonstrated their effectiveness in enabling spatial open-vocabulary navigation tasks. However, these approaches are limited to static environments and do not account for the refinement of navigation plans based on the agent's real-time experiences. Table 1 presents a comparison between the proposed method and existing methods.

**中文译文**

视觉-语言导航（VLN）使用机器人的视觉输入来执行给定语言指令，至今已得到广泛研究。早期研究采用方法将语言指令和视觉输入映射到离散动作 [19, 20] 或连续动作 [21, 22]。然而，这些方法高度依赖数据，引发了数据采集成本方面的担忧。为解决这些问题，使用基础模型的研究逐渐出现 [18, 23, 8, 9]。[23] 提出了一种基于拓扑图的导航方法，使用三种不同的基础模型。[18] 使用基于 CLIP [24] 的开放词汇目标检测器和探索技术展示了目标导航。[8] 提出创建一种预构建空间地图，用于存储物体的视觉-语言特征；而 [9] 则建议通过存储空间中的像素级视觉-语言特征来生成地图。通过将语言指令落地到这些地图中，两种方法都证明了其在空间开放词汇导航任务中的有效性。然而，这些方法局限于静态环境，并未考虑根据智能体实时经验来细化导航计划。表 1 给出了本文方法与现有方法的比较。

![Fig. 2 System overview](<E2Map Experience-and-Emotion Map for Self-Reflective Robot Navigation with Language Models.assets/e2map_arch.png>)

**Original Caption**

Figure 2. System Overview: (a) E2Map is created by embedding visual-language features and emotion parameters into corresponding grid cells. (b) When a user provides a language instruction, the goal selector generates code through goal selection APIs to decide goals to reach. (c) The planning algorithm then uses emotion as a cost to generate the optimal path to the goal. (d) If the agent encounters unexpected events during navigation, the E2Map is updated through the sequential operation of the event descriptor and emotion evaluator. Following the update, the planning algorithm replans the path to adjust the agent’s behavior in a one-shot manner.

**中文图注**

图 2. 系统概览：（a）E2Map 通过将视觉-语言特征和情绪参数嵌入对应网格单元来构建。（b）当用户给出语言指令时，目标选择器通过目标选择 API 生成代码，以决定需要到达的目标。（c）随后，规划算法将情绪作为代价，生成通往目标的最优路径。（d）如果智能体在导航过程中遇到意外事件，E2Map 会通过事件描述器和情绪评估器的顺序操作进行更新。更新后，规划算法重新规划路径，以单次经验驱动的方式调整智能体行为。

### 2.3 Learning from Experience / 从经验中学习

**Original**

Methods for optimizing robot behavior based on past experiences have been widely explored in reinforcement learning [25]. Reinforcement learning quantifies rewards from experiences and trains models to maximize these rewards. Similarly, in imitation learning, several studies have proposed acquiring additional expert data when the agent experiences a situation it cannot solve on its own during operation [26, 27]. However, these approaches require extensive interactions with the environment or additional data acquisition for learning, making immediate behavior corrections impractical. In contrast, the proposed method leverages LLM prompting, avoiding parameter updates, and grounds the agent's experiences in E2Map for immediate behavior corrections in a one-shot manner.

**中文译文**

基于过往经验优化机器人行为的方法已在强化学习中得到广泛探索 [25]。强化学习会从经验中量化奖励，并训练模型最大化这些奖励。类似地，在模仿学习中，一些研究提出，当智能体在运行过程中遇到无法独立解决的情境时，额外采集专家数据 [26, 27]。然而，这些方法需要大量环境交互或额外数据采集才能学习，因此难以实现即时行为修正。与之不同，本文方法利用 LLM 提示，不需要参数更新，并将智能体经验锚定到 E2Map 中，从而以单次经验驱动的方式实现即时行为修正。

## 3. Method / 方法

### 3.1 Building and Initializing E2Map / 构建并初始化 E2Map

**Original**

E2Map is a spatial grid map that captures both the visual-language features of the environment and the agent's emotional responses to its experiences. In this paper, we define emotion as the spatial extent reflecting how the agent perceives the space to maintain homeostasis, inspired by [10]. We ground emotion within the spatial map by modeling it as a weighted summation of Gaussian distribution.

**中文译文**

E2Map 是一种空间网格地图，既捕获环境的视觉-语言特征，也捕获智能体对自身经验产生的情绪反应。受 [10] 启发，本文将情绪定义为一种空间范围，它反映智能体为了维持稳态而如何感知空间。我们将情绪建模为高斯分布的加权求和，并据此把情绪锚定到空间地图中。

**Original**

E2Map is mathematically defined as $\mathcal{M} \in \mathcal{R}^{\bar{H} \times \bar{W} \times (C_{lang} + C_{emo})}$, where $\bar{H}$ and $\bar{W}$ represent the size of the top-down grid map, $C_{lang}$ denotes the dimension of the visual-language features for each grid cell, and $C_{emo}$ indicates the number of parameters for emotion. Each grid cell represents $s$ meters of actual space, so the size of the space represented by E2Map is $s\bar{H} \times s\bar{W}$ meters. The proposed methodology first builds $\mathcal{M}_{lang} \in \mathcal{R}^{\bar{H} \times \bar{W} \times C_{lang}}$ by embedding visual-language features of RGB images of the environment into a corresponding grid cell. Similar to [9], we used LSeg [28] as the pre-trained VLM to encode RGB images and determine the position of each pixel in the grid map using depth images and camera poses.

**中文译文**

在数学上，E2Map 定义为 $\mathcal{M} \in \mathcal{R}^{\bar{H} \times \bar{W} \times (C_{lang} + C_{emo})}$，其中 $\bar{H}$ 和 $\bar{W}$ 表示俯视网格地图的尺寸，$C_{lang}$ 表示每个网格单元中视觉-语言特征的维度，$C_{emo}$ 表示情绪参数的数量。每个网格单元代表真实空间中的 $s$ 米，因此 E2Map 所表示空间的大小为 $s\bar{H} \times s\bar{W}$ 米。本文方法首先构建 $\mathcal{M}_{lang} \in \mathcal{R}^{\bar{H} \times \bar{W} \times C_{lang}}$，方法是将环境 RGB 图像的视觉-语言特征嵌入到对应网格单元中。与 [9] 类似，我们使用 LSeg [28] 作为预训练 VLM 来编码 RGB 图像，并利用深度图像和相机位姿确定每个像素在网格地图中的位置。

**Original**

To embed the emotion for each grid cell, we first define a multivariate Gaussian distribution $\mathcal{N}(\mathbf{x} \mid \bm{\mu}_{\mathbf{p}_i}, \bm{\Sigma}_{\mathbf{p}_i})$ for each occupied grid cell $\mathbf{p}_i=[x,y]^\intercal$, where $\mathbf{x}\in \mathcal{R}^{\bar{H} \times \bar{W}}$, $\bm{\mu}_{\mathbf{p}_i}=[x,y]^\intercal$ and $\bm{\Sigma}_{\mathbf{p}_i} = [\sigma_{x}^2, 0 ; 0, \sigma_{y}^2]$. The covariance matrix is initialized as an identity matrix scaled by a coefficient. In the remainder of the paper, we use the terms $\mathcal{N}(\cdot\mid\bm{\mu}_{\mathbf{p}_i},\bm{\Sigma}_{\mathbf{p}_i})$ and $\mathcal{N}_{\mathbf{p}_i}(\cdot)$ interchangeably to denote the same distribution. Finally, the emotion is calculated as the weighted summation of multivariate Gaussian distributions, as follows:

$$
E(\mathbf{x})=\sum_{\mathbf{p}_i\in \mathcal{O}}w_{\mathbf{p}_i} \mathcal{N}_{\mathbf{p}_i}(\mathbf{x}),
$$

where $\mathcal{O}$ is the set of occupied grid cells, and $w_{\mathbf{p}_i}$ is the weight parameter. Note that, to reduce computation time for calculating the emotion at the grid cell, we only consider Gaussian distributions whose value at the grid cell exceeds a specified threshold. The weight parameter $w_{\mathbf{p}_i}$ is initialized based on the number of these valid Gaussian distributions:

$$
w_{\mathbf{p}_i} = \frac{1}{N^{val}_{\mathbf{p}_i}},\ \forall \mathbf{p}_i\in \mathcal{O}.
$$

**中文译文**

为了将情绪嵌入每个网格单元，我们首先为每个被占据的网格单元 $\mathbf{p}_i=[x,y]^\intercal$ 定义一个多元高斯分布 $\mathcal{N}(\mathbf{x} \mid \bm{\mu}_{\mathbf{p}_i}, \bm{\Sigma}_{\mathbf{p}_i})$，其中 $\mathbf{x}\in \mathcal{R}^{\bar{H} \times \bar{W}}$，$\bm{\mu}_{\mathbf{p}_i}=[x,y]^\intercal$，且 $\bm{\Sigma}_{\mathbf{p}_i} = [\sigma_{x}^2, 0 ; 0, \sigma_{y}^2]$。协方差矩阵初始化为由某一系数缩放的单位矩阵。在本文其余部分，我们交替使用 $\mathcal{N}(\cdot\mid\bm{\mu}_{\mathbf{p}_i},\bm{\Sigma}_{\mathbf{p}_i})$ 和 $\mathcal{N}_{\mathbf{p}_i}(\cdot)$ 来表示同一分布。最后，情绪被计算为多个多元高斯分布的加权求和，如下所示：

$$
E(\mathbf{x})=\sum_{\mathbf{p}_i\in \mathcal{O}}w_{\mathbf{p}_i} \mathcal{N}_{\mathbf{p}_i}(\mathbf{x}),
$$

其中 $\mathcal{O}$ 是被占据网格单元的集合，$w_{\mathbf{p}_i}$ 是权重参数。需要注意的是，为了减少计算网格单元情绪值的时间，我们只考虑在该网格单元处取值超过指定阈值的高斯分布。权重参数 $w_{\mathbf{p}_i}$ 基于这些有效高斯分布的数量进行初始化：

$$
w_{\mathbf{p}_i} = \frac{1}{N^{val}_{\mathbf{p}_i}},\ \forall \mathbf{p}_i\in \mathcal{O}.
$$

**Original**

We initialize the weight as the reciprocal of the number of valid Gaussian distributions $N^{val}_{\mathbf{p}_i}$ to ensure that the emotion at the grid cell is not disproportionately influenced by the number of these distributions. The covariance matrix and the weight parameter constitute the emotion parameters $\Theta^{emo}_i=\{\bm{\Sigma}_{\mathbf{p}_i},w_{\mathbf{p}_i}\}$ for each occupied grid cell. These parameters are stored in $\mathcal{M}$ along with the visual-language feature and updated based on the agent's experiences.

**中文译文**

我们将权重初始化为有效高斯分布数量 $N^{val}_{\mathbf{p}_i}$ 的倒数，以确保网格单元处的情绪值不会受到这些分布数量的不成比例影响。对于每个被占据的网格单元，协方差矩阵和权重参数共同构成情绪参数 $\Theta^{emo}_i=\{\bm{\Sigma}_{\mathbf{p}_i},w_{\mathbf{p}_i}\}$。这些参数与视觉-语言特征一起存储在 $\mathcal{M}$ 中，并基于智能体经验进行更新。

### 3.2 Reflecting Emotion and Updating E2Map / 反映情绪并更新 E2Map

**Original**

The proposed methodology leverages the capabilities of LLM and LMM to update the E2Map based on the agent's navigation experiences. First, when the agent encounters an event, the event descriptor, an LMM, generates a language description that explains the image sequence of the situation. To narrow the scope of the problem, we assume that the agent's events are indicated through a simulator or sensor information, rather than relying on a separate event detection algorithm. Then, an emotion evaluator, an LLM, assesses the agent's emotional response to the experience. The emotion evaluator takes the language description of the situation as input and evaluates the emotion as a score based on two criteria. Finally, E2Map is updated considering the emotion score and the grid cells' location to update. The proposed methodology uses GPT-4o [29] for the event descriptor and Llama3 [30] for the emotion evaluator. A detailed explanation of each process is provided below.

**中文译文**

本文方法利用 LLM 和 LMM 的能力，根据智能体的导航经验更新 E2Map。首先，当智能体遇到某个事件时，作为 LMM 的事件描述器会生成一段语言描述，用来解释该情境的图像序列。为了缩小问题范围，我们假设智能体事件由仿真器或传感器信息给出，而不是依赖单独的事件检测算法。随后，作为 LLM 的情绪评估器评估智能体对该经验的情绪反应。情绪评估器以情境的语言描述为输入，并基于两个准则将情绪评估为分数。最后，系统根据情绪分数以及需要更新的网格单元位置来更新 E2Map。本文方法使用 GPT-4o [29] 作为事件描述器，并使用 Llama3 [30] 作为情绪评估器。下面给出每个过程的详细说明。

#### 3.2.1 Event descriptor / 事件描述器

**Original**

The event descriptor generates a language description that explains the sequence of images of the agent's experience. To enable the LMM to describe the situation, we input three images to the model: the image captured before the event $I_{t_{evt}-h}$, the image at the time of event $I_{t_{evt}}$, and the image after the event $I_{t_{evt}+h}$, where $t_{evt}$ is the timestep when the event occurred and $h$ is the hyperparameter. The LMM is then prompted with these images to generate a description of the event. To enable the LMM to provide a detailed description of the situation, we employ step-by-step reasoning, known for its strong performance in zero-shot prompting [31]. Specifically, instead of merely requesting a single description for the three images, we prompt the LMM by first indicating that the images represent sequential scenes of an event, requesting it to describe each scene individually and then combine them into a comprehensive explanation of the entire situation.

$$
l_{evt}=\mathcal{F}_{ed}(I_{t_{evt}-h},I_{t_{evt}},I_{t_{evt}+h},p_{ed}),
$$

where $l_{evt}$ is the description of the event, $\mathcal{F}_{ed}$ is the event descriptor, and $p_{ed}$ is the prompt of the event descriptor.

**中文译文**

事件描述器会生成一段语言描述，用来解释智能体经验中的图像序列。为了让 LMM 描述情境，我们向模型输入三张图像：事件发生前捕获的图像 $I_{t_{evt}-h}$、事件发生时的图像 $I_{t_{evt}}$，以及事件发生后的图像 $I_{t_{evt}+h}$，其中 $t_{evt}$ 是事件发生的时间步，$h$ 是超参数。随后，系统用这些图像提示 LMM 生成事件描述。为了让 LMM 给出更细致的情境描述，我们采用逐步推理；该方法已知在零样本提示中表现很强 [31]。具体而言，我们并不是简单要求模型为三张图像生成一段描述，而是先提示 LMM：这些图像表示某一事件的连续场景；然后要求它分别描述每个场景，最后将这些描述整合为对整个情境的完整解释。

$$
l_{evt}=\mathcal{F}_{ed}(I_{t_{evt}-h},I_{t_{evt}},I_{t_{evt}+h},p_{ed}),
$$

其中 $l_{evt}$ 是事件描述，$\mathcal{F}_{ed}$ 是事件描述器，$p_{ed}$ 是事件描述器的提示。

![Fig. 3 Emotion evaluator prompt example](<E2Map Experience-and-Emotion Map for Self-Reflective Robot Navigation with Language Models.assets/ee_prompt.png>)

**Original Caption**

Figure 3. An example of a few-shot prompt for the emotion evaluator: The sentences highlighted in gray provide instructions to inform the LLM about the task. The sentence highlighted in green serves as an event description, while the sentences highlighted in blue demonstrate how to evaluate emotion. The full prompts for the event descriptor and emotion evaluator are provided in the supplementary material.

**中文图注**

图 3. 情绪评估器的少样本提示示例：灰色高亮句子为 LLM 提供任务说明；绿色高亮句子作为事件描述；蓝色高亮句子展示如何评估情绪。事件描述器和情绪评估器的完整提示见补充材料。

#### 3.2.2 Emotion evaluator / 情绪评估器

**Original**

The emotion evaluator assesses the agent's emotional response based on the language description of the situation generated by the event descriptor. To enable the LLM to evaluate the emotions related to the situation, we utilize few-shot prompting. An example of manually created few-shot prompts is shown in Fig. 3. We defined two criteria for evaluating emotions: upsetness, which represents the impact the agent feels in the given situation, and guiltiness, which represents the impact on the environment caused by the agent's actions. Our criteria are inspired by human emotions that drive avoidance and reparative behavior [32, 33, 34]. We employed few-shot prompting to instruct the LLM to provide scores out of three for each criterion and to explain the reasons behind these scores. The final emotion score is computed by adding the two scores.

$$
s_{emo}=\mathcal{F}_{ee}(l_{evt},p_{ee}),
$$

where $s_{emo}$ is the emotion score, $\mathcal{F}_{ee}$ is the emotion evaluator, and $p_{ee}$ is the few-shot prompt of emotion evaluator. Note that, although this study addressed negative emotions such as upsetness and guiltiness, demonstrations of the emotion evaluator for assessing positive emotions are provided in the supplementary material.

**中文译文**

情绪评估器基于事件描述器生成的情境语言描述，评估智能体的情绪反应。为了让 LLM 能够评估与该情境相关的情绪，我们使用少样本提示。图 3 展示了一个人工构造的少样本提示示例。我们定义了两个情绪评估准则：受挫程度（upsetness），表示智能体在给定情境中感受到的影响；内疚程度（guiltiness），表示智能体行为对环境造成的影响。我们的准则受到人类情绪的启发，因为这类情绪会驱动回避行为和补偿性行为 [32, 33, 34]。我们使用少样本提示，要求 LLM 为每个准则给出三分制评分，并解释评分原因。最终情绪分数由两个分数相加得到。

$$
s_{emo}=\mathcal{F}_{ee}(l_{evt},p_{ee}),
$$

其中 $s_{emo}$ 是情绪分数，$\mathcal{F}_{ee}$ 是情绪评估器，$p_{ee}$ 是情绪评估器的少样本提示。需要注意的是，尽管本文处理了受挫程度和内疚程度等负面情绪，但补充材料中也提供了用于评估正面情绪的情绪评估器示例。

**Original**

To update the E2Map, we first identify the locations of the $n$ grid cells, denoted as $\mathbf{p}_{update}$, associated with the object or space involved in the event, taking into account the agent's pose at the time of the event. Next, we calculate the unit direction vector $\Vec{\mathbf{v}}=(v_x, v_y)$ representing the agent's orientation at the time of the event. This vector is used to adjust the emotion parameters of each relevant grid cell based on the emotion score. We then update the standard deviation of each diagonal element in the covariance matrix by incorporating both the emotion score and the corresponding component of the direction vector. Our update rule is inspired by the Weber–Fechner law [35], which states that the intensity of a sensation increases as the logarithm of the stimulus. The standard deviation is updated as follows:

$$
\sigma_{k}^{new}=\sigma_{k}v_k\log\left(\frac{s_{emo}}{T}\right),\ \textrm{where}\ k\in\{x,y\},
$$

$(\cdot)^{new}$ refers to the updated value or function, and $T$ is the temperature parameter.

**中文译文**

为了更新 E2Map，我们首先确定与事件中涉及的物体或空间相关的 $n$ 个网格单元位置，记为 $\mathbf{p}_{update}$，同时考虑事件发生时智能体的位姿。接着，我们计算单位方向向量 $\Vec{\mathbf{v}}=(v_x, v_y)$，它表示事件发生时智能体的朝向。该向量用于根据情绪分数调整每个相关网格单元的情绪参数。随后，我们结合情绪分数和方向向量的相应分量，更新协方差矩阵中各对角元素的标准差。我们的更新规则受到韦伯-费希纳定律 [35] 启发，该定律指出，感觉强度会随刺激的对数增长。标准差更新如下：

$$
\sigma_{k}^{new}=\sigma_{k}v_k\log\left(\frac{s_{emo}}{T}\right),\ \textrm{where}\ k\in\{x,y\},
$$

其中 $(\cdot)^{new}$ 表示更新后的值或函数，$T$ 是温度参数。

**Original**

By updating the covariance matrix, the multivariate Gaussian distribution expands, which means the emotional response to the event affects a broader spatial area. However, since a multivariate Gaussian distribution is a probability density function that integrates to one over all regions, increasing the covariance reduces the value of the distribution at the grid cell's location. This results in a smaller emotion value at the grid cell according to Eq. (1). To ensure that the emotion at the grid cell is maintained even after the covariance update, we propose a simple method for updating the weight parameter $w_{\mathbf{p}_i}$ as follows:

$$
w_{\mathbf{p}_i}^{new} = w_{\mathbf{p}_i}\frac{\mathcal{N}_{\mathbf{p}_i}(\mathbf{p}_i)}{\mathcal{N}^{new}_{\mathbf{p}_i}(\mathbf{p}_i)}.
$$

By updating the emotion parameters according to Eq. (4) and Eq. (5), we can expand the spatial extent of the emotion's influence by recalculating Eq. (1), while preserving the magnitude of the emotion within the given grid cell.

**中文译文**

通过更新协方差矩阵，多元高斯分布会扩展，这意味着事件引发的情绪反应会影响更广的空间区域。然而，由于多元高斯分布是一个在所有区域积分为 1 的概率密度函数，增大协方差会降低该分布在网格单元位置处的取值。根据式（1），这会导致该网格单元处的情绪值变小。为了保证即使在协方差更新后，网格单元处的情绪仍能保持，我们提出一种简单方法来更新权重参数 $w_{\mathbf{p}_i}$：

$$
w_{\mathbf{p}_i}^{new} = w_{\mathbf{p}_i}\frac{\mathcal{N}_{\mathbf{p}_i}(\mathbf{p}_i)}{\mathcal{N}^{new}_{\mathbf{p}_i}(\mathbf{p}_i)}.
$$

按照式（4）和式（5）更新情绪参数后，我们可以通过重新计算式（1）扩展情绪影响的空间范围，同时保持给定网格单元内的情绪强度。

**Original Caption**

Algorithm 1. Navigation with E2Map in the real world.

**中文标题**

算法 1. 真实世界中使用 E2Map 进行导航。

**Original**

~~~text
goal_list = GoalSelector(l_inst)
p_agent = Localization(P_0)
for goal in goal_list:
    tau = Planning(p_agent, goal, M)
    while not arrived(goal):
        a_t = MPPI(p_agent, tau)
        agent.run(a_t)
        p_agent = Localization(P_t)
        if event occurs:
            l_evt = F_ed(I_{t_evt-h}, I_{t_evt}, I_{t_evt+h}, p_ed)
            s_emo = F_ee(l_evt, p_ee)
            p_update = get_update_pose(p_agent)
            M.update(s_emo, p_update)
            tau = Planning(p_agent, goal, M)
        t = t + 1
~~~

**中文译文**

~~~text
目标列表 = 目标选择器(l_inst)
p_agent = 定位(P_0)
对于 目标列表中的每个目标:
    tau = 规划(p_agent, 目标, M)
    当 尚未到达(目标) 时:
        a_t = MPPI(p_agent, tau)
        智能体.run(a_t)
        p_agent = 定位(P_t)
        如果 事件发生:
            l_evt = F_ed(I_{t_evt-h}, I_{t_evt}, I_{t_evt+h}, p_ed)
            s_emo = F_ee(l_evt, p_ee)
            p_update = get_update_pose(p_agent)
            M.update(s_emo, p_update)
            tau = 规划(p_agent, 目标, M)
        t = t + 1
~~~

### 3.3 Navigating with E2Map / 使用 E2Map 进行导航

**Original**

In this section, we explain how the proposed system works using E2Map. The overall algorithm is presented in Algorithm 1. When a language instruction $l_{inst}$ is received from the user, the *goal selector* converts this instruction into code that utilizes the goal selection APIs to determine the goal locations (line 1), as shown in Fig. 2(b). The goal selection API returns the location of the grid cell that the robot needs to visit, considering the object mentioned in the language instruction and the spatial information related to that object. A detailed explanation of the *goal selector* is provided in the supplementary material.

**中文译文**

本节说明所提系统如何使用 E2Map 工作。整体算法见算法 1。当系统从用户处接收到语言指令 $l_{inst}$ 时，*目标选择器* 会将该指令转换为代码，并调用目标选择 API 来确定目标位置（第 1 行），如图 2(b) 所示。目标选择 API 会结合语言指令中提到的物体及其相关空间信息，返回机器人需要访问的网格单元位置。*目标选择器* 的详细说明见补充材料。

**Original**

Once the goal is determined, the agent can use any cost-based off-the-shelf navigation system to move towards the goal. We use the D$^*$ algorithm [36] for path planning, MPPI [37] for control, and 3D LiDAR-based localization [38] for pose estimation. The agent's initial pose is estimated using LiDAR point cloud $P_0$ (line 2), and D$^*$ algorithm generates a minimum-cost path $\tau$ to the destination, using the emotion computed by Eq. (1) as a cost (line 4). The MPPI algorithm then calculates the control values $a_t$ to follow this path, based on the agent's current position $p_{agent}$ (line 6). During the agent's movement, a localization algorithm estimates the agent's position in real-time (line 8).

**中文译文**

目标确定后，智能体可以使用任意基于代价的现成导航系统向目标移动。本文使用 D$^*$ 算法 [36] 进行路径规划，使用 MPPI [37] 进行控制，并使用基于三维 LiDAR 的定位方法 [38] 进行位姿估计。智能体的初始位姿由 LiDAR 点云 $P_0$ 估计得到（第 2 行），D$^*$ 算法以式（1）计算出的情绪作为代价，生成到目标的最小代价路径 $\tau$（第 4 行）。随后，MPPI 算法根据智能体当前位置 $p_{agent}$ 计算控制量 $a_t$，以跟随该路径（第 6 行）。在智能体移动过程中，定位算法会实时估计智能体位置（第 8 行）。

**Original**

If the agent encounters an event during navigation, the E2Map is updated (line 9--13), as described in Section 3.2. When the navigation cost (emotion) changes, the D$^*$ algorithm recalculates a new minimum-cost path (line 14). This allows the agent to adjust its behavior in a one-shot manner based on a single experience.

**中文译文**

如果智能体在导航过程中遇到事件，E2Map 会按照第 3.2 节所述进行更新（第 9--13 行）。当导航代价（情绪）发生变化时，D$^*$ 算法会重新计算新的最小代价路径（第 14 行）。这使智能体能够基于一次经验，以单次经验驱动的方式调整自身行为。

**Original**

Our method with E2Map appears similar to a potential field [39], where negative emotions act like repulsive forces and the goal functions as an attractive force. However, to circumvent the local minima problem inherent in potential fields, we employed a separate planner to determine the path toward the goal, instead of using the goal as the attractive force within the potential field.

**中文译文**

本文使用 E2Map 的方法看起来类似于势场法 [39]：负面情绪类似斥力，目标则类似吸引力。然而，为了规避势场法固有的局部极小值问题，我们没有在势场中将目标作为吸引力，而是采用独立的规划器来确定通往目标的路径。

![Fig. 4 Gazebo environment](<E2Map Experience-and-Emotion Map for Self-Reflective Robot Navigation with Language Models.assets/209_gazebo.png>)

![Fig. 4 E2Map](<E2Map Experience-and-Emotion Map for Self-Reflective Robot Navigation with Language Models.assets/209_e2map.png>)

**Original Caption**

Figure 4. We evaluated our method in the ROS Gazebo simulator. (a) We scanned the real-world setup using a 3D scanner and transferred the 3D model to the Gazebo simulator. (b) The initial E2Map for the environment.

**中文图注**

图 4. 我们在 ROS Gazebo 仿真器中评估了本文方法。（a）我们使用三维扫描仪扫描真实世界实验布置，并将三维模型转移到 Gazebo 仿真器中。（b）该环境的初始 E2Map。

## 4. Experiments / 实验

### 4.1 Experimental Setup / 实验设置

**Original**

We conducted experiments in both simulated and real-world environments. Using the ROS Gazebo simulator [40], we created a simulated environment that mirrored the real-world setup used for evaluation, as shown in Fig. 4. In the simulated environment, we designed three scenarios to assess our method (Fig. 5). First, after building the initial E2Map, we introduced a new static obstacle, such as a danger sign (*danger sign*), to evaluate the method's ability to adapt to environmental changes. Second, we positioned a human figure behind a wall and had a human step out unexpectedly (*human-wall*). Third, we added a door that opened unexpectedly as the robot approached (*dynamic door*). The *human-wall* and *dynamic door* scenarios were designed to test whether our method could adjust behavior based on experiences with dynamic events.

**中文译文**

我们在仿真环境和真实世界环境中都进行了实验。使用 ROS Gazebo 仿真器 [40]，我们创建了一个与真实评估设置相对应的仿真环境，如图 4 所示。在仿真环境中，我们设计了三个场景来评估本文方法（图 5）。首先，在构建初始 E2Map 后，我们引入新的静态障碍物，例如危险标志（*danger sign*），以评估该方法适应环境变化的能力。其次，我们将一个人形物体置于墙后，并让人突然走出（*human-wall*）。第三，我们加入一扇门，当机器人接近时它会意外打开（*dynamic door*）。*human-wall* 和 *dynamic door* 场景用于测试本文方法是否能够基于动态事件经验调整行为。

**Original**

For quantitative analysis, we compared our method against baselines with state-of-the-art performance in open-vocabulary object navigation [23, 9]. Our method and the baselines received identical language instructions and navigated accordingly, with success rates calculated for performance evaluation. Details about the baseline methods are provided in the supplementary material. After evaluation in the simulated environment, we demonstrated the scalability and applicability of our method in real-world scenarios.

**中文译文**

在定量分析中，我们将本文方法与开放词汇目标导航中具有先进性能的基线方法 [23, 9] 进行比较。本文方法和基线方法接收相同语言指令，并据此导航；我们计算成功率作为性能评估指标。基线方法的细节见补充材料。在仿真环境评估之后，我们进一步在真实世界场景中展示本文方法的可扩展性与适用性。

![Fig. 5 Danger sign](<E2Map Experience-and-Emotion Map for Self-Reflective Robot Navigation with Language Models.assets/danger_sign.png>)

![Fig. 5 Human-wall](<E2Map Experience-and-Emotion Map for Self-Reflective Robot Navigation with Language Models.assets/human_wall.png>)

![Fig. 5 Dynamic door](<E2Map Experience-and-Emotion Map for Self-Reflective Robot Navigation with Language Models.assets/dynamic_door.png>)

**Original Caption**

Figure 5. Three experimental scenarios.

**中文图注**

图 5. 三个实验场景。

![Fig. 6 Before the event](<E2Map Experience-and-Emotion Map for Self-Reflective Robot Navigation with Language Models.assets/before_e2map_gazebo.png>)

![Fig. 6 After the event](<E2Map Experience-and-Emotion Map for Self-Reflective Robot Navigation with Language Models.assets/after_e2map_gazebo.png>)

**Original Caption**

Figure 6. Update of the E2Map and behavior adjustment after an event: The spatial extent of the wall's emotional influence expands following incidents, such as a collision with a person stepping out from behind the wall. After the E2Map is updated, the robot adjusts its behavior to maintain a safe distance from the wall, preventing future collisions with humans.

**中文图注**

图 6. 事件发生后 E2Map 的更新与行为调整：在发生诸如与从墙后走出的人碰撞等事件后，墙的情绪影响空间范围会扩大。E2Map 更新后，机器人会调整行为，在经过墙附近时保持安全距离，从而避免未来再次与人发生碰撞。

**Original Caption**

Table 2. Quantitative Results in Simulated Environment.

**中文表题**

表 2. 仿真环境中的定量结果。

| Methods | *static* | *danger sign* | *human-wall* | *dynamic door* |
|---|---:|---:|---:|---:|
| LM-Nav [23] | 5/10 | 1/10 | 0/10 | 1/10 |
| VLMaps [9] | 10/10 | 0/10 | 0/10 | 0/10 |
| E2Map (ours) | **10/10** | **9/10** | **9/10** | **9/10** |

**中文译表**

| 方法 | 静态环境 | 危险标志 | 人-墙 | 动态门 |
|---|---:|---:|---:|---:|
| LM-Nav [23] | 5/10 | 1/10 | 0/10 | 1/10 |
| VLMaps [9] | 10/10 | 0/10 | 0/10 | 0/10 |
| E2Map（本文方法） | **10/10** | **9/10** | **9/10** | **9/10** |

### 4.2 Experiments in Simulated Environment / 仿真环境实验

**Original**

In the simulated environment, we provided ten different language instructions for both our method and the baselines for each of the three scenarios and calculated the success rate. For each episode, the robot started from the same position, and the language instructions referred to a maximum of four objects. Full language instructions are provided in the supplementary material. Success was defined as the robot reaching all goals in order without collisions, with a goal considered reached if the robot was within a specified distance from it. The episode was reset if a collision occurred or the agent reached the goal. Table 2 showed the results.

**中文译文**

在仿真环境中，对于三个场景中的每一个，我们为本文方法和基线方法提供十条不同语言指令，并计算成功率。每个回合中，机器人都从同一位置出发，语言指令最多涉及四个物体。完整语言指令见补充材料。成功定义为机器人按顺序到达所有目标且不发生碰撞；如果机器人距离目标小于指定距离，则认为到达该目标。一旦发生碰撞或智能体到达目标，该回合即被重置。表 2 给出了实验结果。

**Original**

We first evaluated our method and the baselines in a *static* environment, without environmental changes or dynamic events, to assess their baseline performance using language instructions from the *danger sign* scenario. As shown in the table, both our method and VLMaps succeeded in all ten attempts, while LM-Nav succeeded only five times. The challenges LM-Nav faces in multi-goal navigation were previously noted in [9]. In scenarios involving environmental changes and dynamic events, our method outperforms baselines in all three scenarios, as shown in the table. We found that the baselines repeatedly collided with the danger sign, human figure, and dynamic door, despite having previously encountered similar situations. In some cases, LM-Nav succeeded in the *danger sign* and *dynamic door* scenarios because its topological graph-based goal selection algorithm occasionally chose goal positions where the robot avoided encountering the danger sign and the door. In contrast, in the *danger sign* scenario, while our method initially collided with the danger sign, it avoided it in subsequent encounters by updating the E2Map. Similarly, in the *human-wall* and *dynamic door* scenarios, after experiencing collisions with the human figure and dynamic door, our method adapted its behavior to maintain a safe distance from both the wall and the door when passing by them. The qualitative result of our method in *human-wall* scenario is provided in Fig. 6. The results demonstrated that our method can adjust the agent's behavior in a one-shot manner, leading to a higher success rate in scenarios with environmental changes and dynamic events. Examples of qualitative results from the *event descriptor* and *emotion evaluator* for each scenario are provided in the supplementary material.

**中文译文**

我们首先在无环境变化、无动态事件的 *static* 环境中评估本文方法和基线方法，以 *danger sign* 场景中的语言指令测试其基础性能。如表中所示，本文方法和 VLMaps 在十次尝试中全部成功，而 LM-Nav 只成功五次。LM-Nav 在多目标导航中面临的困难此前已在 [9] 中被指出。在包含环境变化和动态事件的场景中，如表所示，本文方法在全部三个场景中均优于基线。我们发现，尽管基线方法此前已经遇到过类似情境，它们仍反复与危险标志、人形物体和动态门发生碰撞。在某些情况下，LM-Nav 在 *danger sign* 和 *dynamic door* 场景中能够成功，是因为其基于拓扑图的目标选择算法偶尔选择了机器人不会遇到危险标志或门的位置。相比之下，在 *danger sign* 场景中，尽管本文方法最初会与危险标志碰撞，但它会通过更新 E2Map 在后续遭遇中避开危险标志。类似地，在 *human-wall* 和 *dynamic door* 场景中，本文方法在经历与人形物体和动态门的碰撞后，会调整行为，在经过墙和门附近时保持安全距离。本文方法在 *human-wall* 场景中的定性结果见图 6。结果表明，本文方法能够以单次经验驱动的方式调整智能体行为，从而在包含环境变化和动态事件的场景中获得更高成功率。每个场景中 *事件描述器* 和 *情绪评估器* 的定性结果示例见补充材料。

![Fig. 7 Real-world setup](<E2Map Experience-and-Emotion Map for Self-Reflective Robot Navigation with Language Models.assets/209_realworld.png>)

**Original Caption**

Figure 7. Real-world setup for the experiments.

**中文图注**

图 7. 实验的真实世界设置。

### 4.3 Experiments in Real World / 真实世界实验

**Original**

To evaluate the scalability and applicability of our method in real-world settings, we first set up a real-world environment by placing objects such as a sofa, chair, table, refrigerator, and microwave in the conference room at Seoul National University, as shown in Fig. 7. We used the same language instructions as in the simulation and incorporated real humans and danger signs to replicate the *danger sign* and *human-wall* scenarios from the simulation. We excluded the *dynamic door* scenario to prevent possible damage to the robot and the conference room door from collisions. As shown in Table 3, our method demonstrated performance similar to that in the simulated environment, indicating its potential for real-world applications.

**中文译文**

为了评估本文方法在真实世界设置中的可扩展性和适用性，我们首先在首尔国立大学的一间会议室中布置了沙发、椅子、桌子、冰箱和微波炉等物体，构建真实世界环境，如图 7 所示。我们使用与仿真中相同的语言指令，并加入真实人类和危险标志，以复现仿真中的 *danger sign* 和 *human-wall* 场景。为了避免碰撞可能损坏机器人和会议室门，我们排除了 *dynamic door* 场景。如表 3 所示，本文方法表现出与仿真环境相近的性能，表明其具备真实世界应用潜力。

**Original Caption**

Table 3. Quantitative Results in Real-world Environment.

**中文表题**

表 3. 真实世界环境中的定量结果。

| Methods | *static* | *danger sign* | *human-wall* |
|---|---:|---:|---:|
| E2Map (ours) | **10/10** | **9/10** | **9/10** |

**中文译表**

| 方法 | 静态环境 | 危险标志 | 人-墙 |
|---|---:|---:|---:|
| E2Map（本文方法） | **10/10** | **9/10** | **9/10** |

## 5. Conclusion / 结论

**Original**

In this paper, we proposed E2Map, a spatial map that captures the agent's emotional responses to its experiences, inspired by human emotional mechanisms. By updating E2Map using various LLM capabilities, the agent can adjust its behavior in a one-shot manner after encountering specific events. Experiments in both simulated and real-world environments demonstrated that our method significantly improves navigation performance in stochastic scenarios. However, there are several promising directions for future work. Our method relies on simulator or sensor information to trigger E2Map updates. Integrating anomaly detection algorithms to autonomously identify such events would be a valuable enhancement. Furthermore, although we demonstrated that our method can also address positive emotions, our experiments primarily involved scenarios with negative emotions. Future work could explore the extension of the methodology to tasks involving positive emotions to provide a more comprehensive evaluation of its applicability.

**中文译文**

本文提出 E2Map：一种受人类情绪机制启发、用于捕获智能体对自身经验产生的情绪反应的空间地图。通过使用 LLM 的多种能力更新 E2Map，智能体在遇到特定事件后能够以单次经验驱动的方式调整自身行为。在仿真环境和真实世界环境中的实验表明，本文方法显著提升了随机场景中的导航性能。不过，未来仍有若干有前景的研究方向。本文方法依赖仿真器或传感器信息来触发 E2Map 更新。若能整合异常检测算法，使系统自主识别此类事件，将是一个有价值的增强方向。此外，尽管我们展示了本文方法也能够处理正面情绪，但实验主要涉及负面情绪场景。未来工作可以探索将该方法扩展到涉及正面情绪的任务中，从而更全面地评估其适用性。

**Original**

We believe that our work contributes to advancing the development of strong autonomy in robotics.

**中文译文**

我们相信，本文工作有助于推动机器人强自主性的发展。

## Acknowledgment / 致谢

**Original**

This research was funded by the Korean Ministry of Land, Infrastructure and Transport through the Smart City Innovative Talent Education Program, by the Korea Institute for Advancement of Technology under a MOTIE grant (P0020536), and by the Ministry of Education and the NRF of Korea. K. Kim, D. Jung, and the corresponding author are affiliated with the Smart City Global Convergence program. Research facilities were provided by the Institute of Engineering Research at Seoul National University.

**中文译文**

本研究获得韩国国土交通部“智慧城市创新人才教育项目”、韩国产业技术振兴院 MOTIE 资助项目（P0020536）、韩国教育部以及韩国国家研究基金会（NRF）的资助。K. Kim、D. Jung 和通讯作者隶属于 Smart City Global Convergence 项目。研究设施由首尔国立大学工程研究所提供。

## References / 参考文献

**Original**

The original paper uses IEEE references managed by `root.bbl` and `root.bib`. To preserve bibliographic fidelity, the reference list below keeps titles and publication metadata in their original English form.

**中文译文**

原论文使用 `root.bbl` 与 `root.bib` 管理 IEEE 格式参考文献。为保持文献信息准确，下面的参考文献列表保留英文题名与出版信息。

1. W. Huang, P. Abbeel, D. Pathak, and I. Mordatch, “Language models as zero-shot planners: Extracting actionable knowledge for embodied agents,” ICML, 2022.
2. B. Ichter et al., “Do as I can, not as I say: Grounding language in robotic affordances,” CoRL, 2022.
3. W. Huang et al., “Inner monologue: Embodied reasoning through planning with language models,” CoRL, 2022.
4. J. Liang et al., “Code as policies: Language model programs for embodied control,” ICRA, 2023.
5. Y. Mu et al., “Robocodex: Multimodal code generation for robotic behavior synthesis,” ICML, 2024.
6. J. Chen et al., “Roboscript: Code generation for free-form manipulation tasks across real and simulation,” CoRR, 2024.
7. W. Huang et al., “Voxposer: Composable 3D value maps for robotic manipulation with language models,” CoRL, 2023.
8. B. Chen et al., “Open-vocabulary queryable scene representations for real world planning,” ICRA, 2023.
9. C. Huang, O. Mees, A. Zeng, and W. Burgard, “Visual language maps for robot navigation,” ICRA, 2023.
10. A. R. Damasio, *Feeling & Knowing: Making Minds Conscious*, Pantheon Books, 2021.
11. J. Tierney and R. F. Baumeister, *The Power of Bad: And How to Overcome It*, Penguin UK, 2019.
12. A. Galvez-Pol, M. Nadal, and J. M. Kilner, “Emotional representations of space vary as a function of peoples’ affect and interoceptive sensibility,” *Scientific Reports*, 2021.
13. A. Zeng et al., “Socratic models: Composing zero-shot multimodal reasoning with language,” ICLR, 2023.
14. S. S. Raman et al., “Planning with large language models via corrective re-prompting,” NeurIPS Foundation Models for Decision Making Workshop, 2022.
15. C. H. Song et al., “LLM-Planner: Few-shot grounded planning for embodied agents with large language models,” ICCV, 2023.
16. Y. Ding, X. Zhang, C. Paxton, and S. Zhang, “Task and motion planning with large language models for object rearrangement,” IROS, 2023.
17. W. Yu et al., “Language to rewards for robotic skill synthesis,” CoRL, 2023.
18. S. Y. Gadre et al., “Cows on pasture: Baselines and benchmarks for language-driven zero-shot object navigation,” CVPR, 2023.
19. P. Anderson et al., “Vision-and-language navigation: Interpreting visually-grounded navigation instructions in real environments,” CVPR, 2018.
20. P.-L. Guhur et al., “Airbert: In-domain pretraining for vision-and-language navigation,” ICCV, 2021.
21. J. Krantz et al., “Beyond the nav-graph: Vision-and-language navigation in continuous environments,” ECCV, 2020.
22. Y. Hong, Z. Wang, Q. Wu, and S. Gould, “Bridging the gap between learning in discrete and continuous environments for vision-and-language navigation,” CVPR, 2022.
23. D. Shah et al., “LM-Nav: Robotic navigation with large pre-trained models of language, vision, and action,” CoRL, 2023.
24. A. Radford et al., “Learning transferable visual models from natural language supervision,” ICML, 2021.
25. R. S. Sutton and A. G. Barto, *Reinforcement Learning: An Introduction*, MIT Press, 2018.
26. S. Ross, G. Gordon, and D. Bagnell, “A reduction of imitation learning and structured prediction to no-regret online learning,” AISTATS, 2011.
27. H.-S. Yoon et al., “Self-balancing online dataset for incremental driving intelligence,” IROS, 2021.
28. B. Li et al., “Language-driven semantic segmentation,” ICLR, 2022.
29. OpenAI et al., “GPT-4o system card,” 2024.
30. A. Dubey et al., “The Llama 3 herd of models,” arXiv:2407.21783, 2024.
31. T. Kojima et al., “Large language models are zero-shot reasoners,” NeurIPS, 2022.
32. A. M. Leventhal, “Sadness, depression, and avoidance behavior,” *Behavior Modification*, 2008.
33. M. Ghorbani et al., “Guilt, shame, and reparative behavior: The effect of psychological proximity,” *Journal of Business Ethics*, 2013.
34. M. Pivetti, M. Camodeca, and M. Rapino, “Shame, guilt, and anger: Their cognitive, physiological, and behavioral correlates,” *Current Psychology*, 2016.
35. S. Dehaene, “The neural basis of the Weber-Fechner law: A logarithmic mental number line,” *Trends in Cognitive Sciences*, 2003.
36. A. Stentz, *The D* Algorithm for Real-Time Planning of Optimal Traverses*, 1994.
37. G. Williams, A. Aldrich, and E. Theodorou, “Model predictive path integral control using covariance variable importance sampling,” arXiv:1509.01149, 2015.
38. K. Koide, J. Miura, and E. Menegatti, “A portable three-dimensional LiDAR-based system for long-term and wide-area people behavior measurement,” *International Journal of Advanced Robotic Systems*, 2019.
39. Y. K. Hwang, N. Ahuja, et al., “A potential field approach to path planning,” *IEEE Transactions on Robotics and Automation*, 1992.
40. N. Koenig and A. Howard, “Design and use paradigms for Gazebo, an open-source multi-robot simulator,” IROS, 2004.
41. S. Suzuki et al., “Topological structural analysis of digitized binary images by border following,” *Computer Vision, Graphics, and Image Processing*, 1985.

## Supplementary Material / 补充材料

### Contributions by Person / 个人贡献

**Original**

**Chan Kim** co-led the project, designed and integrated the proposed system, led the real-world experiments, and wrote the paper.

**中文译文**

**Chan Kim** 共同领导该项目，设计并集成所提出的系统，主导真实世界实验，并撰写论文。

**Original**

**Keonwoo Kim** served as the project manager, designed the proposed system, implemented the E2Map update pipeline, led the simulation experiments, and contributed to writing the paper.

**中文译文**

**Keonwoo Kim** 担任项目经理，设计所提出的系统，实现 E2Map 更新流水线，主导仿真实验，并参与论文写作。

**Original**

**Mintaek Oh** implemented a path planning and control algorithm, set up the experimental environment for both simulated and real-world experiments, and supported the real-world experiments.

**中文译文**

**Mintaek Oh** 实现路径规划与控制算法，搭建仿真和真实世界实验环境，并支持真实世界实验。

**Original**

**Hanbi Baek** implemented the goal selector, event descriptor, and emotion evaluator, and designed the corresponding prompts.

**中文译文**

**Hanbi Baek** 实现目标选择器、事件描述器和情绪评估器，并设计相应提示词。

**Original**

**Jiyang Lee** designed and equipped a real quadruped robot with sensors and a computing unit, and implemented a low-level control algorithm for the robot's operation.

**中文译文**

**Jiyang Lee** 设计真实四足机器人并为其配置传感器和计算单元，同时实现机器人运行所需的底层控制算法。

**Original**

**Donghwi Jung** implemented a LiDAR-based localization and mapping system for real-world experiments.

**中文译文**

**Donghwi Jung** 为真实世界实验实现基于 LiDAR 的定位与建图系统。

**Original**

**Soojin Woo** implemented a LiDAR-based localization and mapping system for real-world experiments.

**中文译文**

**Soojin Woo** 为真实世界实验实现基于 LiDAR 的定位与建图系统。

**Original**

**Younkyung Woo** created the 3D model of the real-world environment for the Gazebo simulation.

**中文译文**

**Younkyung Woo** 为 Gazebo 仿真创建真实世界环境的三维模型。

**Original**

**John Tucker** contributed to the discussions on affordance in the framework proposed in this study.

**中文译文**

**John Tucker** 参与了本文所提出框架中关于可供性的讨论。

**Original**

**Roya Firoozi** provided detailed feedback and contributed discussions and ideas related to affordance in the writing of this paper.

**中文译文**

**Roya Firoozi** 在论文写作过程中提供了详细反馈，并贡献了与可供性相关的讨论和想法。

**Original**

**Seung-Woo Seo** advised on the project and helped guide the research direction.

**中文译文**

**Seung-Woo Seo** 为项目提供建议，并帮助指导研究方向。

**Original**

**Mac Schwager** discussed the idea of language-based robot control and planning as a joint research topic during S. Kim's visit to his lab and provided valuable feedback, as well as opportunities for discussions between the two labs of Seoul National University and Stanford.

**中文译文**

**Mac Schwager** 在 S. Kim 访问其实验室期间，将基于语言的机器人控制与规划作为联合研究主题进行讨论，并提供了宝贵反馈，也为首尔国立大学和斯坦福两所实验室之间的交流创造了机会。

**Original**

**Seong-Woo Kim** came up with the basic idea for this paper while staying at Schwager's Lab at Stanford. As the principal investigator, he organized and launched the research team and named the project ``E2Map.'' The connection between the two different modalities, language and space, was inspired by Damasio's book [10], which suggests that emotions encompass the spatial concept of homeostasis.

**中文译文**

**Seong-Woo Kim** 在斯坦福 Schwager 实验室访问期间提出了本文的基本想法。作为项目负责人，他组织并启动研究团队，并将项目命名为 “E2Map”。语言与空间这两种不同模态之间的联系受到 Damasio 著作 [10] 的启发；该书指出，情绪包含稳态这一空间性概念。

![Fig. S1 Object grounding](<E2Map Experience-and-Emotion Map for Self-Reflective Robot Navigation with Language Models.assets/209_object_grounding.png>)

**Original Caption**

Figure S1. The qualitative results of object grounding in the experimental environment.

**中文图注**

图 S1. 实验环境中目标锚定的定性结果。

### Goal Selector / 目标选择器

**Original**

The *goal selector* is an LLM that translates free-form language instructions into code, using goal selection APIs to identify goal locations. We use Llama3 [30] for the *goal selector*. The list of goal selection APIs is provided in Table S1. These APIs localize objects by calculating the similarity between visual-language features from $\mathcal{M}_{lang}$ and the text embeddings of the object, similar to the approach in [9].

**中文译文**

*目标选择器* 是一个 LLM，它将自由形式语言指令转换为代码，并使用目标选择 API 识别目标位置。本文使用 Llama3 [30] 作为*目标选择器*。目标选择 API 列表见表 S1。与 [9] 的方法类似，这些 API 通过计算来自 $\mathcal{M}_{lang}$ 的视觉-语言特征与物体文本嵌入之间的相似度来定位物体。

**Original**

First, a pre-trained CLIP text encoder converts the text of the object $l_{obj}$ and a neutral word $l_{neu}$ (e.g., ``other") into vector embeddings $\mathbf{e}_{obj}$ and $\mathbf{e}_{neu}$, respectively, where $\mathbf{e}_{obj}, \mathbf{e}_{neu} \in \mathcal{R}^{C_{lang}}$. The visual-language feature map $\mathcal{M}_{lang} \in \mathcal{R}^{\bar{H} \times \bar{W} \times C_{lang}}$ is then flattened into a matrix $Q \in \mathcal{R}^{\bar{H}\bar{W} \times C_{lang}}$, and similarity $S = Q \cdot [\mathbf{e}_{obj}, \mathbf{e}_{neu}]^\intercal \in \mathcal{R}^{\bar{H}\bar{W} \times 2}$ is computed. By applying the $\argmax$ operator along the row axis of $S$ and reshaping the result to dimensions $\bar{H} \times \bar{W}$, the grid cells corresponding to the given object can be identified. The qualitative result of object grounding in our environment is shown in Fig. S1.

**中文译文**

首先，预训练 CLIP 文本编码器分别将物体文本 $l_{obj}$ 和中性词 $l_{neu}$（例如 “other”）转换为向量嵌入 $\mathbf{e}_{obj}$ 和 $\mathbf{e}_{neu}$，其中 $\mathbf{e}_{obj}, \mathbf{e}_{neu} \in \mathcal{R}^{C_{lang}}$。随后，将视觉-语言特征图 $\mathcal{M}_{lang} \in \mathcal{R}^{\bar{H} \times \bar{W} \times C_{lang}}$ 展平为矩阵 $Q \in \mathcal{R}^{\bar{H}\bar{W} \times C_{lang}}$，并计算相似度 $S = Q \cdot [\mathbf{e}_{obj}, \mathbf{e}_{neu}]^\intercal \in \mathcal{R}^{\bar{H}\bar{W} \times 2}$。沿 $S$ 的行轴应用 $\argmax$ 算子，并将结果重塑为 $\bar{H} \times \bar{W}$ 的维度，即可识别与给定物体对应的网格单元。本文环境中目标锚定的定性结果见图 S1。

**Original**

To remove outliers, we first clustered the grid cells corresponding to the given object using the method described in [41] and then calculated the average similarity score for the grid cells in each cluster. If the number of grid cells in a cluster or the average similarity score is below a specified threshold, the cluster is considered an outlier. After rejecting outliers, we selected the cluster with the highest average similarity score as the object of interest. Finally, considering the spatial information in the language instruction, it selects the grid cell around the object as the goal.

**中文译文**

为了去除离群点，我们首先使用 [41] 中描述的方法，对与给定物体对应的网格单元进行聚类，然后计算每个聚类中网格单元的平均相似度分数。如果某一聚类中的网格单元数量或平均相似度低于指定阈值，则将该聚类视为离群点。剔除离群点后，我们选择平均相似度最高的聚类作为关注对象。最后，系统结合语言指令中的空间信息，选择该物体周围的网格单元作为目标。

**Original Caption**

Table S1. Goal Selection APIs and Their Functions.

**中文表题**

表 S1. 目标选择 API 及其功能。

| APIs | Functions |
|---|---|
| `go_to($l_{obj}$)` | Return the position of the nearest grid cell corresponding to the given object. |
| `go_left_of($l_{obj}$)` | Return the position of the leftmost grid cell corresponding to the given object. |
| `go_right_of($l_{obj}$)` | Return the position of the rightmost grid cell corresponding to the given object. |
| `go_top_of($l_{obj}$)` | Return the position of the uppermost grid cell corresponding to the given object. |
| `go_bottom_of($l_{obj}$)` | Return the position of the bottommost grid cell corresponding to the given object. |
| `go_between($l_{obj1}$, $l_{obj2}$)` | Return the position of the grid cell located between the two given objects. |

**中文译表**

| API | 功能 |
|---|---|
| `go_to($l_{obj}$)` | 返回与给定物体对应的最近网格单元位置。 |
| `go_left_of($l_{obj}$)` | 返回与给定物体对应的最左侧网格单元位置。 |
| `go_right_of($l_{obj}$)` | 返回与给定物体对应的最右侧网格单元位置。 |
| `go_top_of($l_{obj}$)` | 返回与给定物体对应的最上方网格单元位置。 |
| `go_bottom_of($l_{obj}$)` | 返回与给定物体对应的最下方网格单元位置。 |
| `go_between($l_{obj1}$, $l_{obj2}$)` | 返回位于两个给定物体之间的网格单元位置。 |

### Experimental Details / 实验细节

![Fig. S2 Obstacle map](<E2Map Experience-and-Emotion Map for Self-Reflective Robot Navigation with Language Models.assets/vsobstaclemap.png>)

![Fig. S2 E2Map](<E2Map Experience-and-Emotion Map for Self-Reflective Robot Navigation with Language Models.assets/vse2map.png>)

**Original Caption**

Figure S2. Obstacle Map vs. E2Map: The obstacle map used in VLMap is a discrete binary map that does not reflect the agent's experience. In contrast, E2Map is a continuous cost map based on emotion, modeled as a weighted sum of multivariate Gaussian distributions. This allows E2Map to be updated based on the agent's experience by adjusting the emotion parameters.

**中文图注**

图 S2. 障碍物地图与 E2Map 对比：VLMap 使用的障碍物地图是离散二值地图，不反映智能体经验。相比之下，E2Map 是一种基于情绪的连续代价地图，被建模为多元高斯分布的加权和。因此，E2Map 可以通过调整情绪参数，根据智能体经验进行更新。

#### Baselines / 基线方法

**Original**

As outlined in the original paper, we compared our method to state-of-the-art baselines in open-vocabulary object navigation [23, 9]. To isolate the effect of spatial representation on navigation performance, we used the same navigation system for both our method and the baselines. For LM-Nav [23], we utilized its topological graph and language querying system for goal localization. For VLMap [9], we applied our goal selector for goal localization. Once the goal was determined, we generated an obstacle map for robot navigation using the method described in [9]. Specifically, we first defined a list of potential obstacles and performed object grounding by comparing the text of the obstacle list with the visual-language feature map $\mathcal{M}_{lang}$. After that, we set the grid cells to one if they corresponded to obstacles and to zero otherwise, thereby creating the obstacle map as shown in Fig. S2(a). Finally, for both LM-Nav and VLMap, the navigation system generated a path to the goal while avoiding obstacles indicated on the obstacle map.

**中文译文**

如原论文所述，我们将本文方法与开放词汇目标导航中的先进基线方法 [23, 9] 进行比较。为了隔离空间表征对导航性能的影响，我们让本文方法和基线方法使用相同的导航系统。对于 LM-Nav [23]，我们使用其拓扑图和语言查询系统进行目标定位。对于 VLMap [9]，我们应用本文目标选择器进行目标定位。目标确定后，我们使用 [9] 中描述的方法生成用于机器人导航的障碍物地图。具体而言，我们首先定义潜在障碍物列表，并通过比较障碍物列表文本与视觉-语言特征图 $\mathcal{M}_{lang}$ 来进行目标锚定。之后，如果网格单元对应障碍物，则将其设为 1，否则设为 0，由此创建如图 S2(a) 所示的障碍物地图。最后，对于 LM-Nav 和 VLMap，导航系统都会在避开障碍物地图所示障碍物的同时生成通往目标的路径。

#### Full List of Language Instructions / 语言指令完整列表

**Original**

The complete set of language instructions used in our experiments is detailed in Table S2. As outlined in the original paper, the language instructions referenced up to four objects. Note that, to ensure that the robot navigates to the area behind the wall in the *human-wall* scenario, the final object in the instruction is the picture positioned behind the walls.

**中文译文**

实验中使用的完整语言指令见表 S2。如原论文所述，语言指令最多引用四个物体。需要注意的是，为了确保机器人在 *human-wall* 场景中导航到墙后区域，指令中的最后一个物体是放置在墙后的图片。

![Fig. S3 Quadruped robot](<E2Map Experience-and-Emotion Map for Self-Reflective Robot Navigation with Language Models.assets/limbo_spec.png>)

**Original Caption**

Figure S3. The quadruped robot used in the experiments.

**中文图注**

图 S3. 实验中使用的四足机器人。

#### Hardware Setup / 硬件设置

**Original**

For both simulation and real-world experiments, we used a Unitree Go1 quadruped robot. In the simulation, we utilized ground truth pose data, while in the real world, we estimated the robot’s pose using LiDAR-based localization [38]. The real-world robot is equipped with an Intel RealSense L515 RGB-D camera, a Velodyne VLP-16 3D LiDAR, and an Intel NUC 13 with i7 CPU for computation (Fig. S3). For real-world experiments, the navigation algorithm shown in Fig. 2(c) runs on the Intel NUC, while all other algorithms are executed on a server with four RTX-4090 GPUs. The Intel NUC and the server communicate remotely via Wi-Fi.

**中文译文**

在仿真和真实世界实验中，我们均使用 Unitree Go1 四足机器人。在仿真中，我们使用真实位姿数据；在真实世界中，我们使用基于 LiDAR 的定位方法 [38] 估计机器人位姿。真实世界机器人配备 Intel RealSense L515 RGB-D 相机、Velodyne VLP-16 三维 LiDAR，以及搭载 i7 CPU 的 Intel NUC 13 用于计算（图 S3）。在真实世界实验中，图 2(c) 所示的导航算法运行在 Intel NUC 上，而其他所有算法均在配备四块 RTX-4090 GPU 的服务器上执行。Intel NUC 与服务器通过 Wi-Fi 远程通信。

**Original Caption**

Table S2. List of Language Instructions and Outcomes by Scenario.

**中文表题**

表 S2. 不同场景下的语言指令与结果列表。

| Scenario | Language Instructions | LM-Nav | VLMap | E2Map |
|---|---|---:|---:|---:|
| danger sign | Move to the picture. | X | X | X |
| danger sign | Head to the bottom side of the chair. | O | X | O |
| danger sign | First, reach the picture and stop at the bottom side of the microwave. | X | X | O |
| danger sign | Go to the bottom side of the chair and finish your move at the picture. | X | X | O |
| danger sign | Move toward the picture and go straight to the bottom side of the chair. | X | X | O |
| danger sign | Move past to the right side of the chair, then continue to the door. | X | X | O |
| danger sign | First, go straight to the picture, head to the microwave, then finally proceed to the table. | X | X | O |
| danger sign | Go to the bottom side of the chair, then make your way to the picture, and finally stop at the bottom of the microwave. | X | X | O |
| danger sign | Go to the right side of the chair, move to the table, then head to the microwave and finally reach the door. | X | X | O |
| danger sign | Move to the bottom side of the chair, head to the table, go by the door, and finish at the microwave. | X | X | O |
| human-wall | Go straight to the picture. | X | X | X |
| human-wall | Reach the picture. | X | X | O |
| human-wall | Move to the table, and finish at the picture. | X | X | O |
| human-wall | Head between the shelving and refrigerator, and end at the picture. | X | X | O |
| human-wall | Head toward the refrigerator, and finally stop at the picture. | X | X | O |
| human-wall | First, go in front of the microwave, move to the top of the refrigerator, and end your trajectory at the picture. | X | X | O |
| human-wall | Head to the bottom of the shelving, walk to the table, and finish your move in front of the picture. | X | X | O |
| human-wall | Move between the table and microwave, pass to the refrigerator, and head straight to the picture. | X | X | O |
| human-wall | Pass to the rightside of the table, go to the microwave, move between the table and refrigerator, and reach the picture. | X | X | O |
| human-wall | Walk to the bottom side of the shelving, go to the table, then move to the refrigerator, and finish at the picture. | X | X | O |
| dynamic door | Head to the table. | O | X | X |
| dynamic door | Walk to the microwave. | X | X | O |
| dynamic door | Move to the refrigerator, and move to the bottom of chair. | X | X | O |
| dynamic door | Go to the chair, then take a step toward the table. | X | X | O |
| dynamic door | Make your way to the microwave, and stop at the TV monitor. | X | X | O |
| dynamic door | Move to the microwave, pass the picture, and finally stop at the bottom of the chair. | X | X | O |
| dynamic door | Take a step toward the picture, move to the refrigerator, and reach the chair. | X | X | O |
| dynamic door | Walk to the chair, go to the microwave, and stop at the refrigerator. | X | X | O |
| dynamic door | Make your way to the microwave, pass the picture, and arrive between the chair and the refrigerator. | X | X | O |
| dynamic door | Head to the picture, stop at the table, go to the refrigerator, and reach to the rightside of the chair. | X | X | O |

**中文译表**

| 场景 | 语言指令 | LM-Nav | VLMap | E2Map |
|---|---|---:|---:|---:|
| 危险标志 | 移动到图片处。 | X | X | X |
| 危险标志 | 前往椅子下侧。 | O | X | O |
| 危险标志 | 首先到达图片处，然后停在微波炉下侧。 | X | X | O |
| 危险标志 | 前往椅子下侧，并在图片处结束移动。 | X | X | O |
| 危险标志 | 朝图片方向移动，然后径直前往椅子下侧。 | X | X | O |
| 危险标志 | 移动经过椅子右侧，然后继续前往门。 | X | X | O |
| 危险标志 | 首先径直前往图片处，再前往微波炉，最后到达桌子。 | X | X | O |
| 危险标志 | 前往椅子下侧，然后移动到图片处，最后停在微波炉下方。 | X | X | O |
| 危险标志 | 前往椅子右侧，移动到桌子，再前往微波炉，最后到达门。 | X | X | O |
| 危险标志 | 移动到椅子下侧，前往桌子，经过门旁，最后停在微波炉处。 | X | X | O |
| 人-墙 | 径直前往图片处。 | X | X | X |
| 人-墙 | 到达图片处。 | X | X | O |
| 人-墙 | 移动到桌子，并在图片处结束。 | X | X | O |
| 人-墙 | 前往架子和冰箱之间，并在图片处结束。 | X | X | O |
| 人-墙 | 朝冰箱方向前进，最后停在图片处。 | X | X | O |
| 人-墙 | 首先到微波炉前方，移动到冰箱上方，最后在图片处结束轨迹。 | X | X | O |
| 人-墙 | 前往架子下方，走到桌子，并在图片前方结束移动。 | X | X | O |
| 人-墙 | 移动到桌子和微波炉之间，经过冰箱，并径直前往图片处。 | X | X | O |
| 人-墙 | 经过桌子右侧，前往微波炉，移动到桌子和冰箱之间，并到达图片处。 | X | X | O |
| 人-墙 | 走到架子下侧，前往桌子，再移动到冰箱，最后在图片处结束。 | X | X | O |
| 动态门 | 前往桌子。 | O | X | X |
| 动态门 | 走到微波炉。 | X | X | O |
| 动态门 | 移动到冰箱，然后移动到椅子下方。 | X | X | O |
| 动态门 | 前往椅子，然后朝桌子迈进一步。 | X | X | O |
| 动态门 | 前往微波炉，并停在电视显示器处。 | X | X | O |
| 动态门 | 移动到微波炉，经过图片，最后停在椅子下方。 | X | X | O |
| 动态门 | 朝图片迈进一步，移动到冰箱，并到达椅子。 | X | X | O |
| 动态门 | 走到椅子，前往微波炉，并停在冰箱处。 | X | X | O |
| 动态门 | 前往微波炉，经过图片，并到达椅子和冰箱之间。 | X | X | O |
| 动态门 | 前往图片处，在桌子处停下，去往冰箱，并到达椅子右侧。 | X | X | O |

### Full Prompts / 完整提示词

**Original**

We include all the prompts used for our system in Fig. S4--S8.

- **Goal selector**: Fig. S5
- **Event descriptor**: Fig. S6
- **Emotion evaluator**: Fig. S7--S8

For both the *event descriptor* and *emotion evaluator*, we used the same system prompt (Fig. S4) to provide them with a consistent identity.

**中文译文**

我们在图 S4--S8 中给出了系统使用的全部提示词。

- **目标选择器**：图 S5
- **事件描述器**：图 S6
- **情绪评估器**：图 S7--S8

对于*事件描述器*和*情绪评估器*，我们使用相同的系统提示词（图 S4），以赋予它们一致的身份设定。

### Qualitative Results of Event Descriptor and Emotion Evaluator / 事件描述器与情绪评估器的定性结果

**Original**

We provide the qualitative results of the *event descriptor* and *emotion evaluator*, along with corresponding images, for events occurring in each scenario of the experiments in Fig. S9--S17.

- **danger sign**: Fig. S9--S11
- **human-wall**: Fig. S12--S14
- **dynamic door**: Fig. S15--S17

**中文译文**

我们在图 S9--S17 中提供了实验各场景事件对应的*事件描述器*与*情绪评估器*定性结果，并给出相应图像。

- **危险标志**：图 S9--S11
- **人-墙**：图 S12--S14
- **动态门**：图 S15--S17

### Evaluating Positive Emotions / 评估正面情绪

**Original**

Although our experiments did not address events related to positive emotions, our method is not limited to negative emotions and can also handle positive emotions through appropriate prompting. To demonstrate this capability, we prompted the *emotion evaluator* with emotionally positive situations. Fig. S18 shows the prompt used for the *emotion evaluator*, and the same system prompt (Fig. S4) was used to maintain a consistent identity. The qualitative results of the *event descriptor* and *emotion evaluator*, along with the corresponding image, are presented in Fig. S19--S21. We provided the *event descriptor* with an image featuring a sofa, symbolizing a place of relaxation. As shown in Fig. S21, the *emotion evaluator* rated this image as positive, associating it with comfort and relaxation. These results confirm that our method can address both negative and positive emotions through appropriate prompting.

**中文译文**

尽管我们的实验没有处理与正面情绪相关的事件，但本文方法并不限于负面情绪，也可以通过适当提示处理正面情绪。为了展示这一能力，我们使用情绪积极的情境提示*情绪评估器*。图 S18 展示了*情绪评估器*使用的提示词，并使用相同的系统提示词（图 S4）来保持一致身份设定。*事件描述器*和*情绪评估器*的定性结果以及对应图像见图 S19--S21。我们向*事件描述器*提供了一张包含沙发的图像，沙发象征放松场所。如图 S21 所示，*情绪评估器*将该图像评定为正面，并将其与舒适和放松联系起来。这些结果确认，本文方法可以通过适当提示同时处理负面和正面情绪。

![Fig. S4 System prompt](<E2Map Experience-and-Emotion Map for Self-Reflective Robot Navigation with Language Models.assets/system_prompt.png>)

**Original Caption**

Figure S4. System prompt used for both the *event descriptor* and the *emotion evaluator*.

**中文图注**

图 S4. 同时用于*事件描述器*和*情绪评估器*的系统提示词。

![Fig. S5 Goal selector prompt](<E2Map Experience-and-Emotion Map for Self-Reflective Robot Navigation with Language Models.assets/gs_prompt.png>)

**Original Caption**

Figure S5. Prompt for the *goal selector*.

**中文图注**

图 S5. *目标选择器*提示词。

![Fig. S6 Event descriptor prompt](<E2Map Experience-and-Emotion Map for Self-Reflective Robot Navigation with Language Models.assets/ed_prompt.png>)

**Original Caption**

Figure S6. Prompt for the *event descriptor*.

**中文图注**

图 S6. *事件描述器*提示词。

![Fig. S7 Emotion evaluator prompt 1](<E2Map Experience-and-Emotion Map for Self-Reflective Robot Navigation with Language Models.assets/ee_prompt_1.png>)

**Original Caption**

Figure S7. Prompt for the *emotion evaluator* (1/2).

**中文图注**

图 S7. *情绪评估器*提示词（1/2）。

![Fig. S8 Emotion evaluator prompt 2](<E2Map Experience-and-Emotion Map for Self-Reflective Robot Navigation with Language Models.assets/ee_prompt_2.png>)

**Original Caption**

Figure S8. Prompt for the *emotion evaluator* (2/2).

**中文图注**

图 S8. *情绪评估器*提示词（2/2）。

![Fig. S9 Danger sign event before](<E2Map Experience-and-Emotion Map for Self-Reflective Robot Navigation with Language Models.assets/ds_event_0.jpg>)

![Fig. S9 Danger sign event](<E2Map Experience-and-Emotion Map for Self-Reflective Robot Navigation with Language Models.assets/ds_event_1.jpg>)

![Fig. S9 Danger sign event after](<E2Map Experience-and-Emotion Map for Self-Reflective Robot Navigation with Language Models.assets/ds_event_2.jpg>)

**Original Caption**

Figure S9. Event images of the *danger sign* scenario.

**中文图注**

图 S9. *危险标志*场景中的事件图像。

![Fig. S10 Danger sign event descriptor result](<E2Map Experience-and-Emotion Map for Self-Reflective Robot Navigation with Language Models.assets/ds_ed_result.png>)

**Original Caption**

Figure S10. Qualitative results of the *event descriptor* in the *danger sign* scenario.

**中文图注**

图 S10. *危险标志*场景中*事件描述器*的定性结果。

![Fig. S11 Danger sign emotion evaluator result](<E2Map Experience-and-Emotion Map for Self-Reflective Robot Navigation with Language Models.assets/ds_ee_result.png>)

**Original Caption**

Figure S11. Qualitative results of the *emotion evaluator* in the *danger sign* scenario.

**中文图注**

图 S11. *危险标志*场景中*情绪评估器*的定性结果。

![Fig. S12 Human-wall event before](<E2Map Experience-and-Emotion Map for Self-Reflective Robot Navigation with Language Models.assets/hw_event_0.jpg>)

![Fig. S12 Human-wall event](<E2Map Experience-and-Emotion Map for Self-Reflective Robot Navigation with Language Models.assets/hw_event_1.jpg>)

![Fig. S12 Human-wall event after](<E2Map Experience-and-Emotion Map for Self-Reflective Robot Navigation with Language Models.assets/hw_event_2.jpg>)

**Original Caption**

Figure S12. Event images of the *human-wall* scenario.

**中文图注**

图 S12. *人-墙*场景中的事件图像。

![Fig. S13 Human-wall event descriptor result](<E2Map Experience-and-Emotion Map for Self-Reflective Robot Navigation with Language Models.assets/hw_ed_result.png>)

**Original Caption**

Figure S13. Qualitative results of the *event descriptor* in the *human-wall* scenario.

**中文图注**

图 S13. *人-墙*场景中*事件描述器*的定性结果。

![Fig. S14 Human-wall emotion evaluator result](<E2Map Experience-and-Emotion Map for Self-Reflective Robot Navigation with Language Models.assets/hw_ee_result.png>)

**Original Caption**

Figure S14. Qualitative results of the *emotion evaluator* in the *human-wall* scenario.

**中文图注**

图 S14. *人-墙*场景中*情绪评估器*的定性结果。

![Fig. S15 Dynamic door event before](<E2Map Experience-and-Emotion Map for Self-Reflective Robot Navigation with Language Models.assets/dd_event_0.jpg>)

![Fig. S15 Dynamic door event](<E2Map Experience-and-Emotion Map for Self-Reflective Robot Navigation with Language Models.assets/dd_event_1.jpg>)

![Fig. S15 Dynamic door event after](<E2Map Experience-and-Emotion Map for Self-Reflective Robot Navigation with Language Models.assets/dd_event_2.jpg>)

**Original Caption**

Figure S15. Event images of the *dynamic door* scenario.

**中文图注**

图 S15. *动态门*场景中的事件图像。

![Fig. S16 Dynamic door event descriptor result](<E2Map Experience-and-Emotion Map for Self-Reflective Robot Navigation with Language Models.assets/dd_ed_result.png>)

**Original Caption**

Figure S16. Qualitative results of the *event descriptor* in the *dynamic door* scenario.

**中文图注**

图 S16. *动态门*场景中*事件描述器*的定性结果。

![Fig. S17 Dynamic door emotion evaluator result](<E2Map Experience-and-Emotion Map for Self-Reflective Robot Navigation with Language Models.assets/dd_ee_result.png>)

**Original Caption**

Figure S17. Qualitative results of the *emotion evaluator* in the *dynamic door* scenario.

**中文图注**

图 S17. *动态门*场景中*情绪评估器*的定性结果。

![Fig. S18 Positive emotion evaluator prompt](<E2Map Experience-and-Emotion Map for Self-Reflective Robot Navigation with Language Models.assets/pos_ee_prompt.png>)

**Original Caption**

Figure S18. Prompt for the *emotion evaluator* to assess positive emotions.

**中文图注**

图 S18. 用于评估正面情绪的*情绪评估器*提示词。

![Fig. S19 Positive event image](<E2Map Experience-and-Emotion Map for Self-Reflective Robot Navigation with Language Models.assets/pos_event.jpg>)

**Original Caption**

Figure S19. Image provided to the *event descriptor* for evaluating positive emotion.

**中文图注**

图 S19. 提供给*事件描述器*以评估正面情绪的图像。

![Fig. S20 Positive event descriptor result](<E2Map Experience-and-Emotion Map for Self-Reflective Robot Navigation with Language Models.assets/pos_ed_result.png>)

**Original Caption**

Figure S20. Qualitative results of the *event descriptor* in the positive scenario.

**中文图注**

图 S20. 正面场景中*事件描述器*的定性结果。

![Fig. S21 Positive emotion evaluator result](<E2Map Experience-and-Emotion Map for Self-Reflective Robot Navigation with Language Models.assets/pos_ee_result.png>)

**Original Caption**

Figure S21. Qualitative results of the *emotion evaluator* in the positive scenario.

**中文图注**

图 S21. 正面场景中*情绪评估器*的定性结果。

