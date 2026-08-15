# Instructor Guide

## Module summary

This module should help learners reason about architecture choices, not memorize SKU names. Emphasize workload requirements, governance, performance, operational ownership, and cloud availability.

## Audience and prerequisites

Best fit for BI platform owners, Power BI administrators, architects, semantic model developers, data engineers, and technical decision makers.

Learners should understand workspaces, semantic models, refresh, Service deployment, and performance concepts.

## Learning objectives

- Compare licensing and capacity options.
- Explain capacity-dependent features.
- Explain XMLA endpoint workflows.
- Explain paginated report scenarios.
- Explain Fabric-oriented patterns conceptually.
- Review capacity metrics and throttling behavior.
- Select Gov-safe alternatives when commercial/Fabric features are unavailable.

## Delivery flow

1. Start with workload requirements: users, data size, refresh, governance, latency, and integration.
2. Compare Pro, PPU, Premium capacity, and Fabric capacity.
3. Discuss large semantic models and XMLA endpoint workflows.
4. Discuss paginated reports.
5. Introduce Fabric capacity, OneLake, Lakehouse, Warehouse, Direct Lake, and Semantic Link conceptually.
6. Compare Direct Lake with Import and DirectQuery.
7. Review capacity metrics and throttling signals.
8. Map each architecture option to Gov readiness and validation needs.
9. Close with Gov-safe alternate architecture.

## Feature availability

| Feature | Status | Instructor note |
|---|---|---|
| Capacity comparison | Gov-ready conceptually | Required discussion. |
| XMLA endpoint | Verify for Gov | Optional hands-on only. |
| Paginated reports | Verify for Gov | Optional hands-on only. |
| Large semantic models | Verify for Gov | Optional hands-on only. |
| Fabric/Direct Lake/OneLake | Commercial-focused / Verify for Gov | Conceptual unless confirmed. |
| Semantic Link | Commercial-focused / Verify for Gov | Conceptual unless confirmed. |
| Autoscale | Commercial-focused / Verify for Gov | Conceptual unless confirmed. |
| Capacity metrics | Verify for Gov | Demo only if validated. |

## Environment setup

- Power BI Service access.
- Optional Premium/PPU/Fabric workspace.
- Optional XMLA-compatible tooling.
- Optional Power BI Report Builder for paginated reports.
- Optional Fabric workspace with Lakehouse/Warehouse/Direct Lake support.
- Optional capacity metrics app access.

## Lab facilitation notes

- Do not require Fabric hands-on activities for Azure Government customers unless validated.
- Keep the required path as architecture comparison and decision-making.
- Use Import-mode semantic models as the Gov-safe fallback for Direct Lake concepts.
- Treat XMLA, paginated reports, large models, and capacity metrics as optional hands-on activities.

## Common issues and fixes

| Issue | Likely cause | Fix |
|---|---|---|
| XMLA connection fails | Capacity, workspace, or tenant setting limitation | Validate capacity and XMLA endpoint settings. |
| Paginated report cannot publish | Licensing/workspace/cloud limitation | Mark **Verify for Gov** and use conceptual path. |
| Direct Lake unavailable | Fabric feature not enabled or unavailable in cloud | Use Import-mode alternate path. |
| Capacity metrics unavailable | Missing capacity admin role or app unsupported | Use conceptual throttling discussion. |
| Large model setting unavailable | Workspace not on compatible capacity | Validate capacity and tenant settings. |

## Gov delivery notes

Treat Fabric capacity, Direct Lake, OneLake, Lakehouse, Warehouse, Semantic Link, and autoscale as **Commercial-focused / Verify for Gov** unless confirmed. XMLA, paginated reports, large semantic models, and capacity metrics are **Verify for Gov**.

## Commercial-enhanced options

- Demonstrate XMLA endpoint connection.
- Publish a paginated report.
- Demonstrate Direct Lake over a Lakehouse or Warehouse.
- Review capacity metrics app.
- Demonstrate Semantic Link in Fabric notebooks where available.

