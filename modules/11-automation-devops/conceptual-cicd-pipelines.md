# Conceptual CI/CD Pipelines

These are conceptual patterns. Do not use them as production pipelines without validating identity, cloud endpoints, tenant settings, secrets handling, network access, and customer policy.

## Azure DevOps conceptual pipeline

```yaml
trigger:
  branches:
    include:
      - main

stages:
  - stage: Validate
    jobs:
      - job: ValidatePBIP
        steps:
          - script: echo "Validate PBIP structure and required files"

  - stage: DeployDev
    dependsOn: Validate
    jobs:
      - job: Deploy
        steps:
          - script: echo "Authenticate to Power BI using approved identity"
          - script: echo "Deploy report and semantic model to Dev workspace"
          - script: echo "Record deployment evidence"
```

## GitHub Actions conceptual pipeline

```yaml
name: Power BI Deployment

on:
  push:
    branches:
      - main

jobs:
  validate:
    runs-on: windows-latest
    steps:
      - uses: actions/checkout@v4
      - name: Validate PBIP structure
        run: echo "Validate required PBIP files"

  deploy-dev:
    needs: validate
    runs-on: windows-latest
    steps:
      - uses: actions/checkout@v4
      - name: Authenticate
        run: echo "Use approved identity and cloud endpoint"
      - name: Deploy
        run: echo "Deploy to Power BI workspace"
```

## Required validation before implementation

- Power BI cloud endpoint for the tenant.
- API availability in the tenant cloud.
- Authentication approach.
- Service principal tenant setting.
- Workspace permissions.
- Secret or certificate storage.
- Runner network access.
- Audit and deployment evidence requirements.
- Rollback process.

## Gov-safe alternate path

If API automation is not approved or not available:

1. Use PBIP and git for source control.
2. Use pull requests for review.
3. Deploy manually from Power BI Desktop or Service.
4. Complete the deployment checklist.
5. Record commit ID, workspace, deployer, and validation evidence.

