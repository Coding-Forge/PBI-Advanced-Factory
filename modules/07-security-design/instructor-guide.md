# Instructor Guide

## Module summary

Security design should be taught as layered controls, not as a single RLS checkbox. Clarify which layer controls content access, which layer controls semantic model reuse, and which layer filters data after access is granted.

## Audience and prerequisites

Best fit for semantic model developers, report authors, BI platform owners, Power BI administrators, security reviewers, and data stewards.

Learners should understand workspaces, semantic models, relationships, basic DAX filters, and publishing.

## Learning objectives

- Explain Power BI security layers.
- Create static and dynamic RLS.
- Use security mapping tables.
- Test RLS in Desktop and Service.
- Explain Build permission.
- Review OLS and sensitivity labels as validation-dependent controls.
- Identify Gov-specific restrictions for external sharing, B2B, Purview, and labels.

## Delivery flow

1. Start with a security scenario: different users should see different territories.
2. Explain content access vs. data access.
3. Create static RLS role filters.
4. Create dynamic RLS using a security mapping table.
5. Test as roles in Desktop.
6. Discuss Service role assignment and test-as-role behavior.
7. Explain Build permission using shared semantic model scenarios.
8. Discuss OLS and sensitivity labels as optional validated controls.
9. Review export, sharing, external user, and B2B policy.
10. Close with the security review checklist.

## Feature availability

| Feature | Status | Instructor note |
|---|---|---|
| Static RLS | Gov-ready | Required core lab. |
| Dynamic RLS | Gov-ready | Required core lab; validate identity values. |
| Service role assignment | Gov-ready | Requires Service workspace and permissions. |
| Build permission | Gov-ready | Can be demonstrated conceptually if Service access is unavailable. |
| OLS | Verify for Gov | Keep optional; may require external tools/XMLA/capacity. |
| Sensitivity labels | Verify for Gov | Keep optional; requires Purview/MIP setup. |
| External sharing/B2B | Verify for Gov | Often restricted; discuss through governance review. |

## Environment setup

- Power BI Desktop installed.
- PBIP model/report from earlier modules.
- Security sample files under `Student\Labs\Source\07-security-design\data`.
- Optional: Power BI Service workspace.
- Optional: Tenant with Purview sensitivity labels configured.
- Optional: XMLA-compatible tooling for OLS demonstration.

## Lab facilitation notes

- Use synthetic user principal names from the lab data; do not use real customer identities in committed files.
- Teach learners to validate security with test users before production.
- Emphasize that workspace Admin/Member/Contributor access can bypass intended viewer experiences.
- Clarify that RLS filters data but does not replace workspace/App governance.

## Common issues and fixes

| Issue | Likely cause | Fix |
|---|---|---|
| RLS does not filter in Desktop | Role filter is on wrong table or relationship path is broken | Validate relationship path from security table to facts. |
| Dynamic RLS returns blank | `USERPRINCIPALNAME()` does not match mapping table | Normalize identity values and validate exact UPN format. |
| User sees more data than expected | User has workspace role that bypasses viewer path or belongs to multiple mappings | Review workspace role and security mapping rows. |
| Service testing differs from Desktop | Role assignment or identity differs | Test with actual user assignment in Service. |
| Sensitivity labels unavailable | Purview labels not configured or unsupported in tenant | Mark **Verify for Gov** and use conceptual path. |

## Gov delivery notes

Static and dynamic RLS are Gov-ready core labs. OLS, sensitivity labels, Purview integration, external sharing, and B2B behavior must be validated in the target Azure Government environment and customer policy context.

## Commercial-enhanced options

- Demonstrate sensitivity labels in a configured commercial tenant.
- Demonstrate OLS using XMLA-compatible tooling.
- Demonstrate downstream Build permission with Analyze in Excel or thin reports.


