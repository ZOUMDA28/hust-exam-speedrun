---
name: hust-exam-speedrun
description: "华科课程考试速通复习资料生成器：从零基础到 80+ 分。当用户几天内要考试、要求'速通/速成/抱佛脚/零基础'复习、或要求'以后做资料只生成html'时触发。**唯一交付物：单文件交互式 HTML 讲义**（KaTeX 实时公式 + 5 种语义块 + 可折叠答案 + 侧边锚点导航 + 顶部阅读进度），按题型套路组织。学习路线图/必背公式/解题套路/例题精讲/作业详解/速记口诀——一份 HTML 自带完整复习链路。覆盖工作流：调研样卷确定题型 → 写 HTML 讲义 → 本地保存供浏览器打开 → 可选上传飞书作为附件共享。适用于任何一门有样卷和作业答案的课程。"
agent_created: true
---

# 华科考试速通复习资料生成（单文件 HTML 讲义）

## 目标

为一名零基础、考前 1~3 天的学生，产出「按题型套路组织」的单文件交互式 HTML 讲义，目标 80+ 分。**唯一交付物是 HTML**，不再生成 markdown/飞书云文档——HTML 在任何设备都能用、能离线、可邮件、可发U盘、可挂飞书，全程以最快路径执行，不追求系统性、只追求拿分。

## 总流程（按序执行）

```
调研资料(≤30min) → 问4个决策问题 → 写HTML讲义（唯一交付物） → 本地保存 → 可选上传飞书附件
```

**为什么唯一交付物是 HTML**：
- **零依赖**：发邮件、传U盘、存手机、挂飞书，任何方式都能用
- **离线可用**：KaTeX 资源 + 图片可内联 base64，断网照常复习
- **碎片时间友好**：通勤、食堂、等人都能"刷"，比飞书文档打开快
- **公式友好**：KaTeX 渲染 LaTeX 公式比任何在线文档都漂亮
- **可折叠答案**：先做题，看不下去再展开，对照练习

## 第一阶段：资料调研

在用户工作区找齐四类材料，并快速判断各自可用性：

| 材料 | 用途 | 处理方式 |
|------|------|----------|
| 样卷（历年真题） | **讲义的组织骨架**——按样卷大题反推题型和分值 | PDF 文字版直接读；扫描版找配套扫描图上传知识库供自测 |
| 总复习提纲 | 老师划的重点范围 | 对照样卷交叉确认考试范围 |
| 作业解答 docx | 例题来源 + 讲义"作业同类题索引" | 用 `scripts/extract_docx_text.py` 解包提取文字（docx 是 zip，word/document.xml 里的 `<w:t>` 是正文、`<m:t>` 是 Word 公式） |
| 课件/教材 PDF | 公式核对 | 已有 `_txt/` 提取文本则用文本；正文公式会破碎，只做核对不做主素材 |

关键判断点：
- **样卷是整个流程的地基**。读完样卷后总结出：几道大题、每题考什么知识点、分值分布。讲义就按这个结构写。
- 扫描版 PDF 提不出文字时，检查是否有配套扫描图目录（如 `_img/`）。图片直接上传知识库给用户自测用，不要耗时间做 OCR。
- 作业 docx 要抽查 1~2 份：判断题目是纯文字还是大量公式，据此决定"导入在线版"还是"传原文件"（见第四阶段）。

## 第二阶段：问用户 4 个决策问题（AskUserQuestion，一次问完）

1. **考试范围**：按全范围+样卷题型，还是老师划了重点？（选重点则让用户补充）
2. **讲义结构**：按题型套路组织（推荐）还是按章节？
3. **作业答案处理**：docx 原样进飞书+讲义做题型索引（推荐），还是重排精讲？
4. **知识库是否分享给同学**。

用户如果催"快点"，跳过提问直接按推荐项执行。

## 第三阶段：撰写讲义 HTML（唯一交付物）

### 输出位置与命名

每份讲义单独一个 HTML 文件，文件名按章节/题型命名：

```
.workbuddy/wiki_html/
├── 00_复习路线图.html                  ← 首页（提纲时间表）
├── 01_第1章_信号与系统基础.html          ← 零基础入门（必须最先写，按周次的教程或按章节）
├── 02_第2章_连续系统时域分析.html
├── ...每章一章
├── 10_加练例题册_每题型超详解.html
└── 11_样卷_7题完整手写详解.html
```

如要把讲义上传分享（同学/老师），**只上传 HTML 原文件**（`drive +upload` 即可，飞书会保留原文件名直接打开），不做 markdown 转换、不做飞书云文档。

### 必备 CSS 体系（详见 references/html-template.md）

```css
:root {
  --bg:#f8f6f1; --card:#fff; --ink:#1a1a2e; --ink-soft:#4a4a6a;
  --accent:#2d5a8e; --accent-light:#e8f0fa; --accent2:#c0392b; --accent2-light:#fdecea;
  --green:#27ae60; --green-light:#eafaf1; --orange:#e67e22; --orange-light:#fef5e7;
  --purple:#6c3483; --purple-light:#f4ecf7; --border:#e0ddd5; --code-bg:#f0ede6;
}
```

### 5 种语义块（配色固定，全篇统一使用）

| class | 色 | 前缀 | 用途 |
|-------|----|------|------|
| `.key` | 绿 | ✅ 核心结论 | 必背的定义、定理、重要结论 |
| `.tip` | 蓝 | 💡 提示 | 易混辨析、知识串联 |
| `.warn` | 橙 | ⚠️ 易错点 | 考场常踩的坑 |
| `.routine` | 紫 | 🎯 解题套路 | 固定编号步骤，照套即可 |
| `.example-box` | 框线 | 例题 | 含 `.ex-tag` 标签 + `.collapse` 可折叠解答 |

### 章节骨架模板（直接复用）

```html
<section class="chapter" id="anchor">
  <h2>📶 章节标题</h2>

  <div class="key"><strong>定义：</strong>……</div>

  <h3>小节</h3>
  <div class="formula-block">
    <span class="label">公式名</span>
    $$E = \int_{-\infty}^{\infty}|f(t)|^2 dt$$
  </div>

  <div class="routine">
    <p><strong>套路：</strong>对于 ……</p>
    <ol class="steps">
      <li>步骤1</li>
      <li>步骤2</li>
    </ol>
  </div>

  <div class="example-box">
    <span class="ex-tag">例题</span>
    <p><strong>题目：</strong>……</p>
    <div class="collapse" onclick="this.classList.toggle('open')">
      <div class="collapse-head">点击查看解答 <span class="arrow">▶</span></div>
      <div class="collapse-body">
        <p>步骤……</p>
        <div class="key">答案：……</div>
      </div>
    </div>
  </div>
</section>
```

### 完整讲义骨架（一份标准讲义的目录）

1. **顶栏 topbar**：课程章节名 + 阅读进度（`#progress`）
2. **侧边栏 sidebar**：分组锚点链接（入门/正文/作业详解/总结）
3. **🗺️ 学习路线图（必有，放在最前）**：
   - 与相邻章节对比表（连续 vs 离散，老套路迁移到新题型）
   - 本章 3 大核心 + 编号步骤
   - `.tip` 总结重点
4. **正文**：每个核心概念一节，含公式块 + 对比表 + 解题套路
5. **作业详解**：每题一个 `<section class="chapter" id="hw-*">`，完整解答 + 折叠展开
6. **📌 知识图谱与速记**：表格 + `.warn` 易错点列表 + 速记口诀

### <head> 必含

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"
        onload="renderMath()"></script>
<script>
  function renderMath(){
    renderMathInElement(document.body,{delimiters:[
      {left:"$$",right:"$$",display:true},{left:"$",right:"$",display:false}
    ]});
  }
  window.addEventListener('scroll',()=>{
    const sc=document.documentElement.scrollTop;
    const tot=document.documentElement.scrollHeight-window.innerHeight;
    const pct=tot>0?Math.min(100,Math.round(sc/tot*100)):0;
    const el=document.getElementById('progress');
    if(el)el.textContent='阅读进度 '+pct+'%';
  });
</script>
```

### 写作硬性要求

- 公式一律 `$$...$$`（行间）或 `$...$`（行内），KaTeX 自动渲染。
- 用户自称零基础时**每一步算术都展开**（复数取模、通分、指数运算都要写）。
- 例题优先取自作业题（有官方答案可对照），其次教材典型题。
- 折叠答案用 `<div class="collapse" onclick="this.classList.toggle('open')">`，避免把答案直接露出。

### 离线化（推荐，做完 HTML 后做一次）

考试环境可能无网。把外部 KaTeX 资源内联 + 图片转 base64，让 HTML 单文件完全离线可用：

1. 下载 KaTeX 的 `katex.min.css` / `katex.min.js` / `auto-render.min.js` 本地化（或用 `<link>` + `<script>` 在线，浏览器会缓存）。
2. matplotlib 输出的 PNG → base64 → `<img src="data:image/png;base64,...">` 内联。
3. 保存为 `讲义_离线版.html`，自包含、可邮件发送、可刻U盘。

### 画图题配图（强烈推荐）

频谱图 / 幅频曲线 / 波形图——纯文字讲不透，必须配图。**HTML 用 base64 内联**：

```python
import base64, matplotlib.pyplot as plt
plt.savefig('tmp.png', dpi=150)
b64 = base64.b64encode(open('tmp.png','rb').read()).decode()
html_img = f'<img src="data:image/png;base64,{b64}" alt="..." style="max-width:100%;border:1px solid var(--border);border-radius:6px;">'
```

写入 HTML 后用浏览器打开是单文件，离线也好用。**关键技巧**：150dpi，中文字体 `'Microsoft YaHei'`；unicode 下标（₄₀等）在雅黑里缺字，图里用普通数字 `4/0`；频谱图 `ax.stem` + 逐点 `annotate` 数值；幅频曲线标 3 个关键点（起点/极值/终点）。

### 补充资料的处理方式（按格式分流）

| 资料格式 | 处理方式 |
|---|---|
| 学长/同学的 HTML 讲义 | **直接重写为统一标准的 HTML**（参考本模板的 CSS+class 体系），融合到讲义合集 |
| HTML 讲义（其他AI/工具产物） | 直接打开人工重写为标准模板 |
| PDF/PPT/扫描版原文件 | **不转换**，单独上传飞书/网盘作为参考资料，标注链接进 HTML 讲义目录 |

## 第四阶段：交付（HTML 上传到飞书作为附件）

如需把讲义分享给同学（飞书作为最终共享渠道）：

1. **本地交付**：HTML 文件存到 `.workbuddy/wiki_html/`，用户直接双击打开；也可用任意 HTTP 服务器临时托管（`python -m http.server 8000`）。
2. **飞书附件**：`lark-cli drive +upload --as user --file <html> --name "<讲义>.html"` 上传，云空间直接双击就能在浏览器里打开。
3. **同一课程多份讲义**：建一个云空间文件夹（如 `/信号与系统速通讲义/`），把全部 HTML 丢进去，发文件夹链接给同学。

### 已知坑（实战踩过，务必避开）

1. **KaTeX CDN 在离线环境加载失败**：kaTeX 走 jsdelivr CDN，国内考试机可能无外网。**强烈建议本地化 KaTeX**，或考试前确认网络可用。
2. **matplotlib 中文缺字**：unicode 下标（₄₀等）在雅黑里缺字，图里和讲义里一律用普通 `4/0`。
3. **公式块表格内 LaTeX 竖线**：HTML 写 `<td>...</td>` 而不是表格管道 `|`，飞书转换才安全。
4. **KaTeX 行内公式 `$...$` 和加粗冲突**：行内公式前后用空格隔开避免被吃掉：`**结论是** $E = mc^2$` 不要连写。
5. **飞书上传 docx 丢公式**：本流程**不做 markdown 转换**，直接传 HTML 文件，无此问题。
6. **折叠按钮 onclick 在某些环境失效**：搭配 `<a href="#" onclick="...">` 或 `<button>` 形式更稳。

## 第五阶段：验证与交付

- 抽查 2 篇讲义 + 1 篇作业的渲染（公式块、表格完整性）。
- 验证知识库节点树完整、无重复。
- 确认分享权限（open_sharing=open）。
- 最终回复必须包含：知识库链接、内容清单、两天冲刺计划摘要、"分享给同学"的操作说明、邀请用户把卡壳的题干打字发来以便补精讲。

## 时间控制

用户考前时间极紧，全程优先速度：调研≤30min、讲义撰写是大头（直接写，不要反复打磨）、飞书操作串行防错。用户催促时跳过非必要确认，按推荐默认值直接执行。

## 中期增量更新（用户考前进来新资料/参考范本时）

用户可能中途发来：新资料文件夹、别的课的优秀知识库链接要求"参考这个写"。处理原则：

1. **参考范本知识库**：`wiki +node-list --space-id <URL里的space_id>` 读结构 → 提炼可借鉴的组织范式（如：路线图用 callout+考点优先级表+⭐频率标注、emoji 分区容器、讲义编号体系），不要照抄内容。
2. **新增资料按格式分流**（见第三阶段"补充资料的处理方式"表格）：md 笔记直接 import、HTML 转换后 import、PDF/PPT 上传原件。
3. **重组已有知识库**：新建 emoji 容器节点 → `wiki +move --node-token --target-parent-token` 把存量节点归位（保留用户已认可的板块，如"题型训练/加练"，不推倒重来）。
4. **首页升级为复习路线图**：用 `docs +update --command overwrite` 整篇替换（URL 不变，已分享的链接不受影响）。
5. **画图题配图**：若新资料里带样卷完整解答（如其他工具生成的 HTML），提取解析式用 matplotlib 生成标准答案图，`docs +media-insert` 追加进详解文档——画图题光靠文字讲不透。
6. 每次批量操作后**必须去重收尾**（见已知坑2）。
