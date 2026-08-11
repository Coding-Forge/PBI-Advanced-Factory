# Slide Outline

## 1. Why Power Query architecture matters

- Transformation logic is part of the solution.
- One long query is hard to test and maintain.
- Staging makes intent visible.

## 2. Staging query pattern

- Raw source queries
- Staging queries
- Final model queries
- Load-enabled vs. load-disabled queries

## 3. Folder-combine pattern

- File filters
- Sample file transformation
- Schema consistency
- Hidden/temp file handling
- Future monthly files

## 4. M language fundamentals

- Applied steps
- Step references
- Lists, records, and tables
- Generated M vs. handwritten M

## 5. Parameters

- Source path parameters
- Environment switching
- RangeStart and RangeEnd
- Parameter governance

## 6. Custom functions

- Function inputs
- Reusable cleanup logic
- Invoking functions
- Testing functions

## 7. Query folding

- What folds
- Why folding matters
- View Native Query
- Folding blockers
- Connector dependency

## 8. Native queries and source systems

- When native queries help
- When native queries hurt maintainability
- Security and gateway considerations

## 9. Data quality and errors

- Explicit types
- Replacing errors
- Keeping error rows for review
- Business-rule checks

## 10. Incremental refresh preparation

- DateTime requirements
- RangeStart and RangeEnd
- Filtering fact data
- Service policy validation

## 11. Azure Government considerations

- Core Desktop transformations are Gov-ready.
- Connectors and dataflows require validation.
- Dataflows Gen2 is commercial-focused unless confirmed.

## 12. Lab review

- Staged solution
- Folder combine
- Parameters and functions
- Validation checklist

