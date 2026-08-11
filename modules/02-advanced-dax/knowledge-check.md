# Knowledge Check

## Questions

1. What is filter context?
2. What is row context?
3. What is context transition?
4. Why is `CALCULATE` considered one of the most important DAX functions?
5. When would you use `REMOVEFILTERS`?
6. How is `KEEPFILTERS` different from replacing a filter inside `CALCULATE`?
7. Why should base measures be created before derived measures?
8. What does a date table need to support reliable time intelligence?
9. What is a semi-additive measure?
10. Why might `ALLSELECTED` be better than `ALL` in a ranking measure?
11. What is a disconnected table used for in a measure-switching pattern?
12. Why is DAX Studio marked **Verify for Gov**?

## Answer key

1. Filter context is the set of filters applied to a DAX expression by visuals, slicers, relationships, and explicit DAX filters.
2. Row context is the current row being evaluated, commonly created by calculated columns or iterator functions.
3. Context transition converts row context into filter context, commonly through `CALCULATE`.
4. `CALCULATE` evaluates an expression in a modified filter context and also performs context transition.
5. Use `REMOVEFILTERS` when the intent is to clear filters from a table or column.
6. `KEEPFILTERS` intersects a new filter with existing filters instead of replacing the existing filter.
7. Base measures centralize core logic and make derived measures easier to read, test, and maintain.
8. A reliable date table should be continuous, have one row per date, include useful date attributes, and relate correctly to fact tables.
9. A semi-additive measure can be aggregated across some dimensions but not across time in a simple additive way, such as inventory or balance.
10. `ALLSELECTED` can preserve user selections outside the visual while ranking items inside the selected context.
11. A disconnected table can capture a user selection that drives DAX logic without directly filtering the model.
12. DAX Studio is a local external tool, but customer workstation policy, tenant connectivity, XMLA endpoint settings, and Service access can vary in Azure Government.

