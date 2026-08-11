# Slide Outline

## 1. Performance optimization mindset

- Measure first.
- Identify the bottleneck.
- Change one thing.
- Measure again.

## 2. Performance layers

- Source system
- Power Query
- Semantic model
- DAX
- Visual rendering
- Service refresh
- Capacity

## 3. Performance Analyzer

- Recording interactions
- Visual display time
- DAX query time
- Other/render time
- Copying queries for deeper analysis

## 4. Model size and cardinality

- Column cardinality
- Data types
- Precision
- Date/time splits
- Unused columns
- Relationship design

## 5. DAX optimization

- Variables
- Measure branching
- Avoiding repeated logic
- Filter scope
- Iterator caution

## 6. Visual optimization

- Visual count
- High-cardinality visuals
- Tables and matrices
- Cross-highlighting
- Custom visuals
- Page complexity

## 7. Power Query and refresh optimization

- Query folding
- Staging
- Filtering early
- Removing columns early
- Incremental refresh preparation

## 8. Aggregations

- Import aggregation tables
- DirectQuery detail tables
- Group-by columns
- Manage aggregations
- Source validation

## 9. DirectQuery and hybrid patterns

- Import vs. DirectQuery
- Dual mode
- Hybrid tables
- Large models
- Tradeoffs

## 10. Service and capacity monitoring

- Refresh history
- Dataset settings
- Capacity metrics
- Admin monitoring
- Gov validation requirements

## 11. External tools

- DAX Studio
- VertiPaq Analyzer
- Tabular Editor
- Customer workstation and tenant policy

## 12. Lab review and benchmark targets

- Before/after observations
- Production readiness
- Documentation expectations

