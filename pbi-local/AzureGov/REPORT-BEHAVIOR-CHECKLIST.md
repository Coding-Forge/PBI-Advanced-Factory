# AzureGov Report — Expected Visual Behavior Checklist

Use this while clicking through `AdvancedPBI.pbip` in Power BI Desktop to confirm each
visual behaves as designed. Check off items as you verify them.

**Model context:** Star schema with `FactSales` (line-item transactions) at the
center, `DimCustomer` / `DimProduct` / `DimTerritory` / `DimOrderDate` /
`DimShipDate` dimensions, a `BridgeCustomerSegment` many-to-many bridge to
`DimSegment`, `FactTargets` (monthly snapshot targets), and RLS roles
`East Region` (static) and `Dynamic Territory Security` (dynamic, via
`SecurityUserTerritory`). All 5 pages share 4 nav buttons in the same screen
position for cross-page navigation.

---

## Page 1 — Executive Overview

- [ ] **Title card** ("Sales Overview — [Territory/Region]"): text changes
      dynamically based on whichever territory/region slicer selection is
      active; shows "All Territories" when nothing is selected.
- [ ] **4 KPI cards** (Sales Amount, Gross Margin %, Order Count, Sales
      YoY %): plain numbers that recalculate instantly as any slicer/cross-filter
      on the page changes.
- [ ] **Date slicer** (Order Date): filters every visual on the page, including
      the trend line and territory matrix.
- [ ] **Region slicer** (Territory Region): filters everything on the page;
      also drives the dynamic title text.
- [ ] **Trend line chart** (Sales YTD, Sales Prior Year, Sales YoY % vs. Date):
      three lines on one chart — YTD accumulates within the selected year,
      Prior Year shows the same calendar period shifted back one year, YoY %
      is the delta between them. Selecting a date range (or via the date
      slicer) should re-shape all three lines together.
- [ ] **Territory matrix** (Territory Region → Territory Name rows, Sales
      Amount & Gross Margin % columns): expandable/collapsible outline rows;
      clicking a row cross-filters the KPI cards and trend line.
- [ ] **Nav buttons (4)**: click to jump to Executive Overview / Sales &
      Margin Analysis / Customer & Segmentation Detail / Security &
      Navigation pages — no data reset.

**Interaction check:** slicing region/date should move every number on the
page in sync; clicking a territory row in the matrix should also filter the
KPI cards/trend line, not just highlight it.

---

## Page 2 — Sales & Margin Analysis

- [ ] **Margin Target slicer** (list: 20% / 25% / 30% / 35% / 40%):
      single-select "what-if" list — the label picked determines
      `Selected Margin Target`.
- [ ] **Margin Adjustment % slicer** (numeric range slider, –10% to +20%, 1%
      steps, default 0%): a true drag slider (What-If Parameter) — dragging
      it changes `Selected Margin Adjustment %`.
- [ ] **Target KPI card** (Selected Margin Target): echoes back whichever
      target % is selected in the first slicer.
- [ ] **Adjusted Gross Margin KPI card**: recalculates as
      `Gross Margin % + adjustment%` × Sales Amount — should visibly move in
      real time as you drag the adjustment slider, even with no target
      slicer selection.
- [ ] **Status KPI card** (Gross Margin vs Target): shows the numeric gap
      between actual Gross Margin % and the selected target; sign flips
      (positive/negative) depending on target chosen.
- [ ] **Margin table** (Territory × Product Category, Gross Margin %, Gross
      Margin vs Target, Margin Target Status): **conditional formatting** —
      row/cell background color should change (green = Above/At target,
      amber = Near target, red = Below target) as you change the target
      slicer. This is the main conditional-formatting demo on this page.
- [ ] **Rank table** (Customer, Sales Amount, Customer Sales Rank, Is Top 5
      Customer): rank recalculates based on whatever filter context is
      active (only cross-filtering from this page's own visuals, since there
      are no region/date slicers on this page).
- [ ] **Nav buttons (4)**: same cross-page navigation as page 1.

**Interaction check:** dragging the Margin Adjustment % slider should
immediately move the Adjusted Gross Margin card; changing the Margin Target
list selection should change the Status card and re-color the margin table.

---

## Page 3 — Customer & Segmentation Detail

- [ ] **Metric slicer** (Metric Parameter list: Sales Amount / Gross Margin /
      Gross Margin % / Quantity): a plain single-select list — used only to
      filter, NOT connected to the chart below (intentionally a separate,
      simpler slicer pattern next to the field-parameter chart for
      contrast).
- [ ] **Metric chart** (bar chart, Product Category by a switchable Y-axis
      bound to the `PBI Field Parameters` field parameter: Sales Amount /
      Gross Margin / Gross Margin % / Quantity): the **true field-parameter
      demo** — changing which measure drives the Y-axis (e.g. via a slicer
      bound to the same field parameter, or the visual's built-in field
      parameter controls) should re-scale/re-label the bars.
- [ ] Custom tooltip: hovering a bar on the metric chart shows the Sales
      Detail Tooltip page.
- [ ] **Segment table** (Customer Name, Sales Amount): reflects the
      customer→segment many-to-many bridge — a customer can be reachable
      through multiple segments via the bridge table's bothDirections
      relationship.
- [ ] **Date compare table** (Territory Region, Sales by Order Date, Sales by
      Ship Date): the two measures use two different active relationships to
      two role-playing date dimensions (`DimOrderDate` vs `DimShipDate`) —
      values should differ slightly since not every order ships the same
      day/period.
- [ ] **Customer transactions table** (line-item detail: SalesOrderLineKey,
      OrderDate, Customer, Product Category, Quantity, Sales Amount, Gross
      Margin, Gross Margin %): raw transaction grain, cross-filters with
      everything else on the page.
- [ ] **Nav buttons (4)**.

**Interaction check:** the metric chart's Y-axis should be changeable to any
of the 4 measures via field-parameter mechanics, and the bars should
re-scale/re-label accordingly. Hovering a bar should pop the custom tooltip
page.

---

## Page 4 — Security, Navigation & Tooltip

- [ ] **RLS instructions textbox**: static text — no interactivity, just
      guidance to use Desktop's "View As Roles" to test `East Region`
      (static) and `Dynamic Territory Security` (dynamic, via
      `USERPRINCIPALNAME()`).
- [ ] **Security table** (UserPrincipalName, TerritoryKey, TerritoryName from
      `SecurityUserTerritory`): the mapping table that drives the dynamic RLS
      role — shows all mapped users/territories when viewed as report author
      (no role applied). Using "View As Role → Dynamic Territory Security"
      with a specific UPN should filter this (and everything else in the
      model) down to only that user's assigned territory.
- [ ] **Tooltip chart** (bar chart, same field-parameter Y-axis switcher as
      page 3's metric chart, by Product Category): same field-parameter
      behavior as page 3; also wired to show the Sales Detail Tooltip page
      on hover.
- [ ] **Nav buttons (4)**.

**Interaction check:** applying "View As → East Region" should restrict all
territory-based visuals report-wide to only the "East" region; applying
"View As → Dynamic Territory Security" with a specific user should restrict
to just that user's territory per the `SecurityUserTerritory` mapping.

---

## Page 5 — Sales Detail Tooltip (hidden tooltip page, not in nav)

- [ ] Small 320×240 canvas, only reachable by hovering a data point on the
      metric_chart/tooltip_chart bars (or any other visual wired to it).
- [ ] **Tooltip line chart** (Sales Amount by Date): mini trend for the
      hovered category.
- [ ] **Tooltip sales / Tooltip margin visuals**: additional KPI-style detail
      for the hovered category (Sales Amount, Gross Margin context).
- [ ] Should **not** appear in normal page navigation/tabs — only as a
      floating tooltip popup.

---

## Highest-risk areas to double-check first

1. Field-parameter axis-switching on the metric chart (page 3) and tooltip
   chart (page 4) — this is the most failure-prone Power BI mechanic.
2. Conditional-formatting colors on page 2's margin table (green/amber/red
   by Margin Target Status).
3. RLS "View As Role" behavior for both `East Region` and
   `Dynamic Territory Security` on page 4.
