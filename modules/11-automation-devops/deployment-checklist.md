# Deployment Checklist

Use this checklist before deploying Power BI content between environments.

## Source control

- [ ] PBIP source is committed.
- [ ] PBIX is not the source of record.
- [ ] Pull request or peer review is complete.
- [ ] Version/tag strategy is documented.
- [ ] Generated or binary artifacts are excluded unless intentionally required.

## Model and report validation

- [ ] Model opens successfully in Power BI Desktop.
- [ ] Report pages load successfully.
- [ ] Measures return expected results.
- [ ] RLS roles are tested.
- [ ] Accessibility review is complete.
- [ ] Performance baseline is acceptable.

## Environment configuration

- [ ] Target workspace is identified.
- [ ] Workspace permissions are reviewed.
- [ ] Data source parameters are set for target environment.
- [ ] Credentials or gateway mappings are documented.
- [ ] Refresh schedule is documented.
- [ ] App distribution plan is documented.

## Automation validation

- [ ] REST API endpoint is validated for target cloud.
- [ ] PowerShell module and endpoint are validated.
- [ ] Service principal is approved and scoped.
- [ ] Secrets or certificates are stored securely.
- [ ] XMLA endpoint requirements are validated if used.
- [ ] CI/CD runner network access is validated.

## Azure Government validation

- [ ] Tenant cloud is documented.
- [ ] API endpoint behavior is validated or marked **Verify for Gov**.
- [ ] Service principal behavior is validated or marked **Verify for Gov**.
- [ ] Fabric Git integration is validated or marked **Commercial-focused / Verify for Gov**.
- [ ] Azure DevOps/GitHub Actions platform policy is validated.
- [ ] Customer-specific deployment restrictions are documented.

## Release evidence

- [ ] Deployment date recorded.
- [ ] Deployed version/commit recorded.
- [ ] Deployer recorded.
- [ ] Smoke test result recorded.
- [ ] Rollback plan documented.

