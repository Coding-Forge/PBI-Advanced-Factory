# Module 2: Advanced DAX

## Module summary

This module teaches learners how to reason about DAX evaluation context and apply advanced measure patterns in enterprise Power BI models. The module uses the semantic model from Module 1 and focuses on correctness, maintainability, and performance.

## Learning objectives

By the end of this module, learners will be able to:

- Explain row context, filter context, and context transition.
- Use `CALCULATE` to intentionally modify filter context.
- Apply `ALL`, `REMOVEFILTERS`, `ALLEXCEPT`, `KEEPFILTERS`, and `TREATAS`.
- Build reusable measures with variables and measure branching.
- Create advanced time-intelligence measures.
- Use calculation groups to reduce repeated time-intelligence DAX when validated tooling is available.
- Handle semi-additive calculations.
- Build ranking, Top N, and dynamic segmentation patterns.
- Create dynamic titles and measure switching patterns.
- Debug and optimize DAX measures.
- Identify Azure Government considerations for DAX Studio and external tools.

## Feature availability

| Feature | Status | Delivery note |
|---|---|---|
| Core DAX language | Gov-ready | Desktop modeling feature and generally cloud-independent. |
| Context transition and `CALCULATE` | Gov-ready | Core DAX concept. |
| Time-intelligence patterns | Gov-ready | Requires a valid date table. |
| Calculation groups | Verify for Gov | Native Desktop authoring depends on Desktop version; TMDL, XMLA, external tools, capacity behavior, and workstation policy require validation. |
| Ranking and Top N | Gov-ready | Core DAX and visual interaction pattern. |
| Dynamic titles and measure switching | Gov-ready | Can use disconnected tables or field parameters. |
| DAX Studio | Verify for Gov | Local tool; Service model access depends on tenant policy, XMLA, and workstation rules. |
| External tools | Verify for Gov | Validate customer workstation policy and tenant connectivity. |

## Module artifacts

- [Instructor Guide](instructor-guide.md)
- [Learner Guide](learner-guide.md)
- [Slide Outline](slide-outline.md)
- [DAX Pattern Reference](dax-pattern-reference.md)
- [Knowledge Check](knowledge-check.md)
- [Module labs](..\..\labs\02-advanced-dax\README.md)

