# Module 1: Advanced Semantic Modeling

## Module summary

This module teaches learners how to design semantic models that are scalable, reusable, secure, and performant. The module starts with dimensional modeling fundamentals and then moves into modeling features such as role-playing dimensions, bridge tables, date dimensions, and composite model design choices.

## Learning objectives

By the end of this module, learners will be able to:

- Explain why star schema design is preferred for enterprise Power BI models.
- Separate fact, dimension, bridge, and helper tables.
- Configure relationship cardinality and filter direction intentionally.
- Model role-playing dimensions such as order date, ship date, and invoice date.
- Use bridge tables to solve many-to-many analysis requirements.
- Describe when composite models, DirectQuery, Dual mode, and hybrid tables are appropriate.
- Identify Azure Government considerations for advanced modeling features.

## Feature availability

| Feature | Status | Delivery note |
|---|---|---|
| Star schema modeling | Gov-ready | Core Desktop modeling pattern. |
| Relationships and cardinality | Gov-ready | Core Desktop modeling feature. |
| Role-playing dimensions | Gov-ready | Can be implemented with duplicated date dimensions or inactive relationships plus DAX. |
| Bridge tables | Gov-ready | Core modeling pattern. |
| Composite models | Verify for Gov | Validate source, gateway, Service, and tenant requirements. |
| DirectQuery and Dual mode | Verify for Gov | Depends on connector, gateway, network, and source system support. |
| Hybrid tables | Verify for Gov | Validate licensing, capacity, incremental refresh, and cloud support. |
| Large semantic models | Verify for Gov | Requires compatible capacity and tenant settings. |

## Module artifacts

- [Instructor Guide](instructor-guide.md)
- [Learner Guide](learner-guide.md)
- [Slide Outline](slide-outline.md)
- [Teaching Deck](assets\advanced-semantic-modeling.pptx)
- [Knowledge Check](knowledge-check.md)
- [Troubleshooting Notes](troubleshooting.md)
- [Module labs](..\..\Student\Labs\Source\01-advanced-semantic-modeling\README.md)



