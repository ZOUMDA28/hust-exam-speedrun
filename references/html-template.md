# 华科考试复习·零基础交互式讲义（HTML 模板）

> 这份是把复习资料用 **交互式单页 HTML** 组织的标准方案。优势：
> 浏览器直接打开（本地或知识库附件），KaTeX 实时渲染公式，可折叠的例题解答，
> 顶部阅读进度 + 侧边锚点导航。考试当天通勤、食堂、考前等候都能"刷"。

---

## 何时使用

- 用户给的学习资料里有 HTML 样例（豆包/Doubao/学长生成的零基础交互式教程）
- 用户明确说"按这个格式做讲义"或"做交互式零基础讲义"
- 时间允许 ≥ 2 小时做讲义（PDF/scanned 资料不可 OCR 时，把文字稿重新组织成此格式比 MD 更友好）

## 输出文件结构

每份讲义单独一个 .html，文件名按章节命名：

```
信号与系统_第N章_第M节_零基础交互式教程.html
```

体积参考：单章讲义 40–70 KB，8 份一周内可完成。

---

## 必须包含的 CSS 体系（直接复用，色系是这套定义）

```css
:root {
  --bg:#f8f6f1; --card:#fff; --ink:#1a1a2e; --ink-soft:#4a4a6a;
  --accent:#2d5a8e; --accent-light:#e8f0fa; --accent2:#c0392b; --accent2-light:#fdecea;
  --green:#27ae60; --green-light:#eafaf1; --orange:#e67e22; --orange-light:#fef5e7;
  --purple:#6c3483; --purple-light:#f4ecf7; --teal:#148f77; --teal-light:#e0f2ef;
  --border:#e0ddd5; --code-bg:#f0ede6;
}
```

## 5 种语义块（必须区分，配色+前缀图标已固定）

| class | 颜色 | 前缀 | 用途 |
|-------|------|------|------|
| `.key` | 绿 | ✅ 核心结论 | 必须记住的定义、定理、重要结论 |
| `.tip` | 蓝 | 💡 提示 | 易混点辨析、知识串联提示 |
| `.warn` | 橙 | ⚠️ 易错点 | 考场常踩的坑、漏写扣分项 |
| `.routine` | 紫 | 🎯 解题套路 | 固定步骤列表，照着套就行 |
| `.example-box` | 框线 | 例题 | 含 `.ex-tag` 标签 + `.collapse` 可折叠解答 |

公式块：

```html
<div class="formula-block">
  <span class="label">连续信号的能量与功率</span>
  $$E = \int_{-\infty}^{\infty}|f(t)|^2 dt$$
  $$P = \lim_{\tau\to\infty}\frac{1}{\tau}\int_{-\tau/2}^{\tau/2}|f(t)|^2 dt$$
</div>
```

## 章节模板

```html
<section class="chapter" id="<anchor>">
  <h2>📶 <章节标题></h2>
  <div class="key">...</div>
  <h3>小节</h3>
  <div class="formula-block">...</div>
  <div class="routine">
    <ol class="steps">
      <li>步骤1</li>
      <li>步骤2</li>
    </ol>
  </div>
  <div class="example-box">
    <span class="ex-tag">例题</span>
    <p><strong>题目：</strong>...</p>
    <div class="collapse" onclick="this.classList.toggle('open')">
      <div class="collapse-head">点击查看解答 <span class="arrow">▶</span></div>
      <div class="collapse-body">
        <p>解答步骤...</p>
        <div class="key">答案</div>
      </div>
    </div>
  </div>
</section>
```

## 必备的 <head>

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"
        onload="renderMath()"></script>
<script>
  function renderMath(){renderMathInElement(document.body,{delimiters:[
    {left:"$$",right:"$$",display:true},{left:"$",right:"$",display:false}
  ]});}
  window.addEventListener('scroll',()=>{
    const sc=document.documentElement.scrollTop;
    const tot=document.documentElement.scrollHeight-window.innerHeight;
    const pct=tot>0?Math.min(100,Math.round(sc/tot*100)):0;
    const el=document.getElementById('progress');
    if(el)el.textContent='阅读进度 '+pct+'%';
  });
</script>
```

## 必备的 <body> 结构

```html
<div class="topbar">
  <h1>📡 <课程章节> · <周次>零基础教程（第N章）</h1>
  <span class="progress" id="progress">阅读进度 0%</span>
</div>
<div class="layout">
  <nav class="sidebar" id="sidebar">
    <div class="nav-group">分组名</div>
    <a href="#anchor">小节名</a>
    ...
  </nav>
  <main class="main">
    <!-- 第一章一定是 roadmap 学习路线图 -->
    <section class="chapter" id="roadmap">
      <h2>🗺️ 学习路线图</h2>
      ...
    </section>
    <!-- 其他章节 -->
  </main>
</div>
```

---

## 章节组织规范（按周次的教程结构）

每份讲义按"周次"对应的章节组织，**第 1 章永远是 🗺️ 学习路线图**：

1. **🗺️ 学习路线图**——本章两/三大核心 + 与相邻章节对比（连续 vs 离散）+ 编号步骤（`<ol class="steps">`）
2. **章节正文**（每个核心概念一节，含公式块 + 表格 + 解题套路）
3. **作业详解**（每道题一个 `<section class="chapter" id="hw-*">`，完整解答 + 折叠展开）
4. **📌 知识图谱与速记**（最终 chapter，含表格 + ⚠️易错点 列表）

---

## 一键生成脚本

`scripts/md_to_html.py` 支持把 markdown 大纲转成此格式（如果你先写 MD 版本规划）
