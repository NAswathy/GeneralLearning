#!/usr/bin/env python3
import html
import os
import re
import sys
import zipfile
from datetime import datetime, timezone


def esc(value):
    return html.escape(value, quote=False)


def para(text="", style=None):
    runs = []
    remaining = text
    pattern = re.compile(r"`([^`]+)`")
    pos = 0
    for match in pattern.finditer(remaining):
        if match.start() > pos:
            runs.append((remaining[pos:match.start()], False))
        runs.append((match.group(1), True))
        pos = match.end()
    if pos < len(remaining):
        runs.append((remaining[pos:], False))
    if not runs:
        runs = [("", False)]

    ppr = ""
    if style:
        ppr = f'<w:pPr><w:pStyle w:val="{style}"/></w:pPr>'
    body = [f"<w:p>{ppr}"]
    for value, code in runs:
        rpr = ""
        if code:
            rpr = '<w:rPr><w:rStyle w:val="CodeChar"/><w:rFonts w:ascii="Courier New" w:hAnsi="Courier New"/><w:color w:val="C00000"/></w:rPr>'
        body.append(f"<w:r>{rpr}<w:t xml:space=\"preserve\">{esc(value)}</w:t></w:r>")
    body.append("</w:p>")
    return "".join(body)


def code_para(text):
    return (
        '<w:p><w:pPr><w:pStyle w:val="CodeBlock"/></w:pPr>'
        '<w:r><w:rPr><w:rFonts w:ascii="Courier New" w:hAnsi="Courier New"/><w:sz w:val="18"/></w:rPr>'
        f'<w:t xml:space="preserve">{esc(text)}</w:t></w:r></w:p>'
    )


def split_table_line(line):
    value = line.strip()
    if value.startswith("|"):
        value = value[1:]
    if value.endswith("|"):
        value = value[:-1]
    return [cell.strip() for cell in value.split("|")]


def is_separator_row(line):
    cells = split_table_line(line)
    if not cells:
        return False
    return all(re.fullmatch(r":?-{3,}:?", cell.strip()) for cell in cells)


def table_xml(rows):
    if not rows:
        return ""
    col_count = max(len(row) for row in rows)
    width = max(1200, int(9000 / max(1, col_count)))
    parts = [
        '<w:tbl>',
        '<w:tblPr>',
        '<w:tblStyle w:val="TableGrid"/>',
        '<w:tblW w:w="0" w:type="auto"/>',
        '<w:tblBorders>',
        '<w:top w:val="single" w:sz="4" w:space="0" w:color="BFBFBF"/>',
        '<w:left w:val="single" w:sz="4" w:space="0" w:color="BFBFBF"/>',
        '<w:bottom w:val="single" w:sz="4" w:space="0" w:color="BFBFBF"/>',
        '<w:right w:val="single" w:sz="4" w:space="0" w:color="BFBFBF"/>',
        '<w:insideH w:val="single" w:sz="4" w:space="0" w:color="BFBFBF"/>',
        '<w:insideV w:val="single" w:sz="4" w:space="0" w:color="BFBFBF"/>',
        '</w:tblBorders>',
        '</w:tblPr>',
        '<w:tblGrid>',
    ]
    for _ in range(col_count):
        parts.append(f'<w:gridCol w:w="{width}"/>')
    parts.append('</w:tblGrid>')

    for r_idx, row in enumerate(rows):
        parts.append("<w:tr>")
        for c_idx in range(col_count):
            cell = row[c_idx] if c_idx < len(row) else ""
            shade = '<w:shd w:fill="D9EAF7"/>' if r_idx == 0 else ""
            bold_start = '<w:b/>' if r_idx == 0 else ""
            parts.append(
                '<w:tc>'
                f'<w:tcPr><w:tcW w:w="{width}" w:type="dxa"/>{shade}<w:tcMar>'
                '<w:top w:w="80" w:type="dxa"/><w:left w:w="80" w:type="dxa"/>'
                '<w:bottom w:w="80" w:type="dxa"/><w:right w:w="80" w:type="dxa"/>'
                '</w:tcMar></w:tcPr>'
                '<w:p><w:r><w:rPr>'
                f'{bold_start}'
                '<w:sz w:val="18"/></w:rPr>'
                f'<w:t xml:space="preserve">{esc(cell)}</w:t>'
                '</w:r></w:p>'
                '</w:tc>'
            )
        parts.append("</w:tr>")
    parts.append("</w:tbl>")
    return "".join(parts)


def parse_markdown(markdown):
    lines = markdown.splitlines()
    out = []
    i = 0
    in_code = False
    while i < len(lines):
        line = lines[i]
        if line.startswith("```"):
            in_code = not in_code
            i += 1
            continue
        if in_code:
            out.append(code_para(line))
            i += 1
            continue
        if line.strip().startswith("|") and "|" in line.strip()[1:]:
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                if not is_separator_row(lines[i]):
                    rows.append(split_table_line(lines[i]))
                i += 1
            out.append(table_xml(rows))
            continue
        if line.startswith("# "):
            out.append(para(line[2:].strip(), "Title"))
        elif line.startswith("## "):
            out.append(para(line[3:].strip(), "Heading1"))
        elif line.startswith("### "):
            out.append(para(line[4:].strip(), "Heading2"))
        elif line.startswith("#### "):
            out.append(para(line[5:].strip(), "Heading3"))
        elif line.startswith("- "):
            out.append(para(line[2:].strip(), "ListParagraph"))
        elif not line.strip():
            out.append(para(""))
        else:
            out.append(para(line.strip()))
        i += 1
    return "".join(out)


def content_types():
    return """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
  <Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>
  <Override PartName="/word/settings.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.settings+xml"/>
  <Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>
  <Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/>
</Types>"""


def rels():
    return """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/>
  <Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties" Target="docProps/app.xml"/>
</Relationships>"""


def document_rels():
    return """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rIdStyles" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>
  <Relationship Id="rIdSettings" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/settings" Target="settings.xml"/>
</Relationships>"""


def styles():
    return """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:style w:type="paragraph" w:default="1" w:styleId="Normal"><w:name w:val="Normal"/><w:pPr><w:spacing w:after="120"/></w:pPr><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:sz w:val="20"/></w:rPr></w:style>
  <w:style w:type="paragraph" w:styleId="Title"><w:name w:val="Title"/><w:basedOn w:val="Normal"/><w:pPr><w:spacing w:after="240"/></w:pPr><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:b/><w:color w:val="1F4E79"/><w:sz w:val="34"/></w:rPr></w:style>
  <w:style w:type="paragraph" w:styleId="Heading1"><w:name w:val="heading 1"/><w:basedOn w:val="Normal"/><w:next w:val="Normal"/><w:qFormat/><w:pPr><w:keepNext/><w:spacing w:before="300" w:after="120"/></w:pPr><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:b/><w:color w:val="1F4E79"/><w:sz w:val="26"/></w:rPr></w:style>
  <w:style w:type="paragraph" w:styleId="Heading2"><w:name w:val="heading 2"/><w:basedOn w:val="Normal"/><w:next w:val="Normal"/><w:qFormat/><w:pPr><w:keepNext/><w:spacing w:before="220" w:after="100"/></w:pPr><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:b/><w:color w:val="2F75B5"/><w:sz w:val="22"/></w:rPr></w:style>
  <w:style w:type="paragraph" w:styleId="Heading3"><w:name w:val="heading 3"/><w:basedOn w:val="Normal"/><w:next w:val="Normal"/><w:qFormat/><w:pPr><w:keepNext/><w:spacing w:before="180" w:after="80"/></w:pPr><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:b/><w:color w:val="3F3F3F"/><w:sz w:val="20"/></w:rPr></w:style>
  <w:style w:type="paragraph" w:styleId="ListParagraph"><w:name w:val="List Paragraph"/><w:basedOn w:val="Normal"/><w:pPr><w:ind w:left="360"/></w:pPr></w:style>
  <w:style w:type="paragraph" w:styleId="CodeBlock"><w:name w:val="Code Block"/><w:basedOn w:val="Normal"/><w:pPr><w:spacing w:before="0" w:after="0"/><w:shd w:fill="F3F6F8"/></w:pPr><w:rPr><w:rFonts w:ascii="Courier New" w:hAnsi="Courier New"/><w:sz w:val="18"/></w:rPr></w:style>
  <w:style w:type="character" w:styleId="CodeChar"><w:name w:val="Code Char"/><w:rPr><w:rFonts w:ascii="Courier New" w:hAnsi="Courier New"/><w:sz w:val="19"/></w:rPr></w:style>
  <w:style w:type="table" w:styleId="TableGrid"><w:name w:val="Table Grid"/><w:basedOn w:val="TableNormal"/><w:uiPriority w:val="59"/><w:rsid w:val="00E825C1"/><w:pPr><w:spacing w:after="0" w:line="240" w:lineRule="auto"/></w:pPr><w:tblPr><w:tblInd w:w="0" w:type="dxa"/><w:tblCellMar><w:top w:w="80" w:type="dxa"/><w:left w:w="80" w:type="dxa"/><w:bottom w:w="80" w:type="dxa"/><w:right w:w="80" w:type="dxa"/></w:tblCellMar></w:tblPr></w:style>
</w:styles>"""


def settings():
    return """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:settings xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:zoom w:percent="100"/></w:settings>"""


def core_props():
    now = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:dcmitype="http://purl.org/dc/dcmitype/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dc:title>UI Developer PRD: TrueGuide sgRNA Search</dc:title>
  <dc:creator>Codex</dc:creator>
  <cp:lastModifiedBy>Codex</cp:lastModifiedBy>
  <dcterms:created xsi:type="dcterms:W3CDTF">{now}</dcterms:created>
  <dcterms:modified xsi:type="dcterms:W3CDTF">{now}</dcterms:modified>
</cp:coreProperties>"""


def app_props():
    return """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties" xmlns:vt="http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes">
  <Application>Codex OpenXML Generator</Application>
</Properties>"""


def document_xml(body_xml):
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:body>
    {body_xml}
    <w:sectPr><w:pgSz w:w="12240" w:h="15840"/><w:pgMar w:top="720" w:right="720" w:bottom="720" w:left="720" w:header="360" w:footer="360" w:gutter="0"/></w:sectPr>
  </w:body>
</w:document>"""


def main():
    if len(sys.argv) != 3:
        print("usage: _markdown_to_docx.py input.md output.docx", file=sys.stderr)
        return 2
    src, dst = sys.argv[1], sys.argv[2]
    with open(src, "r", encoding="utf-8") as f:
        markdown = f.read()
    body = parse_markdown(markdown)
    os.makedirs(os.path.dirname(dst) or ".", exist_ok=True)
    with zipfile.ZipFile(dst, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", content_types())
        z.writestr("_rels/.rels", rels())
        z.writestr("docProps/core.xml", core_props())
        z.writestr("docProps/app.xml", app_props())
        z.writestr("word/document.xml", document_xml(body))
        z.writestr("word/styles.xml", styles())
        z.writestr("word/settings.xml", settings())
        z.writestr("word/_rels/document.xml.rels", document_rels())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
