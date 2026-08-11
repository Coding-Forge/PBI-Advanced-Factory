# Cross-Cutting Standards

These standards apply to every module, lab, instructor guide, learner guide, and capstone activity in the Power BI Advanced Factory workshop.

## Target learner personas

| Persona | Description | Training emphasis |
|---|---|---|
| Report author | Builds reports and dashboards for business users. | Advanced report UX, drillthrough, tooltips, bookmarks, accessibility, performance-aware visual design. |
| Semantic model developer | Designs reusable semantic models for multiple reports and teams. | Star schema, relationships, DAX, calculation groups, performance optimization, shared semantic models. |
| BI platform owner | Owns workspace design, governance, deployment, and production support. | Workspaces, Apps, deployment pipelines, tenant settings, monitoring, adoption, support runbooks. |
| Data engineer or analytics engineer | Prepares and serves data for Power BI models. | Power Query, query folding, DirectQuery, dataflows, lakehouse or warehouse integration, incremental refresh. |
| Power BI administrator | Manages tenant settings, security, audit, capacity, gateways, and governance. | Admin portal, activity logs, gateway management, capacity metrics, Purview, DLP, security controls. |
| Executive sponsor or product owner | Sponsors BI adoption and needs to understand value, risk, and operating model. | Governance model, content lifecycle, adoption metrics, certified semantic models, production support. |

## Prerequisite knowledge

Learners should already be comfortable with:

- Power BI Desktop basics
- Loading and transforming data
- Creating basic relationships
- Creating basic measures
- Building report pages with visuals, slicers, and filters
- Publishing reports to the Power BI Service
- Basic workspace navigation
- Basic Microsoft Entra ID, Microsoft 365 group, or security group concepts

The workshop should not spend significant time on beginner report-building mechanics unless needed to support an advanced concept.

## Licensing assumptions

Document licensing requirements per module and lab. Use these assumptions unless a customer-specific delivery plan says otherwise:

| Capability area | Baseline assumption | Notes |
|---|---|---|
| Core authoring | Power BI Desktop | Local authoring is required for Desktop labs. |
| Service publishing and sharing | Power BI Pro | Most Service labs require Pro or equivalent capacity-backed access. |
| Advanced Service features | Power BI Premium Per User, Premium capacity, or Fabric capacity | Validate requirements for deployment pipelines, XMLA, large models, paginated reports, and advanced refresh. |
| Fabric features | Fabric capacity or trial where available | Treat as optional and commercial-focused unless validated for the target tenant. |
| Governance and admin labs | Power BI admin, Fabric admin, Microsoft 365 admin, or delegated roles | Use least privilege for customer environments. |
| Purview and sensitivity labels | Microsoft Purview licensing and configuration | Validate MIP label publishing and Power BI integration. |

## Required software versions

Before delivery, record the tested versions used for lab validation:

- Power BI Desktop monthly release
- On-premises data gateway version, if used
- DAX Studio version, if used
- Tabular Editor version, if used
- ALM Toolkit version, if used
- PowerShell modules, if used
- Browser versions supported for Service labs

For Azure Government delivery, validate the Service experience in the target cloud because Desktop features can appear before Service parity is available.

## Required tenant roles and permissions

Each lab must list required roles and permissions before the first step.

Common role requirements:

| Lab area | Typical requirement |
|---|---|
| Publish content | Workspace Contributor, Member, or Admin |
| Configure semantic model refresh | Semantic model owner or workspace role with appropriate rights |
| Configure gateway data source | Gateway admin or data source user, depending on task |
| Assign RLS users | Semantic model security permission or workspace role |
| Create Apps | Workspace Admin or Member |
| Deployment pipelines | Pipeline access plus compatible workspace permissions |
| Tenant settings review | Power BI/Fabric admin role |
| Activity logs | Power BI/Fabric admin or audit log permissions |
| Service principal automation | Entra ID app registration, tenant setting approval, workspace access |
| Sensitivity labels | Purview label policy access and Power BI sensitivity label integration |

Do not require broad admin roles for learner labs unless the module is explicitly administrator-focused.

## Sample data requirements

Training data must be safe, portable, and suitable for both commercial and Azure Government customers.

Requirements:

- Use synthetic or publicly approved data only.
- Do not include customer names, tenant names, subscription IDs, user principal names, secrets, tokens, or environment-specific identifiers.
- Use realistic business domains such as sales, finance, operations, support, or inventory.
- Include enough dimensional complexity to support advanced modeling labs.
- Include enough transaction volume to demonstrate performance considerations without creating impractical lab setup times.
- Include security mapping tables for RLS labs.
- Include intentionally imperfect data for Power Query quality and error-handling labs.
- Keep data source paths relative where possible.

Recommended core dataset:

| Table | Purpose |
|---|---|
| `sales-fact` | Transaction fact table for modeling, DAX, and performance labs. |
| `date-dimension` | Date table for time intelligence and role-playing dimensions. |
| `customer-dimension` | Customer hierarchy, geography, and segmentation. |
| `product-dimension` | Product category, SKU, and margin attributes. |
| `territory-dimension` | Region, district, and account ownership attributes. |
| `sales-targets` | Budget or quota table for variance analysis. |
| `security-user-map` | Dynamic RLS mapping table. |
| `support-tickets` | Secondary fact table for composite model and many-to-many examples. |

## Accessibility standards

Every report lab should include accessibility expectations:

- Meaningful page names
- Descriptive visual titles
- Alt text for important visuals
- Logical tab order
- Sufficient color contrast
- Avoidance of color-only meaning
- Keyboard navigation review
- Consistent layout and spacing
- Clear slicer and filter labels
- Mobile layout review when applicable

Accessibility checks should be part of final validation, not an optional afterthought.

## Azure Government validation process

Use this process before marking a lab Gov-ready:

1. Identify every feature, connector, visual, API, admin setting, and external tool used by the lab.
2. Assign each item a status: **Gov-ready**, **Verify for Gov**, or **Commercial-focused**.
3. Validate required features in the target Azure Government tenant or document why validation is pending.
4. Confirm required licensing, capacity, and tenant settings.
5. Confirm data residency and compliance requirements.
6. Confirm gateway, network, identity, and firewall requirements.
7. Confirm whether external tools are allowed by the customer workstation policy.
8. Provide a Gov-safe alternate path for any required feature that is not available.
9. Document validation date, tenant cloud, and validation owner in the lab notes.

## Commercial-only feature callout format

Use this format when a feature should not be required for Azure Government learners:

```markdown
> **Azure Government note:** This feature is marked **Commercial-focused**. It may be unavailable or delayed in Azure Government clouds. Treat this section as conceptual unless the customer tenant has been validated. Use the Gov-safe alternate path for hands-on delivery.
```

Use this format when availability is uncertain:

```markdown
> **Azure Government note:** This feature is marked **Verify for Gov**. Confirm cloud availability, licensing, capacity, tenant settings, and customer policy before making this a required lab step.
```

## Lab validation checklist

Every lab must be validated before it is marked complete:

- [ ] Starter files open successfully.
- [ ] Data source paths resolve or setup instructions explain how to remap them.
- [ ] Learner steps can be completed from a clean starter state.
- [ ] Expected outputs match screenshots and validation notes.
- [ ] Required roles, licenses, and tenant settings are documented.
- [ ] Azure Government readiness label is present.
- [ ] Commercial-only or parity-sensitive features have a callout.
- [ ] Gov-safe alternate path exists when needed.
- [ ] Troubleshooting notes cover likely errors.
- [ ] Cleanup steps are included when the lab changes tenant resources.
- [ ] Solution files match the final expected state.

## Instructor delivery notes template

Use this structure for `instructor-guide.md`:

```markdown
# Instructor Guide

## Module summary

## Audience and prerequisites

## Learning objectives

## Feature availability

| Feature | Status | Delivery note |
|---|---|---|

## Environment setup

## Demo flow

## Lab facilitation notes

## Common issues and fixes

## Discussion prompts

## Knowledge check answer guide

## Gov delivery notes

## Commercial-enhanced options
```

## Learner handout template

Use this structure for `learner-guide.md`:

```markdown
# Learner Guide

## What you will learn

## Scenario

## Prerequisites

## Azure Government readiness

## Lab files

## Tasks

### Task 1: ...

### Task 2: ...

## Validate your work

## Troubleshooting

## Optional extension

## Clean up
```

## Answer key and expected outcome template

Use this structure for `knowledge-check.md` or `answer-key.md`:

```markdown
# Answer Key and Expected Outcomes

## Knowledge check answers

## Lab validation

| Task | Expected result | How to verify |
|---|---|---|

## Completed solution notes

## Common acceptable variations

## Common mistakes

## Remediation guidance
```

