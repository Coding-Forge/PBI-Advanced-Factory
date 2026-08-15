# Instructor Guide

## Module summary

This module should position DevOps as repeatability and governance, not automation for its own sake. PBIP is the foundation because it makes Power BI artifacts reviewable in git.

## Audience and prerequisites

Best fit for semantic model developers, report authors, BI platform owners, administrators, DevOps engineers, and architects.

Learners should understand PBIP basics, git concepts, Power BI Service deployment, workspaces, and tenant permissions.

## Learning objectives

- Review PBIP structure.
- Track changes with git.
- Explain external-tool workflows.
- Explain API and PowerShell deployment options.
- Explain service principal authentication requirements.
- Explain Fabric Git integration caveats.
- Compare Azure DevOps and GitHub Actions conceptual pipelines.
- Apply a deployment readiness checklist.

## Delivery flow

1. Start with why PBIP is the source of record.
2. Review PBIP folder/file structure.
3. Show git status and diff concepts.
4. Discuss branching and pull request review.
5. Discuss Tabular Editor and ALM Toolkit use cases.
6. Discuss REST API and PowerShell automation.
7. Discuss service principals and tenant settings.
8. Discuss Fabric workspace Git integration where available.
9. Walk through conceptual Azure DevOps and GitHub Actions pipelines.
10. Close with deployment checklist and Gov validation.

## Feature availability

| Feature | Status | Instructor note |
|---|---|---|
| PBIP and git workflow | Gov-ready | Required core path. |
| Tabular Editor/ALM Toolkit | Verify for Gov | Optional only. |
| REST APIs/PowerShell | Verify for Gov | Optional only. |
| Service principals | Verify for Gov | Optional only. |
| Fabric Git integration | Commercial-focused / Verify for Gov | Conceptual unless confirmed. |
| Azure DevOps/GitHub Actions | Verify for Gov | Conceptual unless customer platform and endpoints are validated. |

## Environment setup

- Git installed.
- PBIP project from earlier modules.
- Optional approved external tools.
- Optional Power BI REST API permissions.
- Optional Entra ID app registration/service principal.
- Optional Azure DevOps or GitHub repository.
- Optional Fabric workspace Git integration.

## Lab facilitation notes

- Do not create service principals in customer tenants without explicit approval.
- Do not require external cloud automation for Gov delivery unless approved.
- Keep the required lab path local: PBIP structure and git workflow.
- Present CI/CD as a pattern that must be adapted to customer identity and endpoint constraints.

## Common issues and fixes

| Issue | Likely cause | Fix |
|---|---|---|
| PBIP files not visible | Report saved as PBIX only | Save as Power BI project/PBIP. |
| Git diff is noisy | Binary/generated files included | Confirm repo ignores generated artifacts and PBIX outputs. |
| API call fails | Wrong cloud endpoint, permissions, or tenant setting | Validate cloud endpoint and app/user permissions. |
| Service principal blocked | Tenant setting or workspace access missing | Validate admin approval and workspace role. |
| Fabric Git unavailable | Feature not enabled or unsupported in cloud | Use local PBIP git workflow. |

## Gov delivery notes

PBIP and local git workflows are Gov-ready. REST APIs, PowerShell, service principals, XMLA, external tools, Fabric Git integration, Azure DevOps, and GitHub Actions must be validated for Azure Government delivery.

## Commercial-enhanced options

- Demonstrate Fabric workspace Git integration.
- Demonstrate REST API deployment.
- Demonstrate service principal authentication.
- Run a CI/CD pipeline in a validated environment.

