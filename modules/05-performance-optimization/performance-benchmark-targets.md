# Performance Benchmark Targets

Use these targets as teaching benchmarks. They are not universal production SLAs; production targets should be adjusted for customer data volume, capacity, network, source systems, and user expectations.

## Report interaction targets

| Area | Training target | Notes |
|---|---|---|
| Initial page load | Under 5 seconds for workshop data | Small synthetic data should load quickly. |
| Slicer interaction | Under 2 seconds for core pages | If slower, inspect visual count and DAX query time. |
| Drillthrough navigation | Under 3 seconds for workshop data | Detail pages should use focused visuals. |
| Tooltip display | Under 1 second for workshop data | Tooltip pages should stay lightweight. |
| Mobile page interaction | Under 3 seconds for workshop data | Mobile layout should use fewer visuals. |

## Model design targets

| Area | Training target | Notes |
|---|---|---|
| Unused columns | Remove from final model | Keep only fields needed for reporting, relationships, and calculations. |
| High-cardinality text | Avoid unless required | Consider splitting, grouping, or excluding. |
| Date/time columns | Split when appropriate | Reduces cardinality and improves compression. |
| Relationship direction | Single-direction by default | Use bi-directional only with documented justification. |
| Measures | Branch from base measures | Avoid repeated aggregation logic. |

## DAX targets

| Area | Training target | Notes |
|---|---|---|
| Base measures | Simple and reusable | Use `SUM`, `COUNTROWS`, `DISTINCTCOUNT`, and similar primitives. |
| Derived measures | Use variables when logic repeats | Improve readability and avoid repeated computation. |
| Filter removal | Scope narrowly | Prefer column/table-specific filter removal. |
| Ranking | Preserve intended selection context | Choose `ALL`, `ALLSELECTED`, or scoped tables intentionally. |

## Refresh targets

| Area | Training target | Notes |
|---|---|---|
| Query folding | Preserve through source filters where possible | Source-dependent and must be validated. |
| Full refresh | Avoid for large production facts | Use incremental refresh when supported. |
| Error rows | Capture or document | Do not silently discard without a business rule. |

## Azure Government validation targets

- Confirm whether external tools are allowed on the customer workstation.
- Confirm XMLA endpoint availability before using Service model diagnostics.
- Confirm incremental refresh support for the workspace/license/cloud.
- Confirm capacity metrics app availability before making it a required lab.
- Confirm connector and gateway support before DirectQuery or aggregation labs.

