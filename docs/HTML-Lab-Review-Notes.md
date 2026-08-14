# HTML Lab Review — What Changed & Illustration Suggestions

The learner-facing lab pages in `Student/Labs/Web/*.html` are **generated** by
`tools/build-html-labs.ps1` — do not hand-edit the HTML output, edit the
script and re-run it:

```powershell
pwsh -NoProfile -File tools\build-html-labs.ps1
```

This review expanded the **"Detailed step-by-step procedure"** section for
Labs 04–12 (Labs 01–03 were already explicit and were left unchanged) so the
walkthrough reads as a true click-by-click guide instead of a summary of
tasks. Each step now names the exact ribbon/pane/menu path, the specific
field or setting values to use, and what to check to confirm the step
worked.

## Summary of changes by lab

| Lab | What was expanded |
|---|---|
| 04 – Report Design & UX | Executive summary page build order, drillthrough setup, tooltip page, bookmarks/buttons, page navigation, field parameters, conditional formatting, mobile layout, accessibility (tab order, alt text, contrast) |
| 05 – Performance Optimization | Performance Analyzer capture steps, reading DAX query vs. visual display time, DAX rewrite guidance (variables, iterators, avoiding unnecessary context transition), aggregation table design |
| 06 – Advanced Analytics/AI | What-if parameter creation end to end, decomposition tree/forecasting/key influencers guidance framed as "review/verify, do not implement" (per Module 06 not-covered scope), Python/R and Azure ML noted as out of scope |
| 07 – Security Design | Static and dynamic RLS DAX and table setup, "View as roles" testing steps, Build permission review process |
| 08 – Service/Enterprise Deployment | Workspace planning fields, publish steps, refresh/credentials/gateway review, App packaging and audience setup |
| 09 – Monitoring & Governance | Usage metrics report walkthrough, refresh history review, tenant settings walkthrough |
| 10 – Premium/Fabric Capacity | Licensing/capacity comparison worksheet, XMLA endpoint check, Direct Lake notes, Capacity Metrics app review |
| 11 – Automation/DevOps | Git workflow (branch/commit/PR) steps, PR review checklist, service principal registration documentation, CI/CD conceptual walkthrough |
| 12 – Capstone | All 7 capstone tasks broken into more specific sub-actions that reference the patterns built in Labs 01–11 |

A regression was found and fixed during this pass: an earlier hand-patch had
added "Jeopardy review" links (per-lab bottom nav) and an index.html "Review
games" panel directly to the generated HTML, but never to the generator
script. Any future regeneration would have silently deleted those links.
Both link sets are now built into `build-html-labs.ps1` itself (`New-LabPage`
bottom nav and `New-IndexPage`), so they will survive future regenerations.

## Suggested illustrations (placeholders in the HTML now)

Each spot below already has a `<div class="figure"><figcaption>...` callout
in the generated HTML marking where a screenshot should go. Add real
screenshots later by replacing the placeholder `<div class="figure">` with
`<figure class="figure"><img src="images/<lab>/<name>.png" alt="..."><figcaption>...</figcaption></figure>`
(see the existing Lab 02 calculation-groups image for the pattern).

| Lab | Suggested illustration |
|---|---|
| 04 | Annotated finished Executive Summary page — callouts on KPI card row, trend chart, territory breakdown |
| 04 | Drillthrough: right-click context menu showing "Drillthrough" + the resulting filtered Customer Detail page |
| 04 | Field parameter: same chart before/after switching the parameter slicer (axis/label change) |
| 05 | Performance Analyzer pane, highest-cost visual expanded, annotated DAX query time vs. visual display time |
| 06 | What-if adjustment slider before/after (0% vs. +10%), two margin cards visibly different |
| 07 | "View as roles" dialog with dynamic role + test UPN, next to the resulting filtered report page |

## Follow-ups not done in this pass

- Labs 01–03 were not given new `.figure` illustration markers (their
  procedures were already detailed); add markers there later if consistency
  is wanted.
- No real screenshots were captured — only placeholder captions were added,
  per the request to come back and add pictures later.
