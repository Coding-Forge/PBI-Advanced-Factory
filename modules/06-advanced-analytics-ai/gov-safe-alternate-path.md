# Gov-Safe Alternate Path

Use this path when advanced analytics or AI-assisted features are unavailable, unvalidated, or disallowed in an Azure Government delivery environment.

## Required Gov-ready core

| Goal | Gov-safe approach |
|---|---|
| Scenario analysis | What-if parameters and DAX measures. |
| Driver analysis | Matrix, bar chart, slicers, drillthrough, and manually selected explanatory fields. |
| Trend analysis | Line charts, rolling averages, and DAX variance measures. |
| Exception detection | Rule-based DAX flags and conditional formatting. |
| Segmentation | Explicit dimension attributes, grouping, and DAX segmentation. |
| Narrative guidance | Static text boxes, dynamic titles, and documented interpretation notes. |

## AI feature fallback map

| AI or advanced feature | Fallback |
|---|---|
| Key influencers | Rank measures, Top N visuals, and side-by-side dimension comparison. |
| Decomposition tree | Matrix hierarchy, drillthrough, and stacked bar charts by selected dimensions. |
| Forecasting | Rolling average, prior-period comparison, and manually documented assumptions. |
| Anomaly detection | DAX thresholds, standard deviation bands, and conditional formatting. |
| Python/R visuals | Native visuals and precomputed data preparation outside the lab. |
| Azure ML integration | Import scored sample output as a static dataset. |
| Copilot | Instructor-provided prompts and static examples without live AI execution. |

## Required documentation

For each unavailable feature, document:

- Feature name
- Intended learning goal
- Availability status
- Reason it is not required
- Gov-safe alternate lab step
- Any customer validation needed for future use

