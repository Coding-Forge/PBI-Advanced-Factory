# Labs 1–7 Completion Notes (pbi-local)

This document tracks the review of `pbi-local` against the Module 1–7 lab
guides in `Student\Labs\Source\`, what was implemented directly in the PBIP,
and what remains conceptual, discussion-only, or **Verify for Gov** by design.

## Summary of hands-on changes made to `pbi-local`

| Module | Lab | Status | Notes |
|---|---|---|---|
| 1 | Lab 1 Star schema refactor | Done | `FactSales`, `DimCustomer`, `DimProduct`, `DimTerritory`, `DimProductCategory` all match the lab's exact column/keep-remove spec. |
| 1 | Lab 2 Role-playing dimensions | Done | `DimOrderDate`/`DimShipDate` built via `fn_DimDate`; relationships to `FactSales` are one-to-many, single-direction. |
| 1 | Lab 3 Bridge table pattern | Done | `BridgeCustomerSegment` + `DimSegment` implemented per spec. |
| 1 | Lab 4 Composite/DirectQuery comparison | **Conceptual only** | See [Conceptual/Gov-only items](#conceptual-and-gov-only-items) below. |
| 2 | Labs 1–3, 5–8 | Done | Base measures, `CALCULATE`/`KEEPFILTERS` patterns, time intelligence, ranking/Top N, dynamic title/metric switcher, calculation group (`Time Intelligence`/`Time Calculation`), DAX variables used throughout. |
| 2 | Lab 4 Semi-additive measures | Done | Added `Target Sales Amount (Ending Balance)` measure demonstrating the last-value-by-month pattern against `FactTargets` (a monthly snapshot fact). |
| 3 | Labs 1–5 | Done | Staged query architecture (`raw_Orders_*` → `stg_OrdersCombined` → `FactOrders`), folder-style monthly combine, all 5 parameters (`RawDataBaseUrl`, `SourceFolderPath`, `EnvironmentName`, `RangeStart`, `RangeEnd`), `fn_CleanText`, `err_OrdersReview` data-quality review query. |
| 3 | Lab 6 Query folding | **Conceptual only** | See below — CSV/Web sources in this workshop do not fold. |
| 3 | Lab 7 Incremental refresh prep | Done | `FactOrders` now filters `OrderDate` using `RangeStart`/`RangeEnd` so the query is functionally ready for a Service-side incremental refresh policy. |
| 4 | Lab 1 Drillthrough | Done | `Customer Detail` page added, bound to `DimCustomer[CustomerName]` drillthrough filter, with KPI cards, transaction table, and Back button. |
| 4 | Lab 2 Report page tooltip | Done | `Sales Tooltip` page added (Tooltip page type) and assigned to the Executive Summary matrix visual. |
| 4 | Lab 3 Bookmarks and buttons | Done | `Show Info` / `Hide Info` bookmarks and buttons added on the Dynamic Navigation page, toggling an info panel visual. |
| 4 | Lab 4 Dynamic navigation | Done | Existing `Dynamic Navigation` page/buttons already present. |
| 4 | Lab 5 Field parameters | Done | `Metric Parameter` field parameter and disconnected `Margin Target` what-if pattern already present. |
| 4 | Lab 6 Conditional formatting | Done | `Margin Target Status Color` measure + Conditional Formatting page already present. |
| 4 | Lab 7 Mobile layout | Done | `Mobile Layout Check` page already present. |
| 4 | Lab 8 Accessibility review | **Documentation only** | See below — this lab is a review/checklist exercise, not a build task. |
| 5 | All labs | **Documentation/process only** | Performance Analyzer, model size/cardinality review, DAX Studio, visual optimization, aggregation tables, and incremental refresh policy are process/analysis exercises performed live in Desktop/Service, not static PBIP artifacts. See below. |
| 6 | Lab 1 What-if parameters | Done | Native What-If parameter `Margin Adjustment %` (-10% to 20%, 1% step) added with `Adjusted Gross Margin %`/`Adjusted Gross Margin` measures and a slicer/card on the Margin Target What-If page. |
| 6 | Labs 2–7 | **Verify for Gov / Conceptual** | Decomposition tree, forecasting, key influencers, Python/R, Azure ML, Copilot — see below. |
| 7 | Lab 1 Static RLS | Done | `East Region` role added, filtering `DimTerritory[TerritoryRegion] = "East"`. |
| 7 | Lab 2 Dynamic RLS | Done | `SecurityUserTerritory` table imported from `data/security/security-user-territory.csv`, related to `DimTerritory[TerritoryKey]`; `Dynamic Territory Security` role filters `SecurityUserTerritory[UserPrincipalName] = USERPRINCIPALNAME()`. |
| 7 | Lab 3 Testing roles in Desktop/Service | **Manual/process** | Use **Modeling > View as** in Desktop with sample UPNs from `security-user-territory.csv` (e.g. `alex.manager@contoso.example`, `devon.director@contoso.example`, `jordan.rep@contoso.example`). Service-side testing requires publishing to a workspace — not applicable to `pbi-local` as a local PBIP. |
| 7 | Lab 4 Build permission | **Conceptual/discussion** | See below. |
| 7 | Optional: OLS, sensitivity labels | **Verify for Gov** | See below. |

## Conceptual and Gov-only items

These lab sections are intentionally **not** implemented as PBIP artifacts,
either because the lab itself defines them as discussion/conceptual tasks,
because they depend on Power BI Service/tenant features that aren't present
in a local PBIP, or because the target environment (Azure Government) needs
separate validation per the module's own Gov-readiness notes.

### Module 1 Lab 4 — Composite model / DirectQuery comparison
Conceptual by design. Discussion points for delivery:
- **Import candidates:** all current dimensions and facts (`DimCustomer`, `DimProduct`, `DimTerritory`, date tables, `FactSales`, `FactTargets`, `FactOrders`) — small/medium volume, refreshed on a schedule, no real-time requirement.
- **DirectQuery candidates:** none in this workshop's synthetic dataset; would apply to a live, frequently-changing operational source (e.g., an ERP order table) if this model were extended.
- **Dual mode candidates:** shared dimensions like `DimProductCategory`/`DimTerritory` if a composite model paired an Import fact table with a DirectQuery fact table, to avoid duplicate query plans.
- **Tradeoffs to discuss:** DirectQuery trades performance/DAX feature parity for freshness and reduced storage; Dual mode lets Power BI choose the most efficient plan per query; composite models increase authoring complexity and require careful relationship/aggregation design.
- **Azure Government note:** Verify for Gov — composite/DirectQuery source, gateway, and tenant support must be validated per target environment.

### Module 3 Lab 6 — Query folding
Conceptual/partial by design given the data sources used:
- All current sources are CSV files served over `Web.Contents` (GitHub raw URLs). **CSV/Web sources do not support query folding** — Power BI must download and locally process the full file before applying any Power Query steps.
- To demonstrate folding hands-on, a SQL Server, Fabric Warehouse/Lakehouse SQL endpoint, or similar folding-capable connector would be required; this is outside the scope of the local synthetic-CSV dataset.
- **Discussion path used instead:** compare a filter step applied directly in `Csv.Document`/`Table.SelectRows` (not folded, always full download) vs. what folding would look like against a SQL source (`View Native Query` available, filter pushed to the source engine).
- **Gov note:** Gov-ready / Verify for source — folding behavior depends entirely on the connector and source, which must be validated per environment.

### Module 4 Lab 8 — Accessibility review
This is a review/checklist exercise rather than a build task. Recommended review notes for `pbi-local`:
- **Alt text:** add descriptive alt text to KPI cards and charts (e.g., "Line chart showing sales trend by order date") — not yet set on newly added visuals; recommend setting via the visual's Alt Text formatting pane in Desktop.
- **Tab order:** review and set explicit tab order per page so keyboard navigation follows a logical KPI → filter → detail flow; the `tabOrder` property already exists per visual container and should be audited page-by-page in Desktop.
- **Color contrast:** the `Margin Target Status Color` measure uses standard status colors (`#107C10` green, `#FFB900` amber, `#D13438` red) — verify these meet WCAG AA contrast against the report's background/theme.
- **Descriptive titles/labels:** confirm every visual has a meaningful title (many currently rely on default field-based titles); recommend an editorial pass before delivery.
- **Non-color meaning:** `Margin Target Status` already pairs color with a text status label (Above/At/Near/Below target), satisfying the "don't rely on color alone" requirement.

### Module 5 — Performance Optimization (all labs)
This entire module is a **live diagnostic/process exercise** performed against a running Desktop session or Service workspace, not something that produces static PBIP file changes. Recommended facilitation notes:
- **Lab 1 Performance Analyzer:** run in Desktop against the Executive Summary and Dynamic Navigation pages; the pivotTable/matrix visuals with expanded hierarchies are good first candidates to test given their row-level expansion.
- **Lab 2 Model size/cardinality:** `FactSales` (~60K rows) and `FactOrders` (~450 rows) are both low/medium cardinality for this workshop; no columns were identified as unnecessary high-cardinality risks in the current schema. `CustomerName`, `ProductName`, `SalesChannel` are the highest-cardinality text columns and are reasonable candidates for a cardinality discussion.
- **Lab 3 DAX Studio:** Verify for Gov — requires external tool approval.
- **Lab 4 Visual optimization:** review page visual counts; Executive Summary and Dynamic Navigation currently each have 3 visuals, within a reasonable range.
- **Lab 5 Aggregation table:** conceptual grain design — a Month × Territory × ProductCategory summary of `FactSales[SalesAmount]`/`[GrossMargin]` would be the natural aggregation candidate.
- **Lab 6 Incremental refresh policy:** `FactOrders` is now prepared with `RangeStart`/`RangeEnd` filtering (see Module 3 Lab 7 above); applying and running the actual policy requires publishing to the Service — Verify for Gov.

### Module 6 Labs 2–7 — AI-assisted / advanced visuals
All Verify for Gov / Commercial-focused per the module's own guidance; not implemented as hands-on PBIP artifacts:
- **Lab 2 Decomposition tree:** Gov-safe alternate path (matrix hierarchy + drillthrough) is already available via the Customer Detail drillthrough page and the Executive Summary/Dynamic Navigation matrices.
- **Lab 3 Forecasting:** Gov-safe alternate path — `Sales Rolling 90 Days` and `Sales YoY`/`Sales Prior Year` measures already provide trend/comparison context without the Analytics-pane forecast feature.
- **Lab 4 Key influencers:** Gov-safe alternate path — `Customer Sales Rank`/`Is Top 5 Customer` measures already support ranked/Top-N comparison.
- **Lab 5 Python/R visuals, Lab 6 Azure ML, Lab 7 Copilot:** conceptual only; no tenant validation performed for this workshop.

### Module 7 Lab 4 — Build permission behavior
Conceptual/discussion task, not a PBIP artifact:
- **Build permission** grants a user the ability to create new reports/Analyze in Excel connections against the published semantic model, independent of any specific report's RLS.
- **Recommended persona mapping** (from `data/security/security-role-matrix.csv`): Executive Sponsor and Regional Manager personas should **not** have Build permission (App Viewer only); Analyst and Semantic Model Developer personas may have Build permission if approved for thin-report authoring.
- **Risk/governance discussion:** Build permission bypasses report-level visuals but **does not bypass RLS** — a user with Build permission and the `Dynamic Territory Security` role still only sees their assigned territories in any report/Excel connection they build. Document this clearly for the audience since it's a common point of confusion.
- This can only be configured/demonstrated once the semantic model is published to the Service — Verify for Gov.

### Module 7 Optional labs — OLS and sensitivity labels
Both explicitly marked **Verify for Gov** in the lab guide; not implemented:
- **Object-level security (OLS):** would require Tabular Editor or XMLA-endpoint tooling not used in this local-PBIP workflow. Candidate sensitive fields for an OLS discussion: none in the current synthetic dataset are sensitive enough to warrant OLS (all data is synthetic), but `SecurityUserTerritory[UserPrincipalName]` would be a reasonable "hide this table/column from report authors" candidate in a real deployment.
- **Sensitivity labels:** require Microsoft Purview Information Protection configuration at the tenant level — outside the scope of a local PBIP file and must be validated per target Azure Government tenant.

## Other known gaps (carried over from earlier review, not part of Labs 1–7 scope)

- `docs\auto-date-time-cleanup-todo.md` — Auto Date/Time leftovers still present in the 5 other module PBIP projects (Module 1 solution, Module 2 starter/solution, Module 3 starter/solution). Not addressed here per explicit scoping to `pbi-local` only.
- `Student\Labs\Source\01-03\data` — per-module authoring data copies still contain the original small sample CSVs and have not been resynced with `tools\generate-sample-data.py`.
