# Troubleshooting Notes

## Folder combine

| Symptom | Likely cause | Resolution |
|---|---|---|
| Extra rows appear after combine | Hidden, temp, or unrelated files are included | Filter to `.csv`, exclude hidden files, and use a naming pattern such as `orders-`. |
| Combine fails after adding a new file | New file has different columns or delimiters | Validate schema and update the transform sample file logic. |
| Column types are inconsistent | Auto type detection used different samples | Remove automatic type steps and apply explicit types after combine. |

## Parameters

| Symptom | Likely cause | Resolution |
|---|---|---|
| Source path parameter fails | Path points to the wrong folder or lacks escaping | Validate the folder path and use a parameter value appropriate to the local environment. |
| Privacy warning appears | Combining sources with different privacy levels | Review privacy level settings and customer policy before changing them. |
| Environment switching breaks refresh | Service/gateway path differs from Desktop path | Document gateway mapping or use a supported cloud/source path. |

## Custom functions

| Symptom | Likely cause | Resolution |
|---|---|---|
| Function returns errors for nulls | Function assumes text input | Add null handling before text operations. |
| Function prevents folding | Custom row-by-row operation cannot be pushed to source | Apply foldable filters before invoking the function. |
| Function is hard to debug | Too much logic is nested in one expression | Break logic into named steps before converting to a function. |

## Query folding

| Symptom | Likely cause | Resolution |
|---|---|---|
| View Native Query is disabled | Step does not fold or connector does not expose native query view | Check earlier steps, simplify transformation, or use a folding-capable source for the demo. |
| Query is slow even though it folds | Source system is slow or missing indexes | Filter earlier, reduce columns, or coordinate with source owners. |
| Query stops folding after a step | Non-foldable transformation introduced | Move foldable filters and column selection before the blocking step. |

## Incremental refresh

| Symptom | Likely cause | Resolution |
|---|---|---|
| Incremental refresh settings unavailable | `RangeStart` and `RangeEnd` parameters missing or wrong type | Create DateTime parameters with exact names and use them in a date/time filter. |
| Refresh policy does not work in Service | Workspace, license, or tenant does not support required feature | Validate Service support before delivery, especially for Azure Government customers. |
| Filter is applied to the wrong column | Fact table uses text or date role mismatch | Use the transaction date/time column intended for partitioning. |

## Azure Government validation

| Area | Validation need |
|---|---|
| Connectors | Confirm availability in target cloud and customer network. |
| Gateways | Confirm gateway version, data source mapping, and credential policy. |
| Dataflows | Confirm Service availability, workspace support, and tenant settings. |
| Dataflows Gen2 | Confirm Fabric and sovereign cloud availability before including. |
| Incremental refresh | Confirm licensing, workspace, Service behavior, and gateway/source support. |

