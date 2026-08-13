# Lab 06: Advanced Analytics and AI-Assisted Insights

## Lab summary

These labs introduce advanced analytical features while preserving a Gov-ready path that does not depend on AI services or unvalidated tenant features.

## Novice-friendly how-to guide

### Create a what-if parameter

1. Select **Modeling > New parameter > Numeric range**.
2. Name it `Margin Adjustment %`.
3. Enter the minimum, maximum, and increment values from the lab.
4. Keep the generated slicer.
5. Use the generated parameter measure in an adjusted-margin DAX measure.
6. Change the slicer value and confirm visuals update.

### Use advanced visuals safely

1. Confirm the visual is available in the target tenant.
2. Add the visual to a practice page first.
3. Add the measure to analyze.
4. Add the dimensions that may explain the result.
5. Document what the visual suggests and what still needs human validation.

## Azure Government readiness

The what-if parameter lab is **Gov-ready**. Decomposition tree, forecasting, anomaly detection, key influencers, Python/R visuals, Azure ML integration, and Copilot are **Verify for Gov** or **Commercial-focused**.

## Power BI project format

Build report artifacts as PBIP projects. PBIP is the source-controlled format for this workshop. PBIX files can be generated from PBIP later if needed.

## Prerequisites

- Power BI Desktop.
- PBIP report/model from earlier modules.
- Optional tenant validation for AI visuals, Python/R, Azure ML, or Copilot.

### Exercise 1: What-if parameters

**Objective:** Build a scenario analysis experience.

### Tasks

1. Create a what-if parameter named `Margin Adjustment %`.
2. Set a reasonable range such as -10% to 20%.
3. Create an adjusted gross margin measure using the selected parameter value.
4. Add the parameter slicer to a report page.
5. Compare base and adjusted margin visuals.

### Expected result

Users can adjust a parameter and see scenario measures update.

### Exercise 2: Decomposition tree where available

> **Azure Government note:** Decomposition tree is **Verify for Gov**. Confirm visual availability and tenant settings before making this hands-on.

**Objective:** Explore drivers behind a metric.

### Tasks when available

1. Add a decomposition tree visual.
2. Use Sales Amount or Gross Margin as the analyzed metric.
3. Add explanatory fields such as Territory, Product Category, Customer Type, and Segment.
4. Explore high and low value paths.

### Gov-safe alternate path

Use a matrix hierarchy and drillthrough page to explore the same dimensions manually.

### Exercise 3: Forecasting where available

> **Azure Government note:** Forecasting is **Verify for Gov**. Validate visual support, tenant policy, and data residency before requiring it.

**Objective:** Add forecast context to a trend.

### Tasks when available

1. Add a line chart with date on the X axis.
2. Add Sales Amount as the value.
3. Enable forecasting in the Analytics pane.
4. Review confidence intervals and assumptions.

### Gov-safe alternate path

Create rolling average and prior-period comparison measures.

### Exercise 4: Key influencers where available

> **Azure Government note:** Key influencers is **Verify for Gov** because it is an AI visual.

**Objective:** Explore possible drivers of an outcome.

### Tasks when available

1. Add a key influencers visual.
2. Select a target metric or category.
3. Add explanatory fields.
4. Review influencers and segments.
5. Discuss interpretation limits.

### Gov-safe alternate path

Use ranked visuals, Top N measures, and slicer-driven comparisons.

### Exercise 5: Optional Python or R visuals

> **Azure Government note:** Python/R visuals are **Verify for Gov**. Validate Desktop configuration, approved packages, Service support, and customer policy.

**Objective:** Understand when code-based visuals are appropriate.

### Tasks when available

1. Confirm approved runtime and packages.
2. Create a simple Python or R visual using non-sensitive workshop data.
3. Document package dependencies.
4. Review Service limitations.

### Gov-safe alternate path

Use native visuals or precomputed data instead of code-based visuals.

### Exercise 6: Optional Azure Machine Learning integration

> **Azure Government note:** Azure ML integration is **Verify for Gov**. Validate cloud, region, network, identity, endpoint, and data residency before delivery.

**Objective:** Understand scored data integration options.

### Conceptual tasks

1. Review the scoring architecture.
2. Identify identity and network dependencies.
3. Identify data residency constraints.
4. Discuss importing scored output as a safe alternate path.

### Gov-safe alternate path

Use a static scored sample table and explain how it would be produced outside the lab.

### Exercise 7: Copilot conceptual section

> **Azure Government note:** Copilot in Power BI/Fabric is **Commercial-focused / Verify for Gov**. Treat as conceptual unless confirmed available.

**Objective:** Understand potential Copilot use cases and governance controls.

### Conceptual tasks

1. Review potential Copilot-assisted workflows.
2. Discuss tenant, capacity, licensing, and data boundary requirements.
3. Review human validation requirements.
4. Map each workflow to a non-AI fallback.

## Validation checklist

- [ ] What-if parameter works.
- [ ] Scenario measures respond to parameter selection.
- [ ] Optional AI/advanced visuals are labeled with availability status.
- [ ] Gov-safe alternate path is documented for each optional feature.
- [ ] Python/R prerequisites are documented if used.
- [ ] Azure ML architecture dependencies are documented if discussed.
- [ ] Copilot is conceptual unless tenant availability is validated.
- [ ] AI-generated or ML-driven output includes human-review guidance.

