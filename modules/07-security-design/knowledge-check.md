# Knowledge Check

## Questions

1. What is the difference between workspace access and RLS?
2. Why is Build permission important?
3. When would static RLS be appropriate?
4. When would dynamic RLS be preferred?
5. Why must `USERPRINCIPALNAME()` values be validated?
6. Why should hidden columns not be treated as a security boundary?
7. What is object-level security used for?
8. Why are sensitivity labels marked **Verify for Gov**?
9. Why is external sharing often more restricted for Gov customers?
10. What should be included in RLS test evidence?

## Answer key

1. Workspace access controls who can access content; RLS filters data visible to users after they have access.
2. Build permission allows users to create downstream content or analyze data from a semantic model, which can expand data access.
3. Static RLS is appropriate for simple, stable roles such as one role per region.
4. Dynamic RLS is preferred when access is user-specific, group-specific, or driven by a mapping table.
5. Dynamic RLS depends on exact identity matching; mismatches can return blanks or incorrect access.
6. Hidden columns improve usability but do not prevent access by users with sufficient model permissions.
7. OLS hides tables or columns from users and can protect sensitive model objects when supported.
8. Sensitivity labels require Purview/MIP configuration and cloud/tenant support that must be validated.
9. Gov tenants often have stricter B2B, external collaboration, compliance, and data handling policies.
10. Include test user/group, expected access, actual result, date, tester, role assignment, and exceptions.

