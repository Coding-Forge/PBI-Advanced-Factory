# Azure Government Readiness Review

This review summarizes Azure Government readiness across the Power BI Advanced Factory workshop. It does not replace validation in the target customer tenant. Any feature marked **Verify for Gov** or **Commercial-focused** must be validated before it is used as a required hands-on lab step.

## Readiness status legend

| Status | Meaning |
|---|---|
| **Gov-ready** | Suitable for the required Gov delivery path, subject to normal licensing, tenant settings, and customer policy. |
| **Verify for Gov** | Requires validation in the target tenant, cloud, region, capacity, connector, gateway, or workstation policy. |
| **Commercial-focused** | Commercial-only, commercial-first, or commonly delayed/unavailable in sovereign clouds. Use conceptually or provide a Gov-safe alternate path. |

## Module readiness matrix

| Module | Required Gov-ready path | Verify for Gov / Commercial-focused items | Gov-safe alternate |
|---|---|---|---|
| 1. Advanced Semantic Modeling | Star schema, relationships, role-playing dimensions, bridge tables, date dimensions | Composite models, DirectQuery source behavior, hybrid tables, large semantic models | Import-mode model, duplicated role-playing dimensions, standard DAX measures, conceptual discussion for tenant-dependent features |
| 2. Advanced DAX | Core DAX, context transition, time intelligence, ranking, dynamic titles, measure switching | Calculation groups, DAX Studio and external tooling | Use Desktop visuals and Performance Analyzer; keep DAX Studio optional; use separate measures when calculation groups are not validated |
| 3. Advanced Power Query | Local files, staging, parameters, custom functions, folder combine, data quality checks | Query folding by source, Service incremental refresh, dataflows, Dataflows Gen2, connectors | File-based labs, Desktop preparation, conceptual folding review |
| 4. Report Design and UX | Drillthrough, tooltips, bookmarks, buttons, navigation, field parameters, conditional formatting, mobile layout, accessibility review | Personalized visuals, AI visuals, mobile app policy | Native visuals and non-AI interaction patterns |
| 5. Performance Optimization | Performance Analyzer, model/cardinality review, visual optimization, DAX optimization | DAX Studio, VertiPaq Analyzer, capacity metrics, Service incremental refresh, aggregation over DirectQuery source | Desktop-only performance review and conceptual capacity discussion |
| 6. Advanced Analytics and AI | What-if parameters and non-AI analysis patterns | Decomposition tree, forecasting, anomaly detection, key influencers, Python/R, Azure ML, Copilot | What-if parameters, DAX thresholds, rolling averages, matrix/drillthrough analysis |
| 7. Security Design | Static RLS, dynamic RLS, Desktop role testing, Build permission concepts | OLS, sensitivity labels, Purview, external sharing, B2B behavior | RLS-only core path plus documented governance review |
| 8. Service Enterprise Deployment | Workspaces, publishing, Apps, refresh concepts, shared semantic models | Gateways, App audiences, deployment pipelines, cloud connections, certification tenant settings | Instructor demo or conceptual walkthrough when Service capabilities are unavailable |
| 9. Monitoring and Governance | Usage metrics, refresh history, tenant settings review where permitted | Activity/audit logs, admin monitoring workspace, capacity metrics, Purview, DLP | Operations runbook, refresh history, usage review, conceptual admin monitoring |
| 10. Premium, Fabric, and Capacity | Capacity comparison and architecture decision framework | Fabric capacity, Direct Lake, OneLake, Lakehouse, Warehouse, Semantic Link, autoscale, XMLA, paginated reports, capacity metrics | Import-mode semantic model, aggregations, incremental refresh where validated, conceptual Fabric discussion |
| 11. Automation and DevOps | PBIP, git workflow, deployment checklist | REST APIs, PowerShell, service principals, XMLA, Tabular Editor, ALM Toolkit, Fabric Git integration, Azure DevOps, GitHub Actions | Reviewed manual deployment from PBIP with recorded evidence |
| 12. Capstone | PBIP, Import model, DAX, report UX, RLS, Service/App path where available, governance and operations documentation | Fabric/Git/Copilot/API/automation/capacity extensions | Gov-ready capstone path with optional commercial-enhanced extensions excluded unless validated |

## Commercial-only and parity-sensitive features

The following features must not be required for Azure Government learners unless explicitly validated:

- Fabric workspace Git integration
- Fabric capacity workloads
- Direct Lake
- OneLake
- Lakehouse and Warehouse
- Semantic Link
- Copilot in Power BI/Fabric
- AI visuals where tenant availability is not confirmed
- Dataflows Gen2
- Autoscale
- Deployment pipelines where cloud/license support is not confirmed
- REST API/service principal automation where endpoint and tenant settings are not confirmed
- XMLA read/write workflows where capacity and tenant settings are not confirmed

## Gov-safe alternate steps

| If this feature is unavailable | Use this alternate |
|---|---|
| Fabric Git integration | Local PBIP project plus git workflow. |
| Direct Lake | Import semantic model with incremental refresh and aggregations where validated. |
| OneLake/Lakehouse/Warehouse | Approved customer data source or local synthetic data. |
| Copilot | Static examples, instructor prompts, and human-authored explanations. |
| AI visuals | Native visuals, DAX thresholds, Top N, rankings, and drillthrough. |
| Dataflows Gen2 | Power Query in Desktop or standard dataflows where validated. |
| Deployment pipelines | Manual workspace promotion with deployment checklist evidence. |
| REST API automation | Manual deployment from PBIP with recorded commit ID and validation evidence. |
| Service principal authentication | User-led/manual deployment using approved roles. |
| XMLA external tooling | Desktop-only model authoring and conceptual ALM discussion. |
| Capacity metrics | Usage metrics, refresh history, Performance Analyzer, and operations runbook notes. |

## Current validation status

This repository has documented Azure Government readiness labels and Gov-safe alternate paths, but it has **not** been validated in a live Azure Government tenant in this session.

| Validation area | Status | Notes |
|---|---|---|
| Module content review | Complete | Each module includes feature availability notes. |
| Feature labels | Complete | Modules use Gov-ready, Verify for Gov, and Commercial-focused labels. |
| Gov-safe alternate paths | Complete | Alternates are documented in module labs and dedicated Gov-safe path files. |
| Gov tenant lab validation | Gap documented | Requires access to the target customer tenant. |
| Customer-approved connectors | Pending | Requires customer data source and connector list. |
| Gateway setup and identity | Pending | Requires customer gateway/network/identity details. |
| External tool policy | Pending | Requires customer workstation/tooling policy. |
| Sensitivity labels and Purview | Pending | Requires MIP/Purview tenant configuration details. |
| Fabric feature availability | Pending | Requires target tenant/capacity validation. |
| Copilot/AI availability | Pending | Requires target tenant/capacity/admin validation. |
| REST API/service principal availability | Pending | Requires tenant endpoint, app registration, and admin setting validation. |

## Pre-delivery validation checklist

- [ ] Identify target cloud: Commercial, GCC, GCC High, or DoD.
- [ ] Confirm Power BI/Fabric licensing.
- [ ] Confirm workspace and capacity type.
- [ ] Confirm allowed connectors and data sources.
- [ ] Confirm gateway topology and ownership.
- [ ] Confirm identity format for RLS.
- [ ] Confirm external tool policy for DAX Studio, Tabular Editor, and ALM Toolkit.
- [ ] Confirm sensitivity label and Purview availability.
- [ ] Confirm Fabric feature availability.
- [ ] Confirm Copilot and AI visual availability.
- [ ] Confirm REST API and service principal support.
- [ ] Confirm Azure DevOps or GitHub Actions policy.
- [ ] Remove or convert unvalidated features to conceptual-only sections before delivery.

