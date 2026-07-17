#!/usr/bin/env python3
"""
批量替换 HTML 课程中的 emoji → 内联动画 SVG
用法: python3 replace_emoji.py <project_dir>
"""
import os, re, sys

# ─── emoji → SVG 文件名映射 (合并所有项目) ───
EMOJI_MAP = {
    "📚": "books", "📖": "books", "📄": "document", "📝": "note",
    "🎯": "target", "💡": "lightbulb", "✅": "check", "❌": "cross",
    "📌": "pin", "🔗": "link", "✏️": "pencil", "✏": "pencil",
    "🔍": "search", "🔧": "wrench", "⚙️": "gear", "🧭": "compass",
    "📐": "ruler", "📊": "chart", "🗺️": "map", "🚀": "rocket",
    "🧠": "brain", "🧩": "puzzle", "🤖": "robot", "🔬": "microscope",
    "🧪": "flask", "⚠️": "warning", "✨": "sparkles", "🏆": "trophy",
    "💻": "monitor", "🏷️": "tag", "🟦": "square", "⏱️": "timer",
    "🔥": "fire", "🌐": "globe", "🎓": "graduation", "🗣": "speak",
    "📅": "calendar", "📦": "package", "📎": "attachment",
    "📈": "chart-up", "🛠": "tools", "🔊": "speaker", "🎬": "video",
    "❓": "question", "🤔": "thinking", "➡": "arrow-right",
    "🔵": "dot", "🟡": "dot-yellow", "📋": "clipboard", "🎤": "microphone",
    "✍": "writing", "✍️": "writing", "🔑": "key", "✦": "star",
    "⭐": "star", "🎯": "target", "⚠": "warning", "⏱": "timer",
    "🗺": "map", "🏷": "tag", "🛠": "tools",
    "🔬": "microscope", "🧪": "flask", "🧭": "compass",
    "📡": "satellite", "📰": "news", "⚡": "lightning",
    "🧑": "robot", "🗣": "speaking", "🎤": "microphone",
    "🎬": "video", "📋": "clipboard", "📊": "chart-bar",
    "🔄": "link", "🔁": "link", "🖼": "monitor",
    "🔒": "tag", "📸": "monitor", "📥": "package",
    "📤": "package", "💬": "speak", "🏛": "books",
    "🌱": "sparkles", "🌟": "sparkles", "🌿": "flask",
    "🏗": "tools", "🚪": "rocket", "📷": "monitor",
    "🔮": "search", "🔭": "search", "🔢": "chart",
    "💰": "trophy", "💎": "trophy", "🏥": "target",
    "🏠": "globe", "🌳": "flask", "🌲": "flask",
    "🌍": "globe", "🌈": "sparkles", "🌀": "warning",
    "⛔": "cross", "☁": "flask", "☀": "sparkles",
    # 检查标记变体
    "✓": "check", "✔": "check", "✗": "cross", "✘": "cross",
}

# 需要映射 SVG 路径
ICON_DIRS = {}

def get_svg_path(project_dir, icon_name):
    """查找 SVG 文件"""
    candidates = [
        os.path.join(project_dir, "assets", "icons", f"{icon_name}.svg"),
    ]
    for c in candidates:
        if os.path.exists(c):
            return c
    return None

def load_svg_inline(svg_path):
    """加载 SVG 并转成适合内联的单行"""
    with open(svg_path, "r", encoding="utf-8") as f:
        svg = f.read()
    # 移除 xml 声明和包裹的换行
    svg = svg.strip()
    if svg.startswith('<?xml'):
        svg = re.sub(r'<\?xml[^>]*>\n?', '', svg)
    # 转为单行（方便替换）
    svg = re.sub(r'\s+', ' ', svg).strip()
    # 调整尺寸为 1em × 1em，方便行内显示
    svg = re.sub(r'width="[^"]*"', 'width="1em"', svg)
    svg = re.sub(r'height="[^"]*"', 'height="1em"', svg)
    svg = re.sub(r'style="[^"]*"', '', svg)
    # 保持 viewBox
    return svg

def replace_emoji_in_html(html_path, project_dir):
    """替换单个 HTML 文件中的 emoji"""
    with open(html_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # 跳过已经有内联 SVG 的文件（避免重复替换）
    if 'class="emoji-svg"' in content:
        return False
    
    replaced_count = 0
    new_content = content
    
    # 按 emoji 长度降序排列（长 emoji 先匹配）
    for emoji in sorted(EMOJI_MAP.keys(), key=len, reverse=True):
        icon_name = EMOJI_MAP[emoji]
        svg_path = get_svg_path(project_dir, icon_name)
        if not svg_path:
            continue
        
        svg_inline = load_svg_inline(svg_path)
        if not svg_inline:
            continue
        
        # 替换 emoji 为内联 SVG
        replacement = f'<span class="emoji-svg">{svg_inline}</span>'
        
        # 用正则替换（注意 emoji 可能含特殊字符）
        escaped = re.escape(emoji)
        new_content, n = re.subn(escaped, replacement, new_content)
        replaced_count += n
    
    if replaced_count > 0:
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        return replaced_count
    return False

def add_css_to_html(html_path):
    """给 HTML 添加 emoji-svg 样式"""
    with open(html_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    if '.emoji-svg' in content:
        return False
    
    # 在 </style> 前插入
    css_block = '''
  /* 内联动画 SVG 图标 */
  .emoji-svg { display: inline-flex; align-items: center; vertical-align: middle; }
  .emoji-svg svg { display: inline-block; margin: 0 1px; }'''
    
    if '</style>' in content:
        content = content.replace('</style>', css_block + '\n</style>')
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(content)
        return True
    return False

def process_project(project_dir):
    """处理一个项目的所有 HTML 文件"""
    lessons_dir = os.path.join(project_dir, "lessons")
    if not os.path.exists(lessons_dir):
        print(f"  ✗ 没有 lessons/ 目录: {project_dir}")
        return 0, 0
    
    html_files = sorted([f for f in os.listdir(lessons_dir) if f.endswith(".html")])
    total_replaced = 0
    total_files = 0
    
    print(f"\n📂 {os.path.basename(project_dir)} ({len(html_files)} 个文件)")
    
    for fname in html_files:
        fpath = os.path.join(lessons_dir, fname)
        
        # 加 CSS
        add_css_to_html(fpath)
        
        # 替换 emoji
        n = replace_emoji_in_html(fpath, project_dir)
        if n:
            print(f"  ✓ {fname}: 替换了 {n} 处")
            total_replaced += n
            total_files += 1
    
    # 也处理首页
    index_path = os.path.join(project_dir, "index.html")
    if os.path.exists(index_path):
        add_css_to_html(index_path)
        n = replace_emoji_in_html(index_path, project_dir)
        if n:
            print(f"  ✓ index.html: 替换了 {n} 处")
            total_replaced += n
            total_files += 1
    
    return total_files, total_replaced

if __name__ == "__main__":
    projects = [
        "/home/zjq/paperlesson",
        "/home/zjq/speakscope",
        "/home/zjq/aihot-topics",
    ]
    
    grand_total_files = 0
    grand_total_replaced = 0
    
    for proj in projects:
        files, replaced = process_project(proj)
        grand_total_files += files
        grand_total_replaced += replaced
    
    print("\n" + "="*50)
    print(f"✅ 总计: {grand_total_files} 个文件, {grand_total_replaced} 处 emoji 替换")
    print("="*50)
