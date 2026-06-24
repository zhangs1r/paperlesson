# paperlesson-replicate

一键复刻 PaperLesson 论文/教材精读网站项目，保留你的专属风格和领域。

## 工作流

按以下顺序依次执行每个阶段，不要跳步。

---

## 阶段 1：收集用户信息

先通过 ask 工具收集用户以下信息，不要跳步：

### 1.1 专业领域
问用户：你的专业/研究方向是什么？（例如：计算机视觉 / NLP / 机器人 / 生物信息学 / 量子物理 / 经济学 等）

### 1.2 风格微调
说明：我将以 PaperLesson 原版「学术出版风」为基础为你生成，你可以微调以下内容：

预设基础（不可改，这是 skill 的核心风格）：
- 背景：暖米纸色 `#F7F4EE`
- 点缀色：赤陶橙 `#CC785C`
- 字体：标题 Noto Serif SC，正文 Inter，代码 JetBrains Mono
- 三层结构：分馆（group）→ 来源块（collection）→ 课程页（lesson）

可微调项（用 ask 问用户）：
- **点缀色**：是否想换一个颜色？提供选项：保留赤陶橙 / 换成蓝色系（#4A90D9）/ 换成绿色系（#5A9E6F）/ 自定义
- **领域示例**：提示词中的默认示例（如 E2Map 论文）要不要换成你领域的典型内容？
- **项目名称**：网站标题用什么？默认 "PaperLesson"，可以改
- **GitHub 用户名**：你的 GitHub 用户名是什么？
- **仓库名**：你打算创建的 GitHub 仓库名叫什么？默认 "paperlesson"

### 1.3 输出目录
确认文件输出到哪个目录。默认使用当前工作目录。

---

## 阶段 2：检查 teach skill 依赖

1. 用 `memory` 工具（operation: list）检查全局是否已有 `teach` skill。
2. 更直接的方式：尝试查找 `.reasonix/skills/` 下的 `teach` 相关文件，或在全局注册中搜索。
3. **如果找不到 teach skill**：
   - 告知用户："正在为你全局安装 teach skill，之后你可以用 /teach 命令让 AI 生成课程。"
   - 创建一个名为 `teach` 的全局 skill，内容在**阶段 4** 给出（将改写后的 `/teach` 提示词注册为 skill 本体）。
   - 使用 `install_skill` 工具的 scope=global 来安装。
4. **如果已有 teach skill**：
   - 告知用户："检测到已安装 teach skill，跳过安装。"
   - 但**新生成的改写版提示词仍会以文本形式输出给用户**，方便他们手动更新。

> teach skill 的内容不是本阶段生成的——它的内容来自阶段 4 改写后的第一段提示词。所以本阶段只做检测和占位说明，实际安装发生在阶段 4 改写完成后。

---

## 阶段 3：生成项目脚手架

在当前工作目录（或用户指定的目录）下，生成完整的 PaperLesson 项目文件。

### 3.1 创建目录结构

```
.
├── index.html
├── shared/
│   └── theme.css
├── data/
│   └── course-catalog.js
├── lessons/
│   └── assets/
│       ├── course.css
│       └── course.js
├── MISSION.md
├── README.md
├── learning-records/
│   └── 0001-template.md
└── .gitignore
```

### 3.2 生成 shared/theme.css

基于 PaperLesson 原版 theme.css 生成，但应用用户选择的微调：

- 如果用户改了点缀色 → 替换 `--accent` 及 `--accent-light` / `--accent-deep` / `--accent-dim`
- 如果用户改了字体 → 替换 Google Fonts 的 @import URL 和对应变量
- 保留完整的 CSS 变量系统、间距系统、圆角系统、阴影系统
- 保留所有 utility class、卡片样式、按钮样式、表格、导航栏、页脚

原版 css 的参考内容如下（从中提取骨架，不要完全照搬——要根据用户的微调来修改）：

```css
/* 字体导入 */
@import url('https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@400;600;700;900&family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

:root {
  /* 色板 */
  --paper: #F7F4EE;
  --paper-light: #FBFAF7;
  --ink: #1A1A2E;
  --ink-80: #3A3A4A;
  --ink-60: #5A5A6A;
  --ink-40: #8A8A9A;
  --ink-20: #BABAC6;
  --accent: #CC785C;
  --accent-light: #E8C4B0;
  --accent-deep: #A85D42;
  --accent-dim: rgba(204, 120, 92, 0.12);
  --border: #E8E4DC;
  --border-light: #F0ECE4;
  --success: #5A9E6F;
  --code-bg: #F0EDE6;

  /* 字体栈 */
  --font-serif: 'Noto Serif SC', 'Newsreader', Georgia, 'Times New Roman', serif;
  --font-sans: 'Inter', -apple-system, 'PingFang SC', 'Microsoft YaHei', sans-serif;
  --font-mono: 'JetBrains Mono', 'SF Mono', 'Fira Code', monospace;

  /* 字号、间距、圆角、阴影系统 */
  /* ... 完整系统见下方说明 */
}
```

> 完整的字号/间距/圆角/阴影系统参考原项目 `shared/theme.css`，你需要在生成时复现完整的变量体系和样式类。所有选择器名称和结构保持与 PaperLesson 一致。

### 3.3 生成 index.html

基于原版 index.html 生成，但：
- 标题使用用户指定的项目名（替换 "PaperLesson"）
- Hero 区域使用用户领域相关的描述
- 导航栏 logo 使用用户项目名
- 保持完整的三层结构（分馆 → 来源块 → 课程页）
- 保持完整的 JavaScript 数据驱动渲染逻辑（`getData`、`buildStats`、`renderCatalog`、`renderCards` 等）
- 页脚使用用户项目名

### 3.4 生成 data/course-catalog.js

生成完整骨架，包含：
- `featuredCollectionId` 留空字符串
- 两个默认分馆（group）："论文馆" 和 "教材馆"
- 空的 `collections` 数组
- 空的 `lessons` 数组
- 空的 `references` / `learningRecords` / `siteLinks` 数组
- 添加注释说明每个字段的用途

结构示例：
```js
window.PAPERLESSON_DATA = {
  featuredCollectionId: "",
  groups: [
    {
      id: "papers",
      kind: "论文馆",
      title: "论文精读课程馆",
      emoji: "📄",
      description: "适合一篇论文拆成多节课，或者几篇相关论文并列管理。",
      meta: ["适合单篇或小系列论文", "先搭来源块，再拆课程"]
    },
    {
      id: "books",
      kind: "教材馆",
      title: "教材与长期主线课程馆",
      emoji: "📘",
      description: "适合整本书、长周期课程或系统化主题主线。",
      meta: ["适合整本书 / 系统主线", "适合长期扩写与补课"]
    }
  ],
  collections: [],
  lessons: [],
  references: [],
  learningRecords: [],
  siteLinks: []
};
```

### 3.5 生成 lessons/assets/course.css 和 course.js

参考原项目 `lessons/assets/slam-course.css` 和 `slam-course.js`，生成课程页面配套的单页样式和 JS。

**course.css**：课程页面的专用样式，包含：
- 学术出版风配色（与全局 theme.css 一致）
- 课程专属排版（lesson-header、h2 带左边框、qa-block、quiz、comparison-table 等）
- 响应式设计
- 使用 CSS 变量引用 theme.css 的色板

**course.js**：课程页面的交互功能，包含：
- 折叠练习的展开/收起状态管理
- 交互功能块的初始化
- 页面加载完成后触发

### 3.6 生成示例课程 HTML

在 `lessons/` 下创建 `0001-示例课程.html`，作为用户参考模板。内容包含：

- 引用 `../shared/theme.css` 和 `assets/course.css`
- MathJax v3 CDN
- 完整的课程结构：标题 → 正文（含 LaTeX 公式）→ 课后练习（`<details>/<summary>` 折叠）
- 顶部「返回课程馆」链接
- 底部导航
- 注释标注每个区块的用途（方便用户理解结构）

### 3.7 生成 MISSION.md

简洁的项目使命文档，包含：
- 项目目标
- 学习者背景模板
- 课程规划模板

### 3.8 生成 README.md

完整的项目文档，包含：
- 项目简介
- 文件结构
- 快速开始（本地预览 + GitHub Pages 部署）
- 如何添加新课程（两种场景：续课 / 全新来源块）

### 3.9 生成 .gitignore

标准 Node.js / 编辑器 gitignore：
```
node_modules/
.DS_Store
Thumbs.db
*.log
```

### 3.10 生成 learning-records/0001-template.md

学习记录模板，包含日期、主题、核心收获、疑问等占位字段。

---

## 阶段 4：改写两段提示词

基于用户在阶段 1 提供的领域信息，将原版两段提示词改写为用户专属版本。

### 4.1 改写 /teach 提示词

原版提示词中有以下需要替换的内容：
- 第 2 条中的默认风格描述（根据用户微调更新配色值）
- 第 7 条中的命名示例（如果用户改了领域）
- 第 9 条中的 course-catalog.js 字段 —— 保留原结构
- 所有示例引用（原版示例论文 E2Map → 替换为用户领域相关的示例，如用户是 CV 方向可换成 ViT/ResNet 等）

改写后的提示词格式：

```markdown
/teach "这里填论文、书本、markdown、pdf 或资料目录路径"

请你带着我完整精读这篇论文或这本书的内容...
...
[保留原版 11 条规则的完整结构，仅替换领域特定内容]
...
```

将改写后的完整提示词输出为一个代码块，方便用户复制。

### 4.2 改写追问插课提示词

同样基于用户领域改写，结构不变，仅替换示例内容。

改写后的格式：

```markdown
/teach 我读完了 【课程文件名】，这门课属于 【collection id】，有几个疑问：

[用户填入自己的问题]

请基于以上问题生成若干节新的答疑课程...
...
[保留原版 10 条规则的完整结构，仅替换领域特定内容]
...
```

### 4.3 注册 teach skill（如果尚未安装）

如果阶段 2 检测到 teach skill 不存在，现在用 `install_skill` 工具注册它：

- name: `teach`
- scope: `global`
- runAs: `inline`（或 `subagent`，取决于你判断哪种更适合 —— teach 命令需要生成文件，推荐 inline）
- description: `使用 `/teach` 命令让 AI 从论文/教材生成多节 HTML 精读课程，支持课后追问插课和 course-catalog 自动更新。安装自 paperlesson-replicate。`
- body: **使用阶段 4.1 改写后的完整 `/teach` 提示词作为 body**

告诉用户：teach skill 已安装到全局，以后你在任意项目中都可以用 `/teach "论文路径"` 来生成课程。

### 4.4 提示用户手动保存追问提示词

告知用户：追问插课提示词由于需要手动填入问题，不适合注册为 skill，建议你保存到项目根目录的 `qa-prompt.md` 文件中，每次追问时复制使用。

---

## 阶段 5：输出部署指南

5.1 告诉用户所有文件已生成在哪个目录。
5.2 告诉用户如何本地预览：

```bash
cd 你的项目目录
python -m http.server 8000
# 浏览器访问 http://localhost:8000
```

5.3 教用户如何上传 GitHub：

```bash
# 1. 在 https://github.com/new 创建新仓库（Public）
# 2. 在项目目录下运行：
git init
git add .
git commit -m "🎉 init: paperlesson replica"
git branch -M main
git remote add origin https://github.com/你的用户名/你的仓库名.git
git push -u origin main
```

5.4 教用户如何开启 GitHub Pages：
- 进入 GitHub 仓库 → Settings → Pages
- Branch 选 `main`，文件夹选 `/ (root)`，点 Save
- 等待 1-2 分钟，访问 `https://你的用户名.github.io/你的仓库名/`

5.5 教用户后续如何用：
- 添加新课程：`/teach "论文或书本路径"`
- 追问插课：复制 qa-prompt.md 的内容，填入问题和课程名
- 所有文件改完后：`git add . && git commit -m "xxx" && git push` 自动部署

---

## 重要原则

1. **不要跳步**：严格按照阶段 1 → 2 → 3 → 4 → 5 的顺序执行
2. **询问用户**：阶段 1 必须用 ask 工具交互式收集，不要自己假设
3. **保持结构**：生成的文件结构必须与 PaperLesson 原版一致（三层目录、数据驱动、CSS 变量体系）
4. **领域适配**：改写提示词时，示例和默认值要换成用户领域的内容，但规则结构不变
5. **完整输出**：阶段 4 改写后的提示词必须以可复制的代码块形式输出
6. **teach skill 内容**：teach skill 的 body 就是阶段 4.1 改写后的 `/teach` 提示词全文
