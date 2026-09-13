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

## 完整 CSS 样式（所有语义块 + 布局，直接复制到 `<style>` 中）

```css
/* ===== 基础布局 ===== */
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: -apple-system, "Microsoft YaHei", sans-serif; background: var(--bg); color: var(--ink); line-height: 1.7; }
.topbar { position: sticky; top: 0; z-index: 100; background: var(--card); border-bottom: 1px solid var(--border); padding: 12px 24px; display: flex; justify-content: space-between; align-items: center; box-shadow: 0 2px 8px rgba(0,0,0,0.06); }
.topbar h1 { font-size: 18px; color: var(--accent); }
.progress { font-size: 13px; color: var(--ink-soft); background: var(--accent-light); padding: 4px 12px; border-radius: 12px; }
.layout { display: flex; max-width: 1200px; margin: 0 auto; }
.sidebar { width: 240px; position: sticky; top: 60px; height: calc(100vh - 60px); overflow-y: auto; padding: 20px 16px; border-right: 1px solid var(--border); font-size: 14px; }
.sidebar .nav-group { font-weight: bold; color: var(--accent); margin-top: 16px; margin-bottom: 8px; font-size: 13px; text-transform: uppercase; letter-spacing: 1px; }
.sidebar a { display: block; padding: 6px 12px; color: var(--ink-soft); text-decoration: none; border-radius: 6px; margin-bottom: 2px; }
.sidebar a:hover { background: var(--accent-light); color: var(--accent); }
.main { flex: 1; padding: 30px 40px; min-width: 0; }
.chapter { margin-bottom: 40px; }
.chapter h2 { color: var(--accent); border-bottom: 2px solid var(--accent); padding-bottom: 8px; margin-bottom: 20px; font-size: 22px; }
.chapter h3 { color: var(--ink); margin-top: 24px; margin-bottom: 12px; font-size: 18px; }
p { margin-bottom: 12px; }

/* ===== 5 种核心语义块 ===== */
.key, .tip, .warn, .routine { padding: 14px 18px; border-radius: 8px; margin: 14px 0; border-left: 4px solid; }
.key { background: var(--green-light); border-color: var(--green); }
.tip { background: var(--accent-light); border-color: var(--accent); }
.warn { background: var(--orange-light); border-color: var(--orange); }
.routine { background: var(--purple-light); border-color: var(--purple); }
.key strong { color: var(--green); }
.tip strong { color: var(--accent); }
.warn strong { color: var(--orange); }
.routine strong { color: var(--purple); }

/* ===== 新增语义块 ===== */
/* .kp - 知识点小标签 */
.kp { display: inline-block; background: var(--purple-light); color: var(--purple); font-size: 12px; padding: 2px 10px; border-radius: 12px; font-weight: 600; margin-right: 8px; vertical-align: middle; }

/* .sol-step - 分步解答 */
.sol-step { display: flex; gap: 12px; margin: 12px 0; padding: 12px 16px; background: var(--card); border-left: 4px solid var(--accent); border-radius: 0 8px 8px 0; box-shadow: 0 1px 3px rgba(0,0,0,0.06); }
.sol-step .step-num { flex-shrink: 0; width: 28px; height: 28px; background: var(--accent); color: #fff; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold; font-size: 14px; }
.sol-step .step-content { flex: 1; }
.sol-step .step-content p { margin-top: 6px; }

/* .formula-block - 公式块 */
.formula-block { background: var(--accent-light); padding: 16px 20px; border-radius: 8px; margin: 14px 0; position: relative; }
.formula-block .label { display: inline-block; background: var(--accent); color: #fff; font-size: 12px; padding: 3px 10px; border-radius: 4px; font-weight: 600; margin-bottom: 10px; }

/* .checklist - 勾选清单 */
.checklist { list-style: none; padding: 0; margin: 14px 0; }
.checklist li { padding: 8px 12px; margin-bottom: 4px; background: var(--card); border-radius: 6px; border: 1px solid var(--border); transition: background 0.2s; }
.checklist li:hover { background: var(--accent-light); }
.checklist input[type="checkbox"] { margin-right: 10px; cursor: pointer; }
.checklist label { cursor: pointer; display: flex; align-items: center; }
.checklist li:has(input:checked) { background: var(--green-light); text-decoration: line-through; opacity: 0.7; }

/* .tag - 标签系统 */
.tag { display: inline-block; font-size: 12px; padding: 3px 10px; border-radius: 4px; font-weight: 600; margin-right: 6px; }
.tag-must { background: var(--accent2-light); color: var(--accent2); }
.tag-aim { background: var(--orange-light); color: var(--orange); }

/* .card - 卡片容器 */
.card { background: var(--card); border-radius: 10px; padding: 20px; margin: 16px 0; box-shadow: 0 2px 8px rgba(0,0,0,0.06); border: 1px solid var(--border); }
.card h4 { color: var(--accent); margin-bottom: 10px; font-size: 16px; }

/* .timer-table - 倒计时时间表 */
.timer-table { width: 100%; border-collapse: collapse; margin: 14px 0; }
.timer-table th, .timer-table td { padding: 10px 14px; text-align: left; border-bottom: 1px solid var(--border); }
.timer-table th { background: var(--accent); color: #fff; font-weight: 600; }
.timer-table tr:hover { background: var(--accent-light); }
.timer-table .time-col { width: 120px; font-weight: 600; color: var(--accent); }

/* ===== 例题盒 + 折叠 ===== */
.example-box { border: 1px solid var(--border); border-radius: 10px; padding: 16px 20px; margin: 16px 0; background: var(--card); position: relative; }
.example-box .ex-tag { position: absolute; top: -10px; left: 16px; background: var(--accent); color: #fff; font-size: 12px; padding: 2px 12px; border-radius: 4px; font-weight: 600; }
.collapse { margin-top: 12px; border: 1px dashed var(--border); border-radius: 6px; overflow: hidden; cursor: pointer; }
.collapse-head { padding: 10px 16px; background: var(--code-bg); font-size: 14px; color: var(--ink-soft); display: flex; justify-content: space-between; align-items: center; }
.collapse .arrow { transition: transform 0.3s; }
.collapse.open .arrow { transform: rotate(90deg); }
.collapse-body { max-height: 0; overflow: hidden; transition: max-height 0.3s ease; padding: 0 16px; }
.collapse.open .collapse-body { max-height: 5000px; padding: 12px 16px; }

/* ===== 表格 ===== */
table { width: 100%; border-collapse: collapse; margin: 14px 0; }
th, td { padding: 10px 14px; border: 1px solid var(--border); text-align: left; }
th { background: var(--accent-light); color: var(--accent); font-weight: 600; }

/* ===== 响应式 ===== */
@media (max-width: 768px) {
  .sidebar { display: none; }
  .main { padding: 20px 16px; }
  .topbar { padding: 10px 16px; }
  .topbar h1 { font-size: 15px; }
}
```

## 10 种语义块（必须区分，配色+前缀图标已固定）

| class | 颜色 | 前缀 | 用途 |
|-------|------|------|------|
| `.key` | 绿 | ✅ 核心结论 | 必须记住的定义、定理、重要结论 |
| `.tip` | 蓝 | 💡 提示 | 易混点辨析、知识串联提示 |
| `.warn` | 橙 | ⚠️ 易错点 | 考场常踩的坑、漏写扣分项 |
| `.routine` | 紫 | 🎯 解题套路 | 固定步骤列表，照着套就行 |
| `.example-box` | 框线 | 例题 | 含 `.ex-tag` 标签 + `.collapse` 可折叠解答 |
| `.kp` | 紫小标签 | 无（内嵌） | **知识点标签**：紫色圆角小标签，内嵌在解答步骤旁标注所用公式/考点 |
| `.sol-step` | 蓝左边框 | 步骤编号 | **解题步骤**：蓝色左边框分步卡片，每步配 .kp 知识点标注 |
| `.formula-block` | 浅蓝背景 | label标签 | **公式块**：带 label 标签的公式展示块，可容纳多个公式 |
| `.checklist` | 勾选框 | ☐/☑ | **勾选清单**：用于冲刺计划/复习清单，可交互勾选 |
| `.tag` + `.tag-must`/`.tag-aim` | 红/橙底 | 文字标签 | **难度/重要性标签**：.tag-must 必考(红)、.tag-aim 目标分(橙) |

公式块：

```html
<div class="formula-block">
  <span class="label">连续信号的能量与功率</span>
  $$E = \int_{-\infty}^{\infty}|f(t)|^2 dt$$
  $$P = \lim_{\tau\to\infty}\frac{1}{\tau}\int_{-\tau/2}^{\tau/2}|f(t)|^2 dt$$
</div>
```

知识点标签 + 分步解答：

```html
<div class="sol-step">
  <span class="step-num">1</span>
  <div class="step-content">
    <span class="kp">能量公式</span>
    <p>根据能量定义，代入信号表达式：</p>
    $$E = \int_{-\infty}^{\infty}|f(t)|^2 dt$$
  </div>
</div>
```

难度/重要性标签：

```html
<span class="tag tag-must">必考</span>
<span class="tag tag-aim">目标80+</span>
```

勾选清单：

```html
<ul class="checklist">
  <li><label><input type="checkbox"> 完成第1章公式背诵</label></li>
  <li><label><input type="checkbox" checked> 做完2023年真题</label></li>
</ul>
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

## 自测题集模板（example-box + collapse）

```html
<section class="chapter" id="self-test">
  <h2>📝 自测题集 <span class="tag tag-must">共20题</span></h2>

  <div class="tip">
    <strong>使用说明：</strong>先自己做，做完再点"查看解答"对答案。每道题都标注了考点和难度。
  </div>

  <h3>一、选择题（5题）</h3>

  <div class="example-box">
    <span class="ex-tag">第1题</span>
    <span class="tag tag-must">必考</span>
    <span class="kp">数据表示</span>
    <p><strong>题目：</strong>……</p>
    <p>A. ……　B. ……　C. ……　D. ……</p>
    <div class="collapse" onclick="this.classList.toggle('open')">
      <div class="collapse-head">点击查看解答 <span class="arrow">▶</span></div>
      <div class="collapse-body">
        <div class="sol-step">
          <span class="step-num">1</span>
          <div class="step-content">
            <span class="kp">考点：补码表示</span>
            <p>分析题干……</p>
          </div>
        </div>
        <div class="sol-step">
          <span class="step-num">2</span>
          <div class="step-content">
            <span class="kp">公式：补码转换</span>
            <p>计算过程……</p>
          </div>
        </div>
        <div class="key">答案：C</div>
      </div>
    </div>
  </div>

  <h3>二、填空题（5题）</h3>
  <!-- 同上结构 -->

  <h3>三、综合计算题（10题）</h3>
  <!-- 同上结构 -->
</section>
```

---

## 综合精讲模板（五大题型套路与真题精讲）

文件名：`计基_综合_五大题型套路与真题精讲.html`

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <title>计算机系统基础·综合精讲</title>
  <!-- 此处插入 KaTeX + CSS（参考上方完整CSS样式） -->
</head>
<body>
<div class="topbar">
  <h1>🎯 计算机系统基础 · 五大题型套路与真题精讲</h1>
  <span class="progress" id="progress">阅读进度 0%</span>
</div>
<div class="layout">
  <nav class="sidebar">
    <div class="nav-group">总览</div>
    <a href="#overview">考试概况</a>
    <a href="#distribution">分值分布</a>
    <div class="nav-group">五大题型</div>
    <a href="#type1">题型一：数据表示</a>
    <a href="#type2">题型二：汇编语言</a>
    <a href="#type3">题型三：栈帧与过程</a>
    <a href="#type4">题型四：链接与加载</a>
    <a href="#type5">题型五：异常与IO</a>
    <div class="nav-group">真题精讲</div>
    <a href="#exam-2023">2023年真题详解</a>
    <a href="#exam-2024">2024年真题详解</a>
    <div class="nav-group">自测</div>
    <a href="#self-test">自测题集（20题）</a>
    <a href="#formula">必背公式速查</a>
  </nav>
  <main class="main">

    <section class="chapter" id="overview">
      <h2>📋 考试概况</h2>
      <div class="card">
        <h4>考试信息</h4>
        <table>
          <tr><th>项目</th><th>内容</th></tr>
          <tr><td>考试时长</td><td>120分钟</td></tr>
          <tr><td>满分</td><td>100分</td></tr>
          <tr><td>题型数量</td><td>5道大题</td></tr>
          <tr><td>难度</td><td>中等偏上</td></tr>
        </table>
      </div>
    </section>

    <section class="chapter" id="distribution">
      <h2>📊 分值分布与考点频率</h2>
      <div class="card">
        <h4>五大题型分值占比</h4>
        <table>
          <tr><th>题型</th><th>分值</th><th>难度</th><th>优先级</th></tr>
          <tr><td>数据表示</td><td>20分</td><td>⭐⭐</td><td><span class="tag tag-must">必拿分</span></td></tr>
          <tr><td>汇编语言</td><td>20分</td><td>⭐⭐⭐</td><td><span class="tag tag-must">必考</span></td></tr>
          <tr><td>栈帧与过程</td><td>20分</td><td>⭐⭐⭐</td><td><span class="tag tag-must">必考</span></td></tr>
          <tr><td>链接与加载</td><td>20分</td><td>⭐⭐⭐⭐</td><td><span class="tag tag-aim">目标80+</span></td></tr>
          <tr><td>异常与IO</td><td>20分</td><td>⭐⭐⭐⭐</td><td><span class="tag tag-aim">目标80+</span></td></tr>
        </table>
      </div>
    </section>

    <!-- 每个题型一个 section，套路+公式+真题示例 -->
    <section class="chapter" id="type1">
      <h2>📐 题型一：数据表示</h2>
      <div class="key"><strong>题型特征：</strong>给出一个数，在不同表示法之间转换</div>
      <div class="formula-block">
        <span class="label">核心公式</span>
        $$公式1$$
        $$公式2$$
      </div>
      <div class="routine">
        <p><strong>解题套路：</strong></p>
        <ol class="steps">
          <li>步骤1</li>
          <li>步骤2</li>
          <li>步骤3</li>
        </ol>
      </div>
      <h3>真题示例</h3>
      <div class="example-box">
        <span class="ex-tag">2023真题</span>
        <span class="tag tag-must">必考</span>
        <p><strong>题目：</strong>……</p>
        <div class="collapse" onclick="this.classList.toggle('open')">
          <div class="collapse-head">点击查看解答 <span class="arrow">▶</span></div>
          <div class="collapse-body">
            <div class="sol-step">
              <span class="step-num">1</span>
              <div class="step-content"><span class="kp">知识点</span><p>……</p></div>
            </div>
            <div class="key">答案：……</div>
          </div>
        </div>
      </div>
    </section>

    <!-- 题型二到五同上结构... -->

    <section class="chapter" id="self-test">
      <h2>📝 自测题集</h2>
      <!-- 插入自测题集模板（见上方） -->
    </section>

    <section class="chapter" id="formula">
      <h2>📌 必背公式速查表</h2>
      <div class="card">
        <!-- 所有核心公式汇总 -->
      </div>
    </section>

  </main>
</div>
</body>
</html>
```

---

## 冲刺计划模板（精确到小时的时间表）

文件名：`计基_冲刺计划_XX月XX-XX日.html`

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <title>计基冲刺计划</title>
  <!-- 此处插入 KaTeX + CSS -->
</head>
<body>
<div class="topbar">
  <h1>⏰ 计算机系统基础 · 考前冲刺计划</h1>
  <span class="progress" id="progress">阅读进度 0%</span>
</div>
<div class="layout">
  <nav class="sidebar">
    <div class="nav-group">总览</div>
    <a href="#countdown">倒计时总览</a>
    <a href="#materials">资料清单</a>
    <div class="nav-group">Day 1</div>
    <a href="#day1-am">上午：数据表示+汇编</a>
    <a href="#day1-pm">下午：栈帧+链接</a>
    <a href="#day1-eve">晚上：真题模拟</a>
    <div class="nav-group">Day 2</div>
    <a href="#day2-am">上午：查漏补缺</a>
    <a href="#day2-pm">下午：错题回顾</a>
    <a href="#day2-eve">晚上：公式速通</a>
    <div class="nav-group">策略</div>
    <a href="#priority">刷题优先级</a>
    <a href="#checklist">完成清单</a>
  </nav>
  <main class="main">

    <section class="chapter" id="countdown">
      <h2>⏳ 倒计时总览</h2>
      <table class="timer-table">
        <tr><th>天数</th><th>日期</th><th>可用小时</th><th>核心任务</th><th>目标</th></tr>
        <tr><td>Day 1</td><td>XX月XX日</td><td class="time-col">10h</td><td>五大题型过一遍 + 1套真题</td><td>建立知识框架</td></tr>
        <tr><td>Day 2</td><td>XX月XX日</td><td class="time-col">8h</td><td>错题回顾 + 公式速背 + 策略</td><td>上考场状态</td></tr>
      </table>
    </section>

    <section class="chapter" id="materials">
      <h2>📚 资料清单与优先级</h2>
      <ul class="checklist">
        <li><label><input type="checkbox"> <span class="tag tag-must">必看</span> 历年真题（11套）</label></li>
        <li><label><input type="checkbox"> <span class="tag tag-must">必看</span> 综合精讲HTML讲义</label></li>
        <li><label><input type="checkbox"> <span class="tag tag-must">必看</span> 作业解答（5次）</label></li>
        <li><label><input type="checkbox"> <span class="tag tag-aim">选做</span> 课后习题</label></li>
        <li><label><input type="checkbox"> <span class="tag tag-aim">选看</span> 课件PPT</label></li>
      </ul>
    </section>

    <section class="chapter" id="day1-am">
      <h2>🌅 Day 1 · 上午（8:00-12:00）</h2>
      <table class="timer-table">
        <tr><th>时间</th><th>任务</th><th>资料</th><th>验收标准</th></tr>
        <tr><td class="time-col">8:00-9:00</td><td>数据表示题型精讲</td><td>综合精讲 p1</td><td>能独立完成3道转换题</td></tr>
        <tr><td class="time-col">9:00-10:30</td><td>汇编语言题型精讲</td><td>综合精讲 p2</td><td>能看懂常见指令序列</td></tr>
        <tr><td class="time-col">10:30-12:00</td><td>栈帧与过程</td><td>综合精讲 p3</td><td>能画出栈帧结构图</td></tr>
      </table>
      <div class="tip"><strong>提醒：</strong>每学完一个题型，立刻做2道真题验证掌握程度。</div>
    </section>

    <!-- Day 1 下午、晚上，Day 2 全天... 同上结构 -->

    <section class="chapter" id="priority">
      <h2>🎯 刷题优先级排序</h2>
      <div class="routine">
        <p><strong>优先级从高到低：</strong></p>
        <ol class="steps">
          <li><strong>近3年真题</strong>（题型最接近，必须全部吃透）</li>
          <li><strong>作业题</strong>（老师出题风格参考）</li>
          <li><strong>综合精讲例题</strong>（典型题型，掌握套路）</li>
          <li><strong>自测题集</strong>（查漏补缺）</li>
          <li><strong>课后习题</strong>（时间充裕再做）</li>
        </ol>
      </div>
    </section>

    <section class="chapter" id="checklist">
      <h2>✅ 完成清单</h2>
      <ul class="checklist">
        <li><label><input type="checkbox"> 五大题型套路全部过一遍</label></li>
        <li><label><input type="checkbox"> 做完3套真题（限时）</label></li>
        <li><label><input type="checkbox"> 错题全部搞懂</label></li>
        <li><label><input type="checkbox"> 必背公式能默写</label></li>
        <li><label><input type="checkbox"> 易错点TOP20过一遍</label></li>
      </ul>
    </section>

  </main>
</div>
</body>
</html>
```

---

## 考前速通模板（考前1-2天抱佛脚）

文件名：`考前速通冲刺指南.html`

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <title>考前速通冲刺指南</title>
  <!-- 此处插入 KaTeX + CSS -->
</head>
<body>
<div class="topbar">
  <h1>🚀 考前速通冲刺指南 · 计算机系统基础</h1>
  <span class="progress" id="progress">阅读进度 0%</span>
</div>
<div class="layout">
  <nav class="sidebar">
    <div class="nav-group">考前必读</div>
    <a href="#overview">考试概况</a>
    <a href="#strategy">考场策略</a>
    <div class="nav-group">Day 1 攻坚</div>
    <a href="#day1-core">核心考点地毯式</a>
    <a href="#day1-practice">实战刷题</a>
    <div class="nav-group">Day 2 冲刺</div>
    <a href="#day2-mock">真题模拟</a>
    <a href="#day2-review">错题查漏</a>
    <div class="nav-group">速查手册</div>
    <a href="#formulas">必背公式 TOP 30</a>
    <a href="#mistakes">易错点 TOP 20</a>
    <a href="#exam-tips">考场技巧</a>
  </nav>
  <main class="main">

    <section class="chapter" id="overview">
      <h2>📋 考试概况</h2>
      <div class="card">
        <h4>快速了解考试</h4>
        <table>
          <tr><th>项目</th><th>详情</th></tr>
          <tr><td>考试时间</td><td>XX月XX日 XX:XX-XX:XX（120分钟）</td></tr>
          <tr><td>考试地点</td><td>东XX楼 XXX教室</td></tr>
          <tr><td>考试题型</td><td>5道大题，每题20分</td></tr>
          <tr><td>携带物品</td><td>学生证、身份证、计算器（如需）、笔</td></tr>
          <tr><td>及格线</td><td>60分</td></tr>
        </table>
      </div>
      <div class="warn">
        <strong>注意：</strong>提前30分钟到达考场，不要迟到！
      </div>
    </section>

    <section class="chapter" id="day1-core">
      <h2>🔥 Day 1 · 核心考点地毯式攻坚</h2>
      <div class="key"><strong>目标：</strong>把所有核心考点过一遍，建立完整知识框架</div>
      <h3>上午：三大基础题型</h3>
      <div class="card">
        <h4>8:00-10:00 数据表示 <span class="tag tag-must">必拿分</span></h4>
        <ul>
          <li>补码/移码/反码转换</li>
          <li>浮点数表示（IEEE 754）</li>
          <li>大小端与字节序</li>
        </ul>
      </div>
      <div class="card">
        <h4>10:00-12:00 汇编语言 <span class="tag tag-must">必考</span></h4>
        <ul>
          <li>常见指令（mov/add/sub/push/pop/call/ret）</li>
          <li>条件码与跳转</li>
          <li>寻址方式</li>
        </ul>
      </div>
      <!-- 下午、晚上类似结构 -->
    </section>

    <!-- Day 2 冲刺... -->

    <section class="chapter" id="formulas">
      <h2>📐 必背公式 TOP 30</h2>
      <div class="tip"><strong>使用方法：</strong>遮住答案，自己先想，想不出来再看。考前1小时再过一遍。</div>
      <div class="formula-block">
        <span class="label">1. 补码范围</span>
        $$n位补码范围：-2^{n-1} \sim 2^{n-1} - 1$$
      </div>
      <div class="formula-block">
        <span class="label">2. 浮点数规格化</span>
        $$(-1)^s \times 1.f \times 2^{e-bias}$$
      </div>
      <!-- 更多公式... -->
    </section>

    <section class="chapter" id="mistakes">
      <h2>⚠️ 易错点 TOP 20</h2>
      <div class="warn">
        <strong>易错点1：</strong>补码的最小值没有对应的正数表示（-128 在8位补码中无法取反+1得到正数）
      </div>
      <div class="warn">
        <strong>易错点2：</strong>小端模式下，低地址存低字节，高地址存高字节（不要搞反）
      </div>
      <!-- 更多易错点... -->
    </section>

    <section class="chapter" id="exam-tips">
      <h2>🎯 考场策略</h2>
      <div class="routine">
        <p><strong>答题顺序（推荐）：</strong></p>
        <ol class="steps">
          <li><strong>先扫全卷</strong>（5分钟）：看看5道题分别考什么，心里有底</li>
          <li><strong>先做会的</strong>：数据表示 → 汇编 → 栈帧，保证基础分拿满</li>
          <li><strong>再啃难的</strong>：链接 → 异常，能写多少写多少</li>
          <li><strong>最后检查</strong>（15分钟）：重点检查计算错误和单位</li>
        </ol>
      </div>
      <div class="tip">
        <strong>时间分配建议：</strong>每道大题约20分钟，不会的题先跳过，最后回来补。
      </div>
      <div class="key">
        <strong>核心原则：</strong>会做的题一定要做对，不会的题尽量写步骤拿过程分。
      </div>
    </section>

  </main>
</div>
</body>
</html>
```

---

## 一键生成脚本

`scripts/md_to_html.py` 支持把 markdown 大纲转成此格式（如果你先写 MD 版本规划）
