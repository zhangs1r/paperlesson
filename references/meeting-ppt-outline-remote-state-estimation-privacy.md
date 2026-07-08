# 组会PPT大纲：Remote State Estimation with Privacy Against Active Eavesdroppers

**汇报人：** [留空]
**指导教师：** 倪雨青
**日期：** [留空]

---

## Page 1 - 封面

**Key Content:**
**Remote State Estimation with Privacy Against Active Eavesdroppers**

Matthew J. Crimson, Justin M. Kennedy, Daniel E. Quevedo

School of Electrical Engineering and Robotics, Queensland University of Technology, Brisbane, Australia

Published in *Automatica*, 2024

**Comments/Notes:**
封面页。论文发表于 Automatica 2024，研究主动窃听者场景下的远程状态估计隐私保护问题。

---

## Page 2 - Outline

**Key Content:**
1. Background & Motivation
2. Problem Setup & System Model
3. Encoding Scheme Design
4. Remote State Estimation
5. Expected Performance Analysis
6. Encoding Design Variable
7. Eavesdropper Detection (QCD)
8. Simulations & Results
9. Conclusion

**Comments/Notes:**
报告分为9个部分，从研究背景到实验验证逐步展开。

---

## Page 3 - Motivation（研究动机）

**Key Content:**
- Cyber-Physical Systems (CPSs) are vulnerable to eavesdropping attacks that compromise state confidentiality
- Traditional cryptography has limitations: assumes limited computation power, introduces communication overhead and delays
- Existing encoding schemes rely on **acknowledgments** (Tsiamis et al., 2018, 2020), which are vulnerable to **active eavesdroppers** that can block ACKs while eavesdropping
- Active eavesdropping: combines eavesdropping + jamming to prevent critical events, improving its own estimation performance
- **Key gap:** Need an encoding scheme that does **not** rely on acknowledgments after eavesdropper detection

**Figure:** [Fig. 1: System architecture]

**Comments/Notes:**
这篇论文的核心动机是：现有的隐私编码方案依赖ACK确认包，但主动窃听者可以同时窃听和干扰ACK。比如Stuxnet病毒就是先监听正常状态再发动攻击。所以需要一种不依赖ACK的编码方案。

---

## Page 4 - Related Work（相关工作）

**Key Content:**
- **Tsiamis et al. (2017, 2018, 2020):** State-secrecy codes using linear time-varying transformations; eavesdropper's error covariance grows to open-loop prediction under critical events. **Limitation:** relies on acknowledgments
- **Ding et al. (2021):** Remote estimation with active eavesdropper; threshold-based detection using packet dropout ratio. **Inspiration:** activate encoding scheme upon detection
- **Crimson et al. (2023, IFAC):** Previous work on scalar first-order systems with pseudo-random noise transmission
- **This paper extends** Crimson et al. (2023) from scalar to **vector case**, and adds **eavesdropper detection** via Quickest Change Detection (QCD)

**Comments/Notes:**
相关工作的三个关键脉络：Tsiamis的state-secrecy codes（依赖ACK有漏洞）、Ding的主动窃听检测（启发式阈值）、作者自己的IFAC 2023工作（标量→向量推广）。本文的新贡献是检测+编码的联合设计。

---

## Page 5 - Contribution（本文贡献）

**Key Content:**
1. **Extend** encoding scheme from scalar first-order systems to the **vector case**, with eavesdropper detection
2. **Derive expressions** for expected steady-state estimation error covariance for both eavesdropper and legitimate user (as functions of system dynamics, channel quality, encoding parameter)
3. **Propose offline encoding design** to balance confidentiality vs. estimation performance degradation; drive eavesdropper's trace **above open-loop prediction**
4. **QCD-based detection** to activate encoding scheme only when eavesdropper is present, minimizing performance impact

**Comments/Notes:**
三个核心贡献：从标量推广到向量系统、推导了稳态期望协方差的解析表达式、设计了QCD检测+噪声注入的联合方案。关键创新点：窃听者的估计误差可以大于开环预测——这意味着窃听者收到数据还不如不用数据。

---

## Page 6 - Problem Setup

**Key Content:**
- **System model:** Linear discrete-time invariant, $x_{k+1} = A x_k + w_k,\ y_k = C x_k + v_k$
- **Stable dynamics:** $\rho(A) < 1$
- **Sensor:** Runs local Kalman filter, transmits encoded packet $z_k$
- **Legitimate user:** Receives via unreliable channel with dropout probability
- **Active eavesdropper:** Intercepts transmissions AND jams legitimate user's channel

**Channel qualities:**
- Nominal (no attack): $\gamma = \mathbb{P}[\lambda_k = 0],\ k < \Lambda$
- Under attack: $\bar{\gamma} = \mathbb{P}[\lambda_k = 0],\ k \geq \Lambda$, with $\gamma < \bar{\gamma}$
- Eavesdropper's channel: $\gamma^e = \mathbb{P}[\lambda_k^e = 0],\ k \geq \Lambda$

**Figure:** [Fig. 1: Architecture]

**Comments/Notes:**
系统建模是标准的远程估计框架。传感器本地跑卡尔曼滤波，然后把估计值传给远程用户。信道用伯努利丢包模型。窃听者同时具备窃听和干扰能力——它能听到传感器发的包，同时干扰传感器到合法用户的信道。

---

## Page 7 - Encoding Scheme Design

**Key Content:**
- **Detection variable** $\nu_k \in \{0,1\}$: 0 = eavesdropper detected (formed at legitimate user, shared via feedback)
- **Pseudo-random indicator** $u_k \in \{0,1\}$: pre-arranged between sensor and legitimate user
- **Transmitted packet:**
  
  $$z_k = \begin{cases} \hat{x}_k^s, & \text{if } \nu_k = 1 \text{ or } (\nu_k, u_k) = (0, 1) \\ n_k, & \text{if } (\nu_k, u_k) = (0, 0) \end{cases}$$
  
- **Noise design:** $n_k \sim \mathcal{N}(0, \bar{P})$, same marginal distribution as $\hat{x}_k^s$ — eavesdropper cannot distinguish
- **Design variable:** $\mu \triangleq \mathbb{P}(u_k = 0)$, probability of sending noise

**Algorithm 1:** Encoding at the Sensor

**Comments/Notes:**
核心编码方案：用一个伪随机伯努利指示器决定发真实估计值还是噪声。关键在于这个序列是传感器和合法用户事先约定好的，窃听者不知道。噪声设计成和真实估计值同分布，所以窃听者无法区分。$\mu$ 是核心设计参数，控制发送噪声的概率。

---

## Page 8 - Remote State Estimation: Legitimate User

**Key Content:**
- Legitimate user knows $u_k$ and $\nu_k$, so it can use optimal MMSE estimation
- **State estimate:**
  
  $$\hat{x}_k = \begin{cases} \hat{x}_k^s, & \text{if } (\lambda_k, u_k) = (1, 1) \\ A\hat{x}_{k-1}, & \text{if } \lambda_k = 0 \text{ or } (\lambda_k, u_k) = (1, 0) \end{cases}$$
  
- **Error covariance:**
  
  $$P_k = \begin{cases} \bar{P}, & \text{if } (\lambda_k, u_k) = (1, 1) \\ AP_{k-1}A^\top + Q, & \text{if } \lambda_k = 0 \text{ or } (\lambda_k, u_k) = (1, 0) \end{cases}$$

**Comments/Notes:**
合法用户知道什么时候会发噪声，所以能做出最优估计。当收到噪声包或丢包时，用开环预测。收到真实估计值时，直接同步到传感器的估计值。

---

## Page 9 - Remote State Estimation: Eavesdropper

**Key Content:**
- Eavesdropper is **unaware** of the encoding scheme — believes every packet is the state estimate
- **Sub-optimal estimate:**
  
  $$\hat{x}_k^e = \begin{cases} \hat{x}_k^s, & \text{if } (\lambda_k^e, u_k) = (1, 1) \\ n_k, & \text{if } (\lambda_k^e, u_k) = (1, 0) \\ A\hat{x}_{k-1}^e, & \text{if } \lambda_k^e = 0 \end{cases}$$
  
- **Error covariance (Lemma 1):**
  
  $$P_k^e = \begin{cases} \bar{P}, & \text{if } (\lambda_k^e, u_k) = (1, 1) \\ P_n = P^{OP} + \bar{P}, & \text{if } (\lambda_k^e, u_k) = (1, 0) \\ AP_{k-1}^e A^\top + Q, & \text{if } \lambda_k^e = 0 \end{cases}$$

- **Key insight:** $P_n > P^{OP}$ — receiving noise makes eavesdropper **worse than open-loop prediction**

**Comments/Notes:**
窃听者不知道编码方案，所以当它收到噪声包时，会真的把它当成状态估计值用进去，导致估计误差协方差大于开环预测。这是整个方案的精髓：用噪声主动损害窃听者的估计性能。

---

## Page 10 - Expected Performance Analysis

**Key Content:**
- **Why expectation?** Sensor doesn't know channel outcomes (no ACKs), so compute **expected** steady-state error covariance
- **Legitimate user Markov chain (Fig. 2):** States = dropout count, transition: returns to 0 with prob $(1-\bar{\gamma})(1-\mu)$
- **Lemma 2:** Steady-state expectation of legitimate user's error covariance:
  
  $$\lim_{k\to\infty} \mathbb{E}[P_k] = (1-\bar{\gamma})(1-\mu)W + (\bar{\gamma}+(1-\bar{\gamma})\mu)S$$
  
- **Eavesdropper Markov chain (Fig. 3):** Two absorbing states (estimate received / noise received), each followed by dropouts
- **Lemma 3:** Steady-state expectation of eavesdropper's error covariance:
  
  $$\lim_{k\to\infty} \mathbb{E}[P_k^e] = (1-\gamma^e)(1-\mu)W^e + \gamma^e S^e + (1-\gamma^e)\mu H^e$$

**Figure:** [Fig. 2: Markov chain for legitimate user] [Fig. 3: Markov chain for eavesdropper]

**Comments/Notes:**
因为传感器不能发ACK，所以用期望来刻画长期性能。两个马尔可夫链模型分别描述合法用户和窃听者的估计误差协方差演化。关键结果是给出了稳态协方差的解析表达式，依赖于系统参数 $A,Q$、信道质量 $\bar{\gamma},\gamma^e$ 和设计参数 $\mu$。

---

## Page 11 - Encoding Design Variable

**Key Content:**
- **Performance metrics:**
  - $J(\mu) = \text{trace}\lim_{k\to\infty}\mathbb{E}[P_k]$ (legitimate user)
  - $J^e(\mu) = \text{trace}\lim_{k\to\infty}\mathbb{E}[P_k^e]$ (eavesdropper)
- **Lemma 4 (Monotonicity):** $J^e(\mu)$ is monotonically increasing in $\mu$ — more noise = worse eavesdropper
- **Lemma 5 (Upper bound):** $J(\mu) < \text{trace } P^{OP}$ for $\mu < 1$ — legitimate user always better than open-loop
- **Theorem 6:** Choose $\mu$ in range $\mu^{OP} < \mu < 1$ where
  
  $$\mu^{OP} = \frac{\gamma^e(\text{tr}S^e - \text{tr}W^e) + \text{tr}W^e - \text{tr}P^{OP}}{(\gamma^e - 1)(\text{tr}H^e - \text{tr}W^e)}$$
  
  Ensures: $J(\mu) < \text{tr}P^{OP} < J^e(\mu)$

**Comments/Notes:**
核心设计定理。$\mu$ 需要选在 $\mu^{OP}$ 和 1 之间，使得合法用户的误差协方差有上界（小于开环预测），而窃听者的误差协方差大于开环预测。窃听者收到数据比不用数据还差——这才是真正的保密性。

---

## Page 12 - Eavesdropper Detection (QCD)

**Key Content:**
- **Detection principle:** Active eavesdropper degrades legitimate user's channel quality ($\gamma \to \bar{\gamma}$), causing statistical change in $\lambda_k$
- **QCD formulation:** Shiryaev's optimal stopping with geometric prior
  - No-change posterior: $\mathbb{P}_\epsilon(k < \Lambda | \mathcal{F}_k)$
  - Stopping rule: $\tau^\star = \inf\{k \geq 1: \mathbb{P}_\epsilon(k < \Lambda | \mathcal{F}_k) \leq h\}$
- **Efficient recursion (scalar):**
  
  $$\hat{M}_k^1 = N_k(1-\kappa)b^1(\lambda_k)\hat{M}_{k-1}^1$$
  
- Detection variable $\nu_k = 0$ when $\tau^\star$ declared → activates encoding

**Comments/Notes:**
用 Quickest Change Detection (QCD) 来检测窃听者。原理是窃听者干扰合法用户信道时，丢包率会从 $\gamma$ 变化到 $\bar{\gamma}$。QCD 用 Shiryaev 最优停时理论，递归计算"没有变化"的后验概率。当这个概率低于阈值 $h$ 时，宣告检测到窃听者。

---

## Page 13 - Experiment Setup

**Key Content:**
- **System:** Second-order linear dynamics
  
  $$A = \begin{bmatrix} 0.5 & 0.1 \\ 0.4 & 0.6 \end{bmatrix},\ C = I_2,\ Q = R = 10^{-2}I_2$$
  
  $\rho(A) = 0.7562 < 1$ (stable)
  
- **Key values:** $\text{tr}\bar{P} = 0.0114$, $\text{tr}P_n = 0.0502$, $\text{tr}P^{OP} = 0.0388$
- **Channel setups:** Four cases comparing different $\gamma^e$ vs $\bar{\gamma}$ conditions
- **QCD parameters:** $\kappa = 5\times 10^{-6}$, $h = 3\times 10^{-3}$ (zero false alarm), detection at $k = 779$ (delay = 79 steps)

**Comments/Notes:**
实验用了二阶稳定系统，谱半径0.7562。设置了四种信道质量对比。QCD检测在窃听者入侵后79步内检测到（入侵在k=700，检测在k=779）。

---

## Page 14 - Main Results: Relative Performance

**Key Content:**
- **Fig. 4:** Relative performance $(J^e(\mu) - J(\mu))/J(\mu)$ for four channel scenarios
  - Worse eavesdropper channel ($\gamma^e > \bar{\gamma}$): $J^e > J$ for all $\mu \geq 0$
  - Equal channels ($\gamma^e = \bar{\gamma}$): $J^e > J$ for $\mu > 0$
  - Better eavesdropper channel ($\gamma^e < \bar{\gamma}$): needs $\mu > 0.14$ for advantage
  - Extreme case ($\bar{\gamma}=1, \gamma^e=0$): $\mu > 0.705$ still gives advantage

**Figure:** [Fig. 4: Comparison of absolute difference]

**Comments/Notes:**
图4展示了四种场景下窃听者和合法用户的性能差距。即使窃听者信道比合法用户好（$\gamma^e=0.3$ vs $\bar{\gamma}=0.5$），只要 $\mu > 0.14$，合法用户仍然更优。极端情况（合法用户收不到任何包，窃听者能收到所有包），只要 $\mu > 0.705$ 仍然有效。

---

## Page 15 - Main Results: QCD Detection

**Key Content:**
- **Fig. 5:** Moving average test — naive threshold detection is unreliable (false alarm at $k=668$)
- **Fig. 6:** QCD no-change posterior — drops sharply after intrusion at $k=700$, detection at $k=779$
- **Fig. 7:** Trace comparison with QCD — before detection, legitimate user's performance degrades; after detection ($k=779$), encoding activates and eavesdropper's trace spikes above $P^{OP}$

**Figure:** [Fig. 5: Moving average test] [Fig. 6: QCD test] [Fig. 7: Trace comparison]

**Comments/Notes:**
移动平均法会触发误报（k=668就误报窃听），而QCD方法准确在k=779检测到。检测后编码方案激活，窃听者的误差协方差迅速飙升到开环预测之上。

---

## Page 16 - Comparison with Tsiamis et al. (2018)

**Key Content:**
- **Tsiamis et al.:** Encode packet as $z_k = \hat{x}_k^s - L^{k-t_k}\hat{x}_{t_k}^s$; eavesdropper converges to $P^{OP}$ under critical event
- **This work:** Eavesdropper's error covariance **exceeds** $P^{OP}$ — packets actively harm the eavesdropper
- **Trade-off:** Better confidentiality at moderate performance loss for legitimate user

**Figure:** [Fig. 8: Comparison of traces]

**Comments/Notes:**
与Tsiamis等人的方法对比：Tsiamis的方法在窃听者漏包后收敛到开环预测（误差协方差等于 $P^{OP}$），而本文的方法可以超过开环预测。代价是合法用户会有适度的性能损失。

---

## Page 17 - Conclusion

**Key Content:**
- **Proposed:** Encoding scheme activated on detection of active eavesdropper
- **Method:** Transmit noise or state estimate based on pseudo-random indicator; QCD for detection
- **Results:** Eavesdropper's expected steady-state error covariance > open-loop prediction; legitimate user's < open-loop prediction
- **No ACKs needed** after detection
- **Open problem:** Online sequential design of when to transmit noise

**Comments/Notes:**
总结：提出了一种不依赖ACK的主动窃听防御方案，核心是QCD检测+随机噪声注入。可以确保窃听者的估计性能比不用数据还差。

---

## Page 18 - Q&A

**Key Content:**
**Thank you! 欢迎提问**

**Comments/Notes:**
问答环节。

---

*注：大纲中标注的图片来自论文原文，后续在PPT中从图片目录 `/tmp/paper-md/` 选取对应图片插入。*
