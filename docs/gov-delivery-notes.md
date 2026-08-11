# Azure Government Delivery Notes

Use these notes when delivering to Azure Government, GCC, GCC High, or DoD customers.

## Required delivery position

- PBIP is the source-controlled Power BI format.
- Use synthetic data only.
- Required labs must follow the Gov-ready path.
- Features marked **Verify for Gov** require tenant validation before hands-on delivery.
- Features marked **Commercial-focused** are conceptual unless explicitly validated.

## Features to validate before hands-on use

- App audiences
- Deployment pipelines
- Dataflows and Dataflows Gen2
- DAX Studio, Tabular Editor, ALM Toolkit
- XMLA endpoints
- Large semantic models
- Paginated reports
- Sensitivity labels and Purview
- Activity/audit logs
- Admin monitoring workspace
- Capacity metrics
- Fabric capacity
- Direct Lake
- OneLake, Lakehouse, Warehouse
- Semantic Link
- Copilot and AI visuals
- REST APIs and service principals
- Azure DevOps and GitHub Actions automation

## Gov-safe defaults

- Import-mode semantic model
- Local synthetic CSV data
- Power Query in Desktop
- Core DAX
- Native report visuals
- Static and dynamic RLS
- Manual Service deployment where automation is not validated
- Operations runbook documentation

