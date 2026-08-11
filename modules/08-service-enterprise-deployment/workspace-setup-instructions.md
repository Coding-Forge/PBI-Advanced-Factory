# Workspace Setup Instructions

Use these instructions for training workspaces. Do not use production customer workspaces for hands-on labs unless explicitly approved.

## Recommended workspace pattern

| Workspace | Purpose |
|---|---|
| `PBI-AdvancedFactory-Dev` | Learner or instructor publishing workspace. |
| `PBI-AdvancedFactory-Test` | Optional validation workspace. |
| `PBI-AdvancedFactory-Prod` | Optional production-like App distribution workspace. |

For smaller deliveries, use a single training workspace and explain the dev/test/prod pattern conceptually.

## Required permissions

| Task | Minimum typical role |
|---|---|
| Publish report and semantic model | Contributor |
| Configure semantic model refresh | Contributor, Member, or Admin depending on ownership |
| Create or update App | Member or Admin |
| Manage workspace access | Admin |
| Certify content | User with certification permission under tenant governance |
| Deployment pipelines | Pipeline access plus required workspace permissions |

## Setup steps

1. Create a dedicated training workspace.
2. Assign instructor as Admin.
3. Assign learners as Contributor only if hands-on publishing is allowed.
4. Confirm workspace license/capacity requirements.
5. Confirm whether tenant allows Apps, App audiences, endorsement, and deployment pipelines.
6. Confirm gateway or data source requirements.
7. Confirm that all lab data is synthetic.

## Azure Government validation

- Validate tenant restrictions on sharing and external users.
- Validate App audience availability.
- Validate gateway and network path.
- Validate cloud connection availability.
- Validate deployment pipeline availability.
- Validate certification/endorsement tenant settings.

