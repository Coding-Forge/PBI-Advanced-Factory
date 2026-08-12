# Three-Day Power BI Advanced Factory Training Agenda

Use this agenda as a customer-facing starting point for a three-day delivery window. The default schedule assumes delivery from **10:00 AM to 3:00 PM** each day with a **30-minute break from 12:00 PM to 12:30 PM**.

## Customer-facing agenda

### Day 1: Data preparation and semantic model foundation

| Time | Format | Topic | Outcome |
|---|---|---|---|
| 10:00-10:15 | Presentation | Welcome, goals, environment check, and PBIP-first workflow | Learners understand the workshop flow, files, and expected deliverables. |
| 10:15-10:45 | Presentation + demo | Power Query staging patterns and source parameters | Learners understand raw, staging, function, error-review, and final load queries. |
| 10:45-11:45 | Lab | Module 3: Advanced Power Query, Labs 1-3 | Learners create parameters, load monthly files, append staging queries, and preserve source lineage. |
| 11:45-12:00 | Discussion | Data quality strategy | Learners understand why invalid rows should be reviewed before removal. |
| 12:00-12:30 | Break | Midday break |  |
| 12:30-1:15 | Lab | Module 3: Advanced Power Query, Labs 4-7 | Learners create `fn_CleanText`, `err_OrdersReview`, `FactOrders`, and incremental refresh prep parameters. |
| 1:15-1:45 | Presentation + demo | Star schema, grain, keys, and relationship design | Learners understand how the flat file becomes a reusable semantic model. |
| 1:45-2:45 | Lab | Module 1: Advanced Semantic Modeling, Labs 1-2 | Learners create fact/dimension tables, date tables, and role-playing date relationships. |
| 2:45-3:00 | Review | Day 1 checkpoint and Q&A | Learners confirm data prep and model foundation are ready for Day 2. |

### Day 2: Advanced DAX and interactive report design

| Time | Format | Topic | Outcome |
|---|---|---|---|
| 10:00-10:15 | Review | Day 1 recap and model validation | Learners confirm relationships, date tables, and source queries are working. |
| 10:15-10:45 | Presentation + demo | DAX evaluation context and base measures | Learners understand filter context, row context, and measure branching. |
| 10:45-11:45 | Lab | Module 2: Advanced DAX, Labs 1-3 | Learners create base measures, `CALCULATE` patterns, and time-intelligence measures. |
| 11:45-12:00 | Discussion | DAX validation habits | Learners practice testing measures in simple visuals before adding complexity. |
| 12:00-12:30 | Break | Midday break |  |
| 12:30-1:15 | Lab | Module 2: Advanced DAX, Labs 4-8 | Learners review semi-additive patterns, Top N/ranking, calculation groups, dynamic titles, and DAX optimization. |
| 1:15-1:45 | Presentation + demo | Report UX patterns | Learners understand drillthrough, tooltips, bookmarks, navigation, and field parameters. |
| 1:45-2:45 | Lab | Module 4: Report Design and UX, Labs 1-5 | Learners create guided report interactions and field parameters for metric or dimension switching. |
| 2:45-3:00 | Review | Day 2 checkpoint and Q&A | Learners confirm measures and report interactions are ready for optimization and deployment topics. |

### Day 3: Performance, security, deployment, and operations

| Time | Format | Topic | Outcome |
|---|---|---|---|
| 10:00-10:15 | Review | Day 2 recap and report validation | Learners confirm visuals, measures, and interaction patterns are working. |
| 10:15-10:45 | Presentation + demo | Performance Analyzer, model size, and DAX optimization | Learners understand how to capture a baseline before changing the report. |
| 10:45-11:30 | Lab | Module 5: Performance Optimization, Labs 1-4 | Learners capture performance evidence, review model size, and optimize one DAX or visual pattern. |
| 11:30-12:00 | Presentation + discussion | Security design and RLS patterns | Learners understand static RLS, dynamic RLS, and Build permission considerations. |
| 12:00-12:30 | Break | Midday break |  |
| 12:30-1:15 | Lab | Module 7: Security Design, Labs 1-3 | Learners create or review static/dynamic RLS and test roles in Desktop or Service where available. |
| 1:15-1:45 | Presentation + demo | Publishing, refresh, Apps, and governed distribution | Learners understand the Service deployment path and tenant-dependent checks. |
| 1:45-2:30 | Lab | Modules 8-9: Service Deployment and Monitoring/Governance | Learners publish where available, review refresh settings, and document ownership/support notes. |
| 2:30-2:50 | Discussion | PBIP lifecycle and next steps | Learners understand how PBIP, source control, and deployment checklists support production readiness. |
| 2:50-3:00 | Closeout | Wrap-up, Q&A, and action items | Customer leaves with a completed lab path, validation notes, and recommended next steps. |

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

