# Module 7: Security Design

## Module summary

This module teaches Power BI security patterns that protect data while preserving usability. It covers static and dynamic row-level security, security mapping tables, role testing, Build permission, object-level security, sensitivity labels, export controls, and sharing risk.

## Learning objectives

By the end of this module, learners will be able to:

- Explain the difference between workspace access, App access, sharing, Build permission, RLS, and OLS.
- Implement static row-level security.
- Implement dynamic row-level security using user principal name.
- Build a security mapping table.
- Test roles in Power BI Desktop and the Power BI Service.
- Explain Build permission and downstream semantic model access.
- Identify when object-level security is appropriate.
- Explain sensitivity labels, export controls, external sharing, B2B, and Purview considerations.
- Identify Azure Government security validation requirements.

## Feature availability

| Feature | Status | Delivery note |
|---|---|---|
| Static RLS | Gov-ready | Core Power BI security capability. |
| Dynamic RLS | Gov-ready | Validate identity format, Entra ID sync, and guest-user behavior. |
| Role testing in Desktop | Gov-ready | Core Desktop capability. |
| Role assignment in Service | Gov-ready | Requires workspace/model permissions. |
| Build permission | Gov-ready | Validate tenant and workspace governance model. |
| OLS | Verify for Gov | Often requires XMLA-compatible tooling and compatible capacity. |
| Sensitivity labels | Verify for Gov | Requires Microsoft Purview Information Protection configuration and cloud support. |
| External sharing/B2B | Verify for Gov | Often restricted by GCC/GCC High/DoD policy, B2B configuration, and data handling rules. |

## Module artifacts

- [Instructor Guide](instructor-guide.md)
- [Learner Guide](learner-guide.md)
- [Slide Outline](slide-outline.md)
- [Teaching Deck](assets\security-design.pptx)
- [Security Review Checklist](security-review-checklist.md)
- [Knowledge Check](knowledge-check.md)
- [Module labs](..\..\Student\Labs\Source\07-security-design\README.md)



