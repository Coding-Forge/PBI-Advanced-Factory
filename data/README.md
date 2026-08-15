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

## Data volume

These CSVs are generated (not hand-authored) so the workshop has enough scale and history
for time-intelligence, performance, and analytics labs to behave realistically, while
staying well under GitHub's file-size limits (no Git LFS required):

| File | Approx. rows | Notes |
|---|---|---|
| `sales-fact.csv` / `sales-flat.csv` | ~60,000 | 3 full years (2024-01-01 to 2026-12-31) with seasonality and month-over-month growth so YoY/Prior Year/Rolling 90 Days measures return real values. |
| `customer-dimension.csv` | 120 | Includes 5 fixed "anchor" customers (`C001`-`C005`) referenced by name in report visuals and labs; the rest are generated. |
| `product-dimension.csv` / `reference\product-category-map.csv` | 40 | Includes 5 fixed anchor products (`P001`-`P005`); the rest are generated across the same 4 categories. |
| `customer-segments.csv` | ~165 | Multi-valued bridge rows across the 120 customers. |
| `targets.csv` | 576 | Every territory x product category x month combination across the 3-year range. |
| `monthly-orders\*.csv` | 150 rows/file | March file keeps a ~10% intentional data-quality issue rate (bad dates, non-numeric quantity, missing product code/customer) for the Module 3 data-quality lab. |

Territories (`T01`-`T04`) are intentionally fixed and never regenerated — the RLS/security
CSVs and Module 7 labs reference these exact keys and names.

### Regenerating this data

Run `tools\generate-sample-data.py` from the repo root (`python tools\generate-sample-data.py`)
to regenerate all of the files above with a fixed random seed (deterministic, reproducible
output). Do not hand-edit `sales-fact.csv`/`sales-flat.csv`/`targets.csv`/`customer-segments.csv`/
`product-dimension.csv`/`reference\product-category-map.csv` directly — update the generator
script instead so the files stay in sync with each other. `customer-dimension.csv`'s anchor rows,
`security\*.csv`, and `security-user-map.csv` are not touched by the script.

## Power BI Web connector pattern

In Power BI Desktop:

1. Select **Get data > Web**.
2. Paste the raw URL for the CSV file.
3. Choose the CSV/table result.
4. Transform data as needed.

For folder-combine labs, use the listed monthly order URLs as individual Web sources unless the lab has been adapted to use a GitHub API folder listing.

