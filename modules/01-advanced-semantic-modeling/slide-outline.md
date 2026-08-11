# Slide Outline

## 1. Why semantic modeling matters

- Advanced Power BI starts with the model.
- Poor models create slow reports, complex DAX, and inconsistent metrics.
- Enterprise models should be reusable, governed, and understandable.

## 2. From flat files to analytical models

- Reporting exports vs. analytical models
- Repeated text attributes
- Hidden grain problems
- Fact and dimension separation

## 3. Star schema design

- Fact table grain
- Dimension attributes
- Surrogate/business keys
- Conformed dimensions
- Model readability

## 4. Relationship design

- One-to-many relationships
- Cardinality
- Single-direction filtering
- Ambiguity and bi-directional filters
- Many-to-many risks

## 5. Role-playing dimensions

- Order date, ship date, invoice date
- Duplicated dimensions vs. inactive relationships
- `USERELATIONSHIP` pattern overview

## 6. Bridge tables

- Multi-valued attributes
- Customer-to-segment example
- Bridge table grain
- Filter direction considerations

## 7. Composite models and storage modes

- Import
- DirectQuery
- Dual
- Composite models
- Hybrid table concept
- Gov validation requirements

## 8. Calculation groups

- Why repeated time-intelligence measures are hard to maintain
- Calculation item concept
- External tooling and XMLA considerations
- Gov validation requirements

## 9. Field parameters

- Dynamic report exploration
- Controlled flexibility
- When to use field parameters vs. disconnected tables

## 10. Large semantic model considerations

- Cardinality reduction
- Aggregations
- Incremental refresh
- Capacity and tenant settings
- Gov validation requirements

## 11. Module lab walkthrough

- Data overview
- Target model
- Validation checks
- Optional commercial-enhanced path

## 12. Knowledge check and discussion

- Design tradeoffs
- Gov readiness
- Production review checklist

