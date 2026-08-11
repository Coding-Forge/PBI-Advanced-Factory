# Learner Guide

## What you will learn

In this module, you will build an advanced semantic model from synthetic business data. You will transform a report-oriented dataset into a clean star schema, add relationship patterns for real-world analysis, and evaluate advanced modeling features that may require tenant validation.

## Scenario

Contoso Advanced Manufacturing has a sales analytics report that started as a single flat table. The report is now hard to maintain, DAX is inconsistent, and new requirements require multiple date roles, customer segments, and flexible analysis paths. Your job is to create a reusable semantic model that can support multiple reports.

## Prerequisites

- Power BI Desktop
- Basic understanding of relationships and measures
- Access to the module data files in `labs\01-advanced-semantic-modeling\data`

## Azure Government readiness

The core labs use local CSV files and Power BI Desktop modeling features, so they are designed to be Gov-ready. Optional sections for composite models, calculation groups, hybrid tables, large semantic models, and some Service validation steps are marked **Verify for Gov**.

## Lab files

| File | Purpose |
|---|---|
| `sales-flat.csv` | Denormalized source table for the star schema refactor lab. |
| `customer-segments.csv` | Multi-valued customer segment data for bridge-table lab. |
| `targets.csv` | Sales target fact table for comparing actuals to targets. |

Power BI artifacts for this workshop should be created as PBIP projects. PBIP is the source-controlled format; PBIX can be generated from PBIP later if a packaged file is needed.

## Tasks

1. Import the flat sales dataset.
2. Identify facts, dimensions, and attributes.
3. Create a star schema model.
4. Configure relationships and validate filter direction.
5. Add role-playing date analysis.
6. Add a bridge table for customer segments.
7. Evaluate composite model and DirectQuery design choices.
8. Review calculation groups and field parameters.
9. Validate the model against the expected outcomes.

## Validate your work

Your completed model should include:

- A sales fact table.
- Date, customer, product, and territory dimensions.
- A sales target table.
- A customer segment bridge pattern.
- Measures for sales, quantity, gross margin, gross margin percentage, target, and variance.
- Date analysis for order date and ship date.
- Clear Gov-readiness notes for tenant-dependent features.

## Optional extension

If your tenant and workstation allow it, use Tabular Editor to create a calculation group for time intelligence and create field parameters to switch between key business measures.

