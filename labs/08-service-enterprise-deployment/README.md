# Module 8 Labs: Power BI Service Enterprise Deployment

## Lab summary

These labs cover Service deployment, refresh, gateways, shared semantic models, thin reports, Apps, optional App audiences, optional deployment pipelines, and endorsement governance.

## Novice-friendly how-to guide

### Publish a report

1. Open the PBIP-authored report in Power BI Desktop.
2. Sign in with the account approved for the training workspace.
3. Select **Home > Publish**.
4. Choose the target workspace.
5. Wait for publishing to complete.
6. Open the report in the Power BI Service.
7. Confirm the report and semantic model are both present.

### Review refresh settings

1. In the Power BI Service, open the workspace.
2. Find the semantic model.
3. Open **Settings**.
4. Review data source credentials, gateway or cloud connection, and scheduled refresh.
5. Document anything that cannot be configured in the training tenant.

## Azure Government readiness

Core workspaces, publishing, refresh, and Apps are generally **Gov-ready**, subject to tenant policy and licensing. App audiences, deployment pipelines, gateways, and cloud connections are **Verify for Gov**.

## Power BI project format

PBIP is the source-controlled format for workshop development. Publish from PBIP-authored content as needed. PBIX files are optional generated artifacts and are not the source of record.

## Prerequisites

- Power BI Service access.
- Training workspace.
- PBIP report/model from prior modules.
- Appropriate permissions for publishing and refresh.
- Optional gateway for gateway-backed refresh.

## Lab 1: Publish report and semantic model

**Objective:** Publish workshop content to a governed workspace.

### Tasks

1. Confirm workspace name and role.
2. Open the PBIP report in Power BI Desktop.
3. Publish to the training workspace.
4. Verify the report and semantic model in the Service.
5. Record owner and workspace details.

### Expected result

The report and semantic model are available in the Service workspace.

## Lab 2: Scheduled refresh

**Objective:** Configure refresh and credentials.

### Tasks

1. Open semantic model settings.
2. Review data source credentials.
3. Configure credentials where supported.
4. Set a refresh schedule.
5. Run refresh and review refresh history.

### Expected result

Refresh configuration and history are documented.

## Lab 3: Gateway-backed refresh

> **Azure Government note:** Gateways are **Verify for Gov**. Validate gateway version, network path, data source support, credentials, and tenant policy.

**Objective:** Understand gateway-backed refresh.

### Tasks when available

1. Identify the gateway cluster.
2. Map the semantic model data source to a gateway data source.
3. Validate credentials.
4. Run refresh.
5. Review gateway troubleshooting signals.

### Alternate path

Review gateway architecture and document required setup without configuring a live gateway.

## Lab 4: Shared semantic model and thin report

**Objective:** Separate model ownership from report creation.

### Tasks

1. Identify the published semantic model.
2. Grant Build permission to an approved learner or group where appropriate.
3. Create a new thin report connected to the shared semantic model.
4. Publish the thin report.
5. Document reuse and governance implications.

### Expected result

Learners understand semantic model reuse and Build permission.

## Lab 5: Power BI App distribution

**Objective:** Package content for consumers.

### Tasks

1. Select workspace content for the App.
2. Configure App name, description, and navigation.
3. Assign consumers or groups.
4. Publish or update the App.
5. Validate consumer experience.

### Expected result

Content is distributed through an App instead of broad workspace access.

## Optional lab: App audiences

> **Azure Government note:** App audiences are **Verify for Gov**. Confirm Service availability and tenant settings before making this hands-on.

**Objective:** Tailor App content by audience.

### Tasks when available

1. Create multiple audiences.
2. Assign different reports or pages to each audience.
3. Add user groups.
4. Validate audience-specific views.

## Optional lab: Deployment pipelines

> **Azure Government note:** Deployment pipelines are **Verify for Gov**. Confirm licensing, capacity, workspace type, and Service availability before making this hands-on.

**Objective:** Understand dev/test/prod promotion.

### Tasks when available

1. Create or open a deployment pipeline.
2. Assign dev, test, and prod workspaces.
3. Compare content between stages.
4. Deploy content to the next stage.
5. Review deployment rules.

## Lab 6: Promoted and certified content governance

**Objective:** Review endorsement requirements.

### Tasks

1. Complete the endorsement governance checklist.
2. Decide whether content is eligible for Promoted.
3. Decide whether content is eligible for Certified.
4. Document ownership, refresh, security, and support evidence.

### Expected result

Learners understand endorsement as a governance process, not just a label.

## Validation checklist

- [ ] Workspace role and ownership documented.
- [ ] Report and semantic model published or demonstrated.
- [ ] Refresh settings reviewed.
- [ ] Gateway requirements documented.
- [ ] Shared semantic model and Build permission reviewed.
- [ ] App distribution reviewed.
- [ ] App audiences marked **Verify for Gov**.
- [ ] Deployment pipelines marked **Verify for Gov**.
- [ ] Endorsement checklist completed.

