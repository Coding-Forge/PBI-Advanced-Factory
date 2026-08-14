#!/usr/bin/env python3
"""
Builds the Lab 01 (Advanced Semantic Modeling) instructor deck.
Run from repo root: python tools/pptx-labs/build_lab01.py
Output: modules/01-advanced-semantic-modeling/assets/advanced-semantic-modeling.pptx
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from slide_kit import (
    new_presentation, title_slide, agenda_slide, section_break_slide,
    content_slide, table_slide, diagram_slide, bridge_diagram_slide,
    checklist_slide, closing_slide,
)

OUT_PATH = Path(__file__).resolve().parent.parent.parent / \
    "modules" / "01-advanced-semantic-modeling" / "assets" / "advanced-semantic-modeling.pptx"

MODULE_NO = 1
TITLE = "Advanced Semantic Modeling"
SUBTITLE = "Building a governed, reusable star schema for Contoso Advanced Manufacturing"

AGENDA_TOPICS = [
    "Why semantic modeling matters",
    "From flat files to analytical models",
    "Star schema design",
    "Relationship design",
    "Role-playing dimensions",
    "Bridge tables",
    "Composite models and storage modes",
    "Large semantic model considerations",
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
            "Welcome learners to Module 1. Frame this as the foundation module for the entire "
            "workshop: every later module \u2014 DAX, Power Query, report UX, performance, security "
            "\u2014 assumes the semantic model underneath is well-designed.",
            "Set the stakes early: a flat, ungoverned data export can still 'work' in a report, but "
            "it quietly produces slow visuals, duplicated business logic in DAX measures, and "
            "numbers that don't reconcile between reports. Today is about preventing that.",
            "Preview the lab: students will take a flat CSV sales export for Contoso Advanced "
            "Manufacturing and refactor it into a star schema with fact/dimension separation, "
            "role-playing dates, and a bridge table for multi-valued customer segments.",
            "Mention the Azure Government angle up front so it isn't a surprise later: most of this "
            "module is Gov-ready because it only uses local CSVs and core Desktop modeling features. "
            "Composite models, DirectQuery, and large semantic model features are 'Verify for Gov' "
            "and are treated as optional/conceptual only.",
        ]
    )
    page += 1

    # 2. Agenda
    agenda_slide(
        prs, MODULE_NO, AGENDA_TOPICS, page=page,
        script=[
            "Walk through the ten topics quickly \u2014 don't over-explain, just orient the room to the "
            "shape of the session: concepts first (1-3), relationship mechanics (4-6), advanced "
            "storage/scale topics (7-8), then the hands-on lab and wrap-up (9-10).",
            "Call out that topics 7 and 8 (composite models, large semantic models) are conceptual "
            "discussion only for most students \u2014 they are Verify-for-Gov and depend on tenant "
            "settings the classroom environment may not have enabled.",
            "Tell students the lab (topic 9) is where all of this becomes real: they will build the "
            "actual fact table, dimension tables, and relationships described in topics 2-6.",
        ]
    )
    page += 1

    # 3. Topic 1 - Why semantic modeling matters
    content_slide(
        prs, 1, "Why Semantic Modeling Matters", page=page,
        lead_items=[
            "Advanced Power BI starts with the model, not the visual canvas.",
            "A poor model shows up later as slow reports, overly complex DAX, and metrics that "
            "don't match between two reports built by different authors.",
            "Enterprise-grade models need three qualities: reusable (many reports can share one "
            "model), governed (naming, keys, and relationships follow a standard), and "
            "understandable (a new author can open it and know what belongs where).",
        ],
        why_items=[
            "Every later module in this workshop \u2014 DAX, Power Query, report UX, performance, "
            "security \u2014 builds directly on top of the model shape decided here.",
            "Fixing a bad model after 20 reports depend on it is far more expensive than designing "
            "it correctly in Lab 01.",
            "A governed model is what lets an organization certify a single 'source of truth' "
            "semantic model instead of every team rebuilding their own.",
        ],
        footer="Instructor prompt: ask the room to describe a report they've seen where numbers "
               "didn't match across two dashboards \u2014 was it a model problem or a DAX problem?",
        script=[
            "Open with a direct statement: 'Advanced Power BI starts with the model.' Everything "
            "else in this workshop \u2014 the DAX patterns in Module 2, the Power Query techniques in "
            "Module 3, even the report UX and performance modules \u2014 assumes you already have a "
            "clean, dimensional model underneath.",
            "Explain the failure mode concretely: when a model is just a wide flat table pretending "
            "to be a data model, authors compensate with increasingly complex DAX \u2014 nested "
            "CALCULATE statements, filter context hacks \u2014 to work around the missing structure. "
            "That complexity is a symptom, not a feature.",
            "Define the three qualities \u2014 reusable, governed, understandable \u2014 and tie each one "
            "to a concrete pain point: reusable avoids rebuilding the same logic in five different "
            "reports; governed means naming and keys are predictable so new authors don't guess; "
            "understandable means the model documents itself through table names, hidden keys, and "
            "relationship direction.",
            "Ask the discussion question from the slide footer and let 2-3 students answer before "
            "moving on. Use their answers to bridge into the next topic: most mismatched numbers "
            "trace back to grain problems, which is exactly what we cover next.",
        ]
    )
    page += 1

    # 4. Topic 2 - From flat files to analytical models
    content_slide(
        prs, 2, "From Flat Files to Analytical Models", page=page,
        lead_items=[
            "The lab's raw source, sales-flat.csv, is a reporting export: one row per sales order "
            "line, but with customer, product, and territory attribute text repeated on every row.",
            "Repeated text attributes (CustomerName, ProductCategory, TerritoryName, etc.) are the "
            "visible symptom of a flat file; the invisible risk is a hidden grain problem \u2014 you "
            "can't tell just by looking whether a row is unique per order, per line, or per shipment.",
            "The fix is always the same two moves: identify the true grain of the fact table, then "
            "split repeated attributes out into their own dimension tables.",
        ],
        why_items=[
            "A flat file is fine as a data *source* \u2014 it is not the final analytical model.",
            "Once grain is fixed and dimensions are split out, the same governed model can support "
            "many reports without duplicating business logic in every one of them.",
            "Making the grain explicit up front prevents silent double-counting later, which is one "
            "of the hardest DAX bugs to diagnose after the fact.",
        ],
        footer="Lab connection: Exercise 1 (Star schema refactor) does exactly this \u2014 splits "
               "sales-flat.csv into FactSales plus DimCustomer, DimProduct, and DimTerritory.",
        script=[
            "Bring up the actual source file: sales-flat.csv. Point out that it looks like a "
            "perfectly normal Excel-style export \u2014 one row per sales order line \u2014 but every row "
            "also repeats the customer's name, type, state, region; the product's name, category, "
            "subcategory; and the territory's name and region.",
            "Explain why that repetition is the tell-tale sign of a reporting export instead of an "
            "analytical model: if you group by CustomerName in Power BI against this flat table, it "
            "will 'work', but every calculation is now scanning far more repeated text than "
            "necessary, and there is no single place to fix a customer's attribute if it changes.",
            "Introduce the phrase 'hidden grain problem' \u2014 the grain (what one row represents) "
            "isn't documented anywhere in a flat file. You have to reverse-engineer it by testing: "
            "is SalesOrderLineKey actually unique? Could there be two rows for one order? This "
            "matters because measures like SUM() silently produce wrong totals if the grain is "
            "wrong and you don't realize it.",
            "Close the loop by explaining the fix is always the same recipe: 1) determine the true "
            "grain of the fact table (in this lab, transaction/order-line grain), 2) split every "
            "repeated attribute column into its own dimension table keyed by an ID, 3) leave only "
            "keys and numeric measures in the fact table. This is exactly what Exercise 1 in the lab "
            "has students do step by step.",
        ]
    )
    page += 1

    # 5. Topic 3 - Star schema design
    table_slide(
        prs, 3, "Star Schema Design", page=page,
        headers=["Concept", "What it means in this lab", "Why it matters"],
        col_widths=[2.6, 5.3, 4.0],
        rows=[
            ["Fact table grain", "FactSales is kept at transaction/order-line grain "
             "(SalesOrderLineKey is the unique row identifier).", "Every measure's meaning depends "
             "on knowing exactly what one fact row represents."],
            ["Dimension attributes", "DimCustomer, DimProduct, DimTerritory each hold only "
             "descriptive attributes plus their key.", "Attributes live in exactly one place, so "
             "updates and filters are consistent everywhere."],
            ["Surrogate / business keys", "CustomerKey, ProductKey, TerritoryKey act as the join "
             "keys between fact and dimension tables.", "Stable keys let relationships stay valid "
             "even if descriptive text (like a product name) changes."],
            ["Conformed dimensions", "DimTerritory is shared by both FactSales and FactTargets.", "One "
             "dimension can filter multiple fact tables consistently \u2014 actuals and targets slice "
             "the same way."],
            ["Model readability", "Keys are hidden from report view; table and column names read "
             "like business terms.", "A new report author can open the model and understand it "
             "without a data dictionary."],
        ],
        note="Lab tie-in: the exact keep/remove column lists for FactSales and each Dim table are "
             "spelled out in Exercise 1 of the README \u2014 follow them precisely so relationships "
             "in Exercise 1-3 resolve without ambiguity.",
        script=[
            "This is the conceptual heart of the module, so slow down here. Star schema means one "
            "central fact table (the 'many' side, holding transactions and numeric measures) "
            "surrounded by dimension tables (the 'one' side, holding descriptive attributes).",
            "Walk each row of the table. For fact table grain, stress that the grain decision comes "
            "first \u2014 before you write a single relationship \u2014 because every other decision "
            "depends on it. In this lab, grain is 'one row per sales order line.'",
            "For surrogate/business keys, explain the difference simply: this lab uses the "
            "business keys already present in the source (CustomerKey, ProductKey, TerritoryKey) "
            "rather than generating new integer surrogate keys, which is a perfectly valid approach "
            "for smaller, well-controlled synthetic datasets like this one. In larger enterprise "
            "warehouses, you'd often add a generated surrogate key layer, but that's out of scope "
            "here.",
            "For conformed dimensions, use the DimTerritory example directly from this lab: because "
            "the *same* DimTerritory table relates to both FactSales and FactTargets, a single "
            "territory slicer filters actuals and targets together consistently \u2014 that's the "
            "entire point of a conformed dimension.",
            "End by previewing that Exercise 1 in the lab gives students the *exact* column lists "
            "to keep and remove for every table \u2014 there's no guesswork, so if their relationships "
            "don't resolve later, the first thing to check is whether they followed those column "
            "lists precisely.",
        ]
    )
    page += 1

    # 6. Topic 4 - Relationship design
    content_slide(
        prs, 4, "Relationship Design", page=page,
        lead_items=[
            "Default to one-to-many relationships from a dimension (the 'one' side) into a fact or "
            "bridge table (the 'many' side).",
            "Cardinality should almost always be one-to-many in this workshop's models \u2014 many-to-"
            "many is a warning sign to re-examine the grain, not a design goal.",
            "Cross-filter direction should default to single, flowing from dimension into fact. "
            "Bidirectional filtering is a deliberate, documented exception \u2014 never a shortcut for "
            "unclear design.",
            "Watch for ambiguity: if Power BI can't determine a single filter path between two "
            "tables (for example DimProduct \u2192 DimProductCategory \u2192 FactTargets), it will refuse "
            "to create the relationship or mark it inactive.",
        ],
        why_items=[
            "Single-direction, one-to-many relationships are predictable: a slicer on a dimension "
            "always filters the fact table the same way, every time.",
            "Bidirectional and many-to-many relationships can create ambiguous filter paths that "
            "silently produce wrong totals \u2014 exactly the kind of bug that's painful to trace back.",
            "Getting relationship design right here means Module 2's DAX measures can stay simple "
            "instead of compensating for model ambiguity with CALCULATE and TREATAS gymnastics.",
        ],
        footer="Preview: FactTargets is stored at product-category grain while DimProduct is at "
               "individual-product grain \u2014 relating them directly creates a many-to-many risk, "
               "which is exactly why DimProductCategory exists (next topic covers the fix).",
        script=[
            "Set the default rule clearly: in this workshop, relationships should be one-to-many, "
            "single-direction, from dimension into fact. That's the safe, predictable 90% case.",
            "Explain cardinality using a plain description: 'one-to-many' means one row on the "
            "dimension side can match many rows on the fact side \u2014 one customer, many sales "
            "transactions. If Power BI reports 'many-to-many' between two tables you expected to be "
            "one-to-many, that's almost always a sign your grain or key assumptions are wrong, not "
            "something to just accept and move past.",
            "On cross-filter direction, be concrete about the risk of bidirectional filtering: it "
            "can create filter paths that loop back on themselves and produce wrong totals that are "
            "hard to spot because the report still runs \u2014 it just quietly shows the wrong number. "
            "Tell students: if you think you need bidirectional filtering, that's your cue to pause "
            "and discuss it with the class or instructor before flipping the switch.",
            "Foreshadow the FactTargets/DimProduct grain mismatch that's coming up in Exercise 1's "
            "DimProductCategory step \u2014 it's a perfect concrete example of exactly the ambiguity "
            "this slide is warning about, and having it primed now will make that exercise step "
            "click immediately when students get there.",
        ]
    )
    page += 1

    # 7. Topic 5 - Role-playing dimensions
    content_slide(
        prs, 5, "Role-Playing Dimensions", page=page,
        lead_items=[
            "FactSales carries three separate date columns \u2014 OrderDate, ShipDate, and "
            "InvoiceDate \u2014 that all logically relate to 'a date', but represent different "
            "business events.",
            "Two implementation patterns exist: duplicate the date dimension physically (DimOrderDate, "
            "DimShipDate, each with their own relationship), or keep one date table with multiple "
            "inactive relationships activated per-measure using USERELATIONSHIP.",
            "The lab's required path is the duplicated-table pattern \u2014 simpler to reason about "
            "for learners, and it avoids needing a USERELATIONSHIP wrapper in every date measure.",
        ],
        why_items=[
            "Without separate role-playing tables, Power BI can only relate one FactSales date "
            "column to a single shared DimDate at a time \u2014 you'd lose the ability to slice by "
            "ship date and order date independently in the same visual.",
            "This is a textbook example of why relationship *direction* and *count* decisions from "
            "the previous topic have real downstream consequences for what analysis is even "
            "possible.",
            "Understanding both patterns (duplicate table vs. USERELATIONSHIP) prepares students for "
            "Module 2, where USERELATIONSHIP appears again as a DAX-level technique.",
        ],
        footer="Lab connection: Exercise 2 has students build DimOrderDate and DimShipDate from the "
               "reusable fn_DimDate Power Query function (or the DAX CALENDAR pattern) and relate "
               "each to its matching FactSales date column.",
        script=[
            "Ask the room: 'How many separate dates does a single sales transaction actually have?' "
            "Let them notice OrderDate, ShipDate, and InvoiceDate all exist on the same fact row \u2014 "
            "this is the classic role-playing dimension scenario.",
            "Explain the term 'role-playing dimension' directly: it's one dimension \u2014 a calendar "
            "\u2014 playing multiple 'roles' against the same fact table. The calendar itself doesn't "
            "change; what changes is which date column on the fact table it's related to.",
            "Present both implementation options honestly, with tradeoffs: duplicating the date "
            "table (DimOrderDate, DimShipDate as separate physical tables, each actively related) is "
            "simple and each slicer works with plain-language 'order date' or 'ship date' filters "
            "without extra DAX. The alternative \u2014 one shared DimDate table with multiple inactive "
            "relationships activated via USERELATIONSHIP inside specific measures \u2014 saves a table "
            "but pushes complexity into every measure that needs date-role-specific behavior.",
            "Tell students this lab uses the duplicated-table pattern deliberately because it's "
            "easier for newer authors to reason about, and set expectations that USERELATIONSHIP "
            "will come back explicitly in Module 2 when they're more comfortable with DAX.",
        ]
    )
    page += 1

    # 8. Topic 6 - Bridge tables
    bridge_diagram_slide(
        prs, 6, "Bridge Tables", page=page,
        note="Customers can belong to multiple segments at once. DimSegment and DimCustomer both "
             "relate one-to-many into BridgeCustomerSegment \u2014 never relate a bridge table "
             "directly into a fact table.",
        script=[
            "Introduce the business problem first, before the model: a single customer in this "
            "dataset can belong to more than one market segment simultaneously \u2014 for example "
            "'Enterprise' and 'Government'. A simple one-to-many DimCustomer-to-Segment column can't "
            "represent that.",
            "Walk through the diagram (adapted here to show the bridge concept using the same fact/"
            "dimension visual language as star schema): BridgeCustomerSegment sits between "
            "DimCustomer and DimSegment, at 'customer-segment pair' grain \u2014 one row per valid "
            "customer/segment combination.",
            "Emphasize the critical rule: DimCustomer relates one-to-many into the bridge table, and "
            "DimSegment relates one-to-many into the bridge table \u2014 but the bridge table itself "
            "does NOT relate directly to FactSales. Filtering flows: Segment slicer \u2192 bridge \u2192 "
            "DimCustomer \u2192 FactSales.",
            "Mention the filter-direction consideration explicitly: getting a segment slicer to "
            "filter sales requires the bridge table's relationships to propagate correctly, which is "
            "exactly what Exercise 3 has students build and test.",
        ]
    )
    page += 1

    # 9. Topic 7 - Composite models and storage modes
    table_slide(
        prs, 7, "Composite Models and Storage Modes", page=page,
        headers=["Storage mode", "Behavior", "Gov note"],
        col_widths=[2.2, 6.3, 3.4],
        rows=[
            ["Import", "Data is loaded and cached in the model; fastest query performance, needs a "
             "scheduled refresh.", "Gov-ready \u2014 this lab's required path."],
            ["DirectQuery", "Queries pass through live to the source at report-view time; no caching, "
             "always current, but subject to source/gateway latency.", "Verify for Gov \u2014 depends "
             "on connector, gateway, and network path."],
            ["Dual", "A table can behave as Import or DirectQuery depending on the query context, "
             "chosen automatically by the engine.", "Verify for Gov \u2014 same dependencies as "
             "DirectQuery."],
            ["Composite model", "Mixes Import and DirectQuery tables in one model.", "Verify for Gov "
             "\u2014 validate source, gateway, Service, and tenant requirements first."],
            ["Hybrid table", "A single table split into an Import 'hot' partition and a DirectQuery "
             "'cold' partition via incremental refresh policy.", "Verify for Gov \u2014 validate "
             "licensing, capacity, and incremental refresh support."],
        ],
        note="Exercise 4 is a conceptual/discussion exercise only \u2014 identify Import vs. "
             "DirectQuery candidates and document tradeoffs for performance, freshness, source load, "
             "and feature support. Confirm tenant settings before treating this as hands-on.",
        script=[
            "This topic shifts from 'required, hands-on' to 'important to understand, but "
            "conceptual for most students.' Say that explicitly so nobody is confused about why "
            "Exercise 4 doesn't involve actually building a DirectQuery connection.",
            "Go through each storage mode row and anchor it to a plain tradeoff: Import is fast but "
            "stale until refresh; DirectQuery is always fresh but as slow as the source and gateway "
            "allow; Dual lets the engine pick the best of both per-query for small dimension tables; "
            "composite models mix Import fact tables with DirectQuery for huge or highly volatile "
            "tables; hybrid tables split one table's history into Import for old/stable data and "
            "DirectQuery for the most recent, fast-changing rows.",
            "Stress the Gov note column: everything except plain Import here is 'Verify for Gov', "
            "meaning before treating any of it as a real project decision, the student needs to "
            "confirm the target tenant's connector support, gateway availability, network path to "
            "the source, and licensing/capacity settings actually support it.",
            "Run Exercise 4 as a discussion, not a build: ask students, given what they know about "
            "FactSales/FactTargets and the dimensions, which tables would be good Import candidates "
            "(hint: everything in this lab, since it's small synthetic CSV data) versus which "
            "*could* need DirectQuery in a real enterprise scenario (very large, rapidly changing "
            "fact tables, or a real-time operational source).",
        ]
    )
    page += 1

    # 10. Topic 8 - Large semantic model considerations
    content_slide(
        prs, 8, "Large Semantic Model Considerations", page=page,
        lead_items=[
            "Cardinality reduction: split high-cardinality text columns out into smaller lookup "
            "dimensions (exactly what DimProductCategory does for ProductCategory).",
            "Aggregations: pre-summarized tables that Power BI automatically substitutes for a "
            "detailed fact table when a query doesn't need row-level detail, cutting query cost.",
            "Incremental refresh: only reprocess the partitions of a large fact table that actually "
            "changed, instead of a full reload every time.",
            "Capacity and tenant settings: large semantic model storage format and related features "
            "require specific Premium/Fabric capacity and tenant-level enablement.",
        ],
        why_items=[
            "These techniques exist specifically for scale \u2014 they matter once a fact table grows "
            "from thousands to hundreds of millions of rows, which this lab's synthetic dataset "
            "intentionally does not simulate.",
            "Cardinality reduction is the one technique students already practiced today, without "
            "necessarily realizing it, when they built DimProductCategory.",
            "All of this is 'Verify for Gov' \u2014 large model features depend on capacity SKU and "
            "tenant settings that must be confirmed before committing to them in a government "
            "tenant.",
        ],
        footer="Instructor note: this is intentionally a lighter-weight topic in Lab 01 \u2014 "
               "aggregations and incremental refresh get much deeper, hands-on treatment later in "
               "the performance-optimization module.",
        script=[
            "Frame this as a preview, not a deep dive \u2014 tell students explicitly that "
            "aggregations and incremental refresh will come back in much more depth in the "
            "Performance Optimization module later in the workshop. Today's job is just to know "
            "these concepts exist and roughly what problem each one solves.",
            "Connect cardinality reduction back to something they already did: point out that "
            "DimProductCategory, which they built to solve the FactTargets grain mismatch, is *also* "
            "a cardinality reduction technique \u2014 it's a smaller, low-cardinality lookup table that "
            "keeps relationships efficient. Same technique, two motivations (correctness AND scale).",
            "Briefly define aggregations and incremental refresh in one sentence each, using the "
            "language on the slide, but don't go deep \u2014 park detailed examples for the later "
            "module.",
            "Reinforce the Gov note one more time: capacity SKU and tenant settings gate all of "
            "this, so it should never be assumed available by default in a government tenant "
            "without checking first.",
        ]
    )
    page += 1

    # 11. Topic 9 - Module lab walkthrough
    checklist_slide(
        prs, "Module Lab Walkthrough", kicker="Topic 09 \u2014 What you'll build", page=page,
        items=[
            "Data overview: sales-flat.csv, customer-segments.csv, targets.csv (via raw GitHub URL)",
            "Exercise 1: Star schema refactor \u2014 FactSales + DimCustomer/Product/Territory/"
            "ProductCategory",
            "Exercise 2: Role-playing dimensions \u2014 DimOrderDate and DimShipDate",
            "Exercise 3: Bridge table \u2014 BridgeCustomerSegment + DimSegment",
            "Exercise 4: Composite model / DirectQuery comparison (conceptual, Verify for Gov)",
            "Target model: one central FactSales, single-direction relationships, hidden keys",
            "Validation checklist: confirm grain, naming, cardinality, and measure totals",
            "Optional commercial-enhanced path: composite/hybrid table exploration if tenant allows",
        ],
        script=[
            "This slide is the bridge from lecture into hands-on work \u2014 walk through it as a "
            "literal table of contents for what's about to happen at the keyboard.",
            "Point out the three raw data files and how each maps to an exercise: sales-flat.csv "
            "feeds Exercise 1's star schema refactor, customer-segments.csv feeds Exercise 3's "
            "bridge table, and targets.csv is what makes the DimProductCategory grain-mismatch "
            "problem real in Exercise 1.",
            "Remind students of the 'target model' shape one more time before they start: one "
            "central FactSales table, clean dimensions, single-direction relationships flowing from "
            "dimension into fact, and business keys hidden from report view. If their model doesn't "
            "look like that at the end, something needs fixing before moving to Module 2.",
            "Tell them Exercise 4 is discussion/documentation only \u2014 there is no DirectQuery "
            "connection to actually build in this classroom environment \u2014 so they should treat "
            "it as a written tradeoff exercise, not a technical build step.",
        ]
    )
    page += 1

    # 12. Topic 10 - Knowledge check and discussion
    checklist_slide(
        prs, "Knowledge Check & Discussion", kicker="Topic 10 \u2014 Wrap-up", page=page,
        items=[
            "The model uses a star schema with clear fact/dimension separation.",
            "Relationships are one-to-many, single-direction, wherever possible.",
            "Role-playing dates (order/ship) filter independently without ambiguity.",
            "The bridge table supports multi-segment customer analysis without duplicating rows.",
            "Design tradeoffs: when would you accept bidirectional filtering, and how would you "
            "document that exception?",
            "Gov readiness: which parts of today's model are Gov-ready vs. Verify for Gov, and why?",
            "Production review checklist: what would you check before approving this model for a "
            "real deployment?",
        ],
        script=[
            "Use this as a discussion-driven wrap-up rather than a quiz \u2014 the goal is to surface "
            "reasoning, not just recall facts.",
            "Pick 2-3 items and ask specific students to answer out loud, especially the design "
            "tradeoff and Gov readiness questions \u2014 those require synthesizing multiple topics "
            "from today rather than repeating a single slide.",
            "For the production review checklist question, connect it back to the lab's own "
            "Validation checklist (grain, naming, cardinality, filter direction, role-playing dates, "
            "bridge table, Gov labeling, and measure totals) \u2014 tell students this exact checklist "
            "is what they should run before considering any model 'done', not just in this lab but "
            "in real project work.",
            "Close by connecting forward: everything validated today \u2014 grain, keys, relationships "
            "\u2014 is the foundation Module 2 (Advanced DAX) will build measures on top of. If a "
            "measure misbehaves in Module 2, the first thing to re-check is whether the model "
            "foundation from today is actually correct.",
        ]
    )
    page += 1

    # 13. Closing
    closing_slide(
        prs, MODULE_NO, "Module 02: Advanced DAX \u2014 building governed, reusable measures on top "
                        "of today's star schema.",
        page=page,
        script=[
            "Congratulate the class on completing the foundation module \u2014 this is the module "
            "everything else depends on, and it's normal for the star-schema refactor exercise to "
            "take real focus and time.",
            "Remind students to keep their completed PBIP model open or close at hand, since Module "
            "2 builds DAX measures directly on top of the FactSales/Dim tables they just created.",
            "Take final questions before moving on, especially anything about the Verify-for-Gov "
            "topics (composite models, storage modes, large semantic models) since those are the "
            "most likely source of lingering confusion.",
        ]
    )

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    prs.save(str(OUT_PATH))
    print(f"Saved: {OUT_PATH} ({len(prs.slides.__iter__.__self__._sldIdLst)} slides)")


if __name__ == "__main__":
    build()
