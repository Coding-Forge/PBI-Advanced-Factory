# Operations Runbook Template

Use this template for production or production-like Power BI content.

## Content inventory

| Item | Value |
|---|---|
| Workspace | |
| App name | |
| Report name | |
| Semantic model name | |
| PBIP source location | |
| Business owner | |
| Technical owner | |
| Support contact | |

## Data sources

| Source | Type | Gateway required | Credential owner | Refresh dependency |
|---|---|---|---|---|
| | | | | |

## Refresh operations

| Item | Value |
|---|---|
| Refresh schedule | |
| Expected duration | |
| Failure notification recipients | |
| Retry process | |
| Escalation path | |

## Access and governance

| Area | Notes |
|---|---|
| Workspace roles | |
| App audiences or users | |
| Build permission | |
| RLS/OLS | |
| Sensitivity labels | |
| Export restrictions | |
| External sharing | |

## Monitoring process

| Check | Frequency | Owner | Evidence |
|---|---|---|---|
| Usage metrics review | | | |
| Refresh history review | | | |
| Gateway health review | | | |
| Access review | | | |
| Performance review | | | |

## Incident response

| Scenario | First checks | Escalation |
|---|---|---|
| Refresh failure | Credentials, gateway, source availability, privacy settings | Semantic model owner, gateway admin, source owner |
| Report slow | Usage metrics, Performance Analyzer, capacity metrics if available | Report owner, model owner, capacity admin |
| Access issue | Workspace role, App audience, RLS role, group membership | Workspace admin, security owner |
| Data quality issue | Source data, Power Query steps, refresh history | Source owner, model owner |

## Azure Government validation

- [ ] Tenant cloud documented.
- [ ] Activity/audit log access validated or marked **Verify for Gov**.
- [ ] Admin monitoring workspace validated or marked **Verify for Gov**.
- [ ] Capacity metrics validated or marked **Verify for Gov**.
- [ ] Purview and DLP validated or marked **Verify for Gov**.
- [ ] Customer-specific policy restrictions documented.

