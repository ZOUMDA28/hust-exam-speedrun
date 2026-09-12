# hust-exam-speedrun

**华科课程考试速通复习资料生成器** —— 一个 [WorkBuddy](https://www.workbuddy.cn/) / Claude Code 风格的 Agent Skill：给考前 1~3 天、零基础的学生，自动把课程资料（样卷、作业解答、课件）整理成「按题型套路组织」的速通讲义，并一键建成可分享的飞书知识库，目标 80+ 分。

## 它能做什么

把一学期的课压缩成考前两天能刷完的拿分套路：

1. **调研样卷** —— 按历年样卷大题反推题型和分值分布，讲义结构 = 考卷结构
2. **按题型写零基础讲义** —— 每个题型一篇：必背公式 → 做题套路（固定步骤）→ 例题精讲（每步算术不跳步）→ 作业同类题索引 → 易错警示
3. **标准讲义集** —— 首页冲刺计划（精确到小时）、公式速查总表（考前 1 小时必看）、零基础预备知识、样卷自测指南、手把手计算细节、加练例题册
4. **搭建飞书知识库** —— 讲义公式渲染为飞书公式块、作业 Word 原件上传（公式完整）、样卷原图入库、开放链接分享给同学

适用于任何一门**有历年样卷和作业答案**的课程，不限专业。

## 安装

### WorkBuddy 用户

```bash
git clone https://github.com/ZOUMDA28/hust-exam-speedrun.git ~/.workbuddy/skills/hust-exam-speedrun
```

重启会话后，说"我要速通 XX 课"即可触发。

### Claude Code 用户

```bash
git clone https://github.com/ZOUMDA28/hust-exam-speedrun.git ~/.claude/skills/hust-exam-speedrun
```

## 使用前提

- 工作区里有课程资料：**样卷**（最关键）、作业解答 docx、课件/总复习提纲
- 飞书已连接（`lark-cli auth status` 可用），用于建知识库

## Skill 结构

```
hust-exam-speedrun/
├── SKILL.md                          # 五阶段主流程（调研→决策→写讲义→建知识库→交付）
├── references/
│   └── lark-cli-cheatsheet.md        # 飞书命令速查 + 实战踩坑记录
└── scripts/
    ├── extract_docx_text.py          # 解包 docx 提取正文+公式文字，建题型索引
    └── import_md_to_wiki.sh          # 批量导入讲义进飞书知识库（防限流）
```

## 实战踩坑记录（已内置到 Skill）

| 坑 | 解法 |
|----|------|
| `drive +import` 导入含 Word 公式的 docx，**公式全部丢失** | 作业答案改用 `drive +upload` 上传原文件；仅 markdown 讲义走 import |
| `import + move` 产生同标题**双份节点** | 导完 `node-list` 查重，删除时 `--obj-type` 必须传 `wiki` |
| Markdown 表格内 LaTeX 竖线 `\|` 截断表格列 | 统一写成 `\vert` |
| 纯扫描版样卷 PDF 提不出文字 | 直接把扫描图上传知识库供自测，不做 OCR |

## 实战案例

2026 春《信号与线性系统》（管致中第六版）：3 小时内产出 14 篇讲义 + 3 页样卷原图 + 8 份作业答案，建成飞书知识库并开放分享，覆盖卷积/傅里叶/拉普拉斯/z 变换/电路建模等全部 7 大题型。

## License

MIT
