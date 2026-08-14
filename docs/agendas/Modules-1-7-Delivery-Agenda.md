# Advanced Power BI — Modules 1–7 Delivery Agenda

**Delivery window:** 10:00 AM – 3:00 PM daily, with a 30-minute break at 12:00–12:30 PM
**Scope:** Modules 1–7 (Advanced Semantic Modeling → Security Design)
**Format:** 3-day standard workshop (also adaptable to a compressed single day — see notes below)

This agenda sequences Modules 1–7 across three delivery days. Each day balances short presentation/demo blocks with hands-on lab time, and ends with a checkpoint so learners leave with a working, validated artifact before moving to the next day.

---

## Day 1 — Power Query & Semantic Model Foundation

**Modules covered:** Module 3 (Advanced Power Query), Module 1 (Advanced Semantic Modeling)

| Time | Format | Topic | Outcome |
|---|---|---|---|
| 10:00–10:15 | Presentation | Welcome, goals, environment check, PBIP-first workflow | Learners understand the workshop flow, files, and expected deliverables. |
| 10:15–10:45 | Presentation + demo | Module 3 overview: Power Query staging patterns and source parameters | Learners understand raw, staging, function, error-review, and final load queries. |
| 10:45–11:45 | Lab | Module 3 exercises 1–3: Advanced Power Query | Learners create parameters, load monthly files, append staging queries, and preserve source lineage. |
| 11:45–12:00 | Discussion | Data quality strategy | Learners understand why invalid rows should be reviewed before removal. |
| **12:00–12:30** | **Break** | **Midday break** | |
| 12:30–1:15 | Lab | Module 3 exercises 4–7: Advanced Power Query | Learners create a cleansing function, an error-review query, a fact load query, and incremental refresh prep parameters. |
| 1:15–1:45 | Presentation + demo | Module 1 overview: star schema, grain, keys, relationship design | Learners understand how the flat file becomes a reusable semantic model. |
| 1:45–2:45 | Lab | Module 1 exercises 1–2: Advanced Semantic Modeling | Learners create fact/dimension tables, date tables, and role-playing date relationships. |
| 2:45–3:00 | Review | Day 1 checkpoint and Q&A | Learners confirm data prep and model foundation are ready for Day 2. |

---

## Day 2 — Advanced DAX & Interactive Report Design

**Modules covered:** Module 2 (Advanced DAX), Module 4 (Report Design & UX)

| Time | Format | Topic | Outcome |
|---|---|---|---|
| 10:00–10:15 | Review | Day 1 recap and model validation | Learners confirm relationships, date tables, and source queries are working. |
| 10:15–10:45 | Presentation + demo | Module 2 overview: DAX evaluation context and base measures | Learners understand filter context, row context, and measure branching. |
| 10:45–11:45 | Lab | Module 2 exercises 1–3: Advanced DAX | Learners create base measures, `CALCULATE` patterns, and time-intelligence measures. |
| 11:45–12:00 | Discussion | DAX validation habits | Learners practice testing measures in simple visuals before adding complexity. |
| **12:00–12:30** | **Break** | **Midday break** | |
| 12:30–1:15 | Lab | Module 2 exercises 4–8: Advanced DAX | Learners build semi-additive patterns, Top N/ranking, calculation groups, dynamic titles, and optimization passes. |
| 1:15–1:45 | Presentation + demo | Module 4 overview: report UX patterns | Learners understand drillthrough, tooltips, bookmarks, navigation, and field parameters. |
| 1:45–2:45 | Lab | Module 4 exercises 1–5: Report Design & UX | Learners build guided report interactions and field parameters for metric/dimension switching. |
| 2:45–3:00 | Review | Day 2 checkpoint and Q&A | Learners confirm measures and report interactions are ready for optimization, analytics, and security topics. |

---

## Day 3 — Report Polish, Performance, Analytics & Security

**Modules covered:** Module 4 (cont'd), Module 5 (Performance Optimization), Module 6 (Advanced Analytics & AI), Module 7 (Security Design)

| Time | Format | Topic | Outcome |
|---|---|---|---|
| 10:00–10:15 | Review | Day 2 recap and report validation | Learners confirm visuals, measures, and interaction patterns are working. |
| 10:15–10:45 | Lab | Module 4 exercises 6–8: Report Design & UX | Learners complete conditional formatting, mobile layout, and an accessibility review. |
| 10:45–11:20 | Presentation + demo | Module 5 overview: Performance Analyzer, model size, DAX optimization | Learners understand how to capture a performance baseline before changing the report. |
| 11:20–12:00 | Lab | Module 5: Performance Optimization | Learners capture performance evidence, review model size, and optimize one DAX or visual pattern. |
| **12:00–12:30** | **Break** | **Midday break** | |
| 12:30–1:00 | Presentation + demo | Module 6 overview: scenario analysis and analytics/AI-assisted features | Learners understand what-if parameters, advanced analytics visuals, and cloud-dependent fallback patterns. |
| 1:00–1:30 | Lab | Module 6: Advanced Analytics & AI-Assisted Insights | Learners build a what-if scenario; advanced AI visuals covered per the cloud-availability matrix (see note below). |
| 1:30–2:00 | Presentation + discussion | Module 7 overview: security design and RLS patterns | Learners understand static RLS, dynamic RLS, testing, and Build-permission considerations. |
| 2:00–2:45 | Lab | Module 7 exercises 1–3: Security Design | Learners create or review static/dynamic RLS and test roles in Desktop and/or Service where available. |
| 2:45–3:00 | Closeout | Wrap-up, optional follow-on modules, Q&A, action items | Customer leaves with a completed Modules 1–7 path, validation notes, and recommended next steps. |

---

## Notes for the instructor

- **Module 6 cloud dependency:** Decomposition tree, forecasting, key influencers, Python/R visuals, and Azure Machine Learning integration are Commercial-only per the *Exercise Cloud Coverage Matrix*. In Government (GCC High) or DoD deliveries, treat these as **Not Covered** and replace with the what-if scenario exercise plus a walkthrough/discussion of the concepts instead of hands-on labs.
- **Compressing to a single day:** If this agenda needs to fit a 1-day briefing instead of 3 days, do not try to force all seven modules into 5 hours of hands-on time. Instead, right-size the scope during scoping — for example, run only Modules 1, 2, and 4 hands-on, and demo the rest (3, 5, 6, 7) at a conceptual level. Confirm the final scope with the customer before the delivery date.
- **If a lab runs long**, move to the next module's starter file rather than letting learners fall behind — do not extend past the 3:00 PM end time.
- **Tenant readiness**: Mark any Service, Fabric, Copilot, XMLA, external-tool, or deployment-pipeline content as conceptual-only unless it has been validated in the delivery tenant.
- Copy this agenda for each customer engagement and adjust dates, audience emphasis, and lab depth as needed.
