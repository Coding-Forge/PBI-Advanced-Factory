# Knowledge Check

## Questions

1. Why is PBIP preferred over PBIX as the source of record?
2. What should a pull request review look for in Power BI source changes?
3. Why are Tabular Editor and ALM Toolkit marked **Verify for Gov**?
4. What must be validated before using Power BI REST APIs?
5. Why do service principals require admin approval?
6. Why is Fabric workspace Git integration marked **Commercial-focused / Verify for Gov**?
7. What is one risk of storing secrets in a CI/CD pipeline?
8. Why should CI/CD endpoint behavior be validated for Azure Government?
9. What is a Gov-safe alternate path when automation is unavailable?
10. What deployment evidence should be recorded?

## Answer key

1. PBIP stores report and model source files in a reviewable, git-friendly project structure; PBIX is a packaged binary artifact.
2. Reviewers should inspect model changes, report definitions, parameters, security, measures, data sources, and unintended generated changes.
3. They are external tools and Service connectivity may depend on XMLA, tenant policy, workstation policy, and cloud support.
4. Validate cloud endpoint, permissions, tenant settings, authentication, workspace access, and API availability.
5. Service principals can automate access to tenant resources and therefore require tenant settings, app registration, scoping, and governance approval.
6. Fabric Git integration may be commercial-first or unavailable/delayed in sovereign clouds.
7. Exposed secrets can grant unauthorized access; use approved secret stores and least privilege.
8. Commercial endpoints and sovereign cloud endpoints can differ, and API behavior/availability must match the target tenant.
9. Use PBIP and git for source control, perform reviewed manual deployment, and record deployment evidence.
10. Record commit/version, workspace, deployer, date, validation results, refresh status, and rollback plan.

