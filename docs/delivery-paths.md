# Delivery Paths

This workshop can be delivered as a complete progressive program or split into focused tracks. Use this guide to help instructors and stakeholders choose the right delivery model for the customer audience.

## Recommended progressive flow

The full workshop is designed to build one Power BI solution over time. Modules 1-5 are the core authoring sequence, Modules 7-9 add enterprise security and operations, Module 11 formalizes lifecycle management, and the capstone ties the pieces together.

```text
Power Query / Data Prep
        ↓
Semantic Model
        ↓
DAX
        ↓
Report UX
        ↓
Performance + Security
        ↓
Service Deployment
        ↓
Monitoring / Governance
        ↓
DevOps / Lifecycle
        ↓
Capstone
```

## Module dependency model

| Module | Relationship to other modules |
|---|---|
| **1. Advanced Semantic Modeling** | Foundation. Other technical labs should build from this model. |
| **2. Advanced DAX** | Builds directly on Module 1's semantic model. |
| **3. Advanced Power Query** | Can stand alone, but ideally feeds the model-building story from Module 1. |
| **4. Report Design and UX** | Builds on Modules 1 and 2: model plus measures become report pages. |
| **5. Performance Optimization** | Builds on Modules 1-4 because learners tune the model, DAX, and report UX. |
| **6. Advanced Analytics and AI** | Builds on the report/model, but can be delivered as a standalone feature module. |
| **7. Security Design** | Builds on the semantic model from Module 1 and supports later Service governance. |
| **8. Service Enterprise Deployment** | Builds on the completed report/model from prior modules. |
| **9. Monitoring, Administration, and Governance** | Builds on Module 8 deployment; needs something published to monitor. |
| **10. Premium, Fabric, and Capacity Architecture** | Mostly conceptual/architecture; can stand alone, but references performance and deployment topics. |
| **11. Automation, DevOps, and Lifecycle Management** | Builds on PBIP artifacts created throughout the workshop. |
| **Capstone** | Pulls everything together end to end. |

## Suggested delivery tracks

| Track | Modules | Best for |
|---|---|---|
| **Authoring track** | 1, 2, 3, 4, 5 | Report authors, semantic model developers, analysts |
| **Governance and operations track** | 7, 8, 9 | BI platform owners, admins, support teams, governance leads |
| **Architecture track** | 10 | Architects, platform owners, technical decision makers |
| **DevOps track** | 11 | BI developers, DevOps engineers, platform owners |
| **Applied capstone** | 12 | Mixed teams ready to apply the full lifecycle |

## Delivery recommendations

### Full progressive workshop

Use this when the customer wants an end-to-end advanced Power BI program.

Recommended sequence:

1. Module 3: Advanced Power Query
2. Module 1: Advanced Semantic Modeling
3. Module 2: Advanced DAX
4. Module 4: Report Design and UX
5. Module 5: Performance Optimization
6. Module 7: Security Design
7. Module 8: Service Enterprise Deployment
8. Module 9: Monitoring, Administration, and Governance
9. Module 11: Automation, DevOps, and Lifecycle Management
10. Module 10: Premium, Fabric, and Capacity-Aware Architecture
11. Capstone

Module 6 can be inserted after Module 4 or delivered as an optional feature module depending on customer interest and tenant availability.

### Short authoring workshop

Use this when the customer mainly needs better report/model development practices.

Recommended modules:

1. Module 3: Advanced Power Query
2. Module 1: Advanced Semantic Modeling
3. Module 2: Advanced DAX
4. Module 4: Report Design and UX
5. Module 5: Performance Optimization

### Governance and deployment workshop

Use this when the customer already builds reports but needs enterprise deployment discipline.

Recommended modules:

1. Module 7: Security Design
2. Module 8: Service Enterprise Deployment
3. Module 9: Monitoring, Administration, and Governance
4. Module 11: Automation, DevOps, and Lifecycle Management

### Architecture briefing

Use this for leadership, architects, platform owners, or customers making licensing/capacity decisions.

Recommended modules:

1. Module 10: Premium, Fabric, and Capacity-Aware Architecture
2. Selected content from Module 8: Service Enterprise Deployment
3. Selected content from Module 9: Monitoring, Administration, and Governance
4. Selected content from Module 11: Automation, DevOps, and Lifecycle Management

### Azure Government delivery

For Azure Government customers, use the Gov-ready path by default:

- Keep PBIP as the source of record.
- Use CSV data from the repository raw URLs.
- Use Import-mode models unless DirectQuery/connectors are validated.
- Keep Fabric, Direct Lake, OneLake, Copilot, AI visuals, REST APIs, service principals, deployment pipelines, XMLA, and external tools optional until validated.
- Use the documented Gov-safe alternate paths for unvalidated features.

## Local PBIP development area

Use `pbi-local\` for ongoing local Power BI solution development. This folder is intended for work-in-progress PBIP projects and related local development artifacts before selected starter/solution artifacts are promoted into the appropriate `labs\<module>\starter\` or `labs\<module>\solution\` folders.

Recommended pattern:

```text
pbi-local\
  PBI-AdvancedFactory.Working\
  PBI-AdvancedFactory.Starter\
  PBI-AdvancedFactory.Solution\
```

When an artifact is ready for learners, copy or promote it from `pbi-local\` into the relevant lab folder.

