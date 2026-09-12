#!/usr/bin/env python3
"""解包 docx 提取文本（正文 <w:t> + Word 公式 <m:t>），用于快速了解作业内容、建题型索引。

用法:
    python extract_docx_text.py <file1.docx> [file2.docx ...]
    python extract_docx_text.py "*.docx"          # 支持 glob
    python extract_docx_text.py <file.docx> -o out.txt  # 写入文件

docx 本质是 zip；word/document.xml 中 <w:t> 是正文文字，<m:t> 是 OMML 公式文字。
公式会以线性文字混入，足以判断题目类型，不能用于精确排版。
"""
import argparse
import glob
import re
import sys
import zipfile


def extract(docx_path: str) -> str:
    with zipfile.ZipFile(docx_path) as z:
        xml = z.read("word/document.xml").decode("utf-8", errors="ignore")
    # 段落分隔：把 </w:p> 换成换行，让输出有基本结构
    xml = xml.replace("</w:p>", "\n")
    texts = re.findall(r"<(?:w|m):t[^>]*>([^<]*)</(?:w|m):t>", xml)
    # findall 会丢换行，改为逐段处理
    out_lines = []
    for para in xml.split("\n"):
        line = "".join(re.findall(r"<(?:w|m):t[^>]*>([^<]*)</(?:w|m):t>", para))
        if line.strip():
            out_lines.append(line)
    return "\n".join(out_lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="+", help="docx 文件路径，支持 glob 通配符")
    ap.add_argument("-o", "--output", help="合并结果写入此文件（可选）")
    args = ap.parse_args()

    paths = []
    for f in args.files:
        paths.extend(glob.glob(f))

    if not paths:
        print("no docx matched", file=sys.stderr)
        sys.exit(1)

    chunks = []
    for p in paths:
        try:
            text = extract(p)
        except Exception as e:  # noqa: BLE001
            print(f"=== {p} ERROR {e} ===")
            continue
        header = f"===== {p} ({len(text)} chars) ====="
        print(header)
        print(text[:800])  # 预览前 800 字符
        print()
        chunks.append(header + "\n" + text)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as fp:
            fp.write("\n\n".join(chunks))
        print(f"[saved] {args.output}")


if __name__ == "__main__":
    main()
