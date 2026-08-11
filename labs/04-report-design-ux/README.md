# Module 4 Labs: Advanced Report Design and User Experience

## Lab summary

These labs guide learners through building an interactive report experience using the semantic model and measures created in earlier modules.

## Azure Government readiness

The required labs are **Gov-ready** because they use core Power BI Desktop report features. Personalized visuals are **Verify for Gov**. AI visuals are **Verify for Gov / Commercial-focused** and should not be required in Gov delivery unless validated.

## Power BI project format

Build report artifacts as PBIP projects. PBIP is the source-controlled format for this workshop. PBIX files can be generated from PBIP later if a packaged file is needed.

## Prerequisites

- Module 1 semantic model.
- Module 2 DAX measures.
- Power BI Desktop.

## Lab 1: Drillthrough

**Objective:** Add a detail path from summary analysis to entity detail.

### Tasks

1. Create a page named `Customer Detail`.
2. Add `CustomerName` as a drillthrough field.
3. Add customer-level KPI cards and a transaction table.
4. Add a Back button.
5. Test drillthrough from a customer visual on the summary page.

### Expected result

Users can right-click a customer and navigate to a filtered detail page.

## Lab 2: Report page tooltips

**Objective:** Add contextual detail without cluttering the main report page.

### Tasks

1. Create a page named `Sales Tooltip`.
2. Set page size to Tooltip.
3. Add compact KPIs and a small trend visual.
4. Enable the page as a tooltip.
5. Assign the tooltip page to a main report visual.

### Expected result

Hovering over the assigned visual displays compact contextual information.

## Lab 3: Bookmarks and buttons

**Objective:** Create guided interactions.

### Tasks

1. Create an information panel or slicer panel.
2. Add Show and Hide bookmarks.
3. Add buttons that trigger the bookmarks.
4. Review bookmark options for Data, Display, and Current page.
5. Add a Reset button if appropriate.

### Expected result

Users can reveal and hide guided content without leaving the page.

## Lab 4: Dynamic navigation

**Objective:** Improve report navigation.

### Tasks

1. Add page navigation buttons.
2. Add a report page navigator where appropriate.
3. Use clear labels and consistent placement.
4. Test navigation from every page.

### Expected result

Users can move through the report without relying only on page tabs.

## Lab 5: Conditional formatting

**Objective:** Use visual formatting to highlight business meaning.

### Tasks

1. Define thresholds for sales variance or gross margin percentage.
2. Apply conditional formatting to a table, matrix, or KPI visual.
3. Use colors and icons sparingly.
4. Add a note explaining threshold meaning.

### Expected result

Formatting highlights exceptions without overwhelming the report.

## Lab 6: Mobile layout

**Objective:** Create a mobile-optimized report view.

### Tasks

1. Open Mobile layout view.
2. Add the highest-value visuals.
3. Resize visuals for readability.
4. Avoid dense tables unless necessary.
5. Validate mobile layout flow.

### Expected result

The report has a readable mobile experience with prioritized content.

## Lab 7: Accessibility review

**Objective:** Validate the report for accessibility and usability.

### Tasks

1. Add alt text for important visuals.
2. Review tab order.
3. Check color contrast.
4. Confirm visual titles and labels are descriptive.
5. Verify that color is not the only way meaning is conveyed.

### Expected result

The report includes documented accessibility improvements.

## Optional: Personalized visuals

> **Azure Government note:** Personalized visuals are marked **Verify for Gov**. Confirm Service availability and tenant settings before making this hands-on.

Discuss or demonstrate personalized visuals only after validation.

## Optional: AI visuals

> **Azure Government note:** AI visuals are marked **Verify for Gov / Commercial-focused**. Provide a non-AI alternate path for Azure Government delivery.

Discuss or demonstrate AI visuals only after validation.

## Validation checklist

- [ ] Report pages have clear audience and purpose.
- [ ] Drillthrough works from summary to detail.
- [ ] Tooltip page is configured and assigned.
- [ ] Bookmarks capture only intended behavior.
- [ ] Navigation buttons are consistent.
- [ ] Conditional formatting has documented thresholds.
- [ ] Mobile layout is readable.
- [ ] Accessibility review is complete.
- [ ] Personalized visuals and AI visuals have Gov notes.

