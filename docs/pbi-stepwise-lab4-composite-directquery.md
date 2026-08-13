# pbi-stepwise — Lab 4: Composite Model / DirectQuery Comparison

**Status:** Conceptual only, per lab instructions (`Student\Labs\Source\01-advanced-semantic-modeling\README.md`, Lab 4). No hands-on build required in `pbi-stepwise`; this document satisfies the lab's deliverable. Marked **Verify for Gov** in the source lab.

## Objective

Compare Import, DirectQuery, Dual, and composite model design choices for the star schema built in Labs 1-3, and justify a storage-mode design instead of defaulting to DirectQuery.

## Current model (all Import)

| Table | Grain | Volume (training data) |
|---|---|---|
| `FactSales` | Sales order line | Small (synthetic CSV) |
| `FactTargets` | Territory/category/month | Small |
| `DimCustomer`, `DimProduct`, `DimProductCategory`, `DimTerritory`, `DimSegment` | Standard dimension | Small |
| `BridgeCustomerSegment` | Customer-segment mapping | Small |
| `DimOrderDate`, `DimShipDate` | Date | ~2,500 rows each (2023-2029) |

At this data volume, Import mode is correct for every table — the entire dataset fits comfortably in memory, refresh is instant, and there is no source-system load concern.

## Storage-mode analysis (if this were a production model with a live ERP/CRM source)

| Table | Recommended mode | Why |
|---|---|---|
| `FactSales` | **Import** (or Import with incremental refresh) | High query volume from report visuals; DirectQuery would push every slicer/filter change to the source system and hurt interactivity. Incremental refresh handles growth without full reloads. |
| `FactTargets` | **Import** | Low volume, low update frequency (monthly). No benefit to DirectQuery. |
| `DimCustomer`, `DimProduct`, `DimTerritory`, `DimProductCategory`, `DimSegment` | **Dual** (candidate) | Dual-mode dimensions can participate in both Import fact queries and any future DirectQuery fact table without duplicating storage, and they satisfy the "single version of dimension truth" requirement in a composite model. |
| `BridgeCustomerSegment` | **Import** | Small mapping table; no freshness requirement beyond nightly refresh. |
| `DimOrderDate`, `DimShipDate` | **Import** (Dual optional) | Static/generated calendar; freshness is irrelevant since dates are calculated, not sourced. |

### Where DirectQuery might be justified

- A near-real-time operational table (e.g., current-day order status, inventory levels) that must reflect source-system state within seconds/minutes, where Import's refresh latency is unacceptable.
- Very large fact tables (billions of rows) that cannot fit in the semantic model's memory budget even with aggregations.

### Where DirectQuery is a poor fit here

- Any dimension table — dimension queries are frequent, low-latency, and the data itself changes rarely; Import trivially wins on performance.
- `FactSales`/`FactTargets` at this training data scale — there is no freshness or volume justification, and DirectQuery would add query latency and place unnecessary load on the source for every visual interaction.

## Composite model tradeoffs (general guidance)

| Factor | Import | DirectQuery | Composite/Dual |
|---|---|---|---|
| Query performance | Fastest (in-memory VertiPaq) | Slower (round-trip to source per query) | Import-speed for Import/Dual tables; DirectQuery-speed for DQ tables |
| Data freshness | As of last refresh | Real-time | Mixed — Dual tables adapt per query context |
| Source system load | None after refresh | Continuous, proportional to report usage | Only for DirectQuery portion |
| Feature support | Full DAX/time intelligence support | Some DAX functions restricted or slower | Full support for Import/Dual; DirectQuery-side limits still apply |
| Model size limits | Bound by available memory (or Premium capacity) | Effectively unbounded (source handles storage) | Best of both — large DQ fact + small Import/Dual dimensions |
| Refresh complexity | Simple; may need incremental refresh at scale | None (always current) | Manage both refresh AND live query paths |

## Azure Government note

Composite model, DirectQuery, Dual storage mode, and large semantic model features are marked **Verify for Gov** in the source lab. Before treating this as a required, hands-on pattern for a Gov tenant:

- Confirm the target data source connector is supported in Azure Government's Power BI service.
- Confirm On-premises Data Gateway (or VNet gateway) connectivity and any required government cloud-specific configuration.
- Confirm capacity/licensing (Premium/Fabric capacity) requirements for composite models and large semantic models are met in the Gov tenant.
- Validate with a small pilot before committing a training exercise or production model to DirectQuery/composite mode in a Gov environment.

## Conclusion

For the `pbi-stepwise` training model, **Import mode for all tables is the correct, justified choice** — there is no freshness or volume requirement that DirectQuery would solve, and Import maximizes report performance and DAX feature support. This analysis satisfies Lab 4's conceptual deliverable without introducing DirectQuery/composite complexity into the training PBIP.
