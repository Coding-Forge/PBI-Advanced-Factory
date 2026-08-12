# Advanced Power BI Training Outline

## Purpose

Create a structured set of training modules and labs for advanced Power BI Desktop and Power BI Service capabilities. The material should be suitable for mixed customer audiences, including commercial and Azure Government customers.

## Availability legend

Use these labels throughout training and lab content:

| Label | Meaning |
|---|---|
| **Gov-ready** | Feature is generally appropriate for Azure Government training, subject to normal licensing and tenant settings. |
| **Verify for Gov** | Feature may vary by cloud, region, license, tenant setting, preview status, or capacity configuration. Confirm in the customer's tenant before using in a required lab. |
| **Commercial-focused** | Feature is commercial-only, preview-first in commercial, or commonly unavailable/delayed in Azure Government. Cover conceptually or provide an alternate Gov-ready lab path. |

## Training architecture

The workshop should be organized around three learning tracks:

1. **Advanced authoring** - Power BI Desktop modeling, DAX, Power Query, report UX, and performance tuning.
2. **Enterprise operations** - Power BI Service workspaces, deployment, security, governance, refresh, monitoring, and administration.
3. **Modern lifecycle and Fabric-aware patterns** - source control, deployment automation, Premium/Fabric capacity, Direct Lake, XMLA, and related enterprise architecture considerations.

## Module 1: Advanced semantic modeling

**Goal:** Teach customers how to design scalable, maintainable semantic models that support enterprise reporting.

**Topics:**

- Star schema design and dimensional modeling
- Fact tables, dimension tables, bridge tables, and role-playing dimensions
- Relationship direction and cardinality
- Many-to-many modeling patterns
- Bi-directional filtering: appropriate and risky use cases
- Composite models
- Import, DirectQuery, Dual storage mode, and hybrid tables
- Aggregation tables
- Calculation groups
- Field parameters
- Model perspectives
- Shared semantic models and thin reports
- Managing large semantic models

**Azure Government considerations:**

| Feature | Gov status | Notes |
|---|---|---|
| Star schema, relationships, DAX measures | Gov-ready | Core Desktop modeling concepts. |
| Composite models and DirectQuery | Gov-ready | Data source support and gateway configuration still need tenant validation. |
| Calculation groups | Verify for Gov | Native Desktop authoring depends on Desktop version; validate TMDL, XMLA, external tools, and capacity/workstation policy as needed. |
| Field parameters | Gov-ready | Confirm Desktop and Service version parity for the customer tenant. |
| Hybrid tables and advanced incremental refresh | Verify for Gov | Licensing, capacity, and cloud support should be validated. |
| Large semantic models | Verify for Gov | Requires Premium, PPU, or Fabric capacity capabilities depending on tenant. |

**Lab ideas:**

- Build a star schema from a flat sales dataset.
- Refactor a weak model into fact and dimension tables.
- Add role-playing date dimensions.
- Compare Import, DirectQuery, and composite model behavior.

## Module 2: Advanced DAX

**Goal:** Help authors reason about filter context, row context, and reusable measure patterns.

**Topics:**

- Row context vs. filter context
- Context transition
- `CALCULATE` and advanced filter manipulation
- `ALL`, `REMOVEFILTERS`, `ALLEXCEPT`, `KEEPFILTERS`, `TREATAS`
- Variables and measure branching
- Time intelligence patterns
- Semi-additive measures
- Dynamic segmentation
- Ranking and Top N
- Dynamic measure switching
- Dynamic titles and labels
- Parent-child hierarchies
- Debugging DAX
- Optimizing DAX for model and visual performance

**Azure Government considerations:**

| Feature | Gov status | Notes |
|---|---|---|
| Core DAX language | Gov-ready | Power BI Desktop feature; generally cloud-independent. |
| Time intelligence and calculation patterns | Gov-ready | Requires a well-designed date table. |
| DAX Studio | Verify for Gov | Local tool, but access to Service models depends on tenant, XMLA endpoint, and security policy. |
| External tool integration | Verify for Gov | May be limited by customer workstation policy. |

**Lab ideas:**

- Diagnose incorrect totals caused by context misunderstanding.
- Build a measure branching pattern.
- Create advanced time intelligence measures.
- Build dynamic Top N and ranking visuals.
- Optimize slow measures using variables and filter simplification.

## Module 3: Advanced Power Query and data transformation

**Goal:** Teach reusable, performant, and governable data preparation patterns.

**Topics:**

- M language fundamentals beyond the UI
- Query folding
- Native query considerations
- Parameters and dynamic source configuration
- Custom functions
- Combining files from folders
- Staging queries vs. final load queries
- Error handling and data quality checks
- Incremental refresh preparation
- Reusable transformation patterns
- Data source privacy levels
- Performance tuning in Power Query

**Azure Government considerations:**

| Feature | Gov status | Notes |
|---|---|---|
| Power Query in Desktop | Gov-ready | Core local authoring capability. |
| Query folding | Gov-ready | Depends on connector and source system. |
| Cloud dataflows | Verify for Gov | Availability depends on Power BI/Fabric cloud and tenant configuration. |
| Dataflows Gen2 | Commercial-focused / Verify for Gov | Fabric-related feature; validate sovereign cloud availability before using in Gov labs. |

**Lab ideas:**

- Build a staged Power Query pipeline.
- Prove whether a query folds.
- Convert repeated transformations into a custom function.
- Add parameters for dev/test/prod source switching.
- Prepare a table for incremental refresh.

## Module 4: Advanced report design and user experience

**Goal:** Teach authors to create highly interactive, accessible, and role-aware reports.

**Topics:**

- Advanced slicer and filter design
- Drillthrough pages
- Tooltip pages
- Bookmarks and buttons
- Page and visual navigation
- Dynamic visuals
- Conditional formatting
- Small multiples
- Report page tooltips
- Personalized visuals
- Mobile-optimized layouts
- Accessibility design
- Designing for executive, analyst, and operational audiences

**Azure Government considerations:**

| Feature | Gov status | Notes |
|---|---|---|
| Drillthrough, tooltips, bookmarks, buttons | Gov-ready | Core report authoring capabilities. |
| Mobile layouts | Gov-ready | Validate mobile app policy for Gov users. |
| Personalized visuals | Verify for Gov | Depends on Service feature availability and tenant settings. |
| AI visuals | Verify for Gov / Commercial-focused | Some AI experiences may lag or be unavailable in sovereign clouds. |

**Lab ideas:**

- Add drillthrough from summary to transaction detail.
- Build a bookmark-driven guided analysis experience.
- Create report page tooltips.
- Design an executive summary and analyst detail page.
- Create a mobile-optimized version of a report.

## Module 5: Performance optimization

**Goal:** Teach practical diagnostics and optimization techniques across model, DAX, Power Query, and visual layers.

**Topics:**

- Performance Analyzer in Power BI Desktop
- DAX Studio query timings
- VertiPaq Analyzer concepts
- Reducing column cardinality
- Removing unused columns and tables
- Optimizing relationships
- Optimizing visuals
- Import vs. DirectQuery tradeoffs
- Aggregations
- Incremental refresh
- Hybrid and large-model strategies
- Service-side refresh and query troubleshooting

**Azure Government considerations:**

| Feature | Gov status | Notes |
|---|---|---|
| Performance Analyzer | Gov-ready | Desktop feature. |
| DAX Studio and VertiPaq Analyzer | Verify for Gov | Local tools; Service model access may depend on tenant and XMLA support. |
| Aggregations | Gov-ready | Validate source and DirectQuery behavior. |
| Incremental refresh | Verify for Gov | Licensing, workspace, and capacity may affect availability. |
| Capacity metrics | Verify for Gov | App and telemetry availability can vary by cloud and capacity type. |

**Lab ideas:**

- Use Performance Analyzer to identify slow visuals.
- Reduce a model's size by lowering cardinality.
- Use DAX Studio to compare measure performance.
- Create an aggregation table over a DirectQuery source.
- Configure incremental refresh and test policy behavior.

## Module 6: Advanced analytics and AI-assisted insights

**Goal:** Introduce advanced analytics capabilities while clearly separating Gov-ready features from commercial-only or parity-sensitive experiences.

**Topics:**

- Key influencers visual
- Decomposition tree
- Forecasting
- Anomaly detection
- Clustering
- What-if parameters
- Python and R visuals
- Natural language Q&A configuration
- Azure Machine Learning integration
- Copilot and AI-assisted experiences

**Azure Government considerations:**

| Feature | Gov status | Notes |
|---|---|---|
| What-if parameters | Gov-ready | Desktop modeling/reporting feature. |
| Decomposition tree | Verify for Gov | Confirm visual availability and tenant settings. |
| Key influencers | Verify for Gov | AI feature availability may differ in Gov clouds. |
| Forecasting/anomaly detection | Verify for Gov | Validate feature and data residency requirements. |
| Python/R visuals | Verify for Gov | Depends on Desktop configuration, package policy, and Service support. |
| Azure Machine Learning integration | Verify for Gov | Depends on Azure cloud, region, workspace, network, and identity configuration. |
| Copilot in Power BI/Fabric | Commercial-focused / Verify for Gov | Treat as conceptual unless confirmed available in the customer's sovereign tenant. |

**Lab ideas:**

- Build a what-if parameter scenario analysis.
- Use decomposition tree for driver analysis where available.
- Add forecasting to a time-series visual.
- Compare AI visual availability between commercial and Gov delivery paths.

## Module 7: Security design

**Goal:** Teach security patterns that protect data while preserving usability.

**Topics:**

- Static row-level security
- Dynamic row-level security using user principal name
- Object-level security
- Security table patterns
- Testing roles in Power BI Desktop
- Assigning roles in the Power BI Service
- Build permission and downstream access
- Sensitivity labels
- Export controls
- Sharing vs. App vs. workspace access
- External sharing risks

**Azure Government considerations:**

| Feature | Gov status | Notes |
|---|---|---|
| RLS | Gov-ready | Core Power BI capability. |
| Dynamic RLS | Gov-ready | Validate identity format and Entra ID synchronization. |
| OLS | Verify for Gov | Often requires XMLA-compatible tooling and compatible capacity. |
| Sensitivity labels | Verify for Gov | Requires Microsoft Purview Information Protection configuration and cloud support. |
| External sharing | Verify for Gov | Often restricted by tenant, B2B, GCC/GCC High/DoD policy, and data handling rules. |

**Lab ideas:**

- Implement static and dynamic RLS.
- Test RLS roles in Desktop and Service.
- Demonstrate Build permission effects.
- Add sensitivity labels where available.
- Review export and sharing settings from a governance perspective.

## Module 8: Power BI Service enterprise deployment

**Goal:** Teach how to publish, govern, refresh, and distribute content at enterprise scale.

**Topics:**

- Workspace roles
- Workspace organization patterns
- Power BI Apps
- App audiences
- Deployment pipelines
- Promoted and certified content
- Scheduled refresh
- Data source credentials
- Gateway configuration
- Cloud connections
- Shared semantic models
- Thin reports
- Semantic model impact analysis
- Refresh history and troubleshooting

**Azure Government considerations:**

| Feature | Gov status | Notes |
|---|---|---|
| Workspaces, Apps, sharing, refresh | Gov-ready | Validate tenant sharing restrictions and licensing. |
| App audiences | Verify for Gov | Confirm Service parity in target cloud. |
| Deployment pipelines | Verify for Gov | Requires compatible licensing/capacity and Service availability. |
| Certified semantic models | Gov-ready / Verify for Gov | Requires tenant endorsement settings and governance process. |
| Cloud connections | Verify for Gov | Connector and Service availability may vary. |

**Lab ideas:**

- Publish a report and semantic model to a workspace.
- Configure scheduled refresh and credentials.
- Configure a gateway-backed data source.
- Create an App with audience targeting where available.
- Promote or certify a semantic model using a governance checklist.

## Module 9: Monitoring, administration, and governance

**Goal:** Teach platform owners how to monitor adoption, control risk, and support production workloads.

**Topics:**

- Usage metrics
- Refresh history
- Activity logs
- Admin portal tenant settings
- Admin monitoring workspace
- Capacity metrics app
- Gateway monitoring
- Audit logs
- Microsoft Purview integration
- Data loss prevention policies
- Adoption tracking
- Support and troubleshooting operating model

**Azure Government considerations:**

| Feature | Gov status | Notes |
|---|---|---|
| Usage metrics and refresh history | Gov-ready | Tenant policy may affect access. |
| Activity logs and audit logs | Verify for Gov | Requires admin permissions and audit configuration. |
| Admin monitoring workspace | Verify for Gov | Availability can vary by cloud and tenant. |
| Capacity metrics app | Verify for Gov | Confirm for Premium/Fabric capacity type and cloud. |
| Purview integration and DLP | Verify for Gov | Depends on M365/Purview cloud, licensing, and tenant configuration. |

**Lab ideas:**

- Interpret usage metrics for a deployed report.
- Troubleshoot a failed refresh.
- Review tenant settings that affect export and sharing.
- Inspect gateway status and data source mappings.
- Build an adoption and support checklist.

## Module 10: Premium, Fabric, and capacity-aware architecture

**Goal:** Explain advanced architecture choices for large models, enterprise scale, and Fabric-integrated analytics.

**Topics:**

- Power BI Pro, Premium Per User, Premium capacity, and Fabric capacity
- Large semantic models
- XMLA endpoint
- Paginated reports
- Direct Lake mode
- OneLake integration
- Lakehouse and warehouse integration
- Semantic Link
- Capacity planning
- Autoscale and workload management
- Capacity metrics and throttling behavior

**Azure Government considerations:**

| Feature | Gov status | Notes |
|---|---|---|
| Premium capacity concepts | Verify for Gov | Validate SKU, tenant, and cloud availability. |
| XMLA endpoint | Verify for Gov | Requires compatible capacity and admin settings. |
| Paginated reports | Verify for Gov | Usually supported in many enterprise scenarios, but validate cloud and licensing. |
| Fabric capacity | Commercial-focused / Verify for Gov | Fabric service parity in sovereign clouds must be confirmed. |
| Direct Lake, OneLake, Lakehouse, Warehouse, Semantic Link | Commercial-focused / Verify for Gov | Treat as conceptual or optional unless confirmed in the target Gov tenant. |
| Autoscale | Commercial-focused / Verify for Gov | Validate availability and licensing before including in Gov delivery. |

**Lab ideas:**

- Compare Pro, PPU, Premium, and Fabric capacity scenarios.
- Connect to a semantic model through XMLA where available.
- Publish and manage a paginated report where available.
- Demonstrate Direct Lake conceptually, with an alternate Import-mode lab for Gov.
- Analyze capacity metrics where available.

## Module 11: Automation, DevOps, and lifecycle management

**Goal:** Teach repeatable deployment and source-control patterns for enterprise BI solutions.

**Topics:**

- PBIP project format
- Source control strategy
- Git integration in Fabric workspaces
- Power BI REST APIs
- PowerShell management
- Service principals
- Deployment automation
- Tabular Editor
- ALM Toolkit
- XMLA read/write workflows
- CI/CD with Azure DevOps or GitHub Actions
- Automated documentation and lineage

**Azure Government considerations:**

| Feature | Gov status | Notes |
|---|---|---|
| PBIP project format | Gov-ready | Desktop/project authoring pattern; Service integration still needs validation. |
| Power BI REST APIs | Verify for Gov | Endpoint, permission, and service principal behavior should be validated in target cloud. |
| PowerShell management | Verify for Gov | Module support and endpoint targeting may differ by cloud. |
| Service principals | Verify for Gov | Requires tenant settings, Entra ID app registration, and admin approval. |
| Git integration in Fabric workspaces | Commercial-focused / Verify for Gov | Do not require in Gov labs unless confirmed. |
| Tabular Editor and ALM Toolkit | Verify for Gov | Local tools; Service connectivity depends on XMLA and tenant policy. |
| GitHub Actions/Azure DevOps CI/CD | Verify for Gov | Depends on network, identity, API endpoint, and customer platform policy. |

**Lab ideas:**

- Save a report as PBIP and review file structure.
- Use source control to track report and model changes.
- Deploy content using a scripted approach where APIs are available.
- Compare ALM Toolkit changes between semantic model versions.
- Create a conceptual CI/CD pipeline with Gov-safe alternate steps.

## Capstone lab: Enterprise-ready Power BI solution

**Goal:** Have learners apply the full lifecycle from model design through deployment and operations.

**Scenario:**

Build an advanced Power BI solution for a fictional enterprise business domain, with a Gov-compatible path and a commercial-enhanced path.

**Required Gov-ready path:**

1. Build an optimized semantic model using star schema principles.
2. Add advanced DAX measures.
3. Build an interactive report with drillthrough, tooltips, bookmarks, and mobile layout.
4. Configure static and dynamic RLS.
5. Publish to the Power BI Service.
6. Configure scheduled refresh and gateway where applicable.
7. Package content as a Power BI App.
8. Add promotion/certification documentation.
9. Review usage, refresh, and support operations.

**Optional commercial-enhanced path:**

1. Add Fabric workspace Git integration if available.
2. Use Direct Lake, OneLake, Lakehouse, or Warehouse features if available.
3. Demonstrate Copilot or AI-assisted authoring if available.
4. Use deployment pipelines if available.
5. Automate deployment using REST APIs and service principals.

## Recommended customer-facing advanced feature shortlist

| Area | Advanced features | Gov delivery note |
|---|---|---|
| Modeling | Star schema, relationships, role-playing dimensions, bridge tables, composite models, aggregations | Most are Gov-ready or tenant-dependent; validate composite/hybrid model choices. |
| DAX | Context transition, advanced `CALCULATE`, time intelligence, calculation groups, dynamic measures | Core DAX is Gov-ready; validate Desktop calculation group authoring, TMDL, XMLA, or external-tool paths. |
| Power Query | Query folding, parameters, custom functions, incremental refresh | Mostly Gov-ready; validate dataflows and incremental refresh licensing. |
| Reporting | Bookmarks, drillthrough, tooltip pages, field parameters, dynamic UX, mobile layouts | Gov-ready; validate personalized visuals and AI visuals. |
| Performance | Performance Analyzer, DAX Studio, VertiPaq optimization, aggregations | Desktop capabilities are Gov-ready; Service model access may require validation. |
| Service | Workspaces, Apps, certified semantic models, gateways, deployment pipelines | Core features Gov-ready; deployment pipelines and App audiences should be validated. |
| Security | Dynamic RLS, OLS, sensitivity labels, tenant governance | RLS Gov-ready; OLS, labels, and Purview integration require validation. |
| DevOps | PBIP, REST APIs, PowerShell, Tabular Editor, ALM Toolkit, Git integration | PBIP Gov-ready; Service automation and Git integration require validation. |
| Fabric/Premium | XMLA, large models, paginated reports, Direct Lake, OneLake, capacity monitoring | Premium features vary; Fabric/Direct Lake/OneLake are commercial-focused unless confirmed in Gov. |

