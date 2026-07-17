#!/usr/bin/env python3
"""
PaperLesson SVG Icon Set — 把课程里的 emoji 替换为统一风格的 SVG 图标。
生成展示 PDF。
"""

import os, weasyprint, textwrap

# ── 设计规范 ──
# 遵循 PaperLesson 设计系统
ACCENT = "#CC785C"
ACCENT_DEEP = "#A85D42"
ACCENT_LIGHT = "#E8C4B0"
ACCENT_DIM = "rgba(204, 120, 92, 0.15)"
INK = "#1A1A2E"
INK_60 = "#5A5A6A"
INK_40 = "#8A8A9A"
PAPER = "#F7F4EE"
PAPER_LIGHT = "#FBFAF7"
BORDER = "#E8E4DC"

# ── 图标定义 ──
# (id, emoji, 中文名, 用途说明, svg_paths)
# svg_paths: list of (d, fill?, stroke?, stroke_width?)
# viewBox 统一 0 0 24 24, stroke="#CC785C", stroke-width=2, 圆头圆角

def icon_svg(d_paths, view_box="0 0 24 24"):
    """从路径列表构建 SVG 字符串"""
    parts = []
    for item in d_paths:
        d = item[0]
        attrs = {
            "d": d,
            "fill": item[1] if len(item) > 1 else "none",
            "stroke": item[2] if len(item) > 2 else ACCENT,
            "stroke-width": str(item[3]) if len(item) > 3 else "2",
            "stroke-linecap": "round",
            "stroke-linejoin": "round",
        }
        tag = "<path "
        for k, v in attrs.items():
            if v and v != "none":
                tag += f'{k}="{v}" '
            elif k == "fill" and v == "none":
                tag += f'{k}="none" '
        tag += "/>"
        parts.append(tag)
    paths_str = "\n        ".join(parts)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="{view_box}" width="32" height="32">
        {paths_str}
      </svg>'''

# ── 30 个图标 ──
ICONS = [
    # 1 书籍/资料
    ("books", "📚", "书籍", "学习资料 / 参考文献",
     [("M4 4h6v8l-3-2-3 2V4z", "none", ACCENT, 2),
      ("M10 4h6v8l-3-2-3 2V4z", "none", ACCENT, 2),
      ("M16 3h4v10l-2-1.5-2 1.5V3z", "none", ACCENT, 2)],
     "24 24"),
    # 2 目标
    ("target", "🎯", "目标", "课程目标 / 核心重点",
     [("M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20z", "none", ACCENT, 2),
      ("M12 6a6 6 0 1 0 0 12 6 6 0 0 0 0-12z", "none", ACCENT, 2),
      ("M12 10a2 2 0 1 0 0 4 2 2 0 0 0 0-4z", ACCENT, "none", 0)],
     "24 24"),
    # 3 灯泡/洞察
    ("lightbulb", "💡", "洞察", "关键洞察 / 提示",
     [("M12 2a6 6 0 0 0-4 10.3c1 .8 1.5 2 1.5 3.2v.5h5v-.5c0-1.3.5-2.5 1.5-3.3A6 6 0 0 0 12 2z", "none", ACCENT, 2),
      ("M9 18h6", "none", ACCENT, 2),
      ("M10 21h4", "none", ACCENT, 2)],
     "24 24"),
    # 4 对勾
    ("check", "✅", "已完成", "已完成 / 已覆盖",
     [("M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20z", "none", ACCENT, 2),
      ("M8 12l3 3 5-5", "none", ACCENT, 2)],
     "24 24"),
    # 5 叉号
    ("cross", "❌", "未完成", "未完成 / 不适用",
     [("M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20z", "none", ACCENT, 2),
      ("M9 9l6 6M15 9l-6 6", "none", ACCENT, 2)],
     "24 24"),
    # 6 大头针
    ("pin", "📌", "标记", "标记 / 待阅读",
     [("M12 2a7 7 0 0 0-7 7c0 5 7 13 7 13s7-8 7-13a7 7 0 0 0-7-7z", "none", ACCENT, 2),
      ("M12 9a2 2 0 1 0 0 4 2 2 0 0 0 0-4z", ACCENT, "none", 0)],
     "24 24"),
    # 7 链接
    ("link", "🔗", "链接", "拓展阅读 / 引用链接",
     [("M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71", "none", ACCENT, 2),
      ("M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71", "none", ACCENT, 2)],
     "24 24"),
    # 8 笔记/备忘录
    ("note", "📝", "笔记", "复习 / 笔记 / 思考题",
     [("M16 3H5a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V8l-5-5z", "none", ACCENT, 2),
      ("M16 3v5h5", "none", ACCENT, 2),
      ("M8 13h8M8 17h5M8 9h1", "none", ACCENT, 2)],
     "24 24"),
    # 9 文档
    ("document", "📄", "文档", "论文 / 文件 / 资料",
     [("M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8l-6-6z", "none", ACCENT, 2),
      ("M14 2v6h6", "none", ACCENT, 2),
      ("M9 13h6M9 17h6", "none", ACCENT, 2)],
     "24 24"),
    # 10 铅笔
    ("pencil", "✏️", "练习", "练习题 / 作业",
     [("M17 3a2.83 2.83 0 1 1 4 4L7.5 20.5 2 22l1.5-5.5L17 3z", "none", ACCENT, 2),
      ("M15 5l4 4", "none", ACCENT, 2)],
     "24 24"),
    # 11 放大镜
    ("search", "🔍", "搜索", "查找 / 探索",
     [("M10 2a8 8 0 1 0 0 16 8 8 0 0 0 0-16z", "none", ACCENT, 2),
      ("M21 21l-6-6", "none", ACCENT, 2)],
     "24 24"),
    # 12 扳手
    ("wrench", "🔧", "工具", "方法 / 实现工具",
     [("M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.8-3.8a1 1 0 0 0-1.4-1.4l-3.8 3.8-1.6-1.6a1 1 0 0 0-1.4 0 5 5 0 0 0-6.3 7.5l-6.2 6.3a1 1 0 0 0 1.4 1.4l6.2-6.3a5 5 0 0 0 7.5-6.3z", "none", ACCENT, 2)],
     "24 24"),
    # 13 齿轮
    ("gear", "⚙️", "设置", "机制 / 系统配置",
     [("M12 15a3 3 0 1 0 0-6 3 3 0 0 0 0 6z", "none", ACCENT, 2),
      ("M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06A1.65 1.65 0 0 0 4.68 15a1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06A1.65 1.65 0 0 0 9 4.68a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06A1.65 1.65 0 0 0 19.4 9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z", "none", ACCENT, 2)],
     "24 24"),
    # 14 罗盘
    ("compass", "🧭", "导航", "方向 / 导航 / 指引",
     [("M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20z", "none", ACCENT, 2),
      ("M16.24 7.76l-2.12 6.36-6.36 2.12 2.12-6.36 6.36-2.12z", "none", ACCENT, 2),
      ("M12 12m-1 0a1 1 0 1 0 2 0 1 1 0 1 0-2 0", ACCENT, "none", 0)],
     "24 24"),
    # 15 三角尺
    ("ruler", "📐", "度量", "评估 / 测量 / 指标",
     [("M4 20l16-16M4 20l8-8M4 20l4-4M4 20h16", "none", ACCENT, 2),
      ("M20 4v16H4", "none", ACCENT, 2)],
     "24 24"),
    # 16 图表
    ("chart", "📊", "图表", "数据 / 实验结果",
     [("M4 20h16", "none", ACCENT, 2),
      ("M6 16v-4M10 16v-6M14 16v-8M18 16v-2", "none", ACCENT, 2)],
     "24 24"),
    # 17 地图
    ("map", "🗺️", "地图", "路线 / 规划 / SLAM地图",
     [("M3 7l6-3 6 3 6-3v13l-6 3-6-3-6 3V7z", "none", ACCENT, 2),
      ("M9 4v13M15 7v13", "none", ACCENT, 2)],
     "24 24"),
    # 18 火箭
    ("rocket", "🚀", "进阶", "进阶 / 启动 / 高效",
     [("M12 2s-4 7-4 12a4 4 0 0 0 8 0c0-5-4-12-4-12z", "none", ACCENT, 2),
      ("M10 14l-4 4M14 14l4 4", "none", ACCENT, 2),
      ("M12 14v4M10 20h4", "none", ACCENT, 2)],
     "24 24"),
    # 19 大脑
    ("brain", "🧠", "思维", "思考 / 认知 / 理解",
     [("M12 4a5 5 0 0 1 5 5c0 2-1 3-1 4s1 2 1 3a4 4 0 0 1-4 4h-2a4 4 0 0 1-4-4c0-1 1-2 1-3s-1-2-1-4a5 5 0 0 1 5-5z", "none", ACCENT, 2),
      ("M9 10h6M9 14h4", "none", ACCENT, 2)],
     "24 24"),
    # 20 拼图
    ("puzzle", "🧩", "组件", "模块 / 组件 / 拼合",
     [("M19 10h2a2 2 0 0 1 2 2v6a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2v-6a2 2 0 0 1 2-2h2", "none", ACCENT, 2),
      ("M7 10V7a3 3 0 0 1 3-3h0a3 3 0 0 1 3 3v3", "none", ACCENT, 2),
      ("M11 10V7a3 3 0 0 1 3-3h0a3 3 0 0 1 3 3v3", "none", ACCENT, 2)],
     "24 24"),
    # 21 机器人
    ("robot", "🤖", "机器人", "机器人 / AI / 自动化",
     [("M8 12h8", "none", ACCENT, 2),
      ("M6 8h12a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2v-8a2 2 0 0 1 2-2z", "none", ACCENT, 2),
      ("M9 8V6a3 3 0 0 1 6 0v2", "none", ACCENT, 2),
      ("M9 15v1M15 15v1", "none", ACCENT, 2)],
     "24 24"),
    # 22 显微镜
    ("microscope", "🔬", "研究", "研究 / 深入分析",
     [("M6 2h12M9 2v6a3 3 0 0 1-3 3h0a3 3 0 0 0-3 3v8h12v-8a3 3 0 0 0-3-3h0a3 3 0 0 1-3-3V2", "none", ACCENT, 2),
      ("M6 20h12", "none", ACCENT, 2)],
     "24 24"),
    # 23 试管
    ("flask", "🧪", "实验", "实验 / 测试 / 验证",
     [("M9 2h6M12 2v8l5 8a3 3 0 0 1-3 3h-4a3 3 0 0 1-3-3l5-8", "none", ACCENT, 2),
      ("M7 17h10", "none", ACCENT, 2)],
     "24 24"),
    # 24 警告
    ("warning", "⚠️", "注意", "注意 / 警告 / 重要提醒",
     [("M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z", "none", ACCENT, 2),
      ("M12 9v4M12 17h.01", "none", ACCENT, 2)],
     "24 24"),
    # 25 星星/闪光
    ("sparkles", "✨", "亮点", "亮点 / 精彩 / 新特性",
     [("M12 2l1.5 4.5L18 8l-4.5 1.5L12 14l-1.5-4.5L6 8l4.5-1.5L12 2z", "none", ACCENT, 2),
      ("M8 18l1 2 2-1-1-2-2 1zM16 14l1 2 2-1-1-2-2 1z", "none", ACCENT, 2)],
     "24 24"),
    # 26 奖杯
    ("trophy", "🏆", "成就", "成就 / 里程碑 / 优胜",
     [("M6 2h12v2a6 6 0 0 1-12 0V2z", "none", ACCENT, 2),
      ("M8 11a4 4 0 0 0 8 0", "none", ACCENT, 2),
      ("M12 14v8M8 22h8", "none", ACCENT, 2),
      ("M18 5h2a2 2 0 0 1 2 2v1a3 3 0 0 1-4 2.8M6 5H4a2 2 0 0 0-2 2v1a3 3 0 0 0 4 2.8", "none", ACCENT, 2)],
     "24 24"),
    # 27 电脑
    ("monitor", "💻", "编程", "代码 / 编程 / 实现",
     [("M2 4a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V4z", "none", ACCENT, 2),
      ("M8 20h8M12 16v4", "none", ACCENT, 2),
      ("M8 8l3 3-3 3M13 14h3", "none", ACCENT, 2)],
     "24 24"),
    # 28 标签
    ("tag", "🏷️", "标签", "标签 / 分类 / 关键词",
     [("M20.59 13.41l-7.17 7.17a2 2 0 0 1-2.83 0L2 12V2h10l8.59 8.59a2 2 0 0 1 0 2.82z", "none", ACCENT, 2),
      ("M7 7h.01", "none", ACCENT, 2)],
     "24 24"),
    # 29 方块标记 (替代 🟦)
    ("square", "🟦", "方块标记", "列表项 / 要点标记",
     [("M4 4h16v16H4z", "none", ACCENT, 2)],
     "24 24"),
    # 30 时钟/时间
    ("timer", "⏱️", "计时", "时间 / 时长 / 进度",
     [("M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20z", "none", ACCENT, 2),
      ("M12 6v6l4 2", "none", ACCENT, 2)],
     "24 24"),
]

def build_html():
    """生成展示 HTML"""
    rows = []
    for icon in ICONS:
        icon_id, emoji, name, desc, paths, vb = icon
        svg = icon_svg(paths, vb)
        rows.append(f'''
        <div class="icon-card">
          <div class="icon-row">
            <div class="icon-box emoji-box">{emoji}</div>
            <div class="arrow">→</div>
            <div class="icon-box svg-box">{svg}</div>
          </div>
          <div class="icon-label">{name}</div>
          <div class="icon-desc">{desc}</div>
        </div>''')

    icons_grid = "\n".join(rows)

    html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>PaperLesson · SVG 图标集</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@400;600;700;900&family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{
    font-family: 'Inter', -apple-system, 'PingFang SC', 'Microsoft YaHei', sans-serif;
    background: {PAPER};
    color: {INK};
    line-height: 1.6;
    -webkit-font-smoothing: antialiased;
    padding: 0;
  }}

  .page {{
    width: 210mm;
    min-height: 297mm;
    padding: 20mm 15mm;
    margin: 0 auto;
    background: {PAPER_LIGHT};
  }}

  /* 封面 */
  .cover {{
    text-align: center;
    padding: 50mm 0 30mm;
    page-break-after: always;
  }}
  .cover h1 {{
    font-family: 'Noto Serif SC', serif;
    font-size: 42px;
    font-weight: 900;
    letter-spacing: -0.03em;
    color: {INK};
    margin-bottom: 12px;
  }}
  .cover h1 .accent {{ color: {ACCENT}; }}
  .cover .subtitle {{
    font-size: 18px;
    color: {INK_60};
    max-width: 400px;
    margin: 0 auto 40px;
    line-height: 1.8;
  }}
  .cover .divider {{
    width: 60px;
    height: 3px;
    background: {ACCENT};
    margin: 30px auto;
    border-radius: 2px;
  }}
  .cover .meta {{
    font-size: 14px;
    color: {INK_40};
    margin-top: 40px;
  }}
  .cover .icon-preview {{
    margin: 40px auto;
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 12px;
    max-width: 400px;
  }}
  .cover .icon-preview svg {{ width: 48px; height: 48px; opacity: 0.7; }}

  /* 说明页 */
  .intro {{
    page-break-after: always;
    padding: 30mm 0;
  }}
  .intro h2 {{
    font-family: 'Noto Serif SC', serif;
    font-size: 28px;
    margin-bottom: 20px;
  }}
  .intro p {{
    font-size: 15px;
    color: {INK_60};
    line-height: 1.9;
    max-width: 520px;
    margin-bottom: 16px;
  }}
  .intro .stat-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 16px;
    margin: 30px 0;
  }}
  .intro .stat-card {{
    background: {PAPER};
    border: 1px solid {BORDER};
    border-radius: 12px;
    padding: 20px;
    text-align: center;
  }}
  .intro .stat-card .num {{
    font-size: 36px;
    font-weight: 700;
    color: {ACCENT};
  }}
  .intro .stat-card .label {{
    font-size: 12px;
    color: {INK_40};
    margin-top: 4px;
  }}
  .intro .specs {{
    background: {PAPER};
    border: 1px solid {BORDER};
    border-radius: 12px;
    padding: 20px 24px;
    margin-top: 24px;
  }}
  .intro .specs h3 {{
    font-size: 16px;
    font-weight: 600;
    margin-bottom: 12px;
  }}
  .intro .specs dl {{
    display: grid;
    grid-template-columns: auto 1fr;
    gap: 8px 20px;
    font-size: 14px;
  }}
  .intro .specs dt {{
    font-weight: 600;
    color: {ACCENT_DEEP};
    white-space: nowrap;
  }}
  .intro .specs dd {{
    color: {INK_60};
  }}

  /* 图标网格 */
  .grid-section {{
    page-break-after: always;
    padding: 10mm 0;
  }}
  .grid-section:last-child {{
    page-break-after: auto;
  }}
  .grid-section h2 {{
    font-family: 'Noto Serif SC', serif;
    font-size: 22px;
    margin-bottom: 6px;
    color: {INK};
  }}
  .grid-section .section-desc {{
    font-size: 13px;
    color: {INK_40};
    margin-bottom: 24px;
  }}
  .grid {{
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 12px;
  }}
  .icon-card {{
    background: {PAPER_LIGHT};
    border: 1px solid {BORDER};
    border-radius: 12px;
    padding: 16px 12px;
    text-align: center;
    transition: box-shadow .2s;
  }}
  .icon-row {{
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    margin-bottom: 10px;
  }}
  .icon-box {{
    display: flex;
    align-items: center;
    justify-content: center;
    width: 44px;
    height: 44px;
    border-radius: 10px;
  }}
  .emoji-box {{ font-size: 28px; }}
  .svg-box {{
    background: {ACCENT_DIM};
  }}
  .arrow {{
    font-size: 18px;
    color: {INK_20};
    font-weight: 300;
  }}
  .icon-label {{
    font-size: 15px;
    font-weight: 600;
    color: {INK};
    margin-bottom: 2px;
  }}
  .icon-desc {{
    font-size: 11px;
    color: {INK_40};
    line-height: 1.4;
  }}

  /* 底页 */
  .footer-page {{
    page-break-after: auto;
    text-align: center;
    padding: 40mm 0 20mm;
  }}
  .footer-page h2 {{
    font-family: 'Noto Serif SC', serif;
    font-size: 24px;
    margin-bottom: 16px;
  }}
  .footer-page p {{
    font-size: 14px;
    color: {INK_60};
    max-width: 400px;
    margin: 0 auto;
    line-height: 1.8;
  }}

  @page {{
    size: A4;
    margin: 0;
  }}
  @media print {{
    body {{ background: white; }}
  }}
</style>
</head>
<body>

<div class="page">
  <!-- 封面 -->
  <div class="cover">
    <h1>PaperLesson <span class="accent">·</span> 图标集</h1>
    <div class="divider"></div>
    <p class="subtitle">将课程中的 emoji 替换为统一风格的矢量图标<br>适配 PaperLesson 设计系统</p>
    <div class="icon-preview">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="48" height="48"><path d="M4 4h6v8l-3-2-3 2V4zM10 4h6v8l-3-2-3 2V4zM16 3h4v10l-2-1.5-2 1.5V3z" fill="none" stroke="{ACCENT}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="48" height="48"><path d="M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20zM8 12l3 3 5-5" fill="none" stroke="{ACCENT}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="48" height="48"><path d="M12 2a6 6 0 0 0-4 10.3c1 .8 1.5 2 1.5 3.2v.5h5v-.5c0-1.3.5-2.5 1.5-3.3A6 6 0 0 0 12 2zM9 18h6M10 21h4" fill="none" stroke="{ACCENT}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="48" height="48"><path d="M12 2a7 7 0 0 0-7 7c0 5 7 13 7 13s7-8 7-13a7 7 0 0 0-7-7z" fill="none" stroke="{ACCENT}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><circle cx="12" cy="9" r="2" fill="{ACCENT}" stroke="none"/></svg>
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="48" height="48"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71" fill="none" stroke="{ACCENT}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71" fill="none" stroke="{ACCENT}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="48" height="48"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0zM12 9v4M12 17h.01" fill="none" stroke="{ACCENT}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
    </div>
    <p class="meta">PaperLesson Design System · 2026</p>
  </div>

  <!-- 说明页 -->
  <div class="intro">
    <h2>为什么用 SVG 代替 emoji？</h2>
    <p>PaperLesson 课程中大量使用 emoji 作为视觉标记，统计显示 99 节课中有 <strong>5337 处</strong> emoji 使用。虽然直观，但 emoji 存在明显的短板。</p>

    <div class="stat-grid">
      <div class="stat-card">
        <div class="num">99</div>
        <div class="label">课程文件</div>
      </div>
      <div class="stat-card">
        <div class="num">5337</div>
        <div class="label">emoji 使用处</div>
      </div>
      <div class="stat-card">
        <div class="num">30</div>
        <div class="label">SVG 图标数</div>
      </div>
    </div>

    <div class="specs">
      <h3>🎨 设计规范</h3>
      <dl>
        <dt>风格</dt><dd>线性描边 · 圆头圆角 · 简约学术</dd>
        <dt>尺寸</dt><dd>32×32 px（ViewBox 24×24）</dd>
        <dt>主色</dt><dd><span style="color:{ACCENT}">●</span> {ACCENT} — 陶土橙（accent）</dd>
        <dt>描边</dt><dd>2px · round cap · round join</dd>
        <dt>适配</dt><dd>与 PaperLesson 主题色系统完全统一</dd>
        <dt>用法</dt><dd>替换 emoji → &lt;svg&gt; 标签 / &lt;img&gt; 引用</dd>
      </dl>
    </div>

    <div class="specs" style="margin-top:16px;">
      <h3>💡 emoji 的三个问题</h3>
      <dl>
        <dt>① 分辨率</dt><dd>在不同平台渲染效果不一致，高DPI下模糊</dd>
        <dt>② 风格</dt><dd>无法与品牌色统一，破坏视觉一致性</dd>
        <dt>③ 语义</dt><dd>用户对 emoji 的理解有歧义</dd>
      </dl>
    </div>
  </div>

  <!-- 图标网格 -->
  <div class="grid-section">
    <h2>图标全集</h2>
    <p class="section-desc">30 个 SVG 图标 · emoji → SVG 对照</p>
    <div class="grid">
      {icons_grid}
    </div>
  </div>

  <!-- 底页 -->
  <div class="footer-page">
    <h2>下一步</h2>
    <div class="divider" style="margin:20px auto;"></div>
    <p>确定图标方案后，编写批量替换脚本<br>将 99 节课程的 5337 处 emoji 一键替换为 SVG</p>
  </div>
</div>

</body>
</html>'''
    return html


if __name__ == "__main__":
    outdir = "/home/zjq/paperlesson/achievements"
    os.makedirs(outdir, exist_ok=True)

    html = build_html()
    html_path = os.path.join(outdir, "icon-set.html")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✅ HTML 已保存: {html_path}")

    pdf_path = os.path.join(outdir, "PaperLesson-Icon-Set.pdf")
    weasyprint.HTML(filename=html_path).write_pdf(pdf_path)
    print(f"✅ PDF 已保存: {pdf_path}")
    print(f"   文件大小: {os.path.getsize(pdf_path) / 1024:.0f} KB")
