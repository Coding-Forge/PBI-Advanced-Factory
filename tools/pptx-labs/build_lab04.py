#!/usr/bin/env python3
"""
Builds the Lab 04 (Report Design & UX) instructor deck.
Run from repo root: python tools/pptx-labs/build_lab04.py
Output: modules/04-report-design-ux/assets/report-design-ux.pptx
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from slide_kit import (
    new_presentation, title_slide, agenda_slide,
    content_slide, table_slide, checklist_slide, closing_slide,
)

OUT_PATH = Path(__file__).resolve().parent.parent.parent / \
    "modules" / "04-report-design-ux" / "assets" / "report-design-ux.pptx"

MODULE_NO = 4
TITLE = "Report Design & UX"
SUBTITLE = ("Turning the Contoso semantic model into an interactive, accessible, "
            "audience-aware decision experience")

AGENDA_TOPICS = [
    "Advanced report UX principles",
    "Audience-driven design",
    "Slicers and filters",
    "Drillthrough",
    "Report page tooltips",
    "Bookmarks and buttons",
    "Dynamic navigation",
    "Field parameters",
    "Conditional formatting",
    "Mobile layout",
    "Accessibility",
    "Azure Government considerations",
    "Module lab walkthrough",
    "Knowledge check and discussion",
]


def build():
    prs = new_presentation()
    page = 1

    # 1. Title
    title_slide(
        prs, MODULE_NO, TITLE, SUBTITLE,
        script=[
            "Welcome learners to Module 4. Frame the shift: Modules 1\u20133 built the semantic model, "
            "DAX measures, and Power Query transforms. Today we finally put a face on all of that "
            "work \u2014 the report canvas the business actually sees and clicks on.",
            "Set the stakes: a technically correct model with a poor report UX still fails, because "
            "the business can't find the answer they need in under 10 seconds. Report UX is not "
            "decoration \u2014 it is the difference between a deployed report and a shelfware report.",
            "Preview the lab: students will add drillthrough from customer visuals to a Customer "
            "Detail page, build a tooltip page, wire up bookmarks and navigation buttons, create a "
            "Metric Parameter field parameter over Sales Amount / Gross Margin / Gross Margin % / "
            "Quantity, apply conditional formatting tied to margin thresholds, build a mobile "
            "layout, and run an accessibility review.",
            "Call out Azure Government up front: every required lab in this module is Gov-ready "
            "because it uses core Desktop authoring features. Personalized visuals and AI visuals "
            "are Verify-for-Gov and are treated as optional/discussion-only.",
        ]
    )
    page += 1

    # 2. Agenda
    agenda_slide(
        prs, MODULE_NO, AGENDA_TOPICS, page=page,
        script=[
            "Walk the fourteen topics quickly. Group them mentally for the class: principles and "
            "audience (1\u20132), the four core interactivity patterns (3\u20136 \u2014 filters, drillthrough, "
            "tooltips, bookmarks), the navigation and self-service layer (7\u20138), formatting and "
            "reach (9\u201311), then Gov considerations, the lab, and the wrap-up (12\u201314).",
            "Point out that this is the widest module so far in terms of topic count, but each "
            "topic is intentionally shorter than a modeling or DAX topic \u2014 report UX is many small "
            "well-chosen decisions, not one big architectural one.",
            "Tell students the lab (topic 13) exercises hit every one of topics 3 through 11 "
            "directly \u2014 there is no purely theoretical topic in this module except the Gov note "
            "and the wrap-up.",
        ]
    )
    page += 1

    # 3. Topic 1 - Advanced report UX principles
    content_slide(
        prs, 1, "Advanced Report UX Principles", page=page,
        lead_items=[
            "Treat each report page as a decision interface, not a data dump: the top of the page "
            "should answer 'what is going on?' before it offers 'and here is how to dig in'.",
            "Layout follows audience and task \u2014 the same measures might be shown as KPI cards "
            "for an executive, a matrix for an analyst, and a status table for an operator.",
            "Use interactivity (slicers, drillthrough, tooltips, bookmarks) to reduce cognitive "
            "load, not to add cleverness \u2014 every interactive element competes with the primary "
            "question the page is trying to answer.",
            "If a slicer, button, or visual doesn't help the user decide what to do next, delete "
            "it or move it to a hidden panel behind a bookmark.",
        ],
        why_items=[
            "A technically perfect model can still fail adoption if the report makes the answer "
            "hard to find in the first 10 seconds.",
            "Consistency across pages (slicer placement, filter meaning, navigation) is what lets "
            "users trust that the number they see is the number they asked for.",
            "Every later topic in this module is a specific technique for applying these three "
            "principles \u2014 audience fit, cognitive load reduction, and consistency.",
        ],
        footer="Instructor prompt: ask the room to describe a report they've abandoned because it "
               "was hard to use \u2014 what specifically made them give up?",
        script=[
            "Open with a reframing statement: 'A report is not a dashboard \u2014 it is a decision "
            "interface.' The user opens it to answer a question and take action. Every design "
            "choice should be judged against that.",
            "Explain the three principles concretely. Audience and task means the executive KPI "
            "card layout is a different page from the analyst matrix, even if both use the same "
            "[Sales Amount] and [Gross Margin %] measures \u2014 the layout and level of detail change, "
            "not the underlying measures.",
            "On cognitive load, give a concrete anti-example: five slicers at the top of the page, "
            "each of which could contradict the others, is not more powerful \u2014 it's more "
            "confusing. If two of those slicers are for occasional analyst use, they belong behind "
            "a bookmark-driven panel that appears only when needed.",
            "Close with the discussion prompt in the footer, and use answers to bridge into topic "
            "2: most abandoned reports failed because they were designed for one audience \u2014 "
            "usually 'someone technical' \u2014 and shown to everyone.",
        ]
    )
    page += 1

    # 4. Topic 2 - Audience-driven design
    table_slide(
        prs, 2, "Audience-Driven Design", page=page,
        headers=["Audience", "Primary question", "Recommended page pattern"],
        col_widths=[2.4, 4.6, 4.9],
        rows=[
            ["Executive summary",
             "Are we on plan? What are the top exceptions I need to act on?",
             "KPI cards + a small variance/status matrix; minimal slicers; drillthrough to detail."],
            ["Analyst exploration",
             "Why is this metric moving? Which slice is driving the trend?",
             "Matrices with row hierarchies, field parameter slicers for metric/dimension "
             "switching, tooltips for extra context."],
            ["Operational monitoring",
             "What needs attention right now?",
             "Conditional-formatted status tables, refresh timestamp visible, focused filter set."],
            ["Detail and exception handling",
             "For this specific customer / product / territory, what happened?",
             "Drillthrough target page with entity KPIs and a transaction table."],
        ],
        note="Lab tie-in: the Customer Detail page built in Exercise 1 is the 'detail and exception' "
             "pattern; the field parameter work in Exercise 5 is the 'analyst exploration' pattern.",
        script=[
            "Walk each row of the table. Emphasize that the same semantic model powers all four "
            "audience patterns \u2014 nothing in the model changes. What changes is which visuals sit "
            "on the page, how many slicers, and where the drillthrough targets go.",
            "For the executive row, stress restraint: executives typically want three to five KPIs "
            "and a variance table, not a canvas of 15 charts. If they need to dig deeper, they "
            "drill through \u2014 they don't scroll.",
            "For analyst exploration, tie forward to topic 8 (field parameters): field parameters "
            "let one page serve many analyst questions without duplicating the page five times.",
            "For the detail/exception row, tie forward to topic 4 (drillthrough) \u2014 that entire "
            "pattern exists to serve this audience. The executive on the summary page right-clicks "
            "an exception, lands on a Customer Detail page filtered to that entity, and gets exactly "
            "the deep context they need without leaving the report.",
        ]
    )
    page += 1

    # 5. Topic 3 - Slicers and filters
    content_slide(
        prs, 3, "Slicers and Filters", page=page,
        lead_items=[
            "Three filter scopes in Power BI: visual-level (only that visual), page-level (all "
            "visuals on the current page), and report-level (every page in the report).",
            "Slicers are just page-level filters rendered as an on-canvas control \u2014 use them "
            "when the user needs to change the filter interactively; use the Filters pane for "
            "fixed context they should not change.",
            "Place slicers in a consistent location on every page (typically the top strip or a "
            "left rail) so users don't have to hunt for them.",
            "Use Sync slicers (View \u2192 Sync slicers) so that a slicer change on one page carries "
            "to related pages \u2014 but only for slicers where that shared context genuinely makes "
            "sense (e.g., Year, Territory), not for page-specific slicers like a metric switcher.",
        ],
        why_items=[
            "Inconsistent slicer placement and unclear scope is the number-one source of 'the "
            "numbers don't match' complaints \u2014 users forget which filters are still active.",
            "Correctly scoped page/report filters keep the on-canvas slicer count small, which "
            "directly reduces cognitive load from topic 1.",
            "Sync slicers preserve the user's mental model as they navigate pages built in the "
            "next topics (drillthrough, dynamic navigation).",
        ],
        footer="Design rule: if a slicer is on the page for compliance/context only (never "
               "changed), it should be a page-level filter in the Filters pane, not an on-canvas "
               "slicer competing for attention.",
        script=[
            "Start by clarifying the three filter scopes precisely, because students often conflate "
            "them: visual filter is one visual, page filter is one page, report filter is every "
            "page. Slicers themselves live on a page and are effectively an interactive page filter.",
            "Explain the placement rule with an example: if the Territory slicer is top-left on the "
            "summary page, it should be top-left on every page that uses it. Users navigating "
            "between pages should never have to search for where the slicer moved to.",
            "Cover Sync slicers concretely: point out that when you enable it, you get separate "
            "toggles for 'sync' and 'visible' per page, so you can have a slicer that's visible on "
            "the summary page and hidden but still filtering on the detail page. That is the "
            "correct way to preserve filter context across a drillthrough.",
            "Close with the footer rule and pivot to topic 4: once slicer context is right, the "
            "next question is what to do when a user wants to leave a filtered summary and go "
            "deep on one row. That's drillthrough.",
        ]
    )
    page += 1

    # 6. Topic 4 - Drillthrough
    content_slide(
        prs, 4, "Drillthrough", page=page,
        lead_items=[
            "Drillthrough sends the user from a summary visual to a dedicated detail page, "
            "automatically filtered to the value they right-clicked (e.g., a specific customer).",
            "Configure it by adding the entity field (DimCustomer[CustomerName] in this lab) to "
            "the Drill-through field well on the target page \u2014 that field defines the filter "
            "context the target page inherits.",
            "Add a Back button (Insert \u2192 Buttons \u2192 Navigator \u2192 Back) so the user returns to "
            "the exact summary page and filter state they came from.",
            "Design the detail page as an entity page: KPI cards for that customer, plus a "
            "transaction table \u2014 not another summary. It should answer 'tell me everything "
            "about this one entity.'",
        ],
        why_items=[
            "Drillthrough replaces the 'build one giant page with every level of detail' anti-"
            "pattern with a clean summary \u2192 detail flow that matches how executives actually work.",
            "Because the target page inherits filter context automatically, you don't have to "
            "duplicate slicers on the detail page \u2014 the model does the filtering for you.",
            "The Back button is not optional UX polish \u2014 without it, users get stuck on the "
            "detail page and often close the report entirely rather than use the page tabs.",
        ],
        footer="Lab connection: Exercise 1 builds the Customer Detail page with CustomerName as "
               "the drillthrough field, customer KPI cards, a transaction table, and a Back button.",
        script=[
            "Walk the mechanics in the order the lab does: create the target page (Customer "
            "Detail), then add the drillthrough field. Stress that the drillthrough field's job is "
            "to define what filter context is inherited when the user right-clicks and drills.",
            "Explain the right-click gesture explicitly \u2014 first-time users often don't discover "
            "drillthrough because they left-click everything. The instructor should demo the right-"
            "click flow at least once so learners see it work.",
            "On the target page design, contrast it with an analyst page: a Customer Detail page "
            "does NOT need Territory or Segment slicers, because it's already filtered to one "
            "customer. Adding those slicers only invites the user to break the intended filter "
            "context.",
            "Emphasize the Back button strongly. Insert \u2192 Buttons \u2192 Navigator \u2192 Back is the "
            "correct path \u2014 it returns to the exact source page and filter state, which no "
            "generic 'go to page X' button can do reliably. Preview topic 5: sometimes users don't "
            "need a full detail page, just a peek \u2014 that's what tooltip pages are for.",
        ]
    )
    page += 1

    # 7. Topic 5 - Report page tooltips
    content_slide(
        prs, 5, "Report Page Tooltips", page=page,
        lead_items=[
            "A report page tooltip is a small, custom-designed page that appears on hover over a "
            "visual \u2014 it lets you show extra context (a trend, a KPI breakdown) without adding "
            "another visual to the main canvas.",
            "Set the target page's Page information \u2192 Page type to 'Tooltip' so it uses the "
            "compact tooltip page size, then design compact visuals sized to that canvas.",
            "Assign the tooltip on the source visual: Format visual \u2192 General \u2192 Tooltips \u2192 "
            "Type: Report page, and select the tooltip page.",
            "Design constraints: keep it under a handful of small visuals, avoid slicers on a "
            "tooltip page (they can't be interacted with), and rely on the source visual's filter "
            "context flowing in automatically.",
        ],
        why_items=[
            "Tooltip pages fight the 'add another chart to the canvas' reflex \u2014 they let one "
            "clean main visual carry rich context that only appears when the user wants it.",
            "Because they inherit filter context from the hovered data point, a single tooltip "
            "page can serve many source visuals across the report.",
            "They pair well with drillthrough: hover for a quick peek, right-click drillthrough "
            "for the full detail page.",
        ],
        footer="Lab connection: Exercise 2 builds a Sales Tooltip page (compact KPIs + a small "
               "trend visual) and assigns it to a main report visual.",
        script=[
            "Introduce the concept by contrast: the default Power BI tooltip is a plain text list "
            "of the data point's values \u2014 useful but limited. A report page tooltip lets you show "
            "an actual mini visualization instead.",
            "Walk the three configuration steps in order: create the page, change the page type "
            "to Tooltip (which resizes the canvas to a small tooltip-appropriate size), then go to "
            "the source visual and assign the tooltip page.",
            "Cover the design constraints deliberately \u2014 students often try to cram five visuals "
            "onto a tooltip page and end up with something illegibly small. One or two KPI cards "
            "and a small trend line is the sweet spot. And no slicers, because the user is "
            "hovering, not clicking.",
            "Tie it back to the UX principles: tooltip pages are the poster child for topic 1's "
            "'reduce cognitive load' principle \u2014 they hide detail until asked for, keeping the "
            "main canvas clean. Preview topic 6: sometimes you want that same reveal behavior for "
            "an entire panel, not just a hover \u2014 that's bookmarks and buttons.",
        ]
    )
    page += 1

    # 8. Topic 6 - Bookmarks and buttons
    content_slide(
        prs, 6, "Bookmarks and Buttons", page=page,
        lead_items=[
            "A bookmark captures a snapshot of the current report state \u2014 which visuals are "
            "visible, current slicer selections, sort order, and drill state \u2014 and lets you "
            "restore it with a button click.",
            "Common patterns: Show/Hide panels (an info panel, an advanced-slicer panel), Reset "
            "filters, and stepwise guided walkthroughs of a report page.",
            "In the Bookmark options menu, control what the bookmark actually captures: Data "
            "(slicer state), Display (visual visibility), Current page (which page is shown), and "
            "Selected visuals (only capture a subset).",
            "Trigger bookmarks from buttons: Insert \u2192 Buttons \u2192 Blank/Navigator, then in the "
            "button's Action settings choose Type: Bookmark and pick the target bookmark.",
        ],
        why_items=[
            "Bookmarks let one page do the work of three or four \u2014 an info panel can be hidden "
            "by default and revealed only when a first-time user asks for it.",
            "The Data / Display / Current page checkboxes matter: a bookmark that captures Data "
            "when you only meant to change visibility will silently reset the user's slicer "
            "selections when the button is clicked \u2014 a classic UX bug.",
            "Reset filters bookmarks are the safety net that lets analysts explore aggressively "
            "without fear of leaving the report in a confusing state.",
        ],
        footer="Design rule: for a Show/Hide panel bookmark, uncheck 'Data' \u2014 you only want to "
               "toggle visibility, not overwrite the user's current slicer selections.",
        script=[
            "Define a bookmark plainly: it's a saved snapshot of report state. The most common "
            "mistake first-time authors make is not realizing the Data checkbox is on by default, "
            "so their Show/Hide panel button also silently resets slicers.",
            "Walk the common patterns \u2014 Show/Hide info panel is by far the most common in "
            "production reports, followed by Reset filters. Guided walkthroughs (a sequence of "
            "bookmarks stepping the user through a page) are more advanced and rarely worth the "
            "maintenance cost.",
            "Demo the Selection pane briefly: this is how you build a Show/Hide panel \u2014 group "
            "the panel's visuals in the Selection pane, hide them, save a 'Panel Hidden' bookmark, "
            "unhide them, save a 'Panel Shown' bookmark. Wire two buttons to those bookmarks.",
            "Reinforce the footer rule one more time \u2014 uncheck Data for visibility-only "
            "bookmarks. It's the single most common source of 'why did my slicer reset?' bug "
            "reports. Preview topic 7: buttons are also how we build the navigation layer of the "
            "report, which is what dynamic navigation is about.",
        ]
    )
    page += 1

    # 9. Topic 7 - Dynamic navigation
    content_slide(
        prs, 7, "Dynamic Navigation", page=page,
        lead_items=[
            "Page navigation buttons (Insert \u2192 Buttons \u2192 Navigator \u2192 Page navigator) build a "
            "one-click nav bar automatically from your report's pages \u2014 it stays in sync as you "
            "add or rename pages.",
            "For custom navigation, use individual Blank buttons with Action \u2192 Type: Page "
            "navigation, and place them consistently (typically a top or left rail).",
            "Give every navigation button visible affordance: a filled shape, a clear label, and "
            "a visible border or icon. Transparent-on-white buttons are functionally invisible \u2014 "
            "users can't click what they can't see.",
            "Use consistent labels (e.g., 'Summary', 'Customers', 'Products'), consistent size, "
            "and consistent placement across every page \u2014 navigation controls should never "
            "surprise the user by moving between pages.",
        ],
        why_items=[
            "Users often can't find the built-in Power BI page tabs (especially in embedded or "
            "Service views) \u2014 in-canvas navigation removes that discoverability problem.",
            "Consistent placement and visible affordance directly address the discoverability "
            "issue this lab was corrected for: previously the nav buttons were near-invisible, and "
            "users didn't know they could click through.",
            "Page navigator visuals cost nothing to maintain when pages are added or renamed \u2014 "
            "prefer them over hand-wired button lists for standard nav bars.",
        ],
        footer="Corrected guidance: give every dynamic navigation button a solid fill, a visible "
               "border, and a text label \u2014 the earlier version of this lab had near-invisible "
               "buttons that users couldn't discover.",
        script=[
            "Start with the discoverability problem: even a well-designed report fails if the user "
            "doesn't know they can navigate. In-canvas navigation solves that, but only if the "
            "buttons are actually visible.",
            "Demo the Page navigator first because it's the fastest win: one insert, and Power BI "
            "generates a button per page, kept in sync automatically. For most reports this is all "
            "you need. Custom Blank buttons with Page navigation actions are the fallback when you "
            "need styling or ordering the navigator doesn't give you.",
            "Emphasize the visible-affordance rule strongly \u2014 this is the corrected guidance for "
            "this specific lab. The prior version had transparent buttons that were technically "
            "there but functionally invisible. Every navigation button should have a solid fill, a "
            "visible border, and a clearly readable text label. If you can't see it against the "
            "canvas without hovering, users can't either.",
            "Close on consistency: buttons should live in the same spot on every page, in the "
            "same order, at the same size. Users navigate by muscle memory once they've clicked "
            "twice \u2014 don't break that. Preview topic 8: dynamic navigation moves users between "
            "pages; field parameters let a user reshape a single page without moving at all.",
        ]
    )
    page += 1

    # 10. Topic 8 - Field parameters
    content_slide(
        prs, 8, "Field Parameters", page=page,
        lead_items=[
            "A field parameter (Modeling \u2192 New parameter \u2192 Fields) creates a slicer-driven "
            "switcher over a chosen set of measures or dimension columns \u2014 one page, many views.",
            "The lab's Metric Parameter switches between [Sales Amount], [Gross Margin], [Gross "
            "Margin %], and [Quantity]; an optional Dimension Parameter switches between "
            "DimProductCategory[ProductCategory], DimTerritory[TerritoryRegion], and "
            "DimSegment[Segment].",
            "Field parameters are the native replacement for the older 'disconnected table + "
            "SWITCH measure' pattern \u2014 they handle formatting and dimensions natively where the "
            "DAX pattern needs extra work.",
            "When choosing fields, pick columns whose tables all filter FactSales via the star "
            "schema. Mixing unrelated tables triggers an InvalidUnconstrainedJoin error \u2014 the "
            "corrected lab avoids that.",
        ],
        why_items=[
            "One field-parameter page replaces four near-duplicate pages (one per metric), which "
            "cuts maintenance cost and eliminates 'which page had the right filter?' confusion.",
            "Because the switcher is model-driven, adding a new metric later means adding it to "
            "the parameter \u2014 not rebuilding a page or editing every SWITCH measure.",
            "The InvalidUnconstrainedJoin correction matters: this lab previously hit that error "
            "by including fields the model couldn't relate. The current lab picks fields from "
            "tables that all relate to FactSales through the star schema.",
        ],
        footer="Corrected guidance: dimension field parameters must draw from tables that share a "
               "common filter path through the fact table \u2014 mixing unrelated tables causes an "
               "InvalidUnconstrainedJoin error.",
        script=[
            "Introduce field parameters as the answer to a very common request: 'can I let the "
            "user pick which metric they're looking at without me building four separate pages?' "
            "Before field parameters, the pattern was a disconnected selector table plus a DAX "
            "SWITCH \u2014 the Deeper Understanding Challenge in the lab actually walks through that "
            "older pattern so students can compare.",
            "Walk the mechanics from the lab: Modeling \u2192 New parameter \u2192 Fields, pick the four "
            "measures, keep 'Add slicer to this page' checked, and Power BI generates both the "
            "parameter table and a slicer wired to it. Drop the generated parameter field into a "
            "visual's values well and the visual now switches with the slicer.",
            "Cover the InvalidUnconstrainedJoin correction explicitly. This lab used to throw that "
            "error because the dimension parameter mixed columns from tables the engine couldn't "
            "resolve to a single filter path. The fix is to pick dimension columns whose tables "
            "all filter FactSales \u2014 in this lab, DimProductCategory, DimTerritory, and DimSegment "
            "all do. If you get InvalidUnconstrainedJoin in the wild, that's the diagnostic.",
            "Close with the tradeoff between native field parameters and the disconnected-table + "
            "SWITCH pattern: field parameters are almost always better for pure metric or "
            "dimension swapping. The SWITCH pattern is still useful when you need custom fallback "
            "logic \u2014 which is exactly what the optional Deeper Understanding Challenges in the "
            "lab explore.",
        ]
    )
    page += 1

    # 11. Topic 9 - Conditional formatting
    table_slide(
        prs, 9, "Conditional Formatting", page=page,
        headers=["Technique", "When to use it", "How to apply it in this lab"],
        col_widths=[2.6, 4.6, 4.7],
        rows=[
            ["Background / font color by rule",
             "Categorical status (Above / At / Near / Below target).",
             "Format \u2192 conditional formatting \u2192 Rules; source the color from a color measure "
             "like [Margin Target Status Color] which returns hex values (#107C10, #FFB900, "
             "#D13438)."],
            ["Color scale (gradient)",
             "Continuous variance measures where relative magnitude matters.",
             "Use for [Gross Margin vs Target] on a matrix; pick a low / mid / high anchor "
             "aligned to the business thresholds."],
            ["Icons",
             "Quick status glance in dense tables.",
             "Rules-based icons on the status column; keep the icon set to three states to match "
             "the target-status categories."],
            ["Data bars",
             "In-row magnitude comparison against a simple range.",
             "Good for [Sales Amount] within a customer or product-category table; avoid on "
             "percentages where scale is misleading."],
            ["Documented thresholds",
             "Always \u2014 every rule needs a documented business meaning.",
             "Add a small note visual on the page that spells out the threshold ranges (e.g., "
             ">= +5%: Above target)."],
        ],
        note="Lab tie-in: Exercise 6 applies these techniques. The Deeper Understanding Challenge "
             "builds [Margin Target Status] and [Margin Target Status Color] measures that plug "
             "directly into rule-based conditional formatting.",
        script=[
            "Frame the topic with a warning: conditional formatting is the single easiest place "
            "to over-decorate a report. Every color and icon must earn its place by conveying "
            "business meaning \u2014 if you can't say what a color means in one sentence, it doesn't "
            "belong.",
            "Walk each row. For rule-based color, tie it directly to the lab's [Margin Target "
            "Status Color] measure \u2014 that measure returns actual hex codes, and conditional "
            "formatting has a 'Field value' option that reads those hex codes directly. That's the "
            "cleanest, most maintainable pattern.",
            "Contrast color scales with rules: scales are continuous (small variance = light "
            "color, large variance = dark), rules are categorical (specific ranges = specific "
            "colors). Pick based on whether the business thinks in bands or in magnitudes.",
            "Close on the documented-thresholds rule. Every conditional format needs a note "
            "somewhere on the page that spells out what the color means \u2014 otherwise the report "
            "author is the only person who ever really understands the report. Preview topic 10: "
            "everything we just discussed also has to work on a phone screen.",
        ]
    )
    page += 1

    # 12. Topic 10 - Mobile layout
    content_slide(
        prs, 10, "Mobile Layout", page=page,
        lead_items=[
            "Open the Mobile layout view (View \u2192 Mobile layout) to build a separate portrait "
            "arrangement of the same visuals \u2014 the desktop layout is untouched.",
            "Only place the highest-value visuals: top KPI cards and one primary chart per page. "
            "Dense matrices and multi-slicer strips do not translate to a phone.",
            "Size for touch: buttons and slicers need to be big enough for a thumb (roughly 44 "
            "pixels / ~11 mm minimum), and visuals need to be readable without pinch-zoom.",
            "Validate the layout by previewing every page in mobile view before publishing \u2014 an "
            "empty mobile canvas falls back to a scaled desktop layout, which is rarely usable.",
        ],
        why_items=[
            "Executives and field users increasingly consume Power BI on phones \u2014 a report "
            "without a mobile layout effectively excludes them.",
            "The scaled-desktop fallback is one of the most common 'report looks broken on my "
            "phone' complaints \u2014 explicitly building the mobile layout prevents it.",
            "Prioritizing 'the two visuals that answer the primary question' on mobile forces "
            "the same discipline topic 1 asked for on desktop \u2014 audience-first design.",
        ],
        footer="Lab connection: Exercise 7 builds a mobile layout for the summary page \u2014 the "
               "top KPIs and one trend visual, sized for touch, validated in mobile preview.",
        script=[
            "Open with the audience question: who reads this report on a phone, and what is the "
            "one question they need answered before they put the phone back in their pocket? That "
            "answer drives the entire mobile layout.",
            "Walk the mechanics: View \u2192 Mobile layout gives you a phone-shaped canvas and a "
            "list of the page's existing visuals. You drag the ones you want onto the mobile "
            "canvas and resize them. Visuals not placed on the mobile canvas simply don't appear "
            "in mobile mode \u2014 they aren't lost, they just aren't shown.",
            "Cover the touch sizing rule with the ~44 pixel / 11 mm minimum. Under that size, "
            "users start fat-fingering the wrong slicer value or wrong button, which reads as "
            "'the report is buggy' from their perspective.",
            "Close on validation: previewing every page in mobile view before publishing is not "
            "optional. Preview topic 11: mobile layout is about reach across devices; accessibility "
            "is about reach across users.",
        ]
    )
    page += 1

    # 13. Topic 11 - Accessibility
    content_slide(
        prs, 11, "Accessibility", page=page,
        lead_items=[
            "Alt text: add descriptive alt text on every non-decorative visual so screen readers "
            "can announce what the visual is showing.",
            "Tab order: set Selection pane \u2192 Tab order deliberately so keyboard users move "
            "through the page in a logical reading order, not the arbitrary order visuals were "
            "added.",
            "Contrast: text and meaningful UI must meet the WCAG 4.5:1 contrast ratio against its "
            "background \u2014 pale-gray-on-white footers and axis labels are a common failure.",
            "Never let color be the only signal: pair color with an icon, a text status label, or "
            "a shape so color-blind users get the same message (the Above/At/Near/Below target "
            "labels do exactly this).",
        ],
        why_items=[
            "Accessibility is a real requirement for many organizations \u2014 government tenants in "
            "particular have accessibility mandates that a color-only status report will fail.",
            "The keyboard tab order is invisible to sighted users but is the primary navigation "
            "for many assistive-tech users \u2014 if it's not set, they experience the page as random.",
            "Building accessibility in from the start is far cheaper than retrofitting it after a "
            "compliance review flags the report.",
        ],
        footer="Lab connection: Exercise 8 runs a formal accessibility review \u2014 alt text, tab "
               "order, contrast, visual titles, and 'color is not the only signal' \u2014 and "
               "documents each improvement.",
        script=[
            "Frame this as a real production requirement, not a nice-to-have. Many organizations "
            "\u2014 especially government customers this workshop targets \u2014 will refuse to deploy a "
            "report that fails an accessibility review.",
            "Walk each item. Alt text: it's not enough to type 'chart' \u2014 it should describe what "
            "the visual shows ('Bar chart of Sales Amount by Territory, current quarter, showing "
            "West as the top region'). Power BI can auto-generate a starting alt text but always "
            "review and edit it.",
            "Tab order: demo the Selection pane's tab-order view briefly. The default order is "
            "the order you added visuals \u2014 which is almost never a logical reading order. Fix "
            "it once per page and it's done.",
            "Emphasize the color-is-not-the-only-signal rule with the lab's Margin Target Status "
            "pattern: 'Above target' / 'Near target' / 'Below target' is a text label AND a color "
            "AND (if you use icon formatting) an icon. Redundant encoding is the accessibility "
            "win. Preview topic 12: some Power BI features have limits in Azure Government \u2014 "
            "that's what we cover next.",
        ]
    )
    page += 1

    # 14. Topic 12 - Azure Government considerations
    table_slide(
        prs, 12, "Azure Government Considerations", page=page,
        headers=["Feature", "Gov status", "Delivery guidance"],
        col_widths=[3.0, 2.8, 6.1],
        rows=[
            ["Drillthrough, tooltips, bookmarks, navigation, conditional formatting",
             "Gov-ready",
             "Core Desktop authoring \u2014 no tenant validation needed for the required labs."],
            ["Field parameters",
             "Gov-ready",
             "Validate Desktop and Service parity in the customer's tenant before treating as "
             "production-ready."],
            ["Mobile layout",
             "Gov-ready",
             "Validate the customer's mobile app policy and device management before assuming "
             "the report reaches phones."],
            ["Personalized visuals",
             "Verify for Gov",
             "Depends on Service availability and tenant settings. Do not require in Gov labs "
             "unless validated in advance."],
            ["AI visuals (Q&A, Key influencers, Decomposition tree, Smart narrative)",
             "Verify for Gov / Commercial-focused",
             "Provide a non-AI alternate path for Gov delivery; treat as demo-only until "
             "validated."],
        ],
        note="Rule of thumb: everything the required lab exercises use is Gov-ready. Anything "
             "labeled 'Optional' or 'Deeper Understanding' involving personalized or AI visuals is "
             "Verify for Gov and must be checked before treating as hands-on.",
        script=[
            "Set expectations: this slide is a reference, not a deep dive. Most of what students "
            "just learned is fully Gov-ready \u2014 the entire required lab is. Only the optional "
            "personalized-visuals and AI-visuals paths need extra validation.",
            "Walk the table row by row. For the top row, stress that drillthrough, tooltips, "
            "bookmarks, navigation, and conditional formatting are all core Desktop features \u2014 no "
            "tenant setting can disable them for the required lab flow.",
            "For field parameters and mobile, explain 'Gov-ready' with a caveat: the feature is "
            "supported, but you should still validate Desktop/Service parity and mobile device "
            "policy in the specific customer tenant. It's a smoke test, not a blocker.",
            "For personalized and AI visuals, be firm: if this is a Gov delivery, plan a non-AI "
            "path from day one. Don't build a lab that depends on Q&A or Key influencers and then "
            "discover on delivery day that the tenant doesn't have them. Preview: with concepts "
            "covered, it's lab time.",
        ]
    )
    page += 1

    # 15. Module lab walkthrough
    checklist_slide(
        prs, "Module Lab Walkthrough", kicker="Topic 13 \u2014 What you'll build", page=page,
        items=[
            "Exercise 1: Drillthrough \u2014 Customer Detail page + Back button",
            "Exercise 2: Report page tooltip \u2014 Sales Tooltip page assigned to a visual",
            "Exercise 3: Bookmarks and buttons \u2014 Show/Hide panel + Reset filters",
            "Exercise 4: Dynamic navigation \u2014 visible buttons with clear labels on every page",
            "Exercise 5: Field parameters \u2014 Metric Parameter (+ optional Dimension Parameter)",
            "Deeper challenges: disconnected metric selector + margin target selector (DAX SWITCH)",
            "Exercise 6: Conditional formatting \u2014 rule-based colors tied to margin thresholds",
            "Exercise 7: Mobile layout \u2014 prioritized visuals sized for touch",
            "Exercise 8: Accessibility review \u2014 alt text, tab order, contrast, non-color signals",
            "Validation: run the UX validation checklist before considering the report done",
        ],
        script=[
            "This slide is the bridge from concepts into hands-on work. Walk it as a literal table "
            "of contents for the next block of lab time.",
            "Point out that Exercises 1 through 5 map directly onto topics 4 through 8 of this "
            "deck \u2014 the topic order and exercise order intentionally match, so students can flip "
            "back to the corresponding slide if they get stuck on an exercise.",
            "Call out the two Deeper Understanding Challenges as optional but valuable: they build "
            "a disconnected metric selector and a margin target selector using Power Query + DAX "
            "SWITCH. The margin selector produces the [Margin Target Status] and [Margin Target "
            "Status Color] measures that Exercise 6 then uses for conditional formatting \u2014 so if "
            "students want the richest Exercise 6, they should do that challenge first.",
            "Remind students that the required exercises are all Gov-ready, and that Exercises 7 "
            "(mobile) and 8 (accessibility) are not optional polish \u2014 they're production "
            "requirements for most real deployments.",
        ]
    )
    page += 1

    # 16. Knowledge check and discussion
    checklist_slide(
        prs, "Knowledge Check & Discussion", kicker="Topic 14 \u2014 Wrap-up", page=page,
        items=[
            "Report pages have a clear audience and a primary question they answer.",
            "Drillthrough works from a summary visual to Customer Detail, and Back returns.",
            "The tooltip page is assigned and shows compact context on hover.",
            "Bookmarks capture only the intended state (Data unchecked for visibility toggles).",
            "Navigation buttons are visible, labelled, and consistent on every page.",
            "The field parameter switches metrics without an InvalidUnconstrainedJoin error.",
            "Conditional formatting has documented business thresholds.",
            "Mobile layout is readable and touch-friendly on every page.",
            "Accessibility review is complete: alt text, tab order, contrast, non-color signals.",
            "Discussion: when would you accept AI visuals in a Gov delivery, and how would you "
            "document the fallback path?",
        ],
        script=[
            "Use this as a discussion-driven wrap-up rather than a quiz. The goal is to surface "
            "reasoning across topics, not just recall which button lives in which menu.",
            "Pick 2\u20133 items and ask specific students to answer out loud. The navigation "
            "visibility item and the field-parameter InvalidUnconstrainedJoin item are especially "
            "worth surfacing because they are the two known pitfalls this lab was corrected to "
            "avoid \u2014 make sure the class understands both.",
            "For the bookmark 'Data unchecked' item, walk through the specific scenario one more "
            "time: a Show/Hide info panel bookmark should not reset slicers, so uncheck Data. This "
            "is the single most common UX bug in bookmark-heavy reports.",
            "Close by connecting forward: everything today assumed the model and DAX from Modules "
            "1\u20132 are correct and the report runs quickly. Module 5 is where we make it run "
            "quickly \u2014 performance optimization on top of exactly this report.",
        ]
    )
    page += 1

    # 17. Closing
    closing_slide(
        prs, MODULE_NO,
        "Module 05: Performance Optimization \u2014 measuring, diagnosing, and tuning the reports "
        "you just built so they stay fast at production scale.",
        page=page,
        subtitle="Learners now have an interactive, accessible, audience-aware Contoso report "
                 "built on the Modules 1\u20133 foundation.",
        script=[
            "Congratulate the class on completing the report design and UX module. This is often "
            "the module that changes how learners think about their existing reports the most \u2014 "
            "expect them to come back tomorrow wanting to redesign old dashboards.",
            "Remind students to keep their completed report artifact open or close at hand, since "
            "Module 5 profiles and tunes exactly this report against the same semantic model.",
            "Take final questions before moving on, especially anything about field parameters "
            "(InvalidUnconstrainedJoin), navigation button discoverability, or the Gov status of "
            "personalized and AI visuals \u2014 those three are the most common lingering-confusion "
            "topics from this module.",
        ]
    )

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    prs.save(str(OUT_PATH))
    print(f"Saved: {OUT_PATH} ({len(prs.slides.__iter__.__self__._sldIdLst)} slides)")


if __name__ == "__main__":
    build()
