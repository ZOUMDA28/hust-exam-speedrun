#!/bin/bash
# 批量把 markdown 讲义导入飞书并移入知识库（串行 + 防限流）
# 用法: bash import_md_to_wiki.sh <SPACE_ID> <清单文件>
# 清单文件每行格式: <md相对路径>|<飞书文档标题>
set -u
SPACE="$1"
LIST="$2"
FAIL=0

while IFS='|' read -r f t; do
  [ -z "$f" ] && continue
  tok=$(lark-cli drive +import --as user --type docx --file "$f" --name "$t" --format json -q '.data.token' 2>/dev/null)
  if [ -z "$tok" ] || [ "$tok" = "null" ]; then
    echo "IMPORT_FAIL|$t"; FAIL=1; continue
  fi
  mv=$(lark-cli wiki +move --as user --obj-type docx --obj-token "$tok" --target-space-id "$SPACE" --format json 2>/dev/null | grep -c '"ok": true')
  if [ "$mv" -ge 1 ]; then
    echo "OK|$t|$tok"
  else
    echo "MOVE_FAIL|$t|$tok"; FAIL=1
  fi
  sleep 1
done < "$LIST"

# ⚠️ 已知问题: import+move 可能产生同标题双节点，导入完成后必须
#    node-list 检查重复；删除用 --obj-type wiki（不是 docx）
exit $FAIL
