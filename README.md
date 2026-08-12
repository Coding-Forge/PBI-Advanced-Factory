# Power BI Advanced Factory

Advanced Power BI training and lab material for customers using Power BI Desktop, the Power BI Service, and enterprise deployment patterns.

## Audience

This workshop is intended for report authors, semantic model developers, BI platform owners, and administrators who already understand the basics of Power BI and need to move into advanced modeling, performance, governance, deployment, and lifecycle management.

## Azure Government note

Some Power BI, Microsoft Fabric, Copilot, AI, Git integration, and preview features reach Azure Government clouds later than commercial cloud or may not be available in all sovereign environments. Training material in this repo should explicitly mark each feature as one of:

- **Available in Azure Government** - suitable for Gov customer labs.
- **Commercial only or not yet confirmed for Azure Government** - explain conceptually, but do not require it in Gov labs.
- **Verify in tenant** - availability may depend on licensing, tenant settings, region, capacity, preview status, or admin configuration.

For customer delivery, validate feature availability in the target tenant before finalizing labs.

## Core documents

- [Workshop Data](data\README.md)
- [HTML Lab Site](Student\Labs\Web\index.html)
- [Advanced Power BI Training Outline](docs\advanced-powerbi-training-outline.md)
- [Deliverable Checklist](docs\deliverable-checklist.md)
- [Authoring Standards](docs\authoring-standards.md)
- [Cross-Cutting Standards](docs\cross-cutting-standards.md)
- [Delivery Paths](docs\delivery-paths.md)
- [Three-Day Training Agenda](docs\three-day-training-agenda.md)
- [Customer Training Datasheet](docs\customer-training-datasheet.md)
- [Azure Government Readiness Review](docs\azure-government-readiness-review.md)
- [Instructor Deck](docs\instructor-deck.md)
- [Learner Workbook](docs\learner-workbook.md)
- [Lab Manual](docs\lab-manual.md)
- [Environment Setup Guide](docs\environment-setup-guide.md)
- [Troubleshooting Guide](docs\troubleshooting-guide.md)
- [Knowledge Checks and Answer Keys](docs\knowledge-checks-and-answer-keys.md)
- [Gov Delivery Notes](docs\gov-delivery-notes.md)
- [Commercial Delivery Notes](docs\commercial-delivery-notes.md)
- [Labs README](labs\README.md)

## Modules

- [Module 1: Advanced Semantic Modeling](modules\01-advanced-semantic-modeling\README.md)
- [Module 2: Advanced DAX](modules\02-advanced-dax\README.md)
- [Module 3: Advanced Power Query and Data Transformation](modules\03-advanced-power-query\README.md)
- [Module 4: Advanced Report Design and User Experience](modules\04-report-design-ux\README.md)
- [Module 5: Performance Optimization](modules\05-performance-optimization\README.md)
- [Module 6: Advanced Analytics and AI-Assisted Insights](modules\06-advanced-analytics-ai\README.md)
- [Module 7: Security Design](modules\07-security-design\README.md)
- [Module 8: Power BI Service Enterprise Deployment](modules\08-service-enterprise-deployment\README.md)
- [Module 9: Monitoring, Administration, and Governance](modules\09-monitoring-governance\README.md)
- [Module 10: Premium, Fabric, and Capacity-Aware Architecture](modules\10-premium-fabric-capacity\README.md)
- [Module 11: Automation, DevOps, and Lifecycle Management](modules\11-automation-devops\README.md)
- [Capstone Lab: Enterprise-Ready Power BI Solution](labs\12-capstone\README.md)

## Local Power BI development

Use `pbi-local\` for ongoing PBIP solution development. PBIP projects in that folder can be promoted into `labs\<module>\starter\` or `labs\<module>\solution\` when they are ready for learner use.

## HTML lab delivery

The student-facing HTML lab site is in `Student\Labs\Web`. Open `Student\Labs\Web\index.html` to launch the lab menu. Customer branding is controlled by `Student\Labs\Web\scripts\delivery-config.js`; see `Student\Labs\Web\BRANDING.md`.
