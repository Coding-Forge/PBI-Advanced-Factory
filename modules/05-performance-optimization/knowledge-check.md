# Knowledge Check

## Questions

1. Why should performance optimization start with measurement?
2. What does Performance Analyzer help identify?
3. How can high-cardinality columns affect model performance?
4. Why should unused columns be removed from a semantic model?
5. What is one advantage of using variables in DAX?
6. Why can too many visuals slow a report page?
7. What is the purpose of an aggregation table?
8. Why is DirectQuery not always faster than Import?
9. What is incremental refresh designed to improve?
10. Why are DAX Studio and VertiPaq Analyzer marked **Verify for Gov**?
11. Why are capacity metrics marked **Verify for Gov**?
12. What should be documented after a performance optimization change?

## Answer key

1. Measurement identifies the actual bottleneck and prevents random changes that may not improve performance.
2. Performance Analyzer helps separate visual display time, DAX query time, and other rendering overhead.
3. High-cardinality columns compress poorly and can increase memory usage and query cost.
4. Unused columns increase model size, refresh cost, and user confusion.
5. Variables improve readability and can avoid repeating expensive expressions.
6. Each visual can issue queries and require rendering, so too many visuals increase page load and interaction time.
7. Aggregation tables answer summary-level queries from smaller Import tables while preserving detailed DirectQuery access when needed.
8. DirectQuery depends on source performance, network latency, query folding, and visual query patterns.
9. Incremental refresh reduces refresh effort by processing only the relevant recent partitions instead of the entire fact table.
10. They are external tools, and access may depend on workstation policy, tenant settings, XMLA, and cloud support.
11. Capacity metrics app and telemetry availability can vary by cloud, capacity type, tenant settings, and permissions.
12. Document the baseline, change made, result, tradeoff, and any remaining validation needed.

