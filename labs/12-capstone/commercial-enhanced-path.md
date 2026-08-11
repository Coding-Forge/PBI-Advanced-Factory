# Capstone Commercial-Enhanced Path

Use this path only when the tenant, licensing, capacity, data boundary, admin settings, and customer policy have been validated.

## Optional extensions

| Extension | Validation required |
|---|---|
| Fabric workspace Git integration | Fabric availability, workspace support, git provider, branch policy. |
| Direct Lake | Fabric capacity, OneLake/Lakehouse/Warehouse source, model support. |
| OneLake/Lakehouse/Warehouse | Fabric workload availability, data governance, security. |
| Copilot | Tenant/capacity/licensing availability, data residency, admin settings, sensitivity controls. |
| AI visuals | Visual availability, tenant policy, data residency. |
| Deployment pipelines | License/capacity/workspace support, deployment rules. |
| REST API deployment | Endpoint, authentication, permissions, tenant settings. |
| Service principal automation | Entra ID app, admin approval, security group scoping, workspace access. |
| XMLA workflows | Capacity, tenant setting, tooling, read/write permission. |
| Capacity metrics | Capacity admin role, app availability, telemetry. |

## Required controls

- Keep PBIP as source of record.
- Document feature availability status.
- Document fallback path.
- Record validation evidence.
- Avoid customer-sensitive data in AI/Copilot demos.
- Require human review for AI-generated output.

