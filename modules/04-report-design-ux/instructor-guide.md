# Instructor Guide

## Module summary

Advanced report design is about helping users answer questions quickly and confidently. The goal is not to demonstrate every visual; it is to teach interaction patterns that guide users through a decision flow.

## Audience and prerequisites

Best fit for report authors, semantic model developers, product owners, and BI platform owners.

Learners should understand basic report visuals, slicers, filters, formatting, and publishing.

## Learning objectives

- Match report layout to audience and decision type.
- Add drillthrough pages for detail analysis.
- Add report page tooltips for contextual explanations.
- Use bookmarks and buttons for guided navigation.
- Build dynamic navigation patterns.
- Use field parameters for guided report exploration.
- Apply conditional formatting intentionally.
- Create and validate mobile layouts.
- Review accessibility.
- Identify Gov validation needs for personalized visuals and AI visuals.

## Delivery flow

1. Start with audience personas and report intent.
2. Show the difference between executive summary, analyst exploration, and operational monitoring pages.
3. Add drillthrough from summary visuals to detail pages.
4. Add report page tooltips.
5. Build bookmark and button interactions.
6. Add dynamic navigation and field parameters.
7. Add conditional formatting and create a mobile layout.
8. Run accessibility review.
9. Discuss personalized visuals and AI visuals as tenant-dependent.

## Feature availability

| Feature | Status | Instructor note |
|---|---|---|
| Drillthrough, tooltips, bookmarks, buttons | Gov-ready | Required core path. |
| Field parameters | Gov-ready | Validate Desktop and Service parity before delivery. |
| Conditional formatting | Gov-ready | Required core path. |
| Mobile layout | Gov-ready | Validate mobile app and customer device policy. |
| Personalized visuals | Verify for Gov | Do not require unless Service feature and tenant setting are validated. |
| AI visuals | Verify for Gov / Commercial-focused | Treat conceptually unless available in target tenant. |

## Environment setup

- Power BI Desktop installed.
- A PBIP report based on the Module 1 model and Module 2 measures.
- Optional: Power BI Service workspace for personalized visuals validation.
- Optional: Mobile app/device or Desktop mobile layout preview.

## Lab facilitation notes

- Keep pages purposeful and avoid "visual gallery" report design.
- Reinforce that every interaction should answer a user question.
- Require accessibility checks before considering a report complete.
- Avoid required AI visual or personalized visual steps for Azure Government delivery unless validated.

## Common issues and fixes

| Issue | Likely cause | Fix |
|---|---|---|
| Drillthrough does not appear | Drillthrough field is missing from the target page | Add the correct drillthrough field and test from a matching visual. |
| Tooltip page does not show | Page size or tooltip setting is not configured | Set page information to tooltip and assign the tooltip page to the visual. |
| Bookmark changes too much | Bookmark captures data, display, or current page unintentionally | Edit bookmark options to capture only intended behavior. |
| Field parameter does not switch the visual | Generated parameter field was not added to the correct visual well | Add the parameter field to Values, Axis, or Rows depending on the visual goal. |
| Mobile layout is unreadable | Desktop layout was not optimized for mobile | Build a separate mobile layout with fewer visuals and larger touch targets. |
| Conditional formatting distracts users | Too many colors or unclear thresholds | Use a limited palette and document business meaning. |

## Gov delivery notes

The required report interaction labs are Gov-ready because they use Desktop authoring features. Personalized visuals and AI visuals should be marked **Verify for Gov** or **Commercial-focused** and should not be required in a Gov lab without tenant validation.

## Commercial-enhanced options

- Demonstrate personalized visuals in the Service.
- Demonstrate AI visuals such as Key influencers or decomposition tree if available.
- Publish the report and review the experience in Teams or PowerPoint where customer policy allows.

