# Module 5: Performance Optimization

## Module summary

This module teaches practical performance diagnostics and optimization techniques across the semantic model, Power Query, DAX, visuals, refresh, and capacity layers. The module emphasizes a repeatable investigation process before applying fixes.

## Learning objectives

By the end of this module, learners will be able to:

- Use Performance Analyzer to identify slow visuals and expensive DAX queries.
- Explain how model size, column cardinality, relationships, and unused fields affect performance.
- Apply DAX optimization techniques using variables, measure branching, and simpler filter logic.
- Reduce visual-level performance issues.
- Explain when aggregations, incremental refresh, DirectQuery, hybrid tables, and large models are appropriate.
- Identify Azure Government considerations for DAX Studio, VertiPaq Analyzer, capacity metrics, and Service-side refresh.

## Feature availability

| Feature | Status | Delivery note |
|---|---|---|
| Performance Analyzer | Gov-ready | Desktop feature and required core path. |
| Model size and cardinality review | Gov-ready | Core modeling practice. |
| Visual optimization | Gov-ready | Core report authoring practice. |
| DAX optimization | Gov-ready | Core DAX practice. |
| DAX Studio | Verify for Gov | Validate workstation policy, external tools, XMLA, and Service access. |
| VertiPaq Analyzer | Verify for Gov | Often used through external tooling; validate policy and connectivity. |
| Aggregations | Gov-ready / Verify for source | Pattern is supported, but source and DirectQuery behavior require validation. |
| Incremental refresh | Verify for Gov | Depends on license, workspace, Service, gateway, and source support. |
| Capacity metrics | Verify for Gov | App and telemetry availability can vary by cloud and capacity type. |

## Module artifacts

- [Instructor Guide](instructor-guide.md)
- [Learner Guide](learner-guide.md)
- [Slide Outline](slide-outline.md)
- [Performance Benchmark Targets](performance-benchmark-targets.md)
- [Knowledge Check](knowledge-check.md)
- [Module labs](..\..\labs\05-performance-optimization\README.md)

