Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
$webRoot = Join-Path $repoRoot "Student\Labs\Web"
$scriptsRoot = Join-Path $webRoot "scripts"
$stylesRoot = Join-Path $webRoot "styles"
$brandingRoot = Join-Path $webRoot "Branding\Default"

New-Item -ItemType Directory -Force -Path $webRoot, $scriptsRoot, $stylesRoot, $brandingRoot | Out-Null

$utf8NoBom = [System.Text.UTF8Encoding]::new($false)

function Write-Utf8NoBom([string]$Path, [string]$Content) {
  [System.IO.File]::WriteAllText($Path, $Content, $utf8NoBom)
}

$themeScript = @'
<script>
  (() => {
    const param = new URLSearchParams(window.location.search).get("clawpilotTheme");
    const theme =
      param || (window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light");
    document.documentElement.setAttribute("data-theme", theme);
  })();
</script>
'@

$themeCss = @'
:root {
  color-scheme: light;
  --cp-bg: #f7f4ef;
  --cp-bg-elevated: #fcfbf8;
  --cp-surface: #ffffff;
  --cp-surface-soft: #f5f5f5;
  --cp-border: #dedede;
  --cp-border-strong: #919191;
  --cp-text: #242424;
  --cp-text-muted: #5c5c5c;
  --cp-text-soft: #6f6f6f;
  --cp-accent: #b11f4b;
  --cp-accent-hover: #9a1a41;
  --cp-accent-soft: rgba(177, 31, 75, 0.08);
  --cp-accent-fg: #ffffff;
  --cp-success: #16a34a;
  --cp-danger: #dc2626;
  --cp-warning: #f59e0b;
  --cp-link: #0078d4;
  --cp-shadow: 0 18px 48px rgba(0, 0, 0, 0.12);
  --cp-overlay: rgba(255, 255, 255, 0.8);
  --cp-panel: rgba(255, 255, 255, 0.86);
  --cp-panel-strong: rgba(255, 255, 255, 0.96);
  --cp-sheen: rgba(255, 255, 255, 0.55);
  --cp-highlight: rgba(177, 31, 75, 0.12);
}
html[data-theme="dark"] {
  color-scheme: dark;
  --cp-bg: #3d3b3a;
  --cp-bg-elevated: #343231;
  --cp-surface: #292929;
  --cp-surface-soft: #2e2e2e;
  --cp-border: #474747;
  --cp-border-strong: #5f5f5f;
  --cp-text: #dedede;
  --cp-text-muted: #919191;
  --cp-text-soft: #b0b0b0;
  --cp-accent: #fd8ea1;
  --cp-accent-hover: #fb7b91;
  --cp-accent-soft: rgba(253, 142, 161, 0.14);
  --cp-accent-fg: #1a1a1a;
  --cp-success: #4ade80;
  --cp-danger: #f87171;
  --cp-warning: #fbbf24;
  --cp-link: #4da6ff;
  --cp-shadow: 0 18px 48px rgba(0, 0, 0, 0.32);
  --cp-overlay: rgba(41, 41, 41, 0.88);
  --cp-panel: rgba(41, 41, 41, 0.72);
  --cp-panel-strong: rgba(41, 41, 41, 0.96);
  --cp-sheen: rgba(255, 255, 255, 0.04);
  --cp-highlight: rgba(253, 142, 161, 0.12);
}
'@

$baseCss = @"
$themeCss
* { box-sizing: border-box; }
body { margin: 0; background: var(--cp-bg); color: var(--cp-text); font-family: "Segoe UI", Aptos, Calibri, -apple-system, BlinkMacSystemFont, sans-serif; line-height: 1.55; }
a { color: var(--cp-link); }
button, input { font: inherit; }
.shell { max-width: 1120px; margin: auto; padding: 24px; }
.topnav, .bottomnav { display: flex; align-items: center; justify-content: space-between; gap: 12px; padding: 14px 0; }
.topnav a, .bottomnav a { font-weight: 700; text-decoration: none; }
.crumb, .small, .meta { color: var(--cp-text-muted); }
header { padding: 32px 0 28px; border-block: 1px solid var(--cp-border); }
.eyebrow { color: var(--cp-accent); font-weight: 800; text-transform: uppercase; font-size: 0.8rem; }
h1 { max-width: 860px; margin: 8px 0 12px; font-size: clamp(2rem, 5vw, 3.7rem); line-height: 1.06; letter-spacing: 0; }
h2 { margin: 0 0 12px; font-size: 1.45rem; letter-spacing: 0; }
h3 { margin: 0 0 8px; font-size: 1.05rem; letter-spacing: 0; }
.lede { max-width: 780px; color: var(--cp-text-muted); font-size: 1.05rem; }
.meta { display: flex; flex-wrap: wrap; gap: 8px 18px; margin-top: 18px; font-size: 0.9rem; }
.start { display: inline-flex; align-items: center; margin-top: 24px; padding: 12px 18px; background: var(--cp-accent); color: var(--cp-accent-fg); border-radius: 0.625rem; text-decoration: none; font-weight: 800; }
.start:hover { background: var(--cp-accent-hover); }
main { padding: 30px 0; }
.roadmap { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 14px; }
.lab-card, .panel, .urlcard, .checklist, .task-card { background: var(--cp-surface); border: 1px solid var(--cp-border); border-radius: 16px; box-shadow: 0 0 2px var(--cp-border), 0 1px 2px var(--cp-border); }
.lab-card { display: flex; flex-direction: column; min-height: 250px; padding: 20px; border-top: 4px solid var(--cp-accent); text-decoration: none; color: var(--cp-text); }
.lab-card:hover { border-color: var(--cp-border-strong); transform: translateY(-2px); }
.number { width: 38px; height: 38px; display: grid; place-items: center; border-radius: 50%; background: var(--cp-accent); color: var(--cp-accent-fg); font-weight: 800; }
.lab-card h3 { margin: 16px 0 8px; }
.lab-card p, .task-card p, .panel p { color: var(--cp-text-muted); }
.outcome { margin-top: auto; padding-top: 18px; color: var(--cp-accent); font-weight: 700; }
.requirements, .track-grid { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 18px; margin-top: 28px; }
.panel { padding: 20px; }
.panel ul { margin: 8px 0 0; padding-left: 20px; }
.layout { display: grid; grid-template-columns: minmax(0, 1fr) 270px; gap: 28px; align-items: start; }
article { min-width: 0; }
aside { position: sticky; top: 18px; }
section { margin: 0 0 30px; }
.task-list { display: grid; gap: 14px; }
.task-card { padding: 18px; overflow-x: auto; }
.task-card ul, .task-card ol { margin: 8px 0 0; padding-left: 22px; }
.lab-sequence { display: grid; gap: 14px; }
.figure { margin: 14px 0 0; padding: 14px; background: var(--cp-surface); border: 1px solid var(--cp-border); border-radius: 16px; }
.figure img { display: block; max-width: 100%; height: auto; border: 1px solid var(--cp-border); border-radius: 0.625rem; }
.figure figcaption { margin-top: 8px; color: var(--cp-text-muted); font-size: 0.9rem; }
.column-table { width: 100%; max-width: 100%; table-layout: fixed; border-collapse: collapse; margin-top: 10px; font-size: 0.9rem; }
.column-table th, .column-table td { padding: 8px 10px; border: 1px solid var(--cp-border); text-align: left; vertical-align: top; }
.column-table th { background: var(--cp-surface-soft); color: var(--cp-text); }
.column-table td, .column-table th { overflow-wrap: anywhere; word-break: normal; }
.column-table code { font-family: Consolas, "Courier New", Courier, monospace; white-space: normal; overflow-wrap: anywhere; }
.steps { counter-reset: step; list-style: none; padding: 0; display: grid; gap: 16px; }
.steps > li { counter-increment: step; position: relative; padding: 18px 18px 18px 64px; background: var(--cp-surface); border: 1px solid var(--cp-border); border-radius: 16px; box-shadow: 0 0 2px var(--cp-border), 0 1px 2px var(--cp-border); }
.steps > li::before { content: counter(step); position: absolute; left: 18px; top: 18px; width: 32px; height: 32px; display: grid; place-items: center; border-radius: 50%; background: var(--cp-accent); color: var(--cp-accent-fg); font-weight: 800; }
.steps p { margin: 6px 0 0; color: var(--cp-text-muted); }
.tag { display: inline-flex; align-items: center; padding: 3px 8px; border-radius: 999px; background: var(--cp-accent-soft); color: var(--cp-accent); font-weight: 700; font-size: 0.78rem; }
.callout { padding: 16px; border-left: 4px solid var(--cp-warning); background: var(--cp-surface-soft); border-radius: 0 0.625rem 0.625rem 0; }
.callout.success { border-left-color: var(--cp-success); }
.urls { display: grid; gap: 12px; }
.urlcard { padding: 15px; }
.urlcard strong { display: block; margin-bottom: 6px; }
.code { display: block; overflow: auto; padding: 10px; background: var(--cp-surface-soft); border: 1px solid var(--cp-border); border-radius: 0.625rem; font: 12px/1.45 Consolas, "Courier New", Courier, monospace; white-space: nowrap; }
pre.code { white-space: pre; }
.answer-key { background: var(--cp-surface); border: 1px solid var(--cp-border); border-radius: 16px; box-shadow: 0 0 2px var(--cp-border), 0 1px 2px var(--cp-border); overflow: hidden; }
.answer-key summary { cursor: pointer; padding: 16px 18px; font-weight: 800; color: var(--cp-accent); background: var(--cp-surface-soft); }
.answer-key__body { padding: 18px; }
.answer-key__body p { color: var(--cp-text-muted); }
.copy { margin-top: 9px; padding: 7px 11px; border: 1px solid var(--cp-border-strong); border-radius: 0.625rem; background: var(--cp-surface); color: var(--cp-text); cursor: pointer; }
.copy:hover { border-color: var(--cp-accent); color: var(--cp-accent); }
.checklist { padding: 18px; }
.checklist label { display: flex; gap: 9px; align-items: flex-start; margin: 10px 0; }
.checklist input { margin-top: 5px; accent-color: var(--cp-accent); }
.progress { height: 7px; background: var(--cp-surface-soft); border-radius: 0.625rem; overflow: hidden; }
.bar { height: 100%; width: 0; background: var(--cp-accent); transition: width 0.2s; }
.bottomnav { border-top: 1px solid var(--cp-border); padding: 22px 0 34px; }
footer { padding: 24px 0 36px; border-top: 1px solid var(--cp-border); color: var(--cp-text-muted); font-size: 0.85rem; }
@media (max-width: 840px) { .roadmap, .requirements, .track-grid, .layout { grid-template-columns: 1fr; } aside { position: static; order: -1; } .shell { padding: 16px; } }
@media print { aside, .topnav, .bottomnav, .copy { display: none !important; } .layout { display: block !important; } .lab-card, .panel, .urlcard, .checklist, .task-card { box-shadow: none !important; break-inside: avoid-page; } }
"@

$printCss = @'
@page { size: letter; margin: 0.55in; }
body { font-size: 10pt; line-height: 1.4; print-color-adjust: exact; -webkit-print-color-adjust: exact; }
.shell { max-width: none !important; padding: 0 !important; }
header { padding: 14pt 0 !important; }
h1 { font-size: 25pt !important; }
h2 { font-size: 16pt !important; break-after: avoid-page; }
section, .panel, .urlcard, .checklist, .task-card { break-inside: avoid-page; }
a[href^="http"]::after { content: " (" attr(href) ")"; font-size: 8pt; overflow-wrap: anywhere; }
input[type="checkbox"] { appearance: none; width: 10pt; height: 10pt; border: 1pt solid var(--cp-border-strong); background: var(--cp-surface); }
'@

$brandJs = @'
(() => {
  const defaultBrand = {
    customerName: "Customer",
    workshopName: "Power BI Advanced Factory",
    titleSuffix: "",
    logoPath: "",
    badgePath: "",
    theme: {},
    icons: {}
  };
  const cssVarNames = {
    accent: "--cp-accent",
    accentHover: "--cp-accent-hover",
    accentSoft: "--cp-accent-soft",
    accentForeground: "--cp-accent-fg",
    link: "--cp-link"
  };
  const style = document.createElement("style");
  style.textContent = `
    .delivery-brand { display: flex; align-items: center; gap: 12px; min-height: 66px; padding: 12px 0; border-bottom: 1px solid var(--cp-border); }
    .delivery-brand__mark { width: 40px; height: 40px; display: grid; flex: 0 0 40px; place-items: center; overflow: hidden; background: var(--cp-accent); color: var(--cp-accent-fg); border-radius: 0.625rem; font-weight: 800; }
    .delivery-brand__mark img { width: 100%; height: 100%; padding: 6px; object-fit: contain; background: var(--cp-surface); }
    .delivery-brand__badge { display: block; width: min(100%, 430px); max-height: 74px; object-fit: contain; object-position: left center; }
    .delivery-brand__name, .delivery-brand__workshop { display: block; letter-spacing: 0; }
    .delivery-brand__name { color: var(--cp-text); font-size: 1rem; font-weight: 800; }
    .delivery-brand__workshop { color: var(--cp-text-muted); font-size: 0.78rem; }
  `;
  document.head.appendChild(style);

  function getConfigPath() {
    const script = document.currentScript || [...document.scripts].find((item) => item.src.endsWith("/delivery-brand.js"));
    const queryConfig = new URLSearchParams(window.location.search).get("brandConfig");
    return queryConfig || script?.dataset.config || "scripts/delivery-config.js";
  }
  function mergeBrandConfig(config) {
    return { ...defaultBrand, ...config, theme: { ...defaultBrand.theme, ...(config?.theme || {}) }, icons: { ...defaultBrand.icons, ...(config?.icons || {}) } };
  }
  function applyTheme(theme) {
    Object.entries(cssVarNames).forEach(([key, cssVar]) => {
      if (theme[key]) document.documentElement.style.setProperty(cssVar, theme[key]);
    });
  }
  function createMark(brand) {
    const mark = document.createElement("span");
    mark.className = "delivery-brand__mark";
    if (brand.logoPath) {
      const image = document.createElement("img");
      image.src = brand.logoPath;
      image.alt = "";
      mark.appendChild(image);
    } else {
      mark.textContent = (brand.customerName || "C").slice(0, 1).toUpperCase();
    }
    return mark;
  }
  function createTextBrand(brand) {
    const text = document.createElement("span");
    const customer = document.createElement("strong");
    customer.className = "delivery-brand__name";
    customer.textContent = brand.customerName;
    const workshop = document.createElement("span");
    workshop.className = "delivery-brand__workshop";
    workshop.textContent = brand.workshopName;
    text.append(customer, workshop);
    return text;
  }
  function createBadge(brand) {
    const badge = document.createElement("img");
    badge.className = "delivery-brand__badge";
    badge.src = brand.badgePath;
    badge.alt = `${brand.customerName} ${brand.workshopName}`;
    badge.onerror = () => badge.replaceWith(createMark(brand), createTextBrand(brand));
    return badge;
  }
  function renderBrand(brand) {
    applyTheme(brand.theme);
    const shell = document.querySelector(".shell");
    if (!shell || shell.querySelector(".delivery-brand")) return;
    const masthead = document.createElement("div");
    masthead.className = "delivery-brand";
    masthead.setAttribute("aria-label", `${brand.customerName} ${brand.workshopName}`);
    if (brand.badgePath) masthead.appendChild(createBadge(brand));
    else masthead.append(createMark(brand), createTextBrand(brand));
    shell.prepend(masthead);
    const suffix = brand.titleSuffix || brand.customerName;
    if (suffix && !document.title.endsWith(` - ${suffix}`)) document.title = `${document.title} - ${suffix}`;
  }
  function loadConfig() {
    return new Promise((resolve) => {
      if (window.deliveryBrandConfig) return resolve(window.deliveryBrandConfig);
      const script = document.createElement("script");
      script.src = getConfigPath();
      script.defer = true;
      script.onload = () => resolve(window.deliveryBrandConfig || {});
      script.onerror = () => resolve({});
      document.head.appendChild(script);
    });
  }
  const ready = (callback) => document.readyState === "loading" ? document.addEventListener("DOMContentLoaded", callback, { once: true }) : callback();
  loadConfig().then((config) => ready(() => renderBrand(mergeBrandConfig(config))));
})();
'@

$progressJs = @'
document.querySelectorAll(".copy").forEach((button) => {
  button.addEventListener("click", async () => {
    const text = document.getElementById(button.dataset.copy).textContent;
    await navigator.clipboard.writeText(text);
    const oldText = button.textContent;
    button.textContent = "Copied";
    setTimeout(() => button.textContent = oldText, 1200);
  });
});

document.querySelectorAll("[data-progress]").forEach((box) => {
  const key = "pbi-advanced-factory:" + box.dataset.progress;
  const checks = [...box.querySelectorAll("input")];
  let saved = [];
  try { saved = JSON.parse(localStorage.getItem(key) || "[]"); } catch {}
  checks.forEach((check, index) => {
    check.checked = !!saved[index];
    check.addEventListener("change", update);
  });
  function update() {
    const state = checks.map((check) => check.checked);
    localStorage.setItem(key, JSON.stringify(state));
    const done = state.filter(Boolean).length;
    box.querySelector(".count").textContent = done;
    box.querySelector(".bar").style.width = (checks.length ? done / checks.length * 100 : 0) + "%";
  }
  update();
});
'@

$deliveryConfig = @'
window.deliveryBrandConfig = {
  customerName: "Customer",
  workshopName: "Power BI Advanced Factory",
  titleSuffix: "Advanced Factory",
  logoPath: "",
  badgePath: "",
  theme: {
    accent: "#b11f4b",
    accentHover: "#9a1a41",
    accentSoft: "rgba(177, 31, 75, 0.08)",
    accentForeground: "#ffffff",
    link: "#0078d4"
  },
  icons: {}
};
'@

$brandingReadme = @'
# Customer Branding

Branding is controlled by `scripts\delivery-config.js`.

For each customer engagement:

1. Create a folder under `Branding\CustomerName`.
2. Add logo or badge SVG/PNG files.
3. Update `scripts\delivery-config.js` with customer name, workshop name, logo path, badge path, and theme values.
4. Open `index.html` to verify the masthead and accent color.

You can also test an alternate config by opening a page with:

```text
?brandConfig=Branding/CustomerName/delivery-config.js
```

Theme keys:

- `accent`
- `accentHover`
- `accentSoft`
- `accentForeground`
- `link`

Keep all lab HTML styling on the Clawpilot variables. Branding should only override the allowed variables through configuration.
'@

$modules = @(
  @{
    Number = "01"; File = "01-advanced-semantic-modeling.html"; Title = "Advanced Semantic Modeling"; Eyebrow = "Lab 1 - Semantic model foundation"; Level = "Advanced authoring"; Deliverable = "PBIP semantic model plan"; Summary = "Refactor a flat export into a reusable semantic model with facts, dimensions, role-playing dates, a segment bridge, targets, and Gov-aware optional storage-mode decisions.";
    Outcomes = @("Star schema from flat export", "Relationship setup reference", "Role-playing date tables", "Customer segment bridge", "Composite-model decision notes");
    Tasks = @(
      @{ Title = "Import the lab CSV sources"; Body = @("Use Get data > Web for sales-flat.csv, customer-segments.csv, and targets.csv.", "Keep the raw sales query as a source reference before creating model queries.") },
      @{ Title = "Refactor sales into facts and dimensions"; Body = @("Create FactSales, DimCustomer, DimProduct, DimProductCategory, and DimTerritory with the README column lists.", "Remove duplicate rows from dimensions and hide technical keys that are not useful to report consumers.") },
      @{ Title = "Create date roles"; Body = @("Build DimOrderDate and DimShipDate using the approved Power Query fn_DimDate or DAX CALENDAR pattern.", "Mark date tables and connect each role to the matching FactSales date column.") },
      @{ Title = "Configure relationships and targets"; Body = @("Create one-to-many, single-direction relationships from dimensions to facts and bridge tables.", "Use DimProductCategory for product-category target relationships instead of a many-to-many shortcut.") },
      @{ Title = "Add customer segment bridge"; Body = @("Create BridgeCustomerSegment and DimSegment from customer-segments.csv.", "Test segment filtering without duplicating customer rows.") },
      @{ Title = "Document optional storage choices"; Body = @("Compare Import, DirectQuery, Dual, composite, hybrid, and large-model tradeoffs.", "Keep tenant-dependent features marked Verify for Gov unless validated.") }
    );
    Checklist = @("Star schema created", "Fact and dimension names are clear", "Relationships validate as one-to-many where possible", "Filter direction is single unless justified", "Role-playing dates work", "Bridge table supports segment analysis", "Optional tenant-dependent features are labeled Verify for Gov", "Measures total correctly by date, product, customer, territory, and segment")
  },
  @{
    Number = "02"; File = "02-advanced-dax.html"; Title = "Advanced DAX"; Eyebrow = "Lab 2 - Measures and context"; Level = "Advanced authoring"; Deliverable = "Trusted measure layer"; Summary = "Build a tested DAX measure layer with evaluation context, CALCULATE patterns, time intelligence, semi-additive logic, calculation groups, ranking, dynamic logic, and optimization.";
    Outcomes = @("Base and branched measures", "CALCULATE filter modifiers", "Advanced time intelligence", "Semi-additive pattern", "Calculation groups", "Ranking and dynamic metric logic");
    Tasks = @(
      @{ Title = "Create and test base measures"; Body = @("Create Sales Amount, Quantity, Gross Margin, Gross Margin %, Target Sales Amount, Sales Variance, and Sales Variance %.", "Format and test each measure in a simple visual before branching.") },
      @{ Title = "Explore row and filter context"; Body = @("Use visuals and slicers to observe filter context.", "Create a calculated-column example only to demonstrate row context and why measures are preferred for aggregations.") },
      @{ Title = "Apply CALCULATE filter modifiers"; Body = @("Create filter-removal, product share, and KEEPFILTERS examples.", "Discuss REMOVEFILTERS, ALL, ALLEXCEPT, and TREATAS so learners choose modifiers intentionally.") },
      @{ Title = "Build time and semi-additive patterns"; Body = @("Create YTD, prior year, YoY, YoY %, and rolling 90-day measures.", "Review an ending-balance or last-nonblank pattern for snapshot facts.") },
      @{ Title = "Add ranking and dynamic logic"; Body = @("Create Customer Sales Rank and Is Top 5 Customer measures.", "Create a dynamic title and disconnected MetricSelector/SWITCH measure.") },
      @{ Title = "Review calculation groups"; Body = @("Use native Power BI Desktop calculation group authoring when available.", "Review TMDL View or Tabular Editor only when those workflows are validated; otherwise compare to separate measures.") },
      @{ Title = "Optimize and document"; Body = @("Use variables and measure branching to reduce repeated logic.", "Keep DAX Studio and external tooling optional and Verify for Gov.") }
    );
    Checklist = @("Base measures exist and are formatted", "CALCULATE examples validated", "Time intelligence works by month", "Semi-additive pattern explained or implemented", "Ranking/Top N works", "Dynamic title and metric switch created", "Calculation groups implemented or reviewed", "Variables and branching used", "External tooling marked Verify for Gov")
  },
  @{
    Number = "03"; File = "03-advanced-power-query.html"; Title = "Advanced Power Query"; Eyebrow = "Lab 3 - Data shaping"; Level = "Advanced authoring"; Deliverable = "Reusable Power Query pipeline"; Summary = "Create a staged Power Query pipeline from monthly Web CSVs with parameters, source lineage, reusable functions, data quality review, folding concepts, and incremental refresh preparation.";
    Outcomes = @("Staged query architecture", "Parameter reference", "Folder/append pattern", "Reusable M function", "Data quality review", "Incremental refresh prep");
    Tasks = @(
      @{ Title = "Create parameters and Web sources"; Body = @("Create RawDataBaseUrl, SourceFolderPath, EnvironmentName, RangeStart, and RangeEnd.", "Use Get data > Web for the three monthly order CSV files and name raw queries by source month.") },
      @{ Title = "Append and stage monthly files"; Body = @("Add a SourceFile lineage column to each raw query.", "Append into stg_OrdersCombined and disable load for raw and staging queries.") },
      @{ Title = "Document source switching"; Body = @("Keep the required Web-source queries pointed at RawDataBaseUrl.", "Document how EnvironmentName and optional SourceFolderPath would map to Dev/Test/Prod or offline delivery.") },
      @{ Title = "Create reusable cleanup logic"; Body = @("Create fn_CleanText for null-safe trim, clean, and proper-case logic.", "Invoke it for customer/channel and product reference text fields.") },
      @{ Title = "Review data quality and errors"; Body = @("Create err_OrdersReview as a disabled-load reference of stg_OrdersCombined.", "Keep valid rows in FactOrders and preserve readable DataQualityIssue reasons for excluded rows.") },
      @{ Title = "Validate folding and refresh readiness"; Body = @("Discuss folding blockers for file sources and validate View Native Query only with a folding-capable source.", "Filter FactOrders[OrderDate] with RangeStart and RangeEnd and mark Service incremental refresh Verify for Gov.") }
    );
    Checklist = @("Raw and staging queries have load disabled", "Final fact query has explicit data types", "Monthly files append with SourceFile lineage", "All five parameters documented", "Custom text cleanup function handles nulls", "Data quality issues identified and documented", "Query folding demonstrated or explained with source limitations", "RangeStart and RangeEnd are DateTime", "Service features include Gov notes")
  },
  @{
    Number = "04"; File = "04-report-design-ux.html"; Title = "Report Design and UX"; Eyebrow = "Lab 4 - Guided report experience"; Level = "Advanced authoring"; Deliverable = "Interactive report pages"; Summary = "Design audience-focused report pages with clear filters, drillthrough, tooltips, bookmarks, navigation, field parameters, conditional formatting, mobile layout, and accessibility review.";
    Outcomes = @("Audience-focused pages", "Drillthrough details", "Report page tooltip", "Bookmarks and navigation", "Field parameters and selectors", "Mobile and accessibility review");
    Tasks = @(
      @{ Title = "Plan audience pages and filters"; Body = @("Define executive, analyst, and operational/detail page purposes.", "Place slicers and page filters consistently so users understand report context.") },
      @{ Title = "Add drillthrough and tooltips"; Body = @("Create Customer Detail drillthrough with Back navigation.", "Create and assign a compact Sales Tooltip page.") },
      @{ Title = "Add bookmarks and navigation"; Body = @("Use Show/Hide or Reset bookmarks with intentional Data, Display, and Current page settings.", "Add page navigation buttons or a navigator with consistent labels.") },
      @{ Title = "Add guided metric exploration"; Body = @("Create Metric Parameter and optional Dimension Parameter field parameters.", "Compare the native field parameter to a disconnected Metric Selector SWITCH pattern.") },
      @{ Title = "Add target-driven formatting"; Body = @("Create the optional Margin Target disconnected table and measures if time allows.", "Use conditional formatting with documented thresholds and non-color cues.") },
      @{ Title = "Create mobile and accessible experiences"; Body = @("Build a mobile layout with prioritized visuals and touch-friendly sizing.", "Add alt text, tab order, contrast checks, descriptive titles, and keyboard-friendly design.") }
    );
    Checklist = @("Report pages have clear audience and purpose", "Filters and slicers are understandable", "Drillthrough works", "Tooltip page assigned", "Bookmarks capture only intended behavior", "Navigation buttons are consistent", "Field parameter switches intended fields", "Conditional formatting has documented thresholds", "Mobile layout is readable", "Accessibility review is complete", "Personalized and AI visuals have Gov notes")
  },
  @{
    Number = "05"; File = "05-performance-optimization.html"; Title = "Performance Optimization"; Eyebrow = "Lab 5 - Measure, optimize, validate"; Level = "Advanced authoring"; Deliverable = "Performance improvement notes"; Summary = "Use an evidence-driven workflow to diagnose report, model, DAX, visual, refresh, and capacity performance.";
    Outcomes = @("Performance Analyzer baseline", "Model reduction plan", "DAX optimization", "Before/after performance evidence");
    Tasks = @(
      @{ Title = "Capture and benchmark a baseline"; Body = @("Use Performance Analyzer to record DAX query time, visual display time, and other time.", "Change one thing at a time and capture before/after observations with the same interaction.") },
      @{ Title = "Review model size and cardinality"; Body = @("Identify unused columns, high-cardinality text fields, date/time columns, and excessive numeric precision.", "Document model-reduction recommendations before changing production models.") },
      @{ Title = "Optimize DAX and visuals"; Body = @("Refactor repeated DAX with variables or measure branching.", "Reduce low-value visuals, dense tables, unnecessary interactions, and high-cardinality visual detail.") },
      @{ Title = "Review refresh and Power Query design"; Body = @("Filter early, remove columns early, preserve folding where supported, and keep staging queries clear.", "Confirm RangeStart/RangeEnd and the fact date/time column for incremental refresh readiness.") },
      @{ Title = "Document aggregations and capacity notes"; Body = @("Define a summary grain and explain Import, DirectQuery, or hybrid tradeoffs.", "Mark DAX Studio, VertiPaq Analyzer, Service incremental refresh, capacity metrics, and unvalidated sources as Verify for Gov.") }
    );
    Checklist = @("Performance Analyzer baseline captured", "Before/after benchmark observations recorded", "Model size/cardinality recommendations documented", "DAX optimization uses variables or measure branching", "Visual count/interactions reviewed", "Aggregation table grain documented", "Incremental refresh parameters and policy documented", "DAX Studio, VertiPaq Analyzer, and capacity metrics marked Verify for Gov")
  },
  @{
    Number = "06"; File = "06-advanced-analytics-ai.html"; Title = "Advanced Analytics and AI"; Eyebrow = "Lab 6 - Scenario and AI-aware analysis"; Level = "Feature module"; Deliverable = "Analytics scenario and Gov-safe alternatives"; Summary = "Use what-if parameters as the Gov-ready core and evaluate advanced/AI features only when tenant availability is validated.";
    Outcomes = @("What-if parameter", "Driver-analysis options", "AI feature validation", "Gov-safe fallback map");
    Tasks = @(
      @{ Title = "Create what-if scenario"; Body = @("Create Margin Adjustment %.", "Build adjusted gross margin measures and visuals.") },
      @{ Title = "Evaluate advanced visuals"; Body = @("Use decomposition tree, forecasting, anomaly detection, or key influencers only if available.", "Document interpretation limits and human validation requirements.") },
      @{ Title = "Review code and ML options"; Body = @("Keep Python/R visuals and Azure ML optional.", "Document runtime, package, identity, network, region, data residency, and Service requirements.") },
      @{ Title = "Discuss Copilot"; Body = @("Use the conceptual section unless Copilot is validated.", "Require human review for AI-generated output.") },
      @{ Title = "Map Gov-safe fallbacks"; Body = @("Provide matrix/drillthrough, DAX thresholds, Top N, rolling averages, prior-period comparison, and native visual alternatives.") }
    );
    Checklist = @("What-if parameter works", "Scenario measures respond to parameter selection", "Optional AI/advanced visuals labeled", "Gov-safe fallback documented for each optional feature", "Python/R and Azure ML prerequisites documented if discussed", "Copilot treated as optional", "Human review requirement noted")
  },
  @{
    Number = "07"; File = "07-security-design.html"; Title = "Security Design"; Eyebrow = "Lab 7 - RLS and governance"; Level = "Governance"; Deliverable = "Security test evidence"; Summary = "Configure static and dynamic RLS, test roles, review Build permission, and document OLS, Purview, labels, external sharing, and B2B validation needs.";
    Outcomes = @("Static RLS", "Dynamic RLS", "Role testing evidence", "Security review checklist");
    Tasks = @(
      @{ Title = "Load security mapping"; Body = @("Use Get data > Web for security-user-territory and security-role-matrix.", "Relate SecurityUserTerritory to DimTerritory using TerritoryKey.") },
      @{ Title = "Create RLS roles"; Body = @("Create the East Region static role.", "Create Dynamic Territory Security with USERPRINCIPALNAME().") },
      @{ Title = "Test roles in Desktop and Service"; Body = @("Use View as in Desktop with sample UPNs.", "Assign users or groups to Service roles and document gaps where Service testing is unavailable.") },
      @{ Title = "Review Build permission and sharing"; Body = @("Document who can build thin reports or Analyze in Excel.", "Separate content access, semantic model reuse, App distribution, and external/B2B sharing decisions.") },
      @{ Title = "Document optional controls"; Body = @("Mark OLS, sensitivity labels, Purview, external sharing, and B2B as Verify for Gov unless validated.") }
    );
    Checklist = @("Security data loaded", "Static RLS created", "Dynamic RLS created", "Desktop role test documented", "Service role assignment reviewed", "Build permission behavior documented", "External sharing/B2B limitations documented", "Gov validation notes captured")
  },
  @{
    Number = "08"; File = "08-service-enterprise-deployment.html"; Title = "Service Enterprise Deployment"; Eyebrow = "Lab 8 - Publish and distribute"; Level = "Operations"; Deliverable = "Published workspace/App plan"; Summary = "Publish PBIP-authored content to the Service, configure refresh, review gateways, shared semantic models, Apps, App audiences, deployment pipelines, and endorsement.";
    Outcomes = @("Workspace design and roles", "Refresh and gateway notes", "App packaging", "Endorsement checklist");
    Tasks = @(
      @{ Title = "Plan workspace design and roles"; Body = @("Document dev/test/prod or training workspace intent, naming convention, domain/subject area, owners, and support model.", "Assign least-privileged Admin, Member, Contributor, or Viewer roles.") },
      @{ Title = "Publish content"; Body = @("Publish from the PBIP-authored report.", "Verify the report and semantic model in the Service and record owner/workspace details.") },
      @{ Title = "Configure refresh"; Body = @("Review credentials, privacy levels, schedule, refresh history, and ownership.", "Document gateway or cloud connection requirements.") },
      @{ Title = "Review reuse and distribution"; Body = @("Create or discuss thin report/Build permission.", "Package content as an App and validate the consumer path where available.") },
      @{ Title = "Apply deployment governance"; Body = @("Complete promoted/certified endorsement checklist.", "Keep App audiences and deployment pipelines Verify for Gov and document a manual promotion path if unavailable.") }
    );
    Checklist = @("Workspace design, role, and ownership documented", "Report/model published or demonstrated", "Refresh settings and history reviewed", "Gateway/cloud connection notes captured", "Shared semantic model and Build permission reviewed", "App distribution reviewed", "App audiences and deployment pipelines marked Verify for Gov", "Endorsement checklist completed")
  },
  @{
    Number = "09"; File = "09-monitoring-governance.html"; Title = "Monitoring and Governance"; Eyebrow = "Lab 9 - Operate and support"; Level = "Operations"; Deliverable = "Operations runbook"; Summary = "Monitor adoption, troubleshoot refresh, review tenant settings, inspect gateways, and document support operations.";
    Outcomes = @("Usage and adoption review", "Refresh troubleshooting", "Tenant setting notes", "Operations runbook");
    Tasks = @(
      @{ Title = "Review usage and adoption"; Body = @("Open usage metrics where available.", "Document adoption observations, training needs, support signals, and retirement candidates.") },
      @{ Title = "Troubleshoot refresh"; Body = @("Review refresh history, credentials, and gateway mapping.", "Document likely causes and next actions.") },
      @{ Title = "Review governance settings"; Body = @("Review sharing, export, publish-to-web, external users, Build permission, and certification controls.", "Use read-only review unless approved.") },
      @{ Title = "Review optional admin signals"; Body = @("Activity logs, admin monitoring, capacity metrics, Purview, and DLP are Verify for Gov.", "Record available evidence and access blockers.") },
      @{ Title = "Complete operations runbook"; Body = @("Document owners, sources, refresh, access, monitoring cadence, incident response, and Azure Government validation notes.") }
    );
    Checklist = @("Usage reviewed", "Adoption follow-up documented", "Refresh process documented", "Tenant settings reviewed", "Gateway notes captured", "Optional admin features labeled", "Runbook completed")
  },
  @{
    Number = "10"; File = "10-premium-fabric-capacity.html"; Title = "Premium, Fabric, and Capacity"; Eyebrow = "Lab 10 - Architecture decisions"; Level = "Architecture"; Deliverable = "Capacity architecture recommendation"; Summary = "Compare Pro, PPU, Premium, and Fabric capacity and evaluate XMLA, paginated reports, Direct Lake, OneLake, Semantic Link, capacity metrics, and Gov-safe alternatives.";
    Outcomes = @("Capacity comparison", "XMLA/paginated/large-model validation", "Fabric feature validation", "Gov-safe architecture", "Capacity metrics concepts");
    Tasks = @(
      @{ Title = "Compare licensing and capacity options"; Body = @("Define user scale, model size, refresh, latency, governance, and integration needs.", "Compare Pro, PPU, Premium capacity, and Fabric capacity.") },
      @{ Title = "Review XMLA endpoint"; Body = @("Validate capacity, tenant settings, workspace configuration, tooling, and cloud support.", "Document read/write and ALM use cases.") },
      @{ Title = "Review paginated reports and large models"; Body = @("Validate paginated report licensing, workspace support, Report Builder use, and export behavior.", "Document large semantic model size, memory, refresh, and storage-format considerations.") },
      @{ Title = "Review Fabric concepts"; Body = @("Direct Lake, OneLake, Lakehouse, Warehouse, Semantic Link, and autoscale are Commercial-focused / Verify for Gov.", "Document fallback paths when these features are not validated.") },
      @{ Title = "Review capacity metrics and choose architecture"; Body = @("Map interactive workload, background workload, refresh pressure, and throttling symptoms to operational actions.", "Record the recommended architecture, risks, validation needs, and Gov-safe fallback.") }
    );
    Checklist = @("Workload documented", "Capacity options compared", "XMLA/paginated/large model notes captured", "Fabric features labeled", "Semantic Link and autoscale labeled", "Capacity metrics discussed", "Gov-safe architecture selected")
  },
  @{
    Number = "11"; File = "11-automation-devops.html"; Title = "Automation and DevOps"; Eyebrow = "Lab 11 - PBIP lifecycle"; Level = "DevOps"; Deliverable = "Deployment checklist"; Summary = "Use PBIP and git as the source-control foundation, then review external tools, APIs, service principals, Fabric Git integration, and conceptual CI/CD.";
    Outcomes = @("Lifecycle goals", "PBIP source review", "Git workflow", "Automation validation", "Deployment checklist");
    Tasks = @(
      @{ Title = "Define lifecycle goals"; Body = @("Document repeatability, reviewability, promotion, governance, and rollback expectations.", "Confirm PBIX is not the source of record.") },
      @{ Title = "Review PBIP structure"; Body = @("Inspect report and semantic model source files.", "Identify generated or binary files that should not drive review.") },
      @{ Title = "Practice git workflow"; Body = @("Create a branch, make a small change, review status/diff, and commit.", "Discuss pull request review, tags, releases, and rollback evidence.") },
      @{ Title = "Review external tools and automation"; Body = @("Tabular Editor, ALM Toolkit, REST APIs, PowerShell, and service principals are Verify for Gov.", "Document XMLA, endpoint, identity, permission, and workstation policy needs.") },
      @{ Title = "Review Fabric Git and CI/CD"; Body = @("Fabric workspace Git integration is Commercial-focused / Verify for Gov.", "Azure DevOps and GitHub Actions require endpoint, identity, network, and policy validation.") },
      @{ Title = "Complete deployment checklist"; Body = @("Document source, security, refresh, environment config, automation validation, Azure Government validation, release evidence, and rollback path.") }
    );
    Checklist = @("Lifecycle goals documented", "PBIP structure reviewed", "Git workflow and PR/release expectations documented", "External tools labeled", "API/service principal validation documented", "Fabric Git caveats documented", "CI/CD path selected", "Gov endpoint/identity/network validation documented", "Deployment checklist completed")
  },
  @{
    Number = "12"; File = "12-capstone.html"; Title = "Capstone"; Eyebrow = "Lab 12 - Enterprise-ready solution"; Level = "Applied capstone"; Deliverable = "Validated PBIP solution package"; Summary = "Bring together modeling, DAX, report UX, performance, security, Service deployment, governance, monitoring, and lifecycle management.";
    Outcomes = @("PBIP source project", "Optimized model and DAX", "Interactive report experience", "RLS-secured deployment", "Governance and operations evidence");
    Tasks = @(
      @{ Title = "Build the semantic model"; Body = @("Create fact and dimension tables, relationships, hidden technical fields, and model-grain documentation.", "Document Gov-sensitive features as Gov-ready, Verify for Gov, or Commercial-focused.") },
      @{ Title = "Add advanced DAX"; Body = @("Create base, time-intelligence, variance, ranking/Top N, dynamic title, or measure-switching logic.", "Validate totals at multiple grains.") },
      @{ Title = "Build the report experience"; Body = @("Create executive, analyst, detail drillthrough, tooltip, bookmark/button, conditional formatting, mobile layout, and accessibility evidence.") },
      @{ Title = "Configure security"; Body = @("Create static and dynamic RLS, test in Desktop and Service where available, and document Build permission behavior.") },
      @{ Title = "Publish and distribute"; Body = @("Publish from PBIP-authored content, configure credentials and refresh where available, document gateway requirements, and create or review a Power BI App.") },
      @{ Title = "Govern and operate"; Body = @("Complete endorsement governance, operations runbook, usage metrics review, refresh history review, support ownership, and escalation path.") },
      @{ Title = "Optional enhanced extensions"; Body = @("Add Fabric/Git/Copilot/AI/API/automation features only after validation.", "Document availability status and fallback path for every optional feature.") }
    );
    Checklist = @("PBIP source project used", "Semantic model follows star schema principles", "Advanced DAX measures validated", "Report UX and accessibility complete", "Static and dynamic RLS tested", "Service/App path completed or documented", "Refresh and gateway requirements documented", "Endorsement checklist complete", "Operations runbook complete", "Monitoring and support tasks documented", "Optional enhanced features validated and labeled", "Rubric and evidence package submitted")
  }
)

function HtmlEncode([string]$value) {
  return [System.Net.WebUtility]::HtmlEncode($value)
}

function RenderList($items) {
  (($items | ForEach-Object { "<li>$(HtmlEncode $_)</li>" }) -join "`n")
}

function RenderTasks($tasks) {
  (($tasks | ForEach-Object {
    $body = RenderList $_.Body
    @"
<div class="task-card">
  <h3>$(HtmlEncode $_.Title)</h3>
  <ul>
    $body
  </ul>
</div>
"@
  }) -join "`n")
}

function RenderChecklist($module) {
  (($module.Checklist | ForEach-Object { "<label><input type=""checkbox"">$(HtmlEncode $_)</label>" }) -join "`n")
}

function RenderUrls($moduleNumber) {
  if ($moduleNumber -eq "01") {
    return @'
<section>
  <h2>Source files</h2>
  <div class="urls">
    <div class="urlcard"><strong>sales-flat.csv</strong><code class="code" id="u1">https://raw.githubusercontent.com/Coding-Forge/PBI-Advanced-Factory/main/data/sales-flat.csv</code><button class="copy" data-copy="u1">Copy URL</button></div>
    <div class="urlcard"><strong>customer-segments.csv</strong><code class="code" id="u2">https://raw.githubusercontent.com/Coding-Forge/PBI-Advanced-Factory/main/data/customer-segments.csv</code><button class="copy" data-copy="u2">Copy URL</button></div>
    <div class="urlcard"><strong>targets.csv</strong><code class="code" id="u3">https://raw.githubusercontent.com/Coding-Forge/PBI-Advanced-Factory/main/data/targets.csv</code><button class="copy" data-copy="u3">Copy URL</button></div>
  </div>
</section>
'@
  }
  if ($moduleNumber -eq "03") {
    return @'
<section>
  <h2>Source files</h2>
  <div class="urls">
    <div class="urlcard"><strong>orders-2026-01.csv</strong><code class="code" id="u1">https://raw.githubusercontent.com/Coding-Forge/PBI-Advanced-Factory/main/data/monthly-orders/orders-2026-01.csv</code><button class="copy" data-copy="u1">Copy URL</button></div>
    <div class="urlcard"><strong>orders-2026-02.csv</strong><code class="code" id="u2">https://raw.githubusercontent.com/Coding-Forge/PBI-Advanced-Factory/main/data/monthly-orders/orders-2026-02.csv</code><button class="copy" data-copy="u2">Copy URL</button></div>
    <div class="urlcard"><strong>orders-2026-03.csv</strong><code class="code" id="u3">https://raw.githubusercontent.com/Coding-Forge/PBI-Advanced-Factory/main/data/monthly-orders/orders-2026-03.csv</code><button class="copy" data-copy="u3">Copy URL</button></div>
    <div class="urlcard"><strong>product-category-map.csv</strong><code class="code" id="u4">https://raw.githubusercontent.com/Coding-Forge/PBI-Advanced-Factory/main/data/reference/product-category-map.csv</code><button class="copy" data-copy="u4">Copy URL</button></div>
  </div>
</section>
'@
  }
  if ($moduleNumber -eq "07") {
    return @'
<section>
  <h2>Source files</h2>
  <div class="urls">
    <div class="urlcard"><strong>security-user-territory.csv</strong><code class="code" id="u1">https://raw.githubusercontent.com/Coding-Forge/PBI-Advanced-Factory/main/data/security/security-user-territory.csv</code><button class="copy" data-copy="u1">Copy URL</button></div>
    <div class="urlcard"><strong>security-role-matrix.csv</strong><code class="code" id="u2">https://raw.githubusercontent.com/Coding-Forge/PBI-Advanced-Factory/main/data/security/security-role-matrix.csv</code><button class="copy" data-copy="u2">Copy URL</button></div>
  </div>
</section>
'@
  }
  return ""
}

function RenderLabSequence($moduleNumber) {
  $labReadme = Get-ChildItem -Path (Join-Path $repoRoot "Student\Labs\Source") -Directory |
    Where-Object { $_.Name -like "$moduleNumber-*" } |
    Select-Object -First 1 |
    ForEach-Object { Join-Path $_.FullName "README.md" }

  if (-not $labReadme -or -not (Test-Path $labReadme)) {
    return ""
  }

  $content = Get-Content -Path $labReadme -Raw
  $matches = [regex]::Matches($content, '(?ms)^## (?<title>Lab \d+: [^\r\n]+)(?<body>.*?)(?=^## |\z)')

  if ($matches.Count -eq 0) {
    return ""
  }

  $cards = foreach ($match in $matches) {
    $title = HtmlEncode $match.Groups["title"].Value
    $body = $match.Groups["body"].Value
    $objectiveMatch = [regex]::Match($body, '\*\*Objective:\*\*\s*(?<objective>[^\r\n]+)')
    $objective = if ($objectiveMatch.Success) { HtmlEncode $objectiveMatch.Groups["objective"].Value.Trim() } else { "See the lab README for detailed instructions." }
    $status =
      if ($body -match '\*\*Commercial-focused\*\*|Commercial-focused') { "Commercial-focused" }
      elseif ($body -match '\*\*Verify for Gov\*\*|Verify for Gov') { "Verify for Gov" }
      elseif ($body -match '\*\*Gov-ready\*\*|Gov-ready') { "Gov-ready" }
      else { "Core or module-dependent" }

    @"
<div class="task-card">
  <h3>$title <span class="tag">$(HtmlEncode $status)</span></h3>
  <p>$objective</p>
</div>
"@
  }

  @"
<section>
  <h2>Module lab sequence</h2>
  <p class="small">This sequence is generated from the matching lab README so the Markdown and HTML paths expose the same numbered labs.</p>
  <div class="lab-sequence">$($cards -join "`n")</div>
</section>
"@
}

function RenderHowToGuide($moduleNumber) {
  switch ($moduleNumber) {
    "01" { return @'
<section><h2>Novice-friendly how-to guide</h2><div class="task-list">
<div class="task-card"><h3>Reference a raw query into facts and dimensions</h3><ol><li>Right-click <code>raw_SalesFlat</code> and choose <strong>Reference</strong>.</li><li>Rename the new query to <code>FactSales</code>, <code>DimCustomer</code>, <code>DimProduct</code>, or <code>DimTerritory</code>.</li><li>Keep or remove columns to match the README table.</li><li>Remove duplicate rows from dimensions only.</li></ol></div>
<div class="task-card"><h3>Create DimProductCategory</h3><ol><li>Reference <code>DimProduct</code>.</li><li>Rename the query <code>DimProductCategory</code>.</li><li>Remove <code>ProductKey</code>, <code>ProductName</code>, and <code>ProductSubcategory</code>.</li><li>Keep only <code>ProductCategory</code>, confirm text type, and remove duplicates.</li></ol></div>
<div class="task-card"><h3>Create date role tables</h3><ol><li>Use the approved <code>fn_DimDate</code> or DAX <code>CALENDAR</code> pattern.</li><li>Create <code>DimOrderDate</code> and <code>DimShipDate</code>.</li><li>Mark each table as a date table.</li><li>Relate each role table to the matching fact date column.</li></ol></div>
<div class="task-card"><h3>Create relationships in Model view</h3><ol><li>Drag each dimension primary key to the matching fact or bridge foreign key.</li><li>Confirm one-to-many cardinality, single cross-filter direction, and active status.</li><li>Use <code>DimProductCategory</code> for target category relationships.</li></ol></div>
<div class="task-card"><h3>Evaluate composite model choices</h3><ol><li>Identify Import, DirectQuery, and Dual candidates.</li><li>Document freshness, performance, source-load, gateway, and tenant constraints.</li><li>Keep composite, DirectQuery, hybrid, and large-model work marked Verify for Gov unless validated.</li></ol></div>
</div></section>
'@ }
    "02" { return @'
<section><h2>Novice-friendly how-to guide</h2><div class="task-list">
<div class="task-card"><h3>Create a measure</h3><ol><li>Select the table that should store the measure.</li><li>Select <strong>Modeling &gt; New measure</strong>.</li><li>Type the measure name, equals sign, and DAX expression.</li><li>Set formatting and test in a simple visual.</li></ol></div>
<div class="task-card"><h3>Build a DAX test visual</h3><ol><li>Add a table or matrix visual.</li><li>Add one dimension field and the measure being tested.</li><li>Add slicers for date, territory, or product category.</li><li>Change slicer selections and verify totals.</li></ol></div>
<div class="task-card"><h3>Use CALCULATE safely</h3><ol><li>Start from a working base measure.</li><li>Use <code>REMOVEFILTERS</code> to ignore a dimension intentionally.</li><li>Use <code>ALLEXCEPT</code> only to preserve a named grain.</li><li>Use <code>KEEPFILTERS</code> to narrow existing filters.</li><li>Use <code>TREATAS</code> for intentional disconnected-table filtering.</li></ol></div>
<div class="task-card"><h3>Create a calculation group</h3><ol><li>Confirm explicit base measures work.</li><li>Open <strong>Model view</strong> and select <strong>Calculation group</strong>.</li><li>Enable <strong>Discourage implicit measures</strong> if prompted.</li><li>Name the table <code>Time Intelligence</code> and the column <code>Time Calculation</code>.</li><li>Add calculation items and test with base measures.</li></ol></div>
<div class="task-card"><h3>Review TMDL or external-tool paths</h3><ol><li>Use TMDL View or Tabular Editor only when validated.</li><li>If no calculation group authoring path is validated, use separate DAX measures as the fallback.</li></ol></div>
</div><figure class="figure"><img src="images/02-advanced-dax/CalculationGroups-annotated.png" alt="Annotated Power BI Desktop Model view showing a calculation group, its column, and calculation items."><figcaption>Calculation group authoring in Power BI Desktop Model view.</figcaption></figure></section>
'@ }
    "03" { return @'
<section><h2>Novice-friendly how-to guide</h2><div class="task-list">
<div class="task-card"><h3>Create Power Query parameters</h3><ol><li>Open <strong>Transform data</strong>.</li><li>Select <strong>Manage Parameters &gt; New Parameter</strong>.</li><li>Create <code>RawDataBaseUrl</code>, <code>SourceFolderPath</code>, <code>EnvironmentName</code>, <code>RangeStart</code>, and <code>RangeEnd</code>.</li><li>Keep <code>SourceFolderPath</code> blank unless using offline delivery.</li></ol></div>
<div class="task-card"><h3>Append queries</h3><ol><li>Select <strong>Home &gt; Append Queries &gt; Append Queries as New</strong>.</li><li>Choose <strong>Three or more tables</strong>.</li><li>Add each raw monthly query in order.</li><li>Name the result <code>stg_OrdersCombined</code>.</li></ol></div>
<div class="task-card"><h3>Create a custom function</h3><ol><li>Create a Blank Query named <code>fn_CleanText</code>.</li><li>Paste the function from the answer key in Advanced Editor.</li><li>Invoke it on selected customer, channel, and product text columns.</li></ol></div>
<div class="task-card"><h3>Use column quality and error review</h3><ol><li>Turn on column quality or profile.</li><li>Create readable <code>DataQualityIssue</code> reasons.</li><li>Reference <code>stg_OrdersCombined</code> as <code>err_OrdersReview</code>.</li><li>Disable load for the error review query.</li></ol></div>
<div class="task-card"><h3>Disable load for staging queries</h3><ol><li>Right-click raw and staging queries.</li><li>Clear <strong>Enable load</strong>.</li><li>Leave final model-ready queries enabled.</li></ol></div>
</div></section>
'@ }
    "04" { return @'
<section><h2>Novice-friendly how-to guide</h2><div class="task-list">
<div class="task-card"><h3>Plan audience pages and filters</h3><ol><li>Write the audience and decision question for each page.</li><li>Use executive, analyst, and operational/detail purposes to decide visuals.</li><li>Place slicers consistently and label them clearly.</li><li>Avoid hidden or conflicting filter states.</li></ol></div>
<div class="task-card"><h3>Create a drillthrough page</h3><ol><li>Add a page named <code>Customer Detail</code>.</li><li>Add <code>DimCustomer[CustomerName]</code> to the Drill-through field well.</li><li>Add customer visuals and a Back button.</li><li>Test by right-clicking a customer on another page.</li></ol></div>
<div class="task-card"><h3>Create a tooltip page</h3><ol><li>Add a page and set page type to <strong>Tooltip</strong>.</li><li>Build compact KPIs or a trend.</li><li>Assign the tooltip page to a main visual.</li></ol></div>
<div class="task-card"><h3>Create a field parameter</h3><ol><li>Select <strong>Modeling &gt; New parameter &gt; Fields</strong>.</li><li>Name it <code>Metric Parameter</code>.</li><li>Select <code>[Sales Amount]</code>, <code>[Gross Margin]</code>, <code>[Gross Margin %]</code>, and <code>[Quantity]</code>.</li><li>Add the generated parameter field to a visual.</li></ol></div>
<div class="task-card"><h3>Review accessibility</h3><ol><li>Add descriptive titles and alt text.</li><li>Set a logical tab order.</li><li>Check contrast and avoid color-only meaning.</li><li>Confirm keyboard users can follow the report flow.</li></ol></div>
</div></section>
<section><h2>Deeper Understanding Challenge</h2><div class="task-card"><h3>Build a disconnected metric selector</h3><p>Compare native field parameters with a Power Query selector table and a DAX <code>SWITCH</code> measure.</p><ol><li>Create a blank Power Query named <code>Metric Selector</code>.</li><li>Use <code>#table</code> to create rows for Sales Amount, Gross Margin, Gross Margin %, and Quantity.</li><li>Load the table without relationships.</li><li>Create <code>Selected Metric Value</code> using <code>SELECTEDVALUE</code> and <code>SWITCH</code>.</li></ol><pre class="code"><code>let
    Source =
        #table(
            type table [Metric = text, SortOrder = Int64.Type],
            {
                {"Sales Amount", 0},
                {"Gross Margin", 1},
                {"Gross Margin %", 2},
                {"Quantity", 3}
            }
        )
in
    Source</code></pre><pre class="code"><code>Selected Metric Value =
VAR SelectedMetric =
    SELECTEDVALUE ( 'Metric Selector'[Metric], "Sales Amount" )
RETURN
    SWITCH (
        SelectedMetric,
        "Sales Amount", [Sales Amount],
        "Gross Margin", [Gross Margin],
        "Gross Margin %", [Gross Margin %],
        "Quantity", [Quantity],
        [Sales Amount]
    )</code></pre></div></section>
'@ }
    "05" { return @'
<section>
  <h2>Novice-friendly how-to guide</h2>
  <div class="task-list">
    <div class="task-card"><h3>Use Performance Analyzer</h3><ol><li>Open the report page to test.</li><li>Select <strong>View &gt; Performance Analyzer</strong>.</li><li>Select <strong>Start recording</strong>.</li><li>Refresh visuals or interact with slicers.</li><li>Expand each visual result and record DAX query time, visual display time, and other time.</li></ol></div>
    <div class="task-card"><h3>Document before/after benchmark evidence</h3><ol><li>Record the baseline timing before changing anything.</li><li>Change one thing at a time.</li><li>Run the same interaction again.</li><li>Record the after timing, tradeoff, and remaining risk.</li></ol></div>
    <div class="task-card"><h3>Reduce model size</h3><ol><li>Review columns in Data or Model view.</li><li>Identify columns not used in relationships, measures, slicers, or visuals.</li><li>Remove unused columns in Power Query, not just hide them.</li><li>Reduce precision or split DateTime columns only when the report does not need full detail.</li></ol></div>
    <div class="task-card"><h3>Optimize a measure with variables</h3><ol><li>Copy the original measure to a notes area before changing it.</li><li>Create variables with <code>VAR</code> for repeated expressions.</li><li>Return the final result with <code>RETURN</code>.</li><li>Compare old and new results in the same visual.</li></ol></div>
    <div class="task-card"><h3>Prepare refresh optimization</h3><ol><li>Filter rows early when the source supports it.</li><li>Remove unused columns early.</li><li>Preserve query folding where available.</li><li>Confirm <code>RangeStart</code>, <code>RangeEnd</code>, and the partition date/time column before defining incremental refresh.</li></ol></div>
  </div>
</section>
'@ }
    "06" { return @'
<section>
  <h2>Novice-friendly how-to guide</h2>
  <div class="task-list">
    <div class="task-card"><h3>Create a what-if parameter</h3><ol><li>Select <strong>Modeling &gt; New parameter &gt; Numeric range</strong>.</li><li>Name the parameter <code>Margin Adjustment %</code>.</li><li>Set minimum, maximum, and increment values from the lab.</li><li>Keep the generated slicer.</li><li>Use the generated parameter measure inside an adjusted-margin DAX measure.</li></ol></div>
    <div class="task-card"><h3>Use an advanced visual only when available</h3><ol><li>Confirm the visual is available in the target tenant.</li><li>Add the visual to a duplicate or practice page.</li><li>Add the measure to analyze and the dimensions to explain it.</li><li>Document what the visual suggests and what it does not prove.</li></ol></div>
    <div class="task-card"><h3>Create a Gov-safe fallback</h3><ol><li>Use a matrix, bar chart, Top N filter, rolling average, or threshold measure.</li><li>Document how the fallback answers the same business question.</li><li>Mark AI or external runtime features as optional unless validated.</li></ol></div>
  </div>
</section>
'@ }
    "07" { return @'
<section>
  <h2>Novice-friendly how-to guide</h2>
  <div class="task-list">
    <div class="task-card"><h3>Create a static RLS role</h3><ol><li>Select <strong>Modeling &gt; Manage roles</strong>.</li><li>Select <strong>New</strong> and name the role <code>East Region</code>.</li><li>Select the territory table.</li><li>Add a filter such as <code>[TerritoryRegion] = "East"</code>.</li><li>Save the role and test it with <strong>View as</strong>.</li></ol></div>
    <div class="task-card"><h3>Create a dynamic RLS role</h3><ol><li>Load the security mapping table.</li><li>Create the relationship from the security table to the secured dimension.</li><li>Open <strong>Manage roles</strong> and create <code>Dynamic Territory Security</code>.</li><li>Filter the security table with <code>[UserPrincipalName] = USERPRINCIPALNAME()</code>.</li><li>Use <strong>View as</strong> with sample UPNs to confirm access.</li></ol></div>
    <div class="task-card"><h3>Assign Service roles safely</h3><ol><li>Publish only to an approved training workspace.</li><li>Assign users or groups to RLS roles.</li><li>Check workspace role implications before testing.</li><li>Use App distribution for consumers when available instead of broad workspace access.</li></ol></div>
    <div class="task-card"><h3>Test roles</h3><ol><li>Select <strong>Modeling &gt; View as</strong>.</li><li>Choose the role to test.</li><li>For dynamic RLS, enter a sample user principal name.</li><li>Record what data is visible and compare it to the expected mapping table.</li></ol></div>
  </div>
</section>
'@ }
    "08" { return @'
<section>
  <h2>Novice-friendly how-to guide</h2>
  <div class="task-list">
    <div class="task-card"><h3>Plan workspace design and roles</h3><ol><li>Identify whether the workspace is development, test, production, or training-only.</li><li>Use a naming convention that includes domain or subject area where appropriate.</li><li>Record content owner and support owner.</li><li>Assign the least-privileged workspace role: Admin, Member, Contributor, or Viewer.</li><li>Prefer App distribution for consumers instead of adding viewers directly to production workspaces.</li></ol></div>
    <div class="task-card"><h3>Publish a report</h3><ol><li>Open the PBIP-authored report in Power BI Desktop.</li><li>Sign in with the approved training account.</li><li>Select <strong>Home &gt; Publish</strong>.</li><li>Choose the target workspace.</li><li>Open the report in the Power BI Service and confirm the report and semantic model are present.</li></ol></div>
    <div class="task-card"><h3>Review refresh settings</h3><ol><li>Open the workspace in the Power BI Service.</li><li>Find the semantic model and open <strong>Settings</strong>.</li><li>Review credentials, privacy levels, gateway or cloud connection, schedule, and refresh history.</li><li>Document anything that cannot be configured in the training tenant.</li></ol></div>
    <div class="task-card"><h3>Package content as an App</h3><ol><li>Select workspace content for the App.</li><li>Configure name, description, navigation, and consumers.</li><li>Publish or update the App.</li><li>Validate the consumer experience where available.</li></ol></div>
  </div>
</section>
'@ }
    "09" { return @'
<section>
  <h2>Novice-friendly how-to guide</h2>
  <div class="task-list">
    <div class="task-card"><h3>Review usage metrics</h3><ol><li>Open the report or App in the Power BI Service.</li><li>Open usage metrics when tenant policy and permissions allow it.</li><li>Review views, unique viewers, page usage, and trends.</li><li>Document adoption observations, training needs, support signals, and retirement candidates.</li><li>If usage metrics are unavailable, record the tenant, license, or permission blocker.</li></ol></div>
    <div class="task-card"><h3>Review refresh history</h3><ol><li>Open the workspace and select the semantic model.</li><li>Open refresh history or semantic model settings.</li><li>Record recent success/failure status, duration, and recipients.</li><li>For failures, capture the error summary, credential/gateway clue, likely cause, and next action.</li></ol></div>
    <div class="task-card"><h3>Complete runbook evidence</h3><ol><li>Record content inventory, owners, sources, access model, monitoring cadence, and incident paths.</li><li>Mark activity logs, audit logs, admin monitoring, capacity metrics, Purview, and DLP as Verify for Gov unless validated.</li></ol></div>
  </div>
</section>
'@ }
    "10" { return @'
<section>
  <h2>Novice-friendly how-to guide</h2>
  <div class="task-list">
    <div class="task-card"><h3>Compare capacity options</h3><ol><li>Start with user count, model size, refresh frequency, latency, sharing, governance, and integration needs.</li><li>Compare Pro, PPU, Premium capacity, and Fabric capacity against those requirements.</li><li>Mark features that require tenant, license, capacity, or cloud validation.</li><li>Choose a Gov-safe fallback when a feature is not validated.</li><li>Record the recommendation and reason.</li></ol></div>
    <div class="task-card"><h3>Review capacity metrics conceptually</h3><ol><li>Identify the capacity or workspace that would be monitored.</li><li>Review refresh duration, query duration, throttling, memory, interactive workload, background workload, and user activity.</li><li>If the capacity metrics app is unavailable, document what evidence the admin team should provide.</li></ol></div>
  </div>
</section>
'@ }
    "11" { return @'
<section>
  <h2>Novice-friendly how-to guide</h2>
  <div class="task-list">
    <div class="task-card"><h3>Review PBIP source structure</h3><ol><li>Open the PBIP project folder in File Explorer or VS Code.</li><li>Locate the <code>.pbip</code> file.</li><li>Locate the <code>.Report</code> and <code>.SemanticModel</code> folders.</li><li>Open JSON or TMDL files as text to understand what is source-controlled.</li><li>Do not edit generated files unless the lab explicitly tells you to.</li></ol></div>
    <div class="task-card"><h3>Practice a basic git workflow</h3><ol><li>Open a terminal at the repo root.</li><li>Run <code>git status</code>.</li><li>Create or switch to the working branch chosen for the lab.</li><li>Make a small documented change.</li><li>Run <code>git diff</code> to review it.</li><li>Commit only the intended files.</li></ol></div>
    <div class="task-card"><h3>Validate automation boundaries</h3><ol><li>Identify endpoint, identity, network, tenant setting, and permission requirements.</li><li>Mark REST APIs, PowerShell, service principals, XMLA, Fabric Git, and CI/CD as Verify for Gov unless approved.</li></ol></div>
  </div>
</section>
'@ }
    "12" { return @'
<section>
  <h2>Novice-friendly how-to guide</h2>
  <div class="task-list">
    <div class="task-card"><h3>Work through the capstone safely</h3><ol><li>Start from the capstone starter PBIP or completed solution from the previous lab.</li><li>Complete one capability at a time: model, DAX, report UX, security, deployment, governance, and monitoring.</li><li>Save after each major milestone.</li><li>Validate each capability with the rubric before moving to the next one.</li><li>Record evidence as you go instead of waiting until the end.</li></ol></div>
    <div class="task-card"><h3>Package capstone evidence</h3><ol><li>Include the PBIP source project.</li><li>Include screenshots or notes for relationships, report pages, RLS tests, refresh/deployment settings, and governance decisions.</li><li>Complete the validation rubric.</li><li>Mark optional unvalidated features as Verify for Gov or conceptual-only.</li></ol></div>
  </div>
</section>
'@ }
    default { return @'
<section>
  <h2>Novice-friendly how-to guide</h2>
  <div class="task-list">
    <div class="task-card"><h3>Work through each lab step</h3><ol><li>Start from the stated starter PBIP or completed prior module solution.</li><li>Create or modify one object at a time using the exact names in the lab.</li><li>Save after each major change.</li><li>Validate the result in a simple visual, Service page, checklist, or evidence table before moving on.</li></ol></div>
    <div class="task-card"><h3>Document validation</h3><ol><li>Record the feature or setting being tested.</li><li>Record expected behavior before testing.</li><li>Capture actual behavior after testing.</li><li>Mark tenant-dependent features as Verify for Gov if they cannot be validated hands-on.</li></ol></div>
  </div>
</section>
'@ }
  }
}

function RenderImplementationReference($moduleNumber) {
  switch ($moduleNumber) {
    "01" { return @'
<section><h2>Implementation reference table</h2><div class="task-card"><h3>Fact and dimension column reference</h3>
<table class="column-table"><thead><tr><th>Query</th><th>Columns to keep</th><th>Validation</th></tr></thead><tbody>
<tr><td><code>FactSales</code></td><td><code>SalesOrderLineKey</code>, <code>OrderDate</code>, <code>ShipDate</code>, <code>InvoiceDate</code>, <code>CustomerKey</code>, <code>ProductKey</code>, <code>TerritoryKey</code>, <code>Quantity</code>, <code>UnitPrice</code>, <code>UnitCost</code>, <code>SalesAmount</code>, <code>GrossMargin</code></td><td>Transaction grain remains one row per sales order line.</td></tr>
<tr><td><code>DimCustomer</code></td><td><code>CustomerKey</code>, <code>CustomerName</code>, <code>CustomerType</code>, <code>CustomerState</code>, <code>CustomerRegion</code></td><td>Duplicate customer rows removed.</td></tr>
<tr><td><code>DimProduct</code></td><td><code>ProductKey</code>, <code>ProductName</code>, <code>ProductCategory</code>, <code>ProductSubcategory</code></td><td>Product rows stay at product grain.</td></tr>
<tr><td><code>DimProductCategory</code></td><td><code>ProductCategory</code></td><td>One row per category for slicers and targets.</td></tr>
<tr><td><code>DimTerritory</code></td><td><code>TerritoryKey</code>, <code>TerritoryName</code>, <code>TerritoryRegion</code></td><td>Duplicate territory rows removed.</td></tr>
<tr><td><code>BridgeCustomerSegment</code></td><td><code>CustomerKey</code>, <code>Segment</code></td><td>Multi-segment customer mapping.</td></tr>
<tr><td><code>DimSegment</code></td><td><code>Segment</code></td><td>Distinct segment list.</td></tr>
</tbody></table><h3>Relationship reference</h3>
<table class="column-table"><thead><tr><th>From</th><th>To</th><th>Cardinality</th><th>Direction</th><th>Notes</th></tr></thead><tbody>
<tr><td><code>DimCustomer[CustomerKey]</code></td><td><code>FactSales[CustomerKey]</code></td><td>One-to-many</td><td>Single</td><td>Customer filters sales.</td></tr>
<tr><td><code>DimProduct[ProductKey]</code></td><td><code>FactSales[ProductKey]</code></td><td>One-to-many</td><td>Single</td><td>Product filters sales.</td></tr>
<tr><td><code>DimTerritory[TerritoryKey]</code></td><td><code>FactSales[TerritoryKey]</code></td><td>One-to-many</td><td>Single</td><td>Territory filters sales.</td></tr>
<tr><td><code>DimOrderDate[Date]</code></td><td><code>FactSales[OrderDate]</code></td><td>One-to-many</td><td>Single</td><td>Primary date path.</td></tr>
<tr><td><code>DimShipDate[Date]</code></td><td><code>FactSales[ShipDate]</code></td><td>One-to-many</td><td>Single</td><td>Ship-date role path.</td></tr>
<tr><td><code>DimTerritory[TerritoryKey]</code></td><td><code>FactTargets[TerritoryKey]</code></td><td>One-to-many</td><td>Single</td><td>Targets by territory.</td></tr>
<tr><td><code>DimProductCategory[ProductCategory]</code></td><td><code>DimProduct[ProductCategory]</code></td><td>One-to-many</td><td>Single</td><td>Category filters products.</td></tr>
<tr><td><code>DimProductCategory[ProductCategory]</code></td><td><code>FactTargets[ProductCategory]</code></td><td>One-to-many</td><td>Single</td><td>Avoids many-to-many target relationship.</td></tr>
<tr><td><code>DimSegment[Segment]</code></td><td><code>BridgeCustomerSegment[Segment]</code></td><td>One-to-many</td><td>Single</td><td>Segments filter the bridge.</td></tr>
<tr><td><code>DimCustomer[CustomerKey]</code></td><td><code>BridgeCustomerSegment[CustomerKey]</code></td><td>One-to-many</td><td>Single</td><td>Customer filters bridge rows.</td></tr>
</tbody></table></div></section>
'@ }
    "02" { return @'
<section><h2>Implementation reference table</h2><div class="task-card">
<table class="column-table"><thead><tr><th>Item to create</th><th>Exact name</th><th>Pattern or fields</th><th>Validation</th></tr></thead><tbody>
<tr><td>Base measure</td><td><code>Sales Amount</code></td><td><code>SUM(FactSales[SalesAmount])</code></td><td>Totals by customer/product.</td></tr>
<tr><td>Base measure</td><td><code>Quantity</code></td><td><code>SUM(FactSales[Quantity])</code></td><td>Totals by product.</td></tr>
<tr><td>Base measure</td><td><code>Gross Margin</code></td><td><code>SUM(FactSales[GrossMargin])</code></td><td>Totals by territory.</td></tr>
<tr><td>Derived measure</td><td><code>Gross Margin %</code></td><td><code>DIVIDE([Gross Margin], [Sales Amount])</code></td><td>Formatted as percentage.</td></tr>
<tr><td>Target measure</td><td><code>Target Sales Amount</code></td><td><code>SUM(FactTargets[TargetSalesAmount])</code></td><td>Totals by month/category.</td></tr>
<tr><td>Variance measures</td><td><code>Sales Variance</code>, <code>Sales Variance %</code></td><td>Actual minus target; percent uses <code>DIVIDE</code></td><td>No divide-by-zero errors.</td></tr>
<tr><td>Time measures</td><td><code>Sales YTD</code>, <code>Sales Prior Year</code>, <code>Sales YoY</code></td><td>Use <code>DimOrderDate[Date]</code></td><td>Validate by month.</td></tr>
<tr><td>Ranking measure</td><td><code>Customer Sales Rank</code></td><td><code>RANKX</code> over <code>DimCustomer[CustomerName]</code></td><td>Rank respects slicers.</td></tr>
</tbody></table></div></section>
'@ }
    "03" { return @'
<section><h2>Implementation reference table</h2><div class="task-card">
<h3>Module parameter reference</h3>
<table class="column-table"><thead><tr><th>Parameter</th><th>Type</th><th>Suggested value</th><th>Used in core Web path?</th><th>Purpose</th></tr></thead><tbody>
<tr><td><code>RawDataBaseUrl</code></td><td>Text</td><td><code>https://raw.githubusercontent.com/Coding-Forge/PBI-Advanced-Factory/main/data/</code></td><td>Yes</td><td>Base path for raw GitHub CSV files.</td></tr>
<tr><td><code>SourceFolderPath</code></td><td>Text</td><td>Blank, or a local folder path for offline delivery</td><td>No</td><td>Optional folder connector placeholder for instructor/offline scenarios.</td></tr>
<tr><td><code>EnvironmentName</code></td><td>Text or List</td><td><code>Dev</code></td><td>Yes, as documentation/concept</td><td>Introduces Dev/Test/Prod source switching without changing the required Web-source path.</td></tr>
<tr><td><code>RangeStart</code></td><td>Date/Time</td><td><code>2026-01-01 00:00:00</code></td><td>Yes, for incremental refresh prep</td><td>Lower bound for incremental refresh filtering.</td></tr>
<tr><td><code>RangeEnd</code></td><td>Date/Time</td><td><code>2026-04-01 00:00:00</code></td><td>Yes, for incremental refresh prep</td><td>Upper bound for incremental refresh filtering.</td></tr>
</tbody></table>
<table class="column-table"><thead><tr><th>Query</th><th>Source</th><th>Load enabled?</th><th>Required output</th></tr></thead><tbody>
<tr><td><code>raw_Orders_2026_01</code></td><td><code>orders-2026-01.csv</code> Web URL</td><td>No</td><td>All source columns plus <code>SourceFile</code>.</td></tr>
<tr><td><code>raw_Orders_2026_02</code></td><td><code>orders-2026-02.csv</code> Web URL</td><td>No</td><td>All source columns plus <code>SourceFile</code>.</td></tr>
<tr><td><code>raw_Orders_2026_03</code></td><td><code>orders-2026-03.csv</code> Web URL</td><td>No</td><td>All source columns plus <code>SourceFile</code>; contains intentional errors.</td></tr>
<tr><td><code>stg_OrdersCombined</code></td><td>Append raw order queries</td><td>No</td><td>Combined rows with consistent columns.</td></tr>
<tr><td><code>FactOrders</code></td><td>Reference staging query</td><td>Yes</td><td>Typed, valid order rows: <code>OrderId</code>, <code>OrderDate</code>, <code>CustomerName</code>, <code>ProductCode</code>, <code>Quantity</code>, <code>UnitPrice</code>, <code>SalesChannel</code>, <code>SourceFile</code>.</td></tr>
<tr><td><code>err_OrdersReview</code></td><td>Reference staging query</td><td>No</td><td>Rows with a populated <code>DataQualityIssue</code> reason for review.</td></tr>
<tr><td><code>dim_ProductCategory</code></td><td><code>product-category-map.csv</code> Web URL</td><td>Yes</td><td><code>ProductCode</code>, <code>ProductName</code>, <code>ProductCategory</code>, <code>ProductSubcategory</code>.</td></tr>
<tr><td><code>fn_CleanText</code></td><td>Blank query function</td><td>No</td><td>Null-safe trim/clean/proper text function.</td></tr>
</tbody></table></div></section>
'@ }
    "04" { return @'
<section><h2>Implementation reference table</h2><div class="task-card"><table class="column-table"><thead><tr><th>Page or feature</th><th>Exact name</th><th>Required fields/measures</th><th>Validation</th></tr></thead><tbody>
<tr><td>Page</td><td><code>Executive Summary</code></td><td><code>Sales Amount</code>, <code>Gross Margin %</code>, <code>Sales Variance</code>, <code>Quantity</code></td><td>Executive KPIs and exceptions are visible.</td></tr>
<tr><td>Page</td><td><code>Analyst Exploration</code></td><td>Date, territory, product, customer, and segment slicers</td><td>Slicers are clear and affect intended visuals.</td></tr>
<tr><td>Operational/detail page</td><td>Operational or detail page</td><td>Monitoring visuals, exception list, or detail table</td><td>Page answers a specific action question.</td></tr>
<tr><td>Drillthrough page</td><td><code>Customer Detail</code></td><td><code>DimCustomer[CustomerName]</code>, KPI cards, transaction table</td><td>Right-click opens filtered detail and Back returns.</td></tr>
<tr><td>Tooltip page</td><td><code>Sales Tooltip</code></td><td>Compact sales/margin KPIs and trend</td><td>Hover displays contextual information.</td></tr>
<tr><td>Bookmarks</td><td>Show/hide or reset state</td><td>Buttons plus Data, Display, Current page settings</td><td>Only intended visuals or filters change.</td></tr>
<tr><td>Field parameter</td><td><code>Metric Parameter</code></td><td><code>[Sales Amount]</code>, <code>[Gross Margin]</code>, <code>[Gross Margin %]</code>, <code>[Quantity]</code></td><td>Slicer switches the visual metric.</td></tr>
<tr><td>Optional field parameter</td><td><code>Dimension Parameter</code></td><td><code>DimProductCategory[ProductCategory]</code>, <code>DimTerritory[TerritoryRegion]</code>, <code>DimSegment[Segment]</code></td><td>Slicer switches axis or rows.</td></tr>
<tr><td>Conditional formatting</td><td>Margin or variance thresholds</td><td>Status, color, or icon rules with written meaning</td><td>Color is not the only cue.</td></tr>
<tr><td>Mobile layout</td><td>Mobile canvas</td><td>Highest-value KPIs and visuals</td><td>Readable in mobile preview.</td></tr>
<tr><td>Accessibility review</td><td>Alt text, tab order, contrast, titles</td><td>Selection pane and visual formatting settings</td><td>Keyboard and screen-reader path documented.</td></tr>
</tbody></table></div></section>
'@ }
    "05" { return @'
<section><h2>Implementation reference table</h2><div class="task-card">
<table class="column-table"><thead><tr><th>Evidence item</th><th>Where to capture</th><th>What to record</th><th>Outcome</th></tr></thead><tbody>
<tr><td>Baseline timings</td><td>Performance Analyzer</td><td>Visual name, DAX time, display time, other time</td><td>One optimization candidate selected.</td></tr>
<tr><td>Before/after benchmark</td><td>Performance notes</td><td>Baseline, single change, after result, tradeoff, remaining risk</td><td>Improvement claims are evidence-based.</td></tr>
<tr><td>Visual inventory</td><td>Report page</td><td>Visual count, high-cardinality visuals, custom visuals, cross-highlighting</td><td>Low-value overhead identified.</td></tr>
<tr><td>Model review</td><td>Model/Data view</td><td>Unused columns, high-cardinality fields, date/time fields, precision</td><td>Reduction plan documented.</td></tr>
<tr><td>DAX review</td><td>Measure editor</td><td>Before/after measure logic</td><td>Variables or branching added.</td></tr>
<tr><td>Refresh review</td><td>Power Query/Service notes</td><td>Staging, early filters, removed columns, folding status, RangeStart, RangeEnd</td><td>Incremental refresh readiness documented.</td></tr>
<tr><td>Aggregation design</td><td>Model notes</td><td>Summary grain, group-by columns, Import/DirectQuery/hybrid tradeoffs</td><td>Aggregation hit requirements documented.</td></tr>
<tr><td>Capacity/external tools</td><td>Validation notes</td><td>DAX Studio, VertiPaq Analyzer, capacity metrics, admin monitoring status</td><td>Verify for Gov items are labeled.</td></tr>
</tbody></table></div></section>
'@ }
    "06" { return @'
<section><h2>Implementation reference table</h2><div class="task-card">
<table class="column-table"><thead><tr><th>Feature</th><th>Status</th><th>What to create or review</th><th>Fallback</th></tr></thead><tbody>
<tr><td>What-if parameter</td><td>Gov-ready</td><td><code>Margin Adjustment %</code> and adjusted margin measure</td><td>Required core path.</td></tr>
<tr><td>Decomposition tree</td><td>Verify for Gov</td><td>Driver analysis by territory/product/customer/segment</td><td>Matrix plus drillthrough.</td></tr>
<tr><td>Forecasting</td><td>Verify for Gov</td><td>Line chart Analytics pane forecast</td><td>Rolling average and prior-period comparison.</td></tr>
<tr><td>Anomaly detection</td><td>Verify for Gov</td><td>Unusual trend identification on supported visuals</td><td>DAX threshold flags.</td></tr>
<tr><td>Key influencers</td><td>Verify for Gov</td><td>AI visual for outcome analysis</td><td>Top N and ranked comparisons.</td></tr>
<tr><td>Python/R</td><td>Verify for Gov</td><td>Approved runtime/packages only</td><td>Native visuals.</td></tr>
<tr><td>Azure ML</td><td>Verify for Gov</td><td>Validated workspace/identity/network/region</td><td>Static scored output.</td></tr>
<tr><td>Copilot</td><td>Commercial-focused / Verify for Gov</td><td>Conceptual unless tenant, capacity, licensing, and data boundaries are validated</td><td>Human-authored explanation.</td></tr>
<tr><td>Decision framework</td><td>Required documentation</td><td>Available, approved, residency acceptable, fallback identified</td><td>Use non-AI path when any answer is no.</td></tr>
</tbody></table></div></section>
'@ }
    "07" { return @'
<section><h2>Implementation reference table</h2><div class="task-card">
<table class="column-table"><thead><tr><th>Security item</th><th>Exact name</th><th>Configuration</th><th>Validation</th></tr></thead><tbody>
<tr><td>Mapping table</td><td><code>SecurityUserTerritory</code></td><td><code>UserPrincipalName</code>, <code>DisplayName</code>, <code>TerritoryKey</code>, <code>TerritoryName</code>, <code>AccessLevel</code></td><td>Rows loaded from Web URL.</td></tr>
<tr><td>Role matrix</td><td><code>SecurityRoleMatrix</code></td><td>Persona/access documentation table</td><td>Used as documentation, not filtering.</td></tr>
<tr><td>Relationship</td><td>Security to territory</td><td><code>SecurityUserTerritory[TerritoryKey]</code> to <code>DimTerritory[TerritoryKey]</code></td><td>Territory filters sales.</td></tr>
<tr><td>Static role</td><td><code>East Region</code></td><td>Filter <code>DimTerritory</code> to East region or keys</td><td>Only East data visible.</td></tr>
<tr><td>Dynamic role</td><td><code>Dynamic Territory Security</code></td><td><code>[UserPrincipalName] = USERPRINCIPALNAME()</code></td><td>Mapped UPN sees expected territories.</td></tr>
<tr><td>Service role assignment</td><td>RLS role membership</td><td>Assign approved users or groups after publishing</td><td>Test as role where available.</td></tr>
<tr><td>Build permission</td><td>Semantic model reuse</td><td>Grant only to approved thin-report or Analyze in Excel users</td><td>Downstream access risk documented.</td></tr>
<tr><td>Sharing and B2B</td><td>External access path</td><td>Direct sharing, Apps, workspace access, guest users</td><td>Verify for Gov and tenant policy documented.</td></tr>
<tr><td>OLS/labels/Purview</td><td>Optional controls</td><td>Tooling, capacity, MIP/Purview, DLP, export behavior</td><td>Verify for Gov unless validated.</td></tr>
</tbody></table></div></section>
'@ }
    "08" { return @'
<section><h2>Implementation reference table</h2><div class="task-card">
<table class="column-table"><thead><tr><th>Service item</th><th>Configuration</th><th>Permission</th><th>Evidence</th></tr></thead><tbody>
<tr><td>Workspace design</td><td>Dev/test/prod or training intent, domain/subject area, naming convention, owner, support owner</td><td>Workspace Admin to configure</td><td>Workspace plan documented.</td></tr>
<tr><td>Workspace roles</td><td>Admin, Member, Contributor, Viewer assigned by least privilege</td><td>Admin</td><td>Role and rationale recorded.</td></tr>
<tr><td>Report</td><td>PBIP-authored report published</td><td>Contributor or higher</td><td>Report appears in workspace.</td></tr>
<tr><td>Semantic model</td><td>Credentials, privacy levels, refresh, ownership reviewed</td><td>Owner or workspace role</td><td>Settings notes.</td></tr>
<tr><td>Gateway/cloud connection</td><td>Cluster, source mapping, credential owner, network path, or cloud connection documented if needed</td><td>Gateway admin/data source user</td><td>Gateway or cloud notes.</td></tr>
<tr><td>Shared semantic model</td><td>Build permission and thin-report pattern reviewed</td><td>Semantic model owner or workspace role</td><td>Reuse implications documented.</td></tr>
<tr><td>App</td><td>Name, description, navigation, consumers configured</td><td>Member or Admin</td><td>App published or demoed.</td></tr>
<tr><td>App audiences</td><td>Audience-specific content where available</td><td>Member or Admin</td><td>Verify for Gov status.</td></tr>
<tr><td>Deployment pipeline</td><td>Dev/test/prod stages and deployment rules reviewed if available</td><td>Pipeline/workspace access</td><td>Verify for Gov status or manual path.</td></tr>
<tr><td>Endorsement</td><td>Promoted/certified ownership, refresh, security, quality, support evidence</td><td>Tenant governance policy</td><td>Checklist completed.</td></tr>
</tbody></table></div></section>
'@ }
    "09" { return @'
<section><h2>Implementation reference table</h2><div class="task-card">
<table class="column-table"><thead><tr><th>Runbook area</th><th>Fields to complete</th><th>Source</th></tr></thead><tbody>
<tr><td>Content inventory</td><td>Workspace, App, report, semantic model, PBIP path</td><td>Service and repository.</td></tr>
<tr><td>Ownership</td><td>Business owner, technical owner, support contact</td><td>Project governance.</td></tr>
<tr><td>Adoption tracking</td><td>Usage pattern, training need, support signal, retirement candidate, follow-up owner</td><td>Usage metrics, App metrics, support queue, stakeholder feedback.</td></tr>
<tr><td>Data sources</td><td>Source type, gateway required, credential owner</td><td>Semantic model settings.</td></tr>
<tr><td>Refresh</td><td>Schedule, duration, recipients, retry path</td><td>Refresh settings/history.</td></tr>
<tr><td>Access</td><td>Workspace roles, App consumers, Build, RLS/OLS</td><td>Workspace/App/model settings.</td></tr>
<tr><td>Monitoring cadence</td><td>Usage, refresh, gateway, capacity, compliance, owner review rhythm</td><td>Operations model.</td></tr>
<tr><td>Incident response</td><td>Access, refresh, data quality, performance paths</td><td>Support model.</td></tr>
</tbody></table></div></section>
'@ }
    "10" { return @'
<section><h2>Implementation reference table</h2><div class="task-card">
<table class="column-table"><thead><tr><th>Requirement or feature</th><th>Option</th><th>Gov status</th><th>Fallback or evidence</th></tr></thead><tbody>
<tr><td>Standard sharing</td><td>Power BI Pro</td><td>Validate tenant/license</td><td>Instructor demo if no license.</td></tr>
<tr><td>Premium-like user features</td><td>Premium Per User</td><td>Verify for Gov</td><td>Pro-compatible path.</td></tr>
<tr><td>Enterprise scale</td><td>Premium capacity</td><td>Verify for Gov</td><td>Import model plus documented scale plan.</td></tr>
<tr><td>Fabric workloads</td><td>Fabric capacity</td><td>Commercial-focused / Verify for Gov</td><td>Approved source plus Import model.</td></tr>
<tr><td>ALM and external tools</td><td>XMLA endpoint</td><td>Verify for Gov</td><td>Conceptual ALM path if tooling or tenant support is blocked.</td></tr>
<tr><td>Pixel-perfect exports</td><td>Paginated reports</td><td>Verify for Gov</td><td>Standard report export or instructor demo.</td></tr>
<tr><td>Large semantic model</td><td>Large model storage format/capacity settings</td><td>Verify for Gov</td><td>Model reduction, aggregations, incremental refresh where validated.</td></tr>
<tr><td>Lake-native model</td><td>Direct Lake</td><td>Commercial-focused / Verify for Gov</td><td>Import with refresh/aggregations.</td></tr>
<tr><td>Data storage pattern</td><td>OneLake, Lakehouse, Warehouse</td><td>Commercial-focused / Verify for Gov</td><td>Approved source systems plus Import model.</td></tr>
<tr><td>Notebook integration</td><td>Semantic Link</td><td>Commercial-focused / Verify for Gov</td><td>Document model metadata manually.</td></tr>
<tr><td>Capacity elasticity</td><td>Autoscale</td><td>Commercial-focused / Verify for Gov</td><td>Capacity sizing review and operational escalation.</td></tr>
<tr><td>Capacity health</td><td>Capacity metrics app</td><td>Verify for Gov</td><td>Usage, refresh, Performance Analyzer, and admin-provided telemetry.</td></tr>
</tbody></table></div></section>
'@ }
    "11" { return @'
<section><h2>Implementation reference table</h2><div class="task-card">
<table class="column-table"><thead><tr><th>Artifact</th><th>Action</th><th>Gov status</th><th>Evidence</th></tr></thead><tbody>
<tr><td>Lifecycle goals</td><td>Document repeatability, reviewability, promotion, governance, and rollback</td><td>Gov-ready</td><td>Checklist notes and rollback path.</td></tr>
<tr><td>PBIP source</td><td>Keep report/model source in git</td><td>Gov-ready</td><td>Repo path and changed files.</td></tr>
<tr><td>PBIX output</td><td>Generate only when needed</td><td>Gov-ready</td><td>Output artifact note.</td></tr>
<tr><td>Branch and pull request</td><td>Review model, report, DAX, RLS, sources, and generated changes</td><td>Gov-ready</td><td>Review notes, release tag, or rollback note.</td></tr>
<tr><td>External tools</td><td>Use Tabular Editor/ALM Toolkit only if approved</td><td>Verify for Gov</td><td>Policy/XMLA validation.</td></tr>
<tr><td>Automation</td><td>REST API, PowerShell, service principal, CI/CD</td><td>Verify for Gov</td><td>Endpoint, identity, permission, runner, and network notes.</td></tr>
<tr><td>Fabric Git</td><td>Use only if workspace Git is available</td><td>Commercial-focused / Verify for Gov</td><td>Workspace Git branching, folder, sync, conflict, and item-support validation.</td></tr>
<tr><td>Azure Government boundary</td><td>Validate cloud endpoint, authority, network path, tenant settings, and customer policy</td><td>Verify for Gov</td><td>Environment validation notes.</td></tr>
</tbody></table></div></section>
'@ }
    "12" { return @'
<section><h2>Implementation reference table</h2><div class="task-card">
<table class="column-table"><thead><tr><th>Area</th><th>Required artifact</th><th>Validation evidence</th></tr></thead><tbody>
<tr><td>Source control</td><td>PBIP project</td><td>Repository path and source review notes.</td></tr>
<tr><td>Semantic model</td><td>Fact/dimension model</td><td>Relationship diagram or model-grain notes.</td></tr>
<tr><td>DAX</td><td>Base, time, variance, ranking/Top N, dynamic logic</td><td>Measure list and validation visuals.</td></tr>
<tr><td>Report UX</td><td>Executive, analyst, detail, tooltip, bookmark/button, conditional formatting, mobile pages</td><td>Screenshots or review notes plus accessibility checks.</td></tr>
<tr><td>Security</td><td>Static and dynamic RLS</td><td>Desktop and Service role test results where available.</td></tr>
<tr><td>Service distribution</td><td>Published report/model, refresh settings, gateway notes, App plan</td><td>Workspace/App/refresh evidence or documented gap.</td></tr>
<tr><td>Governance and operations</td><td>Endorsement checklist, operations runbook, monitoring/support notes</td><td>Completed documents and support ownership.</td></tr>
<tr><td>Enhanced extensions</td><td>Fabric/Git/Copilot/AI/API/automation feature notes</td><td>Availability status, validation evidence, and fallback path.</td></tr>
<tr><td>Gov readiness</td><td>Feature status notes</td><td>Gov-ready, Verify for Gov, Commercial-focused labels.</td></tr>
<tr><td>Submission</td><td>Validation rubric and evidence package</td><td>Completed rubric plus screenshots/notes.</td></tr>
</tbody></table></div></section>
'@ }
    default { return "" }
  }
}

function RenderAnswerKey($moduleNumber) {
  switch ($moduleNumber) {
    "02" { return @'
<section>
  <h2>Answer key</h2>
  <details class="answer-key">
    <summary>Show DAX formulas</summary>
    <div class="answer-key__body">
      <p>Try to create the measures first. Open this section if you get stuck or want to compare your answer.</p>
<pre class="code"><code>Sales Amount =
SUM ( FactSales[SalesAmount] )

Quantity =
SUM ( FactSales[Quantity] )

Gross Margin =
SUM ( FactSales[GrossMargin] )

Gross Margin % =
DIVIDE ( [Gross Margin], [Sales Amount] )

Target Sales Amount =
SUM ( FactTargets[TargetSalesAmount] )

Sales Variance =
[Sales Amount] - [Target Sales Amount]

Sales Variance % =
DIVIDE ( [Sales Variance], [Target Sales Amount] )

Sales All Products =
CALCULATE (
    [Sales Amount],
    REMOVEFILTERS ( DimProduct )
)

Product Sales Share =
DIVIDE ( [Sales Amount], [Sales All Products] )

Enterprise Customer Sales =
CALCULATE (
    [Sales Amount],
    KEEPFILTERS ( DimCustomer[CustomerType] = "Enterprise" )
)

Sales YTD =
TOTALYTD (
    [Sales Amount],
    DimOrderDate[Date]
)

Sales Prior Year =
CALCULATE (
    [Sales Amount],
    SAMEPERIODLASTYEAR ( DimOrderDate[Date] )
)

Sales YoY =
[Sales Amount] - [Sales Prior Year]

Sales YoY % =
DIVIDE ( [Sales YoY], [Sales Prior Year] )

Sales Rolling 90 Days =
VAR LastVisibleDate =
    MAX ( DimOrderDate[Date] )
RETURN
    CALCULATE (
        [Sales Amount],
        DATESINPERIOD ( DimOrderDate[Date], LastVisibleDate, -90, DAY )
    )

Customer Sales Rank =
RANKX (
    ALLSELECTED ( DimCustomer[CustomerName] ),
    [Sales Amount],
    ,
    DESC,
    DENSE
)

Is Top 5 Customer =
IF ( [Customer Sales Rank] &lt;= 5, 1, 0 )

Sales by Customer Region Grain =
CALCULATE (
    [Sales Amount],
    ALLEXCEPT ( DimCustomer, DimCustomer[CustomerRegion] )
)

Segment Sales via TREATAS =
CALCULATE (
    [Sales Amount],
    TREATAS ( VALUES ( DimSegment[Segment] ), BridgeCustomerSegment[Segment] )
)

Ending Balance Example =
VAR LastVisibleDate =
    MAX ( DimOrderDate[Date] )
RETURN
    CALCULATE (
        [Sales Amount],
        LASTNONBLANK ( DimOrderDate[Date], [Sales Amount] ),
        DimOrderDate[Date] &lt;= LastVisibleDate
    )

Selected Metric =
VAR MetricName =
    SELECTEDVALUE ( MetricSelector[Metric], "Sales Amount" )
RETURN
    SWITCH (
        MetricName,
        "Sales Amount", [Sales Amount],
        "Gross Margin", [Gross Margin],
        "Gross Margin %", [Gross Margin %],
        "Quantity", [Quantity],
        [Sales Amount]
    )

Sales Title =
VAR SelectedRegion =
    SELECTEDVALUE ( DimTerritory[TerritoryRegion], "All Regions" )
RETURN
    "Sales Performance - " &amp; SelectedRegion</code></pre>
      <h3>Calculation group answer key</h3>
      <p>Use these formulas for the <code>Time Calculation</code> calculation items. Each item uses <code>SELECTEDMEASURE()</code> so the same logic can apply to multiple explicit base measures.</p>
<pre class="code"><code>// Current
SELECTEDMEASURE()

// MTD
CALCULATE (
    SELECTEDMEASURE(),
    DATESMTD ( DimOrderDate[Date] )
)

// QTD
CALCULATE (
    SELECTEDMEASURE(),
    DATESQTD ( DimOrderDate[Date] )
)

// YTD
CALCULATE (
    SELECTEDMEASURE(),
    DATESYTD ( DimOrderDate[Date] )
)

// Fiscal YTD
CALCULATE (
    SELECTEDMEASURE(),
    DATESYTD ( DimOrderDate[Date], "6/30" )
)

// Prior Year
CALCULATE (
    SELECTEDMEASURE(),
    SAMEPERIODLASTYEAR ( DimOrderDate[Date] )
)

// YoY Change
VAR PriorYearValue =
    CALCULATE (
        SELECTEDMEASURE(),
        SAMEPERIODLASTYEAR ( DimOrderDate[Date] )
    )
RETURN
    SELECTEDMEASURE() - PriorYearValue

// YoY Change %
VAR PriorYearValue =
    CALCULATE (
        SELECTEDMEASURE(),
        SAMEPERIODLASTYEAR ( DimOrderDate[Date] )
    )
RETURN
    DIVIDE ( SELECTEDMEASURE() - PriorYearValue, PriorYearValue )

// Rolling 90 Days
VAR LastVisibleDate =
    MAX ( DimOrderDate[Date] )
RETURN
    CALCULATE (
        SELECTEDMEASURE(),
        DATESINPERIOD ( DimOrderDate[Date], LastVisibleDate, -90, DAY )
    )</code></pre>
    </div>
  </details>
</section>
'@ }
    "03" { return @'
<section>
  <h2>Answer key</h2>
  <details class="answer-key">
    <summary>Show Power Query M patterns</summary>
    <div class="answer-key__body">
      <p>These snippets show the intended M patterns. Your generated step names may differ depending on how you clicked through Power Query.</p>
<pre class="code"><code>// Parameter value
RawDataBaseUrl = "https://raw.githubusercontent.com/Coding-Forge/PBI-Advanced-Factory/main/data/"

// Optional offline/folder delivery placeholder
SourceFolderPath = ""

// Environment documentation/concept parameter
EnvironmentName = "Dev"

// Incremental refresh preparation parameters
RangeStart = #datetime(2026, 1, 1, 0, 0, 0)
RangeEnd = #datetime(2026, 4, 1, 0, 0, 0)

// Example Web source pattern
Source =
    Csv.Document(
        Web.Contents(RawDataBaseUrl &amp; "monthly-orders/orders-2026-01.csv"),
        [Delimiter = ",", Encoding = 65001, QuoteStyle = QuoteStyle.Csv]
    )

PromotedHeaders =
    Table.PromoteHeaders(Source, [PromoteAllScalars = true])

WithSourceFile =
    Table.AddColumn(
        PromotedHeaders,
        "SourceFile",
        each "orders-2026-01.csv",
        type text
    )

// Append pattern
stg_OrdersCombined =
    Table.Combine({
        raw_Orders_2026_01,
        raw_Orders_2026_02,
        raw_Orders_2026_03
    })

// Text cleanup function
(inputText as nullable text) as nullable text =&gt;
let
    Result =
        if inputText = null then
            null
        else
            Text.Proper(Text.Trim(Text.Clean(inputText)))
in
    Result

// Error review query pattern
err_OrdersReview =
    let
        Source = stg_OrdersCombined,
        AddedDataQualityIssue =
            Table.AddColumn(
                Source,
                "DataQualityIssue",
                each
                    let
                        ParsedOrderDate = try Date.From([OrderDate]) otherwise null,
                        ParsedQuantity = try Number.From([Quantity]) otherwise null,
                        ParsedUnitPrice = try Number.From([UnitPrice]) otherwise null,
                        ProductCodeText = try Text.Trim(Text.From([ProductCode])) otherwise "",
                        Issues =
                            List.RemoveNulls(
                                {
                                    if ParsedOrderDate = null then "Missing or invalid OrderDate" else null,
                                    if ParsedQuantity = null or ParsedQuantity &lt;= 0 then "Missing or non-positive Quantity" else null,
                                    if ParsedUnitPrice = null or ParsedUnitPrice &lt;= 0 then "Missing or non-positive UnitPrice" else null,
                                    if ProductCodeText = "" then "Missing ProductCode" else null
                                }
                            )
                    in
                        Text.Combine(Issues, "; "),
                type text
            ),
        ErrorRows =
            Table.SelectRows(
                AddedDataQualityIssue,
                each [DataQualityIssue] &lt;&gt; ""
            )
    in
        ErrorRows

// FactOrders valid-row filter pattern
ValidatedOrders =
    Table.AddColumn(
        stg_OrdersCombined,
        "DataQualityIssue",
        each
            let
                ParsedOrderDate = try Date.From([OrderDate]) otherwise null,
                ParsedQuantity = try Number.From([Quantity]) otherwise null,
                ParsedUnitPrice = try Number.From([UnitPrice]) otherwise null,
                ProductCodeText = try Text.Trim(Text.From([ProductCode])) otherwise "",
                Issues =
                    List.RemoveNulls(
                        {
                            if ParsedOrderDate = null then "Missing or invalid OrderDate" else null,
                            if ParsedQuantity = null or ParsedQuantity &lt;= 0 then "Missing or non-positive Quantity" else null,
                            if ParsedUnitPrice = null or ParsedUnitPrice &lt;= 0 then "Missing or non-positive UnitPrice" else null,
                            if ProductCodeText = "" then "Missing ProductCode" else null
                        }
                    )
            in
                Text.Combine(Issues, "; "),
        type text
    )

ValidRows =
    Table.SelectRows(
        ValidatedOrders,
        each [DataQualityIssue] = ""
    )

// Final type pattern
TypedOrders =
    Table.TransformColumnTypes(
        ValidRows,
        {
            {"OrderId", Int64.Type},
            {"OrderDate", type date},
            {"CustomerName", type text},
            {"ProductCode", type text},
            {"Quantity", Int64.Type},
            {"UnitPrice", Currency.Type},
            {"SalesChannel", type text},
            {"SourceFile", type text}
        }
    )

// Invoke fn_CleanText in FactOrders after typing
FactOrders =
    Table.TransformColumns(
        TypedOrders,
        {
            {"CustomerName", each fn_CleanText(_), type nullable text},
            {"SalesChannel", each fn_CleanText(_), type nullable text}
        }
    )

// Invoke fn_CleanText in the product reference query
CleanedProductText =
    Table.TransformColumns(
        dim_ProductCategory,
        {
            {"ProductName", each fn_CleanText(_), type nullable text},
            {"ProductCategory", each fn_CleanText(_), type nullable text},
            {"ProductSubcategory", each fn_CleanText(_), type nullable text}
        }
    )

// Incremental refresh filter pattern
FilteredRows =
    Table.SelectRows(
        FactOrders,
        each [OrderDate] &gt;= Date.From(RangeStart)
            and [OrderDate] &lt; Date.From(RangeEnd)
    )</code></pre>
    </div>
  </details>
</section>
'@ }
    "05" { return @'
<section>
  <h2>Answer key</h2>
  <details class="answer-key">
    <summary>Show sample DAX optimization pattern</summary>
    <div class="answer-key__body">
      <p>Use this as a pattern for simplifying repeated measure logic. Your exact measure may vary.</p>
<pre class="code"><code>// Less maintainable pattern
Sales Variance % - Repeated =
DIVIDE (
    SUM ( FactSales[SalesAmount] )
        - SUM ( FactTargets[TargetSalesAmount] ),
    SUM ( FactTargets[TargetSalesAmount] )
)

// Preferred measure-branching pattern
Sales Amount =
SUM ( FactSales[SalesAmount] )

Target Sales Amount =
SUM ( FactTargets[TargetSalesAmount] )

Sales Variance =
[Sales Amount] - [Target Sales Amount]

Sales Variance % =
VAR VarianceAmount = [Sales Variance]
VAR TargetAmount = [Target Sales Amount]
RETURN
    DIVIDE ( VarianceAmount, TargetAmount )</code></pre>
    </div>
  </details>
</section>
'@ }
    "06" { return @'
<section>
  <h2>Answer key</h2>
  <details class="answer-key">
    <summary>Show what-if parameter DAX pattern</summary>
    <div class="answer-key__body">
      <p>Power BI may generate slightly different names for the parameter table and selected-value measure. Adjust names to match your model.</p>
<pre class="code"><code>// Generated or equivalent selected value measure
Margin Adjustment % Value =
SELECTEDVALUE ( 'Margin Adjustment %'[Margin Adjustment %], 0 )

Adjusted Gross Margin =
VAR AdjustmentRate =
    DIVIDE ( [Margin Adjustment % Value], 100 )
RETURN
    [Gross Margin] * ( 1 + AdjustmentRate )

Adjusted Gross Margin % =
DIVIDE ( [Adjusted Gross Margin], [Sales Amount] )

Margin Scenario Title =
VAR Adjustment =
    FORMAT ( DIVIDE ( [Margin Adjustment % Value], 100 ), "0%" )
RETURN
    "Margin scenario: " &amp; Adjustment</code></pre>
    </div>
  </details>
</section>
'@ }
    "07" { return @'
<section>
  <h2>Answer key</h2>
  <details class="answer-key">
    <summary>Show RLS filter expressions</summary>
    <div class="answer-key__body">
      <p>Use these expressions in Manage roles. Exact table names must match your model.</p>
<pre class="code"><code>// Static role option on DimTerritory
DimTerritory[TerritoryRegion] = "East"

// Static role option by territory keys
DimTerritory[TerritoryKey] IN { "T01" }

// Dynamic role filter on SecurityUserTerritory
SecurityUserTerritory[UserPrincipalName] = USERPRINCIPALNAME()

// Useful test UPNs
alex.manager@contoso.example     // T01, T02
casey.lead@contoso.example       // T03
devon.director@contoso.example   // T01, T02, T03, T04
jordan.rep@contoso.example       // T04</code></pre>
    </div>
  </details>
</section>
'@ }
    default { return "" }
  }
}

function RenderDetailedProcedure($moduleNumber) {
  switch ($moduleNumber) {
    "01" { return @'
<section>
  <h2>Detailed step-by-step procedure</h2>
  <ol class="steps">
    <li><strong>Create or open the PBIP project.</strong><p>Open Power BI Desktop. If you are continuing the workshop solution, open the PBIP project in <code>pbi-local\</code>. If this is your first hands-on step, create a new blank report and save it as a Power BI project before importing data.</p></li>
    <li><strong>Connect to the sales flat file.</strong><p>Select <b>Home > Get data > Web</b>. Paste the <code>sales-flat.csv</code> raw URL from the Source files section. Use Anonymous authentication for the public GitHub source, then choose <b>Transform data</b>.</p></li>
    <li><strong>Name the raw query.</strong><p>In Power Query, rename the query to <code>raw_SalesFlat</code>. Do not do all modeling work directly in this raw query; keep it as your source reference.</p></li>
    <li><strong>Create the sales fact query.</strong><p>Right-click <code>raw_SalesFlat</code> and choose <b>Reference</b>. Rename the new query <code>FactSales</code>. Use this exact column list so relationship keys and later DAX measures are not missed.</p>
      <table class="column-table">
        <thead><tr><th>Column</th><th>Action</th><th>Why</th></tr></thead>
        <tbody>
          <tr><td><code>SalesOrderLineKey</code></td><td>Keep</td><td>Unique transaction line identifier.</td></tr>
          <tr><td><code>OrderDate</code></td><td>Keep</td><td>Relationship to <code>DimOrderDate</code>.</td></tr>
          <tr><td><code>ShipDate</code></td><td>Keep</td><td>Relationship to <code>DimShipDate</code>.</td></tr>
          <tr><td><code>InvoiceDate</code></td><td>Keep</td><td>Optional invoice-date analysis.</td></tr>
          <tr><td><code>CustomerKey</code></td><td>Keep</td><td>Relationship to <code>DimCustomer</code>.</td></tr>
          <tr><td><code>ProductKey</code></td><td>Keep</td><td>Relationship to <code>DimProduct</code>.</td></tr>
          <tr><td><code>TerritoryKey</code></td><td>Keep</td><td>Relationship to <code>DimTerritory</code>.</td></tr>
          <tr><td><code>Quantity</code></td><td>Keep</td><td>Additive quantity measure source.</td></tr>
          <tr><td><code>UnitPrice</code></td><td>Keep</td><td>Validation and derived price metrics.</td></tr>
          <tr><td><code>UnitCost</code></td><td>Keep</td><td>Validation and derived cost/margin metrics.</td></tr>
          <tr><td><code>SalesAmount</code></td><td>Keep</td><td>Core sales measure source.</td></tr>
          <tr><td><code>GrossMargin</code></td><td>Keep</td><td>Core gross margin measure source.</td></tr>
          <tr><td><code>CustomerName</code>, <code>CustomerType</code>, <code>CustomerState</code>, <code>CustomerRegion</code></td><td>Remove from <code>FactSales</code></td><td>These belong in <code>DimCustomer</code>.</td></tr>
          <tr><td><code>ProductName</code>, <code>ProductCategory</code>, <code>ProductSubcategory</code></td><td>Remove from <code>FactSales</code></td><td>These belong in <code>DimProduct</code>.</td></tr>
          <tr><td><code>TerritoryName</code>, <code>TerritoryRegion</code></td><td>Remove from <code>FactSales</code></td><td>These belong in <code>DimTerritory</code>.</td></tr>
        </tbody>
      </table>
    </li>
    <li><strong>Create customer, product, and territory dimensions.</strong><p>Reference <code>raw_SalesFlat</code> three more times. Use the exact column lists below, then remove duplicate rows from each dimension query.</p>
      <table class="column-table">
        <thead><tr><th>Query</th><th>Columns to keep</th><th>Columns to remove</th></tr></thead>
        <tbody>
          <tr><td><code>DimCustomer</code></td><td><code>CustomerKey</code>, <code>CustomerName</code>, <code>CustomerType</code>, <code>CustomerState</code>, <code>CustomerRegion</code></td><td>All sales, date, product, and territory columns.</td></tr>
          <tr><td><code>DimProduct</code></td><td><code>ProductKey</code>, <code>ProductName</code>, <code>ProductCategory</code>, <code>ProductSubcategory</code></td><td>All sales, date, customer, and territory columns.</td></tr>
          <tr><td><code>DimProductCategory</code></td><td><code>ProductCategory</code></td><td><code>SalesOrderLineKey</code>, <code>OrderDate</code>, <code>ShipDate</code>, <code>InvoiceDate</code>, <code>CustomerKey</code>, <code>CustomerName</code>, <code>CustomerType</code>, <code>CustomerState</code>, <code>CustomerRegion</code>, <code>ProductKey</code>, <code>ProductName</code>, <code>ProductSubcategory</code>, <code>TerritoryKey</code>, <code>TerritoryName</code>, <code>TerritoryRegion</code>, <code>Quantity</code>, <code>UnitPrice</code>, <code>UnitCost</code>, <code>SalesAmount</code>, <code>GrossMargin</code>. Remove duplicate rows so each category appears once.</td></tr>
          <tr><td><code>DimTerritory</code></td><td><code>TerritoryKey</code>, <code>TerritoryName</code>, <code>TerritoryRegion</code></td><td>All sales, date, customer, and product columns.</td></tr>
        </tbody>
      </table>
    </li>
    <li><strong>Create the product category lookup.</strong><p><code>FactTargets</code> is stored at product-category grain, while <code>DimProduct</code> is stored at product grain. Do not relate <code>DimProduct[ProductCategory]</code> directly to <code>FactTargets[ProductCategory]</code> if Power BI detects many-to-many cardinality. Instead, reference <code>DimProduct</code>, rename the query <code>DimProductCategory</code>, remove <code>ProductKey</code>, <code>ProductName</code>, and <code>ProductSubcategory</code>, keep <code>ProductCategory</code> as the only remaining column, remove duplicate rows from <code>ProductCategory</code>, and load it as a small lookup dimension.</p></li>
    <li><strong>Create date role tables.</strong><p>Create date tables for at least Order Date and Ship Date. For a beginner-friendly path, duplicate or reference a completed date table into <code>DimOrderDate</code> and <code>DimShipDate</code>. Use one of the approved patterns below.</p>
      <details>
        <summary>Answer key / suggested date table patterns</summary>
        <p><strong>Use Power Query</strong> when the date table should be reusable across reports, parameterized by start/end date, aligned to a configurable fiscal year, or enriched with holidays before load. Create a blank query named <code>fn_DimDate</code> and paste this function in Advanced Editor.</p>
        <pre class="code"><code>let
    fn_DimDate =
        (
            StartDate as date,
            EndDate as date,
            optional FiscalYearStartMonth as nullable number,
            optional Holidays as nullable table
        ) as table =&gt;
        let
            FiscalStartMonth = if FiscalYearStartMonth = null then 7 else FiscalYearStartMonth,
            _ValidateFiscalMonth =
                if FiscalStartMonth &lt; 1 or FiscalStartMonth &gt; 12 then
                    error "FiscalYearStartMonth must be a number from 1 through 12."
                else
                    FiscalStartMonth,
            DayCount = Duration.Days(EndDate - StartDate) + 1,
            Source =
                if DayCount &lt; 1 then
                    error "EndDate must be on or after StartDate."
                else
                    List.Dates(StartDate, DayCount, #duration(1, 0, 0, 0)),
            Dates = Table.FromList(Source, Splitter.SplitByNothing(), {"Date"}),
            ChangedType = Table.TransformColumnTypes(Dates, {{"Date", type date}}),
            AddYearMonthDay = Table.AddColumn(ChangedType, "YearMonthDay", each Date.Year([Date]) * 10000 + Date.Month([Date]) * 100 + Date.Day([Date]), Int64.Type),
            AddYearMonth = Table.AddColumn(AddYearMonthDay, "YearMonth", each Date.Year([Date]) * 100 + Date.Month([Date]), Int64.Type),
            AddYear = Table.AddColumn(AddYearMonth, "Year", each Date.Year([Date]), Int64.Type),
            AddQuarter = Table.AddColumn(AddYear, "Quarter", each Date.QuarterOfYear([Date]), Int64.Type),
            AddMonth = Table.AddColumn(AddQuarter, "Month", each Date.Month([Date]), Int64.Type),
            AddDay = Table.AddColumn(AddMonth, "Day", each Date.Day([Date]), Int64.Type),
            AddWeek = Table.AddColumn(AddDay, "Week", each let WeekStart = Date.StartOfWeek([Date], Day.Monday) in Date.Year(WeekStart) * 10000 + Date.Month(WeekStart) * 100 + Date.Day(WeekStart), Int64.Type),
            AddWeekNumber = Table.AddColumn(AddWeek, "WeekNumber", each Date.WeekOfYear([Date], Day.Monday), Int64.Type),
            AddYearWeekNumber = Table.AddColumn(AddWeekNumber, "YearWeekNumber", each Date.Year([Date]) * 100 + Date.WeekOfYear([Date], Day.Monday), Int64.Type),
            AddMonthName = Table.AddColumn(AddYearWeekNumber, "MonthName", each Date.ToText([Date], "MMMM", "en-US"), type text),
            AddMonthShortName = Table.AddColumn(AddMonthName, "MonthShortName", each Date.ToText([Date], "MMM", "en-US"), type text),
            AddYearMonthName = Table.AddColumn(AddMonthShortName, "YearMonthName", each Date.ToText([Date], "yyyy-MMM", "en-US"), type text),
            AddQuarterName = Table.AddColumn(AddYearMonthName, "QuarterName", each "Q" &amp; Text.From([Quarter], "en-US"), type text),
            AddYearQuarter = Table.AddColumn(AddQuarterName, "YearQuarter", each Text.From([Year], "en-US") &amp; "-Q" &amp; Text.From([Quarter], "en-US"), type text),
            AddWeekdayName = Table.AddColumn(AddYearQuarter, "WeekdayName", each Date.ToText([Date], "dddd", "en-US"), type text),
            AddWeekdayShortName = Table.AddColumn(AddWeekdayName, "WeekdayShortName", each Date.ToText([Date], "ddd", "en-US"), type text),
            AddDayOfWeekNumber = Table.AddColumn(AddWeekdayShortName, "DayOfWeekNumber", each Date.DayOfWeek([Date], Day.Monday) + 1, Int64.Type),
            AddIsWeekend = Table.AddColumn(AddDayOfWeekNumber, "IsWeekend", each [DayOfWeekNumber] &gt;= 6, type logical),
            AddFiscalYearNumber = Table.AddColumn(AddIsWeekend, "FiscalYearNumber", each if Date.Month([Date]) &gt;= FiscalStartMonth then Date.Year([Date]) + 1 else Date.Year([Date]), Int64.Type),
            AddFiscalYear = Table.AddColumn(AddFiscalYearNumber, "FiscalYear", each "FY" &amp; Text.From([FiscalYearNumber], "en-US"), type text),
            AddFiscalQuarter = Table.AddColumn(AddFiscalYear, "FiscalQuarter", each Number.IntegerDivide(Number.Mod(Date.Month([Date]) - FiscalStartMonth + 12, 12), 3) + 1, Int64.Type),
            AddFiscalPeriod = Table.AddColumn(AddFiscalQuarter, "FiscalPeriod", each [FiscalYear] &amp; "-Q" &amp; Text.From([FiscalQuarter], "en-US"), type text),
            AddFiscalYearQuarterNumber = Table.AddColumn(AddFiscalPeriod, "FiscalYearQuarterNumber", each [FiscalYearNumber] * 10 + [FiscalQuarter], Int64.Type),
            HolidaySource =
                if Holidays = null then
                    #table(type table [Date = date, HolidayName = text], {})
                else
                    Table.TransformColumnTypes(Holidays, {{"Date", type date}, {"HolidayName", type text}}),
            MergeHolidays = Table.NestedJoin(AddFiscalYearQuarterNumber, {"Date"}, HolidaySource, {"Date"}, "Holiday", JoinKind.LeftOuter),
            ExpandHolidays = Table.ExpandTableColumn(MergeHolidays, "Holiday", {"HolidayName"}, {"HolidayName"}),
            AddIsHoliday = Table.AddColumn(ExpandHolidays, "IsHoliday", each [HolidayName] &lt;&gt; null, type logical),
            AddIsBusinessDay = Table.AddColumn(AddIsHoliday, "IsBusinessDay", each not [IsWeekend] and not [IsHoliday], type logical)
        in
            AddIsBusinessDay
in
    fn_DimDate</code></pre>
        <p>Example lab query:</p>
        <pre class="code"><code>let
    Source = fn_DimDate(#date(2023, 1, 1), #date(2029, 12, 31), 7, null)
in
    Source</code></pre>
        <p><strong>Use DAX</strong> when you need a quick model-local date table. This calculated table starts on January 1 three years before the current year and ends on December 31 three years after the current year.</p>
        <pre class="code"><code>DimDate =
VAR CurrentYear = YEAR ( TODAY () )
VAR StartDate = DATE ( CurrentYear - 3, 1, 1 )
VAR EndDate = DATE ( CurrentYear + 3, 12, 31 )
RETURN
    ADDCOLUMNS (
        CALENDAR ( StartDate, EndDate ),
        "YearMonthDay", YEAR ( [Date] ) * 10000 + MONTH ( [Date] ) * 100 + DAY ( [Date] ),
        "YearMonth", YEAR ( [Date] ) * 100 + MONTH ( [Date] ),
        "Year", YEAR ( [Date] ),
        "Quarter", QUARTER ( [Date] ),
        "MonthNumber", MONTH ( [Date] ),
        "Day", DAY ( [Date] ),
        "Week",
            VAR WeekStart = [Date] - WEEKDAY ( [Date], 2 ) + 1
            RETURN YEAR ( WeekStart ) * 10000 + MONTH ( WeekStart ) * 100 + DAY ( WeekStart ),
        "WeekNumber", WEEKNUM ( [Date], 2 ),
        "YearWeekNumber", YEAR ( [Date] ) * 100 + WEEKNUM ( [Date], 2 ),
        "MonthName", FORMAT ( [Date], "MMMM" ),
        "WeekdayName", FORMAT ( [Date], "dddd" )
    )</code></pre>
        <p>After creating either pattern, mark the table as a date table using the <code>Date</code> column. The Power Query function returns numeric attributes for year-month-day, year-month, year, quarter, month, day, week, week number, year-week number, weekday number, and fiscal sort keys; text attributes for month, short month, year-month, quarter, weekday, short weekday, fiscal year, and fiscal period; and holiday/business-day attributes when supplied.</p>
        <div class="callout"><strong>Side note:</strong> Larger enterprise date dimensions often add period boundary dates, refresh-relative offsets, current-period flags, and ISO week attributes. Keep those optional in Lab 1 because they depend on business calendar rules, refresh timing, and whether the organization uses ISO week calendars.</div>
      </details>
    </li>
    <li><strong>Load targets and customer segments.</strong><p>Use <b>Get data > Web</b> for <code>targets.csv</code> and <code>customer-segments.csv</code>. Use these exact column lists.</p>
      <table class="column-table">
        <thead><tr><th>Query</th><th>Columns to keep</th><th>Notes</th></tr></thead>
        <tbody>
          <tr><td><code>FactTargets</code></td><td><code>TargetMonth</code>, <code>TerritoryKey</code>, <code>ProductCategory</code>, <code>TargetSalesAmount</code></td><td>Monthly target fact table.</td></tr>
          <tr><td><code>BridgeCustomerSegment</code></td><td><code>CustomerKey</code>, <code>Segment</code></td><td>Bridge table that maps customers to one or more segments.</td></tr>
          <tr><td><code>DimSegment</code></td><td><code>Segment</code></td><td>Create this as a distinct list from <code>BridgeCustomerSegment[Segment]</code>.</td></tr>
        </tbody>
      </table>
    </li>
    <li><strong>Close and apply.</strong><p>Confirm data types before loading. Dates should be Date, quantities should be whole numbers, currency/amount columns should be decimal or fixed decimal, and keys should be text unless you intentionally model them otherwise.</p></li>
    <li><strong>Create relationships in Model view.</strong><p>Use the relationship setup reference below to create each relationship explicitly. The core lab path uses one-to-many cardinality and single-direction filtering from dimensions into facts or bridge tables.</p>
      <table class="column-table">
        <thead><tr><th>From table</th><th>From column</th><th>Key role</th><th>To table</th><th>To column</th><th>Key role</th><th>Cardinality</th><th>Cross-filter direction</th><th>Active?</th></tr></thead>
        <tbody>
          <tr><td><code>DimCustomer</code></td><td><code>CustomerKey</code></td><td>PK</td><td><code>FactSales</code></td><td><code>CustomerKey</code></td><td>FK</td><td>One-to-many</td><td>Single</td><td>Yes</td></tr>
          <tr><td><code>DimProduct</code></td><td><code>ProductKey</code></td><td>PK</td><td><code>FactSales</code></td><td><code>ProductKey</code></td><td>FK</td><td>One-to-many</td><td>Single</td><td>Yes</td></tr>
          <tr><td><code>DimTerritory</code></td><td><code>TerritoryKey</code></td><td>PK</td><td><code>FactSales</code></td><td><code>TerritoryKey</code></td><td>FK</td><td>One-to-many</td><td>Single</td><td>Yes</td></tr>
          <tr><td><code>DimOrderDate</code></td><td><code>Date</code></td><td>PK</td><td><code>FactSales</code></td><td><code>OrderDate</code></td><td>FK</td><td>One-to-many</td><td>Single</td><td>Yes</td></tr>
          <tr><td><code>DimShipDate</code></td><td><code>Date</code></td><td>PK</td><td><code>FactSales</code></td><td><code>ShipDate</code></td><td>FK</td><td>One-to-many</td><td>Single</td><td>Yes</td></tr>
          <tr><td><code>DimTerritory</code></td><td><code>TerritoryKey</code></td><td>PK</td><td><code>FactTargets</code></td><td><code>TerritoryKey</code></td><td>FK</td><td>One-to-many</td><td>Single</td><td>Yes</td></tr>
          <tr><td><code>DimProductCategory</code></td><td><code>ProductCategory</code></td><td>PK</td><td><code>DimProduct</code></td><td><code>ProductCategory</code></td><td>FK</td><td>One-to-many</td><td>Single</td><td>Yes</td></tr>
          <tr><td><code>DimProductCategory</code></td><td><code>ProductCategory</code></td><td>PK</td><td><code>FactTargets</code></td><td><code>ProductCategory</code></td><td>FK</td><td>One-to-many</td><td>Single</td><td>Yes</td></tr>
          <tr><td><code>DimSegment</code></td><td><code>Segment</code></td><td>PK</td><td><code>BridgeCustomerSegment</code></td><td><code>Segment</code></td><td>FK</td><td>One-to-many</td><td>Single</td><td>Yes</td></tr>
          <tr><td><code>DimCustomer</code></td><td><code>CustomerKey</code></td><td>PK</td><td><code>BridgeCustomerSegment</code></td><td><code>CustomerKey</code></td><td>FK</td><td>One-to-many</td><td>Single</td><td>Yes</td></tr>
        </tbody>
      </table>
      <p><strong>Crow's-foot model view:</strong></p>
      <pre class="code"><code>DimCustomer  ||--o{  FactSales              : CustomerKey
DimProduct   ||--o{  FactSales              : ProductKey
DimTerritory ||--o{  FactSales              : TerritoryKey
DimOrderDate ||--o{  FactSales              : OrderDate
DimShipDate  ||--o{  FactSales              : ShipDate

DimTerritory ||--o{  FactTargets            : TerritoryKey
DimProductCategory ||--o{  DimProduct       : ProductCategory
DimProductCategory ||--o{  FactTargets      : ProductCategory

DimCustomer  ||--o{  BridgeCustomerSegment  : CustomerKey
DimSegment   ||--o{  BridgeCustomerSegment  : Segment</code></pre>
      <div class="callout"><strong>Bridge-table note:</strong> Keep relationships single-direction for the core lab. If a segment slicer must directly filter sales, discuss the ambiguity and performance tradeoffs before using bidirectional filtering, or use an intentional DAX pattern such as <code>TREATAS</code>.</div>
    </li>
    <li><strong>Validate the model.</strong><p>Create a simple table or matrix with CustomerName, ProductCategory, TerritoryRegion, and SalesAmount. Filter by date and segment to confirm the relationships behave as expected.</p></li>
    <li><strong>Review composite model or DirectQuery choices.</strong><p>This optional lab is marked <strong>Verify for Gov</strong>. Identify which tables are good Import candidates, which sources might require DirectQuery, where Dual dimensions could help, and what gateway, tenant, source, and performance tradeoffs must be validated before using the pattern hands-on.</p></li>
  </ol>
</section>
'@ }
    "02" { return @'
<section>
  <h2>Detailed step-by-step procedure</h2>
  <ol class="steps">
    <li><strong>Open the PBIP model from Lab 1.</strong><p>Confirm the model has FactSales, dimensions, date tables, targets, and segment tables. Do not start DAX work until the relationships are correct.</p></li>
    <li><strong>Create a measure table.</strong><p>In Power BI Desktop, create or choose a table to hold measures. Name measures consistently and place them in display folders if your model supports it.</p></li>
    <li><strong>Create base measures first.</strong><p>Create Sales Amount, Quantity, Gross Margin, Gross Margin %, Target Sales Amount, Sales Variance, and Sales Variance %. Use simple aggregations and <code>DIVIDE</code> for percentages.</p></li>
    <li><strong>Test filter context.</strong><p>Add a matrix with CustomerName on rows and ProductCategory on columns. Add Sales Amount and Gross Margin %. Add slicers for TerritoryRegion and Year. Observe how the same measure changes under different filters.</p></li>
    <li><strong>Build CALCULATE examples.</strong><p>Create a measure that removes product filters and a product share measure that divides current sales by all-product sales. Then create a measure that uses <code>KEEPFILTERS</code> for a selected customer type.</p></li>
    <li><strong>Compare filter modifiers.</strong><p>Discuss when to use <code>REMOVEFILTERS</code>, <code>ALL</code>, <code>ALLEXCEPT</code>, and <code>TREATAS</code>. Validate each pattern in a simple visual before reusing it in production report logic.</p></li>
    <li><strong>Create time intelligence.</strong><p>Using the Order Date table, create YTD, prior-year, year-over-year, year-over-year percent, and rolling-period measures. Validate each measure in a month-level visual.</p></li>
    <li><strong>Review semi-additive logic.</strong><p>Discuss why inventory, backlog, headcount, or balance snapshots should not be summed across dates. Create or review an ending-balance-style last-value pattern from the answer key.</p></li>
    <li><strong>Add ranking and Top N.</strong><p>Create a Customer Sales Rank measure with <code>RANKX</code>. Add a flag for Top 5 customers and use it as a visual filter on a bar chart.</p></li>
    <li><strong>Review calculation groups.</strong><p>This optional lab is marked <strong>Verify for Gov</strong>. If the target Power BI Desktop version supports native calculation group authoring, use <b>Model view > Calculation group</b>, enable <b>Discourage implicit measures</b> if prompted, and create a <code>Time Intelligence</code> calculation group with Current, Prior Year, YoY Change, and YoY Change % items. If TMDL View, Tabular Editor, XMLA, or CI/CD workflows are validated, review those authoring paths too. If no authoring path is validated, compare the design to creating separate DAX measures for each metric/time combination.</p></li>
    <li><strong>Add dynamic report text or metric switching.</strong><p>Create a dynamic title with <code>SELECTEDVALUE</code>. Optionally create a disconnected metric selector table and a <code>SWITCH</code> measure to display a selected metric.</p></li>
    <li><strong>Validate measure branching.</strong><p>Confirm derived measures reuse base measures rather than duplicating <code>SUM</code> logic. Check formatting, naming, and fallback behavior before using the measures on report pages.</p></li>
    <li><strong>Refactor for readability.</strong><p>Use variables for repeated logic. Branch from base measures instead of duplicating calculations. Add formatting and descriptions where appropriate.</p></li>
    <li><strong>Validate and document.</strong><p>Check totals at the customer, product, territory, and date levels. If using DAX Studio or other tools, mark them Verify for Gov unless the customer environment has been validated.</p></li>
  </ol>
</section>
'@ }
    "03" { return @'
<section>
  <h2>Detailed step-by-step procedure</h2>
  <ol class="steps">
    <li><strong>Open the PBIP project and Power Query.</strong><p>Open the current PBIP solution. Select <b>Transform data</b> to open Power Query Editor.</p></li>
    <li><strong>Create module parameters.</strong><p>Create five Power Query parameters: <code>RawDataBaseUrl</code> as Text with value <code>https://raw.githubusercontent.com/Coding-Forge/PBI-Advanced-Factory/main/data/</code>; <code>SourceFolderPath</code> as Text and leave it blank unless using an offline folder path; <code>EnvironmentName</code> as Text or List with current value <code>Dev</code>; <code>RangeStart</code> as Date/Time with value <code>2026-01-01 00:00:00</code>; and <code>RangeEnd</code> as Date/Time with value <code>2026-04-01 00:00:00</code>.</p></li>
    <li><strong>Load monthly order files.</strong><p>Use <b>New Source > Web</b> for each monthly order CSV. Name the raw queries <code>raw_Orders_2026_01</code>, <code>raw_Orders_2026_02</code>, and <code>raw_Orders_2026_03</code>.</p></li>
    <li><strong>Review generated M fundamentals.</strong><p>Use the formula bar to identify applied steps and step references. Point out lists, records, and tables in the generated code, such as the option record in <code>Csv.Document</code> and the query list used by <code>Table.Combine</code>.</p></li>
    <li><strong>Add source lineage.</strong><p>In each raw monthly query, add a custom column named SourceFile with the file name, such as <code>orders-2026-01.csv</code>. This helps identify which file produced each row.</p></li>
    <li><strong>Append the monthly queries.</strong><p>Use <b>Append Queries as New</b> and append the three monthly order queries. Rename the result <code>stg_OrdersCombined</code>.</p></li>
    <li><strong>Create the final fact query.</strong><p>Reference <code>stg_OrdersCombined</code> and name the new query <code>FactOrders</code>. Use the validation pattern to keep only rows with no data quality issue, then apply explicit data types for OrderId, OrderDate, ProductCode, Quantity, UnitPrice, and SalesChannel.</p></li>
    <li><strong>Create and invoke a cleanup function.</strong><p>Create <code>fn_CleanText</code> to trim and clean nullable text values. Invoke it on <code>CustomerName</code> and <code>SalesChannel</code> in <code>FactOrders</code>, and on <code>ProductName</code>, <code>ProductCategory</code>, and <code>ProductSubcategory</code> in the product reference query.</p></li>
    <li><strong>Identify bad data.</strong><p>Use column quality/profile and safe parsing logic to find the intentional bad date and bad quantity in the March file. Create <code>err_OrdersReview</code> as a disabled-load reference query before removing invalid rows from <code>FactOrders</code>.</p></li>
    <li><strong>Document business-rule checks.</strong><p>Keep readable reasons for missing or invalid OrderDate, non-positive Quantity, non-positive UnitPrice, and missing ProductCode so reviewers can understand what was excluded.</p></li>
    <li><strong>Load reference data.</strong><p>Use the Web connector for <code>product-category-map.csv</code>. Merge it into <code>FactOrders</code> on ProductCode or keep it as a dimension/reference table, depending on the lab design.</p></li>
    <li><strong>Prepare for incremental refresh.</strong><p>Use the existing Date/Time parameters <code>RangeStart</code> and <code>RangeEnd</code>. Filter the final fact query on OrderDate using those parameters. Document Service-side incremental refresh as Verify for Gov.</p></li>
    <li><strong>Review native queries and source systems.</strong><p>Keep native SQL optional until source security, gateway behavior, credentials, and Azure Government support are validated. Prefer maintainable Power Query steps for the core lab.</p></li>
  </ol>
</section>
'@ }
    "04" { return @'
<section>
  <h2>Detailed step-by-step procedure</h2>
  <ol class="steps">
    <li><strong>Open the report PBIP.</strong><p>Start from the model and measures created in earlier labs. Confirm that Sales Amount, Gross Margin, variance, date, customer, product, territory, and segment fields are available in the Fields pane before you add any visuals.</p></li>
    <li><strong>Create the executive summary page.</strong><p>Right-click a page tab and choose <b>Insert Page</b>, then rename it <code>Executive Summary</code>. Add 4 KPI cards for Sales Amount, Gross Margin %, Sales Variance, and Quantity across the top of the canvas. Below the cards, add a line chart for the sales trend and one high-level breakdown visual, such as a bar chart of sales by territory.</p>
      <div class="figure"><figcaption><strong>Suggested illustration:</strong> annotated screenshot of the finished Executive Summary page with callouts pointing at the KPI card row, trend chart, and territory breakdown so learners can compare their layout to the target.</figcaption></div>
    </li>
    <li><strong>Plan audience-driven report pages.</strong><p>Before building more pages, write down the primary audience and the one decision question each page must answer (for example, "Which territories are behind target this month?"). Keep executive, analyst, and operational/detail pages distinct so interactivity reduces cognitive load instead of adding confusion.</p></li>
    <li><strong>Create the analyst exploration page.</strong><p>Insert a new page named <code>Analyst Exploration</code>. Add slicers for Order Date, Territory Region, Product Category, and Customer Type along the top or left edge. Add a matrix or table plus a chart that allow comparison across customer, product, territory, and segment.</p></li>
    <li><strong>Validate slicers and filters.</strong><p>Click through each slicer one at a time and confirm the visuals you expect actually change. Place slicers in the same position on every page, use page-level filters (via the Filters pane) where a filter should apply to the whole page instead of one visual, and make sure a new learner could look at the page and explain which filters are currently active.</p></li>
    <li><strong>Create a drillthrough page.</strong><p>Insert a page named <code>Customer Detail</code>. Open the Visualizations pane's Filters area, drag <code>DimCustomer[CustomerName]</code> into the <b>Drill through</b> field well, and confirm <b>Keep all filters</b> matches your design intent. Add KPI cards, a transaction table, and a text box/button styled as a Back button (Format > Action > Back). Save, then right-click a customer name on another page and confirm <b>Drill through > Customer Detail</b> appears and filters correctly.</p>
      <div class="figure"><figcaption><strong>Suggested illustration:</strong> screenshot of the right-click context menu showing the Drillthrough option, plus a second screenshot of the resulting filtered Customer Detail page.</figcaption></div>
    </li>
    <li><strong>Create a report page tooltip.</strong><p>Insert a page named <code>Sales Tooltip</code>. In the Page Information section of the Format pane, set <b>Page size</b> to <b>Tooltip</b> (320x240) and turn on <b>Allow use as tooltip</b>. Add compact KPI cards and a small trend visual sized to fit. Return to the main page, select the visual that should show the tooltip, open Format > General > Tooltips, and set the tooltip type to <b>Report page</b>, pointing at <code>Sales Tooltip</code>.</p></li>
    <li><strong>Add bookmarks and buttons.</strong><p>Open <b>View > Bookmarks</b> to show the Bookmarks pane. Set up the visuals or filters in the state you want to capture, then choose <b>Add</b>. Rename the bookmark clearly (for example, <code>Show Detail Panel</code>). Right-click the bookmark and confirm whether <b>Data</b>, <b>Display</b>, and <b>Current Page</b> should be checked based on what the bookmark is meant to change. Add a button or shape, then under Format > Action, set Type to <b>Bookmark</b> and select the bookmark to apply.</p></li>
    <li><strong>Add navigation.</strong><p>Insert a <b>Buttons > Navigator > Page navigator</b> visual, or add individual buttons with Action type set to <b>Page navigation</b>. Copy the same navigator to every report page in the same position, and use plain labels (page display names) that match what learners see in the page tabs.</p></li>
    <li><strong>Add field parameters.</strong><p>Select <b>Modeling &gt; New parameter &gt; Fields</b>. Name the parameter <code>Metric Parameter</code>, then check <code>Sales Amount</code>, <code>Gross Margin</code>, <code>Gross Margin %</code>, and <code>Quantity</code> from the measure list, leaving <b>Add slicer to this page</b> checked. Drag the generated <code>Metric Parameter</code> field onto the Values well of a chart in place of a single measure, then use the auto-added slicer to switch which metric drives the chart. Optionally repeat the process to create a <code>Dimension Parameter</code> for Product Category, Territory, and Segment.</p>
      <div class="figure"><figcaption><strong>Suggested illustration:</strong> side-by-side screenshots of the same chart before and after switching the field-parameter slicer, showing the axis/label change.</figcaption></div>
    </li>
    <li><strong>Apply conditional formatting.</strong><p>Pick one business threshold, such as negative Sales Variance or Gross Margin % below a target. Select the visual, open the Values field's dropdown, choose <b>Conditional formatting &gt; Background color</b> (or Font color/Icons), configure the rule using your chosen measure and threshold, and add a short label or legend so viewers understand what the color means without relying on color alone.</p></li>
    <li><strong>Build the margin target challenge.</strong><p>If time allows, create the disconnected <code>Margin Target</code> table (a small list of target percentages) via Enter Data, then create DAX measures for the selected target, variance to target, status text, and a status color hex measure. Wire the status color measure into the conditional formatting rule above so the color and the text status stay in sync.</p></li>
    <li><strong>Create mobile layout.</strong><p>Select <b>View &gt; Mobile layout</b>. Drag only the highest-value visuals from the desktop canvas onto the mobile canvas in priority order (KPIs first, detail visuals last), and resize/reflow them so touch targets are large enough to tap comfortably. Avoid placing dense tables on the mobile layout unless the audience specifically needs them on a phone.</p></li>
    <li><strong>Run accessibility review.</strong><p>Select each visual and, in the Format pane's General section, add descriptive alt text under Alt text. Open the Selection pane (View > Selection) and drag items into a logical tab order. Use a contrast checker on your color palette, confirm every visual has a clear title, and verify that no visual relies on color as the only way to communicate meaning (add icons or text labels alongside color).</p></li>
  </ol>
</section>
'@ }
    "05" { return @'
<section>
  <h2>Detailed step-by-step procedure</h2>
  <ol class="steps">
    <li><strong>Open the current report PBIP.</strong><p>Use the report built in the previous labs. Choose one report page that has several visuals and slicers — the Executive Summary or Analyst Exploration page from Lab 4 works well because it has multiple visuals reacting to the same slicers.</p></li>
    <li><strong>Capture a baseline.</strong><p>Select <b>View &gt; Performance Analyzer</b> to open the pane, then select <b>Start recording</b>. Select <b>Refresh visuals</b> to force every visual on the page to re-query, then interact with one or two slicers. Expand each visual's entry in the pane and note the DAX query, visual display, and "Other" timings in milliseconds. Sort mentally (or export to JSON) to identify which visuals have the highest total time.</p>
      <div class="figure"><figcaption><strong>Suggested illustration:</strong> screenshot of the Performance Analyzer pane with the highest-cost visual expanded, annotated to show where DAX query time vs. visual display time appears.</figcaption></div>
    </li>
    <li><strong>Review visual complexity.</strong><p>Count the visuals on the page. For each one, ask whether it duplicates information shown elsewhere, uses a high-cardinality field (like a raw transaction key) on an axis, relies on a custom/imported visual, or isn't needed to answer the page's decision question. List any candidates for removal or consolidation.</p></li>
    <li><strong>Review model fields.</strong><p>Open Model view and inspect the fact and dimension tables for unused columns (right-click a table > look for columns not used in any visual or measure), high-cardinality text columns, numeric columns with excessive decimal precision, and date/time columns that could be simplified to Date-only.</p></li>
    <li><strong>Optimize one DAX measure.</strong><p>Pick a measure that repeats the same sub-expression more than once or uses a broad filter-removal function like <code>ALL</code> unnecessarily. Rewrite it using a <code>VAR</code> to compute the shared sub-expression once, and branch from an existing base measure instead of re-deriving <code>SUM</code>/<code>DIVIDE</code> logic. Add the rewritten measure next to the original on a test visual and compare the numbers to confirm they match before replacing the original.</p></li>
    <li><strong>Optimize visuals.</strong><p>Remove or merge at least one low-value visual identified in step 3. If two visuals cross-filter each other in a way that doesn't help the user's task, select the visual, open <b>Format &gt; Edit interactions</b> (Format ribbon), and set the unwanted interaction to <b>None</b>.</p></li>
    <li><strong>Review aggregation design.</strong><p>On paper or in a notes section, define a possible aggregation table grain, such as Month + Product Category + Territory with summed Sales Amount and Gross Margin. Document whether the detail-level table (FactSales) would stay Import, move to DirectQuery, or be split into an Import aggregation plus a DirectQuery/large detail table in a hybrid pattern.</p></li>
    <li><strong>Review Power Query and incremental refresh.</strong><p>Open Power Query and confirm each query filters early, removes unused columns, and shows "folding" indicators where the source supports it. Identify the fact table's date/time column and check whether <code>RangeStart</code>/<code>RangeEnd</code> parameters exist for incremental refresh. Note whether Service-side incremental refresh has actually been validated in this tenant, or whether it remains conceptual.</p></li>
    <li><strong>Optional external diagnostics.</strong><p>If DAX Studio or VertiPaq Analyzer is an approved tool in your environment, connect to the local model, run a quick query to compare timings, and check table/column sizes. If these tools are not approved, keep this step conceptual and mark it Verify for Gov in your notes.</p></li>
    <li><strong>Review Service and capacity monitoring.</strong><p>Where a workspace is available, open the semantic model's refresh history and settings page, and check whether capacity metrics or the admin monitoring workspace are accessible. Mark capacity metrics Verify for Gov unless you have validated access in this tenant.</p></li>
    <li><strong>Document results.</strong><p>In a short notes section (or the lab worksheet), record the Performance Analyzer baseline numbers, the specific change you made, the after numbers from a second recording, the tradeoff involved (for example, less visual detail vs. faster load), and any remaining risk. Do not claim an improvement without a before/after Performance Analyzer comparison to back it up.</p></li>
  </ol>
</section>
'@ }
    "06" { return @'
<section>
  <h2>Detailed step-by-step procedure</h2>
  <ol class="steps">
    <li><strong>Start with the Gov-ready core.</strong><p>Open the report PBIP and choose a page where margin or sales scenario analysis makes sense — the Sales & Margin Analysis page from earlier labs is a good candidate.</p></li>
    <li><strong>Create a what-if parameter.</strong><p>Select <b>Modeling &gt; New parameter &gt; Numeric range</b>. Name it <code>Margin Adjustment %</code>, set Data type to Decimal number, Minimum to -10, Maximum to 20, Increment to 1, and Default to 0. Leave <b>Add slicer to this page</b> checked so Power BI creates the slicer and the <code>[Margin Adjustment % Value]</code> measure automatically.</p></li>
    <li><strong>Create adjusted measures.</strong><p>Create a measure named <code>Adjusted Gross Margin %</code> that adds <code>[Margin Adjustment % Value] / 100</code> to <code>[Gross Margin %]</code>, then a second measure <code>Adjusted Gross Margin</code> that multiplies the adjusted percentage by <code>[Sales Amount]</code>.</p></li>
    <li><strong>Add scenario visuals.</strong><p>Add the auto-generated parameter slicer, a card for the base <code>[Gross Margin]</code>, a card for <code>[Adjusted Gross Margin]</code>, and a clustered column or line chart comparing the two side by side. Drag the slicer and confirm both cards and the chart move together as you change the adjustment percentage.</p>
      <div class="figure"><figcaption><strong>Suggested illustration:</strong> before/after screenshot pair showing the adjustment slider at 0% vs. +10%, with the two margin cards visibly different.</figcaption></div>
    </li>
    <li><strong>Evaluate decomposition tree.</strong><p>If the Decomposition tree visual is available in your tenant, add it, set Sales Amount or Gross Margin as the analyzed metric, and add Territory, Product Category, Customer Type, and Segment as explain-by fields; try both manual expansion and the AI-driven High Value/Low Value split. If the visual is unavailable or marked Verify for Gov, build the Gov-safe alternate instead: a matrix with the same explain-by fields nested on rows plus the drillthrough page from Lab 4 for order-level detail.</p></li>
    <li><strong>Evaluate forecasting/anomaly options.</strong><p>If available, add a line chart of Sales Amount by date, open the Analytics pane, and add a Forecast line (set forecast length and confidence interval) or Anomaly detection. If unavailable, build the Gov-safe fallback: a rolling-average measure, a prior-period comparison measure, and a DAX-based threshold flag (for example, "Below 90% of prior period").</p></li>
    <li><strong>Evaluate key influencers.</strong><p>If available, add the Key influencers visual, set a clear outcome field (such as a binary "Below Target" flag) and 3-5 explanatory fields, and review the ranked influencer list together as a class, discussing correlation vs. causation. If unavailable, build ranking and Top N visuals instead using the <code>RANKX</code> pattern from Lab 2.</p></li>
    <li><strong>Review Python/R and Azure ML.</strong><p>Do not enable Python/R visuals or Azure ML integration unless the required runtimes, packages, Service support, network egress, identity, and data residency requirements have been validated for this tenant. Use the native visuals covered above, or a static, pre-scored sample output described conceptually, as the fallback.</p></li>
    <li><strong>Review Copilot conceptually.</strong><p>If Copilot for Power BI has not been validated in this tenant, present the conceptual walkthrough only (what it can summarize, what a DAX query prompt looks like) without live demonstration. Emphasize that any AI-generated summary or measure requires human review before being trusted or shared.</p></li>
    <li><strong>Document feature status.</strong><p>For every advanced or AI-assisted feature covered in this lab (decomposition tree, forecasting, anomaly detection, key influencers, Python/R, Azure ML, Copilot), write down whether it is Gov-ready, Verify for Gov, or Commercial-focused in this tenant, and record the fallback pattern actually used in the lab.</p></li>
  </ol>
</section>
'@ }
    "07" { return @'
<section>
  <h2>Detailed step-by-step procedure</h2>
  <ol class="steps">
    <li><strong>Open the PBIP model.</strong><p>Confirm <code>DimTerritory</code> and <code>FactSales</code> exist and that filtering DimTerritory (for example, by clicking a slicer value) already changes the sales visuals on a test page.</p></li>
    <li><strong>Load security mapping files.</strong><p>Select <b>Home &gt; Get data &gt; Web</b> and paste the raw URLs for <code>security-user-territory.csv</code> and <code>security-role-matrix.csv</code>. Rename the first query's table <code>SecurityUserTerritory</code> and keep the second, <code>SecurityRoleMatrix</code>, as reference documentation (not necessarily loaded into the model).</p></li>
    <li><strong>Create relationships.</strong><p>In Model view, drag from <code>SecurityUserTerritory[TerritoryKey]</code> to <code>DimTerritory[TerritoryKey]</code> to create the relationship. Confirm the cardinality shows many-to-one from SecurityUserTerritory to DimTerritory. Test by adding a table with UserPrincipalName and TerritoryName and confirming the mapping looks correct.</p></li>
    <li><strong>Create static RLS.</strong><p>Open <b>Modeling &gt; Manage roles</b>, select <b>Create</b>, and name the role <code>East Region</code>. Select the <code>DimTerritory</code> table and enter a DAX filter such as <code>DimTerritory[TerritoryRegion] = "East"</code> (or filter by specific TerritoryKey values), then select <b>Save</b>.</p></li>
    <li><strong>Create dynamic RLS.</strong><p>In Manage roles, select <b>Create</b> again and name the role <code>Dynamic Territory Security</code>. Select the <code>SecurityUserTerritory</code> table and enter the filter <code>[UserPrincipalName] = USERPRINCIPALNAME()</code>, then Save.</p></li>
    <li><strong>Test in Desktop.</strong><p>Select <b>Modeling &gt; View as</b>, check the static role first and confirm only the expected territory's data appears report-wide. Then check the dynamic role, enter a synthetic UPN copied from the <code>SecurityUserTerritory</code> mapping file (for example, one of the sample UPNs in the answer key), select OK, and verify only that user's mapped territories are visible.</p>
      <div class="figure"><figcaption><strong>Suggested illustration:</strong> screenshot of the "View as roles" dialog with the dynamic role and a test UPN entered, next to the resulting filtered report page.</figcaption></div>
    </li>
    <li><strong>Document expected access.</strong><p>Use <code>security-role-matrix.csv</code> as a reference to record, for each persona/role, which territories they should see and whether they should also have Build permission on the semantic model.</p></li>
    <li><strong>Assign and test roles in Service where available.</strong><p>Publish to a training workspace, open the semantic model's Security settings, add the appropriate users or security groups to each role, and use <b>Test as role</b> in the Service to confirm behavior matches Desktop. If Service access is unavailable in this environment, write down this step as a documented validation gap rather than skipping it silently.</p></li>
    <li><strong>Review Build permission.</strong><p>In the semantic model's manage permissions/access list, review who currently has Build permission, and explain in your notes what Build permission allows (creating thin reports or using Analyze in Excel against this model) and the risk of granting it too broadly (for example, to an entire large security group).</p></li>
    <li><strong>Review sharing and external users.</strong><p>Compare direct report sharing, Power BI Apps, workspace access, and Microsoft Entra B2B guest access as distribution options, and note which of these your organization actually allows. Keep external sharing and B2B guest access marked Verify for Gov unless tenant policy has explicitly validated them.</p></li>
    <li><strong>Review optional controls.</strong><p>Discuss Object-Level Security (OLS), sensitivity labels, Microsoft Purview integration, external sharing, and B2B guest access as further layers of control, keeping each one marked Verify for Gov until validated against the specific customer tenant's policies.</p></li>
  </ol>
</section>
'@ }
    "08" { return @'
<section>
  <h2>Detailed step-by-step procedure</h2>
  <ol class="steps">
    <li><strong>Plan workspace design.</strong><p>Decide whether this workspace represents development, test, production, or a training-only environment. Write down a naming convention (for example, <code>PBI-Adv-Training-Dev</code>), the domain/subject area it belongs to, the workspace owner, and who the support owner will be if issues arise.</p></li>
    <li><strong>Confirm workspace roles.</strong><p>Open workspace access settings and identify your own role, then decide the least-privileged role for each other person who needs access: Admin, Member, Contributor, or Viewer. Confirm you personally have at least Contributor to publish and Admin/Member to configure refresh or create Apps.</p></li>
    <li><strong>Publish the PBIP-authored report.</strong><p>In Power BI Desktop, select <b>Home &gt; Publish</b>, choose the target training workspace, and wait for the publish to complete. Open the workspace in the browser and confirm both the report and its semantic model appear in the content list.</p></li>
    <li><strong>Review semantic model settings.</strong><p>Open the semantic model's <b>Settings</b> page in the Service. Review the data source credentials section, the privacy level setting, the refresh history tab (even if empty so far), and the ownership field at the top.</p></li>
    <li><strong>Configure scheduled refresh where supported.</strong><p>On the same Settings page, expand <b>Data source credentials</b> and set/edit credentials for each Web source, then expand <b>Scheduled refresh</b>, turn it on, and pick a frequency and time zone. If the data source uses raw GitHub URLs, run a manual refresh first to validate anonymous Web access works from the Service before relying on the schedule.</p></li>
    <li><strong>Document gateway or cloud connection requirements.</strong><p>If any source were on-premises or network-restricted (not the case for this training's public GitHub CSVs, but document the pattern), you would need to identify the gateway cluster, the data source mapping within that gateway, the stored credentials, and the gateway owner. Since this lab's sources are public web files, write down explicitly why no gateway is required here.</p></li>
    <li><strong>Create a thin report scenario.</strong><p>In workspace access settings, confirm or grant <b>Build</b> permission to the intended analyst audience on the semantic model. Then, from Power BI Service or Desktop, choose <b>Get data &gt; Power BI semantic models</b>, connect to the published model, and create a new thin report against it to demonstrate the shared-model pattern.</p></li>
    <li><strong>Package as an App.</strong><p>In the workspace, select <b>Create app</b>. On the Setup tab, add a name, description, and logo/theme color. On the Navigation tab, arrange which reports/pages appear and in what order. On the Audience tab, add the intended consumers or security group. Select <b>Publish app</b> and then open the app link to validate the consumer experience.</p></li>
    <li><strong>Review App audiences.</strong><p>If your license/tenant supports multiple audiences, add a second audience on the Audience tab and tailor which content that audience can see. If this hasn't been validated in your tenant, keep it optional and mark it Verify for Gov in your notes.</p></li>
    <li><strong>Review deployment pipelines.</strong><p>If Deployment pipelines are available, open <b>Workspace &gt; Deployment pipelines</b>, map Development/Test/Production workspaces, and review any deployment rules (such as different data source parameters per stage). If unavailable, document the manual promotion path you would use instead (for example, republish PBIP to each workspace in order with reviewed changes).</p></li>
    <li><strong>Complete endorsement checklist.</strong><p>Before marking the semantic model Promoted or Certified, gather evidence for ownership, refresh reliability, security (RLS/roles configured and tested), data quality, and support process, then record that evidence in your workspace or lab notes.</p></li>
  </ol>
</section>
'@ }
    "09" { return @'
<section>
  <h2>Detailed step-by-step procedure</h2>
  <ol class="steps">
    <li><strong>Start from a published report.</strong><p>Use the report and semantic model published in Lab 8. If you do not have workspace access in this environment, follow along with an instructor demo or screenshots instead of skipping the concepts.</p></li>
    <li><strong>Open usage metrics.</strong><p>Open the published report, select the ellipsis (...) menu, and choose <b>Usage metrics report</b> (or <b>View usage metrics</b>). Review total views, unique viewers, views over time, and (if available) App usage. Write down one adoption observation (for example, "views dropped after week 2") and one follow-up action you would take.</p></li>
    <li><strong>Interpret adoption signals.</strong><p>Compare pages/reports with consistently high views (candidates for more investment), very low views (possible training gap or retirement candidate), and declining trends (possible support or relevance issue), and note what each pattern suggests you should do next.</p></li>
    <li><strong>Review refresh history.</strong><p>Open the semantic model's <b>Settings &gt; Refresh history</b> tab. Record the most recent refresh's status (success/failure), its duration, and — if it failed — the error detail shown.</p></li>
    <li><strong>Check credentials and source settings.</strong><p>On the same Settings page, review the data source credentials and privacy level settings, and check whether a gateway is listed as required. Do not change any production credentials or schedules unless you have explicit approval to do so.</p></li>
    <li><strong>Review tenant settings.</strong><p>If you have admin access, open the <b>Admin portal &gt; Tenant settings</b> and review the settings for external sharing, export, publish to web, certification, external guest (B2B) access, and Build permission defaults. If you do not have admin access, use instructor-provided screenshots or a conceptual walkthrough instead.</p></li>
    <li><strong>Inspect gateway health where available.</strong><p>If a gateway is in use, open <b>Admin portal &gt; Manage gateways</b>, review the gateway cluster's status (online/offline), the data source mappings configured on it, who owns the stored credentials, the gateway version, and the escalation path if it goes offline.</p></li>
    <li><strong>Review optional admin signals.</strong><p>Note whether Activity logs, Audit logs, the Admin monitoring workspace, Capacity metrics, Microsoft Purview, and DLP policies are accessible to you. Each requires specific admin permissions and tenant validation — record what you could see and what remained blocked.</p></li>
    <li><strong>Complete the operations runbook.</strong><p>Fill in a short runbook covering: content inventory (which reports/models), owners, data sources, refresh schedule, access model (who can view/edit), monitoring cadence (how often usage/refresh is checked), incident response steps, and Azure Government validation notes for anything not yet confirmed in this tenant.</p></li>
    <li><strong>Define support process.</strong><p>Write down who is responsible for handling refresh failures, access requests, data quality issues, performance complaints, enhancement requests, and adoption follow-up — even if the answer for this training environment is "the instructor" or "TBD."</p></li>
    <li><strong>Document gaps.</strong><p>For every item in this lab you could not access directly (admin portal, gateway management, capacity metrics), write down the specific validation gap and who (role, not necessarily a name) would need to confirm it in a real deployment.</p></li>
  </ol>
</section>
'@ }
    "10" { return @'
<section>
  <h2>Detailed step-by-step procedure</h2>
  <ol class="steps">
    <li><strong>Compare licensing and capacity options.</strong><p>On a worksheet or notes page, write down the number of users, approximate model size, refresh frequency needed, latency/freshness needs, governance requirements, data residency needs, and any Fabric-item integration requirements. Use that list to compare Pro, Premium Per User (PPU), Premium capacity, and Fabric capacity side by side, noting which requirement each option satisfies or fails.</p></li>
    <li><strong>Review XMLA endpoint.</strong><p>If an approved external tool (such as Tabular Editor or SSMS) and XMLA read/write access are available, connect to the workspace's XMLA endpoint and browse the semantic model's metadata. If unavailable, document the use cases instead: ALM/version comparison, external-tool authoring, read/write automation workflows, and the security/admin settings that must be enabled first.</p></li>
    <li><strong>Review paginated report fit.</strong><p>Ask whether this solution needs pixel-perfect export, invoices, statements, or highly formatted operational reports. If so, identify whether your license, workspace, and Report Builder access have been validated for paginated reports before attempting hands-on work.</p></li>
    <li><strong>Review large semantic model needs.</strong><p>Decide whether the model's size, memory footprint, refresh duration, storage format (Large model storage format setting), or XMLA read/write workflows would require capacity-dependent settings in production. Mark any of these Verify for Gov until validated on the target capacity.</p></li>
    <li><strong>Review Direct Lake.</strong><p>Compare Import, DirectQuery, and Direct Lake modes across data freshness, modeling flexibility, fallback-to-DirectQuery behavior, and Azure Government validation status, and record which mode fits this training scenario's needs best.</p></li>
    <li><strong>Review OneLake, Lakehouse, and Warehouse.</strong><p>Discuss conceptually how data could be stored in OneLake, exposed through a Lakehouse or Warehouse, governed with workspace/item permissions, and consumed by Power BI via Direct Lake or a semantic model. Treat these as Commercial-focused / Verify for Gov unless your tenant has explicitly confirmed availability.</p></li>
    <li><strong>Review Semantic Link.</strong><p>Discuss how a Fabric notebook could use Semantic Link to read semantic model metadata and data for data-science workflows, and record the security, availability, and fallback notes relevant to this environment.</p></li>
    <li><strong>Review capacity metrics and throttling.</strong><p>If the Fabric/Premium Capacity Metrics app is available, open it and inspect interactive vs. background workload consumption, refresh pressure, memory usage, and any throttling indicators. If unavailable, discuss the symptoms of throttling (slow refresh, rejected queries, degraded interactivity) and the operational actions an admin would take (scale up, redistribute workloads, or optimize models).</p></li>
    <li><strong>Choose a Gov-safe fallback.</strong><p>For any Fabric-specific feature not yet validated, default to Import mode, well-designed aggregations, incremental refresh (only where Service-side behavior is validated), and standard Power BI Service monitoring as the fallback delivery pattern.</p></li>
    <li><strong>Document architecture recommendation.</strong><p>Write a short recommendation that states the selected licensing/capacity option, the assumptions behind it, the validation steps still required, the fallback path if a feature turns out to be unavailable, known risks, and who needs to review the recommendation before it is finalized.</p></li>
  </ol>
</section>
'@ }
    "11" { return @'
<section>
  <h2>Detailed step-by-step procedure</h2>
  <ol class="steps">
    <li><strong>Define lifecycle management goals.</strong><p>Write down what "good" looks like for this project's delivery process: repeatable builds, reviewable changes, a clear promotion path across environments, governance sign-off points, and a rollback plan if a release goes wrong.</p></li>
    <li><strong>Open the repository.</strong><p>Open the project's git repository and confirm the Power BI work is authored and stored in PBIP format (a <code>.Report</code> folder and a <code>.SemanticModel</code> folder with TMDL/JSON files), and that no <code>.pbix</code> file is being treated as the source of record.</p></li>
    <li><strong>Inspect PBIP structure.</strong><p>Open the <code>.Report/definition</code> folder and note the <code>pages</code>, <code>report.json</code>, and <code>bookmarks</code> structure. Open the <code>.SemanticModel/definition</code> folder and note the <code>tables</code>, <code>relationships.tmdl</code>, and <code>model.tmdl</code> files. Open one table's <code>.tmdl</code> file and identify where columns, measures, and relationships are defined as plain text.</p></li>
    <li><strong>Practice a git workflow.</strong><p>Run <code>git checkout -b my-lab11-change</code> to create a feature branch. Make a small, low-risk change (for example, edit a measure's description or add a new report page). Run <code>git status</code> to see which files changed, run <code>git diff</code> to review exactly what changed line by line, then run <code>git add</code> and <code>git commit -m "..."</code> with a clear, descriptive commit message.</p></li>
    <li><strong>Discuss pull request and release review.</strong><p>List what a reviewer should check before approving a Power BI pull request: model/relationship changes, new or modified measures, data source connection strings, parameters, RLS role definitions, report page changes, any unexpected auto-generated diffs (like GUID churn), a clear release note, a version tag, and evidence that a rollback is possible if needed.</p></li>
    <li><strong>Review Tabular Editor and ALM Toolkit.</strong><p>If these tools are approved for use in your environment, open the semantic model in Tabular Editor to inspect objects, or use ALM Toolkit to compare two versions of the model and generate a change script. If not approved, document the XMLA endpoint access, workstation software approval, customer policy sign-off, and tenant validation that would be required before introducing them.</p></li>
    <li><strong>Review REST API deployment options.</strong><p>Identify the target workspace ID, the correct Power BI REST API or Fabric API cloud endpoint for your tenant (commercial vs. Gov), the permissions/scopes required, and which operations (import, export, refresh) you would automate. Keep hands-on API deployment optional in this lab until the endpoint and permissions have been validated.</p></li>
    <li><strong>Review PowerShell administration.</strong><p>Identify which PowerShell modules are approved (for example, MicrosoftPowerBIMgmt), confirm the correct API endpoint is configured for your cloud, note the admin permissions required to run tenant-level cmdlets, and list 2-3 common administration commands (such as listing workspaces or triggering a refresh) you would use.</p></li>
    <li><strong>Review service principal requirements.</strong><p>Document the steps to register an app in Microsoft Entra ID, get the registration approved by a tenant admin, scope it to a specific security group (not "all users"), assign it the correct workspace role, and store its client secret or certificate securely (such as in a key vault, not in plain text).</p></li>
    <li><strong>Review Fabric Git integration.</strong><p>If available, connect a workspace to a git repository/branch/folder via <b>Workspace settings &gt; Git integration</b>, and review how sync status, incoming/outgoing changes, and conflicts are displayed. If unavailable in your tenant/cloud, use the local PBIP-plus-git workflow from this lab as the Gov-safe equivalent.</p></li>
    <li><strong>Review CI/CD concepts.</strong><p>Walk through a conceptual Azure DevOps or GitHub Actions pipeline for Power BI: a validation stage (lint/check PBIP), a package stage, an authentication stage (service principal login), a deployment stage (API call to import/publish), a configuration stage (per-environment parameters), a smoke-test stage (confirm the report loads and refreshes), and an evidence stage (store logs/screenshots for audit).</p></li>
    <li><strong>Validate Azure Government boundaries.</strong><p>For every automation step above, record the correct Gov cloud endpoint, the identity/authentication method allowed in Gov, network restrictions, customer policy constraints, and whether the specific feature (Git integration, deployment pipelines, REST API) is confirmed available in Azure Government before relying on it.</p></li>
    <li><strong>Complete deployment checklist.</strong><p>Confirm and record: source control is in place and PBIP-based, model/report changes have been validated (opens cleanly, measures work), environment-specific configuration is documented, any automation has been validated in a test run, Azure Government validation notes are current, release evidence is saved, and a rollback path is documented.</p></li>
  </ol>
</section>
'@ }
    "12" { return @'
<section>
  <h2>Detailed step-by-step procedure</h2>
  <ol class="steps">
    <li><strong>Task 1: Build the semantic model.</strong><p>Open or create the capstone PBIP project. Connect to the approved synthetic workshop data sources, create fact and dimension tables using the same naming and column conventions from Lab 1, configure relationships explicitly in Model view, hide technical/key columns from the Fields pane, and label any Gov-sensitive features (Verify for Gov / Commercial-focused) directly in your model documentation.</p></li>
    <li><strong>Task 2: Add advanced DAX.</strong><p>Create base measures (Sales Amount, Gross Margin, Gross Margin %, Quantity), time-intelligence measures (YTD, prior-year, YoY %), variance measures against targets, ranking/Top N measures with <code>RANKX</code>, and dynamic title or measure-switching logic. Validate every measure's totals at the customer, product, territory, and date grain before moving on.</p></li>
    <li><strong>Task 3: Build the report experience.</strong><p>Create the Executive Summary, Analyst Exploration, a detail Drillthrough page, and a Tooltip page following the patterns from Lab 4. Add bookmarks for at least one show/hide or reset interaction, navigation buttons consistent across pages, conditional formatting tied to a documented threshold, a mobile layout, and complete the accessibility checklist (alt text, tab order, contrast, titles).</p></li>
    <li><strong>Task 4: Configure security.</strong><p>Import or create the security mapping table, build a static RLS role and a dynamic RLS role using <code>USERPRINCIPALNAME()</code> following the Lab 7 pattern, test both roles in Desktop with <b>View as</b>, test them in the Service where workspace access is available, and document who should have Build permission and why.</p></li>
    <li><strong>Task 5: Publish and distribute.</strong><p>Publish the PBIP-authored report and semantic model to a training workspace if available. Configure data source credentials and scheduled refresh, document any gateway requirements (or why none are needed), create or review a Power BI App with a defined audience, and document who the intended consumers are and what workspace roles they hold.</p></li>
    <li><strong>Task 6: Govern and operate.</strong><p>Complete an endorsement readiness checklist (ownership, refresh reliability, security, data quality, support evidence), draft a short operations runbook, review usage metrics and refresh history if a workspace is available, and identify the support owner and escalation path for this content.</p></li>
    <li><strong>Task 7: Optional enhanced extensions.</strong><p>Only after explicit validation, layer in Fabric workspace Git integration, Direct Lake, OneLake, Copilot or other AI-assisted authoring, deployment pipelines, REST API automation, service principals, XMLA read/write, external tools, or capacity metrics. For every optional feature you attempt, record its current availability status in this tenant/cloud and the fallback path used if it turns out to be unavailable.</p></li>
    <li><strong>Submit evidence.</strong><p>Package and submit: the PBIP source folder, a completed validation rubric, screenshots or notes documenting each task above, RLS test evidence (roles + test UPNs used), refresh/App/governance evidence where applicable, the operations runbook, and your Azure Government readiness notes covering every feature marked Verify for Gov during the capstone.</p></li>
  </ol>
</section>
'@ }
    default { return "" }
  }
}

function New-LabPage($module, $prev, $next) {
  $tasks = RenderTasks $module.Tasks
  $checks = RenderChecklist $module
  $outcomes = RenderList $module.Outcomes
  $urls = RenderUrls $module.Number
  $labSequence = RenderLabSequence $module.Number
  $howToGuide = RenderHowToGuide $module.Number
  $implementationReference = RenderImplementationReference $module.Number
  $procedure = RenderDetailedProcedure $module.Number
  $answerKey = RenderAnswerKey $module.Number
  $prevLink = if ($prev) { "<a href=""$($prev.File)"">Previous</a>" } else { "<a href=""index.html"">Course home</a>" }
  $nextLink = if ($next) { "<a href=""$($next.File)"">Next</a>" } else { "<a href=""index.html"">Course home</a>" }
  $jeopardyFile = if ([int]$module.Number -le 11) { "jeopardy/lab$($module.Number).html" } else { "jeopardy/final-review.html" }
  $jeopardyLabel = if ([int]$module.Number -le 11) { "Jeopardy review" } else { "Final Jeopardy review" }
  $jeopardyLink = "<a href=""$jeopardyFile"">$jeopardyLabel</a>"
  @"
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Lab $($module.Number) - $(HtmlEncode $module.Title)</title>
  <link rel="stylesheet" href="styles/manual-print.css" media="print">
  $themeScript
  <script src="scripts/delivery-brand.js" defer></script>
  <style>
$baseCss
  </style>
</head>
<body>
  <div class="shell">
    <nav class="topnav">$prevLink<span class="crumb">Lab $($module.Number) of 12</span>$nextLink</nav>
    <header>
      <div class="eyebrow">$(HtmlEncode $module.Eyebrow)</div>
      <h1>$(HtmlEncode $module.Title)</h1>
      <p class="lede">$(HtmlEncode $module.Summary)</p>
      <div class="meta"><span>$(HtmlEncode $module.Level)</span><span>Deliverable: $(HtmlEncode $module.Deliverable)</span><span>PBIP-first</span></div>
    </header>
    <main class="layout">
      <article>
        <section>
          <h2>What you will produce</h2>
          <div class="panel"><ul>$outcomes</ul></div>
        </section>
        $urls
        <section>
          <h2>Walkthrough tasks</h2>
          <div class="task-list">$tasks</div>
        </section>
        $labSequence
        $howToGuide
        $implementationReference
        $procedure
        $answerKey
        <section>
          <h2>Azure Government note</h2>
          <div class="callout">Use the Gov-ready path by default. Features marked Verify for Gov or Commercial-focused require tenant, licensing, capacity, network, identity, or policy validation before hands-on delivery.</div>
        </section>
      </article>
      <aside>
        <div class="checklist" data-progress="lab$($module.Number)">
          <h2>Completion check</h2>
          <div class="progress"><div class="bar"></div></div>
          <p class="small"><span class="count">0</span> of $($module.Checklist.Count) complete</p>
          $checks
        </div>
      </aside>
    </main>
    <nav class="bottomnav">$prevLink$jeopardyLink$nextLink</nav>
    <footer>Power BI Advanced Factory - Synthetic data only - PBIP is the source of record</footer>
  </div>
  <script src="scripts/lab-progress.js"></script>
</body>
</html>
"@
}

function New-IndexPage($modules) {
  $cards = (($modules | ForEach-Object {
    @"
<a class="lab-card" href="$($_.File)">
  <span class="number">$($_.Number)</span>
  <h3>$(HtmlEncode $_.Title)</h3>
  <p>$(HtmlEncode $_.Summary)</p>
  <span class="outcome">$(HtmlEncode $_.Deliverable) - open</span>
</a>
"@
  }) -join "`n")
  @"
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Power BI Advanced Factory Labs</title>
  <link rel="stylesheet" href="styles/manual-print.css" media="print">
  $themeScript
  <script src="scripts/delivery-brand.js" defer></script>
  <style>
$baseCss
  </style>
</head>
<body>
  <div class="shell">
    <header>
      <h1>Power BI Advanced Factory labs</h1>
      <p class="lede">A PBIP-first advanced Power BI lab site with persistent completion checkboxes, raw GitHub CSV data, Azure Government delivery notes, and customer-brandable HTML pages.</p>
      <div class="meta"><span>12 guided labs</span><span>PBIP source control</span><span>Gov-ready core path</span><span>Customer-brandable</span></div>
      <a class="start" href="01-advanced-semantic-modeling.html">Start Lab 1</a>
    </header>
    <main>
      <section>
        <h2>Lab path</h2>
        <div class="roadmap">$cards</div>
      </section>
      <section>
        <div class="panel">
          <h2>Review games</h2>
          <p>Play a classroom Jeopardy review after each lab, or run the cumulative final review before the capstone. Teams earn points by answering clues drawn from that module's knowledge check.</p>
          <p><a class="start" href="jeopardy/index.html" style="margin-top:0;">Open Jeopardy boards</a></p>
        </div>
      </section>
      <section class="requirements">
        <div class="panel">
          <h2>Before you begin</h2>
          <ul>
            <li>Install Power BI Desktop.</li>
            <li>Confirm access to raw.githubusercontent.com.</li>
            <li>Use PBIP as the source-controlled format.</li>
            <li>Use the Gov-ready path unless optional features are validated.</li>
          </ul>
        </div>
        <div class="panel">
          <h2>Branding</h2>
          <p>Edit <code>scripts\delivery-config.js</code> to set the customer name, logo, badge, and accent colors. Alternate configs can be tested with the <code>brandConfig</code> query-string parameter.</p>
        </div>
      </section>
    </main>
    <footer>Power BI Advanced Factory - HTML lab instructions</footer>
  </div>
</body>
</html>
"@
}

Write-Utf8NoBom -Path (Join-Path $stylesRoot "lab-site.css") -Content $baseCss
Write-Utf8NoBom -Path (Join-Path $stylesRoot "manual-print.css") -Content $printCss
Write-Utf8NoBom -Path (Join-Path $scriptsRoot "delivery-brand.js") -Content $brandJs
Write-Utf8NoBom -Path (Join-Path $scriptsRoot "lab-progress.js") -Content $progressJs
Write-Utf8NoBom -Path (Join-Path $scriptsRoot "delivery-config.js") -Content $deliveryConfig
Write-Utf8NoBom -Path (Join-Path $webRoot "BRANDING.md") -Content $brandingReadme

$webImagesRoot = Join-Path $webRoot "images"
$module02ImagesRoot = Join-Path $webImagesRoot "02-advanced-dax"
New-Item -ItemType Directory -Force -Path $module02ImagesRoot | Out-Null
$calculationGroupImage = Join-Path $repoRoot "Student\Labs\Source\02-advanced-dax\images\CalculationGroups-annotated.png"
if (Test-Path $calculationGroupImage) {
  Copy-Item -Path $calculationGroupImage -Destination (Join-Path $module02ImagesRoot "CalculationGroups-annotated.png") -Force
}

Write-Utf8NoBom -Path (Join-Path $webRoot "index.html") -Content (New-IndexPage $modules)
for ($i = 0; $i -lt $modules.Count; $i++) {
  $prev = if ($i -gt 0) { $modules[$i - 1] } else { $null }
  $next = if ($i -lt ($modules.Count - 1)) { $modules[$i + 1] } else { $null }
  Write-Utf8NoBom -Path (Join-Path $webRoot $modules[$i].File) -Content (New-LabPage $modules[$i] $prev $next)
}

Write-Host "Generated HTML labs in $webRoot"


