# Report UX Design Standards

Use these standards for every Power BI report created in this workshop.

## Audience and page purpose

Each report page must have a clear audience and purpose:

| Page type | Primary audience | Purpose |
|---|---|---|
| Executive summary | Executives and sponsors | Fast understanding of performance, risks, and key trends. |
| Analyst exploration | Analysts and power users | Flexible slicing, comparison, and root-cause analysis. |
| Operational detail | Managers and operators | Actionable details, exceptions, and transaction-level records. |
| Tooltip page | All users | Contextual explanation without cluttering the main canvas. |
| Drillthrough page | Analysts and operators | Focused detail for a selected entity. |

## Layout standards

- Put the most important insight in the upper-left or top summary area.
- Use consistent page headers.
- Group related visuals together.
- Keep slicers predictable and consistently placed.
- Avoid crowded pages.
- Use whitespace intentionally.
- Use a limited and consistent color palette.
- Prefer clear visual titles over decorative text.

## Interaction standards

- Use drillthrough for detail paths, not for primary navigation.
- Use bookmarks for guided states such as show/hide panels or reset views.
- Use buttons with clear labels and accessible tooltips.
- Use report page tooltips for context, definitions, or small supporting visuals.
- Avoid hidden interactions that users cannot discover.
- Provide a reset path when users can heavily filter or navigate.

## Conditional formatting standards

- Define threshold meaning before applying colors.
- Use red only for genuine negative or exception states.
- Do not rely on color alone.
- Keep icon sets simple.
- Document business logic behind thresholds.

## Mobile standards

- Create a dedicated mobile layout for important reports.
- Prioritize KPI cards, trend visuals, and high-value filters.
- Avoid dense tables unless required.
- Use large touch targets.
- Validate readability on mobile preview or device.

## Accessibility standards

- Add meaningful alt text for important visuals.
- Set logical tab order.
- Use sufficient color contrast.
- Avoid color-only meaning.
- Use descriptive titles and labels.
- Avoid tiny font sizes.
- Verify keyboard navigation where possible.

## Azure Government notes

- Core report UX features are generally **Gov-ready**.
- Personalized visuals are **Verify for Gov** because Service features and tenant settings may vary.
- AI visuals are **Verify for Gov / Commercial-focused** and should have a non-AI alternate path.
- Mobile app usage should be validated against customer device and app policy.

