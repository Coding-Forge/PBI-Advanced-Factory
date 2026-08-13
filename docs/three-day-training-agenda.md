# Three-Day Power BI Advanced Factory Training Agenda

Use this agenda as a customer-facing starting point for a three-day delivery window. The default schedule assumes delivery from **10:00 AM to 3:00 PM** each day with a **30-minute break from 12:00 PM to 12:30 PM**. The shortened three-day delivery focuses on **Modules 1-7**. Modules 8-12 are listed as optional follow-on topics.

## Customer-facing agenda

### Day 1: Power Query and semantic model foundation

| Time | Format | Topic | Outcome |
|---|---|---|---|
| 10:00-10:15 | Presentation | Welcome, goals, environment check, and PBIP-first workflow | Learners understand the workshop flow, files, and expected deliverables. |
| 10:15-10:45 | Presentation + demo | Lab 03 overview: Power Query staging patterns and source parameters | Learners understand raw, staging, function, error-review, and final load queries. |
| 10:45-11:45 | Lab | Lab 03: Advanced Power Query, Labs 1-3 | Learners create parameters, load monthly files, append staging queries, and preserve source lineage. |
| 11:45-12:00 | Discussion | Data quality strategy | Learners understand why invalid rows should be reviewed before removal. |
| 12:00-12:30 | Break | Midday break |  |
| 12:30-1:15 | Lab | Lab 03: Advanced Power Query, Labs 4-7 | Learners create `fn_CleanText`, `err_OrdersReview`, `FactOrders`, and incremental refresh prep parameters. |
| 1:15-1:45 | Presentation + demo | Lab 01 overview: star schema, grain, keys, and relationship design | Learners understand how the flat file becomes a reusable semantic model. |
| 1:45-2:45 | Lab | Lab 01: Advanced Semantic Modeling, Labs 1-2 | Learners create fact/dimension tables, date tables, and role-playing date relationships. |
| 2:45-3:00 | Review | Day 1 checkpoint and Q&A | Learners confirm data prep and model foundation are ready for Day 2. |

### Day 2: Advanced DAX and interactive report design

| Time | Format | Topic | Outcome |
|---|---|---|---|
| 10:00-10:15 | Review | Day 1 recap and model validation | Learners confirm relationships, date tables, and source queries are working. |
| 10:15-10:45 | Presentation + demo | Lab 02 overview: DAX evaluation context and base measures | Learners understand filter context, row context, and measure branching. |
| 10:45-11:45 | Lab | Lab 02: Advanced DAX, Labs 1-3 | Learners create base measures, `CALCULATE` patterns, and time-intelligence measures. |
| 11:45-12:00 | Discussion | DAX validation habits | Learners practice testing measures in simple visuals before adding complexity. |
| 12:00-12:30 | Break | Midday break |  |
| 12:30-1:15 | Lab | Lab 02: Advanced DAX, Labs 4-8 | Learners review semi-additive patterns, Top N/ranking, calculation groups, dynamic titles, and DAX optimization. |
| 1:15-1:45 | Presentation + demo | Lab 04 overview: report UX patterns | Learners understand drillthrough, tooltips, bookmarks, navigation, and field parameters. |
| 1:45-2:45 | Lab | Lab 04: Report Design and UX, Labs 1-5 | Learners create guided report interactions and field parameters for metric or dimension switching. |
| 2:45-3:00 | Review | Day 2 checkpoint and Q&A | Learners confirm measures and report interactions are ready for optimization and deployment topics. |

### Day 3: Report polish, performance, analytics, and security

| Time | Format | Topic | Outcome |
|---|---|---|---|
| 10:00-10:15 | Review | Day 2 recap and report validation | Learners confirm visuals, measures, and interaction patterns are working. |
| 10:15-10:45 | Lab | Lab 04: Report Design and UX, Labs 6-8 | Learners complete conditional formatting, mobile layout, and accessibility review. |
| 10:45-11:20 | Presentation + demo | Lab 05 overview: Performance Analyzer, model size, and DAX optimization | Learners understand how to capture a baseline before changing the report. |
| 11:20-12:00 | Lab | Lab 05: Performance Optimization | Learners capture performance evidence, review model size, and optimize one DAX or visual pattern. |
| 12:00-12:30 | Break | Midday break |  |
| 12:30-1:00 | Presentation + demo | Lab 06 overview: scenario analysis and AI-aware alternatives | Learners understand what-if parameters, advanced visuals, and Gov-safe fallback patterns. |
| 1:00-1:30 | Lab | Lab 06: Advanced Analytics and AI-Assisted Insights | Learners create a what-if scenario and document optional advanced/AI feature validation. |
| 1:30-2:00 | Presentation + discussion | Lab 07 overview: security design and RLS patterns | Learners understand static RLS, dynamic RLS, testing, and Build permission considerations. |
| 2:00-2:45 | Lab | Lab 07: Security Design, Labs 1-3 | Learners create or review static/dynamic RLS and test roles in Desktop or Service where available. |
| 2:45-3:00 | Closeout | Wrap-up, optional follow-on modules, Q&A, and action items | Customer leaves with a completed Modules 1-7 path, validation notes, and recommended next steps. |

## Optional follow-on topics for a shortened three-day delivery

| Optional module | Topic | When to add it |
|---|---|---|
| Lab 08: Service Enterprise Deployment | Publishing, refresh, Apps, deployment paths | Add when the customer has a training workspace and wants Service deployment practice. |
| Lab 09: Monitoring, Administration, and Governance | Usage metrics, refresh history, tenant settings, operations runbook | Add for administrators, platform owners, or support teams. |
| Lab 10: Premium, Fabric, and Capacity Architecture | Capacity choices, Fabric-aware patterns, Direct Lake concepts | Add for architects, capacity owners, or roadmap discussions. |
| Lab 11: Automation, DevOps, and Lifecycle Management | PBIP, git, external tools, APIs, CI/CD concepts | Add for BI developers or DevOps-oriented teams. |
| Capstone Lab: Capstone | End-to-end solution validation | Add when learners need a final applied exercise or certification-style wrap-up. |

## Instructor customization guide

Copy this file for each customer delivery and adjust the following values before sharing:

| Agenda item to customize | Default | Instructor notes |
|---|---|---|
| Delivery dates | Day 1 / Day 2 / Day 3 | Replace with actual calendar dates when known. |
| Delivery time | 10:00 AM-3:00 PM | Keep the same block or adjust every row consistently. |
| Break | 12:00-12:30 PM | Keep a visible break row in each day. |
| Audience emphasis | Authoring-heavy | Shift time toward governance, architecture, or DevOps if the audience is less hands-on. |
| Tenant readiness | Mixed / validate as needed | Mark any Service, Fabric, Copilot, XMLA, external-tool, or deployment-pipeline content as conceptual unless validated. |
| Lab depth | Guided hands-on | Shorten labs by using starter PBIP files or expand labs by using the full step-by-step HTML pages. |
| Customer-specific examples | Contoso synthetic data | Do not add real customer data unless it has been approved for training use. |

## How to modify the agenda

1. Start with the customer's objective: authoring skills, governance/operations, architecture, or full lifecycle.
2. Keep each day balanced between presentation and lab work.
3. For novice audiences, keep presentation blocks short and move quickly into guided labs.
4. Keep optional or tenant-dependent features labeled **Verify for Gov** or conceptual-only until validated.
5. If a lab runs long, use the next module's starter PBIP rather than letting learners fall behind.
6. If a customer does not have Service access, replace publish/refresh/App activities with screenshots, discussion, or documentation exercises.
7. Before sharing externally, remove internal notes and confirm all times, dates, and prerequisites are correct.

## Reusable blank agenda template

| Time | Format | Topic | Outcome |
|---|---|---|---|
| 10:00-10:15 | Presentation | Welcome and setup |  |
| 10:15-10:45 | Presentation + demo |  |  |
| 10:45-11:45 | Lab |  |  |
| 11:45-12:00 | Discussion |  |  |
| 12:00-12:30 | Break | Midday break |  |
| 12:30-1:15 | Lab |  |  |
| 1:15-1:45 | Presentation + demo |  |  |
| 1:45-2:45 | Lab |  |  |
| 2:45-3:00 | Review | Q&A and checkpoint |  |

