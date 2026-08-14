#!/usr/bin/env python3
"""
Builds the Lab 03 (Advanced Power Query) instructor deck.
Run from repo root: python tools/pptx-labs/build_lab03.py
Output: modules/03-advanced-power-query/assets/advanced-power-query.pptx
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from slide_kit import (
    new_presentation, title_slide, agenda_slide,
    content_slide, table_slide, checklist_slide, closing_slide,
)

OUT_PATH = Path(__file__).resolve().parent.parent.parent / \
    "modules" / "03-advanced-power-query" / "assets" / "advanced-power-query.pptx"

MODULE_NO = 3
TITLE = "Advanced Power Query"
SUBTITLE = ("Staged, parameterized, reusable transformation patterns for the Contoso "
            "monthly orders pipeline")

AGENDA_TOPICS = [
    "Why Power Query architecture matters",
    "Staging query pattern",
    "Folder-combine pattern",
    "M language fundamentals",
    "Parameters",
    "Custom functions",
    "Query folding",
    "Native queries and source systems",
    "Data quality and errors",
    "Incremental refresh preparation",
    "Azure Government considerations",
    "Lab review",
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
            "Welcome learners to Module 3. Frame this module as the 'how the data actually gets "
            "in' half of the semantic-model story: Module 1 designed the shape of the model, "
            "Module 2 wrote measures on top of it, and Module 3 is about the transformation layer "
            "that feeds it \u2014 the M queries that turn raw monthly CSV extracts into clean, "
            "governed, model-ready tables.",
            "Set the stakes: in real projects, the vast majority of pain \u2014 slow refreshes, "
            "unexplained totals, broken relationships \u2014 traces back to Power Query, not to DAX or "
            "the report canvas. Today is about the patterns that prevent that: staging, "
            "parameters, custom functions, folding, and data quality checks.",
            "Preview the lab context: students work with three synthetic monthly order files "
            "(orders-2026-01/02/03.csv) plus a product-category reference, all pulled from raw "
            "GitHub URLs via the Web connector, and they build a staged pipeline that ends in a "
            "single FactOrders query.",
            "Call out the Azure Government angle up front: core Desktop authoring (staging, "
            "parameters, custom functions, folder-combine on local files) is Gov-ready. Query "
            "folding depends on the source, incremental refresh in the Service is Verify for Gov, "
            "and Dataflows Gen2 is commercial-focused. We'll flag each one as it comes up rather "
            "than saving it for the end.",
        ]
    )
    page += 1

    # 2. Agenda
    agenda_slide(
        prs, MODULE_NO, AGENDA_TOPICS, page=page,
        script=[
            "Walk the room through the fourteen items quickly, grouping them into three arcs: "
            "architecture and mechanics (topics 1-4), reusability (parameters and functions, "
            "topics 5-6), and production concerns (folding, native queries, data quality, "
            "incremental refresh, Gov, topics 7-11), followed by the lab review and wrap-up.",
            "Flag which topics are hands-on versus conceptual: staging, folder-combine, "
            "parameters, custom functions, data quality, and incremental refresh preparation are "
            "all hands-on in the lab. Query folding and native queries are largely conceptual "
            "here because our source is a Web-hosted CSV, which doesn't fold.",
            "Tell students the lab walkthrough slide near the end (topic 13) is the literal table "
            "of contents for their keyboard time \u2014 they don't need to memorize the agenda now, "
            "we'll re-anchor to the seven lab exercises before they start.",
        ]
    )
    page += 1

    # 3. Topic 1 - Why Power Query architecture matters
    content_slide(
        prs, 1, "Why Power Query Architecture Matters", page=page,
        lead_items=[
            "Transformation logic is a first-class part of the solution \u2014 not a one-time cleanup "
            "you do once and forget about.",
            "One monolithic query with 40 applied steps is technically valid M, but it is very "
            "hard to test, diff in source control, or hand off to another author.",
            "The fix is architectural: split the pipeline into raw / staging / final layers so "
            "each step's intent is visible in the query name itself (raw_Orders_2026_01, "
            "stg_OrdersCombined, FactOrders).",
            "Loaded queries are a governance decision: only the final model-ready queries should "
            "be load-enabled; raw and staging queries stay available for troubleshooting but do "
            "not ship into the model.",
        ],
        why_items=[
            "Named layers make intent reviewable \u2014 an instructor or reviewer can tell at a "
            "glance what each query is for without opening Advanced Editor.",
            "Disabling load on intermediate queries keeps the semantic model surface area small: "
            "only the tables that reports actually need are visible in the field list.",
            "Every later topic in this module \u2014 parameters, custom functions, folding, "
            "incremental refresh \u2014 assumes this raw / staging / final layering is already in "
            "place. Skip it and the later patterns get much messier.",
        ],
        footer="Lab connection: Exercise 1 (Staged query architecture) creates exactly this "
               "layering \u2014 raw_Orders_2026_01/02/03 \u2192 stg_OrdersCombined \u2192 FactOrders \u2014 with "
               "load disabled on everything except FactOrders.",
        script=[
            "Open with the mindset shift: Power Query is code. It lives in source control (PBIP "
            "format), it gets reviewed, and it deserves the same architectural care you'd give a "
            "SQL view stack or a Python pipeline. Treating it as 'a one-off cleanup wizard' is "
            "the root cause of most Power Query pain in real projects.",
            "Explain the monolithic-query failure mode concretely: when everything lives in a "
            "single query with 40+ generated steps, testing means running the whole thing end to "
            "end, and 'what changed?' in a code review becomes almost impossible to answer. "
            "Splitting the same logic into raw / staging / final layers is not more code \u2014 it's "
            "the same code, organized so its intent is visible in the object names.",
            "Anchor the pattern to the exact names students will use in Lab 03: raw queries are "
            "named with a 'raw_' prefix (raw_Orders_2026_01), staging queries with 'stg_' "
            "(stg_OrdersCombined), and the final model-loaded query gets the business name "
            "(FactOrders). Tell them the naming isn't cosmetic \u2014 it's the primary review signal.",
            "End with the load-enabled rule: only FactOrders gets loaded into the model. Every "
            "raw and staging query has Enable load unchecked. Ask the room why that matters, and "
            "steer them toward the answer: report authors should only see the tables they're "
            "meant to build visuals from, not the plumbing.",
        ]
    )
    page += 1

    # 4. Topic 2 - Staging query pattern (table)
    table_slide(
        prs, 2, "Staging Query Pattern", page=page,
        headers=["Layer", "Naming and role in this lab", "Load enabled?"],
        col_widths=[2.4, 7.5, 2.0],
        rows=[
            ["Raw source",
             "raw_Orders_2026_01, raw_Orders_2026_02, raw_Orders_2026_03 \u2014 one Web query per "
             "monthly file, minimal transformation, source lineage column added.",
             "No"],
            ["Staging",
             "stg_OrdersCombined \u2014 appends the three raw queries with Home > Append Queries as "
             "New, chosen with Three or more tables, before any typing or business logic.",
             "No"],
            ["Final model",
             "FactOrders \u2014 references stg_OrdersCombined, applies explicit data types, invokes "
             "fn_CleanText on text columns, filters out data-quality issues, and is the only "
             "table loaded to the semantic model.",
             "Yes"],
            ["Error review",
             "err_OrdersReview \u2014 a Reference (not Duplicate) of stg_OrdersCombined that keeps "
             "only rows with a non-empty DataQualityIssue column for reviewer follow-up.",
             "No (unless demoing)"],
            ["Reference table",
             "dim_ProductCategory \u2014 loads product-category-map.csv from the reference folder; "
             "text cleanup applied via fn_CleanText, load enabled so it can join to FactOrders "
             "in the model.",
             "Yes"],
        ],
        note="Lab tie-in: Exercise 1 builds the raw \u2192 staging \u2192 final layering and disables load "
             "on the raw and staging queries; Exercise 5 adds err_OrdersReview as a Reference (not "
             "a Duplicate) so both queries share one validated logic stack.",
        script=[
            "Walk the table row by row \u2014 this is the architectural blueprint for the entire "
            "lab, so it earns real airtime.",
            "For the raw layer, stress 'minimal transformation': the only things a raw_ query "
            "should do are connect to the source, promote headers if needed, and add a source "
            "file name column for lineage. Anything more (typing, cleanup, filtering) belongs "
            "downstream so raw stays a faithful mirror of the source.",
            "For the staging layer, call out the specific menu path from the lab: Home > Append "
            "Queries > Append Queries as New, then choose 'Three or more tables' and add all "
            "three raw queries in order. The 'as New' matters \u2014 it creates a new query "
            "(stg_OrdersCombined) instead of destructively modifying one of the raw queries.",
            "For the final model layer, this is where explicit types, fn_CleanText invocation, "
            "and the ValidRows filter (rows where DataQualityIssue = \"\") all live \u2014 it's the "
            "one query that ships into the semantic model.",
            "Draw the Reference-vs-Duplicate distinction explicitly for err_OrdersReview: "
            "Reference means it shares stg_OrdersCombined's logic upstream, so if you fix a bug "
            "in staging both queries benefit. Duplicate would copy the M and silently drift over "
            "time. This is a common Power Query anti-pattern worth naming.",
        ]
    )
    page += 1

    # 5. Topic 3 - Folder-combine pattern
    content_slide(
        prs, 3, "Folder-Combine Pattern", page=page,
        lead_items=[
            "Lab 03 uses the Web connector against three raw GitHub CSV URLs, but the same "
            "pattern applies to Folder connectors in production: point at a folder, filter to "
            "the expected file set, transform a single sample file, and let Power Query apply it "
            "to every file that matches.",
            "Always filter by file name or extension explicitly (e.g., orders-*.csv) to exclude "
            "hidden files, temp files (~$*.csv, *.tmp), and unrelated documents that end up in "
            "shared folders.",
            "The sample-file transformation runs once and is applied to every matching file, so "
            "any per-file cleanup goes there \u2014 not in the combined query.",
            "Schema consistency across files is not automatic. Add a source file name column "
            "before appending so lineage is preserved, and validate that column names and types "
            "match before applying final types downstream.",
        ],
        why_items=[
            "New monthly files should 'just appear' in the model at next refresh without editing "
            "queries \u2014 that is the entire promise of the folder-combine pattern, and it only "
            "works if the filter and sample-file transformation are correct.",
            "Filtering out hidden and temp files prevents refresh failures like 'the file "
            "~$orders-2026-04.csv could not be opened' that happen the first time a colleague "
            "opens the folder in Excel on a shared drive.",
            "Preserving source file lineage is critical for triage: when a data-quality issue "
            "surfaces in FactOrders, the reviewer needs to know which monthly file the bad row "
            "came from.",
        ],
        footer="Lab connection: Exercise 2 has students add a SourceFile column to each raw "
               "query, append them into stg_OrdersCombined, and confirm schema consistency "
               "before applying explicit data types.",
        script=[
            "Explain up front why the lab uses Web URLs instead of a Folder connector: the raw "
            "GitHub URLs are a classroom-friendly source that everyone can reach without shared "
            "storage, but the pattern \u2014 raw per file, add lineage, append, then type \u2014 is "
            "identical to production folder combine.",
            "Talk about the hidden-file trap concretely: in real projects, someone opens the "
            "shared folder in Excel, Excel creates a lock file called ~$orders-2026-04.csv, and "
            "the next Power Query refresh fails because it tries to parse that lock file as CSV. "
            "The fix is always to filter file names explicitly rather than 'combine everything'.",
            "Explain the sample-file transformation model: when you use Combine Files from a "
            "folder, Power Query creates a hidden 'Transform Sample File' query. Any change you "
            "make there is applied to every file. If you edit the combined query directly to fix "
            "a per-file issue, next month's file won't get the fix. Teach students to always go "
            "back to the sample file query for per-file logic.",
            "Close with the lineage point from Exercise 2: adding a SourceFile column before "
            "appending costs almost nothing and pays back the first time someone asks 'which "
            "month did this bad OrderID come from?' \u2014 it's a one-step troubleshooting win.",
        ]
    )
    page += 1

    # 6. Topic 4 - M language fundamentals
    table_slide(
        prs, 4, "M Language Fundamentals", page=page,
        headers=["Concept", "What it is", "Where you meet it in this lab"],
        col_widths=[2.3, 5.0, 4.7],
        rows=[
            ["Applied steps",
             "Ordered named expressions in a let/in block; each step is a variable the next step "
             "can reference by name.",
             "Every raw and staging query \u2014 rename cryptic step names like #\"Changed Type1\" to "
             "readable names before hand-editing."],
            ["Step references",
             "A step references the previous one by its exact name; renaming a step updates "
             "every reference automatically.",
             "Exercise 5 uses AddedDataQualityIssue as a named step that both FactOrders and "
             "err_OrdersReview downstream steps read from."],
            ["Tables",
             "The main tabular value type \u2014 what most Power Query UI actions produce.",
             "stg_OrdersCombined and FactOrders are both table values; Table.SelectRows and "
             "Table.TransformColumns operate on them."],
            ["Lists",
             "Ordered sequences in { } braces \u2014 used for column lists, file lists, and the "
             "issues collection built in Exercise 5.",
             "List.RemoveNulls({...}) inside AddedDataQualityIssue collects only the data-"
             "quality issues that actually applied to a row."],
            ["Records",
             "Named field bags in [ ] brackets \u2014 used for options passed to functions like "
             "Csv.Document and for row-level access.",
             "Each row in Table.AddColumn's each expression is a record; [OrderDate], "
             "[Quantity], [UnitPrice] read fields from it."],
            ["Generated vs handwritten M",
             "UI-generated M is verbose and correct; handwritten M in Advanced Editor is more "
             "concise but must be maintained by humans.",
             "Exercise 5's DataQualityIssue expression is intentionally handwritten \u2014 the UI "
             "cannot generate this pattern."],
        ],
        note="Instructor tip: encourage students to rename cryptic auto-generated step names "
             "(#\"Changed Type1\", #\"Filtered Rows\") to intent-based names before writing custom "
             "M \u2014 the resulting queries are dramatically easier to review.",
        script=[
            "This slide is the 'you need to be able to read M' checkpoint before the parameters "
            "and custom-functions topics. Don't try to teach M syntax exhaustively \u2014 focus on "
            "the four value types (table, list, record, function) and how applied steps chain.",
            "For applied steps, show the let/in structure on the board or in Advanced Editor: "
            "each step is just a named let-binding, and the query returns whatever the 'in' "
            "clause names. Renaming a step in the Applied Steps pane rewrites every reference to "
            "it in the M source \u2014 that's why renaming is safe and highly recommended.",
            "For lists and records, use the Exercise 5 example directly: the Issues expression "
            "builds a list ({...}) of issue strings, List.RemoveNulls trims the nulls, "
            "Text.Combine joins them with '; '. Meanwhile, [OrderDate] and [Quantity] are record "
            "field accesses \u2014 same syntax as records everywhere else in M.",
            "Wrap up with the generated-vs-handwritten distinction. Generated M is the safe "
            "default; it's what the UI produces, and it's fine to ship. Handwritten M is for "
            "cases where the UI can't express what you need (like Exercise 5's multi-issue "
            "check). Teach students that handwritten M lives in Advanced Editor, and they should "
            "rename the step first so its intent survives the round-trip.",
        ]
    )
    page += 1

    # 7. Topic 5 - Parameters
    table_slide(
        prs, 5, "Parameters", page=page,
        headers=["Parameter", "Type", "Suggested value", "Purpose"],
        col_widths=[2.8, 1.5, 4.7, 3.0],
        rows=[
            ["RawDataBaseUrl", "Text",
             "https://raw.githubusercontent.com/Coding-Forge/PBI-Advanced-Factory/main/data/",
             "Base URL for all Web-source CSVs; used in every raw_ query."],
            ["SourceFolderPath", "Text",
             "Blank, or a local folder path for offline delivery",
             "Optional placeholder for a Folder-connector delivery path."],
            ["EnvironmentName", "Text or List",
             "Dev (with Test, Prod as list values)",
             "Documents Dev/Test/Prod source switching without changing the Web-source path."],
            ["RangeStart", "Date/Time", "2026-01-01 00:00:00",
             "Lower bound for incremental-refresh filtering on FactOrders[OrderDate]."],
            ["RangeEnd", "Date/Time", "2026-04-01 00:00:00",
             "Upper bound for incremental-refresh filtering on FactOrders[OrderDate]."],
        ],
        note="Lab connection: Exercise 3 creates RawDataBaseUrl, SourceFolderPath, and "
             "EnvironmentName; Exercise 7 adds the RangeStart / RangeEnd DateTime pair used to "
             "filter FactOrders for incremental refresh preparation.",
        script=[
            "Frame parameters as the anti-hard-coding tool. Every hard-coded string in a Power "
            "Query script is a future migration problem \u2014 the base URL, environment name, and "
            "incremental-refresh window all belong in named parameters that a reviewer can find "
            "in one place.",
            "Walk the five required parameters using the table. RawDataBaseUrl is the only one "
            "that's structurally required for the Web-source path to work in the lab; every "
            "raw_Orders query builds its URL by concatenating RawDataBaseUrl with the monthly "
            "file name.",
            "Explain SourceFolderPath and EnvironmentName honestly: they are documentation "
            "parameters in this lab \u2014 SourceFolderPath is a placeholder for a Folder-connector "
            "delivery model, and EnvironmentName lets students see the shape of Dev/Test/Prod "
            "switching without actually building three source pipelines. Both are governance "
            "hygiene, not runtime dependencies.",
            "For RangeStart and RangeEnd, stress the exact type: Date/Time (not Date, not Text). "
            "Incremental refresh in the Service only recognizes these two parameter names, with "
            "these exact types, on a Date/Time column filter. Getting the type wrong is a very "
            "common Exercise 7 mistake.",
            "Transition into custom functions by noting that parameters and functions are the "
            "two reusability primitives in Power Query \u2014 parameters for values, functions for "
            "logic \u2014 and both live at the top of a well-organized query list.",
        ]
    )
    page += 1

    # 8. Topic 6 - Custom functions
    content_slide(
        prs, 6, "Custom Functions", page=page,
        lead_items=[
            "fn_CleanText is a nullable-text-in, nullable-text-out function that trims "
            "whitespace, cleans non-printable characters, and applies Text.Proper, returning "
            "null safely when input is null.",
            "The pattern: (inputText as nullable text) as nullable text => let Result = if "
            "inputText = null then null else Text.Proper(Text.Trim(Text.Clean(inputText))) in "
            "Result.",
            "Invoke it two ways \u2014 Transform > Invoke Custom Function for a single column, or "
            "Table.TransformColumns in Advanced Editor to clean several columns in one step "
            "(CustomerName, SalesChannel, ProductName, ProductCategory, ProductSubcategory).",
            "Test the function against known edge cases (null, empty string, leading/trailing "
            "whitespace, mixed case) before invoking it across the model.",
        ],
        why_items=[
            "One cleanup function applied consistently everywhere beats five copies of the same "
            "trim/proper/clean logic scattered across five queries \u2014 fewer places to fix bugs "
            "and no risk of drift.",
            "Explicit null handling matters: without the if inputText = null branch, "
            "Text.Trim(null) throws and breaks refresh on the first row with a missing customer "
            "name.",
            "Table.TransformColumns is the idiomatic way to apply a function to a set of "
            "columns without generating one Applied Step per column \u2014 cleaner M, faster to "
            "review, easier to add columns to later.",
        ],
        footer="Lab connection: Exercise 4 creates fn_CleanText and invokes it on the text "
               "columns of both FactOrders (CustomerName, SalesChannel) and dim_ProductCategory "
               "(ProductName, ProductCategory, ProductSubcategory).",
        script=[
            "Introduce custom functions as the DRY (don't repeat yourself) tool for M. Anywhere "
            "you find yourself copying the same three or four steps into multiple queries, "
            "that's a candidate for a function.",
            "Walk fn_CleanText line by line on the slide. The signature (inputText as nullable "
            "text) as nullable text is doing real work: it documents the contract, and Power "
            "Query's function-invocation UI will honor it \u2014 you can't accidentally pass a "
            "number.",
            "Explain the null branch explicitly: Text.Trim, Text.Clean, and Text.Proper all "
            "throw on null input. The if inputText = null then null else ... pattern makes the "
            "function null-safe, which matters because real source data has nulls in text "
            "columns all the time.",
            "Show both invocation styles from the lab. The Invoke Custom Function UI is great "
            "for a one-column demo. Table.TransformColumns is what you actually ship: one step, "
            "a list of {column, transform, type} triples, cleans every text column at once. "
            "Point students at the CleanedOrderText and CleanedProductText examples in the "
            "README as the concrete templates they'll use.",
            "Close by connecting forward: fn_CleanText is the pattern; students will meet other "
            "reusable-logic functions (fn_DimDate, error-wrapping helpers) in later modules, and "
            "they'll all follow this same signature/null-safety recipe.",
        ]
    )
    page += 1

    # 9. Topic 7 - Query folding
    content_slide(
        prs, 7, "Query Folding", page=page,
        lead_items=[
            "Query folding is Power Query's ability to translate M steps into the source "
            "system's native query language (usually SQL) and push work down to the source.",
            "What folds: filters, column selection, joins, group-by, and simple typing against "
            "connectors that support folding (SQL Server, Synapse, Snowflake, and similar).",
            "What breaks folding: adding an index column, custom columns with M functions like "
            "Text.Clean or fn_CleanText, referencing a step that already broke folding, and any "
            "step against a non-folding source (CSV, Excel, Web).",
            "Verify by right-clicking a step and choosing View Native Query \u2014 if the option is "
            "grayed out, folding stopped at or before that step.",
        ],
        why_items=[
            "When folding works, filtering a billion-row fact table down to 10,000 rows for a "
            "date range happens at the source in seconds \u2014 not by streaming a billion rows to "
            "Desktop and filtering client-side.",
            "The Web/CSV source in this lab does not fold, so folding is a concept slide today \u2014 "
            "but every step you write is either fold-preserving or fold-breaking, and knowing "
            "which is which is essential for the next SQL-backed project.",
            "Folding is why the order of steps matters: put filters and column selection as "
            "early as possible, and push any non-folding transformations (like invoking "
            "fn_CleanText) as late as possible so the smallest possible dataset reaches them.",
        ],
        footer="Gov note: query folding is Gov-ready as a Power Query capability, but hands-on "
               "folding validation is Verify for source \u2014 it depends on the specific connector "
               "and source system in the target tenant. Lab Exercise 6 is conceptual for that "
               "reason.",
        script=[
            "Set expectations honestly: Lab 03's source is a Web-hosted CSV, which does not "
            "fold. So this topic is conceptual today. But it is one of the most important "
            "concepts in the entire Power Query surface area for real projects, so we treat it "
            "seriously even without hands-on time.",
            "Define folding in one sentence: Power Query translates as many of your M steps as "
            "it can into the source's native query \u2014 usually SQL \u2014 so the work happens at "
            "the source. Then walk what folds versus what doesn't using the bullets on the "
            "slide.",
            "Give the concrete performance intuition: a billion-row SQL fact table filtered "
            "down to a month of data via a folded WHERE clause returns in seconds. The same "
            "filter after a fold-breaking step (say, an Index Column) streams all billion rows "
            "into Desktop first, then filters client-side. Same query, thousand-fold difference "
            "in runtime.",
            "Teach the View Native Query check: right-click any step, and if View Native Query "
            "is available, folding is still intact at that point. The moment it grays out, you "
            "know exactly which step broke folding \u2014 and you can often reorder steps to fix "
            "it.",
            "Close with the ordering rule of thumb: filter and select columns first, do "
            "expensive per-row transformations (like fn_CleanText) last. That way even on a "
            "partially-folding source, the fold covers the biggest data reduction.",
        ]
    )
    page += 1

    # 10. Topic 8 - Native queries and source systems
    content_slide(
        prs, 8, "Native Queries and Source Systems", page=page,
        lead_items=[
            "A native query is source-system SQL (or equivalent) passed directly through the "
            "Value.NativeQuery function or the connector's SQL text box, rather than expressed "
            "as M steps.",
            "Native queries can push complex logic (window functions, source-specific "
            "optimizations, hints) that Power Query M cannot generate on its own.",
            "The tradeoff: a native query hard-couples the report to a specific source dialect, "
            "requires source-side security review, and is much harder to review or refactor "
            "than equivalent M steps.",
            "Gateway and identity implications: native queries typically require the gateway "
            "account to have sufficient privileges on the source, and some tenants disable "
            "Value.NativeQuery entirely for governance reasons.",
        ],
        why_items=[
            "Prefer maintainable M steps for the 90% case. Reach for native queries only when "
            "there is a specific performance or feature reason M can't cover.",
            "Governance risk is real: a native query hidden inside a query is a security "
            "reviewer's blind spot \u2014 it should be flagged, documented, and reviewed with the "
            "same care as source-side stored procedures.",
            "Portability matters: an M-based transformation can often be repointed at a "
            "different source (dev/test/prod, or SQL Server to Synapse) with parameter changes. "
            "A native query pins you to the current source dialect.",
        ],
        footer="Gov note: native queries are Verify for Gov \u2014 connector, gateway, credential, "
               "and tenant policy must all support them before they ship into a production Gov "
               "model.",
        script=[
            "Frame native queries as a power tool with a real safety catch. They're not evil, "
            "but they're not the default choice either.",
            "Give the concrete example: if the source is SQL Server and you need a window "
            "function that Power Query M can't generate cleanly, dropping a Value.NativeQuery "
            "call with a hand-written T-SQL statement is a perfectly legitimate solution \u2014 "
            "provided it's documented and reviewed.",
            "Talk through the governance concerns explicitly. A native query means the M "
            "reviewer now also needs to review SQL for injection risk, security, and source "
            "impact. Some organizations disable Value.NativeQuery through tenant settings for "
            "exactly this reason. Ask the room whether they know if their tenant allows it.",
            "Close with the Gov flag: in Azure Government tenants, native queries fall under "
            "Verify for Gov \u2014 the connector, gateway, credentials, and any tenant policy on "
            "Value.NativeQuery all have to line up before a native-query pattern ships. It's "
            "not a decision to make in a lab; it's a project-level architecture decision.",
        ]
    )
    page += 1

    # 11. Topic 9 - Data quality and errors
    table_slide(
        prs, 9, "Data Quality and Errors", page=page,
        headers=["Technique", "How it's used in Exercise 5", "Why it matters"],
        col_widths=[2.6, 6.0, 3.4],
        rows=[
            ["Explicit types",
             "Every column on FactOrders is set to its intended type (Date/Time, Int64, "
             "Decimal, Text) as the last step before load.",
             "Prevents silent implicit conversions and surfaces bad values as errors instead of "
             "hiding them as blanks."],
            ["try / otherwise",
             "try Date.From([OrderDate]) otherwise null, try Number.From([Quantity]) otherwise "
             "null, and similar patterns inside AddedDataQualityIssue.",
             "Turns row-level parse failures into inspectable nulls instead of refresh-breaking "
             "errors."],
            ["Business-rule checks",
             "Quantity <= 0, UnitPrice <= 0, and Trim(ProductCode) = \"\" are flagged as "
             "issues alongside type failures.",
             "Technical validity is not the same as business validity \u2014 a zero-quantity order "
             "line parses fine but is still meaningless."],
            ["Error review query",
             "err_OrdersReview is a Reference of stg_OrdersCombined that keeps only rows where "
             "DataQualityIssue <> \"\", with the issue text preserved.",
             "Bad rows are triaged, not silently dropped \u2014 reviewers can see exactly why each "
             "row was excluded from FactOrders."],
            ["FactOrders filter",
             "FactOrders selects rows where DataQualityIssue = \"\" before applying final "
             "types.",
             "The model only contains rows that passed both technical and business validation, "
             "with an audit trail in err_OrdersReview."],
        ],
        note="Lab tie-in: Exercise 5 builds AddedDataQualityIssue once inside stg_OrdersCombined "
             "and reuses it in both err_OrdersReview and FactOrders via a Reference \u2014 one "
             "validation logic stack, two consumers.",
        script=[
            "Open by naming the two failure modes data quality handling has to distinguish. "
            "Technical failures are things Power Query can't parse (a date column with the "
            "value 'unknown', a numeric column with a stray letter). Business failures are "
            "things that parse fine but violate business rules (a Quantity of -3, a UnitPrice "
            "of 0, a blank ProductCode).",
            "Walk the AddedDataQualityIssue pattern from Exercise 5 carefully. The try / "
            "otherwise wrappers convert per-value parse failures into nulls, so the row "
            "survives long enough to be labeled. The Issues list then checks each business "
            "rule separately and collects the failing ones into a semicolon-delimited "
            "DataQualityIssue string. Rows where DataQualityIssue = \"\" passed everything.",
            "Emphasize that err_OrdersReview is a Reference of stg_OrdersCombined, not a "
            "Duplicate. Both err_OrdersReview and FactOrders read the same "
            "AddedDataQualityIssue step \u2014 they just filter it differently. If you fix a rule "
            "in staging, both queries benefit automatically. Duplicate would silently drift.",
            "Talk about the governance value: 'we silently threw away 47 rows' is a data quality "
            "problem waiting to be discovered by a business user. 'We excluded 47 rows and here "
            "is the reviewable list with reasons' is a data quality control. err_OrdersReview "
            "is the audit artifact.",
            "Close by tying to the earlier layering point: err_OrdersReview has load disabled by "
            "default (unless the instructor enables it to show in the model), because the audit "
            "artifact does not belong in the report surface \u2014 it belongs in the pipeline.",
        ]
    )
    page += 1

    # 12. Topic 10 - Incremental refresh preparation
    content_slide(
        prs, 10, "Incremental Refresh Preparation", page=page,
        lead_items=[
            "The two required parameter names are exact: RangeStart and RangeEnd, both of type "
            "Date/Time. The Service will not recognize any other names or types for an "
            "incremental refresh policy.",
            "Filter FactOrders on a Date/Time column (OrderDate) with a step of the form "
            "Table.SelectRows(#\"...\", each [OrderDate] >= RangeStart and [OrderDate] < "
            "RangeEnd) \u2014 half-open on the RangeEnd side to avoid double-counting boundary rows.",
            "In Desktop, the parameters act as manual filter values so students can preview a "
            "single window; in the Service, the incremental refresh policy overrides them for "
            "each partition automatically.",
            "Document the intended refresh and archive windows (e.g., 'keep 3 years, refresh "
            "the last 3 months') as part of the model documentation \u2014 the policy itself lives "
            "in the Service, and its settings must be validated against the target tenant.",
        ],
        why_items=[
            "Without RangeStart and RangeEnd wired correctly in Desktop, the incremental "
            "refresh policy in the Service will refuse to apply and the model will silently "
            "fall back to full refresh \u2014 costing performance and possibly capacity.",
            "The half-open filter ([OrderDate] < RangeEnd) is a subtle but critical detail: the "
            "closed form (<=) causes rows on the partition boundary to appear in two "
            "partitions and inflate totals.",
            "This is the prep half of incremental refresh; the policy application in the "
            "Service is a separate topic and is Verify for Gov \u2014 licensing, capacity, and "
            "workspace type all affect whether the policy is available.",
        ],
        footer="Gov note: Desktop preparation of RangeStart/RangeEnd is Gov-ready. Applying the "
               "policy in the Service is Verify for Gov \u2014 validate license, workspace, and "
               "tenant support before treating Exercise 7 as anything more than preparation.",
        script=[
            "This is the last hands-on topic before the Gov summary. Stress that Exercise 7 "
            "prepares the model for incremental refresh \u2014 it does not enable the policy. The "
            "policy is a Service-side configuration.",
            "Walk the required names and types once more, out loud, because they trip students "
            "up every cohort: RangeStart, RangeEnd, both Date/Time. Not Date. Not Text. The "
            "Service literally looks for those exact names.",
            "Show the filter expression on the slide. Emphasize the half-open interval: "
            "[OrderDate] >= RangeStart AND [OrderDate] < RangeEnd. If a student writes <= "
            "instead of <, midnight-boundary rows will show up in two partitions, and totals "
            "will silently inflate.",
            "Explain the Desktop/Service split concretely: in Desktop, you set RangeStart and "
            "RangeEnd to a short preview window (say, one month) so you can develop and test "
            "against a small slice. In the Service, the incremental refresh policy overrides "
            "these per partition automatically \u2014 you never edit the parameter values there.",
            "Close with the Gov note and forward-look: refresh policy application in the "
            "Service is Verify for Gov, and refresh policy tuning is covered in more depth in "
            "the later Performance Optimization module.",
        ]
    )
    page += 1

    # 13. Topic 11 - Azure Government considerations
    table_slide(
        prs, 11, "Azure Government Considerations", page=page,
        headers=["Feature", "Status", "Delivery note"],
        col_widths=[3.2, 2.8, 6.0],
        rows=[
            ["Power Query in Desktop",
             "Gov-ready",
             "Core local authoring \u2014 staging, parameters, custom functions, folder combine on "
             "local files are all fully supported."],
            ["Folder-combine pattern",
             "Gov-ready",
             "Uses local files in the core lab path \u2014 no external dependencies."],
            ["Parameters and custom functions",
             "Gov-ready",
             "Core Power Query features; no tenant or capacity gating."],
            ["Query folding",
             "Gov-ready / Verify for source",
             "The capability is core Power Query, but hands-on folding validation depends on "
             "the specific connector and source system in the tenant."],
            ["Incremental refresh preparation",
             "Verify for Gov",
             "Desktop RangeStart/RangeEnd prep is Gov-ready; applying the policy in the Service "
             "depends on license, workspace type, and tenant support."],
            ["Cloud dataflows",
             "Verify for Gov",
             "Validate Power BI Service / Fabric availability and tenant settings before "
             "committing to a dataflows-based delivery."],
            ["Dataflows Gen2",
             "Commercial-focused / Verify for Gov",
             "Fabric-related; do not require it in Gov labs unless explicitly validated."],
            ["Connectors",
             "Verify for Gov",
             "Connector availability varies by cloud, gateway, network path, and customer "
             "security policy."],
        ],
        note="Instructor guidance: when a student asks whether a technique 'works in Gov', the "
             "honest answer is almost always 'the Desktop capability yes, the Service policy or "
             "connector verify' \u2014 use this table to give consistent, defensible answers.",
        script=[
            "This is the consolidated Gov reference for the whole module. Don't try to re-teach "
            "each topic \u2014 use it as a quick sweep so students leave with a mental model of "
            "which techniques they can use freely and which need a tenant check.",
            "Point out the pattern: authoring capabilities inside Desktop are Gov-ready almost "
            "across the board, because Desktop itself is a client-side app operating on data "
            "the user already has access to. The Verify-for-Gov items are always the ones that "
            "cross into the Service (incremental refresh policy, cloud dataflows) or that "
            "depend on external systems (connectors, query folding on a specific source).",
            "Call out Dataflows Gen2 specifically as the outlier: it's Fabric-related, and "
            "Fabric feature availability in Gov clouds is on its own release cadence. Treat it "
            "as 'not required in this module' unless the local tenant has been explicitly "
            "validated.",
            "Encourage students to keep a version of this table for their own project work \u2014 "
            "not just for this lab. It's the same shape they should build for any new Power BI "
            "feature they want to adopt in a Gov tenant.",
        ]
    )
    page += 1

    # 14. Topic 12 - Lab review
    content_slide(
        prs, 12, "Lab Review", page=page,
        lead_items=[
            "Staged solution: raw_Orders_2026_01/02/03 \u2192 stg_OrdersCombined \u2192 FactOrders, with "
            "err_OrdersReview referencing staging for triage.",
            "Folder-combine equivalent: three raw Web queries with a SourceFile lineage column, "
            "appended via Append Queries as New into stg_OrdersCombined.",
            "Parameters and functions: RawDataBaseUrl, SourceFolderPath, EnvironmentName, "
            "RangeStart, RangeEnd; fn_CleanText invoked via Table.TransformColumns on the text "
            "columns of FactOrders and dim_ProductCategory.",
            "Validation: only FactOrders and dim_ProductCategory load; explicit types, "
            "null-safe cleanup, and DataQualityIssue-based row filtering are all in place; "
            "Gov-status flags are documented next to any Verify-for-Gov feature.",
        ],
        why_items=[
            "The end state is a semantic-model surface that a reviewer can read at a glance: "
            "two loaded tables, everything else load-disabled, named layers, and parameterized "
            "sources.",
            "Every pattern in this lab \u2014 staging, folder combine, parameters, functions, data "
            "quality, incremental refresh prep \u2014 was chosen because it survives real-world "
            "change: new monthly files, source moves, new columns, new validation rules.",
            "This is the pattern set later modules (Performance Optimization, Enterprise "
            "Deployment) assume is already in place \u2014 a well-architected Power Query layer is "
            "the foundation for both refresh performance and governed source management.",
        ],
        footer="Instructor prompt: walk the query pane in the final PBIP and ask students to "
               "narrate what each query does and why it is or isn't load-enabled. If they can "
               "narrate the pane, they've internalized the pattern.",
        script=[
            "Use this slide as the recap before the lab walkthrough. Everything they're about "
            "to build has already been introduced \u2014 this is the one-slide summary of the end "
            "state.",
            "Walk the four bullets in order, and for each one, ask the room to name which "
            "exercise built that piece. Staged solution = Exercise 1. Folder combine + lineage "
            "= Exercise 2. Parameters + functions = Exercises 3, 4, and 7. Validation and Gov = "
            "Exercise 5 plus the module-wide Gov table.",
            "Emphasize the reviewer-narration test in the footer: if a student can open the "
            "query pane and, without opening Advanced Editor, tell you what each query does and "
            "why it's load-enabled or not, they've internalized the architecture. That's the "
            "bar we're aiming for.",
            "Bridge to the lab walkthrough: 'Here's the checklist of what you'll actually do at "
            "the keyboard.'",
        ]
    )
    page += 1

    # 15. Module lab walkthrough
    checklist_slide(
        prs, "Module Lab Walkthrough", kicker="Topic 13 \u2014 What you'll build", page=page,
        items=[
            "Data sources: orders-2026-01/02/03.csv and product-category-map.csv, via Get data "
            "> Web using the raw GitHub URLs",
            "Exercise 1: Staged query architecture \u2014 raw_ / stg_ / FactOrders layering with "
            "load disabled on raw and staging",
            "Exercise 2: Folder combine \u2014 add SourceFile lineage, append monthly queries, "
            "confirm schema consistency, apply explicit types",
            "Exercise 3: Parameters \u2014 create RawDataBaseUrl, SourceFolderPath, "
            "EnvironmentName; document Dev/Test/Prod switching",
            "Exercise 4: Custom function fn_CleanText \u2014 nullable-text-safe, invoked via "
            "Table.TransformColumns on FactOrders and dim_ProductCategory text columns",
            "Exercise 5: Data quality \u2014 AddedDataQualityIssue in staging, err_OrdersReview as "
            "a Reference, FactOrders filtered to DataQualityIssue = \"\"",
            "Exercise 6: Query folding \u2014 conceptual for the Web/CSV source; discuss what "
            "would fold on SQL Server and how to verify with View Native Query",
            "Exercise 7: Incremental refresh prep \u2014 RangeStart/RangeEnd Date/Time parameters "
            "and a half-open FactOrders[OrderDate] filter",
        ],
        script=[
            "This is the bridge from lecture to keyboard. Read it as a literal table of "
            "contents for the next block of hands-on time.",
            "Point out the two data-source groups: three monthly order files (which drive "
            "Exercises 1, 2, and 5) plus one product-category reference file (which becomes "
            "dim_ProductCategory and gets fn_CleanText applied in Exercise 4).",
            "Set expectations on Exercise 6 upfront: it's a conceptual/discussion exercise "
            "because our Web/CSV source doesn't fold. Students should not spend keyboard time "
            "trying to make View Native Query appear; they should discuss what would fold on a "
            "SQL source and move on.",
            "Remind students of the load-enabled rule one more time before they start: after "
            "Exercise 1, only FactOrders and dim_ProductCategory should be load-enabled. If "
            "their final query pane has more than that, something is not quite right \u2014 fix it "
            "before moving on to the later exercises.",
        ]
    )
    page += 1

    # 16. Knowledge check
    checklist_slide(
        prs, "Knowledge Check & Discussion", kicker="Topic 14 \u2014 Wrap-up", page=page,
        items=[
            "Raw and staging queries have load disabled; only FactOrders and dim_ProductCategory "
            "load into the model.",
            "The final fact query (FactOrders) has explicit data types applied as the last step "
            "before load.",
            "The folder-combine equivalent filters to the expected monthly files only and "
            "preserves a SourceFile lineage column.",
            "fn_CleanText handles null input safely and is invoked via Table.TransformColumns "
            "on the intended text columns.",
            "Data quality issues are surfaced in err_OrdersReview with a readable "
            "DataQualityIssue reason column, not silently dropped.",
            "Query folding is discussed with source limitations named \u2014 Web/CSV does not "
            "fold, SQL-family sources do.",
            "All five module parameters exist and are named exactly: RawDataBaseUrl, "
            "SourceFolderPath, EnvironmentName, RangeStart, RangeEnd.",
            "RangeStart and RangeEnd are Date/Time and used in a half-open filter on "
            "FactOrders[OrderDate].",
            "Gov notes are documented next to Verify-for-Gov features (incremental refresh "
            "policy, dataflows, connectors, Dataflows Gen2).",
            "Discussion: when would you accept a native query, and how would you document that "
            "exception?",
        ],
        script=[
            "Run this as a discussion-driven wrap-up rather than a quiz. The goal is to have "
            "students verbalize the reasoning behind each item, not just tick boxes.",
            "Pick three or four items and call on specific students. Good candidates for a "
            "discussion answer: the fn_CleanText null-handling rationale, the err_OrdersReview "
            "vs. silent-drop distinction, and the RangeStart/RangeEnd half-open filter detail. "
            "Each of those is a common mistake that benefits from being said out loud.",
            "For the native-query discussion question, use it to reinforce the governance "
            "message: a native query is not wrong, but it needs to be documented and reviewed "
            "with the same care as any other source-side artifact.",
            "Close by connecting forward: the query architecture built today is the "
            "foundation Module 4 (Report Design UX) sees as 'the field list', and later modules "
            "(Performance Optimization, Enterprise Deployment) will assume this staged, "
            "parameterized, load-disciplined pattern is already in place.",
        ]
    )
    page += 1

    # 17. Closing
    closing_slide(
        prs, MODULE_NO,
        "Module 04: Report Design UX \u2014 building accessible, high-performance report canvases "
        "on top of the governed FactOrders / dim_ProductCategory model you just built.",
        page=page,
        script=[
            "Congratulate the class on completing Module 3. This is one of the highest-value "
            "modules in the workshop because the patterns \u2014 staging, parameters, functions, "
            "data quality \u2014 apply to essentially every real Power BI project.",
            "Remind students to keep their completed PBIP handy; the FactOrders / "
            "dim_ProductCategory model from today is what the report-design examples in Module "
            "4 will visualize.",
            "Take final questions before moving on, especially anything about the "
            "Verify-for-Gov items (incremental refresh policy in the Service, cloud dataflows, "
            "Dataflows Gen2, native queries) since those are the most common sources of "
            "lingering confusion.",
        ]
    )

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    prs.save(str(OUT_PATH))
    print(f"Saved: {OUT_PATH} ({len(prs.slides.__iter__.__self__._sldIdLst)} slides)")


if __name__ == "__main__":
    build()
