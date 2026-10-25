from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
import re
from xml.sax.saxutils import escape


SRC = Path("DevPRDs/UI_PRD_miRNA_Mimics_Inhibitors_Search.md")
OUT = Path("DevPRDs/UI_PRD_miRNA_Mimics_Inhibitors_Search_Tables.docx")


def x(text):
    return escape(text, {"\"": "&quot;"})


def parse_inline(text, header=False):
    parts = re.split(r"(`[^`]+`)", text)
    runs = []
    for part in parts:
        if not part:
            continue
        is_code = len(part) >= 2 and part[0] == "`" and part[-1] == "`"
        value = part[1:-1] if is_code else part
        props = []
        if header:
            props.append("<w:b/>")
            props.append("<w:color w:val=\"FFFFFF\"/>")
        if is_code:
            props.append("<w:rFonts w:ascii=\"Consolas\" w:hAnsi=\"Consolas\"/>")
            props.append("<w:sz w:val=\"18\"/>")
        rpr = f"<w:rPr>{''.join(props)}</w:rPr>" if props else ""
        runs.append(f"<w:r>{rpr}<w:t xml:space=\"preserve\">{x(value)}</w:t></w:r>")
    return "".join(runs) or "<w:r><w:t></w:t></w:r>"


def paragraph(text, style=None):
    ppr = f"<w:pPr><w:pStyle w:val=\"{style}\"/></w:pPr>" if style else ""
    return f"<w:p>{ppr}{parse_inline(text)}</w:p>"


def split_row(line):
    cells = [c.strip() for c in line.strip().strip("|").split("|")]
    return [c.replace("&lt;br/&gt;", " ").replace("<br/>", " ") for c in cells]


def is_separator(line):
    return bool(re.match(r"^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)+\|?\s*$", line))


def is_table_start(lines, i):
    return i + 1 < len(lines) and lines[i].strip().startswith("|") and is_separator(lines[i + 1])


def cell(text, header=False, width=2500):
    shade = "<w:shd w:fill=\"1F4E79\"/>" if header else ""
    color = "FFFFFF" if header else "222222"
    tcpr = (
        f"<w:tcPr><w:tcW w:w=\"{width}\" w:type=\"dxa\"/>"
        "<w:tcBorders><w:top w:val=\"single\" w:sz=\"4\" w:color=\"BFBFBF\"/>"
        "<w:left w:val=\"single\" w:sz=\"4\" w:color=\"BFBFBF\"/>"
        "<w:bottom w:val=\"single\" w:sz=\"4\" w:color=\"BFBFBF\"/>"
        "<w:right w:val=\"single\" w:sz=\"4\" w:color=\"BFBFBF\"/></w:tcBorders>"
        f"{shade}</w:tcPr>"
    )
    ppr = "<w:pPr><w:spacing w:after=\"60\"/></w:pPr>"
    # Apply color to non-code header text through parse_inline header mode.
    content = parse_inline(text, header=header)
    if header and "<w:color" not in content:
        content = f"<w:r><w:rPr><w:b/><w:color w:val=\"{color}\"/></w:rPr><w:t>{x(text)}</w:t></w:r>"
    return f"<w:tc>{tcpr}<w:p>{ppr}{content}</w:p></w:tc>"


def table(header, rows):
    col_count = max(1, len(header))
    width = int(9360 / col_count)
    grid = "".join(f"<w:gridCol w:w=\"{width}\"/>" for _ in range(col_count))
    xml = [
        "<w:tbl>",
        "<w:tblPr><w:tblW w:w=\"0\" w:type=\"auto\"/><w:tblLook w:val=\"04A0\" w:firstRow=\"1\" w:noHBand=\"0\" w:noVBand=\"1\"/></w:tblPr>",
        f"<w:tblGrid>{grid}</w:tblGrid>",
        "<w:tr>" + "".join(cell(c, header=True, width=width) for c in header) + "</w:tr>",
    ]
    for row in rows:
        if len(row) < col_count:
            row += [""] * (col_count - len(row))
        if len(row) > col_count:
            row = row[: col_count - 1] + [" / ".join(row[col_count - 1 :])]
        xml.append("<w:tr>" + "".join(cell(c, width=width) for c in row) + "</w:tr>")
    xml.append("</w:tbl>")
    xml.append("<w:p/>")
    return "".join(xml)


def md_to_body(text):
    lines = text.splitlines()
    body = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        if line.startswith("# "):
            body.append(paragraph(line[2:].strip(), "Title"))
            i += 1
            continue
        if line.startswith("## "):
            body.append(paragraph(line[3:].strip(), "Heading1"))
            i += 1
            continue
        if line.startswith("### "):
            body.append(paragraph(line[4:].strip(), "Heading2"))
            i += 1
            continue
        if is_table_start(lines, i):
            header = split_row(lines[i])
            i += 2
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append(split_row(lines[i]))
                i += 1
            body.append(table(header, rows))
            continue
        para = [line.strip()]
        i += 1
        while i < len(lines) and lines[i].strip() and not lines[i].startswith("#") and not is_table_start(lines, i):
            para.append(lines[i].strip())
            i += 1
        body.append(paragraph(" ".join(para)))
    return "".join(body)


def make_docx():
    content_types = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
<Default Extension="xml" ContentType="application/xml"/>
<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
<Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>
</Types>"""
    rels = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
</Relationships>"""
    doc_rels = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"/>"""
    styles = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
<w:style w:type="paragraph" w:styleId="Normal"><w:name w:val="Normal"/><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:sz w:val="21"/></w:rPr></w:style>
<w:style w:type="paragraph" w:styleId="Title"><w:name w:val="Title"/><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:b/><w:color w:val="1F4E79"/><w:sz w:val="32"/></w:rPr></w:style>
<w:style w:type="paragraph" w:styleId="Heading1"><w:name w:val="heading 1"/><w:basedOn w:val="Normal"/><w:next w:val="Normal"/><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:b/><w:color w:val="1F4E79"/><w:sz w:val="26"/></w:rPr></w:style>
<w:style w:type="paragraph" w:styleId="Heading2"><w:name w:val="heading 2"/><w:basedOn w:val="Normal"/><w:next w:val="Normal"/><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:b/><w:color w:val="2F5597"/><w:sz w:val="23"/></w:rPr></w:style>
</w:styles>"""
    body = md_to_body(SRC.read_text(encoding="utf-8"))
    document = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
<w:body>{body}<w:sectPr><w:pgSz w:w="12240" w:h="15840"/><w:pgMar w:top="720" w:right="720" w:bottom="720" w:left="720" w:header="360" w:footer="360" w:gutter="0"/></w:sectPr></w:body>
</w:document>"""
    with ZipFile(OUT, "w", ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", content_types)
        z.writestr("_rels/.rels", rels)
        z.writestr("word/_rels/document.xml.rels", doc_rels)
        z.writestr("word/document.xml", document)
        z.writestr("word/styles.xml", styles)
    print(OUT)


if __name__ == "__main__":
    make_docx()
