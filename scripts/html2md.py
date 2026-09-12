"""把零基础详解HTML转markdown：保留h1-h4、表格、class语义（formula→引用块、tip/warning→引用、step→编号、explain→普通段落）"""
import re, html, sys, os

def convert(path):
    raw = open(path, encoding='utf-8').read()
    raw = re.sub(r'<(style|script|head)[\s\S]*?</\1>', '', raw)
    # 表格先行处理
    def table_md(m):
        t = m.group(0)
        rows = re.findall(r'<tr[^>]*>([\s\S]*?)</tr>', t)
        out_rows = []
        for r in rows:
            cells = re.findall(r'<t[hd][^>]*>([\s\S]*?)</t[hd]>', r)
            cells = [re.sub(r'\s+', ' ', strip_tags(c)).strip() or ' ' for c in cells]
            out_rows.append(cells)
        if not out_rows:
            return ''
        lines = []
        for i, r in enumerate(out_rows):
            lines.append('| ' + ' | '.join(r) + ' |')
            if i == 0:
                lines.append('|' + '---|' * len(r))
        return '\n' + '\n'.join(lines) + '\n'
    def strip_tags(s):
        s = re.sub(r'<br\s*/?>', ' ', s)
        s = re.sub(r'<strong>([\s\S]*?)</strong>', r'**\1**', s)
        s = re.sub(r'<b>([\s\S]*?)</b>', r'**\1**', s)
        s = re.sub(r'<em>([\s\S]*?)</em>', r'*\1*', s)
        s = re.sub(r'<[^>]+>', '', s)
        return html.unescape(s)
    raw = re.sub(r'<table[\s\S]*?</table>', table_md, raw)
    # 语义块
    raw = re.sub(r'<div class="formula">([\s\S]*?)</div>', lambda m: '\n> 📐 ' + strip_tags(m.group(1)).strip().replace('\n', ' ') + '\n', raw)
    raw = re.sub(r'<div class="tip">([\s\S]*?)</div>', lambda m: '\n> 💡 ' + strip_tags(m.group(1)).strip().replace('\n', ' ') + '\n', raw)
    raw = re.sub(r'<div class="warning">([\s\S]*?)</div>', lambda m: '\n> ⚠️ ' + strip_tags(m.group(1)).strip().replace('\n', ' ') + '\n', raw)
    raw = re.sub(r'<div class="answer">([\s\S]*?)</div>', lambda m: '\n> ✅ **' + strip_tags(m.group(1)).strip().replace('\n', ' ') + '**\n', raw)
    # 标题
    for i in range(1, 5):
        raw = re.sub(rf'<h{i}>([\s\S]*?)</h{i}>', lambda m, lv=i: '\n' + '#' * (lv + 1) + ' ' + strip_tags(m.group(1)).strip() + '\n', raw)
    # 列表
    raw = re.sub(r'<li>([\s\S]*?)</li>', lambda m: '\n- ' + strip_tags(m.group(1)).strip().replace('\n', ' '), raw)
    # 段落
    raw = re.sub(r'<p>([\s\S]*?)</p>', lambda m: '\n' + strip_tags(m.group(1)).strip() + '\n', raw)
    raw = re.sub(r'<div class="(?:card|example|explain|step|container)[^"]*">([\s\S]*?)</div>', lambda m: strip_tags(m.group(1)) + '\n', raw)
    raw = re.sub(r'<[^>]+>', '\n', raw)
    raw = html.unescape(raw)
    raw = re.sub(r'[ \t]+', ' ', raw)
    # 清理空行
    raw = re.sub(r'\n\s*\n+', '\n\n', raw)
    lines = [l.rstrip() for l in raw.split('\n')]
    return '\n'.join(lines).strip() + '\n'

if __name__ == '__main__':
    outdir = r'C:/Users/23738/Desktop/信号/.workbuddy/tmp/part_md'
    os.makedirs(outdir, exist_ok=True)
    for p in sys.argv[1:]:
        md = convert(p)
        name = os.path.basename(p).replace('.html', '.md')
        open(os.path.join(outdir, name), 'w', encoding='utf-8').write(md)
        print(name, len(md), 'chars')
