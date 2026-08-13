# Auto Date/Time Cleanup TODO

## Background

`pbi-local\AdvancedPBI.SemanticModel` was built with Power BI Desktop's **Auto Date/Time**
option left on. Every `dateTime` column without an explicit relationship (and, in some
cases, columns that *do* have an explicit role-playing date dimension) picked up a hidden
`LocalDateTable_*` table, a `DateTableTemplate_*` template table, an automatic
`joinOnDateBehavior: datePartOnly` relationship, and a default `variation` block on the
source column. This clutters the model with tables that were never part of the documented
lab design and, on `FactSales.OrderDate` / `FactSales.ShipDate`, duplicated the explicit
`DimOrderDate` / `DimShipDate` role-playing relationships taught in Lab 01 Lab 2.

This was fixed in `pbi-local\AdvancedPBI.SemanticModel` on 2026-08-13:

- Set `annotation __PBI_TimeIntelligenceEnabled = 0` in `model.tmdl` (Options > Current
  File > Data Load > **Auto date/time for new files** equivalent, stored per-model) so the
  behavior does not silently return next time a date column is added or the model is
  reloaded in Desktop.
- Removed all `LocalDateTable_*` and `DateTableTemplate_*` `ref table` entries from
  `model.tmdl`.
- Deleted the corresponding `LocalDateTable_*.tmdl` / `DateTableTemplate_*.tmdl` table
  files.
- Removed the auto-generated relationships in `relationships.tmdl` that pointed at those
  tables (`FactSales.OrderDate`, `FactSales.ShipDate`, `FactSales.InvoiceDate`,
  `FactTargets.TargetMonth`, `FactOrders.OrderDate`).
- Removed the matching `variation` blocks from `FactSales.tmdl`, `FactTargets.tmdl`, and
  `FactOrders.tmdl`.

No DAX measure or calculation group referenced the auto date tables (all time
intelligence in `_Measures` and `Time Calculation` uses `DimOrderDate[Date]`), so removing
them does not change any measure behavior. `FactSales.InvoiceDate`, `FactTargets.TargetMonth`,
and `FactOrders.OrderDate` now have no date-dimension relationship, same as before the
Auto Date/Time tables existed as a side effect — they never provided real filtering for
those columns beyond a default drill hierarchy nobody used.

## Remaining work: other module PBIP projects

The same Auto Date/Time leftovers exist in these projects. They were intentionally **not**
touched in this pass so each module's starter/solution history stays isolated; clean up
each one using the same steps as above when that module is revisited:

- [ ] `Student\Labs\Source\01-advanced-semantic-modeling\solution\AdvancedPBI.SemanticModel`
  - `LocalDateTable_2c05766e-6153-432b-a89d-0970cbe753ed`
  - `LocalDateTable_5e0f18ab-e4cf-4db6-9037-d06fd708ed09`
  - `LocalDateTable_252c1600-f105-4832-bef8-c700c8027c13`
  - `LocalDateTable_6da3a195-0266-4b53-82d4-7196f21a806d`
  - `DateTableTemplate_2f05558b-2c6a-4aa8-8376-af48161fbf47`
  - Note: this is the **shipped solution** for Lab 01, whose own README/validation
    checklist says "Role-playing dates work without ambiguity" — the leftover auto date
    tables directly contradict that checklist item, so prioritize this one first.
- [ ] `Student\Labs\Source\02-advanced-dax\starter\AdvancedPBI.SemanticModel` — same 5 tables.
- [ ] `Student\Labs\Source\02-advanced-dax\solution\AdvancedPBI.SemanticModel` — same 5 tables.
- [ ] `Student\Labs\Source\03-advanced-power-query\starter\AdvancedPBI.SemanticModel` — same 5 tables.
- [ ] `Student\Labs\Source\03-advanced-power-query\solution\AdvancedPBI.SemanticModel` — same
  5 tables **plus** `LocalDateTable_35731b34-cb56-4998-ba94-589bde342bb3` (FactOrders.OrderDate)
  and `LocalDateTable_f2d13506-c798-47ce-b8bc-f3d872b81c32` (an additional local date table
  not present in the other projects — confirm which column it's attached to before removing).

## Steps to repeat per project

1. In `definition\model.tmdl`:
   - Set `annotation __PBI_TimeIntelligenceEnabled = 0`.
   - Delete the `ref table LocalDateTable_*` and `ref table DateTableTemplate_*` lines.
2. Delete the corresponding `definition\tables\LocalDateTable_*.tmdl` and
   `DateTableTemplate_*.tmdl` files.
3. In `definition\relationships.tmdl`, delete every `relationship` block whose `toColumn`
   points at a `LocalDateTable_*.Date`.
4. In the fact table `.tmdl` files (`FactSales.tmdl`, `FactTargets.tmdl`,
   `FactOrders.tmdl`, and any others with a date column), delete the `variation Variation`
   block under the affected column, keeping the `annotation SummarizationSetBy` /
   `annotation UnderlyingDateTimeDataType` lines that follow.
5. Reopen the `.pbip` in Power BI Desktop, confirm Model view shows only the intended
   relationships, and confirm Options > Current File > Data Load > **Auto date/time for new
   files** is unchecked for that file.
6. Refresh and spot-check existing visuals/measures still return the same values.
