# Module 2 Labs: Advanced DAX

## Lab summary

These labs build a trusted DAX measure layer over the Module 1 semantic model.

## Azure Government readiness

The required labs are **Gov-ready** because they use Power BI Desktop and core DAX. DAX Studio and other external-tool diagnostics are **Verify for Gov**.

## Prerequisites

- Completed Module 1 semantic model or equivalent model.
- Tables named similarly to `FactSales`, `FactTargets`, `DimOrderDate`, `DimCustomer`, `DimProduct`, `DimTerritory`, `DimSegment`, and `BridgeCustomerSegment`.

## Lab 1: Row context vs. filter context

**Objective:** Diagnose why measures evaluate differently in different visuals.

### Tasks

1. Create base sales, quantity, and gross margin measures.
2. Add a table visual by customer and product category.
3. Add slicers for territory and date.
4. Observe how slicers and visual rows change filter context.
5. Create a calculated column example only to demonstrate row context, then discuss why measures are preferred for aggregations.

### Expected result

Learners can explain why the same measure returns different values across visual cells, slicers, and totals.

## Lab 2: Context transition and `CALCULATE`

**Objective:** Use `CALCULATE` to intentionally modify filter context.

### Tasks

1. Create `[Sales Amount]`.
2. Create a measure that removes product filters.
3. Create product sales share using the unfiltered product total.
4. Create a measure with `KEEPFILTERS` for a selected customer type.
5. Compare results in visuals with slicers applied.

### Expected result

Learners can explain filter replacement, filter removal, and filter preservation.

## Lab 3: Advanced time intelligence

**Objective:** Create reusable time-intelligence measures.

### Tasks

1. Validate the order date table.
2. Create Sales YTD.
3. Create Sales Prior Year.
4. Create Sales YoY and Sales YoY %.
5. Create a rolling 90-day sales measure.
6. Validate results by month.

### Expected result

Learners can branch time-intelligence measures from a trusted base measure.

## Lab 4: Semi-additive measures

**Objective:** Understand measures that should not be summed across time.

### Tasks

1. Review the difference between transaction facts and snapshot facts.
2. Discuss examples such as inventory, backlog, headcount, or account balance.
3. Create or review an ending-balance-style pattern using the DAX pattern reference.
4. Explain why summing snapshots across dates produces incorrect answers.

### Expected result

Learners can identify semi-additive scenarios and choose an appropriate last-value or last-nonblank pattern.

## Lab 5: Dynamic Top N and ranking

**Objective:** Rank customers and filter visuals to a dynamic Top N view.

### Tasks

1. Create a customer sales rank measure.
2. Create an `Is Top 5 Customer` flag measure.
3. Add a customer bar chart.
4. Filter the visual to Top 5 customers.
5. Compare `ALL`, `ALLSELECTED`, and visual filters.

### Expected result

Learners can build rankings that respect the intended report context.

## Lab 6: Dynamic titles and measure switching

**Objective:** Make report text and metrics respond to user selections.

### Tasks

1. Create a dynamic title measure using selected territory or region.
2. Create a disconnected `MetricSelector` table.
3. Create a selected metric measure using `SWITCH`.
4. Add a slicer for metric selection.
5. Validate formatting and fallback behavior.

### Expected result

Learners can create guided flexibility without duplicating pages or visuals.

## Lab 7: DAX optimization

**Objective:** Improve readability and reduce repeated calculations.

### Tasks

1. Identify a measure with repeated logic.
2. Rewrite it using variables.
3. Branch from base measures instead of duplicating aggregation logic.
4. Test the optimized measure in a simple visual.
5. Optional: use DAX Studio or Performance Analyzer to compare behavior.

> **Azure Government note:** DAX Studio is marked **Verify for Gov**. Validate customer workstation policy, external tool usage, Service connectivity, and XMLA settings before making this a required lab step.

### Expected result

Learners can improve measure maintainability and know when external diagnostics require validation.

## Validation checklist

- [ ] Base measures exist and are formatted.
- [ ] Time-intelligence measures return expected values by month.
- [ ] Semi-additive pattern is explained or implemented.
- [ ] Ranking works at the intended filter scope.
- [ ] Dynamic title has a fallback value.
- [ ] Measure switch handles missing or multi-select cases.
- [ ] DAX optimization uses variables and measure branching.
- [ ] DAX Studio and external tooling are labeled **Verify for Gov**.

