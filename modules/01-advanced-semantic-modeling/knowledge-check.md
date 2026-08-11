# Knowledge Check

## Questions

1. Why is a star schema usually preferred over a single flat table in Power BI?
2. What is the grain of a fact table, and why must it be clear?
3. When should you avoid bi-directional relationships?
4. What are two ways to model order date and ship date against the same date dimension?
5. What problem does a bridge table solve?
6. Why can many-to-many relationships create unexpected totals?
7. What is the difference between Import and DirectQuery storage?
8. When might Dual storage mode help a composite model?
9. What problem do calculation groups solve?
10. Why should calculation groups be marked **Verify for Gov**?
11. What problem do field parameters solve?
12. Which Module 1 features should be validated before use in an Azure Government tenant?

## Answer key

1. A star schema reduces duplication, improves model readability, simplifies DAX, and usually improves performance.
2. Grain is the level of detail represented by each fact row. It must be clear so measures aggregate correctly and relationships behave predictably.
3. Avoid bi-directional relationships when they create ambiguous filter paths, hide poor model design, or cause unexpected measure results.
4. Use duplicated role-playing date tables, or use one active relationship plus inactive relationships activated in measures with `USERELATIONSHIP`.
5. A bridge table supports analysis where one entity can belong to multiple categories, such as customers with multiple segments.
6. Many-to-many relationships can duplicate filter paths or apply filters at the wrong grain, which can inflate or suppress totals.
7. Import stores data in the model; DirectQuery sends queries to the source at interaction time.
8. Dual mode can let shared dimensions behave as Import for performance while still participating in DirectQuery queries when needed.
9. Calculation groups centralize repeated calculation logic, such as current period, prior period, and year-over-year calculations.
10. Calculation groups often require external tools, XMLA workflows, or Service capabilities that must be validated in the target tenant.
11. Field parameters let report users switch measures or dimensions through a controlled parameter table and slicer.
12. Composite models, DirectQuery source behavior, calculation groups, hybrid tables, large semantic models, external tooling, and Service behavior for newer features should be validated.

