# Module 1 Labs: Advanced Semantic Modeling

## Lab summary

These labs use synthetic CSV data to build a reusable semantic model for Contoso Advanced Manufacturing.

## Azure Government readiness

The required labs are **Gov-ready** because they use local CSV files and core Power BI Desktop modeling features. The composite model, calculation group, hybrid table, and large semantic model portions are **Verify for Gov** and should be treated as optional unless the target tenant and tooling are validated.

## Lab data

| File | Description |
|---|---|
| `data\sales-flat.csv` | Flat transaction export used for star schema refactoring. |
| `data\customer-segments.csv` | Multi-valued customer segment mapping. |
| `data\targets.csv` | Monthly territory/product category target data. |

## Power BI project format

Build the starter and completed Power BI artifacts as PBIP projects. PBIP is the source-controlled format for this workshop because it makes report and semantic model changes easier to review in git. PBIX files can be generated from PBIP later when a packaged desktop file is needed.

## Lab 1: Star schema refactor

**Objective:** Convert a flat sales export into a dimensional model.

### Tasks

1. Import `sales-flat.csv`.
2. Reference or duplicate the query to create:
   - `FactSales`
   - `DimDate`
   - `DimCustomer`
   - `DimProduct`
   - `DimTerritory`
3. Remove duplicate rows from dimension tables.
4. Keep transaction-level columns in `FactSales`.
5. Create one-to-many relationships from dimensions to `FactSales`.
6. Hide key columns that are not useful for report consumers.

### Expected result

The model has one central fact table and clean dimensions with single-direction filtering into the fact table.

## Lab 2: Role-playing dimensions

**Objective:** Support analysis by order date and ship date.

### Tasks

1. Create `DimOrderDate` from the date values in `OrderDate`.
2. Create `DimShipDate` from the date values in `ShipDate`.
3. Relate `DimOrderDate[Date]` to `FactSales[OrderDate]`.
4. Relate `DimShipDate[Date]` to `FactSales[ShipDate]`.
5. Create measures for sales by order date and sales by ship date.

### Expected result

Learners can slice sales by order date or ship date without ambiguous relationships.

## Lab 3: Bridge table pattern

**Objective:** Model customers that can belong to multiple segments.

### Tasks

1. Import `customer-segments.csv`.
2. Create or identify a distinct `DimSegment` table.
3. Use `customer-segments.csv` as `BridgeCustomerSegment`.
4. Relate `DimCustomer` to `BridgeCustomerSegment`.
5. Relate `DimSegment` to `BridgeCustomerSegment`.
6. Test segment filtering against sales measures.

### Expected result

Customer segments filter sales without duplicating customer rows in the customer dimension.

## Lab 4: Composite model or DirectQuery comparison

> **Azure Government note:** This lab is marked **Verify for Gov**. Confirm connector support, gateway access, tenant settings, network path, and source availability before making this a required hands-on lab.

**Objective:** Compare Import, DirectQuery, Dual, and composite model design choices.

### Conceptual tasks

1. Identify which tables would be good Import candidates.
2. Identify which tables might require DirectQuery.
3. Discuss which dimensions could be Dual mode.
4. Document tradeoffs for performance, freshness, source load, and feature support.

### Expected result

Learners can justify a storage-mode design instead of choosing DirectQuery by default.

## Lab 5: Calculation groups

> **Azure Government note:** This lab is marked **Verify for Gov**. Confirm Tabular Editor, XMLA, capacity, and tenant policy before making this a required hands-on lab.

**Objective:** Reduce repeated time-intelligence measures using a calculation group.

### Tasks when tooling is available

1. Create base measures for sales and gross margin.
2. Use Tabular Editor to add a `Time Intelligence` calculation group.
3. Add calculation items for Current, Prior Year, and Year-over-Year Change.
4. Test calculation items against base measures.

### Conceptual alternate path

If tooling is blocked, review the intended calculation group design and compare it to creating separate DAX measures for every metric/time combination.

### Expected result

Learners understand when calculation groups improve maintainability and why they require tenant/tool validation.

## Lab 6: Field parameters

**Objective:** Let report users switch between business metrics and dimensions.

### Tasks

1. Create base measures for Sales Amount, Gross Margin, Gross Margin %, and Quantity.
2. Create a measure field parameter.
3. Add the field parameter to a slicer.
4. Use the selected parameter in a visual.
5. Optional: create a dimension field parameter for Product Category, Territory, and Customer Segment.

### Expected result

Learners can provide controlled self-service flexibility without creating duplicate report pages.

## Validation checklist

- [ ] The model uses a star schema.
- [ ] Fact and dimension tables have clear names.
- [ ] Relationships are one-to-many where possible.
- [ ] Filter direction is single-direction unless intentionally justified.
- [ ] Role-playing dates work without ambiguity.
- [ ] Bridge table supports multi-segment customer analysis.
- [ ] Optional tenant-dependent features are labeled **Verify for Gov**.
- [ ] Measures produce expected totals by date, product, customer, territory, and segment.

