#!/usr/bin/env python3
"""
Builds the Lab 02 (Advanced DAX) instructor deck.
Run from repo root: python tools/pptx-labs/build_lab02.py
Output: modules/02-advanced-dax/assets/advanced-dax.pptx
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from slide_kit import (
    new_presentation, title_slide, agenda_slide,
    content_slide, table_slide, checklist_slide, closing_slide,
)

OUT_PATH = Path(__file__).resolve().parent.parent.parent / \
    "modules" / "02-advanced-dax" / "assets" / "advanced-dax.pptx"

MODULE_NO = 2
TITLE = "Advanced DAX"
SUBTITLE = "A trusted, testable measure layer on top of the Lab 01 semantic model"

AGENDA_TOPICS = [
    "Why advanced DAX matters",
    "Evaluation context",
    "Context transition",
    "Filter modification",
    "Measure branching",
    "Time intelligence",
    "Semi-additive measures",
    "Calculation groups",
    "Ranking and Top N",
    "Dynamic report logic",
    "Debugging and optimization",
    "Azure Government considerations",
    "Knowledge check and lab review",
]


def build():
    prs = new_presentation()
    page = 1

    # 1. Title
    title_slide(
        prs, MODULE_NO, TITLE, SUBTITLE,
        script=[
            "Welcome learners to Module 2. Frame this module as the layer that sits directly on top "
            "of the semantic model they built in Module 1. The model gave us trusted tables and "
            "relationships; DAX is where those tables turn into trusted business logic \u2014 "
            "[Sales Amount], [Gross Margin], [Sales YTD], [Sales YoY %] and so on.",
            "Set the stakes: in an advanced Power BI course, DAX is almost never wrong because the "
            "syntax is wrong \u2014 it is wrong because the author misread the evaluation context. "
            "That is what this module fixes. Every topic today is really a different lens on the "
            "same question: 'What filter and row context is my measure seeing right now?'",
            "Preview the lab: students will build base measures ([Sales Amount], [Quantity], "
            "[Gross Margin]) on the Lab 01 model, then branch those into filter-modifying measures, "
            "time-intelligence measures, ranking and Top N patterns, dynamic titles, calculation "
            "groups, and finally an optimization pass with variables and measure branching.",
            "Call out the Azure Government angle up front: the core DAX language, CALCULATE, "
            "time-intelligence functions, and ranking are all Gov-ready because they run inside "
            "Power BI Desktop and the engine. Calculation groups, DAX Studio, Tabular Editor, and "
            "the XMLA endpoint are all 'Verify for Gov' \u2014 we will treat them as conceptual unless "
            "the tenant explicitly allows them.",
        ]
    )
    page += 1

    # 2. Agenda
    agenda_slide(
        prs, MODULE_NO, AGENDA_TOPICS, page=page,
        script=[
            "Walk through the thirteen topics briefly \u2014 don't teach yet, just orient the room. "
            "Group them mentally into four arcs: context foundations (1\u20133), how we shape context "
            "on purpose (4\u20135), patterns that solve real reporting problems (6\u201310), and "
            "professional practice: debugging, Gov, and validation (11\u201313).",
            "Call out that topic 8 (calculation groups) and parts of topic 11 (DAX Studio) are "
            "Verify-for-Gov. Depending on the classroom tenant we may cover them conceptually only "
            "and rely on native Desktop authoring instead of Tabular Editor.",
            "Tell learners the hands-on lab lines up almost one-to-one with topics 2\u20139: "
            "Exercise 1 is evaluation context, Exercise 2 is CALCULATE and filter modification, "
            "Exercise 3 is time intelligence, Exercise 4 is semi-additive, Exercise 5 is ranking, "
            "Exercise 6 is dynamic titles / measure switching, Exercise 7 is calculation groups, "
            "Exercise 8 is optimization. Nothing on these slides is theoretical \u2014 it all shows "
            "up in code they will type today.",
        ]
    )
    page += 1

    # 3. Topic 1 - Why advanced DAX matters
    content_slide(
        prs, 1, "Why Advanced DAX Matters", page=page,
        lead_items=[
            "Measures are where business logic lives: [Sales Amount], [Gross Margin], [Sales YTD] "
            "define what those terms officially mean for every report on this model.",
            "Most 'DAX bugs' in production reports are not syntax errors \u2014 they are context "
            "mistakes: the measure runs, but the filter or row context it saw wasn't what the "
            "author expected.",
            "The professional discipline: compose complex measures from small, tested base "
            "measures instead of writing one giant CALCULATE. If [Sales Amount] is right, then "
            "[Sales YoY %] built on top of it is dramatically easier to trust and debug.",
        ],
        why_items=[
            "A measure that returns the wrong number silently is worse than one that errors \u2014 "
            "the report still renders, and stakeholders make decisions on wrong figures.",
            "Composed, branched measures give you a natural test surface: verify [Sales Amount] in "
            "one visual, then every derived measure inherits that correctness.",
            "Everything later in this workshop \u2014 dashboards, RLS, performance tuning \u2014 assumes "
            "the DAX measure layer is trustworthy. Fixing it later is far more expensive than "
            "getting it right now.",
        ],
        footer="Lab connection: every exercise in this module builds on a base [Sales Amount] "
               "measure defined in Exercise 1 \u2014 that pattern is the whole point.",
        script=[
            "Open with the framing sentence: 'In advanced Power BI, DAX is where business logic "
            "lives.' The definition of \"sales\", \"gross margin\", or \"YTD\" for the whole "
            "organization is literally one measure in this model. That's a big responsibility.",
            "Explain the failure mode concretely. Most incorrect reports don't crash \u2014 they show "
            "a wrong number. A measure that meant to sum sales at the customer grain gets dropped "
            "into a totals row and quietly double-counts, or a YTD measure runs against a "
            "malformed date table and returns blank. The engine did exactly what was asked; the "
            "author asked for the wrong thing given the context.",
            "Introduce the composition discipline that will run through the whole module: never "
            "write one giant nested CALCULATE when you can express it as [Base] \u2192 [Derived]. In "
            "this lab, [Sales Amount] is the base; [Sales YTD], [Sales Prior Year], [Sales YoY], "
            "[Sales YoY %], [Rolling 90 Day Sales] all branch off of it. If [Sales Amount] passes "
            "its test in a simple table visual, every downstream measure is testing on a solid "
            "floor.",
            "Close with a transition into the next slide: 'To compose measures safely, we have to "
            "be able to reason about context \u2014 what filters and what row scope is my measure "
            "seeing at the moment it evaluates? That is topic 2.'",
        ]
    )
    page += 1

    # 4. Topic 2 - Evaluation context
    table_slide(
        prs, 2, "Evaluation Context", page=page,
        headers=["Context type", "What it is in this lab", "Where you see it"],
        col_widths=[2.4, 5.4, 4.1],
        rows=[
            ["Filter context",
             "The set of filters currently applied to the model: slicers on Territory or Date, "
             "the row/column of the current matrix cell, page and visual filters.",
             "A matrix by DimCustomer[CustomerName] with a Territory slicer \u2014 each cell of "
             "[Sales Amount] sees a different filter context."],
            ["Row context",
             "The 'current row' scope that exists inside calculated columns and inside iterator "
             "functions like SUMX, AVERAGEX, FILTER over FactSales.",
             "A calculated column FactSales[LineTotal] = FactSales[Quantity] * "
             "FactSales[UnitPrice] \u2014 row context is implicit."],
            ["Query context",
             "The DAX query the visual generates when it runs \u2014 it defines the initial filter "
             "context before any CALCULATE modifies it.",
             "Performance Analyzer 'Copy query' shows the EVALUATE / SUMMARIZECOLUMNS the visual "
             "sent to the engine."],
            ["Visual totals",
             "The totals row of a matrix evaluates its own filter context (all customers) \u2014 "
             "not the sum of the row cells above it.",
             "Grand total of [Sales Amount] recomputes from scratch; that is why totals sometimes "
             "'don't add up' when a measure isn't purely additive."],
        ],
        note="Lab tie-in: Exercise 1 has learners build [Sales Amount], [Quantity], and "
             "[Gross Margin], then drop them into a matrix by customer and product category with "
             "Territory and Date slicers \u2014 exactly to feel these context shifts firsthand.",
        script=[
            "This is the single most important slide in the module. If learners leave today "
            "understanding evaluation context, everything else \u2014 CALCULATE, filter modifiers, "
            "time intelligence \u2014 falls into place. If they don't, no amount of syntax practice "
            "will save them.",
            "Walk each row of the table. Filter context is the easy one to see: it is literally "
            "the slicers plus the axis of the visual. Emphasize that every cell of a matrix has "
            "its own filter context \u2014 that is why the same [Sales Amount] returns a different "
            "number in every cell without you writing any conditional logic.",
            "Row context is trickier because it is invisible in most measures. It only exists "
            "inside calculated columns and inside iterators \u2014 SUMX, AVERAGEX, FILTER, RANKX. Use "
            "the Exercise 1 calculated column example: FactSales[LineTotal] = FactSales[Quantity] "
            "* FactSales[UnitPrice] works only because DAX gives you an implicit 'current row' "
            "scope inside a calculated column. That same expression written as a measure would "
            "error because there is no current row.",
            "Point at the visual-totals row and explain why the grand total of an average or a "
            "ratio measure often surprises people: the totals row is a *separate* evaluation with "
            "its own (unfiltered) filter context, not a sum of the cells above. This is not a "
            "bug \u2014 it is the engine being consistent.",
            "Close with the transition: 'Row and filter context are what you get for free. In the "
            "next topic, we learn how CALCULATE lets us intentionally *change* filter context, "
            "and how it converts row context into filter context \u2014 the mechanic called context "
            "transition.'",
        ]
    )
    page += 1

    # 5. Topic 3 - Context transition
    content_slide(
        prs, 3, "Context Transition and CALCULATE", page=page,
        lead_items=[
            "CALCULATE is the only function that can modify filter context. Every filter modifier "
            "in this module \u2014 ALL, REMOVEFILTERS, ALLEXCEPT, KEEPFILTERS, TREATAS \u2014 is "
            "actually an argument to CALCULATE.",
            "Context transition: when a measure is called inside a row context (a calculated "
            "column or an iterator like SUMX), CALCULATE implicitly converts the current row into "
            "an equivalent filter context before the measure evaluates.",
            "Calculated columns run once at refresh in row context and are stored. Measures run "
            "at query time in filter context. Same DAX expression can produce very different "
            "results depending on which one you write.",
            "Iterators (SUMX, AVERAGEX, FILTER, RANKX) create row context row-by-row over a "
            "table \u2014 use them when the calculation must happen per row before aggregation.",
        ],
        why_items=[
            "Understanding context transition is the difference between a measure that works in a "
            "card and mysteriously breaks in a matrix, versus one you can trust everywhere.",
            "Preferring measures over calculated columns keeps aggregation logic responsive to "
            "slicers instead of being frozen at refresh time.",
            "Naming the mechanic ('context transition') makes it debuggable \u2014 when a measure "
            "surprises you inside SUMX, you now know exactly what to look for.",
        ],
        footer="Lab connection: Exercise 1 uses one calculated column deliberately to feel row "
               "context, then Exercise 2 shifts to CALCULATE-based measures for everything real.",
        script=[
            "Introduce CALCULATE as the single most important function in DAX \u2014 not because of "
            "what it computes, but because it is the *only* function that changes filter context. "
            "Every other pattern in this module is a variation on 'CALCULATE with some kind of "
            "filter argument.'",
            "Explain context transition using the SUMX example. When you write SUMX(FactSales, "
            "[Sales Amount]), the iterator walks FactSales row by row. On each row it calls "
            "[Sales Amount]. But [Sales Amount] is a measure \u2014 it needs filter context, not row "
            "context. Context transition is the engine automatically converting 'the current "
            "FactSales row' into 'a filter that keeps only that row' before [Sales Amount] runs. "
            "That is why the totals come out right.",
            "Use the calculated-column-vs-measure comparison from Exercise 1 as the concrete "
            "example. FactSales[LineTotal] = Quantity * UnitPrice as a *column* is fine \u2014 row "
            "context is implicit and the value is stored. Writing 'Total Line Amount = Quantity * "
            "UnitPrice' as a *measure* will error, because a measure has no current row. And "
            "conversely, a column can't respond to a slicer; a measure can. That is why we prefer "
            "measures for anything a report user should be able to slice.",
            "End with an instructor prompt: 'When you get to Exercise 2 and start writing "
            "CALCULATE, keep asking yourself out loud: what filter context did this measure "
            "inherit, and what am I about to change?' That habit alone prevents most DAX bugs.",
        ]
    )
    page += 1

    # 6. Topic 4 - Filter modification (table)
    table_slide(
        prs, 4, "Filter Modification: ALL, REMOVEFILTERS, ALLEXCEPT, KEEPFILTERS, TREATAS",
        page=page,
        headers=["Function", "What it does", "When to use in this lab"],
        col_widths=[2.4, 5.4, 4.1],
        rows=[
            ["ALL",
             "Removes filters from a table or column and returns the underlying table for "
             "iteration and ranking.",
             "Denominator of a share measure, and inside RANKX where you need the full "
             "unfiltered customer set to rank against."],
            ["REMOVEFILTERS",
             "Same filter-clearing behavior as ALL, but expressed only as a CALCULATE modifier \u2014 "
             "reads more clearly when you are not iterating.",
             "Product Sales Share = DIVIDE([Sales Amount], CALCULATE([Sales Amount], "
             "REMOVEFILTERS(DimProduct)))."],
            ["ALLEXCEPT",
             "Clears filters from a table except the columns you name \u2014 keeps a chosen grain "
             "and drops the rest.",
             "Territory-level share within a customer segment: clear customer filters but keep "
             "DimTerritory[TerritoryName]."],
            ["KEEPFILTERS",
             "Adds to the existing filter context instead of overwriting it \u2014 the intersection "
             "of the current filter and the new one wins.",
             "'Sales for Enterprise customers only' inside a report already filtered by Region \u2014 "
             "KEEPFILTERS preserves the Region filter."],
            ["TREATAS",
             "Applies the values of a disconnected table (or an unrelated column) as if they "
             "were a filter on a model column.",
             "MetricSelector disconnected table in Exercise 6: TREATAS pushes the user's slicer "
             "choice onto a real column."],
        ],
        note="Concept note from README: choose REMOVEFILTERS when you want to clear one table, "
             "ALL when you also need the returned table for iteration/ranking, ALLEXCEPT when "
             "you want to preserve a named grain, and TREATAS when a disconnected selection "
             "must be applied to a model column.",
        script=[
            "This table is a reference card learners will come back to \u2014 tell them so up front. "
            "The five functions all modify filter context, but each has a different intent, and "
            "using the wrong one gives you a measure that 'runs but lies.'",
            "Walk the rows in order. For ALL vs REMOVEFILTERS, be explicit about the difference: "
            "they do the same *filter* thing, but ALL also returns a table you can iterate. If "
            "you are inside RANKX or SUMX, use ALL. If you are just clearing filters inside "
            "CALCULATE, REMOVEFILTERS reads more clearly and signals your intent to the next "
            "author who reads the code.",
            "ALLEXCEPT is the one that trips people up. Reframe it as: 'clear everything on this "
            "table *except* the grain I explicitly name.' The Exercise 2 use case is the classic "
            "one \u2014 you want to clear customer-level filters but keep the territory grain so "
            "you can compute a share within territory.",
            "KEEPFILTERS is the opposite of the default CALCULATE behavior. Normally CALCULATE "
            "overwrites: 'set the Category filter to Bikes' replaces whatever was there. With "
            "KEEPFILTERS, the new filter intersects with the existing one \u2014 so if the user "
            "already sliced to a specific region, the region filter is preserved. Use it any time "
            "your measure has an opinion about a filter but shouldn't override user slicers.",
            "Close on TREATAS by previewing Exercise 6: the MetricSelector disconnected table "
            "isn't related to anything in the model. TREATAS is how you take the user's slicer "
            "choice from that disconnected table and *treat it as* a filter on a real column. It "
            "is the cleanest way to build measure-switching UX.",
        ]
    )
    page += 1

    # 7. Topic 5 - Measure branching
    content_slide(
        prs, 5, "Measure Branching", page=page,
        lead_items=[
            "Define small, formatted base measures once: [Sales Amount] = SUM(FactSales"
            "[SalesAmount]), [Quantity] = SUM(FactSales[OrderQuantity]), [Gross Margin] = "
            "[Sales Amount] - [Total Cost].",
            "Build every derived measure from those bases: [Sales YoY] wraps [Sales Amount] in "
            "a time-intelligence CALCULATE; [Product Sales Share] divides [Sales Amount] by a "
            "REMOVEFILTERS version of itself; [Sales YoY %] divides [Sales YoY] by [Sales Prior "
            "Year].",
            "Naming discipline: base measures are nouns ([Sales Amount]); derived measures append "
            "the transformation ([Sales YTD], [Sales Prior Year], [Sales YoY %]). Consistency "
            "makes the measure list self-documenting.",
            "Set format strings on the Measure tools ribbon before the measure is used elsewhere "
            "\u2014 that formatting flows automatically into every visual.",
        ],
        why_items=[
            "One place to fix logic: if the definition of 'sales' ever changes (net vs gross, "
            "excluding returns), you edit [Sales Amount] and every derived measure inherits it.",
            "Testable in isolation: verify each base measure against a known value in a card "
            "visual first, then trust it downstream.",
            "Readable DAX: [Sales YoY] = [Sales Amount] - [Sales Prior Year] is instantly "
            "understandable; a nested CALCULATE that recomputes SUM(SalesAmount) twice is not.",
            "Reusable across the whole model \u2014 the same [Sales Amount] powers cards, matrices, "
            "time intelligence, ranking, and the calculation group in Exercise 7.",
        ],
        footer="Lab connection: Exercise 1 defines the base measures; every later exercise "
               "(2\u20138) branches off them. The 'Concept note: measure branching and naming' in "
               "the README is worth reading verbatim to students.",
        script=[
            "This is the professional-discipline slide. Measure branching is not a DAX feature "
            "\u2014 it is a design habit. Sell it that way: it is how professional Power BI "
            "developers stay sane on a model with 200 measures.",
            "Walk the concrete example. In this lab, we build three base measures in Exercise 1: "
            "[Sales Amount], [Quantity], [Gross Margin]. Every single downstream measure \u2014 "
            "YTD, prior year, YoY, YoY %, rolling 90 day, product share, top-N flag, dynamic "
            "metric switch, and every calculation-group item in Exercise 7 \u2014 branches from "
            "those three. The base measures are a contract: 'this is what sales means in this "
            "model.'",
            "Use the naming example. [Sales Amount] is the noun. Adding a time context appends a "
            "suffix: [Sales YTD], [Sales Prior Year], [Sales YoY], [Sales YoY %]. When you scan "
            "the measure list alphabetically, everything that starts with 'Sales' groups "
            "together and the transformation is obvious from the name. That is not cosmetic \u2014 "
            "it is documentation.",
            "Give the format-string tip explicitly: set the currency, decimal places, and "
            "thousands separator on the base measure once via the Measure tools ribbon, and it "
            "propagates. If you forget and set it per-visual later, you will fix it in twenty "
            "places instead of one.",
            "Transition into the next topic: 'Now that we have base measures, the first thing "
            "we usually want to branch is time \u2014 YTD, prior year, YoY. That is topic 6.'",
        ]
    )
    page += 1

    # 8. Topic 6 - Time intelligence (table)
    table_slide(
        prs, 6, "Time Intelligence", page=page,
        headers=["Measure", "Expression pattern (Exercise 3)", "What it answers"],
        col_widths=[2.6, 5.9, 3.4],
        rows=[
            ["Sales YTD",
             "CALCULATE([Sales Amount], DATESYTD(DimOrderDate[Date]))",
             "Sales from start of year through the currently filtered date."],
            ["Sales Prior Year",
             "CALCULATE([Sales Amount], SAMEPERIODLASTYEAR(DimOrderDate[Date]))",
             "The same period one year ago \u2014 baseline for YoY."],
            ["Sales YoY",
             "[Sales Amount] - [Sales Prior Year]",
             "Absolute change vs the same period last year."],
            ["Sales YoY %",
             "DIVIDE([Sales YoY], [Sales Prior Year])",
             "Growth rate; DIVIDE handles the zero/blank denominator."],
            ["Rolling 90 Day Sales",
             "VAR LastDate = MAX(DimOrderDate[Date]) RETURN CALCULATE([Sales Amount], "
             "DATESINPERIOD(DimOrderDate[Date], LastDate, -90, DAY))",
             "Smooths spiky daily data over a moving window."],
            ["Date table prerequisite",
             "DimOrderDate must be marked as the date table, contiguous, and cover the full fact "
             "range (validated in Exercise 3, step 1).",
             "All the above return BLANK or wrong values if the date table is malformed."],
        ],
        note="Lab tie-in: Exercise 3 walks these measures top to bottom \u2014 validate the date "
             "table first, then build YTD, Prior Year, YoY, YoY %, and Rolling 90 Day in that "
             "order and verify each in a matrix by month before moving on.",
        script=[
            "Time intelligence is the pattern learners were most eager to use in Module 1 and "
            "couldn't yet. Frame it that way: 'This is the one you have been waiting for, and "
            "the entire pattern is measure branching plus a filter modifier.'",
            "Walk the table top to bottom. Notice that every derived measure is one thin "
            "CALCULATE wrapping the base [Sales Amount] measure. That is measure branching in "
            "action \u2014 [Sales YTD] doesn't re-sum FactSales[SalesAmount]; it wraps the trusted "
            "base measure.",
            "Highlight the date-table prerequisite row explicitly. The single most common "
            "'time intelligence doesn't work' bug is a broken date table: gaps, non-contiguous "
            "dates, date table not marked, or the fact table joined on a date-time column with "
            "time components. Exercise 3 step 1 exists specifically to prevent that class of "
            "bug \u2014 don't let students skip it.",
            "Use the Rolling 90 Day example to introduce variables casually: VAR LastDate = "
            "MAX(...) is written once and reused, which is both more readable and slightly "
            "cheaper to evaluate. This is a preview of the optimization topic later.",
            "End with the validation instruction: in Exercise 3 they will put all five measures "
            "into a matrix by month with year on rows. They should see YTD ramp inside a year "
            "and reset each January, Prior Year offset one column left, YoY difference match, "
            "and YoY % handle the empty first year cleanly. If any of that is off, the fix is "
            "almost always in the date table, not the DAX.",
        ]
    )
    page += 1

    # 9. Topic 7 - Semi-additive measures
    content_slide(
        prs, 7, "Semi-Additive Measures", page=page,
        lead_items=[
            "Transaction facts (FactSales) are fully additive across time \u2014 summing "
            "[Sales Amount] across January, February, and March gives the Q1 total.",
            "Snapshot facts (inventory on hand, account balances, headcount, backlog) are "
            "*not* additive across time \u2014 summing end-of-month inventory across three months "
            "does not equal end-of-quarter inventory.",
            "The DAX pattern is 'last value' or 'last non-blank': at a month level show the "
            "value from the last date in the month; at a quarter or year level show the value "
            "from the last date in the quarter or year \u2014 not the sum.",
            "Typical patterns: CALCULATE([Balance], LASTDATE(DimOrderDate[Date])) or a variable "
            "capturing MAX of the visible date and filtering to that.",
        ],
        why_items=[
            "Wrong semi-additive handling produces silent, catastrophic over-counting \u2014 an "
            "inventory 'total' of 12x what actually exists.",
            "The mistake is easy to make because DAX will happily sum a snapshot measure by "
            "default \u2014 there is no error, just a wrong number.",
            "Naming these measures explicitly ([Ending Inventory], [End-of-Period Balance]) "
            "signals to future report authors that these do not sum across time.",
        ],
        footer="Lab connection: Exercise 4 is deliberately conceptual \u2014 the Contoso dataset is "
               "transactional \u2014 but the pattern from the DAX Pattern Reference must be "
               "understood before students meet a real snapshot fact.",
        script=[
            "Semi-additive is the topic students underestimate. They meet it, nod, and then "
            "months later ship an inventory report that over-counts by a factor of twelve. So "
            "invest time here even though our lab dataset is transactional.",
            "Draw the distinction concretely. FactSales is a transaction fact \u2014 every row is "
            "an event, and events add up across time: yesterday's sales plus today's sales "
            "equals a two-day total. That is fully additive.",
            "Contrast that with inventory. If you have 100 units on hand at end of January, 100 "
            "at end of February, 100 at end of March, you do not have 300 units at end of Q1 \u2014 "
            "you have 100. Same for account balances, headcount, backlog, open cases. Any "
            "measure that represents 'a level or a stock, not a flow' is semi-additive.",
            "Walk the DAX pattern. The standard approach is CALCULATE against LASTDATE of the "
            "visible date range, or capture MAX of the visible date in a variable and filter to "
            "it. Point students at the DAX Pattern Reference doc for the full canonical "
            "version \u2014 there is no need to memorize it, just know when to look it up.",
            "Close with the discussion prompt from Exercise 4: ask learners what snapshots they "
            "deal with at their own organization \u2014 inventory, headcount, contract value, "
            "open opportunities. Naming their own semi-additive cases makes the pattern stick.",
        ]
    )
    page += 1

    # 10. Topic 8 - Calculation groups
    content_slide(
        prs, 8, "Calculation Groups", page=page,
        lead_items=[
            "Problem: with N base measures ([Sales Amount], [Gross Margin], [Quantity]) and M "
            "time variants (YTD, Prior Year, YoY, YoY %, Rolling 90), you would maintain N\u00d7M "
            "measures \u2014 fifteen for just three bases.",
            "Calculation groups solve this with one placeholder: SELECTEDMEASURE(). One "
            "calculation item YTD = CALCULATE(SELECTEDMEASURE(), DATESYTD(DimOrderDate[Date])) "
            "applies to every base measure the user picks.",
            "In the lab (Exercise 7): a 'Time Intelligence' calculation group with items "
            "Current, MTD, QTD, YTD, Fiscal YTD, Prior Year, YoY Change, YoY Change %, Rolling "
            "90 Days \u2014 all defined with SELECTEDMEASURE().",
            "Requires 'Discourage implicit measures' to be enabled. Authoring paths: native "
            "Power BI Desktop (Model view \u2192 Calculation group), TMDL View for PBIP/Git, or "
            "Tabular Editor when external tools are approved.",
        ],
        why_items=[
            "Massive reduction in measure count and maintenance surface: one YTD item covers "
            "every current and future base measure.",
            "Consistent behavior: every base measure gets the *same* YTD logic, not fifteen "
            "hand-written variants that quietly drift over time.",
            "AZURE GOVERNMENT: this feature is Verify for Gov \u2014 native Desktop authoring "
            "depends on Desktop version; TMDL, XMLA endpoint, and Tabular Editor all require "
            "tenant and workstation policy validation before use.",
            "Conceptual alternate path (README): if Tabular Editor or XMLA is blocked, hand-"
            "write [Sales Prior Year], [Gross Margin Prior Year] etc. and understand why the "
            "calculation group would have been better.",
        ],
        footer="Lab connection: Exercise 7 is the calculation group lab \u2014 native Desktop "
               "authoring is the default; TMDL View and Tabular Editor paths are Verify for Gov "
               "and optional.",
        script=[
            "Motivate the feature by showing the maintenance problem first. If we already have "
            "three base measures and want five time variants each, that is fifteen hand-written "
            "measures \u2014 and every one of them is a copy-paste of the same time-intelligence "
            "CALCULATE with a different base measure name. That is a maintenance nightmare "
            "waiting to happen.",
            "Introduce SELECTEDMEASURE() as the trick that makes calculation groups work. It is "
            "a placeholder that resolves at query time to whichever base measure the user "
            "actually put on the visual. So YTD = CALCULATE(SELECTEDMEASURE(), "
            "DATESYTD(DimOrderDate[Date])) is a single definition that works for [Sales "
            "Amount], [Gross Margin], [Quantity], and any base measure you add later.",
            "Walk the Exercise 7 layout concretely. The group is named 'Time Intelligence', the "
            "column is 'Time Calculation', and the items are Current, MTD, QTD, YTD, Fiscal "
            "YTD, Prior Year, YoY Change, YoY Change %, and Rolling 90 Days. Users drop 'Time "
            "Calculation' on a slicer or matrix column and one base measure on the values \u2014 "
            "each cell of the matrix now shows a different time variant of the same base "
            "measure.",
            "Pause on the Azure Government note. Calculation groups are Verify for Gov because "
            "authoring paths vary: native Desktop authoring depends on version; TMDL View "
            "assumes PBIP; Tabular Editor is an external tool subject to workstation policy. "
            "In a classroom on a locked-down tenant, do the concept in native Desktop only, or "
            "skip to the conceptual alternate path in the README where you hand-write the "
            "equivalent measures.",
            "Transition: 'Once base and time-intelligence logic is handled, the next common "
            "pattern report authors want is ranking \u2014 who are my top customers, and how do I "
            "make that respect the report's slicers?'",
        ]
    )
    page += 1

    # 11. Topic 9 - Ranking and Top N
    table_slide(
        prs, 9, "Ranking and Top N",
        page=page,
        headers=["Piece", "Pattern from Exercise 5", "Behavior"],
        col_widths=[2.6, 5.6, 3.7],
        rows=[
            ["Customer Sales Rank",
             "RANKX(ALL(DimCustomer[CustomerName]), [Sales Amount], , DESC, DENSE)",
             "Rank customers by [Sales Amount] across the whole customer set."],
            ["Is Top 5 Customer",
             "IF([Customer Sales Rank] <= 5, 1, 0)",
             "Flag measure you can drop into a visual-level filter."],
            ["ALL vs ALLSELECTED",
             "ALL(DimCustomer) ignores slicers entirely; ALLSELECTED(DimCustomer) respects "
             "outer slicers (Territory, Date) but ignores the visual's own row filter.",
             "Ranking within the currently sliced context needs ALLSELECTED, not ALL."],
            ["Visual-level filter",
             "Add [Is Top 5 Customer] = 1 to the visual-level filter on the customer bar chart.",
             "Cleaner than TOPN-inside-CALCULATE; totals still recompute correctly."],
            ["'Other' bucket concept",
             "Compute [Sales Amount] for non-top-N customers via SUMX of ALL minus TOPN.",
             "Preserves the true total when a bar chart is filtered to Top N."],
        ],
        note="Lab tie-in: Exercise 5 has learners try the same ranking with ALL and with "
             "ALLSELECTED under a Territory slicer \u2014 the difference is the whole point of the "
             "exercise.",
        script=[
            "Ranking is the topic where 'which filter modifier?' becomes visible and testable in "
            "seconds. Frame it that way: 'Same RANKX expression, two different filter modifiers, "
            "two very different answers.'",
            "Walk the pattern in order. First, [Customer Sales Rank] uses RANKX over "
            "ALL(DimCustomer[CustomerName]). The ALL is essential \u2014 without it, RANKX would "
            "iterate only the customers already visible in the current filter context, and "
            "every customer's rank would be 1.",
            "Introduce [Is Top 5 Customer] as a flag measure. This is a professional pattern: "
            "don't try to do the filter and the ranking in one measure \u2014 build a rank measure "
            "and a flag measure, then use the flag on a visual-level filter. It reads cleaner "
            "and totals behave correctly.",
            "Spend real time on ALL vs ALLSELECTED. Have learners predict what happens if they "
            "slice Territory to 'Northwest' with ALL vs ALLSELECTED. ALL ignores the Territory "
            "slicer, so the rank is against the whole company. ALLSELECTED honors the "
            "Territory slicer, so the rank is 'top 5 within Northwest.' Ninety-nine times out "
            "of a hundred the report author wanted ALLSELECTED and used ALL by accident.",
            "Preview 'Top N + Other' briefly. Filtering a chart to Top 5 hides the other "
            "customers but also hides their revenue \u2014 the visible bars no longer add up to the "
            "true total. A common finishing touch is a synthetic 'Other' bar computed as "
            "[Sales Amount] on ALL customers minus [Sales Amount] on the top 5. Mention it as "
            "an extension exercise learners can try after class.",
        ]
    )
    page += 1

    # 12. Topic 10 - Dynamic report logic
    content_slide(
        prs, 10, "Dynamic Report Logic: Titles, Selected Values, Measure Switching", page=page,
        lead_items=[
            "Dynamic title measure: uses SELECTEDVALUE(DimTerritory[TerritoryName], \"All "
            "Territories\") to show a friendly title that updates with the slicer and has a "
            "fallback when nothing (or multiple) is selected.",
            "Disconnected table pattern: a MetricSelector table (Sales Amount / Gross Margin / "
            "Quantity) with no relationships \u2014 users pick one via a slicer, and DAX reads the "
            "choice with SELECTEDVALUE(MetricSelector[Metric]).",
            "Measure switching: [Selected Metric] = SWITCH(TRUE(), SELECTEDVALUE(MetricSelector"
            "[Metric]) = \"Sales Amount\", [Sales Amount], \"Gross Margin\", [Gross Margin], "
            "\"Quantity\", [Quantity], [Sales Amount]).",
            "Always include a fallback branch \u2014 for empty selection, multi-select, or an "
            "unrecognized value \u2014 so the visual never renders BLANK by accident.",
        ],
        why_items=[
            "One page with a metric switcher can replace three near-duplicate pages, cutting "
            "report maintenance in a third.",
            "Dynamic titles give stakeholders a 'you are looking at X for Y' anchor in every "
            "screenshot they share \u2014 huge for report literacy.",
            "Disconnected tables cleanly separate 'user choice' from model relationships \u2014 "
            "there's no risk of the metric slicer accidentally filtering FactSales.",
            "SWITCH(TRUE(), ...) is more readable and easier to extend than nested IFs; the "
            "final fallback branch is your safety net for multi-select and blank cases.",
        ],
        footer="Lab connection: Exercise 6 builds all three patterns \u2014 dynamic title, "
               "MetricSelector disconnected table, and [Selected Metric] with SWITCH \u2014 and "
               "explicitly validates the fallback branch.",
        script=[
            "This slide is where the deck moves from 'correct DAX' to 'DAX that improves report "
            "UX.' Frame it as: 'The same techniques that let us reason about context also let "
            "us respond to the user's context \u2014 slicers, selections, and choices.'",
            "Walk the dynamic title pattern first. SELECTEDVALUE returns the currently filtered "
            "value if exactly one value is in context, and its second argument otherwise. So a "
            "title measure like \"Sales for \" & SELECTEDVALUE(DimTerritory[TerritoryName], "
            "\"All Territories\") gracefully handles single-select, multi-select, and no-"
            "select. Drop that measure into a card visual with no border and you have a live "
            "page title.",
            "Introduce the disconnected table concept using MetricSelector from Exercise 6. It "
            "is a manually created table with a single column of choices \u2014 Sales Amount, "
            "Gross Margin, Quantity \u2014 and no relationships to anything. The point of not "
            "connecting it is that we control how the selection is applied, via DAX.",
            "Walk the SWITCH(TRUE(), ...) pattern line by line. Emphasize the final fallback "
            "expression: what does [Selected Metric] return when the user clears the slicer or "
            "multi-selects? If you don't provide a fallback, the visual will just show BLANK \u2014 "
            "which looks like a broken report. Always end SWITCH with a sensible default (in "
            "Exercise 6, we default back to [Sales Amount]).",
            "Close by tying this to earlier topics: 'This is TREATAS territory too \u2014 if you "
            "wanted to filter FactSales rows by the disconnected selection instead of just "
            "returning a measure, TREATAS is how you would push the choice onto a real column.'",
        ]
    )
    page += 1

    # 13. Topic 11 - Debugging and optimization
    content_slide(
        prs, 11, "Debugging and Optimization", page=page,
        lead_items=[
            "Variables first: VAR PriorYearValue = CALCULATE(...) RETURN [Sales Amount] - "
            "PriorYearValue \u2014 write each intermediate once, name it, reuse it. Faster to read, "
            "often faster to run.",
            "Test in a simple visual: card first, then table with one dimension, then matrix. If "
            "a measure surprises you in a complex matrix, isolate it in a card and re-add "
            "context piece by piece until it breaks.",
            "Performance Analyzer (View \u2192 Performance analyzer) captures each visual's DAX "
            "query and DAX/render duration \u2014 Gov-ready, no external tool needed.",
            "DAX Studio (Verify for Gov) adds Server Timings and Query Plan for deeper "
            "diagnostics \u2014 requires validated workstation policy and tenant settings; not a "
            "requirement for this module.",
            "Branch, don't nest: two [Sales Amount] references in one measure should become "
            "one VAR; a nested SUM inside CALCULATE should almost always be replaced by the "
            "base measure.",
        ],
        why_items=[
            "Variables make measures readable \u2014 which makes them debuggable, which makes them "
            "trustworthy.",
            "Testing in a card visual removes filter-context noise so you can see the raw "
            "value; complex matrices are where measures hide their bugs.",
            "Performance Analyzer is the required, Gov-ready tool \u2014 every learner should be "
            "comfortable clicking Start recording, refreshing the page, and reading the "
            "durations.",
            "External tools stay optional and Verify for Gov \u2014 professional practice is to "
            "reach for the built-in tool first, then escalate.",
        ],
        footer="Lab connection: Exercise 8 has learners rewrite a repeated-logic measure using "
               "variables and measure branching, and optionally compare with Performance "
               "Analyzer.",
        script=[
            "Debugging DAX is a workflow, not a feature. Sell it as a discipline: variables, "
            "simple test visuals, Performance Analyzer, and \u2014 only when tenant policy "
            "allows \u2014 DAX Studio.",
            "Walk the variables pattern with a concrete before/after. If your measure "
            "references [Sales Prior Year] three times, the engine will happily evaluate it "
            "three times too. Capturing it in VAR PriorYearValue once names the intermediate and "
            "guarantees it is computed once. Same for Rolling 90 Days \u2014 VAR LastDate = "
            "MAX(...) is written once and reused.",
            "Give the isolation workflow: card, then table with one dimension, then matrix. Any "
            "time a measure returns a surprising number in a complex matrix, drop it into a "
            "card next to it with the same slicers cleared \u2014 does the surprise persist? Add "
            "one axis at a time until it appears, and that axis is your bug.",
            "Cover Performance Analyzer as the default tool. View \u2192 Performance analyzer, "
            "Start recording, refresh visuals. Each visual reports DAX time, visual time, and "
            "'other'. You can copy the DAX query the visual generated and paste it into a new "
            "table visual to test edits. All of this is native, Gov-ready, and doesn't require "
            "any external policy sign-off.",
            "Handle the DAX Studio question deliberately: it is a powerful tool, but it is "
            "Verify for Gov \u2014 workstation policy, external tool approval, and XMLA endpoint "
            "settings all need validation before it goes into a required workflow. Treat it as "
            "optional and mention it as 'the next step once your environment allows it.'",
        ]
    )
    page += 1

    # 14. Topic 12 - Azure Government considerations (table)
    table_slide(
        prs, 12, "Azure Government Considerations",
        page=page,
        headers=["Capability", "Status", "What to validate"],
        col_widths=[3.4, 2.2, 6.3],
        rows=[
            ["Core DAX language",
             "Gov-ready",
             "None \u2014 core DAX runs in Desktop and the engine. Fully supported."],
            ["CALCULATE and filter modifiers",
             "Gov-ready",
             "None \u2014 ALL, REMOVEFILTERS, ALLEXCEPT, KEEPFILTERS, TREATAS are core DAX."],
            ["Time-intelligence functions",
             "Gov-ready",
             "Requires a valid, marked date table \u2014 not an environment restriction."],
            ["Ranking, Top N, dynamic titles, measure switching",
             "Gov-ready",
             "Core DAX and visual interaction. Disconnected tables are fine."],
            ["Calculation groups",
             "Verify for Gov",
             "Native Desktop authoring depends on Desktop version; TMDL, XMLA endpoint, "
             "Tabular Editor, capacity behavior, and customer workstation policy all require "
             "validation before use."],
            ["Performance Analyzer",
             "Gov-ready",
             "Built-in Desktop feature; no tenant or external dependency."],
            ["DAX Studio",
             "Verify for Gov",
             "External tool. Validate customer workstation policy, tenant XMLA endpoint, and "
             "Service model connectivity before making it required."],
            ["Tabular Editor and other external tools",
             "Verify for Gov",
             "Validate workstation policy and tenant connectivity; keep as optional/alternate "
             "path only."],
        ],
        note="Rule of thumb: if a technique needs only Power BI Desktop and core DAX, it is "
             "Gov-ready. Anything that reaches the XMLA endpoint or invokes an external "
             "process needs an explicit Verify for Gov check before it lands in required lab "
             "steps.",
        script=[
            "This slide exists to make Azure Government sponsorship visible and predictable. "
            "Frame it as: 'The core DAX language does not change between commercial and Gov. "
            "What changes is the tooling around it.'",
            "Walk the top of the table quickly. Everything we covered in topics 1\u20137, plus "
            "topics 9\u201310, is Gov-ready because it runs entirely inside Desktop and the "
            "engine. No tenant policy, no external tool, no XMLA endpoint required.",
            "Slow down on calculation groups. Native Desktop authoring depends on the Desktop "
            "version being new enough to expose the ribbon command. TMDL View assumes PBIP "
            "projects with Git integration \u2014 not always available on locked-down "
            "workstations. Tabular Editor is an external tool subject to policy. In a Gov "
            "classroom, prefer native Desktop authoring, and if that isn't available, take the "
            "conceptual alternate path from the README and hand-write the equivalent measures.",
            "For DAX Studio, be explicit: it is a fantastic tool, but it is Verify for Gov. In "
            "this module we teach Performance Analyzer as the required diagnostic; DAX Studio "
            "is 'next step once your environment supports it,' not 'required today.'",
            "Close with the rule of thumb from the footer: Desktop plus core DAX is safe; "
            "anything that reaches XMLA or launches an external process needs a Verify for Gov "
            "check. That heuristic will serve learners for every future advanced Power BI "
            "feature they meet.",
        ]
    )
    page += 1

    # 15. Topic 13 - Knowledge check topics
    content_slide(
        prs, 13, "Common Mistakes, Validation, and Production Readiness", page=page,
        lead_items=[
            "Common context mistake: writing an aggregation as a calculated column when it "
            "should be a measure \u2014 the column freezes at refresh, ignores slicers, and "
            "bloats the model.",
            "Common filter-modifier mistake: using ALL when you meant ALLSELECTED, or "
            "REMOVEFILTERS(FactSales) when you meant REMOVEFILTERS(DimProduct). The measure "
            "runs, the totals lie.",
            "Common time-intelligence mistake: date table not marked, or joined on a date-time "
            "column with time components \u2014 YTD and prior-year measures return BLANK.",
            "Common measure-branching mistake: rewriting SUM(FactSales[SalesAmount]) inline in "
            "five derived measures instead of branching from [Sales Amount] \u2014 five places to "
            "fix when the definition changes.",
            "Validation approach: card \u2192 table \u2192 matrix. Every base measure verified in a "
            "card with known filters before any derived measure is trusted.",
        ],
        why_items=[
            "Naming the failure modes out loud makes them recognizable when learners encounter "
            "them in their own work \u2014 that is the whole point of a knowledge check.",
            "The validation checklist gives a repeatable, teachable process that survives "
            "beyond this classroom \u2014 not just 'trust me, it's right.'",
            "Production-ready DAX is boring on purpose: consistent naming, formatted base "
            "measures, variables, and simple test visuals. Nothing flashy, everything "
            "traceable.",
        ],
        footer="Instructor prompt: ask each learner to name the one context mistake they are "
               "most likely to make in their own reports \u2014 that meta-awareness is the goal of "
               "this module.",
        script=[
            "This is the last teaching slide before the lab and wrap-up. Use it as a lightning "
            "review, not new material. Read each 'common mistake' aloud and ask the room if "
            "they have seen it \u2014 chances are half the group has.",
            "Spend a moment on the calculated-column-vs-measure mistake, because it is the one "
            "that experienced Excel users make most often \u2014 they instinctively reach for a "
            "column because 'that is where the calculation lives' in a spreadsheet. In a "
            "semantic model, aggregation belongs in a measure so the number responds to "
            "slicers and doesn't bloat the storage engine.",
            "For the time-intelligence mistake, remind them of the Exercise 3 validation step: "
            "before writing YTD, confirm the date table is marked and contiguous. Nine times "
            "out of ten, 'my YTD is blank' is a date table problem.",
            "Walk the card \u2192 table \u2192 matrix validation ladder as a repeatable process. Every "
            "new measure should get its own card visual with a known filter (a specific year, "
            "a specific customer) before it is trusted in a matrix. That habit alone catches "
            "most bugs before they ship.",
            "Close with the instructor prompt: 'Which of these mistakes are you most likely to "
            "make in your own reports?' Getting learners to name their own likely failure mode "
            "makes the next two weeks of applied work much more focused.",
        ]
    )
    page += 1

    # 16. Module lab walkthrough (checklist)
    checklist_slide(
        prs, "Module Lab Walkthrough",
        items=[
            "Exercise 1: Row context vs filter context \u2014 build [Sales Amount], "
            "[Quantity], [Gross Margin]; observe context in a matrix with slicers.",
            "Exercise 2: Context transition and CALCULATE \u2014 [Product Sales Share] with "
            "REMOVEFILTERS and a KEEPFILTERS comparison.",
            "Exercise 3: Advanced time intelligence \u2014 validate DimOrderDate, then Sales "
            "YTD, Prior Year, YoY, YoY %, and Rolling 90 Days.",
            "Exercise 4: Semi-additive measures \u2014 conceptual review of ending-balance and "
            "last-non-blank patterns from the DAX Pattern Reference.",
            "Exercise 5: Dynamic Top N and ranking \u2014 [Customer Sales Rank], [Is Top 5 "
            "Customer]; compare ALL vs ALLSELECTED.",
            "Exercise 6: Dynamic titles and measure switching \u2014 SELECTEDVALUE title, "
            "MetricSelector disconnected table, [Selected Metric] with SWITCH.",
            "Exercise 7: Calculation groups (Verify for Gov) \u2014 'Time Intelligence' group "
            "in Model view; native Desktop path required, TMDL and Tabular Editor optional.",
            "Exercise 8: DAX optimization \u2014 rewrite a repeated-logic measure using "
            "variables and measure branching; optionally compare with Performance Analyzer.",
        ],
        kicker="Lab walkthrough",
        page=page,
        script=[
            "Frame the lab as a directed sequence: exercises 1\u20133 build the foundation, 4 is a "
            "quick concept detour, 5\u20136 add reporting patterns learners will use immediately, "
            "and 7\u20138 are the professional-practice capstone.",
            "Call out the Verify for Gov item explicitly: Exercise 7 has three paths (native "
            "Desktop, TMDL View, Tabular Editor). In a classroom on a Gov tenant, do native "
            "Desktop authoring only \u2014 that is Gov-ready \u2014 and treat TMDL and Tabular "
            "Editor as awareness only.",
            "Set expectations for pacing: exercises 1\u20133 will take the majority of the "
            "hands-on time because context and time intelligence are the concepts learners "
            "need to internalize. Exercises 5\u20138 build faster because they are pattern "
            "applications of what 1\u20134 already established.",
            "Remind learners to test each new measure in a card visual before dropping it into "
            "a matrix \u2014 that habit is what makes the lab tractable in the time available.",
            "Encourage them to keep the DAX Pattern Reference (linked from the module README) "
            "open in a browser tab throughout the lab \u2014 it has the canonical form of every "
            "pattern in this deck.",
        ]
    )
    page += 1

    # 17. Knowledge check & discussion (checklist)
    checklist_slide(
        prs, "Knowledge Check and Discussion",
        items=[
            "Base measures exist for [Sales Amount], [Quantity], [Gross Margin] and are "
            "formatted (Measure tools ribbon).",
            "Time-intelligence measures (YTD, Prior Year, YoY, YoY %, Rolling 90 Days) return "
            "expected values by month against a validated DimOrderDate.",
            "Semi-additive pattern is explained \u2014 learners can identify inventory, "
            "headcount, or balance scenarios in their own work.",
            "Ranking measures work at the intended filter scope \u2014 learners can articulate "
            "the ALL vs ALLSELECTED difference under a Territory slicer.",
            "Dynamic title measure has a sensible fallback for empty or multi-select "
            "conditions (SELECTEDVALUE second argument).",
            "Measure switching handles missing or multi-select cases via a SWITCH(TRUE(), "
            "\u2026, [fallback measure]) final branch.",
            "Calculation groups are implemented natively in Power BI Desktop, or reviewed "
            "conceptually as Verify for Gov.",
            "DAX optimization applied: variables replace repeated expressions; derived "
            "measures branch from base measures instead of re-summing.",
            "External tooling (DAX Studio, Tabular Editor, XMLA) is labeled Verify for Gov "
            "and not required for the module to be complete.",
            "Common context mistake self-assessment: each learner names one failure mode they "
            "personally need to watch for.",
        ],
        kicker="Validation checklist",
        page=page,
        script=[
            "Use this slide as a structured group review, not a quiz. Read each item aloud and "
            "get a thumbs-up around the room \u2014 anywhere you see hesitation, that is the "
            "concept to revisit before the module closes.",
            "The first three items are objective and easy to check. The next three "
            "(ranking scope, dynamic title fallback, SWITCH fallback) are where learners "
            "typically claim understanding but haven't actually tested \u2014 push them to "
            "demonstrate the fallback path in their own report.",
            "For the calculation groups item, accept 'conceptual review' as a pass in Gov "
            "classrooms. The teachable moment is being able to articulate why native Desktop "
            "authoring is Gov-ready and why TMDL and Tabular Editor need validation.",
            "The DAX optimization item is about habit, not any specific measurement \u2014 look "
            "for evidence in their code that variables and measure branching are being used "
            "reflexively.",
            "Close with the self-assessment item: 'Name one context mistake you are most "
            "likely to make.' That meta-awareness carries them into Module 3 (Power Query) and "
            "every subsequent module in the workshop.",
        ]
    )
    page += 1

    # 18. Closing
    closing_slide(
        prs, MODULE_NO,
        next_module="Module 03 \u2014 Advanced Power Query and Data Transformation",
        subtitle="Learners now have a trusted, testable DAX measure layer \u2014 base measures, "
                 "time intelligence, ranking, and dynamic report logic \u2014 built on top of the "
                 "Module 1 semantic model.",
        page=page,
        script=[
            "Wrap up by naming the transformation that happened today: learners walked in with "
            "a working semantic model from Module 1 and are walking out with a trusted, "
            "testable, composable measure layer on top of it. That layer is what every "
            "downstream report will build on.",
            "Reinforce the professional discipline: measure branching, context awareness, "
            "variables, and simple test visuals. Everything else \u2014 calculation groups, "
            "ranking, dynamic titles \u2014 is a specific application of those four habits.",
            "Preview Module 3, Advanced Power Query and Data Transformation. Point out the "
            "logical arc: Module 1 shaped the model, Module 2 gave it trusted business logic "
            "in DAX, and Module 3 tightens the pipeline that feeds it \u2014 M language patterns, "
            "dataflows, and refresh strategy.",
            "Thank the room, remind them to keep the DAX Pattern Reference bookmarked, and "
            "invite questions or feedback before the break.",
        ]
    )

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    prs.save(str(OUT_PATH))
    print(f"Saved: {OUT_PATH}")


if __name__ == "__main__":
    build()
