# Lab Manual

This lab manual links to every module lab and identifies whether the lab is required, optional, or validation-dependent for Azure Government delivery.

## HTML lab site

The student-facing HTML lab experience is available at:

```text
Student\Labs\Web\index.html
```

Each HTML page includes a persistent completion checklist backed by browser `localStorage`. Customer branding is controlled by:

```text
Student\Labs\Web\scripts\delivery-config.js
```

See `Student\Labs\Web\BRANDING.md` for branding instructions.

| Lab | Required path | Gov note |
|---|---|---|
| [Lab 01: Advanced Semantic Modeling](..\Student\Labs\Source\01-advanced-semantic-modeling\README.md) | Required | Core path is Gov-ready; composite/DirectQuery/hybrid/large models are Verify for Gov. |
| [Lab 02: Advanced DAX](..\Student\Labs\Source\02-advanced-dax\README.md) | Required | Core DAX is Gov-ready; calculation groups and DAX Studio are Verify for Gov. |
| [Lab 03: Advanced Power Query](..\Student\Labs\Source\03-advanced-power-query\README.md) | Required | File-based path is Gov-ready; connectors/dataflows/incremental refresh are Verify for Gov. |
| [Lab 04: Report Design UX](..\Student\Labs\Source\04-report-design-ux\README.md) | Required | Core UX and field parameters are Gov-ready; personalized/AI visuals are Verify for Gov. |
| [Lab 05: Performance Optimization](..\Student\Labs\Source\05-performance-optimization\README.md) | Required | Desktop path is Gov-ready; DAX Studio/capacity metrics are Verify for Gov. |
| [Lab 06: Advanced Analytics AI](..\Student\Labs\Source\06-advanced-analytics-ai\README.md) | Required with optional extensions | What-if parameters are Gov-ready; AI features are Verify for Gov or Commercial-focused. |
| [Lab 07: Security Design](..\Student\Labs\Source\07-security-design\README.md) | Required | RLS is Gov-ready; OLS/Purview/labels/B2B are Verify for Gov. |
| [Lab 08: Service Deployment](..\Student\Labs\Source\08-service-enterprise-deployment\README.md) | Required where Service access exists | Gateways/App audiences/deployment pipelines are Verify for Gov. |
| [Lab 09: Monitoring Governance](..\Student\Labs\Source\09-monitoring-governance\README.md) | Required where Service access exists | Admin/capacity/Purview labs are Verify for Gov. |
| [Lab 10: Premium Fabric Capacity](..\Student\Labs\Source\10-premium-fabric-capacity\README.md) | Architecture required, hands-on optional | Fabric/Direct Lake/OneLake are Commercial-focused / Verify for Gov. |
| [Lab 11: Automation DevOps](..\Student\Labs\Source\11-automation-devops\README.md) | PBIP/git required, automation optional | APIs/service principals/Fabric Git/CI-CD are Verify for Gov. |
| [Capstone](..\Student\Labs\Source\12-capstone\README.md) | Required | Gov-ready path required; commercial-enhanced path optional. |

## Lab delivery rules

- Use PBIP as the Power BI source format.
- Use only synthetic data.
- Validate all tenant-dependent features before hands-on delivery.
- Convert unvalidated features to conceptual discussion.
- Record validation evidence and gaps.



