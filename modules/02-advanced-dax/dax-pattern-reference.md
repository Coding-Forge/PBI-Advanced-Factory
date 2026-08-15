# DAX Pattern Reference

Use these patterns as teaching examples. Adapt table and column names to the model created in Module 1.

## Base measures

```DAX
Sales Amount = SUM ( FactSales[SalesAmount] )

Quantity = SUM ( FactSales[Quantity] )

Gross Margin = SUM ( FactSales[GrossMargin] )

Gross Margin % = DIVIDE ( [Gross Margin], [Sales Amount] )
```

## Target and variance

```DAX
Target Sales Amount = SUM ( FactTargets[TargetSalesAmount] )

Sales Variance = [Sales Amount] - [Target Sales Amount]

Sales Variance % = DIVIDE ( [Sales Variance], [Target Sales Amount] )
```

## Filter removal

```DAX
Sales All Products =
CALCULATE (
    [Sales Amount],
    REMOVEFILTERS ( DimProduct )
)

Product Sales Share =
DIVIDE ( [Sales Amount], [Sales All Products] )
```

## Keep filters

```DAX
Enterprise Customer Sales =
CALCULATE (
    [Sales Amount],
    KEEPFILTERS ( DimCustomer[CustomerType] = "Enterprise" )
)
```

## TREATAS

```DAX
Selected Segment Sales =
CALCULATE (
    [Sales Amount],
    TREATAS (
        VALUES ( DimSegment[Segment] ),
        BridgeCustomerSegment[Segment]
    )
)
```

## Year-to-date

```DAX
Sales YTD =
TOTALYTD (
    [Sales Amount],
    DimOrderDate[Date]
)
```

## Prior year

```DAX
Sales Prior Year =
CALCULATE (
    [Sales Amount],
    SAMEPERIODLASTYEAR ( DimOrderDate[Date] )
)
```

## Year-over-year change

```DAX
Sales YoY =
[Sales Amount] - [Sales Prior Year]

Sales YoY % =
DIVIDE ( [Sales YoY], [Sales Prior Year] )
```

## Rolling 90-day sales

```DAX
Sales Rolling 90 Days =
VAR LastVisibleDate = MAX ( DimOrderDate[Date] )
RETURN
    CALCULATE (
        [Sales Amount],
        DATESINPERIOD ( DimOrderDate[Date], LastVisibleDate, -90, DAY )
    )
```

## Semi-additive last value

```DAX
Ending Backlog Amount =
VAR LastVisibleDate =
    MAX ( DimOrderDate[Date] )
RETURN
    CALCULATE (
        [Backlog Amount],
        DimOrderDate[Date] = LastVisibleDate
    )
```

If the model does not include a backlog or inventory table, teach this as a pattern rather than a required measure.

## Ranking

```DAX
Customer Sales Rank =
RANKX (
    ALLSELECTED ( DimCustomer[CustomerName] ),
    [Sales Amount],
    ,
    DESC,
    DENSE
)
```

## Top N flag

```DAX
Is Top 5 Customer =
IF ( [Customer Sales Rank] <= 5, 1, 0 )
```

## Dynamic title

```DAX
Sales Title =
VAR SelectedRegion =
    SELECTEDVALUE ( DimTerritory[TerritoryRegion], "All Regions" )
RETURN
    "Sales Performance - " & SelectedRegion
```

## Measure switch with disconnected table

```DAX
Selected Metric Value =
VAR MetricName =
    SELECTEDVALUE ( MetricSelector[Metric], "Sales Amount" )
RETURN
    SWITCH (
        MetricName,
        "Sales Amount", [Sales Amount],
        "Gross Margin", [Gross Margin],
        "Gross Margin %", [Gross Margin %],
        "Quantity", [Quantity],
        [Sales Amount]
    )
```

## Optimization guidance

- Use variables to avoid repeated expressions.
- Branch from base measures instead of duplicating logic.
- Test measures in simple table visuals before adding complex visuals.
- Prefer `REMOVEFILTERS` over `ALL` when the intent is filter removal.
- Avoid broad filter removal when only one table or column needs to be changed.
- Use DAX Studio only after validating customer policy and environment support.

