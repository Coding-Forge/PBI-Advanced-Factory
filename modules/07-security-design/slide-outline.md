# Slide Outline

## 1. Power BI security layers

- Tenant settings
- Workspace roles
- App audiences
- Sharing links
- Build permission
- RLS and OLS
- Sensitivity labels

## 2. Content access vs. data access

- Who can open the report?
- Who can build from the semantic model?
- What data is visible after access is granted?

## 3. Static RLS

- Role filters
- Territory examples
- Testing roles
- Maintenance tradeoffs

## 4. Dynamic RLS

- Security mapping tables
- `USERPRINCIPALNAME()`
- Many-to-many security mapping
- Identity validation

## 5. Service role assignment

- Assigning users and groups
- Testing as role
- Workspace role implications
- App distribution

## 6. Build permission

- Semantic model reuse
- Thin reports
- Analyze in Excel
- Downstream data access risk

## 7. Object-level security

- Hiding tables or columns
- Tooling and capacity considerations
- Validation requirements

## 8. Sensitivity labels and Purview

- Label inheritance
- Export controls
- MIP/Purview setup
- Tenant policy dependency

## 9. Sharing and external users

- Direct sharing
- Apps
- Workspace access
- B2B and guest users
- Gov restrictions

## 10. Security testing

- Test as role
- Test users
- Group membership
- Negative testing
- Documentation

## 11. Azure Government considerations

- RLS is Gov-ready.
- OLS, labels, Purview, external sharing, and B2B require validation.
- Customer policy may be stricter than platform capability.

## 12. Security review checklist

- Access path
- Data filter path
- Export behavior
- Build permission
- Validation evidence

