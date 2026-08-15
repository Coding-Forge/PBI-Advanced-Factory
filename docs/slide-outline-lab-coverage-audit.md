# Slide Outline to Lab Coverage Audit

This audit compares each module `slide-outline.md` with the corresponding `Student/Labs/Source/<module>/README.md`. Use it as an instructor planning checklist: `Partial` and `Needs review` items are candidates for lab updates or outline simplification.
## Summary

| Module | Covered | Partial | Needs review |
|---|---:|---:|---:|
| 01-advanced-semantic-modeling | 8 | 2 | 0 |
| 02-advanced-dax | 10 | 3 | 0 |
| 03-advanced-power-query | 8 | 4 | 0 |
| 04-report-design-ux | 10 | 3 | 0 |
| 05-performance-optimization | 9 | 3 | 0 |
| 06-advanced-analytics-ai | 12 | 0 | 0 |
| 07-security-design | 10 | 2 | 0 |
| 08-service-enterprise-deployment | 10 | 2 | 0 |
| 09-monitoring-governance | 11 | 1 | 0 |
| 10-premium-fabric-capacity | 12 | 0 | 0 |
| 11-automation-devops | 8 | 4 | 0 |


## 01-advanced-semantic-modeling

| Slide topic | Coverage | Missing/weak terms to review |
|---|---|---|
| 1. Why semantic modeling matters | Covered | complex, governed, inconsistent, matters, reports |
| 2. From flat files to analytical models | Partial | analytical, exports, hidden, problems, repeated, reporting, separation |
| 3. Star schema design | Covered | conformed, readability, surrogate |
| 4. Relationship design | Covered | risks |
| 5. Role-playing dimensions | Covered | duplicated, inactive, overview, userelationship |
| 6. Bridge tables | Covered | considerations |
| 7. Composite models and storage modes | Covered | modes, requirements |
| 8. Large semantic model considerations | Covered | aggregations, capacity, considerations, incremental, reduction |
| 9. Module lab walkthrough | Partial | checks, commercial, enhanced, overview, walkthrough |
| 10. Knowledge check and discussion | Covered | discussion, knowledge, production |

**Coverage note:** Star schema, relationships, role-playing dates, bridge tables, date tables, and composite/DirectQuery comparison are represented in labs.

**Fix item:** Consider adding explicit lab text for model perspectives/shared semantic model concepts if those remain in the slide outline.

## 02-advanced-dax

| Slide topic | Coverage | Missing/weak terms to review |
|---|---|---|
| 1. Why advanced DAX matters | Covered | business, complex, composed, define, matters |
| 2. Evaluation context | Covered | evaluation, level, query |
| 3. Context transition | Covered | columns, iterators |
| 4. Filter modification | Partial | allexcept, modification, removefilters, treatas |
| 5. Measure branching | Partial | derived, naming, reuse, testing |
| 6. Time intelligence | Covered | periods, requirements |
| 7. Semi-additive measures | Covered |  |
| 8. Calculation groups | Covered | considerations, requirements |
| 9. Ranking and Top N | Covered | level, rankx |
| 10. Dynamic report logic | Covered |  |
| 11. Debugging and optimization | Covered | debugging, reducing, testing |
| 12. Azure Government considerations | Covered | considerations, dependent |
| 13. Knowledge check and lab review | Partial | common, knowledge, mistakes, production, strategies |

**Coverage note:** Context, CALCULATE, time intelligence, calculation groups, ranking, dynamic titles, and optimization are represented.

**Fix item:** Parent-child hierarchy appears in the outline but is not a hands-on lab; decide whether to add or remove from outline.

## 03-advanced-power-query

| Slide topic | Coverage | Missing/weak terms to review |
|---|---|---|
| 1. Why Power Query architecture matters | Covered | intent, makes, matters, solution, visible |
| 2. Staging query pattern | Covered |  |
| 3. Folder-combine pattern | Covered | consistency, future, hidden |
| 4. M language fundamentals | Partial | fundamentals, handwritten, language, lists, records, references |
| 5. Parameters | Covered | governance |
| 6. Custom functions | Covered | inputs, invoking, testing |
| 7. Query folding | Partial | blockers, dependency, folds, matters |
| 8. Native queries and source systems | Partial | considerations, maintainability, security, systems |
| 9. Data quality and errors | Partial | business, checks, errors, keeping, replacing |
| 10. Incremental refresh preparation | Covered |  |
| 11. Azure Government considerations | Covered | confirmed, considerations |
| 12. Lab review | Covered | solution |

**Coverage note:** Parameters, staging, custom functions, data quality, query folding, and incremental refresh prep are represented.

**Fix item:** Native query and privacy levels are mostly conceptual; add explicit activities if they are intended hands-on.

## 04-report-design-ux

| Slide topic | Coverage | Missing/weak terms to review |
|---|---|---|
| 1. Advanced report UX principles | Partial | cognitive, decision, follow, interactivity, interfaces, principles, reduce |
| 2. Audience-driven design | Partial | analyst, driven, executive, handling, monitoring, operational |
| 3. Slicers and filters | Partial | avoiding, confusion, filters, slicers |
| 4. Drillthrough | Covered |  |
| 5. Report page tooltips | Covered | assignment, constraints |
| 6. Bookmarks and buttons | Covered | experiences, filters, panels |
| 7. Dynamic navigation | Covered | concepts |
| 8. Field parameters | Covered | driven, duplicated |
| 9. Conditional formatting | Covered | avoiding, usage |
| 10. Mobile layout | Covered | prioritization, specific, touch |
| 11. Accessibility | Covered | keyboard |
| 12. Azure Government considerations | Covered | considerations, depends, policy |
| 13. Lab review | Covered | production, screenshot |

**Coverage note:** Drillthrough, tooltips, bookmarks, navigation, field parameters, conditional formatting, mobile layout, and accessibility are represented.

**Fix item:** Personalized/AI visuals remain optional/conceptual, which is appropriate for shortened delivery.

## 05-performance-optimization

| Slide topic | Coverage | Missing/weak terms to review |
|---|---|---|
| 1. Performance optimization mindset | Covered | again, bottleneck, mindset, thing |
| 2. Performance layers | Covered | layers, rendering, system |
| 3. Performance Analyzer | Covered | analysis, copying |
| 4. Model size and cardinality | Covered | relationship, splits, types |
| 5. DAX optimization | Covered | avoiding, caution, iterator, scope |
| 6. Visual optimization | Covered | complexity, custom, highlighting, matrices |
| 7. Power Query and refresh optimization | Partial | early, filtering, folding, preparation, removing, staging |
| 8. Aggregations | Covered | group, import, manage |
| 9. DirectQuery and hybrid patterns | Partial | hybrid, import, large, tradeoffs |
| 10. Service and capacity monitoring | Covered | admin, dataset, history, monitoring |
| 11. External tools | Covered | customer, editor, tabular, tools |
| 12. Lab review and benchmark targets | Partial | benchmark, documentation, expectations, production, targets |

**Coverage note:** Performance Analyzer, model size review, DAX optimization, visuals, aggregations, and refresh policy are represented.

**Fix item:** VertiPaq Analyzer/DAX Studio remain Verify-for-Gov optional; keep conceptual unless tool access is validated.

## 06-advanced-analytics-ai

| Slide topic | Coverage | Missing/weak terms to review |
|---|---|---|
| 1. Advanced analytics vs. AI-assisted features | Covered | experiences, external, patterns |
| 2. What-if parameters | Covered | business |
| 3. Decomposition tree | Covered | exploration, guided |
| 4. Forecasting | Covered | considerations, seasonality, series |
| 5. Anomaly detection | Covered | considerations, identification, quality, unusual |
| 6. Key influencers | Covered | categorical, explainability, outcomes |
| 7. Python and R visuals | Covered | considerations, security |
| 8. Azure Machine Learning integration | Covered | alignment, overview |
| 9. Copilot in Power BI/Fabric | Covered | assistance, authoring, caveats, exploration, summarization |
| 10. Gov-safe alternate paths | Covered | exception, flags, standard |
| 11. Delivery decision framework | Covered | acceptable, decision, framework |
| 12. Lab review | Covered | labels, notes |

**Coverage note:** What-if parameters and Gov-safe alternatives are represented; advanced/AI visuals are framed as optional.

**Fix item:** Python/R and Azure ML are conceptual; add prepared screenshots if a hands-on tenant is unavailable.

## 07-security-design

| Slide topic | Coverage | Missing/weak terms to review |
|---|---|---|
| 1. Power BI security layers | Covered | audiences, layers, links, workspace |
| 2. Content access vs. data access | Covered | after, granted |
| 3. Static RLS | Covered | examples, maintenance, tradeoffs |
| 4. Dynamic RLS | Covered | identity |
| 5. Service role assignment | Partial | assigning, assignment, distribution, implications, workspace |
| 6. Build permission | Covered | reports |
| 7. Object-level security | Covered | considerations, hiding |
| 8. Sensitivity labels and Purview | Covered | dependency, setup |
| 9. Sharing and external users | Partial | direct, guest, restrictions, workspace |
| 10. Security testing | Covered | documentation, membership, negative |
| 11. Azure Government considerations | Covered | capability, considerations, platform, stricter |
| 12. Security review checklist | Covered | evidence |

**Coverage note:** Static RLS, dynamic RLS, Desktop/Service testing, and Build permission are represented.

**Fix item:** OLS and sensitivity labels are optional conceptual sections; add tooling screenshots if needed.

## 08-service-enterprise-deployment

| Slide topic | Coverage | Missing/weak terms to review |
|---|---|---|
| 1. From authoring to enterprise deployment | Covered | authoring, supportability, targets |
| 2. Workspace design | Partial | conventions, design, domain, naming, production |
| 3. Workspace roles | Partial | admin, contributor, member, roles, viewer |
| 4. Publishing content | Covered | originated, takeover |
| 5. Refresh configuration | Covered | levels, privacy |
| 6. Gateways and cloud connections | Covered | clusters, mappings, premises |
| 7. Shared semantic models and thin reports | Covered | analysis, impact, pattern |
| 8. Power BI Apps | Covered | packaging, targeting |
| 9. Deployment pipelines | Covered |  |
| 10. Endorsement | Covered | workflow |
| 11. Azure Government considerations | Covered | considerations, restrictions |
| 12. Lab review | Covered |  |

**Coverage note:** Publishing, refresh, gateway/cloud connection, thin reports, Apps, audiences, pipelines, and endorsement are represented.

**Fix item:** Deployment pipelines are tenant-dependent; keep alternate manual deployment path clear.

## 09-monitoring-governance

| Slide topic | Coverage | Missing/weak terms to review |
|---|---|---|
| 1. Why monitoring and governance matter | Covered | matter, ownership, production, reliability |
| 2. Usage metrics | Covered | interpretation, trends |
| 3. Refresh monitoring | Covered | system |
| 4. Tenant settings | Covered | build, users |
| 5. Gateway monitoring | Covered | clusters, dependencies, versioning |
| 6. Activity and audit logs | Covered | examples, investigation, logged |
| 7. Admin monitoring workspace | Covered | considerations, insights, visibility |
| 8. Capacity metrics | Covered | concepts, impact, interactive |
| 9. Purview and DLP | Covered | prevention, workflow |
| 10. Adoption tracking | Partial | candidates, needs, patterns, retirement, tracking, training |
| 11. Operations model | Covered | change, handling, owners |
| 12. Lab review | Covered | completion |

**Coverage note:** Usage, refresh history, tenant settings, gateway, and runbook coverage are represented.

**Fix item:** Admin monitoring/audit/Purview topics are optional; add admin screenshots for no-access deliveries.

## 10-premium-fabric-capacity

| Slide topic | Coverage | Missing/weak terms to review |
|---|---|---|
| 1. Capacity-aware architecture | Covered | performance |
| 2. Licensing and capacity options | Covered | assignment |
| 3. Large semantic models | Covered | dependency, format, storage |
| 4. XMLA endpoint | Covered | external, patterns, tools, workflows |
| 5. Paginated reports | Covered | perfect, pixel, reporting |
| 6. Fabric capacity | Covered | experience, units, workloads |
| 7. Direct Lake | Covered | freshness, modeling |
| 8. OneLake, Lakehouse, and Warehouse | Covered | pattern |
| 9. Semantic Link | Covered | science, workflows |
| 10. Capacity metrics and throttling | Covered | signals |
| 11. Azure Government considerations | Covered | parity |
| 12. Architecture decision review | Covered | decision, risks |

**Coverage note:** Capacity comparison, XMLA, paginated reports, large models, Fabric concepts, and capacity metrics are represented.

**Fix item:** Fabric hands-on should remain optional until tenant/capacity availability is validated.

## 11-automation-devops

| Slide topic | Coverage | Missing/weak terms to review |
|---|---|---|
| 1. Lifecycle management goals | Partial | goals, governance, promotion, repeatability, reviewability, rollback |
| 2. PBIP as source of record | Covered | output |
| 3. Git workflow | Partial | branches, commits, practices, releases, requests |
| 4. PBIP file structure | Covered |  |
| 5. External tools | Covered | dependency |
| 6. REST APIs and PowerShell | Covered | export, import, refresh |
| 7. Service principals | Covered | groups |
| 8. Fabric workspace Git integration | Partial | behavior, branching, caveats, connected |
| 9. Azure DevOps conceptual pipeline | Covered | configure, package, smoke |
| 10. GitHub Actions conceptual pipeline | Covered | authenticate |
| 11. Azure Government considerations | Partial | availability, considerations, endpoints, identity, network |
| 12. Deployment checklist | Covered | refresh, rollback |

**Coverage note:** PBIP, git workflow, Tabular Editor/ALM Toolkit, REST/PowerShell, DevOps/GitHub Actions, and checklist are represented.

**Fix item:** CI/CD remains conceptual; add runnable pipeline samples only after environment assumptions are finalized.

