# Capstone Lab: Enterprise-Ready Power BI Solution

## Lab summary

The capstone combines the workshop modules into one end-to-end Power BI delivery. Learners build, secure, publish, package, govern, and monitor an enterprise-ready solution using a Gov-ready path, with optional commercial-enhanced extensions when tenant features are validated.

## Scenario narrative

Contoso Advanced Manufacturing has grown from departmental reporting to an enterprise analytics program. The sales operations team needs a trusted Power BI solution that supports executive review, analyst exploration, operational detail, secured regional access, Service deployment, App distribution, refresh operations, and governance review.

The customer audience includes commercial and Azure Government stakeholders. The core solution must work without requiring Fabric, Copilot, AI visuals, deployment pipelines, or commercial-only features. Where validated, the instructor may add optional commercial-enhanced extensions.

## Power BI project format

All Power BI development must be performed as PBIP projects. PBIP is the source-controlled format for this workshop. PBIX files can be generated from PBIP later if a packaged file is needed, but PBIX is not the source of record.

## Novice-friendly how-to guide

### Work through the capstone safely

1. Start from the capstone starter PBIP or the completed solution from the previous module.
2. Complete one capability at a time: model, DAX, report UX, security, deployment, governance, and monitoring.
3. Save after each major milestone.
4. Validate each capability with the rubric before moving to the next one.
5. Record evidence as you go instead of waiting until the end.

### Package capstone evidence

1. Include the PBIP source project.
2. Include screenshots or notes for model relationships, report pages, RLS tests, refresh/deployment settings, and governance decisions.
3. Complete the validation rubric.
4. Mark optional unvalidated features as **Verify for Gov** or conceptual-only.

## Required Gov-ready learner path

1. Build an optimized semantic model using star schema principles.
2. Add advanced DAX measures.
3. Build an interactive report with drillthrough, tooltips, bookmarks, conditional formatting, and mobile layout.
4. Configure static and dynamic RLS.
5. Publish to the Power BI Service where a training workspace is available.
6. Configure scheduled refresh and gateway requirements where applicable.
7. Package content as a Power BI App where Service access is available.
8. Complete promotion/certification governance documentation.
9. Review usage, refresh, monitoring, and support operations.
10. Complete the validation rubric.

## Optional commercial-enhanced learner path

Only use these extensions when the target tenant and customer policy have been validated:

1. Add Fabric workspace Git integration.
2. Use Direct Lake, OneLake, Lakehouse, or Warehouse features.
3. Demonstrate Copilot or AI-assisted authoring.
4. Use deployment pipelines.
5. Automate deployment using REST APIs and service principals.
6. Use DAX Studio, Tabular Editor, ALM Toolkit, XMLA, or capacity metrics against Service-hosted models.

## Capstone tasks

### Task 1: Build the semantic model

- Import or connect to approved synthetic workshop data.
- Create fact and dimension tables.
- Configure relationships.
- Hide technical fields.
- Document model grain.
- Document Gov-sensitive features as **Gov-ready**, **Verify for Gov**, or **Commercial-focused**.

### Task 2: Add advanced DAX

- Create base measures.
- Create time-intelligence measures.
- Create variance measures.
- Create ranking or Top N measures.
- Create dynamic title or measure-switching logic.
- Validate totals at multiple grains.

### Task 3: Build the report experience

- Create an executive summary page.
- Create an analyst exploration page.
- Create a detail drillthrough page.
- Create a report page tooltip.
- Add bookmarks and buttons.
- Add conditional formatting.
- Create a mobile layout.
- Complete accessibility checks.

### Task 4: Configure security

- Import or create a security mapping table.
- Create static RLS.
- Create dynamic RLS using `USERPRINCIPALNAME()`.
- Test roles in Desktop.
- Test roles in Service where available.
- Document Build permission behavior.

### Task 5: Publish and distribute

- Publish from PBIP-authored content.
- Configure semantic model credentials.
- Configure scheduled refresh where available.
- Document gateway requirements.
- Create or review a Power BI App.
- Document App consumers and workspace roles.

### Task 6: Govern and operate

- Complete endorsement governance checklist.
- Complete operations runbook.
- Review usage metrics where available.
- Review refresh history.
- Document support owner, business owner, and escalation path.

### Task 7: Optional enhanced extensions

- Add optional Fabric/Git/Copilot/AI/API/automation features only after validation.
- Document every optional feature with availability status and fallback path.

## Validation checklist

- [ ] PBIP source project is used.
- [ ] Semantic model follows star schema principles.
- [ ] Advanced DAX measures are validated.
- [ ] Report includes drillthrough, tooltip, bookmark, and mobile layout.
- [ ] Accessibility review is complete.
- [ ] Static and dynamic RLS are configured and tested.
- [ ] Service publishing is completed or instructor-demoed.
- [ ] Refresh and gateway requirements are documented.
- [ ] App packaging is completed or instructor-demoed.
- [ ] Endorsement checklist is complete.
- [ ] Operations runbook is complete.
- [ ] Monitoring and support tasks are documented.
- [ ] Optional commercial-enhanced features are clearly marked and validated.

