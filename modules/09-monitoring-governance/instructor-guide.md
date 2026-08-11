# Instructor Guide

## Module summary

Monitoring and governance close the loop after deployment. Teach this module from the perspective of a support owner who needs to know whether content is used, healthy, secure, and supportable.

## Audience and prerequisites

Best fit for BI platform owners, Power BI administrators, support teams, semantic model owners, and governance leads.

Learners should understand workspaces, semantic models, refresh, gateways, Apps, sharing, and tenant settings.

## Learning objectives

- Review usage metrics and adoption indicators.
- Troubleshoot refresh failures.
- Review tenant settings that affect risk and distribution.
- Inspect gateway status and mapping.
- Explain activity/audit logs and admin monitoring.
- Explain capacity metrics.
- Explain Purview and DLP integration considerations.
- Create a production operations runbook.

## Delivery flow

1. Start with a production support scenario.
2. Review usage metrics for a report or App.
3. Troubleshoot refresh history and credentials.
4. Review gateway monitoring and data source mappings.
5. Review tenant settings that affect export, sharing, Apps, and certification.
6. Discuss activity logs and audit evidence.
7. Discuss admin monitoring workspace and capacity metrics where available.
8. Discuss Purview and DLP integration where available.
9. Build a support and operations runbook.

## Feature availability

| Feature | Status | Instructor note |
|---|---|---|
| Usage metrics | Gov-ready | Required if workspace has content and permissions. |
| Refresh history | Gov-ready | Required for semantic model troubleshooting. |
| Tenant settings | Gov-ready / Admin-required | Can be conceptual if admin role unavailable. |
| Gateway monitoring | Verify for Gov | Keep hands-on only if gateway access exists. |
| Activity/audit logs | Verify for Gov | Requires admin/audit permissions. |
| Admin monitoring workspace | Verify for Gov | Keep optional. |
| Capacity metrics app | Verify for Gov | Keep optional. |
| Purview and DLP | Verify for Gov | Keep optional or conceptual. |

## Environment setup

- Power BI Service workspace with report and semantic model.
- Access to refresh history.
- Optional Power BI/Fabric admin role.
- Optional gateway admin or data source access.
- Optional capacity admin access.
- Optional Purview/MIP labels and DLP policy access.

## Lab facilitation notes

- Do not require learners to change production tenant settings.
- Use read-only review for admin settings unless explicitly approved.
- If admin access is unavailable, use screenshots or conceptual walkthroughs.
- Capture operational decisions in the runbook template.
- Emphasize that Gov customer policy may be stricter than feature availability.

## Common issues and fixes

| Issue | Likely cause | Fix |
|---|---|---|
| Usage metrics unavailable | Permission or tenant setting limitation | Confirm workspace role and tenant policy. |
| Refresh history lacks details | Connector/gateway/source limitation | Review semantic model settings and gateway logs where available. |
| Gateway appears offline | Service stopped, network issue, or gateway version problem | Validate gateway host, service status, network, and version. |
| Audit logs inaccessible | Missing admin/audit role or disabled audit configuration | Mark **Verify for Gov** and use conceptual path. |
| Capacity metrics unavailable | No capacity access or app unsupported | Validate capacity type, role, and cloud support. |

## Gov delivery notes

Usage metrics and refresh history are generally Gov-ready, but tenant policy and permissions still matter. Activity logs, audit logs, admin monitoring workspace, capacity metrics, Purview, and DLP must be validated in the target Azure Government environment.

## Commercial-enhanced options

- Demonstrate activity log queries.
- Demonstrate admin monitoring workspace.
- Demonstrate capacity metrics app.
- Demonstrate Purview sensitivity label and DLP policy review.

