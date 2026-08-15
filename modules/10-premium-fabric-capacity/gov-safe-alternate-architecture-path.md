# Gov-Safe Alternate Architecture Path

Use this path when Fabric or capacity-dependent features are unavailable, unvalidated, or disallowed in an Azure Government environment.

## Architecture pattern

| Requirement | Gov-safe approach |
|---|---|
| Source-controlled report/model development | PBIP in git. |
| Standard semantic model | Import mode with scheduled refresh. |
| Large data handling | Aggregations, incremental refresh where validated, and model optimization. |
| Near-real-time needs | DirectQuery only when connector, gateway, and source performance are validated. |
| Direct Lake alternative | Import mode or DirectQuery with aggregation strategy. |
| OneLake/Lakehouse alternative | Approved Azure data platform or existing governed source. |
| Semantic Link alternative | Exported/queryable semantic model outputs or approved analysis workflow. |
| Capacity monitoring | Refresh history, usage metrics, Performance Analyzer, and capacity metrics only if validated. |
| Paginated reporting | Use standard Power BI reports or validated paginated report support. |

## Required documentation

For each unavailable commercial/Fabric feature, document:

- Intended capability.
- Availability status.
- Why it is not required.
- Gov-safe alternate path.
- Validation needed for future adoption.

## Example decision

If Direct Lake is unavailable, use:

1. PBIP source-controlled report/model.
2. Import semantic model with incremental refresh if validated.
3. Aggregation tables for summary performance.
4. Gateway-backed refresh where required.
5. Usage metrics and refresh history for operations.

