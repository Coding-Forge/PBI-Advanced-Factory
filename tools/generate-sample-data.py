r"""Regenerate the synthetic workshop CSV files under data\.

Why this exists
----------------
The original hand-authored CSVs (5 customers, 5 products, 4 territories,
15 sales rows, a single quarter of 2026) were too small to demonstrate
several of the features the labs teach:

- Time-intelligence measures (Prior Year, YoY, YoY %, Rolling 90 Days,
  Fiscal YTD) need more than one year of history or they always return
  BLANK.
- Module 5 (Performance Optimization) needs enough rows and cardinality
  for Performance Analyzer / DAX Studio / VertiPaq Analyzer / aggregation
  labs to show a measurable difference.
- Module 6 (AI-assisted analytics) and forecasting-style visuals need
  real seasonality/trend to look meaningful.

This script regenerates the base CSVs with much larger volume and a
3-year date range while keeping every existing key, name, and value
that is referenced literally elsewhere in the repo (report visual
filters and RLS docs pin specific customer names, product names, and
territory names/keys). Those five customers (C001-C005), five products
(P001-P005), and four territories (T01-T04) are preserved byte-for-byte
as "anchor" rows; everything else is additional synthetic volume
generated around them.

Usage
-----
    python tools/generate-sample-data.py

Re-running is deterministic (fixed random seed) so the output is stable
across machines and CI.
"""

from __future__ import annotations

import csv
import datetime as dt
import random
from pathlib import Path

SEED = 42
DATA_DIR = Path(__file__).resolve().parent.parent / "data"

# ---------------------------------------------------------------------------
# Anchor entities that must not change (referenced literally elsewhere)
# ---------------------------------------------------------------------------

ANCHOR_CUSTOMERS = [
    # CustomerKey, CustomerName, CustomerType, CustomerState, CustomerRegion
    ("C001", "Northwind Health", "Enterprise", "VA", "East"),
    ("C002", "Contoso Defense", "Government", "MD", "East"),
    ("C003", "Fabrikam Energy", "Enterprise", "TX", "Central"),
    ("C004", "Wide World Logistics", "Commercial", "WA", "West"),
    ("C005", "Adventure Works Gov", "Government", "CO", "West"),
]

ANCHOR_PRODUCTS = [
    # ProductKey, ProductName, ProductCategory, ProductSubcategory
    ("P001", "Secure Gateway", "Security", "Network"),
    ("P002", "Analytics Workspace", "Analytics", "Platform"),
    ("P003", "Data Gateway", "Integration", "Connectivity"),
    ("P004", "Monitoring Pack", "Operations", "Observability"),
    ("P005", "AI Readiness Kit", "Analytics", "AI"),
]

# TerritoryKey, TerritoryName, TerritoryRegion -- fixed; do not add/remove
# territories because security-user-map.csv / security-user-territory.csv
# and the RLS lab documentation pin these exact keys and names.
TERRITORIES = [
    ("T01", "Mid-Atlantic", "East"),
    ("T02", "South Central", "Central"),
    ("T03", "Pacific Northwest", "West"),
    ("T04", "Mountain", "West"),
]

ANCHOR_SEGMENTS = [
    ("C001", "Healthcare"),
    ("C001", "Regulated"),
    ("C002", "Defense"),
    ("C002", "Azure Government"),
    ("C002", "Regulated"),
    ("C003", "Energy"),
    ("C003", "Enterprise"),
    ("C004", "Logistics"),
    ("C004", "Commercial"),
    ("C005", "Azure Government"),
    ("C005", "Regulated"),
]

SEGMENT_POOL = [
    "Healthcare", "Regulated", "Defense", "Azure Government", "Energy",
    "Enterprise", "Logistics", "Commercial", "Public Sector", "Nonprofit",
    "Manufacturing", "Financial Services", "Retail", "Education",
]

# ---------------------------------------------------------------------------
# Synthetic name/category pools for generated (non-anchor) rows
# ---------------------------------------------------------------------------

CUSTOMER_PREFIXES = [
    "Tailspin", "Fourth Coffee", "Litware", "Proseware", "Relecloud",
    "Trey Research", "Woodgrove", "VanArsdel", "Blue Yonder", "Coho Vineyard",
    "Graphic Design Institute", "Humongous Insurance", "Lucerne Publishing",
    "Margie's Travel", "Nod Publishers", "Consolidated Messenger",
    "City Power", "Alpine Ski House", "Best For You Organics",
    "Contoso", "Fabrikam", "Northwind", "Adventure Works", "Wide World",
    "Cascade", "Summit", "Harbor", "Meridian", "Cobalt", "Redwood",
    "Sterling", "Beacon", "Granite", "Vantage", "Pinnacle", "Anchor",
]
CUSTOMER_SUFFIXES = [
    "Health", "Defense", "Energy", "Logistics", "Gov", "Financial",
    "Retail", "Manufacturing", "Insurance", "Media", "University",
    "Foods", "Airlines", "Telecom", "Utilities", "Partners", "Systems",
    "Solutions", "Holdings", "Group", "Labs", "Dynamics",
]
CUSTOMER_TYPES = ["Enterprise", "Government", "Commercial"]
CUSTOMER_TYPE_WEIGHTS = [0.4, 0.3, 0.3]

REGION_STATES = {
    "East": ["VA", "MD", "NY", "MA", "NC", "GA", "FL", "PA"],
    "Central": ["TX", "IL", "OH", "MO", "MN", "WI", "KS"],
    "West": ["WA", "CO", "CA", "AZ", "OR", "UT", "NV"],
}
REGIONS = list(REGION_STATES.keys())

PRODUCT_CATEGORY_INFO = {
    "Security": {
        "subcategories": ["Network", "Identity", "Threat Detection", "Compliance"],
        "adjectives": ["Secure", "Shielded", "Zero Trust", "Encrypted", "Hardened"],
        "nouns": ["Gateway", "Firewall", "Vault", "Sentinel", "Perimeter", "Guard"],
        "price_range": (700, 1700),
    },
    "Analytics": {
        "subcategories": ["Platform", "AI", "Visualization", "Data Science"],
        "adjectives": ["Analytics", "Insight", "Predictive", "Smart", "Adaptive"],
        "nouns": ["Workspace", "Studio", "Readiness Kit", "Dashboard Suite", "Model Hub"],
        "price_range": (2200, 6200),
    },
    "Integration": {
        "subcategories": ["Connectivity", "Messaging", "API Management", "ETL"],
        "adjectives": ["Data", "Unified", "Streaming", "Connected", "Fabric"],
        "nouns": ["Gateway", "Bridge", "Pipeline", "Connector Pack", "Sync Hub"],
        "price_range": (1100, 2400),
    },
    "Operations": {
        "subcategories": ["Observability", "Automation", "Cost Management", "Reliability"],
        "adjectives": ["Monitoring", "Automated", "Resilient", "Managed", "Proactive"],
        "nouns": ["Pack", "Console", "Toolkit", "Control Center", "Ops Suite"],
        "price_range": (550, 1300),
    },
}
CATEGORIES = list(PRODUCT_CATEGORY_INFO.keys())

CHANNELS = ["Enterprise", "Government", "Commercial"]

TOTAL_CUSTOMERS = 120
TOTAL_PRODUCTS = 40
START_MONTH = dt.date(2024, 1, 1)
END_MONTH = dt.date(2026, 12, 1)
TARGET_SALES_ROWS = 60000
MONTHLY_ORDER_ROWS_PER_FILE = 150
MONTHLY_ORDER_DIRTY_RATE = 0.10


def month_range(start: dt.date, end: dt.date) -> list[dt.date]:
    months = []
    current = start
    while current <= end:
        months.append(current)
        year = current.year + (1 if current.month == 12 else 0)
        month = 1 if current.month == 12 else current.month + 1
        current = dt.date(year, month, 1)
    return months


def build_customers(rng: random.Random) -> list[tuple[str, str, str, str, str]]:
    customers = list(ANCHOR_CUSTOMERS)
    used_names = {c[1] for c in customers}
    next_index = len(customers) + 1
    while len(customers) < TOTAL_CUSTOMERS:
        prefix = rng.choice(CUSTOMER_PREFIXES)
        suffix = rng.choice(CUSTOMER_SUFFIXES)
        name = f"{prefix} {suffix}"
        if name in used_names:
            continue
        used_names.add(name)
        region = rng.choice(REGIONS)
        state = rng.choice(REGION_STATES[region])
        ctype = rng.choices(CUSTOMER_TYPES, weights=CUSTOMER_TYPE_WEIGHTS)[0]
        key = f"C{next_index:03d}"
        customers.append((key, name, ctype, state, region))
        next_index += 1
    return customers


def build_products(rng: random.Random) -> list[tuple[str, str, str, str, int, int]]:
    """Returns ProductKey, ProductName, ProductCategory, ProductSubcategory, UnitPrice, UnitCost."""
    anchor_prices = {
        "P001": (1200, 760),
        "P002": (3400, 2100),
        "P003": (1800, 950),
        "P004": (900, 420),
        "P005": (5200, 3100),
    }
    products = [
        (key, name, cat, sub, *anchor_prices[key])
        for key, name, cat, sub in ANCHOR_PRODUCTS
    ]
    used_names = {p[1] for p in products}
    next_index = len(products) + 1
    cat_cycle = list(CATEGORIES)
    while len(products) < TOTAL_PRODUCTS:
        category = cat_cycle[next_index % len(cat_cycle)]
        info = PRODUCT_CATEGORY_INFO[category]
        subcategory = rng.choice(info["subcategories"])
        name = f"{rng.choice(info['adjectives'])} {rng.choice(info['nouns'])}"
        if name in used_names:
            continue
        used_names.add(name)
        low, high = info["price_range"]
        unit_price = rng.randrange(low, high, 50)
        margin_pct = rng.uniform(0.30, 0.45)
        unit_cost = int(round(unit_price * (1 - margin_pct)))
        key = f"P{next_index:03d}"
        products.append((key, name, category, subcategory, unit_price, unit_cost))
        next_index += 1
    return products


def build_segments(rng: random.Random, customers) -> list[tuple[str, str]]:
    segments = list(ANCHOR_SEGMENTS)
    anchor_keys = {c[0] for c in ANCHOR_CUSTOMERS}
    for key, *_ in customers:
        if key in anchor_keys:
            continue
        picks = rng.sample(SEGMENT_POOL, k=rng.choice([1, 1, 2]))
        for segment in picks:
            segments.append((key, segment))
    return segments


def seasonal_weight(month: dt.date) -> float:
    # Mild seasonality: slower in summer, stronger toward calendar year end.
    seasonal = {
        1: 0.90, 2: 0.90, 3: 0.95, 4: 1.00, 5: 1.00, 6: 0.95,
        7: 0.85, 8: 0.85, 9: 1.00, 10: 1.05, 11: 1.15, 12: 1.25,
    }
    return seasonal[month.month]


def growth_factor(month: dt.date) -> float:
    months_since_start = (month.year - START_MONTH.year) * 12 + (month.month - START_MONTH.month)
    return 1.0 + (months_since_start * 0.015)  # ~1.5%/month compounding growth story


def build_sales(rng: random.Random, customers, products):
    months = month_range(START_MONTH, END_MONTH)
    weights = [seasonal_weight(m) * growth_factor(m) for m in months]
    total_weight = sum(weights)
    rows_per_month = [max(1, round(TARGET_SALES_ROWS * w / total_weight)) for w in weights]

    customer_keys = [c[0] for c in customers]
    product_lookup = {p[0]: p for p in products}
    product_keys = [p[0] for p in products]
    territory_keys = [t[0] for t in TERRITORIES]

    sales = []
    line_key = 1001
    for month, n_rows in zip(months, rows_per_month):
        days_in_month = (
            (dt.date(month.year + (1 if month.month == 12 else 0),
                      1 if month.month == 12 else month.month + 1, 1)
             - month).days
        )
        for _ in range(n_rows):
            order_date = month + dt.timedelta(days=rng.randrange(days_in_month))
            ship_date = order_date + dt.timedelta(days=rng.randint(1, 5))
            invoice_date = ship_date + dt.timedelta(days=rng.randint(1, 3))
            customer_key = rng.choice(customer_keys)
            product_key = rng.choice(product_keys)
            territory_key = rng.choice(territory_keys)
            _, _, _, _, unit_price, unit_cost = product_lookup[product_key]
            quantity = rng.randint(1, 10)
            sales_amount = quantity * unit_price
            gross_margin = (unit_price - unit_cost) * quantity
            sales.append((
                line_key, order_date, ship_date, invoice_date,
                customer_key, product_key, territory_key,
                quantity, unit_price, unit_cost, sales_amount, gross_margin,
            ))
            line_key += 1
    return sales


def build_targets(rng: random.Random):
    months = month_range(START_MONTH, END_MONTH)
    territory_base = {"T01": 7000, "T02": 6000, "T03": 5000, "T04": 4000}
    rows = []
    for month in months:
        growth = growth_factor(month)
        seasonal = seasonal_weight(month)
        for territory_key, _, _ in TERRITORIES:
            for category in CATEGORIES:
                base = territory_base[territory_key] * (0.8 + 0.4 * CATEGORIES.index(category) / len(CATEGORIES))
                amount = int(round(base * growth * seasonal * rng.uniform(0.9, 1.1) / 100.0) * 100)
                rows.append((month, territory_key, category, amount))
    return rows


def write_csv(path: Path, header: list[str], rows: list[tuple]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for row in rows:
            writer.writerow(row)


def build_monthly_orders(rng: random.Random, customers, products):
    product_codes = [p[0] for p in products]
    customer_names = [c[1] for c in customers]
    files = {}
    months = [(2026, 1, "01"), (2026, 2, "02"), (2026, 3, "03")]
    order_id = 3001
    for year, month, label in months:
        rows = []
        is_march = label == "03"
        n_dirty = int(round(MONTHLY_ORDER_ROWS_PER_FILE * MONTHLY_ORDER_DIRTY_RATE)) if is_march else 0
        for i in range(MONTHLY_ORDER_ROWS_PER_FILE):
            day = rng.randint(1, 28)
            order_date = f"{year:04d}-{month:02d}-{day:02d}"
            customer_name = rng.choice(customer_names)
            product_code = rng.choice(product_codes)
            quantity = rng.randint(1, 10)
            unit_price = rng.choice([700, 900, 1200, 1800, 2200, 3400, 5200])
            channel = rng.choice(CHANNELS)
            # Preserve the original whitespace-quirk pattern on a few rows.
            if rng.random() < 0.05:
                customer_name = f" {customer_name} "
            if is_march and i < n_dirty:
                issue = rng.choice(["bad_date", "bad_quantity", "missing_product", "missing_customer"])
                if issue == "bad_date":
                    order_date = "not-a-date"
                elif issue == "bad_quantity":
                    quantity = "bad-quantity"
                elif issue == "missing_product":
                    product_code = ""
                elif issue == "missing_customer":
                    customer_name = ""
            rows.append((order_id, order_date, customer_name, product_code, quantity, unit_price, channel))
            order_id += 1
        files[label] = rows
        order_id = 3001 + (int(label) * 100)  # keep the original 31xx/32xx numbering bands
    return files


def main() -> None:
    rng = random.Random(SEED)

    customers = build_customers(rng)
    products = build_products(rng)
    segments = build_segments(rng, customers)
    sales = build_sales(rng, customers, products)
    targets = build_targets(rng)
    monthly_orders = build_monthly_orders(rng, customers, products)

    customer_lookup = {c[0]: c for c in customers}
    product_lookup = {p[0]: p for p in products}
    territory_lookup = {t[0]: t for t in TERRITORIES}

    # customer-dimension.csv
    write_csv(
        DATA_DIR / "customer-dimension.csv",
        ["CustomerKey", "CustomerName", "CustomerType", "CustomerState", "CustomerRegion"],
        customers,
    )

    # product-dimension.csv (drop price columns, keep original 4-column schema)
    write_csv(
        DATA_DIR / "product-dimension.csv",
        ["ProductKey", "ProductName", "ProductCategory", "ProductSubcategory"],
        [(k, n, c, s) for k, n, c, s, _, _ in products],
    )

    # reference/product-category-map.csv (must match product-dimension 1:1)
    write_csv(
        DATA_DIR / "reference" / "product-category-map.csv",
        ["ProductCode", "ProductName", "ProductCategory", "ProductSubcategory"],
        [(k, n, c, s) for k, n, c, s, _, _ in products],
    )

    # customer-segments.csv
    write_csv(
        DATA_DIR / "customer-segments.csv",
        ["CustomerKey", "Segment"],
        segments,
    )

    # targets.csv
    write_csv(
        DATA_DIR / "targets.csv",
        ["TargetMonth", "TerritoryKey", "ProductCategory", "TargetSalesAmount"],
        [(m.isoformat(), t, c, amt) for m, t, c, amt in targets],
    )

    # sales-fact.csv
    write_csv(
        DATA_DIR / "sales-fact.csv",
        ["SalesOrderLineKey", "OrderDate", "ShipDate", "InvoiceDate", "CustomerKey",
         "ProductKey", "TerritoryKey", "Quantity", "UnitPrice", "UnitCost",
         "SalesAmount", "GrossMargin"],
        [
            (lk, od.isoformat(), sd.isoformat(), idt.isoformat(), ck, pk, tk, qty, up, uc, sa, gm)
            for lk, od, sd, idt, ck, pk, tk, qty, up, uc, sa, gm in sales
        ],
    )

    # sales-flat.csv (denormalized)
    flat_rows = []
    for lk, od, sd, idt, ck, pk, tk, qty, up, uc, sa, gm in sales:
        _, cname, ctype, cstate, cregion = customer_lookup[ck]
        _, pname, pcat, psub, _, _ = product_lookup[pk]
        _, tname, tregion = territory_lookup[tk]
        flat_rows.append((
            lk, od.isoformat(), sd.isoformat(), idt.isoformat(),
            ck, cname, ctype, cstate, cregion,
            pk, pname, pcat, psub,
            tk, tname, tregion,
            qty, up, uc, sa, gm,
        ))
    write_csv(
        DATA_DIR / "sales-flat.csv",
        ["SalesOrderLineKey", "OrderDate", "ShipDate", "InvoiceDate",
         "CustomerKey", "CustomerName", "CustomerType", "CustomerState", "CustomerRegion",
         "ProductKey", "ProductName", "ProductCategory", "ProductSubcategory",
         "TerritoryKey", "TerritoryName", "TerritoryRegion",
         "Quantity", "UnitPrice", "UnitCost", "SalesAmount", "GrossMargin"],
        flat_rows,
    )

    # monthly-orders/orders-2026-MM.csv
    for label, rows in monthly_orders.items():
        write_csv(
            DATA_DIR / "monthly-orders" / f"orders-2026-{label}.csv",
            ["OrderId", "OrderDate", "CustomerName", "ProductCode", "Quantity", "UnitPrice", "SalesChannel"],
            rows,
        )

    print(f"Customers: {len(customers)}")
    print(f"Products: {len(products)}")
    print(f"Sales rows: {len(sales)}")
    print(f"Target rows: {len(targets)}")
    print(f"Segment rows: {len(segments)}")
    for label, rows in monthly_orders.items():
        print(f"orders-2026-{label}.csv rows: {len(rows)}")


if __name__ == "__main__":
    main()
