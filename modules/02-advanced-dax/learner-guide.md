# Learner Guide

## What you will learn

You will learn how DAX evaluates measures and how to build reusable patterns for time intelligence, semi-additive metrics, ranking, Top N analysis, dynamic titles, and performance-aware calculations.

## Scenario

Contoso Advanced Manufacturing has a reusable semantic model, but report authors are creating inconsistent sales, margin, target, and ranking calculations. You will create a clean measure layer and validate results across multiple report contexts.

## Prerequisites

- Power BI Desktop
- Completed Module 1 model or equivalent model using the Module 1 CSV files
- Basic DAX measure experience

## Azure Government readiness

The core labs are **Gov-ready** because they use Power BI Desktop and core DAX. Optional diagnostics with DAX Studio or other external tools are **Verify for Gov** because customer workstation policy, tenant connectivity, and XMLA settings may differ.

## Recommended base measures

Create these first and branch from them:

```DAX
Sales Amount = SUM ( FactSales[SalesAmount] )

Quantity = SUM ( FactSales[Quantity] )

Gross Margin = SUM ( FactSales[GrossMargin] )

Gross Margin % = DIVIDE ( [Gross Margin], [Sales Amount] )

Target Sales Amount = SUM ( FactTargets[TargetSalesAmount] )

Sales Variance = [Sales Amount] - [Target Sales Amount]

Sales Variance % = DIVIDE ( [Sales Variance], [Target Sales Amount] )
```

## Tasks

1. Build base measures.
2. Diagnose context behavior in visuals.
3. Create measures using `CALCULATE`.
4. Build advanced time-intelligence measures.
5. Create semi-additive measures.
6. Build rank and Top N logic.
7. Add dynamic titles and measure switching.
8. Optimize and validate the measure layer.

## Validate your work

Your completed module work should include:

- A clean base measure layer.
- At least three time-intelligence measures.
- A semi-additive pattern.
- A rank measure.
- A Top N visual pattern.
- A dynamic title.
- Notes about any optional external-tool diagnostics.

