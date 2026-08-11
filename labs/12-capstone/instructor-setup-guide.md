# Capstone Instructor Setup Guide

## Setup goals

Prepare a training environment where learners can complete the Gov-ready capstone path without requiring commercial-only or unvalidated features.

## Required setup

- Power BI Desktop installed.
- Git installed.
- Workshop repository cloned locally.
- PBIP starter project prepared when available.
- Synthetic workshop data available from prior module lab folders.
- Training workspace available if Service hands-on is planned.
- Test users or synthetic UPN values available for RLS validation.

## Optional setup

Use only when validated:

- Power BI Service workspace for learner publishing.
- On-premises data gateway or gateway demo.
- Deployment pipeline workspaces.
- Fabric workspace.
- Copilot-enabled Power BI/Fabric tenant.
- DAX Studio, Tabular Editor, or ALM Toolkit.
- Azure DevOps or GitHub Actions runner.
- REST API/service principal automation.

## Recommended delivery modes

| Mode | Use when | Notes |
|---|---|---|
| Desktop-only | Service access is limited or Gov tenant features are unvalidated. | Complete modeling, DAX, report UX, RLS, and documentation locally. |
| Instructor-led Service demo | Learners cannot publish but instructor has workspace access. | Instructor demonstrates publishing, refresh, App, and monitoring. |
| Full hands-on Service | Learners have safe training workspace access. | Learners publish and configure refresh/App under supervision. |
| Commercial-enhanced | Commercial tenant features are validated. | Add Fabric, Copilot, deployment pipelines, or automation extensions. |

## Instructor validation before delivery

- [ ] PBIP starter project opens.
- [ ] Data paths resolve.
- [ ] Required synthetic data is present.
- [ ] RLS sample identities are documented.
- [ ] Gov-ready path does not require commercial-only features.
- [ ] Service workspace permissions are validated if used.
- [ ] Optional features are validated or removed from hands-on delivery.
- [ ] Validation rubric is ready.

## Azure Government delivery notes

- Keep Fabric, Direct Lake, OneLake, Copilot, AI visuals, REST API automation, deployment pipelines, XMLA, external tools, and capacity metrics optional unless validated.
- Use the Gov-safe alternate paths documented in prior modules.
- Document any tenant-specific restrictions as part of the capstone evidence.

