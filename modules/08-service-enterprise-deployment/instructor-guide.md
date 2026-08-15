# Instructor Guide

## Module summary

This module shifts from authoring to operational deployment. Emphasize that enterprise Power BI success depends on clear ownership, workspace design, refresh reliability, permissions, and a controlled promotion path.

## Audience and prerequisites

Best fit for BI platform owners, report authors, semantic model developers, Power BI administrators, and support teams.

Learners should understand publishing, workspaces, semantic models, reports, basic permissions, and refresh concepts.

## Learning objectives

- Explain workspace role responsibilities.
- Publish content from PBIP-authored projects.
- Configure refresh and credentials.
- Explain gateway-backed refresh.
- Create shared semantic model and thin report patterns.
- Package and distribute a Power BI App.
- Review App audiences and deployment pipelines where available.
- Apply endorsement governance.
- Identify Gov validation requirements.

## Delivery flow

1. Introduce enterprise workspace patterns.
2. Compare Admin, Member, Contributor, and Viewer roles.
3. Publish report and semantic model to a development workspace.
4. Configure credentials and scheduled refresh.
5. Explain gateway-backed refresh and cloud connections.
6. Create or discuss a thin report connected to a shared semantic model.
7. Package report content as an App.
8. Discuss App audiences where available.
9. Discuss deployment pipelines where available.
10. Review promoted/certified governance checklist.

## Feature availability

| Feature | Status | Instructor note |
|---|---|---|
| Workspaces and roles | Gov-ready | Required core path. |
| Publishing and refresh | Gov-ready / Verify for source | Required where Service access is available. |
| Gateways | Verify for Gov | Requires network and policy validation. |
| Apps | Gov-ready | Required where Service access is available. |
| App audiences | Verify for Gov | Keep optional unless validated. |
| Deployment pipelines | Verify for Gov | Keep optional unless validated. |
| Cloud connections | Verify for Gov | Connector-specific validation needed. |
| Endorsement | Gov-ready / Verify for Gov | Requires tenant settings and process. |

## Environment setup

- Power BI Service access.
- Workspace where learners can publish or instructor demo workspace.
- PBIP project from earlier modules.
- Optional gateway or documented gateway demo environment.
- Optional deployment pipeline-capable workspace/capacity.
- Optional tenant endorsement settings for certification.

## Lab facilitation notes

- If learners cannot publish to a shared tenant, run Service labs as instructor demos.
- Do not ask learners to change production tenant settings.
- Use a dedicated training workspace naming convention.
- Avoid real customer data in Service demos.
- Validate Gov tenant feature availability before delivery.

## Common issues and fixes

| Issue | Likely cause | Fix |
|---|---|---|
| Publish fails | User lacks workspace permission or license | Confirm Pro/capacity access and workspace role. |
| Refresh fails | Credentials, gateway, privacy, or path mismatch | Review data source settings and gateway mapping. |
| App update not visible | App not republished after changes | Update and republish the App. |
| Thin report user cannot connect | Missing Build permission | Grant Build through semantic model permissions or App audience where appropriate. |
| Deployment pipeline unavailable | License/capacity/cloud limitation | Mark **Verify for Gov** and use conceptual path. |

## Gov delivery notes

Core workspaces, roles, publishing, Apps, and refresh are generally Gov-ready, but customer tenant restrictions still matter. App audiences, deployment pipelines, gateways, and cloud connections must be validated in the target Azure Government environment.

## Commercial-enhanced options

- Demonstrate App audiences.
- Demonstrate deployment pipelines across dev/test/prod workspaces.
- Demonstrate certification workflow.
- Demonstrate cloud connection reuse.

