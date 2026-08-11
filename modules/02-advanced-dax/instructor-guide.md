# Instructor Guide

## Module summary

Advanced DAX is primarily about understanding evaluation context and writing measures that are correct before they are clever. This module should repeatedly connect DAX behavior back to model design from Module 1.

## Audience and prerequisites

Best fit for report authors, semantic model developers, BI platform owners, and administrators who review model quality.

Learners should understand basic measures, relationships, slicers, filters, and date tables.

## Learning objectives

- Explain row context, filter context, and context transition.
- Use `CALCULATE` safely and intentionally.
- Compare filter-removal and filter-preservation functions.
- Build measures through branching.
- Create time-intelligence, semi-additive, ranking, Top N, and dynamic title patterns.
- Diagnose common DAX mistakes.
- Identify when DAX Studio or external tools require Gov validation.

## Delivery flow

1. Start with a wrong-total example to show why context matters.
2. Explain filter context using visuals and slicers.
3. Explain row context using calculated columns and iterators.
4. Demonstrate context transition with `CALCULATE`.
5. Build base measures and branch into advanced measures.
6. Add time-intelligence calculations.
7. Add Top N and ranking measures.
8. Add dynamic title and measure switching patterns.
9. Show optimization techniques and optional DAX Studio diagnostics.
10. Close with a review checklist for production DAX.

## Feature availability

| Feature | Status | Instructor note |
|---|---|---|
| Core DAX | Gov-ready | Required for all deliveries. |
| Time intelligence | Gov-ready | Requires a marked or well-formed date table. |
| Dynamic measure patterns | Gov-ready | Use disconnected tables if field parameters are unavailable. |
| DAX Studio | Verify for Gov | Use Desktop-connected model diagnostics when Service/XMLA is unavailable. |
| External tools | Verify for Gov | Confirm workstation and tenant policy before delivery. |

## Environment setup

- Power BI Desktop installed.
- Module 1 model or equivalent model built from `labs\01-advanced-semantic-modeling\data`.
- Optional: DAX Studio installed for diagnostics.
- Optional: Tabular Editor for model inspection, not required for core labs.

## Lab facilitation notes

- Keep measures small and composable.
- Require learners to validate totals at multiple grains.
- Avoid introducing too many functions before learners understand context.
- Use variables for readability and performance.
- Treat DAX Studio as optional because many Gov customers restrict external tools or Service connectivity.

## Common issues and fixes

| Issue | Likely cause | Fix |
|---|---|---|
| Total row looks wrong | Measure logic is evaluated at total context, not row-by-row visual context | Use iterator patterns only when the business logic requires row-wise aggregation. |
| Time-intelligence measure returns blank | Date table is incomplete or relationship is wrong | Validate continuous date table and active relationship. |
| Ranking changes unexpectedly | Rank measure does not preserve intended filters | Use `ALLSELECTED` or explicit filter scope depending on expected behavior. |
| Dynamic title shows blank | Selected value is ambiguous | Use `SELECTEDVALUE` with a fallback value. |
| DAX Studio cannot connect | External tools or XMLA access blocked | Use Performance Analyzer and Desktop visuals as alternate diagnostic path. |

## Gov delivery notes

The required DAX labs are Gov-ready because they rely on Power BI Desktop and core DAX language features. Mark DAX Studio and other external tooling as **Verify for Gov**.

## Commercial-enhanced options

- Connect DAX Studio to a published semantic model through XMLA.
- Use Tabular Editor for bulk measure review.
- Demonstrate DAX query view or newer Desktop diagnostics if available in the delivery environment.

