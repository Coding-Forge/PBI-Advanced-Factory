# Instructor Guide

## Module summary

Performance optimization should be evidence-driven. Teach learners to measure first, identify the likely bottleneck, make one change, and measure again.

## Audience and prerequisites

Best fit for report authors, semantic model developers, BI platform owners, Power BI administrators, and support engineers.

Learners should understand report authoring, semantic modeling, Power Query, basic DAX, and Service refresh concepts.

## Learning objectives

- Use Performance Analyzer to measure report interactions.
- Identify model design issues that increase size or slow queries.
- Reduce cardinality and remove unused columns.
- Optimize visuals and page layout.
- Improve DAX readability and performance.
- Explain aggregation and incremental refresh patterns.
- Identify Gov validation requirements for external tools and capacity telemetry.

## Delivery flow

1. Start with a slow report scenario and define symptoms.
2. Use Performance Analyzer to identify visual, DAX, and render time.
3. Review model size, column cardinality, and relationship design.
4. Optimize a slow DAX measure.
5. Reduce visual load and unnecessary interactions.
6. Discuss aggregations and DirectQuery tradeoffs.
7. Prepare incremental refresh policy conceptually or hands-on when available.
8. Review optional DAX Studio, VertiPaq Analyzer, and capacity metrics paths.
9. Close with benchmark targets and production readiness review.

## Feature availability

| Feature | Status | Instructor note |
|---|---|---|
| Performance Analyzer | Gov-ready | Required core lab. |
| Cardinality and model reduction | Gov-ready | Required core lab. |
| Visual optimization | Gov-ready | Required core lab. |
| DAX optimization | Gov-ready | Required core lab. |
| DAX Studio | Verify for Gov | Keep optional. |
| VertiPaq Analyzer | Verify for Gov | Keep optional. |
| Aggregation tables | Gov-ready / Verify for source | Use conceptual path unless DirectQuery source is available. |
| Incremental refresh | Verify for Gov | Prepare in Desktop; Service policy requires validation. |
| Capacity metrics | Verify for Gov | Discuss conceptually unless app/telemetry is available. |

## Environment setup

- Power BI Desktop installed.
- A PBIP report/model based on earlier modules.
- Optional: DAX Studio for query timings.
- Optional: VertiPaq Analyzer access through supported tooling.
- Optional: Power BI Service workspace with compatible license/capacity for incremental refresh and capacity metrics.

## Lab facilitation notes

- Do not let learners optimize blindly.
- Require before/after observations.
- Keep the required path Desktop-first and Gov-ready.
- Use optional tools only after validating policy and availability.
- Reinforce that DirectQuery is not automatically faster than Import.

## Common issues and fixes

| Issue | Likely cause | Fix |
|---|---|---|
| Visuals are slow | Too many visuals, high-cardinality fields, or expensive measures | Reduce visuals, simplify fields, optimize measures. |
| Model is large | Unused columns, high-cardinality text, unnecessary precision | Remove columns, split date/time, reduce precision. |
| DAX query is slow | Repeated expressions or broad filter removal | Use variables, branch measures, reduce filter scope. |
| Refresh is slow | Non-folding Power Query steps or large full refresh | Improve folding and evaluate incremental refresh. |
| Capacity metrics unavailable | Tenant, cloud, role, or capacity limitation | Mark **Verify for Gov** and use conceptual path. |

## Gov delivery notes

The required labs use Desktop-native capabilities and are Gov-ready. DAX Studio, VertiPaq Analyzer, incremental refresh in the Service, and capacity metrics must be marked **Verify for Gov**.

## Commercial-enhanced options

- Use DAX Studio against a published semantic model through XMLA.
- Use VertiPaq Analyzer to inspect model memory.
- Configure incremental refresh in a supported workspace.
- Review capacity metrics app telemetry.

