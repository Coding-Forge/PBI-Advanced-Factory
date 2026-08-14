#!/usr/bin/env python3
"""
Generates a printable PDF for each Lab README under Student/Labs/Source/<module>/README.md.
Converts Markdown -> styled HTML (with print-friendly CSS/page-break rules) -> PDF via headless
Microsoft Edge (Chromium print-to-pdf). Output PDFs are written to Student/Labs/PDF/<module>.pdf.

Usage:
    python tools\\build-pdf-labs.py

Requires:
    - Python packages: markdown
    - Microsoft Edge (or Chrome) installed for headless PDF printing
"""
import os
import re
import subprocess
import sys
from pathlib import Path

import markdown

REPO_ROOT = Path(__file__).resolve().parent.parent
SOURCE_DIR = REPO_ROOT / "Student" / "Labs" / "Source"
PDF_DIR = REPO_ROOT / "Student" / "Labs" / "PDF"
TMP_HTML_DIR = PDF_DIR / "_tmp_html"

EDGE_CANDIDATES = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
]

CSS = """
@page {
    size: Letter;
    margin: 0.75in 0.7in 0.8in 0.7in;
    @bottom-center {
        content: "Page " counter(page) " of " counter(pages);
        font-family: Segoe UI, Arial, sans-serif;
        font-size: 9px;
        color: #6b7280;
    }
}
html, body {
    font-family: 'Segoe UI', Arial, sans-serif;
    color: #1f2328;
    font-size: 12px;
    line-height: 1.55;
    margin: 0;
    padding: 0;
}
.doc-header {
    border-bottom: 3px solid #2b579a;
    padding-bottom: 10px;
    margin-bottom: 22px;
}
.doc-header .eyebrow {
    text-transform: uppercase;
    letter-spacing: 0.08em;
    font-size: 10px;
    color: #2b579a;
    font-weight: 600;
}
.doc-header h1 {
    margin: 4px 0 0 0;
    font-size: 22px;
}
h1, h2, h3, h4 {
    color: #14213d;
    font-weight: 600;
    page-break-after: avoid;
    break-after: avoid;
}
h1 { font-size: 20px; margin-top: 0; }
h2 {
    font-size: 16px;
    margin-top: 26px;
    padding-top: 6px;
    border-top: 1px solid #d8dee4;
}
h3 { font-size: 13.5px; margin-top: 18px; }
h4 { font-size: 12.5px; margin-top: 14px; }

/* Keep a heading and the content right after it together */
h2, h3, h4 { page-break-inside: avoid; break-inside: avoid; }

p, ul, ol, table, pre, blockquote {
    page-break-inside: avoid;
    break-inside: avoid;
}
/* Long lists/tables can still avoid awkward single-row splits without forcing
   the whole block onto one page when it's larger than a page. */
table { page-break-inside: auto; }
tr { page-break-inside: avoid; break-inside: avoid; }

/* Force a clean page break before each top-level Lab/Exercise heading so a
   lab doesn't start 2 lines from the bottom of a page. */
h2.lab-break { page-break-before: always; break-before: page; }

a { color: #2b579a; text-decoration: none; }
code {
    font-family: Consolas, 'Courier New', monospace;
    background: #f2f4f7;
    padding: 1px 4px;
    border-radius: 3px;
    font-size: 11px;
}
pre {
    background: #f6f8fa;
    border: 1px solid #d8dee4;
    border-radius: 5px;
    padding: 10px 12px;
    overflow-x: auto;
    font-size: 10.5px;
    line-height: 1.4;
}
pre code { background: none; padding: 0; }
table {
    border-collapse: collapse;
    width: 100%;
    margin: 10px 0 16px 0;
    font-size: 11px;
}
th, td {
    border: 1px solid #d8dee4;
    padding: 5px 8px;
    text-align: left;
    vertical-align: top;
}
th { background: #eef2f7; font-weight: 600; }
blockquote {
    margin: 10px 0;
    padding: 6px 14px;
    border-left: 4px solid #2b579a;
    background: #f6f8fa;
    color: #3b4252;
}
ul, ol { margin: 6px 0 12px 0; padding-left: 22px; }
li { margin: 3px 0; }
hr { border: none; border-top: 1px solid #d8dee4; margin: 18px 0; }
img { max-width: 100%; }
strong { color: #14213d; }
"""

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{title}</title>
<style>{css}</style>
</head>
<body>
<div class="doc-header">
    <div class="eyebrow">Advanced Power BI Training &middot; Fallback PDF Edition</div>
    <h1>{title}</h1>
</div>
{body}
</body>
</html>
"""


def slugify_title(module_dir_name: str) -> str:
    # e.g. "01-advanced-semantic-modeling" -> "Lab 01: Advanced Semantic Modeling"
    m = re.match(r"^(\d+)-(.+)$", module_dir_name)
    if not m:
        return module_dir_name
    num, rest = m.groups()
    words = rest.replace("-", " ").split(" ")
    title_words = []
    for w in words:
        if w.lower() in ("ai", "ux", "devops"):
            title_words.append(w.upper() if w.lower() != "devops" else "DevOps")
        else:
            title_words.append(w.capitalize())
    return f"Lab {num}: {' '.join(title_words)}"


def find_edge() -> str:
    for candidate in EDGE_CANDIDATES:
        if os.path.exists(candidate):
            return candidate
    print("ERROR: Could not find Microsoft Edge or Google Chrome for PDF printing.", file=sys.stderr)
    sys.exit(1)


def convert_markdown_to_html_body(md_text: str) -> str:
    html = markdown.markdown(
        md_text,
        extensions=["extra", "tables", "fenced_code", "toc", "sane_lists"],
    )
    # Force a page break before every top-level "## " heading except the first
    # one, so each major section starts cleanly on its own page instead of
    # splitting awkwardly across a page boundary.
    seen_first_h2 = False

    def tag_h2(match):
        nonlocal seen_first_h2
        opening_tag = match.group(0)
        if not seen_first_h2:
            seen_first_h2 = True
            return opening_tag
        return opening_tag[:-1] + ' class="lab-break">' if opening_tag.endswith(">") else opening_tag

    html = re.sub(r"<h2[^>]*>", tag_h2, html)
    return html


def main():
    PDF_DIR.mkdir(parents=True, exist_ok=True)
    TMP_HTML_DIR.mkdir(parents=True, exist_ok=True)

    edge_path = find_edge()

    module_dirs = sorted(
        [d for d in SOURCE_DIR.iterdir() if d.is_dir() and (d / "README.md").exists()],
        key=lambda d: d.name,
    )

    if not module_dirs:
        print("No module README.md files found under", SOURCE_DIR, file=sys.stderr)
        sys.exit(1)

    generated = []
    for module_dir in module_dirs:
        readme_path = module_dir / "README.md"
        md_text = readme_path.read_text(encoding="utf-8")
        title = slugify_title(module_dir.name)

        body_html = convert_markdown_to_html_body(md_text)
        full_html = HTML_TEMPLATE.format(title=title, css=CSS, body=body_html)

        tmp_html_path = TMP_HTML_DIR / f"{module_dir.name}.html"
        tmp_html_path.write_text(full_html, encoding="utf-8")

        pdf_path = PDF_DIR / f"{module_dir.name}.pdf"

        print(f"Rendering {module_dir.name} -> {pdf_path.name}")
        user_data_dir = TMP_HTML_DIR / f"_profile_{module_dir.name}"
        result = subprocess.run(
            [
                edge_path,
                "--headless=new",
                "--disable-gpu",
                "--no-pdf-header-footer",
                f"--user-data-dir={user_data_dir}",
                f"--print-to-pdf={pdf_path}",
                "--print-to-pdf-no-header",
                "--no-sandbox",
                "--no-first-run",
                tmp_html_path.as_uri(),
            ],
            capture_output=True,
            text=True,
            timeout=90,
        )
        import shutil as _shutil
        _shutil.rmtree(user_data_dir, ignore_errors=True)
        if result.returncode != 0 or not pdf_path.exists():
            print(f"  FAILED: {result.stderr}", file=sys.stderr)
            sys.exit(1)
        generated.append(pdf_path)

    # Cleanup temp HTML working directory
    for f in TMP_HTML_DIR.glob("*.html"):
        f.unlink()
    TMP_HTML_DIR.rmdir()

    print(f"\nGenerated {len(generated)} lab PDFs in {PDF_DIR}")


if __name__ == "__main__":
    main()
