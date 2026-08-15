# Knowledge Check

## Questions

1. Why should architecture decisions start with workload requirements?
2. What is one difference between Pro and dedicated capacity?
3. Why is XMLA endpoint marked **Verify for Gov**?
4. What type of reporting need is a good fit for paginated reports?
5. Why are Fabric capacity and Direct Lake marked **Commercial-focused / Verify for Gov**?
6. What is OneLake intended to provide conceptually?
7. What is the Gov-safe fallback for Direct Lake?
8. What does capacity metrics help diagnose?
9. Why is autoscale marked **Commercial-focused / Verify for Gov**?
10. What should be documented before recommending a capacity-dependent feature?

## Answer key

1. Workload requirements determine whether the priority is user scale, refresh, data size, latency, governance, or integration.
2. Dedicated capacity provides shared reserved resources and capacity-scoped features, while Pro is primarily per-user licensing for standard sharing.
3. XMLA requires compatible capacity, workspace configuration, tenant settings, tooling, and cloud support.
4. Pixel-perfect operational reports, printable invoices, formal statements, and highly formatted exports are good paginated report scenarios.
5. Fabric and Direct Lake availability may lag or differ in sovereign clouds and require capacity, tenant, and region validation.
6. OneLake is intended as a unified logical data lake for Fabric workloads.
7. Use Import mode with incremental refresh and aggregations where validated, or DirectQuery only when source performance and connector support are validated.
8. It helps diagnose capacity pressure, refresh workload, interactive workload, throttling, and resource utilization.
9. Autoscale depends on licensing, capacity model, and cloud availability.
10. Document licensing, tenant settings, cloud availability, capacity requirements, admin ownership, security, and fallback path.

