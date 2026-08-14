"""Generate the branded 'Modules 1-7 Delivery Agenda' PDF from the markdown source.

Reads docs/agendas/Modules-1-7-Delivery-Agenda.md, renders it into the same
navy/cyan visual language as the Advanced Power BI datasheets, and prints it
to PDF via Playwright/Chromium.
"""
import re
from pathlib import Path
from playwright.sync_api import sync_playwright

HERE = Path(__file__).parent
MD_PATH = HERE.parent / "agendas" / "Modules-1-7-Delivery-Agenda.md"
OUT_HTML = HERE.parent / "agendas" / "Modules-1-7-Delivery-Agenda.html"
OUT_PDF = HERE.parent / "agendas" / "Modules-1-7-Delivery-Agenda.pdf"

PRIMARY = "#1E2761"
ACCENT = "#0BA5C7"
BG = "#F4F7FB"


def parse_table(lines):
    """Parse a GitHub-flavored markdown table block into (headers, rows)."""
    header = [c.strip() for c in lines[0].strip().strip("|").split("|")]
    rows = []
    for line in lines[2:]:
        if not line.strip().startswith("|"):
            break
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        rows.append(cells)
    return header, rows


def inline_md(text):
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"`(.+?)`", r"<code>\1</code>", text)
    return text


def render_table(header, rows):
    thead = "".join(f"<th>{inline_md(h)}</th>" for h in header)
    body_rows = []
    for r in rows:
        is_break = len(r) > 1 and "Break" in r[1]
        cls = ' class="break-row"' if is_break else ""
        cells = "".join(f"<td>{inline_md(c)}</td>" for c in r)
        body_rows.append(f"<tr{cls}>{cells}</tr>")
    tbody = "\n".join(body_rows)
    return f"""<table class="agenda-table">
      <thead><tr>{thead}</tr></thead>
      <tbody>{tbody}</tbody>
    </table>"""


def markdown_to_html(md_text):
    lines = md_text.splitlines()
    html_parts = []
    i = 0
    in_list = False
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if not stripped:
            i += 1
            continue

        if stripped == "---":
            i += 1
            continue

        if stripped.startswith("| "):
            table_lines = []
            j = i
            while j < len(lines) and lines[j].strip().startswith("|"):
                table_lines.append(lines[j])
                j += 1
            header, rows = parse_table(table_lines)
            html_parts.append(render_table(header, rows))
            i = j
            continue

        if stripped.startswith("# "):
            html_parts.append(f'<h1>{inline_md(stripped[2:])}</h1>')
            i += 1
            continue
        if stripped.startswith("## "):
            html_parts.append(f'<h2>{inline_md(stripped[3:])}</h2>')
            i += 1
            continue
        if stripped.startswith("### "):
            html_parts.append(f'<h3>{inline_md(stripped[4:])}</h3>')
            i += 1
            continue

        if stripped.startswith("- "):
            list_items = []
            j = i
            while j < len(lines) and lines[j].strip().startswith("- "):
                list_items.append(f"<li>{inline_md(lines[j].strip()[2:])}</li>")
                j += 1
            html_parts.append(f'<ul class="note-list">{"".join(list_items)}</ul>')
            i = j
            continue

        # plain paragraph, possibly bold-lead
        html_parts.append(f"<p>{inline_md(stripped)}</p>")
        i += 1

    return "\n".join(html_parts)


def strip_cover_content(md_text):
    """Remove the leading H1 title and its intro paragraph (already on the cover)."""
    lines = md_text.splitlines()
    out = []
    skipping_intro = False
    for idx, line in enumerate(lines):
        stripped = line.strip()
        if idx == 0 and stripped.startswith("# "):
            continue
        if stripped.startswith("**Delivery window:**"):
            skipping_intro = True
            continue
        if skipping_intro:
            if stripped == "" or stripped == "---":
                skipping_intro = False
                continue
            continue
        out.append(line)
    return "\n".join(out)


def build_html():
    md_text = MD_PATH.read_text(encoding="utf-8")
    md_text = strip_cover_content(md_text)
    body_html = markdown_to_html(md_text)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Advanced Power BI - Modules 1-7 Delivery Agenda</title>
<style>
  @page {{ size: Letter; margin: 0; }}
  * {{ box-sizing: border-box; }}
  body {{
    font-family: 'Segoe UI', Calibri, Arial, sans-serif;
    margin: 0;
    color: #1D2433;
    background: {BG};
  }}
  .cover {{
    background: linear-gradient(135deg, {PRIMARY} 0%, #10163D 100%);
    color: #fff;
    padding: 70px 60px;
  }}
  .cover .kicker {{
    text-transform: uppercase;
    letter-spacing: 2px;
    font-size: 12px;
    font-weight: 700;
    color: {ACCENT};
    margin-bottom: 14px;
  }}
  .cover h1 {{
    font-size: 34px;
    font-weight: 800;
    margin: 0 0 14px 0;
    line-height: 1.15;
  }}
  .cover .meta {{
    font-size: 13.5px;
    color: #C9D4EE;
    line-height: 1.7;
  }}
  .cover .meta strong {{ color: #fff; }}
  .content {{
    padding: 34px 46px 50px 46px;
  }}
  h2 {{
    font-size: 18px;
    font-weight: 800;
    color: {PRIMARY};
    border-bottom: 3px solid {ACCENT};
    padding-bottom: 6px;
    margin: 28px 0 6px 0;
  }}
  h2:first-of-type {{ margin-top: 0; }}
  h3 {{
    font-size: 14px;
    font-weight: 700;
    color: {PRIMARY};
    margin: 18px 0 6px 0;
  }}
  p {{
    font-size: 11.5px;
    line-height: 1.55;
    margin: 4px 0 10px 0;
    color: #333;
  }}
  code {{
    background: #E9EEF7;
    border-radius: 3px;
    padding: 1px 5px;
    font-family: Consolas, monospace;
    font-size: 10.5px;
  }}
  .agenda-table {{
    width: 100%;
    border-collapse: collapse;
    margin: 8px 0 16px 0;
    font-size: 10.3px;
  }}
  .agenda-table th {{
    background: {PRIMARY};
    color: #fff;
    text-align: left;
    padding: 7px 8px;
    font-size: 10px;
    text-transform: uppercase;
    letter-spacing: 0.3px;
  }}
  .agenda-table td {{
    padding: 7px 8px;
    border-bottom: 1px solid #E3E8F2;
    vertical-align: top;
    line-height: 1.4;
  }}
  .agenda-table tr:nth-child(even) td {{ background: #FAFBFE; }}
  .agenda-table tr.break-row td {{
    background: #FFF4DE !important;
    font-weight: 700;
    color: #8A5B00;
  }}
  .note-list {{
    margin: 4px 0 14px 0;
    padding-left: 18px;
    font-size: 11.5px;
    line-height: 1.55;
    color: #333;
  }}
  .note-list li {{ margin-bottom: 6px; }}
  .footer-bar {{
    position: running(footer);
  }}
  .page-footer {{
    text-align: center;
    font-size: 9.5px;
    color: #8A93A6;
    padding: 14px 0 30px 0;
  }}
</style>
</head>
<body>
  <div class="cover">
    <div class="kicker">Advanced Power BI &middot; Delivery Agenda</div>
    <h1>Modules 1&ndash;7 Delivery Agenda</h1>
    <div class="meta">
      <strong>Delivery window:</strong> 10:00 AM &ndash; 3:00 PM daily, 30-minute break at 12:00&ndash;12:30 PM<br>
      <strong>Scope:</strong> Modules 1&ndash;7 (Advanced Semantic Modeling &rarr; Security Design)<br>
      <strong>Format:</strong> 3-day standard workshop
    </div>
  </div>
  <div class="content">
    {body_html}
  </div>
  <div class="page-footer">Advanced Power BI &middot; Modules 1&ndash;7 Delivery Agenda &middot; For instructor and scheduling use</div>
</body>
</html>"""
    return html


def main():
    html = build_html()
    OUT_HTML.write_text(html, encoding="utf-8")

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(OUT_HTML.resolve().as_uri())
        page.pdf(
            path=str(OUT_PDF),
            format="Letter",
            print_background=True,
            margin={"top": "0", "bottom": "0", "left": "0", "right": "0"},
        )
        browser.close()
    print(f"Generated {OUT_PDF}")


if __name__ == "__main__":
    main()
