# Licensing and Capacity Comparison

Use this table as a workshop discussion aid. Always validate current licensing, cloud availability, tenant settings, and customer agreements before making delivery or architecture commitments.

| Option | Typical fit | Strengths | Watch-outs | Gov note |
|---|---|---|---|---|
| Power BI Pro | Team and departmental sharing | Low barrier, common licensing model, standard Service features | Per-user licensing, limited advanced capacity features | Validate tenant and license availability. |
| Premium Per User | Individual or small-team access to premium-like features | Lower entry point for some advanced features | Per-user requirement, not same as dedicated capacity | **Verify for Gov**. |
| Premium capacity | Enterprise-scale shared capacity | Dedicated resources, broader enterprise features, large workloads | Capacity management, cost, admin ownership | **Verify for Gov** by SKU/cloud. |
| Fabric capacity | Integrated Fabric workloads | OneLake, Lakehouse, Warehouse, Direct Lake, notebooks, Fabric experiences | Cloud parity, workload governance, capacity management | **Commercial-focused / Verify for Gov**. |

## Capability comparison

| Capability | Pro | PPU | Premium capacity | Fabric capacity | Gov delivery note |
|---|---|---|---|---|---|
| Standard report sharing | Yes | Yes | Yes | Yes | Validate tenant settings. |
| Power BI Apps | Yes | Yes | Yes | Yes | Validate App audience parity. |
| Large semantic models | No / limited | Verify | Verify | Verify | Capacity and settings required. |
| XMLA endpoint | No | Verify | Verify | Verify | Validate tenant/capacity settings. |
| Paginated reports | Verify | Verify | Verify | Verify | Validate cloud and licensing. |
| Deployment pipelines | Verify | Verify | Verify | Verify | Validate capacity/license/cloud. |
| Direct Lake | No | No | No | Verify | Commercial-focused / Verify for Gov. |
| OneLake/Lakehouse/Warehouse | No | No | No | Verify | Commercial-focused / Verify for Gov. |
| Capacity metrics | N/A | Verify | Verify | Verify | Validate app and telemetry. |

## Decision prompts

- How many users need to consume content?
- How many users need to build content?
- How large are the semantic models?
- What refresh frequency is required?
- Are workloads interactive, background, or both?
- Are Fabric workloads required or optional?
- Is the customer in commercial, GCC, GCC High, or DoD?
- What features must be validated before committing to a lab or architecture?

