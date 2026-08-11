# Instructor Guide

## Module summary

Advanced Power Query work should be intentional, reviewable, and easy to troubleshoot. This module emphasizes transformation design patterns that scale beyond one-off report cleanup.

## Audience and prerequisites

Best fit for report authors, semantic model developers, data engineers, analytics engineers, and BI platform owners.

Learners should understand basic Power Query steps, data types, merging, appending, and loading tables into a model.

## Learning objectives

- Build a staged query architecture.
- Explain and validate query folding.
- Use parameters for environment switching.
- Create custom functions.
- Combine monthly files from a folder.
- Add error handling and data quality checks.
- Prepare tables for incremental refresh.
- Identify Power Query features that require Azure Government validation.

## Delivery flow

1. Start with a messy operational data extract scenario.
2. Show why one long query is hard to maintain.
3. Introduce staging queries and load-disabled intermediate steps.
4. Demonstrate folder combine with monthly order files.
5. Add explicit data types and quality checks.
6. Create a custom function for reusable cleanup.
7. Discuss query folding and use "View Native Query" where supported.
8. Create parameters for environment/source switching.
9. Prepare RangeStart and RangeEnd parameters for incremental refresh.
10. Close with Gov connector and dataflow validation notes.

## Feature availability

| Feature | Status | Instructor note |
|---|---|---|
| Local CSV/file transformations | Gov-ready | Required core path. |
| Parameters | Gov-ready | Required core path. |
| Custom functions | Gov-ready | Required core path. |
| Query folding | Gov-ready / Verify for source | Use SQL or another folding-capable source if available; otherwise teach conceptually. |
| Incremental refresh | Verify for Gov | Prepare in Desktop; validate Service policy application before delivery. |
| Dataflows | Verify for Gov | Treat as optional Service extension. |
| Dataflows Gen2 | Commercial-focused / Verify for Gov | Treat as conceptual unless confirmed. |
| Connectors | Verify for Gov | Validate in target tenant and network. |

## Environment setup

- Power BI Desktop installed.
- Lab files under `labs\03-advanced-power-query\data`.
- Optional: SQL Server, Azure SQL, or another query-folding-capable source for folding demonstration.
- Optional: Power BI Service workspace for incremental refresh or dataflow demonstrations.

## Lab facilitation notes

- Keep the required path file-based so it works in commercial and Azure Government contexts.
- Do not promise connector availability without validating customer environment.
- Use query names that communicate intent: `stg_`, `dim_`, `fact_`, and `fn_`.
- Disable load for staging queries unless the lab needs them in the model.
- Show applied steps and M code together so learners understand generated code.

## Common issues and fixes

| Issue | Likely cause | Fix |
|---|---|---|
| Folder combine includes unwanted files | Folder contains hidden, temp, or non-CSV files | Filter by extension, file name pattern, and hidden attributes. |
| Data types change unpredictably | Type detection varies by sample file | Apply explicit data types after combine. |
| Query folding stops early | Non-foldable transformation was introduced | Reorder steps or push transformations to the source. |
| Parameter switching fails | Parameter path or source string does not match environment | Validate parameter values and privacy levels. |
| Incremental refresh cannot be configured | RangeStart/RangeEnd missing or not DateTime | Create DateTime parameters and filter the fact table with them. |

## Gov delivery notes

The required labs are Gov-ready because they use local files and Desktop transformations. Query folding, dataflows, Dataflows Gen2, incremental refresh in the Service, and source connectors should be marked **Verify for Gov** or **Commercial-focused** as noted.

## Commercial-enhanced options

- Demonstrate query folding against Azure SQL or Fabric Warehouse.
- Build a Power BI dataflow or Dataflow Gen2.
- Publish a model and configure incremental refresh policy.

