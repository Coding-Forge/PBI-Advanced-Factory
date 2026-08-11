# Troubleshooting Guide

Use this guide as the workshop-level troubleshooting index.

## Common setup issues

| Issue | Likely cause | Resolution |
|---|---|---|
| PBIP not available | Older Power BI Desktop or feature disabled | Update Desktop and confirm project format support. |
| Data files do not load | Local path mismatch | Remap data source path to the lab `data` folder. |
| Git diff is noisy | Generated/binary artifacts included | Keep PBIP source as record and avoid checking in PBIX as primary source. |

## Module troubleshooting references

- [Module 1 troubleshooting](..\modules\01-advanced-semantic-modeling\troubleshooting.md)
- [Module 3 troubleshooting](..\modules\03-advanced-power-query\troubleshooting.md)

## Service troubleshooting

| Issue | Likely cause | Resolution |
|---|---|---|
| Publish fails | Missing license or workspace permission | Confirm Pro/capacity access and workspace role. |
| Refresh fails | Credentials, gateway, privacy, source, or path issue | Review semantic model settings and refresh history. |
| RLS behaves unexpectedly | Relationship path, UPN mismatch, or role assignment issue | Test in Desktop and Service with expected identities. |
| App changes not visible | App was not updated after workspace changes | Update and republish the App. |

## Azure Government troubleshooting

If a feature is missing or behaves differently:

1. Confirm the tenant cloud.
2. Confirm licensing and capacity.
3. Confirm tenant settings.
4. Confirm feature availability in the target cloud.
5. Use the Gov-safe alternate path when availability is not confirmed.

