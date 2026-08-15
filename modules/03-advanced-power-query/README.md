# Module 3: Advanced Power Query and Data Transformation

## Module summary

This module teaches learners how to build reusable, performant, and governable Power Query transformations. It focuses on staging patterns, query folding, parameters, custom functions, folder-combine patterns, data quality handling, and incremental refresh preparation.

## Learning objectives

By the end of this module, learners will be able to:

- Explain when Power Query logic should be staged, referenced, or loaded.
- Identify query folding and explain why it matters.
- Use parameters for environment switching and reusable logic.
- Build and invoke custom functions.
- Combine files from a folder using a repeatable pattern.
- Add data quality checks and explicit error handling.
- Prepare a fact table for incremental refresh.
- Identify Azure Government considerations for connectors, dataflows, and Dataflows Gen2.

## Feature availability

| Feature | Status | Delivery note |
|---|---|---|
| Power Query in Desktop | Gov-ready | Core local authoring capability. |
| Folder-combine pattern | Gov-ready | Uses local files in the core lab path. |
| Parameters and custom functions | Gov-ready | Core Power Query features. |
| Query folding | Gov-ready / Verify for source | Power Query capability, but folding depends on connector and source system. |
| Incremental refresh preparation | Verify for Gov | Desktop preparation is Gov-ready; Service policy application depends on license, workspace, and tenant support. |
| Cloud dataflows | Verify for Gov | Validate Power BI Service/Fabric availability and tenant settings. |
| Dataflows Gen2 | Commercial-focused / Verify for Gov | Fabric-related; do not require in Gov labs unless validated. |
| Connectors | Verify for Gov | Connector availability can vary by cloud, gateway, network, and customer policy. |

## Module artifacts

- [Instructor Guide](instructor-guide.md)
- [Learner Guide](learner-guide.md)
- [Slide Outline](slide-outline.md)
- [Teaching Deck](assets\advanced-power-query.pptx)
- [Knowledge Check](knowledge-check.md)
- [Troubleshooting Notes](troubleshooting.md)
- [Module labs](..\..\Student\Labs\Source\03-advanced-power-query\README.md)



