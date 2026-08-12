# Workshop Data

Use this folder as the stable raw-data location for Power BI Web connector labs.

## Raw URL base

```text
https://raw.githubusercontent.com/Coding-Forge/PBI-Advanced-Factory/main/data/
```

## Data files

| File | Raw URL |
|---|---|
| `sales-flat.csv` | `https://raw.githubusercontent.com/Coding-Forge/PBI-Advanced-Factory/main/data/sales-flat.csv` |
| `customer-segments.csv` | `https://raw.githubusercontent.com/Coding-Forge/PBI-Advanced-Factory/main/data/customer-segments.csv` |
| `targets.csv` | `https://raw.githubusercontent.com/Coding-Forge/PBI-Advanced-Factory/main/data/targets.csv` |
| `sales-fact.csv` | `https://raw.githubusercontent.com/Coding-Forge/PBI-Advanced-Factory/main/data/sales-fact.csv` |
| `customer-dimension.csv` | `https://raw.githubusercontent.com/Coding-Forge/PBI-Advanced-Factory/main/data/customer-dimension.csv` |
| `product-dimension.csv` | `https://raw.githubusercontent.com/Coding-Forge/PBI-Advanced-Factory/main/data/product-dimension.csv` |
| `security-user-map.csv` | `https://raw.githubusercontent.com/Coding-Forge/PBI-Advanced-Factory/main/data/security-user-map.csv` |
| `monthly-orders/orders-2026-01.csv` | `https://raw.githubusercontent.com/Coding-Forge/PBI-Advanced-Factory/main/data/monthly-orders/orders-2026-01.csv` |
| `monthly-orders/orders-2026-02.csv` | `https://raw.githubusercontent.com/Coding-Forge/PBI-Advanced-Factory/main/data/monthly-orders/orders-2026-02.csv` |
| `monthly-orders/orders-2026-03.csv` | `https://raw.githubusercontent.com/Coding-Forge/PBI-Advanced-Factory/main/data/monthly-orders/orders-2026-03.csv` |
| `reference/product-category-map.csv` | `https://raw.githubusercontent.com/Coding-Forge/PBI-Advanced-Factory/main/data/reference/product-category-map.csv` |
| `security/security-user-territory.csv` | `https://raw.githubusercontent.com/Coding-Forge/PBI-Advanced-Factory/main/data/security/security-user-territory.csv` |
| `security/security-role-matrix.csv` | `https://raw.githubusercontent.com/Coding-Forge/PBI-Advanced-Factory/main/data/security/security-role-matrix.csv` |

## Power BI Web connector pattern

In Power BI Desktop:

1. Select **Get data > Web**.
2. Paste the raw URL for the CSV file.
3. Choose the CSV/table result.
4. Transform data as needed.

For folder-combine labs, use the listed monthly order URLs as individual Web sources unless the lab has been adapted to use a GitHub API folder listing.

