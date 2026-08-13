# Deliverable Checklist

Use this checklist to track creation of training and lab material. Keep Azure Government applicability explicit in every module.

## Repository setup

- [x] Create repo README with workshop purpose and audience
- [x] Create training outline
- [x] Create deliverable checklist
- [x] Create lab folder structure
- [x] Add contribution or authoring standards
- [x] Add naming conventions for modules, labs, datasets, and screenshots
- [x] Add a feature availability legend for Commercial, Gov-ready, Verify for Gov, and Commercial-focused features
- [x] Add a source list for official Microsoft documentation references

## Cross-cutting standards

- [x] Define target learner personas
- [x] Define prerequisite knowledge
- [x] Define licensing assumptions
- [x] Define required software versions
- [x] Define required tenant roles and permissions
- [x] Define sample data requirements
- [x] Define accessibility standards
- [x] Define Azure Government validation process
- [x] Define commercial-only feature callout format
- [x] Define lab validation checklist
- [x] Define instructor delivery notes template
- [x] Define learner handout template
- [x] Define answer key or expected outcome template

## Lab 01: Advanced semantic modeling

- [x] Write instructor guide
- [x] Write learner guide
- [x] Create slide outline
- [x] Create sample dataset
- [ ] Create starter PBIP
- [ ] Create completed PBIP
- [x] Create lab: star schema refactor
- [x] Create lab: role-playing dimensions
- [x] Create lab: many-to-many and bridge table pattern
- [x] Create lab: composite model or DirectQuery comparison
- [x] Create lab: calculation groups
- [x] Create lab: field parameters
- [x] Add Gov notes for calculation groups, hybrid tables, large models, and composite models
- [x] Add knowledge check questions
- [x] Add troubleshooting notes

## Lab 02: Advanced DAX

- [x] Write instructor guide
- [x] Write learner guide
- [x] Create slide outline
- [x] Create DAX pattern reference
- [x] Create lab: row context vs. filter context
- [x] Create lab: context transition and `CALCULATE`
- [x] Create lab: advanced time intelligence
- [x] Create lab: semi-additive measures
- [x] Create lab: dynamic Top N and ranking
- [x] Create lab: dynamic titles and measure switching
- [x] Create lab: DAX optimization
- [x] Add Gov notes for DAX Studio and external tooling
- [x] Add knowledge check questions
- [x] Add answer key

## Lab 03: Advanced Power Query and data transformation

- [x] Write instructor guide
- [x] Write learner guide
- [x] Create slide outline
- [x] Create source files for folder-combine lab
- [x] Create lab: query folding
- [x] Create lab: parameters and source switching
- [x] Create lab: custom functions
- [x] Create lab: staged query architecture
- [x] Create lab: data quality and error handling
- [x] Create lab: incremental refresh preparation
- [x] Add Gov notes for dataflows, Dataflows Gen2, and connector availability
- [x] Add knowledge check questions
- [x] Add troubleshooting notes

## Lab 04: Advanced report design and user experience

- [x] Write instructor guide
- [x] Write learner guide
- [x] Create slide outline
- [x] Create report UX design standards
- [x] Create lab: drillthrough
- [x] Create lab: report page tooltips
- [x] Create lab: bookmarks and buttons
- [x] Create lab: dynamic navigation
- [x] Create lab: conditional formatting
- [x] Create lab: mobile layout
- [x] Create lab: accessibility review
- [x] Add Gov notes for personalized visuals and AI visuals
- [x] Add knowledge check questions
- [ ] Add finished report screenshots

## Lab 05: Performance optimization

- [x] Write instructor guide
- [x] Write learner guide
- [x] Create slide outline
- [ ] Create intentionally slow starter model
- [ ] Create optimized completed model
- [x] Create lab: Performance Analyzer
- [x] Create lab: reduce model size and cardinality
- [x] Create lab: DAX Studio query timings
- [x] Create lab: visual optimization
- [x] Create lab: aggregation table
- [x] Create lab: incremental refresh policy
- [x] Add Gov notes for DAX Studio, VertiPaq Analyzer, capacity metrics, and incremental refresh
- [x] Add knowledge check questions
- [x] Add performance benchmark targets

## Lab 06: Advanced analytics and AI-assisted insights

- [x] Write instructor guide
- [x] Write learner guide
- [x] Create slide outline
- [x] Create lab: what-if parameters
- [x] Create lab: decomposition tree where available
- [x] Create lab: forecasting where available
- [x] Create lab: key influencers where available
- [x] Create optional lab: Python or R visuals
- [x] Create optional lab: Azure Machine Learning integration
- [x] Create optional conceptual section: Copilot in Power BI/Fabric
- [x] Add Gov notes for AI visuals, Copilot, Python/R visuals, and Azure ML integration
- [x] Add Gov-safe alternate lab path
- [x] Add knowledge check questions

## Lab 07: Security design

- [x] Write instructor guide
- [x] Write learner guide
- [x] Create slide outline
- [x] Create security matrix sample data
- [x] Create lab: static RLS
- [x] Create lab: dynamic RLS
- [x] Create lab: testing roles in Desktop and Service
- [x] Create lab: Build permission behavior
- [x] Create optional lab: object-level security
- [x] Create optional lab: sensitivity labels
- [x] Add Gov notes for OLS, sensitivity labels, Purview, external sharing, and B2B limitations
- [x] Add knowledge check questions
- [x] Add security review checklist

## Lab 08: Power BI Service enterprise deployment

- [x] Write instructor guide
- [x] Write learner guide
- [x] Create slide outline
- [x] Create workspace setup instructions
- [x] Create lab: publish report and semantic model
- [x] Create lab: scheduled refresh
- [x] Create lab: gateway-backed refresh
- [x] Create lab: shared semantic model and thin report
- [x] Create lab: Power BI App distribution
- [x] Create optional lab: App audiences
- [x] Create optional lab: deployment pipelines
- [x] Create governance checklist for promoted and certified content
- [x] Add Gov notes for deployment pipelines, App audiences, gateways, and cloud connections
- [x] Add knowledge check questions

## Lab 09: Monitoring, administration, and governance

- [x] Write instructor guide
- [x] Write learner guide
- [x] Create slide outline
- [x] Create lab: usage metrics
- [x] Create lab: refresh troubleshooting
- [x] Create lab: tenant setting review
- [x] Create lab: gateway monitoring
- [x] Create optional lab: activity logs
- [x] Create optional lab: admin monitoring workspace
- [x] Create optional lab: capacity metrics app
- [x] Create optional lab: Purview and DLP review
- [x] Add Gov notes for audit logs, admin monitoring workspace, capacity metrics, Purview, and DLP
- [x] Add knowledge check questions
- [x] Add operations runbook template

## Lab 10: Premium, Fabric, and capacity-aware architecture

- [x] Write instructor guide
- [x] Write learner guide
- [x] Create slide outline
- [x] Create licensing and capacity comparison table
- [x] Create lab: XMLA endpoint connection where available
- [x] Create lab: paginated report where available
- [x] Create lab: large semantic model settings where available
- [x] Create optional commercial lab: Direct Lake
- [x] Create optional commercial lab: OneLake/Lakehouse/Warehouse integration
- [x] Create optional commercial lab: Semantic Link
- [x] Create lab or demo: capacity metrics and throttling concepts
- [x] Add Gov notes for Fabric capacity, Direct Lake, OneLake, XMLA, paginated reports, autoscale, and capacity metrics
- [x] Add Gov-safe alternate architecture path
- [x] Add knowledge check questions

## Lab 11: Automation, DevOps, and lifecycle management

- [x] Write instructor guide
- [x] Write learner guide
- [x] Create slide outline
- [x] Create lab: PBIP file structure
- [x] Create lab: source control workflow
- [x] Create lab: Tabular Editor workflow where available
- [x] Create lab: ALM Toolkit model comparison where available
- [x] Create optional lab: Power BI REST API deployment
- [x] Create optional lab: PowerShell administration
- [x] Create optional lab: service principal authentication
- [x] Create optional commercial lab: Fabric workspace Git integration
- [x] Create conceptual CI/CD pipeline for Azure DevOps
- [x] Create conceptual CI/CD pipeline for GitHub Actions
- [x] Add Gov notes for REST APIs, service principals, XMLA, Git integration, Azure DevOps, and GitHub Actions
- [x] Add knowledge check questions
- [x] Add deployment checklist

## Capstone lab

- [x] Write scenario narrative
- [x] Create Gov-ready learner path
- [x] Create commercial-enhanced learner path
- [ ] Create starter files
- [ ] Create completed solution files
- [x] Create instructor setup guide
- [x] Create learner step-by-step guide
- [x] Create validation rubric
- [x] Include optimized semantic model
- [x] Include advanced DAX
- [x] Include report interactivity
- [x] Include RLS
- [x] Include Service publishing
- [x] Include refresh and gateway setup
- [x] Include App packaging
- [x] Include governance endorsement
- [x] Include monitoring and support tasks
- [x] Include optional Fabric/Git/Copilot extensions only where available

## Azure Government readiness review

- [x] Review every module for commercial-only or parity-sensitive features
- [x] Mark each feature with Gov-ready, Verify for Gov, or Commercial-focused
- [x] Create Gov-safe alternate steps for every required commercial-only feature
- [x] Validate labs in a Gov tenant or document validation gap
- [ ] Validate connectors against customer-approved data sources
- [ ] Validate gateway setup and identity requirements
- [ ] Validate external tool policy for DAX Studio, Tabular Editor, and ALM Toolkit
- [ ] Validate sensitivity label and Purview availability
- [ ] Validate Fabric feature availability before including Fabric labs
- [ ] Validate Copilot/AI feature availability before including AI labs
- [ ] Validate REST API and service principal availability before automation labs

## Final packaging

- [x] Create instructor deck
- [x] Create learner workbook
- [x] Create lab manual
- [ ] Create solution files
- [x] Create datasets and data dictionaries
- [x] Create environment setup guide
- [x] Create troubleshooting guide
- [x] Create knowledge checks
- [x] Create answer keys
- [x] Create capstone rubric
- [x] Create Gov delivery notes
- [x] Create commercial delivery notes
- [ ] Run end-to-end lab validation
- [ ] Tag initial release

