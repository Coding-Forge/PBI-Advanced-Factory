# Capstone Learner Step-by-Step Guide

## Objective

Build and validate an enterprise-ready Power BI solution using PBIP source control and the advanced patterns covered across the workshop.

## Step 1: Prepare the PBIP project

1. Open the starter PBIP project when available.
2. Confirm the project is stored in the repository.
3. Confirm Power BI artifacts are not being developed as PBIX-only files.
4. Review required data sources.

## Step 2: Build the semantic model

1. Load the synthetic training data.
2. Create fact and dimension tables.
3. Configure relationships.
4. Hide technical keys where appropriate.
5. Document the model grain.
6. Validate model fields with a simple table visual.

## Step 3: Add advanced DAX

1. Create base measures.
2. Create gross margin and variance measures.
3. Create time-intelligence measures.
4. Create ranking or Top N measures.
5. Create dynamic report text or metric switching.
6. Validate totals by customer, product, territory, and date.

## Step 4: Build the report

1. Create an executive summary page.
2. Create an analyst exploration page.
3. Create a detail drillthrough page.
4. Create a tooltip page.
5. Add bookmarks and navigation buttons.
6. Add conditional formatting.
7. Create mobile layout.
8. Complete accessibility review.

## Step 5: Configure security

1. Load the security mapping data.
2. Create static RLS.
3. Create dynamic RLS using `USERPRINCIPALNAME()`.
4. Test roles in Desktop.
5. Document expected and actual results.

## Step 6: Publish and distribute where available

1. Publish to the training workspace.
2. Review semantic model settings.
3. Configure credentials and refresh where available.
4. Document gateway requirements.
5. Package content as an App where available.
6. Document Build permission and consumer access.

## Step 7: Govern and operate

1. Complete the endorsement governance checklist.
2. Complete the operations runbook.
3. Review usage metrics where available.
4. Review refresh history.
5. Document support ownership.

## Step 8: Add optional extensions only when validated

Optional extensions may include Fabric Git integration, Direct Lake, OneLake, Copilot, AI visuals, deployment pipelines, REST API deployment, service principals, XMLA, or external tools. Mark every optional feature as **Verify for Gov** or **Commercial-focused / Verify for Gov** unless it is validated in the target tenant.

## Step 9: Submit evidence

Submit:

- PBIP source project.
- Completed validation rubric.
- Screenshots or notes for key report pages.
- RLS test evidence.
- Refresh/App/governance evidence where available.
- Operations runbook.
- Gov validation notes.

