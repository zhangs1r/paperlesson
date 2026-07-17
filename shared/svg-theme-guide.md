# 🎨 Project SVG Icon Theme Guide

> 统一 SVG 图标设计规范 & 动画风格指南
> 适用于 PaperLesson / SpeakScope / AIHOT Topics / LessonWorkspace

---

## 1. 设计系统 (Design Tokens)

所有项目共享同一套设计语言，定义在 `shared/theme.css` 中：

| Token | 值 | 用途 |
|-------|------|------|
| `--paper` | `#F7F4EE` | 页面背景色 |
| `--paper-light` | `#FBFAF7` | 卡片/模块背景 |
| `--ink` | `#1A1A2E` | 主要文字颜色 |
| `--ink-60` | `#5A5A6A` | 次要文字 |
| `--ink-40` | `#8A8A9A` | 辅助信息 |
| `--accent` | `#CC785C` | **主色 — 陶土橙**（图标默认颜色） |
| `--accent-light` | `#E8C4B0` | 浅色点缀 |
| `--accent-deep` | `#A85D42` | 深色强调 |
| `--accent-dim` | `rgba(204,120,92,0.12)` | 图标背景衬底 |
| `--border` | `#E8E4DC` | 边框线 |
| `--success` | `#5A9E6F` | 成功/对勾状态 |

### 项目专属强调色

| 项目 | 副色 | 用途 |
|------|------|------|
| PaperLesson | `--accent` 陶土橙 | 学术、论文精读 |
| SpeakScope | `--accent` + `--success` 绿 | 口语、发音、练习 |
| AIHOT Topics | `--accent` + `--gold #D4A853` | 热点、资讯、策展 |
| LessonWorkspace | `--accent` | 导航 Hub |

---

## 2. SVG 图标规范

### 2.1 画布

- `viewBox="0 0 24 24"`
- 图标内容占 20×20 范围，留 2px 安全边距
- 输出尺寸：导出为 48×48（用于显示），源文件为 24×24 逻辑坐标系

### 2.2 描边风格（默认）

```yaml
描边宽度: 2px
描边颜色: #CC785C (--accent)
描边端点: round (stroke-linecap: round)
描边连接: round (stroke-linejoin: round)
填充: none（空心图标）
```

### 2.3 填充风格（用于强调/状态）

```yaml
填充颜色: #CC785C (--accent)
描边: none
用途: 实心圆点、对勾中心、奖杯等需要强调的元素
```

### 2.4 路径设计原则

- 尽量用最少的路径节点
- 曲线用贝塞尔（C/c），避免大量折线
- 闭合路径需首尾相连（Z/z）
- 可读性：路径命令大写（绝对坐标）优先

### 2.5 图标分类

| 类型 | 说明 | 动画方式 |
|------|------|---------|
| 描边图标 | 空心线稿 | `stroke-dashoffset` 绘制动画 |
| 填充图标 | 实心色块 | `opacity + scale` 弹出动画 |
| 混合图标 | 描边+填充 | 描边先画，填充后弹出 |

---

## 3. 动画风格指南

### 3.1 总体原则

- **慢速优先**：路径绘制速度控制在 0.8–2.5s/条（视路径长度）
- **调皮可爱**：收尾加入弹跳/晃动/缩放 overshoot
- **自然错开**：多路径图标按 0.15s 间隔先后出现
- **循环 vs 一次**：装饰性图标可循环，功能性图标建议一次播放

### 3.2 动画类型

#### 类型 A：路径绘制 (stroke-draw)

```
适用: 所有描边图标（空心线稿）
技术: stroke-dasharray + stroke-dashoffset → 0
时长: 按路径长度比例，base 0.8s + 额外 0.01s/单位长度
延迟: 多路径时，每条延迟 0.15s
节奏: cubic-bezier(0.42, 0, 0.58, 1) 或 ease-in-out
```

```css
@keyframes drawStroke {
  0%   { stroke-dashoffset: <总长度>; }
  100% { stroke-dashoffset: 0; }
}
```

#### 类型 B：填充弹出 (fill-pop)

```
适用: 实心元素（圆点、色块、填充区域）
技术: opacity 0→1 + scale 0→1.2→1
时长: 0.4–0.6s
节奏: cubic-bezier(0.34, 1.56, 0.64, 1) — 弹性回弹
```

```css
@keyframes fillPop {
  0%   { opacity: 0; transform: scale(0); }
  60%  { opacity: 1; transform: scale(1.2); }
  100% { opacity: 1; transform: scale(1); }
}
```

#### 类型 C：整体回弹 (playful-bounce)

```
适用: 所有图标收尾
技术: scale + rotate 组合
时长: 0.6–0.8s
延迟: 在所有路径绘制完成后 +0.2s
节奏: cubic-bezier(0.34, 1.56, 0.64, 1)
```

```css
@keyframes playfulBounce {
  0%   { transform: scale(1) rotate(0deg); }
  30%  { transform: scale(1.18) rotate(3deg); }
  55%  { transform: scale(0.92) rotate(-2deg); }
  78%  { transform: scale(1.06) rotate(1deg); }
  100% { transform: scale(1) rotate(0deg); }
}
```

#### 类型 D：循环动效 (loop)

```
适用: 装饰性、状态指示、加载
可选效果:
  - 呼吸脉冲 (opacity: 40%↔100%)
  - 旋转 (0°↔360°)
  - 摆动 (±15°)
  - 涟漪 (scale 脉冲)
时长: 1.5–3s/周期
```

### 3.3 SVG 文件内动画结构

每个 SVG 文件自包含动画，格式如下：

```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <defs>
    <style>
      /* 路径绘制 */
      @keyframes draw-1 {
        0%   { stroke-dashoffset: 120; }
        100% { stroke-dashoffset: 0; }
      }
      @keyframes pop-1 {
        0%   { opacity: 0; transform: scale(0); }
        60%  { opacity: 1; transform: scale(1.2); }
        100% { opacity: 1; transform: scale(1); }
      }
      @keyframes bounce-1 {
        0%   { transform: scale(1) rotate(0deg); }
        30%  { transform: scale(1.15) rotate(3deg); }
        55%  { transform: scale(0.93) rotate(-2deg); }
        78%  { transform: scale(1.05) rotate(1deg); }
        100% { transform: scale(1) rotate(0deg); }
      }
      .path-a { animation: draw-1 0.8s ease-in-out forwards; }
      .path-b { animation: draw-1 1.2s ease-in-out 0.15s forwards; }
      .fill-x { animation: pop-1 0.5s cubic-bezier(0.34,1.56,0.64,1) 0.3s forwards; opacity: 0; }
      .bounce  { animation: bounce-1 0.6s cubic-bezier(0.34,1.56,0.64,1) 1.5s forwards; }
    </style>
  </defs>
  <g class="bounce">
    <path class="path-a" d="..." stroke="#CC785C" stroke-dasharray="120" stroke-dashoffset="120"/>
    ...
  </g>
</svg>
```

---

## 4. 项目 SVG 库结构

每个项目在自身目录下创建 `assets/icons/` 文件夹：

```
project-root/
├── assets/
│   └── icons/
│       ├── README.md          # 项目专属图标清单
│       ├── check.svg          # 文件名 = 功能英文名
│       ├── target.svg
│       └── ...                # 所有用到的图标
└── index.html
```

### 命名规范

- 全小写英文
- 用连字符 `-` 分隔
- 语义化命名：`check.svg`、`lightbulb.svg`、`microphone.svg`
- 不包含版本/序号

### README.md 模板

```markdown
# SpeakScope SVG Icons

项目主题色: --accent #CC785C
副色: --success #5A9E6F (用于发音/正确标记)
特殊风格: 口语相关图标（🎤🔊）加声波纹路

## 图标清单

| 文件名 | 对应 emoji | 说明 |
|--------|-----------|------|
| check.svg | ✅ | 完成标记，描边+填充混合 |
| ...
```

---

## 5. Favicon 规范

- 格式：SVG（`favicon.svg`）
- viewBox: `0 0 32 32`（favicon 通常需要更紧凑）
- 使用项目最代表性的 1–2 个元素
- 颜色：`--accent` 为主，可加 `--paper` 底色
- 不带动画（favicon 不支持动画 SVG 在所有浏览器中）
- 放在项目根目录

---

## 6. 工作流程

### 为项目设计新图标

1. 查看 `assets/icons/` 现有库
2. 如果已有功能对应的图标 → 复用
3. 如果没有 → 根据本指南设计新 SVG
4. 确定动画类型（描边绘制 / 填充弹出 / 混合）
5. 生成自包含的动画 SVG 文件
6. 添加到项目 `assets/icons/` 并更新 README.md

### 新增项目

1. 确定项目主题色（可从 `shared/theme.css` 的 `--accent` 继承或扩展）
2. 创建 `assets/icons/` 目录
3. 创建 `assets/icons/README.md`
4. 按需设计图标
5. 生成 favicon.svg

---

> 最后更新: 2026-07-17
> 维护: 本指南由 SVG Icon Skill 调用，修改需同步更新 Skill
