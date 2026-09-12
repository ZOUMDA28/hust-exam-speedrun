# lark-cli 飞书命令速查（考试速通知识库场景）

所有命令加 `--as user`（用户身份）。加 `--format json` 拿结构化输出，`-q '.data.token'` 提取字段。

## 认证

```bash
lark-cli auth status
```

## 知识空间

```bash
# 创建知识空间
lark-cli wiki +space-create --as user --name "<课程名>·考前速通80+" --description "<一句话说明>"

# 查看空间信息（含 open_sharing 分享状态）
lark-cli wiki spaces get --as user --space-id <SPACE_ID>

# 更新空间设置（可能需要额外授权，失败就让用户在界面开）
lark-cli api PUT /open-apis/wiki/v2/spaces/<SPACE_ID>/setting --as user --data '{"comment_setting":"allow"}'
```

## 文档导入与移动（markdown 讲义用这条链路）

```bash
# markdown 导入为飞书在线文档（LaTeX $...$ 自动转公式块），返回 .data.token
lark-cli drive +import --as user --type docx --file "<md路径>" --name "<文档标题>" --format json

# 移入知识空间
lark-cli wiki +move --as user --obj-type docx --obj-token <TOKEN> --target-space-id <SPACE_ID>

# ⚠️ import+move 后 node-list 可能出现同标题双节点，删多余那份（见下方 node-delete）
```

## 文件上传（作业 docx 原件、样卷扫描图用这条链路）

```bash
# 上传到知识库某节点下（保留 Word 公式，可下载）
lark-cli drive +upload --as user --file "<文件路径>" --name "<显示名>" --wiki-token <NODE_TOKEN>

# 先创建容器节点：
lark-cli wiki +node-create --as user --space-id <SPACE_ID> --title "<节点标题>" --obj-type docx
```

## 节点管理

```bash
# 列出节点（可加 --parent-node-token 列子节点）
lark-cli wiki +node-list --as user --space-id <SPACE_ID> --format json

# 查看节点详情（拿 URL 用）
lark-cli wiki +node-get --as user --node-token <NODE_TOKEN>

# 删除节点 —— ⚠️ obj-type 必须传 wiki（传 docx 报"节点不存在"）
lark-cli wiki +node-delete --as user --space-id <SPACE_ID> --node-token <NODE_TOKEN> --obj-type wiki --yes
```

## 文档读取与编辑（验证公式渲染用）

```bash
# 读文档 markdown（公式会渲染成 LaTeX 文本，可肉眼检查）
lark-cli docs +fetch --as user --doc <OBJ_TOKEN> --doc-format markdown --format json -q '.data.document.content'

# 文字替换（修首页目录等小改）
lark-cli docs +update --as user --doc <OBJ_TOKEN> --command str_replace --pattern "<旧文本>" --content "<新文本>"

# 整篇替换内容（URL不变，md文件用@引用）
lark-cli docs +update --as user --doc <OBJ_TOKEN> --command overwrite --doc-format markdown --content "@/path/to/new.md"

# 追加内容到文档末尾
lark-cli docs +update --as user --doc <OBJ_TOKEN> --command append --doc-format markdown --content "<md片段>"

# 插入图片到文档末尾（带图注）
lark-cli docs +media-insert --as user --doc <OBJ_TOKEN> --file <png> --type image --caption "图N｜说明" --width 600

# 删除云空间里的文档
lark-cli drive +delete --as user --file-token <TOKEN> --type docx --yes
```

## 节点挂载与改标题

```bash
# 把已有节点挂到父节点下（分区归档用）
lark-cli wiki +move --as user --node-token <NODE> --target-parent-token <PARENT_NODE>

# 改文档标题（lark-cli api 不支持query string，直接PATCH）
lark-cli api PATCH /open-apis/drive/v1/files/<OBJ_TOKEN> --as user --data '{"title": "新标题", "type": "docx"}'
```

## 去重收尾（必做）

import+move 和 upload--wiki-token **每次都产生双份节点**。收尾时按 parent `node-list`，用 python 按 title 分组找重复对，逐个删除（保留含图片/正确 obj_token 的那份）：

```bash
lark-cli wiki +node-delete --as user --space-id <SPACE> --node-token <DUP> --obj-type wiki --yes
```

## 限流注意

批量操作每条命令之间 `sleep 1`；导入失败重试一次；节点列表有 `has_more` 分页。
