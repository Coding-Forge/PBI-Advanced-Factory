# Module 3 Labs: Advanced Power Query and Data Transformation

## Lab summary

These labs teach reusable Power Query transformation patterns using synthetic monthly order files.

## Azure Government readiness

The required labs are **Gov-ready** because they use local files and Power BI Desktop. Query folding against external sources, dataflows, Dataflows Gen2, incremental refresh in the Service, and source connectors are **Verify for Gov** or **Commercial-focused** depending on the feature.

## Power BI project format

Build Power BI artifacts as PBIP projects. PBIP is the source-controlled format for this workshop. PBIX files can be generated from PBIP later if a packaged file is needed.

## Lab data

| File or folder | Description |
|---|---|
| `https://raw.githubusercontent.com/Coding-Forge/PBI-Advanced-Factory/main/data/monthly-orders/orders-2026-01.csv` | January order extract. |
| `https://raw.githubusercontent.com/Coding-Forge/PBI-Advanced-Factory/main/data/monthly-orders/orders-2026-02.csv` | February order extract. |
| `https://raw.githubusercontent.com/Coding-Forge/PBI-Advanced-Factory/main/data/monthly-orders/orders-2026-03.csv` | March order extract with a data quality issue. |
| `https://raw.githubusercontent.com/Coding-Forge/PBI-Advanced-Factory/main/data/reference/product-category-map.csv` | Product category reference table. |

Use **Get data > Web** in Power BI Desktop to load each CSV from the raw GitHub URL.

## Novice-friendly how-to guide

### Create a Power Query parameter

1. In Power BI Desktop, select **Home > Transform data**.
2. In Power Query, select **Manage Parameters > New Parameter**.
3. Enter the exact parameter name from the lab.
4. Choose the data type, such as Text or Date/Time.
5. Enter the current value.
6. Select **OK**.
7. Use the parameter in source or filter steps instead of hard-coded values.

### Append queries

1. In Power Query, select **Home > Append Queries > Append Queries as New**.
2. Choose **Three or more tables** when combining several monthly files.
3. Add each raw monthly query to the append list.
4. Select **OK**.
5. Rename the appended query using the lab's exact query name.
6. Check that column names and data types match.

### Disable load for intermediate queries

1. Right-click each raw or staging query.
2. Clear **Enable load**.
3. Leave only final model-ready queries enabled.
4. Select **Close & Apply** after reviewing query names and data types.

## Lab 1: Staged query architecture

**Objective:** Create maintainable query layers.

### Tasks

1. Create a parameter named `RawDataBaseUrl` with value `https://raw.githubusercontent.com/Coding-Forge/PBI-Advanced-Factory/main/data/`.
2. Create Web queries for the three monthly order files using the raw URLs.
3. Name the raw Web queries `raw_Orders_2026_01`, `raw_Orders_2026_02`, and `raw_Orders_2026_03`.
4. Append the three raw queries into a staged query named `stg_OrdersCombined`.
5. Create a final load query named `fact_Orders`.
6. Disable load for raw and staging queries.

### Expected result

Only the final model-ready query is loaded. Intermediate queries remain available for development and troubleshooting.

## Lab 2: Folder combine

**Objective:** Combine monthly files safely.

### Tasks

1. Load each monthly order CSV using the Web connector.
2. Add a source file name column to each raw query for lineage.
3. Append the monthly queries.
4. Confirm all appended queries share the same schema.
5. Apply explicit data types.

### Expected result

All valid monthly order rows are appended into one query with consistent types and source lineage.

## Lab 3: Parameters and source switching

**Objective:** Use parameters to avoid hard-coded local paths.

### Tasks

1. Create `SourceFolderPath`.
2. Use it in the folder connector.
3. Create an optional `EnvironmentName` parameter with values such as `Dev`, `Test`, and `Prod`.
4. Document how each environment should map to source paths or gateway connections.

### Expected result

The query can be repointed without rewriting applied steps.

## Lab 4: Custom functions

**Objective:** Encapsulate reusable cleanup logic.

### Tasks

1. Create a query named `fn_CleanText`.
2. Convert it to a function that accepts nullable text.
3. Trim whitespace.
4. Clean non-printable characters.
5. Return null safely when input is null.
6. Invoke the function against customer and product text columns.

### Example function

```powerquery
(inputText as nullable text) as nullable text =>
let
    Result =
        if inputText = null then
            null
        else
            Text.Proper(Text.Trim(Text.Clean(inputText)))
in
    Result
```

### Expected result

Text cleanup is reusable and null-safe.

## Lab 5: Data quality and error handling

**Objective:** Detect and handle invalid source rows.

### Tasks

1. Add explicit type conversions.
2. Identify rows with invalid quantity, price, or order date values.
3. Create an error review query.
4. Replace or remove invalid rows according to documented business rules.
5. Add a data quality notes section to the lab output.

### Expected result

Learners can distinguish between silently removing bad data and explicitly reviewing data quality issues.

## Lab 6: Query folding

> **Azure Government note:** Query folding is marked **Gov-ready / Verify for source**. The concept is core Power Query, but hands-on folding validation requires a connector and source that support folding in the target environment.

**Objective:** Understand and validate folding behavior.

### Tasks

1. Review which file-based transformations cannot fold.
2. If a SQL or folding-capable source is available, connect to a sample table.
3. Apply filters and column selection.
4. Use **View Native Query** where available.
5. Add a non-foldable step and observe the effect.

### Expected result

Learners can explain why folding improves performance and why it must be validated per source.

## Lab 7: Incremental refresh preparation

> **Azure Government note:** Incremental refresh preparation in Desktop is generally Gov-ready, but applying and running the policy in the Service is **Verify for Gov**.

**Objective:** Prepare a fact query for incremental refresh.

### Tasks

1. Create DateTime parameters named `RangeStart` and `RangeEnd`.
2. Filter `fact_Orders[OrderDate]` using `RangeStart` and `RangeEnd`.
3. Confirm the filtered column is a DateTime-compatible column.
4. Document the intended refresh and archive windows.
5. Validate Service requirements before making refresh policy setup mandatory.

### Expected result

The fact query is ready for incremental refresh policy configuration when the Service environment supports it.

## Validation checklist

- [ ] Raw and staging queries have load disabled.
- [ ] Final fact query has explicit data types.
- [ ] Folder combine filters to expected files only.
- [ ] Source file lineage is preserved.
- [ ] Custom text cleanup function handles null values.
- [ ] Data quality issues are identified and documented.
- [ ] Query folding is demonstrated or explained with source limitations.
- [ ] Incremental refresh parameters are DateTime and correctly named.
- [ ] Dataflows, Dataflows Gen2, connectors, and Service refresh features include Gov notes.

