# Security Review Checklist

Use this checklist before marking a Power BI security design ready for delivery or production.

## Access model

- [ ] Workspace roles are documented.
- [ ] App audiences are documented.
- [ ] Direct sharing is documented or intentionally disabled.
- [ ] Build permission is documented.
- [ ] External sharing policy is documented.
- [ ] Guest/B2B behavior is validated where applicable.

## RLS design

- [ ] Security requirement is documented in business terms.
- [ ] Static and dynamic roles are named clearly.
- [ ] Security mapping table has one clear grain.
- [ ] `USERPRINCIPALNAME()` values match identity source values.
- [ ] Relationship path from security table to facts is validated.
- [ ] Users with multiple mappings are handled intentionally.
- [ ] Executive/all-access role is documented.
- [ ] Negative testing is completed.

## OLS and sensitive fields

- [ ] Sensitive tables and columns are identified.
- [ ] OLS need is evaluated.
- [ ] OLS tooling and capacity requirements are validated.
- [ ] Sensitive fields are removed from the model when not needed.
- [ ] Hidden fields are not treated as a security boundary.

## Sensitivity labels and export

- [ ] Sensitivity label requirements are documented.
- [ ] Purview/MIP label availability is validated.
- [ ] Export settings are documented.
- [ ] Analyze in Excel behavior is reviewed.
- [ ] PowerPoint/PDF export behavior is reviewed.
- [ ] Data loss prevention requirements are documented.

## Azure Government validation

- [ ] Tenant cloud is documented.
- [ ] RLS tested in Desktop.
- [ ] RLS tested in Service where available.
- [ ] OLS marked **Verify for Gov** unless validated.
- [ ] Sensitivity labels marked **Verify for Gov** unless validated.
- [ ] Purview integration marked **Verify for Gov** unless validated.
- [ ] External sharing/B2B marked **Verify for Gov** unless validated.
- [ ] Customer policy restrictions are documented.

## Evidence

- [ ] Test users or test groups are listed.
- [ ] Expected access matrix is attached.
- [ ] Actual test results are recorded.
- [ ] Exceptions and accepted risks are documented.
- [ ] Owner for future access changes is identified.

