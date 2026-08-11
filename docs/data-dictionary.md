# Datasets and Data Dictionary

This workshop uses synthetic data only. Do not add customer data, tenant identifiers, secrets, subscription IDs, or real user principal names.

## Module 1: Advanced Semantic Modeling

### `labs\01-advanced-semantic-modeling\data\sales-flat.csv`

| Column | Description |
|---|---|
| SalesOrderLineKey | Synthetic transaction line identifier. |
| OrderDate | Order date. |
| ShipDate | Ship date. |
| InvoiceDate | Invoice date. |
| CustomerKey | Synthetic customer key. |
| CustomerName | Synthetic customer name. |
| CustomerType | Customer segment such as Enterprise, Government, or Commercial. |
| CustomerState | Customer state. |
| CustomerRegion | Customer region. |
| ProductKey | Synthetic product key. |
| ProductName | Product name. |
| ProductCategory | Product category. |
| ProductSubcategory | Product subcategory. |
| TerritoryKey | Synthetic territory key. |
| TerritoryName | Territory name. |
| TerritoryRegion | Territory region. |
| Quantity | Units sold. |
| UnitPrice | Unit sales price. |
| UnitCost | Unit cost. |
| SalesAmount | Extended sales amount. |
| GrossMargin | Sales amount less cost. |

### `labs\01-advanced-semantic-modeling\data\customer-segments.csv`

| Column | Description |
|---|---|
| CustomerKey | Synthetic customer key. |
| Segment | Multi-valued customer segment used for bridge-table modeling. |

### `labs\01-advanced-semantic-modeling\data\targets.csv`

| Column | Description |
|---|---|
| TargetMonth | Target month. |
| TerritoryKey | Territory key. |
| ProductCategory | Product category. |
| TargetSalesAmount | Monthly target amount. |

## Module 3: Advanced Power Query

### `labs\03-advanced-power-query\data\monthly-orders\orders-YYYY-MM.csv`

| Column | Description |
|---|---|
| OrderId | Synthetic order identifier. |
| OrderDate | Order date; includes intentional quality issues in March file. |
| CustomerName | Customer name with intentional whitespace variations. |
| ProductCode | Product code. |
| Quantity | Quantity; includes intentional quality issue in March file. |
| UnitPrice | Unit price. |
| SalesChannel | Sales channel. |

### `labs\03-advanced-power-query\data\reference\product-category-map.csv`

| Column | Description |
|---|---|
| ProductCode | Product code. |
| ProductName | Product name. |
| ProductCategory | Product category. |
| ProductSubcategory | Product subcategory. |

## Module 7: Security Design

### `labs\07-security-design\data\security-user-territory.csv`

| Column | Description |
|---|---|
| UserPrincipalName | Synthetic UPN for dynamic RLS. |
| DisplayName | Synthetic display name. |
| TerritoryKey | Territory key granted to user. |
| TerritoryName | Territory name granted to user. |
| AccessLevel | Synthetic access level. |

### `labs\07-security-design\data\security-role-matrix.csv`

| Column | Description |
|---|---|
| Persona | User persona. |
| PowerBIRole | Intended Power BI role. |
| ExpectedAccess | Expected data/content access. |
| BuildPermission | Whether Build permission is intended. |
| ExternalSharingAllowed | Whether external sharing is allowed or requires validation. |
| Notes | Governance notes. |

