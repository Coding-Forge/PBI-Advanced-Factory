# Lab PDFs (Fallback Format)

This folder contains printable PDF fallbacks of every Lab README located under
`Student\Labs\Source\<module>\README.md`. They are intended for students who
cannot access the Markdown source files or the [HTML lab guides](../Web/)
(for example, when working offline, printing physical copies, or using a
device/tool that can't render Markdown or interactive HTML well).

## How these are generated

PDFs are **not hand-authored** — they are generated directly from the
authoritative README.md in each lab's `Source` folder using:

```powershell
python tools\build-pdf-labs.py
```

The script converts each README's Markdown to HTML with print-friendly CSS
(page breaks before each major `##` section, tables/code blocks kept intact
across page boundaries where possible) and then uses headless Microsoft Edge
to print that HTML to PDF.

**Do not hand-edit the PDFs.** If a README changes, re-run the script above to
regenerate the corresponding PDF(s) — the same way `tools\build-html-labs.ps1`
regenerates the `Student\Labs\Web` HTML files.

## Files

| File | Source |
|---|---|
| `01-advanced-semantic-modeling.pdf` | `Student\Labs\Source\01-advanced-semantic-modeling\README.md` |
| `02-advanced-dax.pdf` | `Student\Labs\Source\02-advanced-dax\README.md` |
| `03-advanced-power-query.pdf` | `Student\Labs\Source\03-advanced-power-query\README.md` |
| `04-report-design-ux.pdf` | `Student\Labs\Source\04-report-design-ux\README.md` |
| `05-performance-optimization.pdf` | `Student\Labs\Source\05-performance-optimization\README.md` |
| `06-advanced-analytics-ai.pdf` | `Student\Labs\Source\06-advanced-analytics-ai\README.md` |
| `07-security-design.pdf` | `Student\Labs\Source\07-security-design\README.md` |
| `08-service-enterprise-deployment.pdf` | `Student\Labs\Source\08-service-enterprise-deployment\README.md` |
| `09-monitoring-governance.pdf` | `Student\Labs\Source\09-monitoring-governance\README.md` |
| `10-premium-fabric-capacity.pdf` | `Student\Labs\Source\10-premium-fabric-capacity\README.md` |
| `11-automation-devops.pdf` | `Student\Labs\Source\11-automation-devops\README.md` |
| `12-capstone.pdf` | `Student\Labs\Source\12-capstone\README.md` |

## Requirements to regenerate

- Python 3 with the `markdown` package (`pip install markdown`)
- Microsoft Edge or Google Chrome installed (used in headless mode to print
  the generated HTML to PDF)
