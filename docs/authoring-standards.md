# Authoring Standards

Use these standards when creating training modules, labs, datasets, screenshots, and instructor materials for the Power BI Advanced Factory workshop.

## Content principles

- Write for experienced Power BI users who are moving into advanced authoring, governance, operations, and lifecycle management.
- Separate required Gov-ready steps from optional commercial-enhanced steps.
- Prefer hands-on labs over conceptual-only content when a feature is available in the target environment.
- Keep labs deterministic: every lab should have a starter state, expected result, validation steps, and troubleshooting notes.
- Do not require preview, commercial-only, or Fabric-specific features in the core Gov-ready path unless the customer tenant has been validated.
- Build Power BI deliverables as PBIP projects first so report and semantic model source files can be reviewed and checked into git. Treat PBIX files as generated/exportable artifacts that can be created from PBIP later when needed.

## Azure Government feature availability labels

Every module and lab must identify feature availability using this legend:

| Label | Use when |
|---|---|
| **Gov-ready** | The feature is appropriate for Azure Government delivery, subject to normal licensing, tenant settings, and customer policy. |
| **Verify for Gov** | The feature may vary by cloud, region, license, capacity, tenant setting, preview status, or admin configuration. |
| **Commercial-focused** | The feature is commercial-only, preview-first in commercial, or commonly delayed/unavailable in Azure Government. Provide a conceptual discussion or Gov-safe alternate path. |

When in doubt, use **Verify for Gov** and include a validation note.

## Required module structure

Each module should include:

- `README.md` - module overview, learning objectives, feature availability, and estimated flow without time commitments.
- `instructor-guide.md` - delivery notes, setup requirements, talking points, demo guidance, and troubleshooting.
- `learner-guide.md` - learner-facing explanation and lab steps.
- `knowledge-check.md` - review questions and applied prompts.
- `assets\` - images, diagrams, and supporting files.
- `labs\` or linked lab folder - starter files, solution files, data, and validation steps.

## Required lab structure

Each lab should include:

- Lab objective
- Scenario
- Prerequisites
- Azure Government readiness note
- Required roles, licenses, and tenant settings
- Starter files
- Step-by-step tasks
- Expected outcomes
- Validation steps
- Troubleshooting notes
- Cleanup steps, when applicable
- Optional commercial-enhanced extension, when applicable

## Naming conventions

### Folders

Use two-digit numeric prefixes for ordered modules and labs:

```text
01-advanced-semantic-modeling
02-advanced-dax
03-advanced-power-query
```

Use lowercase folder names with hyphens. Avoid spaces.

### Markdown files

Use lowercase names with hyphens:

```text
instructor-guide.md
learner-guide.md
knowledge-check.md
troubleshooting.md
```

### Power BI files

Use PBIP as the source-controlled format for all Power BI development. Use descriptive names and identify starter vs. completed project folders:

```text
advanced-modeling-starter.pbip
advanced-modeling-solution.pbip
```

Do not check in PBIX as the primary source format. If a PBIX is needed for delivery convenience, generate it from the PBIP after the source project is complete and document that it is an output artifact.

### Data files

Use lowercase names with clear business purpose:

```text
sales-fact.csv
customer-dimension.csv
product-dimension.csv
security-user-map.csv
```

### Screenshots

Use ordered names that map to lab steps:

```text
step-01-model-view.png
step-02-relationship-settings.png
step-03-rls-test-result.png
```

## Commercial-only and parity-sensitive callouts

Use this standard callout when a topic may not be available in Azure Government:

```markdown
> **Azure Government note:** This feature is marked **Verify for Gov**. Confirm availability, licensing, tenant settings, and capacity requirements in the customer tenant before making this a required lab step.
```

Use this standard callout for commercial-focused features:

```markdown
> **Azure Government note:** This feature is marked **Commercial-focused**. Cover it conceptually or use the Gov-safe alternate path instead of requiring it in the lab.
```

## Official documentation source list

Prefer official Microsoft Learn and product documentation as source material. Track references in module or lab content when a feature is version-sensitive.

Recommended source categories:

- Power BI Desktop documentation
- Power BI Service documentation
- Power BI guidance documentation
- Power BI enterprise deployment guidance
- Power BI security documentation
- Power BI REST API documentation
- Power BI PowerShell documentation
- Microsoft Fabric documentation
- Microsoft Learn training paths
- Microsoft Purview Information Protection documentation
- Azure Government documentation
- Power BI release plan and feature availability documentation

## Review checklist for every module

- [ ] Learning objectives are clear.
- [ ] Required prerequisites are listed.
- [ ] Gov-ready, Verify for Gov, and Commercial-focused features are labeled.
- [ ] Required labs have a Gov-ready path.
- [ ] Commercial-enhanced labs are optional.
- [ ] Screenshots do not contain customer data.
- [ ] Sample data is synthetic or approved for training use.
- [ ] Instructor notes include setup and troubleshooting guidance.
- [ ] Learner steps include expected outcomes.
- [ ] Any tenant, license, capacity, or admin dependency is documented.

