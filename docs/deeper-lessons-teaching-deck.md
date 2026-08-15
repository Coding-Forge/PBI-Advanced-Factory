# Power BI Advanced Factory: Deeper Lessons Teaching Deck

This file is the editable source outline for the student-facing PowerPoint deck:

`docs\deeper-lessons-teaching-deck.pptx`

Use it when instructors want to modify the slide flow, add customer-specific emphasis, or trim the deck for shorter deliveries.

## Audience

Power BI report authors, analysts, and BI developers who know the basics and want to understand why the advanced lab patterns matter.

## Deck purpose

Introduce the deeper lab themes before students complete the hands-on work. Each section explains:

- What the pattern is.
- Why it helps report authors and report consumers.
- How it builds on earlier lessons.
- What students should be able to explain after the lab.

## Slide outline

1. **Title: Deeper Power BI Patterns**
   - Position the deck as a bridge from basic report building to reliable analytics delivery.

2. **Why these deeper lessons matter**
   - Advanced features are useful only when they make reports more trustworthy, maintainable, and easier to use.

3. **How the themes build on each other**
   - Power Query prepares data.
   - Semantic modeling creates structure.
   - DAX defines business logic.
   - UX turns logic into decisions.
   - Performance and security make the solution production-ready.

4. **Power Query: from cleanup to repeatable data preparation**
   - Parameters, staging queries, source lineage, functions, error review, and incremental refresh preparation.

5. **Power Query deeper pattern: error review before removal**
   - Teach `err_OrdersReview` as a review table, not a silent deletion step.

6. **Semantic model handoff: why clean data is not enough**
   - Fact/dimension grain, role-playing dates, bridge tables, and relationship direction.

7. **Advanced DAX: the measure layer is the contract**
   - Base measures, branching, context validation, time intelligence, and ranking.

8. **Calculation groups: reusable time intelligence**
   - Use `SELECTEDMEASURE()` to reduce repeated time-intelligence logic.
   - Prefer native Desktop authoring when available; TMDL and external tools are optional validated paths.

9. **Calculation group authoring view**
   - Use the annotated Power BI Desktop Model view screenshot.

10. **Report UX: make the report guide the user**
    - Drillthrough, tooltips, bookmarks, navigation, field parameters, mobile layout, and accessibility.

11. **Field parameters vs disconnected selectors**
    - Native field parameters swap fields/measures.
    - Disconnected selectors plus `SWITCH` teach custom logic and defaults.

12. **Deeper challenge: disconnected metric selector**
    - Power Query creates the selector table.
    - DAX reads the slicer selection.
    - The visual responds without relationships.

13. **Performance: improve with evidence**
    - Capture a baseline with Performance Analyzer.
    - Optimize visuals, model shape, and DAX only after measuring.

14. **Security: design access intentionally**
    - Static RLS, dynamic RLS, testing, Build permission, and documenting expected access.

15. **Instructor facilitation model**
    - Present the pattern.
    - Demo the pattern.
    - Let learners build it.
    - Validate it in a simple visual.
    - Ask reflection questions.

16. **Sources and further learning: data prep and modeling**
    - Power Query M language
    - Query parameters
    - Error handling
    - Star schema guidance
    - Model relationships

17. **Sources and further learning: DAX and UX**
    - Calculation groups
    - DAX `SELECTEDVALUE`
    - DAX `SWITCH`
    - Field parameters
    - Performance Analyzer

18. **Sources and further learning: operations and lifecycle**
    - Row-level security
    - PBIP project format
    - TMDL overview
    - Power BI guidance documentation

## Official sources for slide references

- Power Query M language: https://learn.microsoft.com/powerquery-m/
- Query parameters in Power Query: https://learn.microsoft.com/power-query/power-query-query-parameters
- Error handling in Power Query: https://learn.microsoft.com/power-query/dealing-with-errors
- Star schema guidance: https://learn.microsoft.com/power-bi/guidance/star-schema
- Model relationships in Power BI Desktop: https://learn.microsoft.com/power-bi/transform-model/desktop-relationships-understand
- Calculation groups in Power BI: https://learn.microsoft.com/power-bi/transform-model/calculation-groups
- DAX `SELECTEDVALUE`: https://learn.microsoft.com/dax/selectedvalue-function-dax
- DAX `SWITCH`: https://learn.microsoft.com/dax/switch-function-dax
- Field parameters: https://learn.microsoft.com/power-bi/create-reports/power-bi-field-parameters
- Performance Analyzer: https://learn.microsoft.com/power-bi/create-reports/desktop-performance-analyzer
- Row-level security: https://learn.microsoft.com/fabric/security/service-admin-row-level-security
- Power BI Project files: https://learn.microsoft.com/power-bi/developer/projects/projects-overview
- TMDL overview: https://learn.microsoft.com/analysis-services/tmdl/tmdl-overview

