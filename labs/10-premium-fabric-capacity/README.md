# Module 10 Labs: Premium, Fabric, and Capacity-Aware Architecture

## Lab summary

These labs and demos help learners compare capacity options and evaluate advanced architecture features. Most hands-on activities are optional because they depend on licensing, capacity, cloud, tenant settings, and customer policy.

## Azure Government readiness

Fabric capacity, Direct Lake, OneLake, Lakehouse, Warehouse, Semantic Link, and autoscale are **Commercial-focused / Verify for Gov**. XMLA, paginated reports, large semantic model settings, and capacity metrics are **Verify for Gov**.

## Prerequisites

- Power BI Service access.
- Optional Premium/PPU/Fabric workspace.
- Optional XMLA-compatible tooling.
- Optional Power BI Report Builder.
- Optional capacity metrics app access.
- Optional Fabric workspace with validated feature availability.

## Lab 1: Licensing and capacity comparison

**Objective:** Choose architecture options based on workload requirements.

### Tasks

1. Review the licensing and capacity comparison table.
2. Define a workload scenario.
3. Identify user count, model size, refresh, latency, and governance needs.
4. Select possible capacity options.
5. Document required validation for Azure Government.

### Expected result

Learners can recommend an option with caveats and validation needs.

## Lab 2: XMLA endpoint connection where available

> **Azure Government note:** XMLA endpoint is **Verify for Gov**. Validate capacity, tenant settings, workspace configuration, tooling, and cloud support before making this hands-on.

### Tasks when available

1. Confirm XMLA endpoint setting.
2. Connect with an approved tool.
3. Inspect model metadata.
4. Document allowed read/write operations.

### Alternate path

Review XMLA use cases conceptually and document validation requirements.

## Lab 3: Paginated report where available

> **Azure Government note:** Paginated reports are **Verify for Gov**. Validate licensing, workspace support, Report Builder use, and cloud availability.

### Tasks when available

1. Open or create a simple paginated report.
2. Connect to approved sample data.
3. Add a table and parameter.
4. Publish where supported.
5. Review export behavior.

### Alternate path

Discuss scenarios where paginated reports are preferred over interactive reports.

## Lab 4: Large semantic model settings where available

> **Azure Government note:** Large semantic models are **Verify for Gov**. Validate capacity and tenant settings.

### Tasks when available

1. Review workspace capacity.
2. Review semantic model settings.
3. Identify model size constraints.
4. Document refresh and memory considerations.

## Optional commercial lab: Direct Lake

> **Azure Government note:** Direct Lake is **Commercial-focused / Verify for Gov**. Treat as optional unless validated.

### Tasks when available

1. Review source data in OneLake/Lakehouse/Warehouse.
2. Create or inspect a Direct Lake semantic model.
3. Compare with Import and DirectQuery concepts.
4. Document limitations and fallback path.

## Optional commercial lab: OneLake/Lakehouse/Warehouse integration

> **Azure Government note:** OneLake, Lakehouse, and Warehouse are **Commercial-focused / Verify for Gov**.

### Tasks when available

1. Review workspace items.
2. Identify how data is stored and exposed to Power BI.
3. Compare Lakehouse and Warehouse roles.
4. Document architecture and governance considerations.

## Optional commercial lab: Semantic Link

> **Azure Government note:** Semantic Link is **Commercial-focused / Verify for Gov**.

### Tasks when available

1. Review Semantic Link use cases.
2. Connect to semantic model metadata from a notebook where supported.
3. Document governance and security considerations.

## Lab 5: Capacity metrics and throttling concepts

> **Azure Government note:** Capacity metrics are **Verify for Gov**. Validate app availability, capacity type, permissions, and telemetry.

### Tasks when available

1. Open capacity metrics app.
2. Review interactive and background workload indicators.
3. Identify refresh pressure.
4. Identify throttling symptoms.
5. Document operational follow-up.

### Alternate path

Review capacity metrics conceptually and map likely symptoms to operational actions.

## Validation checklist

- [ ] Capacity comparison completed.
- [ ] XMLA endpoint marked **Verify for Gov**.
- [ ] Paginated reports marked **Verify for Gov**.
- [ ] Large semantic models marked **Verify for Gov**.
- [ ] Direct Lake marked **Commercial-focused / Verify for Gov**.
- [ ] OneLake/Lakehouse/Warehouse marked **Commercial-focused / Verify for Gov**.
- [ ] Semantic Link marked **Commercial-focused / Verify for Gov**.
- [ ] Autoscale marked **Commercial-focused / Verify for Gov**.
- [ ] Capacity metrics marked **Verify for Gov**.
- [ ] Gov-safe alternate architecture documented.

