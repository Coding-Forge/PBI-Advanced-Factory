# Instructor Guide

## Module summary

Advanced semantic modeling is the foundation for every other advanced Power BI topic. Emphasize that DAX, performance, security, and report UX all become easier when the model is intentionally designed.

## Audience and prerequisites

Best fit for report authors, semantic model developers, data engineers, BI platform owners, and Power BI administrators who understand basic Power BI Desktop modeling and publishing.

Learners should already understand tables, relationships, basic measures, slicers, filters, and Service publishing.

## Learning objectives

- Distinguish facts, dimensions, bridge tables, helper tables, and disconnected parameter tables.
- Convert a flat reporting dataset into a star schema.
- Explain relationship cardinality and filter direction tradeoffs.
- Implement role-playing date analysis.
- Use a bridge table for many-to-many analysis.
- Compare Import, DirectQuery, Dual, and composite model patterns.
- Identify Gov-ready, Verify for Gov, and Commercial-focused modeling capabilities.

## Delivery flow

1. Start with the business problem: one report has become slow, hard to maintain, and inconsistent.
2. Show the flat source data and ask learners what will become facts and dimensions.
3. Introduce the target star schema.
4. Build relationships and discuss cardinality/filter direction.
5. Add role-playing date analysis and show both approved date table creation patterns: reusable Power Query function and quick DAX `CALENDAR` table.
6. Introduce bridge tables for multi-valued customer segments.
7. Discuss composite model tradeoffs conceptually before using tenant-dependent features.
8. Close with Gov validation and model-review checklist.

## Feature availability

| Feature | Status | Instructor note |
|---|---|---|
| Star schema | Gov-ready | Required for all deliveries. |
| Role-playing dimensions | Gov-ready | Use duplicated date tables for the safest learner path. |
| Bridge tables | Gov-ready | Required for all deliveries. |
| Composite models | Verify for Gov | Provide conceptual walkthrough if source or tenant support is unavailable. |
| Hybrid tables | Verify for Gov | Mention conceptually; do not require unless tenant is validated. |
| Large semantic models | Verify for Gov | Position as architecture/admin topic, not required hands-on step. |

## Environment setup

- Power BI Desktop installed.
- Access to the lab CSV files under `Student\Labs\Source\01-advanced-semantic-modeling\data`.
- Optional: SQL source or other DirectQuery-capable source for composite model demonstration.

## Lab facilitation notes

- Keep the core lab path Import-mode and file-based so it works for commercial and Azure Government learners.
- Position the Power Query date function as the preferred reusable enterprise pattern because it supports parameters, fiscal periods, and optional holidays before load.
- Position the DAX `CALENDAR` table as a fast report-local pattern for prototypes or smaller reports.
- Treat period boundary dates, refresh-relative offsets, current-period flags, and ISO week attributes as optional extensions because they depend on business calendar rules and refresh behavior.
- Use the relationship setup table and crow's-foot visual when learners create relationships in Model view; it makes PK/FK roles, cardinality, and filter direction explicit.
- Teach `DimProductCategory` as a small lookup dimension between product-level `DimProduct` and category-level `FactTargets`; this prevents Power BI from creating a many-to-many relationship on `ProductCategory`.
- Treat composite models, hybrid tables, and large semantic models as validation-dependent.
- Point learners to Module 2 for calculation groups and Module 4 for field parameters.
- Reinforce that bi-directional filters are not a shortcut for unclear model design.

## Common issues and fixes

| Issue | Likely cause | Fix |
|---|---|---|
| Measures return duplicated totals | Many-to-many relationship or non-unique dimension key | Check dimension uniqueness and bridge-table design. |
| Product category target relationship becomes many-to-many | `DimProduct[ProductCategory]` repeats for multiple products | Create `DimProductCategory` as a distinct product-category lookup and relate it to both `DimProduct` and `FactTargets`. |
| Date slicer affects the wrong metric | Active relationship is tied to the wrong date role | Use role-playing date table or `USERELATIONSHIP` pattern. |
| Date table lacks fiscal or holiday attributes | Only a minimal calendar table was created | Use the Lab 1 `fn_DimDate` Power Query pattern and set the fiscal-year start month. |
| DirectQuery model performs poorly | Source latency, unsupported folding, or too many visual queries | Reduce visuals, aggregate, or use Import/Dual where appropriate. |

## Discussion prompts

- What business questions require transaction-level detail, and what can be aggregated?
- Which dimensions should be conformed across multiple fact tables?
- Where would bi-directional filtering create ambiguity?
- What features must be validated before delivering this module in Azure Government?

## Gov delivery notes

The required lab path uses Power BI Desktop and local CSV files. This keeps the core module Gov-ready. Mark optional composite model, hybrid table, and large-model topics as **Verify for Gov** unless validated in the customer environment.

## Commercial-enhanced options

- Demonstrate DirectQuery against a cloud data warehouse.
- Demonstrate composite models with Dual-mode dimensions.
- Publish to a Premium/Fabric workspace and discuss large semantic model settings.


