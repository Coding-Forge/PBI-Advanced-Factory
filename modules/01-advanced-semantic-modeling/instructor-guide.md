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
- Explain calculation groups and field parameters.
- Identify Gov-ready, Verify for Gov, and Commercial-focused modeling capabilities.

## Delivery flow

1. Start with the business problem: one report has become slow, hard to maintain, and inconsistent.
2. Show the flat source data and ask learners what will become facts and dimensions.
3. Introduce the target star schema.
4. Build relationships and discuss cardinality/filter direction.
5. Add role-playing date analysis.
6. Introduce bridge tables for multi-valued customer segments.
7. Discuss composite model tradeoffs conceptually before using tenant-dependent features.
8. Demonstrate calculation groups and field parameters where available.
9. Close with Gov validation and model-review checklist.

## Feature availability

| Feature | Status | Instructor note |
|---|---|---|
| Star schema | Gov-ready | Required for all deliveries. |
| Role-playing dimensions | Gov-ready | Use duplicated date tables for the safest learner path. |
| Bridge tables | Gov-ready | Required for all deliveries. |
| Composite models | Verify for Gov | Provide conceptual walkthrough if source or tenant support is unavailable. |
| Calculation groups | Verify for Gov | If Tabular Editor/XMLA is blocked, teach conceptually and show screenshots or completed examples. |
| Field parameters | Gov-ready | Validate Service behavior before delivery. |
| Hybrid tables | Verify for Gov | Mention conceptually; do not require unless tenant is validated. |
| Large semantic models | Verify for Gov | Position as architecture/admin topic, not required hands-on step. |

## Environment setup

- Power BI Desktop installed.
- Access to the lab CSV files under `labs\01-advanced-semantic-modeling\data`.
- Optional: Tabular Editor for calculation group demonstration.
- Optional: SQL source or other DirectQuery-capable source for composite model demonstration.
- Optional: Power BI Service workspace for publishing and validating field parameters.

## Lab facilitation notes

- Keep the core lab path Import-mode and file-based so it works for commercial and Azure Government learners.
- Treat composite models, calculation groups, hybrid tables, and large semantic models as validation-dependent.
- If learners cannot use external tools, explain calculation groups using the provided conceptual steps and expected model behavior.
- Reinforce that bi-directional filters are not a shortcut for unclear model design.

## Common issues and fixes

| Issue | Likely cause | Fix |
|---|---|---|
| Measures return duplicated totals | Many-to-many relationship or non-unique dimension key | Check dimension uniqueness and bridge-table design. |
| Date slicer affects the wrong metric | Active relationship is tied to the wrong date role | Use role-playing date table or `USERELATIONSHIP` pattern. |
| Field parameter does not work in Service | Tenant or Desktop/Service parity issue | Validate feature availability and update Desktop. |
| Calculation group cannot be created | External tool/XMLA blocked | Use conceptual path or local-only demonstration. |
| DirectQuery model performs poorly | Source latency, unsupported folding, or too many visual queries | Reduce visuals, aggregate, or use Import/Dual where appropriate. |

## Discussion prompts

- What business questions require transaction-level detail, and what can be aggregated?
- Which dimensions should be conformed across multiple fact tables?
- Where would bi-directional filtering create ambiguity?
- What features must be validated before delivering this module in Azure Government?

## Gov delivery notes

The required lab path uses Power BI Desktop and local CSV files. This keeps the core module Gov-ready. Mark the optional composite model, calculation group, hybrid table, and large-model topics as **Verify for Gov** unless validated in the customer environment.

## Commercial-enhanced options

- Demonstrate DirectQuery against a cloud data warehouse.
- Demonstrate composite models with Dual-mode dimensions.
- Create calculation groups using Tabular Editor.
- Publish to a Premium/Fabric workspace and discuss large semantic model settings.

