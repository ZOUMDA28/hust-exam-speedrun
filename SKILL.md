---
name: hust-exam-speedrun
description: "华科课程考试速通复习资料生成器：从零基础到 80+ 分。当用户几天内要考试、要求'速通/速成/抱佛脚'复习、把课程资料（课件 PDF、作业解答 docx、样卷、总复习提纲）整理成讲义或飞书知识库时触发。覆盖完整工作流：调研样卷确定题型 → 按题型写零基础讲义（必背公式/做题套路/例题精讲/作业索引）→ 搭建飞书知识库并开放分享。适用于任何一门有历年样卷和作业答案的课程。"
agent_created: true
---

# 华科考试速通复习资料生成（讲义 + 飞书知识库）

## 目标

为一名零基础、考前 1~3 天的学生，产出「按题型套路组织」的速通讲义，并建成可分享的飞书知识库，目标 80+ 分。全程以最快路径执行，不追求系统性、只追求拿分。

## 总流程（按序执行）

```
调研资料(≤30min) → 问4个决策问题 → 写讲义markdown → 搭飞书知识库 → 验证公式渲染 → 开放分享 → 交付链接
```

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

## 第三阶段：撰写讲义 markdown

统一放在 `.workbuddy/wiki_md/` 目录，文件名用 `数字-名称.md` 控制排序。**推荐知识库结构**（经两门课实战验证，参考优秀范本）：

```
🚀 复习路线图（必看）        ← 首页：callout考试信息 + 考点优先级表(⭐+分值+对应讲义) + 时间表 + 80+策略 + 目录
├── 📚 零基础入门与公式速查   ← 零基础预备 / 公式速查总表 / 学长笔记(如有md原件直接import) / 零基础详解Part系列 / 手把手计算细节
├── ✍️ 题型训练与加练        ← 题型一~N讲义 / 加练例题册 / 💯样卷完整手写详解(含标准答案图) / 样卷自测指南
└── 📎 作业答案与原始资料     ← 作业答案Word原文件 / 作业答案PDF(如有) / 样卷原图 / 总复习PPT/PDF
```

- 分区容器节点用 emoji 开头命名（📚✍️📎），内部讲义按内容归位。容器用 `wiki +node-create` 创建，子节点用 `wiki +move --node-token X --target-parent-token Y` 挂进去。
- **考点优先级表是路线图灵魂**：每行=优先级(⭐⭐⭐) + 考点 + 分值 + 对应讲义名，让用户一眼知道 80% 时间投哪里。
- 复习时间表精确到半天/时段，最后一段永远是"考前早晨只看公式表"。

### 题型讲义统一模板

```markdown
# 题型N｜XXX（约XX分）

## 一、必背公式
（LaTeX 公式块，每条配一句大白话解释"这是什么、什么时候用"）

## 二、做题套路（固定步骤）
步骤1：……
步骤2：……
（编号步骤，傻瓜式，照着做就能拿分）

## 三、例题精讲
【例】题目
**第1步**：（写出这一步用的公式）
计算过程……（每步算术都写出来，零基础不跳步）
**答案**：……

## 四、作业同类题
这类题 = 第X周作业第Y题（知识库"作业答案"节点里看）

## 五、易错警示
（阅卷得分点、常见丢分写法）
```

### 写作硬性要求

- 用户自称零基础时，**每一步算术都展开**（复数取模、通分、指数运算都要写），宁多勿少。
- 例题优先取自作业题（有官方答案可对照），其次教材典型题；样卷是扫描件读不了就用前者并如实告知。
- 公式一律用 `$...$` / `$$...$$` LaTeX，飞书导入会自动转成公式块。
- **表格单元格内的公式不要用竖线 `|`**（如求值记号 `\big|_{s=jω}`），必须写成 `\vert`，否则 Markdown 表格列被截断。

### 画图题标准答案图（强烈推荐）

频谱图/幅频曲线/波形图类题目，纯文字讲不透——**用 matplotlib 直接生成标准答案图**并插入飞书文档：

1. 从样卷解答中提取每道画图题的解析式（频谱=stem图，幅频曲线=plot+关键点标注）。
2. 生成 PNG（150dpi，中文字体 `Microsoft YaHei`；**注意下标字符如 ₄/₀ 在雅黑里缺字**，写成普通数字）。
3. 插入：`lark-cli docs +media-insert --as user --doc <obj_token> --file <png> --type image --caption "图N｜说明" --width 600`（只能追加到文档末尾，图集章节放文档尾部）。
4. 典型图代码要点：频谱图用 `ax.stem`+逐点 `annotate` 数值；幅频曲线标 3 个关键点（起点/极值/终点）。

### 补充资料的处理方式（按格式分流）

| 资料格式 | 处理方式 |
|---|---|
| 学长/同学的 md 笔记（含 LaTeX） | `drive +import` 直接导入，公式渲染完好，归入📚分区 |
| HTML 讲义（其他AI/工具产物） | 写转换器提为 md（保留 h1-h4/表格/公式块class语义→引用块）再 import；或当原始文件上传 |
| PDF/PPT 原件 | `drive +upload --wiki-token` 上传原件到📎分区，不做转换 |
| HTML 转换器要点 | 表格先正则提 `<tr>/<td>` 转管道表；`class="formula/tip/warning/answer"` 的 div 转 `> 📐/💡/⚠️/✅` 引用块；h1-h4 映射 ##~##### |

## 第四阶段：搭建飞书知识库

前置：`lark-cli auth status` 确认已登录。详细命令见 `references/lark-cli-cheatsheet.md`。

流程（串行执行，每步之间 sleep 1 防限流）：

1. 创建知识空间：`lark-cli wiki +space-create --as user --name "<课程名>·考前速通80+"`
2. 逐篇导入讲义：`lark-cli drive +import --as user --type docx --file <md> --name <标题>` 得到 token，再 `lark-cli wiki +move --as user --obj-type docx --obj-token <tok> --target-space-id <space>` 挪入库
3. 创建容器节点放样卷扫描图，`lark-cli drive +upload --wiki-token <节点>` 传图
4. 作业 docx **直接上传原文件**（见下方"已知坑"），不要用 import
5. 开放分享：先 `lark-cli wiki spaces get` 看 `open_sharing`；若未开，尝试 `lark-cli api PUT /open-apis/wiki/v2/spaces/<id>/setting`，仍不行则指引用户在飞书界面开（知识库设置→开启公开分享）
6. `lark-cli wiki +node-list` 检查结构，用 `lark-cli wiki +node-get` 拿首页 URL 交付

### 已知坑（实战踩过，务必避开）

1. **docx import 丢 Word 公式**：`drive +import` 导入含 OMML 公式的作业 docx 后公式全部丢失（文字在、公式空）。解法：作业答案**上传原 .docx 文件**（`drive +upload`，公式完整可下载）；只有自己写的 markdown 讲义才走 import（md 里的 LaTeX 能正确转公式块）。
2. **import+move 必产生双份节点**（不是偶发，是每次都双份）：`drive +import` 后 `wiki +move --obj-type docx --obj-token` 进库，节点列表会出现同标题 2 个 node；`drive +upload --wiki-token` 同样双份。**收尾必须去重**：按 parent `node-list` 分组找同标题对，`wiki +node-delete --obj-type wiki`（传 docx 报"节点不存在"）删掉一份。含插入图片的文档要保留 obj_token 与 import 返回值一致的那份。
3. **先小规模试跑**：先导入 1 篇讲义 → `docs +fetch --doc-format markdown` 抽查公式渲染 → 确认无误再批量。发现问题（如表格竖线）先改源 md 重新导。
4. **删除测试文档**：`drive +delete --file-token <tok> --type docx --yes`。
5. **整篇替换文档内容**：`docs +update --doc <obj_token> --command overwrite --doc-format markdown --content "@<md文件>"`（内容全换、URL 不变）；标题改名走 `lark-cli api PATCH /open-apis/drive/v1/files/<obj_token>`（body 带 title+type，lark-cli 不支持 query string）。
6. **节点挂到父节点**：`wiki +move --node-token X --target-parent-token Y`（不带 --obj-type/--obj-token，那是 doc→wiki 模式）。
7. **图片只追加到文档末尾**：`docs +media-insert` 无位置参数，图集章节放文档尾部；`--caption` 写图注。
8. **matplotlib 中文**：`plt.rcParams['font.sans-serif']=['Microsoft YaHei']`；下标 unicode（₄₀等）缺字，用普通数字。

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
