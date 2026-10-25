from __future__ import annotations

import html
import re
import zipfile
from pathlib import Path


BASE = Path(__file__).resolve().parent
SOURCE = BASE / "UI_PRD_siRNA_Search.md"
OUTPUT = BASE / "UI_PRD_siRNA_Search_Tables.docx"


def esc(value: str) -> str:
    return html.escape(value, quote=False)


def text_runs(text: str) -> str:
    parts = re.split(r"(`[^`]+`)", text)
    runs = []
    for part in parts:
        if not part:
            continue
        if part.startswith("`") and part.endswith("`"):
            value = esc(part[1:-1])
            runs.append(
                "<w:r><w:rPr><w:rFonts w:ascii=\"Consolas\" w:hAnsi=\"Consolas\"/>"
                "<w:sz w:val=\"19\"/></w:rPr><w:t xml:space=\"preserve\">"
                + value
                + "</w:t></w:r>"
            )
        else:
            value = esc(part)
            runs.append(f"<w:r><w:t xml:space=\"preserve\">{value}</w:t></w:r>")
    return "".join(runs) or "<w:r><w:t></w:t></w:r>"


def paragraph(text: str = "", style: str | None = None) -> str:
    ppr = f"<w:pPr><w:pStyle w:val=\"{style}\"/></w:pPr>" if style else ""
    return f"<w:p>{ppr}{text_runs(text)}</w:p>"


def code_paragraph(text: str) -> str:
    return (
        "<w:p><w:pPr><w:pStyle w:val=\"Code\"/></w:pPr>"
        "<w:r><w:rPr><w:rFonts w:ascii=\"Consolas\" w:hAnsi=\"Consolas\"/>"
        "<w:sz w:val=\"18\"/></w:rPr><w:t xml:space=\"preserve\">"
        + esc(text)
        + "</w:t></w:r></w:p>"
    )


def split_table_row(line: str) -> list[str]:
    stripped = line.strip()
    if stripped.startswith("|"):
        stripped = stripped[1:]
    if stripped.endswith("|"):
        stripped = stripped[:-1]
    return [cell.strip() for cell in stripped.split("|")]


def is_table_sep(line: str) -> bool:
    cells = split_table_row(line)
    if not cells:
        return False
    return all(re.fullmatch(r":?-{3,}:?", cell.strip()) for cell in cells)


def table(rows: list[list[str]]) -> str:
    if not rows:
        return ""
    col_count = max(len(row) for row in rows)
    grid = "".join("<w:gridCol w:w=\"2400\"/>" for _ in range(col_count))
    out = [
        "<w:tbl>",
        "<w:tblPr><w:tblStyle w:val=\"TableGrid\"/>"
        "<w:tblW w:w=\"0\" w:type=\"auto\"/>"
        "<w:tblBorders><w:top w:val=\"single\" w:sz=\"6\" w:color=\"BFBFBF\"/>"
        "<w:left w:val=\"single\" w:sz=\"6\" w:color=\"BFBFBF\"/>"
        "<w:bottom w:val=\"single\" w:sz=\"6\" w:color=\"BFBFBF\"/>"
        "<w:right w:val=\"single\" w:sz=\"6\" w:color=\"BFBFBF\"/>"
        "<w:insideH w:val=\"single\" w:sz=\"6\" w:color=\"BFBFBF\"/>"
        "<w:insideV w:val=\"single\" w:sz=\"6\" w:color=\"BFBFBF\"/></w:tblBorders>"
        "<w:tblCellMar><w:top w:w=\"80\" w:type=\"dxa\"/><w:left w:w=\"80\" w:type=\"dxa\"/>"
        "<w:bottom w:w=\"80\" w:type=\"dxa\"/><w:right w:w=\"80\" w:type=\"dxa\"/></w:tblCellMar>"
        "</w:tblPr>",
        f"<w:tblGrid>{grid}</w:tblGrid>",
    ]
    for row_index, row in enumerate(rows):
        out.append("<w:tr>")
        padded = row + [""] * (col_count - len(row))
        for cell in padded:
            shade = '<w:shd w:fill="4F81BD"/>' if row_index == 0 else ""
            color = '<w:color w:val="FFFFFF"/><w:b/>' if row_index == 0 else ""
            out.append(
                "<w:tc><w:tcPr>"
                + shade
                + "</w:tcPr><w:p><w:r><w:rPr>"
                + color
                + "</w:rPr><w:t xml:space=\"preserve\">"
                + esc(cell)
                + "</w:t></w:r></w:p></w:tc>"
            )
        out.append("</w:tr>")
    out.append("</w:tbl>")
    return "".join(out)


def parse_markdown(markdown: str) -> str:
    lines = markdown.splitlines()
    body: list[str] = []
    i = 0
    in_code = False
    while i < len(lines):
        line = lines[i]
        if line.startswith("```"):
            in_code = not in_code
            i += 1
            continue
        if in_code:
            body.append(code_paragraph(line))
            i += 1
            continue
        if line.startswith("# "):
            body.append(paragraph(line[2:].strip(), "Title"))
        elif line.startswith("## "):
            body.append(paragraph(line[3:].strip(), "Heading1"))
        elif line.startswith("### "):
            body.append(paragraph(line[4:].strip(), "Heading2"))
        elif line.strip().startswith("|") and i + 1 < len(lines) and is_table_sep(lines[i + 1]):
            rows = [split_table_row(line)]
            i += 2
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append(split_table_row(lines[i]))
                i += 1
            body.append(table(rows))
            continue
        elif line.strip():
            body.append(paragraph(line.strip()))
        else:
            body.append(paragraph())
        i += 1
    return "".join(body)


CONTENT_TYPES = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
<Default Extension="xml" ContentType="application/xml"/>
<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
<Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>
<Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>
<Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/>
</Types>"""

RELS = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
</Relationships>"""

DOC_RELS = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"/>"""

APP = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties"
xmlns:vt="http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes">
<Application>Codex</Application></Properties>"""

CORE = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties"
xmlns:dc="http://purl.org/dc/elements/1.1/"
xmlns:dcterms="http://purl.org/dc/terms/"
xmlns:dcmitype="http://purl.org/dc/dcmitype/"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
<dc:title>UI Developer PRD - siRNA Search</dc:title>
<dc:creator>Codex</dc:creator>
<cp:lastModifiedBy>Codex</cp:lastModifiedBy>
</cp:coreProperties>"""

STYLES = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
<w:style w:type="paragraph" w:default="1" w:styleId="Normal"><w:name w:val="Normal"/>
<w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:sz w:val="21"/></w:rPr></w:style>
<w:style w:type="paragraph" w:styleId="Title"><w:name w:val="Title"/>
<w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:b/><w:color w:val="404040"/><w:sz w:val="44"/></w:rPr></w:style>
<w:style w:type="paragraph" w:styleId="Heading1"><w:name w:val="heading 1"/>
<w:basedOn w:val="Normal"/><w:next w:val="Normal"/><w:qFormat/>
<w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:b/><w:color w:val="404040"/><w:sz w:val="30"/></w:rPr></w:style>
<w:style w:type="paragraph" w:styleId="Heading2"><w:name w:val="heading 2"/>
<w:basedOn w:val="Normal"/><w:next w:val="Normal"/><w:qFormat/>
<w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:b/><w:color w:val="404040"/><w:sz w:val="25"/></w:rPr></w:style>
<w:style w:type="paragraph" w:styleId="Code"><w:name w:val="Code"/>
<w:rPr><w:rFonts w:ascii="Consolas" w:hAnsi="Consolas"/><w:sz w:val="18"/></w:rPr></w:style>
<w:style w:type="table" w:styleId="TableGrid"><w:name w:val="Table Grid"/>
<w:tblPr><w:tblBorders><w:top w:val="single" w:sz="4" w:color="auto"/>
<w:left w:val="single" w:sz="4" w:color="auto"/><w:bottom w:val="single" w:sz="4" w:color="auto"/>
<w:right w:val="single" w:sz="4" w:color="auto"/><w:insideH w:val="single" w:sz="4" w:color="auto"/>
<w:insideV w:val="single" w:sz="4" w:color="auto"/></w:tblBorders></w:tblPr></w:style>
</w:styles>"""


def main() -> None:
    body = parse_markdown(SOURCE.read_text(encoding="utf-8"))
    document = (
        "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>"
        "<w:document xmlns:w=\"http://schemas.openxmlformats.org/wordprocessingml/2006/main\">"
        "<w:body>"
        + body
        + "<w:sectPr><w:pgSz w:w=\"12240\" w:h=\"15840\"/>"
        "<w:pgMar w:top=\"720\" w:right=\"720\" w:bottom=\"720\" w:left=\"720\" "
        "w:header=\"720\" w:footer=\"720\" w:gutter=\"0\"/></w:sectPr>"
        "</w:body></w:document>"
    )
    with zipfile.ZipFile(OUTPUT, "w", zipfile.ZIP_DEFLATED) as docx:
        docx.writestr("[Content_Types].xml", CONTENT_TYPES)
        docx.writestr("_rels/.rels", RELS)
        docx.writestr("word/_rels/document.xml.rels", DOC_RELS)
        docx.writestr("word/document.xml", document)
        docx.writestr("word/styles.xml", STYLES)
        docx.writestr("docProps/core.xml", CORE)
        docx.writestr("docProps/app.xml", APP)
    print(OUTPUT)


if __name__ == "__main__":
    main()
