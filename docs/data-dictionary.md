# Datasets and Data Dictionary

This workshop uses synthetic data only. Do not add customer data, tenant identifiers, secrets, subscription IDs, or real user principal names.

## Canonical raw data location

Labs should load CSV data through the Power BI **Web** connector from the repository raw data location:

```text
https://raw.githubusercontent.com/Coding-Forge/PBI-Advanced-Factory/main/data/
```

The lab-local `Student\Labs\Source\...\data` files are retained as authoring/reference copies. The canonical learner-facing source for Power BI imports is the `data\` folder.

## Lab 01: Advanced Semantic Modeling

### `data\sales-flat.csv`

Raw URL:

```text
https://raw.githubusercontent.com/Coding-Forge/PBI-Advanced-Factory/main/data/sales-flat.csv
```

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

### `data\customer-segments.csv`

Raw URL:

```text
https://raw.githubusercontent.com/Coding-Forge/PBI-Advanced-Factory/main/data/customer-segments.csv
```

| Column | Description |
|---|---|
| CustomerKey | Synthetic customer key. |
| Segment | Multi-valued customer segment used for bridge-table modeling. |

### `data\targets.csv`

Raw URL:

```text
https://raw.githubusercontent.com/Coding-Forge/PBI-Advanced-Factory/main/data/targets.csv
```

| Column | Description |
|---|---|
| TargetMonth | Target month. |
| TerritoryKey | Territory key. |
| ProductCategory | Product category. |
| TargetSalesAmount | Monthly target amount. |

## Authoring standards example datasets

### `data\sales-fact.csv`

Raw URL:

```text
https://raw.githubusercontent.com/Coding-Forge/PBI-Advanced-Factory/main/data/sales-fact.csv
```

| Column | Description |
|---|---|
| SalesOrderLineKey | Synthetic transaction line identifier. |
| OrderDate | Order date. |
| ShipDate | Ship date. |
| InvoiceDate | Invoice date. |
| CustomerKey | Customer foreign key. |
| ProductKey | Product foreign key. |
| TerritoryKey | Territory foreign key. |
| Quantity | Units sold. |
| UnitPrice | Unit sales price. |
| UnitCost | Unit cost. |
| SalesAmount | Extended sales amount. |
| GrossMargin | Sales amount less cost. |

### `data\customer-dimension.csv`

Raw URL:

```text
https://raw.githubusercontent.com/Coding-Forge/PBI-Advanced-Factory/main/data/customer-dimension.csv
```

| Column | Description |
|---|---|
| CustomerKey | Synthetic customer key. |
| CustomerName | Synthetic customer name. |
| CustomerType | Customer type. |
| CustomerState | Customer state. |
| CustomerRegion | Customer region. |

### `data\product-dimension.csv`

Raw URL:

```text
https://raw.githubusercontent.com/Coding-Forge/PBI-Advanced-Factory/main/data/product-dimension.csv
```

| Column | Description |
|---|---|
| ProductKey | Synthetic product key. |
| ProductName | Product name. |
| ProductCategory | Product category. |
| ProductSubcategory | Product subcategory. |

### `data\security-user-map.csv`

Raw URL:

```text
https://raw.githubusercontent.com/Coding-Forge/PBI-Advanced-Factory/main/data/security-user-map.csv
```

| Column | Description |
|---|---|
| UserPrincipalName | Synthetic UPN for dynamic RLS examples. |
| DisplayName | Synthetic display name. |
| TerritoryKey | Territory key granted to user. |
| TerritoryName | Territory name granted to user. |
| AccessLevel | Synthetic access level. |

## Lab 03: Advanced Power Query

### `data\monthly-orders\orders-YYYY-MM.csv`

Raw URLs:

```text
https://raw.githubusercontent.com/Coding-Forge/PBI-Advanced-Factory/main/data/monthly-orders/orders-2026-01.csv
https://raw.githubusercontent.com/Coding-Forge/PBI-Advanced-Factory/main/data/monthly-orders/orders-2026-02.csv
https://raw.githubusercontent.com/Coding-Forge/PBI-Advanced-Factory/main/data/monthly-orders/orders-2026-03.csv
```

| Column | Description |
|---|---|
| OrderId | Synthetic order identifier. |
| OrderDate | Order date; includes intentional quality issues in March file. |
| CustomerName | Customer name with intentional whitespace variations. |
| ProductCode | Product code. |
| Quantity | Quantity; includes intentional quality issue in March file. |
| UnitPrice | Unit price. |
| SalesChannel | Sales channel. |

### `data\reference\product-category-map.csv`

Raw URL:

```text
https://raw.githubusercontent.com/Coding-Forge/PBI-Advanced-Factory/main/data/reference/product-category-map.csv
```

| Column | Description |
|---|---|
| ProductCode | Product code. |
| ProductName | Product name. |
| ProductCategory | Product category. |
| ProductSubcategory | Product subcategory. |

## Lab 07: Security Design

## Lab 07: Security Design

### `data\security\security-user-territory.csv`

Raw URL:

```text
https://raw.githubusercontent.com/Coding-Forge/PBI-Advanced-Factory/main/data/security/security-user-territory.csv
```

| Column | Description |
|---|---|
| UserPrincipalName | Synthetic UPN for dynamic RLS. |
| DisplayName | Synthetic display name. |
| TerritoryKey | Territory key granted to user. |
| TerritoryName | Territory name granted to user. |
| AccessLevel | Synthetic access level. |

### `data\security\security-role-matrix.csv`

Raw URL:

```text
https://raw.githubusercontent.com/Coding-Forge/PBI-Advanced-Factory/main/data/security/security-role-matrix.csv
```

| Column | Description |
|---|---|
| Persona | User persona. |
| PowerBIRole | Intended Power BI role. |
| ExpectedAccess | Expected data/content access. |
| BuildPermission | Whether Build permission is intended. |
| ExternalSharingAllowed | Whether external sharing is allowed or requires validation. |
| Notes | Governance notes. |


