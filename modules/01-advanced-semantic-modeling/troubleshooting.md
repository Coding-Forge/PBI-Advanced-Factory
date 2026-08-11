# Troubleshooting Notes

## Import and data preparation

| Symptom | Likely cause | Resolution |
|---|---|---|
| CSV files do not load | File path changed or Power BI cached a previous path | Use **Transform data > Data source settings** and update the source path to `labs\01-advanced-semantic-modeling\data`. |
| Date columns load as text | Locale or type detection issue | Set `OrderDate`, `ShipDate`, `InvoiceDate`, and `TargetMonth` to Date in Power Query. |
| Numeric columns load as text | Locale or delimiter issue | Confirm comma delimiter and set quantity, price, cost, sales, margin, and target columns to Whole Number or Decimal Number. |

## Star schema refactor

| Symptom | Likely cause | Resolution |
|---|---|---|
| Relationship cannot be created as one-to-many | Dimension table contains duplicate keys | Remove duplicates in the dimension query and confirm one row per business key. |
| Sales totals are duplicated | Dimension grain is not unique or bridge table is filtering incorrectly | Validate row counts and relationship direction before adding visuals. |
| Dimension slicer does not filter sales | Relationship is inactive or points to the wrong key | Confirm the relationship connects the dimension key to the fact foreign key. |

## Role-playing dates

| Symptom | Likely cause | Resolution |
|---|---|---|
| Date slicer filters both order and ship date unexpectedly | A single date table is being reused with ambiguous relationships | Use separate role-playing date tables for the Gov-ready beginner path. |
| Ship date analysis returns blank | Relationship is missing or date values do not match | Confirm `DimShipDate[Date]` relates to `FactSales[ShipDate]` and both columns are Date type. |
| Measures do not align by month | Date table lacks a proper month column | Add Year, Month Number, Month Name, and Year-Month columns. |

## Bridge table pattern

| Symptom | Likely cause | Resolution |
|---|---|---|
| Segment totals exceed grand total | Customers belong to multiple segments | Explain that segment totals are not additive when customers can appear in multiple segments. |
| Segment slicer does not filter sales | Relationship path is incomplete | Confirm `DimSegment -> BridgeCustomerSegment -> DimCustomer -> FactSales` path. |
| Many-to-many warning appears | Direct relationship is being attempted between customer and segment dimensions | Use the bridge table instead of directly relating dimensions. |

## Composite models and DirectQuery

> **Azure Government note:** Composite model and DirectQuery labs are **Verify for Gov**. Validate connector support, gateway, network, tenant settings, and source performance before delivery.

| Symptom | Likely cause | Resolution |
|---|---|---|
| DirectQuery option is unavailable | Connector or source does not support DirectQuery | Use Import mode or choose a supported source. |
| Visuals are slow | Source latency or too many visual queries | Reduce visuals, use aggregations, or change appropriate tables to Import/Dual. |
| Model features are unavailable | DirectQuery/composite model limitation | Review feature limitations before choosing storage mode. |

## Calculation groups

> **Azure Government note:** Calculation groups are **Verify for Gov** because they often require external tools, XMLA connectivity, and compatible tenant/capacity settings.

| Symptom | Likely cause | Resolution |
|---|---|---|
| Cannot connect Tabular Editor to model | External tools blocked or unsupported configuration | Use conceptual path or validate workstation policy. |
| XMLA endpoint unavailable | Capacity or tenant setting limitation | Validate workspace capacity and admin settings. |
| Calculation item returns unexpected result | Base measure or calculation expression has incorrect context | Test against one base measure before applying broadly. |

## Field parameters

| Symptom | Likely cause | Resolution |
|---|---|---|
| Parameter does not appear in slicer | Parameter table was not added to the model or visual | Add the generated field parameter column to a slicer. |
| Service behavior differs from Desktop | Feature parity or tenant setting issue | Validate in the target tenant before delivery. |
| Users can choose confusing combinations | Parameter includes too many unrelated fields | Keep parameters focused on a small set of related measures or dimensions. |

