# Learner Guide

## What you will learn

You will learn how to structure Power Query transformations so they are reusable, reviewable, and easier to support. You will combine multiple source files, create parameters and custom functions, add data quality checks, and prepare a table for incremental refresh.

## Scenario

Contoso Advanced Manufacturing receives monthly order extracts from multiple operational systems. The files are similar but not perfect: some values are missing, some text needs cleanup, and the model needs a repeatable pattern that can support future files.

## Prerequisites

- Power BI Desktop
- Basic Power Query experience
- Access to `labs\03-advanced-power-query\data`

## Azure Government readiness

The required labs are **Gov-ready** because they use local files and Power BI Desktop. Query folding against external sources, Service-side incremental refresh, dataflows, Dataflows Gen2, and some connectors are **Verify for Gov** or **Commercial-focused**.

## Power BI project format

If you create a Power BI artifact while completing this module, save it as a PBIP project. PBIP is the source-controlled format for this workshop. PBIX can be generated from PBIP later if a packaged file is needed.

## Lab files

| File or folder | Purpose |
|---|---|
| `https://raw.githubusercontent.com/Coding-Forge/PBI-Advanced-Factory/main/data/monthly-orders/orders-2026-01.csv` | Monthly source file for append/combine. |
| `https://raw.githubusercontent.com/Coding-Forge/PBI-Advanced-Factory/main/data/monthly-orders/orders-2026-02.csv` | Monthly source file for append/combine. |
| `https://raw.githubusercontent.com/Coding-Forge/PBI-Advanced-Factory/main/data/monthly-orders/orders-2026-03.csv` | Monthly source file for append/combine. |
| `https://raw.githubusercontent.com/Coding-Forge/PBI-Advanced-Factory/main/data/reference/product-category-map.csv` | Reference data for merge and cleanup. |

Use **Get data > Web** in Power BI Desktop to load each CSV from the raw GitHub URL.

## Tasks

1. Build a staged query architecture.
2. Combine monthly files from a folder.
3. Apply explicit data types and cleanup rules.
4. Add data quality checks.
5. Create a custom function for reusable text cleanup.
6. Add parameters for source switching.
7. Review query folding concepts.
8. Prepare RangeStart and RangeEnd parameters for incremental refresh.

## Validate your work

Your completed module work should include:

- Load-disabled staging queries.
- A cleaned fact-style orders query.
- A custom function query.
- Parameterized source path or environment value.
- Explicit error-handling steps.
- Incremental refresh preparation notes.
- Azure Government feature availability notes.

