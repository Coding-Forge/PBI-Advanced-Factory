# Module 9 Labs: Monitoring, Administration, and Governance

## Lab summary

These labs teach operational monitoring and governance practices for deployed Power BI content.

## Azure Government readiness

Usage metrics and refresh history are generally **Gov-ready**, subject to permissions and tenant policy. Activity logs, audit logs, admin monitoring workspace, capacity metrics, Purview, and DLP are **Verify for Gov**.

## Prerequisites

- Power BI Service workspace with deployed content.
- Access to semantic model refresh history.
- Optional Power BI/Fabric admin role.
- Optional gateway admin access.
- Optional capacity admin access.
- Optional Purview/DLP access.

## Lab 1: Usage metrics

**Objective:** Interpret report adoption and usage.

### Tasks

1. Open usage metrics for a report or App.
2. Review views and unique viewers.
3. Identify high-use and low-use pages.
4. Document adoption observations.
5. Identify one follow-up action.

### Expected result

Learners can interpret usage data and connect it to support or adoption actions.

## Lab 2: Refresh troubleshooting

**Objective:** Diagnose semantic model refresh issues.

### Tasks

1. Open semantic model refresh history.
2. Review the most recent refresh status.
3. Inspect failure details if present.
4. Review data source credentials.
5. Review gateway mapping if applicable.
6. Document likely cause and next action.

### Expected result

Learners can follow a structured refresh troubleshooting process.

## Lab 3: Tenant setting review

**Objective:** Understand tenant settings that affect governance.

### Tasks

1. Review sharing-related settings.
2. Review export-related settings.
3. Review publish-to-web controls.
4. Review certification and endorsement settings.
5. Review external user settings.
6. Document settings that require customer policy decisions.

### Expected result

Learners understand how tenant settings influence risk and user experience.

## Lab 4: Gateway monitoring

> **Azure Government note:** Gateway monitoring is **Verify for Gov**. Validate gateway access, network path, version, data source, and tenant policy.

**Objective:** Review gateway health and mappings.

### Tasks when available

1. Review gateway cluster status.
2. Review data source mappings.
3. Review credential configuration.
4. Review gateway version.
5. Document support owner and escalation path.

### Alternate path

Use the operations runbook template to document gateway requirements conceptually.

## Optional lab: Activity logs

> **Azure Government note:** Activity logs and audit logs are **Verify for Gov**. Validate admin permissions, audit configuration, and cloud support.

**Objective:** Understand audit evidence.

### Tasks when available

1. Identify an activity to investigate.
2. Query or review activity log data.
3. Identify actor, action, workspace, item, and timestamp.
4. Document how logs support governance.

## Optional lab: Admin monitoring workspace

> **Azure Government note:** Admin monitoring workspace is **Verify for Gov**. Validate availability in the target tenant.

**Objective:** Review tenant-level monitoring.

### Tasks when available

1. Open the admin monitoring workspace.
2. Review available reports.
3. Identify tenant-level adoption or governance indicators.
4. Document follow-up actions.

## Optional lab: Capacity metrics app

> **Azure Government note:** Capacity metrics app is **Verify for Gov**. Validate capacity type, role, app availability, and telemetry.

**Objective:** Interpret capacity health.

### Tasks when available

1. Open the capacity metrics app.
2. Review CPU and memory indicators.
3. Review refresh workload.
4. Identify throttling or overload signals.
5. Document capacity follow-up actions.

## Optional lab: Purview and DLP review

> **Azure Government note:** Purview and DLP are **Verify for Gov**. Validate M365/Purview cloud, labels, licensing, policies, and tenant configuration.

**Objective:** Understand compliance integration.

### Tasks when available

1. Review sensitivity label availability.
2. Review DLP policy scope.
3. Review export and sharing behavior.
4. Document compliance requirements.

## Lab 5: Operations runbook

**Objective:** Create a support-ready runbook.

### Tasks

1. Complete content inventory.
2. Document data sources and refresh.
3. Document access and governance.
4. Document monitoring cadence.
5. Document incident response paths.
6. Add Azure Government validation notes.

### Expected result

Learners produce a draft operations runbook for the deployed solution.

## Validation checklist

- [ ] Usage metrics reviewed or conceptually documented.
- [ ] Refresh troubleshooting process documented.
- [ ] Tenant settings review completed or conceptually documented.
- [ ] Gateway monitoring marked **Verify for Gov**.
- [ ] Activity/audit logs marked **Verify for Gov**.
- [ ] Admin monitoring workspace marked **Verify for Gov**.
- [ ] Capacity metrics marked **Verify for Gov**.
- [ ] Purview and DLP marked **Verify for Gov**.
- [ ] Operations runbook draft completed.

