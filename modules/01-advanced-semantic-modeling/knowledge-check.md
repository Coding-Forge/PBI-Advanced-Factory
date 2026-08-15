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
9. Which Module 1 features should be validated before use in an Azure Government tenant?
10. When should you use the Power Query date function instead of the simple DAX `CALENDAR` date table?
11. Why should month, year-month, and fiscal-period labels have numeric sort columns?
12. Why does the lab use `DimProductCategory` between `DimProduct` and `FactTargets`?

## Answer key

1. A star schema reduces duplication, improves model readability, simplifies DAX, and usually improves performance.
2. Grain is the level of detail represented by each fact row. It must be clear so measures aggregate correctly and relationships behave predictably.
3. Avoid bi-directional relationships when they create ambiguous filter paths, hide poor model design, or cause unexpected measure results.
4. Use duplicated role-playing date tables, or use one active relationship plus inactive relationships activated in measures with `USERELATIONSHIP`.
5. A bridge table supports analysis where one entity can belong to multiple categories, such as customers with multiple segments.
6. Many-to-many relationships can duplicate filter paths or apply filters at the wrong grain, which can inflate or suppress totals.
7. Import stores data in the model; DirectQuery sends queries to the source at interaction time.
8. Dual mode can let shared dimensions behave as Import for performance while still participating in DirectQuery queries when needed.
9. Composite models, DirectQuery source behavior, hybrid tables, large semantic models, and Service behavior for newer modeling features should be validated.
10. Use the Power Query function when the date table should be reusable across reports, parameterized by start/end date, aligned to a configurable fiscal year, or enriched with optional holidays before load. Use the DAX `CALENDAR` table for quick report-local scenarios.
11. Text labels sort alphabetically by default. Numeric sort columns keep labels such as month names, year-month labels, and fiscal periods in chronological order.
12. `DimProduct` is at product grain, so `ProductCategory` can repeat across multiple product rows. `FactTargets` is at product-category grain. A distinct `DimProductCategory` lookup creates one-to-many relationships to both tables and avoids a many-to-many relationship on `ProductCategory`.

