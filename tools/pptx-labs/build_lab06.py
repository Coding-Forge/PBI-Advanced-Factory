#!/usr/bin/env python3
"""
Builds the Lab 06 (Advanced Analytics and AI-Assisted Insights) instructor deck.
Run from repo root: python tools/pptx-labs/build_lab06.py
Output: modules/06-advanced-analytics-ai/assets/advanced-analytics-ai.pptx
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from slide_kit import (
    new_presentation, title_slide, agenda_slide,
    content_slide, table_slide, checklist_slide, closing_slide,
)

OUT_PATH = Path(__file__).resolve().parent.parent.parent / \
    "modules" / "06-advanced-analytics-ai" / "assets" / "advanced-analytics-ai.pptx"

MODULE_NO = 6
TITLE = "Advanced Analytics and AI-Assisted Insights"
SUBTITLE = ("Delivering what-if scenarios, driver analysis, forecasting, and AI visuals in "
            "Power BI \u2014 with a documented Gov-safe fallback for every AI-assisted feature.")

AGENDA_TOPICS = [
    "Advanced analytics vs. AI-assisted features",
    "What-if parameters",
    "Decomposition tree",
    "Forecasting",
    "Anomaly detection",
    "Key influencers",
    "Python and R visuals",
    "Azure Machine Learning integration",
    "Copilot in Power BI / Fabric",
    "Gov-safe alternate paths",
    "Delivery decision framework",
    "Lab review and knowledge check",
]


def build():
    prs = new_presentation()
    page = 1

    # 1. Title
    title_slide(
        prs, MODULE_NO, TITLE, SUBTITLE,
        script=[
            "Welcome learners to Module 6. Frame this as the module where Power BI stops being "
            "purely a modeling and reporting tool and starts overlapping with analytics and AI "
            "features \u2014 what-if scenarios, decomposition tree, forecasting, anomaly detection, "
            "key influencers, Python/R visuals, Azure Machine Learning, and Copilot.",
            "Set the tension up front: almost every advanced feature in this module has a "
            "governance caveat. Only what-if parameters are Gov-ready today. Decomposition tree, "
            "forecasting, anomaly detection, key influencers, Python/R, Azure ML, and Copilot are "
            "each either 'Verify for Gov' or 'Commercial-focused' \u2014 they may or may not work in "
            "the target tenant, and the answer is not obvious from Desktop alone.",
            "Preview the lab shape: Exercise 1 (what-if parameters) is the one universally hands-on "
            "exercise. Exercises 2-4 are 'where available' visuals \u2014 do them if the tenant "
            "supports it, otherwise follow the documented Gov-safe alternate path. Exercises 5-7 "
            "(Python/R, Azure ML, Copilot) are largely conceptual for a mixed classroom.",
            "Tell students the goal of today is dual: they should be able to *build* a what-if "
            "scenario and *decide* whether any given AI-assisted feature is appropriate for a "
            "given delivery \u2014 tenant, cloud, licensing, and residency all factor in, and the "
            "decision framework at the end of the deck is what they'll actually take back to work.",
        ]
    )
    page += 1

    # 2. Agenda
    agenda_slide(
        prs, MODULE_NO, AGENDA_TOPICS, page=page,
        script=[
            "Walk through the twelve topics briefly. Group them for the room: topic 1 sets the "
            "landscape; topic 2 (what-if) is the Gov-ready hands-on core; topics 3-6 are the "
            "built-in AI visuals (decomposition tree, forecasting, anomaly detection, key "
            "influencers); topics 7-9 are the external/AI-assisted integrations (Python/R, Azure "
            "ML, Copilot); topics 10-12 are the governance layer \u2014 fallbacks, decision "
            "framework, and lab review.",
            "Emphasize the split: only topic 2 is guaranteed hands-on. Every AI visual (3-6) is "
            "'Verify for Gov'. The Copilot topic is 'Commercial-focused / Verify for Gov' \u2014 for "
            "many students in a Gov delivery, that entire topic is conceptual.",
            "Tell learners the decision framework in topic 11 is the single most portable takeaway "
            "of the day \u2014 the same four questions apply to every future AI or advanced-analytics "
            "feature Microsoft ships, not just the ones we cover today.",
        ]
    )
    page += 1

    # 3. Topic 1 - Advanced analytics vs. AI-assisted features
    table_slide(
        prs, 1, "Advanced Analytics vs. AI-Assisted Features", page=page,
        headers=["Category", "Examples in Power BI", "Gov status"],
        col_widths=[3.0, 5.6, 3.3],
        rows=[
            ["Analytical patterns",
             "What-if parameters, rolling averages, YoY / prior-period measures, Top N.",
             "Gov-ready \u2014 pure DAX/modeling."],
            ["Built-in AI visuals",
             "Decomposition tree, Key influencers, Q&A visual, Smart Narrative, "
             "anomaly detection, forecasting.",
             "Verify for Gov \u2014 varies by sovereign cloud."],
            ["External ML integration",
             "Python and R visuals in Desktop/Service; Azure Machine Learning scored datasets.",
             "Verify for Gov \u2014 runtime, network, residency."],
            ["Copilot experiences",
             "Copilot in Power BI/Fabric for authoring assist, summarization, data exploration.",
             "Commercial-focused / Verify for Gov."],
            ["Governance and availability",
             "Tenant settings, capacity SKU, data residency, human-review requirements.",
             "Applies to every row above."],
        ],
        note="Lab connection: Exercise 1 lives in the top row (Gov-ready). Every other exercise in "
             "the lab maps to a row below it \u2014 each with its own availability check and Gov-safe "
             "alternate path documented in the README.",
        script=[
            "Open by drawing the distinction on the board: 'advanced analytics' in Power BI covers "
            "everything from a simple rolling-average measure up through Copilot. Not all of it is "
            "AI, and not all of it is available everywhere \u2014 lumping it together is exactly how "
            "delivery teams get surprised in a Gov engagement.",
            "Walk the rows in order. Analytical patterns \u2014 what-if, Top N, YoY \u2014 are pure DAX and "
            "modeling; they run on any tenant, any cloud, no special capacity. Built-in AI visuals "
            "like Decomposition tree and Key influencers are Microsoft-hosted intelligence baked "
            "into Desktop and Service, and their availability varies by sovereign cloud.",
            "External ML integration means either Python/R visuals executing code inside Desktop "
            "(and requiring Service parity), or Azure ML producing a scored dataset that Power BI "
            "consumes. Both introduce runtime, network path, and data residency questions that a "
            "governance team must sign off on.",
            "Copilot is called out separately because its status is currently 'Commercial-focused / "
            "Verify for Gov' \u2014 for many Gov customers today it isn't available at all, so treat "
            "it as a conceptual discussion unless somebody in the room can confirm otherwise.",
            "Close by pointing at the last row: governance and availability apply on top of every "
            "row above. Tenant settings, capacity, residency, and human-review policies decide "
            "whether any of this is deliverable, regardless of what Desktop can technically do.",
        ]
    )
    page += 1

    # 4. Topic 2 - What-if parameters
    content_slide(
        prs, 2, "What-If Parameters", page=page,
        lead_items=[
            "Author with Modeling > New parameter > Numeric range \u2014 in the lab, name it "
            "'Margin Adjustment %' with a range like -10% to 20% and a small increment.",
            "Power BI generates two artifacts: a hidden parameter table with the value range, and "
            "a SELECTEDVALUE-based measure that returns the current slicer selection.",
            "Consume the generated measure inside a DAX measure \u2014 for example an adjusted gross "
            "margin that multiplies the base margin by (1 + 'Margin Adjustment %' Value).",
            "The generated slicer drives every visual bound to the adjusted measure so users can "
            "explore scenarios interactively without editing DAX.",
        ],
        why_items=[
            "What-if is the one advanced analytics feature in this module that is fully Gov-ready "
            "\u2014 no AI service, no external runtime, no tenant caveat.",
            "It turns a static report into a scenario tool: pricing sensitivity, cost-inflation "
            "modeling, target-attainment adjustments \u2014 all without leaving the model.",
            "It reinforces DAX skills from Module 2 \u2014 SELECTEDVALUE, variable measures, and "
            "measure composition \u2014 in a business-facing way.",
        ],
        footer="Lab tie-in: Exercise 1 walks through creating 'Margin Adjustment %', wiring it into "
               "an adjusted gross margin measure, and validating that visuals respond as the "
               "slicer changes.",
        script=[
            "Start with the business framing before the mechanics: what-if parameters let a report "
            "user ask 'what would our margin look like if we raised prices 5%?' or 'what if input "
            "costs went up 8%?' without a modeler having to intervene. That's the value.",
            "Walk the mechanics slowly \u2014 this is the one exercise every student will do, so make "
            "sure they see the flow: Modeling ribbon, New parameter, Numeric range, pick a name "
            "('Margin Adjustment %'), a min, a max, and an increment. Power BI creates the "
            "parameter table plus a companion measure that returns the currently selected value "
            "using SELECTEDVALUE.",
            "Show how the generated measure gets consumed: an adjusted-margin measure just "
            "multiplies the base margin by (1 + [Margin Adjustment % Value]). Point out that "
            "there's nothing magical here \u2014 it's a normal DAX measure that happens to reference a "
            "slicer-driven value. That's why what-if is Gov-ready: no service call, no AI.",
            "Use an analogy that lands with business audiences: it's a live pricing knob. The "
            "board doesn't need to see six versions of the same report at different assumed "
            "margins \u2014 they need one report with a slider on it.",
            "Transition to the next topic by pointing out that everything after this slide leaves "
            "the safety of pure DAX and enters Verify-for-Gov territory \u2014 starting with the "
            "Decomposition tree AI visual.",
        ]
    )
    page += 1

    # 5. Topic 3 - Decomposition tree
    content_slide(
        prs, 3, "Decomposition Tree", page=page,
        lead_items=[
            "AI visual that decomposes a numeric measure (e.g., Sales Amount, Gross Margin) across "
            "a set of explanatory categorical fields chosen at author time.",
            "Two exploration modes: manual drill (author picks the next field) and AI split "
            "(High/Low value) \u2014 the AI split ranks which field's next level explains the most "
            "change in the analyzed measure.",
            "In the lab, students analyze Sales Amount or Gross Margin with Territory, Product "
            "Category, Customer Type, and Segment as 'Explain by' fields.",
            "Availability status: Verify for Gov \u2014 tenant settings and sovereign cloud can "
            "disable the AI splits or the visual entirely.",
        ],
        why_items=[
            "Turns a static hierarchy exploration into a guided one \u2014 the visual points users to "
            "the branch of the tree that actually matters, instead of manual click-and-hope drill.",
            "Highest-value AI visual for guided root-cause analysis by non-technical business "
            "users, because the UI is a familiar drill-down.",
            "Perfect example of a feature where the Gov-safe fallback (a matrix hierarchy with "
            "drillthrough) is functional but noticeably less guided \u2014 helps students internalize "
            "what 'AI-assisted' actually adds.",
        ],
        footer="Lab tie-in: Exercise 2 is 'where available' \u2014 confirm the visual works in the "
               "target tenant first, otherwise use the documented Gov-safe fallback (matrix "
               "hierarchy + drillthrough page).",
        script=[
            "Introduce Decomposition tree as the most approachable of the AI visuals \u2014 it looks "
            "and feels like drill-down, which every business user already understands.",
            "Explain both modes concretely. In manual mode, the user picks the next field to break "
            "the value by (e.g., break Sales Amount by Territory, then by Product Category). In "
            "High value / Low value AI mode, Power BI ranks all the 'Explain by' fields and "
            "recommends the one whose next level contributes most to the high or low outcome.",
            "Walk through the lab's specific setup: analyze Sales Amount or Gross Margin, with "
            "Territory, Product Category, Customer Type, and Segment as explanatory fields. Show "
            "how a High value split might land on Territory first, then Product Category \u2014 that's "
            "the AI telling the user 'this branch is where the money is.'",
            "Be explicit about availability: Decomposition tree is Verify for Gov. In some "
            "sovereign clouds the visual renders but AI splits are disabled; in others the visual "
            "itself may be turned off by tenant policy. The lab's Gov-safe fallback \u2014 a matrix "
            "hierarchy with a drillthrough page \u2014 lets students still do the analysis, just "
            "without the guided splits.",
            "Transition: 'That was AI *guiding* exploration. Next topic is AI *predicting* the "
            "future \u2014 forecasting.'",
        ]
    )
    page += 1

    # 6. Topic 4 - Forecasting
    content_slide(
        prs, 4, "Forecasting", page=page,
        lead_items=[
            "Forecasting lives in the Analytics pane of a line chart \u2014 add a date field on the X "
            "axis, Sales Amount as the value, then enable Forecast.",
            "The engine uses exponential smoothing under the hood and returns a point forecast "
            "plus a shaded confidence interval; the default 95% band represents statistical "
            "uncertainty, not business risk.",
            "Requires a continuous date/time X axis, a reasonable amount of history (roughly at "
            "least two seasonal cycles), and no large gaps \u2014 sparse or irregular data produces "
            "misleading intervals.",
            "Availability status: Verify for Gov \u2014 validate visual support, tenant policy, and "
            "data residency before requiring it in a delivery.",
        ],
        why_items=[
            "Adds forward-looking context to a trend line without students needing to build ARIMA "
            "or Prophet models externally \u2014 fast, in-place, no code.",
            "Teaching the confidence interval correctly is where the real value is: a wide band "
            "means 'the model doesn't know', which is a governance conversation, not just a chart.",
            "Reinforces the human-review rule that runs through this whole module \u2014 the "
            "forecast is a hypothesis, not a commitment.",
        ],
        footer="Lab tie-in: Exercise 3 (where available). Gov-safe fallback is a rolling-average "
               "measure and prior-period comparisons \u2014 no prediction, but comparable trend "
               "framing.",
        script=[
            "Frame forecasting as the AI feature most likely to be misused. Users see a projected "
            "line, mentally treat it as a commitment, and forget that a wide confidence interval "
            "is the model saying 'I don't really know.'",
            "Walk the mechanics: line chart, date on the X axis, Sales Amount as value, Analytics "
            "pane on the right, expand Forecast, set the forecast length and the confidence band "
            "(default 95%). Point out the shaded region \u2014 that's the confidence interval, not the "
            "forecast itself.",
            "Discuss requirements openly: forecasting needs a continuous date axis, enough history "
            "to see at least two seasonal cycles (a year for monthly seasonality, several weeks "
            "for weekly), and clean data without large gaps. If any of those are missing, the "
            "output will look plausible and be wrong.",
            "Use a concrete analogy: 'The forecast is a weather report. A tight confidence band is "
            "clear skies; a wide one means the model is guessing. Don't ship a business plan built "
            "on guessing.' That's the teaching moment.",
            "Close with the Gov fallback: if forecasting isn't approved for the tenant, the lab's "
            "documented alternative is a rolling-average plus prior-period comparison measure \u2014 "
            "not the same feature, but the same *narrative* about trend and change.",
        ]
    )
    page += 1

    # 7. Topic 5 - Anomaly detection
    content_slide(
        prs, 5, "Anomaly Detection", page=page,
        lead_items=[
            "Enabled from the Analytics pane on a line chart with a continuous date/time axis and "
            "a single value \u2014 similar host visual to forecasting.",
            "Flags data points outside an expected pattern (SR-CNN based) and offers a natural-"
            "language 'Explain' pane with candidate contributing fields.",
            "Sensitivity is tunable; higher sensitivity surfaces more anomalies but also more "
            "false positives. The visual highlights, but does not diagnose \u2014 humans decide "
            "whether an anomaly is a real issue.",
            "Availability status: Verify for Gov \u2014 validate Service/Desktop parity and tenant "
            "support before relying on it in a report.",
        ],
        why_items=[
            "Cuts the manual 'stare at the chart looking for spikes' step out of exception "
            "monitoring \u2014 the visual raises its hand.",
            "The Explain pane models what a good AI-assisted feature does: it shows candidate "
            "contributors, but a human still ranks and confirms them.",
            "Data-quality trap: garbage-in, anomalies-out. If the underlying series has data "
            "quality issues (missing days, late-arriving fact rows), the anomalies flagged are "
            "often just data problems.",
        ],
        footer="Instructor note: no dedicated hands-on exercise for anomaly detection in the lab \u2014 "
               "cover conceptually and demo if the tenant supports it; otherwise fall back to a "
               "DAX-based exception measure (e.g., > 2 stdev from rolling mean).",
        script=[
            "Introduce anomaly detection as the mirror image of forecasting: forecasting says "
            "'here's what to expect'; anomaly detection says 'here's a point that didn't match "
            "expectation'.",
            "Explain the mechanics quickly \u2014 same Analytics pane on a line chart, enable Find "
            "anomalies, tune the sensitivity slider. Point out that clicking a flagged anomaly "
            "opens an Explain pane where Power BI proposes candidate explanatory fields.",
            "Stress the data-quality trap. In a real delivery, the first several 'anomalies' the "
            "visual finds are almost always late-arriving rows, missing days, or a partition that "
            "hasn't refreshed \u2014 not business anomalies. Teach students to sanity-check the source "
            "before believing the visual.",
            "Discuss sensitivity honestly: too low, and real anomalies slip through; too high, "
            "and every noisy point gets flagged and users start ignoring the visual entirely \u2014 "
            "the alert-fatigue failure mode.",
            "Gov fallback: a plain DAX exception measure \u2014 something like flagging points more "
            "than two standard deviations from a rolling mean \u2014 is deterministic, auditable, and "
            "runs anywhere. Not as clever, but perfectly acceptable in a Gov delivery.",
        ]
    )
    page += 1

    # 8. Topic 6 - Key influencers
    content_slide(
        prs, 6, "Key Influencers", page=page,
        lead_items=[
            "AI visual that ranks which explanatory fields most increase or decrease a chosen "
            "outcome \u2014 supports both categorical outcomes (e.g., Customer Type = 'Churned') and "
            "numeric outcomes (e.g., Sales Amount).",
            "Two tabs: Key influencers (per-field impact, 'when Territory is X, the outcome is Y% "
            "more likely to be Z') and Top segments (combinations of fields that co-occur with the "
            "outcome).",
            "Requires enough rows and enough variance per explanatory field to be statistically "
            "meaningful \u2014 small or imbalanced datasets produce unstable or trivial rankings.",
            "Availability status: Verify for Gov \u2014 it is an AI visual, so availability can vary "
            "by sovereign cloud and tenant policy.",
        ],
        why_items=[
            "Gives business users a first-pass driver analysis without a data scientist \u2014 "
            "'what's driving churn?' becomes a visual, not a Jupyter notebook.",
            "Explainability is the whole point: unlike a black-box model, Key influencers shows "
            "*which* field and *which* value moves the outcome, in plain language.",
            "Ideal teaching example for AI limitations: correlation, not causation. Territory may "
            "'drive' churn statistically while the actual cause is a product-quality issue "
            "concentrated in that territory.",
        ],
        footer="Lab tie-in: Exercise 4 (where available). Gov-safe fallback is ranked Top N "
               "visuals and slicer-driven comparisons \u2014 they don't rank drivers automatically, "
               "but they let a human do the same reasoning explicitly.",
        script=[
            "Introduce Key influencers by contrasting it with Decomposition tree. Both look at "
            "drivers, but Decomposition tree is a guided drill; Key influencers is a ranked "
            "statistical explanation of a specific outcome.",
            "Walk through both tabs. The Key influencers tab answers 'which field values push the "
            "outcome up or down and by how much?' The Top segments tab answers 'which "
            "*combinations* of field values co-occur with the outcome?' Top segments is often more "
            "actionable in a real business \u2014 a single field rarely tells the whole story.",
            "Be direct about data requirements: this is a statistical visual. Small samples, "
            "highly imbalanced classes, or fields with only one or two distinct values will "
            "produce rankings that are either unstable or obvious. Set expectations before "
            "students see 'weird' results in the lab.",
            "Use the correlation-vs-causation teaching moment explicitly. A visual that says "
            "'Territory West is 40% more likely to churn' is describing a statistical association "
            "\u2014 the underlying cause could be a product line concentrated in that territory, a "
            "specific customer segment, or a service issue. Key influencers cannot tell you which.",
            "Gov fallback: ranked Top N visuals plus slicer-driven side-by-side comparisons. It's "
            "manual driver analysis, but it's transparent and Gov-ready.",
        ]
    )
    page += 1

    # 9. Topic 7 - Python and R visuals
    content_slide(
        prs, 7, "Python and R Visuals", page=page,
        lead_items=[
            "Code-based visuals that render output from a Python or R script inside Desktop, and "
            "\u2014 with matching runtime configured \u2014 in the Service.",
            "Runtime prerequisites: an approved Python or R installation on Desktop, plus a "
            "documented, approved package list (matplotlib, seaborn, ggplot2, etc.). No ad-hoc "
            "package installs in a governed environment.",
            "Service limitations apply: only specific packages are supported in the Service, "
            "output size is capped, and interactivity is limited compared to native visuals.",
            "Availability status: Verify for Gov \u2014 depends on Desktop configuration, approved "
            "packages, Service support, and customer policy on executing code inside a report.",
        ],
        why_items=[
            "Unlocks visualization types Power BI doesn't natively support (custom statistical "
            "plots, network diagrams, specialized scientific charts) \u2014 valuable in the right "
            "context.",
            "Governance concerns are real: an R or Python visual is code the report author wrote, "
            "running on the render host \u2014 that has to be reviewed like any other code artifact.",
            "For most business dashboards the answer is 'don't' \u2014 native visuals plus custom "
            "visuals from AppSource cover the vast majority of needs with less operational risk.",
        ],
        footer="Lab tie-in: Exercise 5 is optional and conceptual for a mixed classroom \u2014 confirm "
               "runtime and approved packages before demoing, and prefer native visuals where "
               "they suffice.",
        script=[
            "Introduce Python/R visuals as the escape hatch: when Power BI's built-in and custom "
            "visuals genuinely can't render what you need, code-based visuals can. That's the "
            "narrow real use case.",
            "Explain the runtime picture. Desktop needs a working Python or R install; the visual "
            "then executes the script and embeds the rendered image (matplotlib, ggplot2). The "
            "Service supports a specific, limited runtime and package list \u2014 anything outside "
            "that list works in Desktop but breaks after publish.",
            "Governance is where this topic gets serious. A Python visual is arbitrary code the "
            "author wrote, running on the report render pipeline. In a governed environment that "
            "code needs the same review path as any other production code \u2014 approved packages, "
            "no arbitrary pip installs, source-controlled scripts.",
            "Talk security concretely: a poorly-written script could exfiltrate data from the "
            "model to an external endpoint, or embed user-controlled input in a way that breaks "
            "assumptions. This is why customer policy often forbids code visuals entirely.",
            "Close with a pragmatic recommendation: for 95% of business reports the answer is "
            "'use a native or trusted custom visual.' Python/R visuals are for the specific 5% "
            "where nothing else fits and governance signs off.",
        ]
    )
    page += 1

    # 10. Topic 8 - Azure Machine Learning integration
    table_slide(
        prs, 8, "Azure Machine Learning Integration", page=page,
        headers=["Dimension", "What to validate", "Why it matters"],
        col_widths=[2.6, 5.4, 4.9],
        rows=[
            ["Architecture",
             "Model trained and hosted in Azure ML; Power BI consumes either a scored dataset or "
             "an online endpoint.",
             "Two very different integration patterns \u2014 pick one and document it."],
            ["Identity",
             "Service principal or managed identity with access to the Azure ML workspace and "
             "endpoint.",
             "Gateway/tenant identity decides who can call the model."],
            ["Network",
             "Private endpoints, VNet integration, and any required outbound rules from the "
             "gateway host.",
             "A model unreachable from the gateway is a model that fails silently at refresh."],
            ["Region and cloud",
             "Azure ML workspace region must match the customer's data residency policy; sovereign "
             "cloud alignment (Commercial vs. Government) is not optional.",
             "Cross-cloud calls are almost always disallowed in Gov engagements."],
            ["Model governance",
             "Model versioning, drift monitoring, retraining cadence, and human-review policy for "
             "scored outputs before they reach a report.",
             "The model is now part of the report's data supply chain \u2014 govern it accordingly."],
        ],
        note="Lab tie-in: Exercise 6 is conceptual \u2014 review architecture, identity, network, and "
             "residency; do NOT stand up a live Azure ML endpoint from the classroom. Gov-safe "
             "alternate: import a static, pre-scored sample table and document how it would be "
             "produced.",
        script=[
            "Frame Azure ML integration as the point where a Power BI report stops being purely a "
            "reporting artifact and becomes the consumer of a machine-learning supply chain. That "
            "reframing is the whole teaching goal here.",
            "Walk the table row by row. Architecture: two patterns \u2014 a batch-scored dataset "
            "loaded into the model, or a live online endpoint queried at refresh or query time. "
            "Pick one, document it, don't mix them without a reason.",
            "Identity and network are where most real integrations fail. A model that scores fine "
            "in Azure ML Studio may be unreachable from the on-premises data gateway if private "
            "endpoints, VNet rules, or firewall paths aren't in place. Include the gateway host in "
            "the connectivity picture from day one.",
            "Region and cloud alignment is the Gov-critical row. An Azure ML workspace in "
            "Commercial cloud consumed by a Power BI Gov tenant is almost always a residency "
            "violation; treat cross-cloud model calls as forbidden until specifically approved.",
            "Close on model governance: once a model's predictions ship in a report, model "
            "versioning, drift, retraining, and human review of scored output are all part of the "
            "report's operational surface. This is why the lab exercise is deliberately conceptual "
            "\u2014 the right first step for a classroom is a static scored sample, not a live "
            "endpoint.",
        ]
    )
    page += 1

    # 11. Topic 9 - Copilot in Power BI / Fabric
    content_slide(
        prs, 9, "Copilot in Power BI / Fabric", page=page,
        lead_items=[
            "Copilot in Power BI supports authoring assistance (generate DAX, create measures, "
            "suggest visuals), summarization of report pages, and natural-language data "
            "exploration.",
            "Requires a Fabric or Power BI Premium capacity SKU with Copilot enabled at the tenant "
            "level, plus explicit workspace assignment \u2014 not a per-user setting.",
            "Prompts, model inputs, and outputs travel to Microsoft-hosted foundation models; "
            "customer data boundary and residency commitments differ from ordinary tenant data.",
            "Availability status: Commercial-focused / Verify for Gov \u2014 for most Government "
            "tenants Copilot is either unavailable or preview only. Treat as conceptual unless "
            "the target tenant is confirmed.",
        ],
        why_items=[
            "Accelerates authoring \u2014 measure drafting, page summarization \u2014 for report authors "
            "already fluent in Power BI. It is not a replacement for understanding the model.",
            "Every Copilot output is a hypothesis: a generated DAX measure can compile and still "
            "be semantically wrong. Human review is a requirement, not a recommendation.",
            "The governance conversation \u2014 tenant, capacity, data boundary, residency, "
            "logging \u2014 is what most students actually need to take back to work, more than the "
            "feature itself.",
        ],
        footer="Lab tie-in: Exercise 7 is a conceptual section \u2014 map potential Copilot workflows "
               "to non-AI fallbacks, and identify tenant, capacity, licensing, and boundary "
               "requirements.",
        script=[
            "Set expectations up front: for many Gov students in the room Copilot is not "
            "available today. That doesn't mean the topic doesn't matter \u2014 the governance "
            "framing here applies to every AI feature Microsoft will ship next.",
            "Walk the three main capability areas: authoring assistance (draft a DAX measure, "
            "suggest visuals for a page), summarization (turn a report page into a written "
            "narrative), and data exploration (ask the model a question in natural language and "
            "get a visual back).",
            "Be explicit about capacity and tenant requirements: Copilot needs a supported Fabric "
            "or Premium SKU, tenant-level enablement by an admin, and explicit workspace "
            "assignment. It is not something an individual author can turn on.",
            "The data boundary conversation is the most important one. Prompts, model inputs, and "
            "generated outputs are processed by Microsoft-hosted foundation models. Whether that "
            "meets a customer's residency and confidentiality commitments is a decision the "
            "customer's governance team makes, not the report author.",
            "Close with the reviewer's rule: every Copilot output is a hypothesis. A generated "
            "measure can be syntactically fine and semantically wrong \u2014 wrong grain, wrong "
            "filter context, right shape. Human review of AI output is a requirement, not a nice-"
            "to-have.",
        ]
    )
    page += 1

    # 12. Topic 10 - Gov-safe alternate paths
    table_slide(
        prs, 10, "Gov-Safe Alternate Paths", page=page,
        headers=["AI-assisted feature", "Gov-safe alternate", "Trade-off"],
        col_widths=[3.0, 5.0, 4.9],
        rows=[
            ["Decomposition tree",
             "Matrix visual with a defined hierarchy + drillthrough page.",
             "Manual drill, no AI-ranked next split."],
            ["Forecasting",
             "Rolling-average measure plus prior-period comparison (MoM, YoY).",
             "Describes trend, does not project forward."],
            ["Anomaly detection",
             "DAX exception measure \u2014 e.g., > 2 stdev from rolling mean.",
             "Deterministic and auditable, but no natural-language explain."],
            ["Key influencers",
             "Ranked Top N visuals + slicer-driven segment comparisons.",
             "Human ranks drivers explicitly; no ranked statistical output."],
            ["Python / R visuals",
             "Native visuals + trusted certified custom visuals from AppSource.",
             "May not cover niche visualization types."],
            ["Azure ML integration",
             "Import a static, pre-scored sample table.",
             "No live scoring; scored offline outside the report boundary."],
            ["Copilot",
             "Documented DAX patterns, templates, and reusable measures.",
             "Slower to author, fully human-authored and reviewable."],
        ],
        note="Rule of thumb: every AI-assisted feature above needs a documented, working, "
             "Gov-safe fallback before the report ships \u2014 even if the AI path is expected to be "
             "available. Feature toggles fail; fallbacks don't.",
        script=[
            "Frame this as the most operationally important slide in the deck. Every AI feature "
            "we've covered has a fallback, and every governed delivery needs the fallback "
            "documented \u2014 not because AI will definitely fail, but because feature availability "
            "can change under you.",
            "Walk the table left to right. Notice the pattern: each fallback trades an AI-provided "
            "insight (ranked splits, projected trend, flagged anomaly, ranked drivers, natural-"
            "language explain) for something the report author explicitly builds and can defend "
            "in a review.",
            "Emphasize that the fallbacks aren't degraded versions of the same thing \u2014 they're "
            "different tools that answer a related question. Rolling-average plus prior-period is "
            "not a forecast; it's a description of trend and change. A DAX exception measure "
            "isn't anomaly detection; it's a rule-based flag. Naming them accurately is part of "
            "governance.",
            "Point out the Copilot row: the fallback for Copilot's authoring assist is well-"
            "documented DAX patterns and reusable measures \u2014 which is basically what a healthy "
            "team already does. The AI accelerates it; it doesn't replace it.",
            "Set the rule of thumb from the note: the fallback must be documented and working "
            "before ship, even when the AI path is expected to be available. Toggles get flipped; "
            "fallbacks don't.",
        ]
    )
    page += 1

    # 13. Topic 11 - Delivery decision framework
    content_slide(
        prs, 11, "Delivery Decision Framework", page=page,
        lead_items=[
            "1. Is the feature technically available in the target tenant, cloud, and capacity? "
            "(Desktop working \u2260 Service working \u2260 Gov Service working.)",
            "2. Is it approved for use \u2014 tenant admin, workspace, and customer policy? Availability "
            "is necessary but not sufficient.",
            "3. Is the data residency acceptable? Where prompts, scored data, or model calls "
            "actually travel matters as much as where the report lives.",
            "4. Is there a documented non-AI fallback that would ship if the AI path is "
            "unavailable, unreliable, or disallowed?",
        ],
        why_items=[
            "The same four questions apply to every AI or advanced analytics feature Microsoft "
            "will ship \u2014 not just today's list. This is the portable skill.",
            "Any 'no' answer above should stop the delivery at that step until it's resolved \u2014 "
            "shipping first and asking later is the usual failure mode.",
            "The fourth question is what makes the difference between a robust delivery and a "
            "fragile one \u2014 an AI feature is fine as an accelerator, dangerous as a dependency.",
        ],
        footer="Instructor prompt: pick any feature from the module (forecasting, Copilot, Azure "
               "ML) and walk the four questions out loud with the class \u2014 makes the framework "
               "concrete before students carry it back to work.",
        script=[
            "Tell the room this is the single most portable takeaway of the module. If they "
            "forget every visual name we discussed, they should still remember these four "
            "questions \u2014 they apply to every AI feature Microsoft has shipped, is shipping, and "
            "will ship next.",
            "Walk each question with a concrete example. Availability: forecasting works in "
            "Desktop but the customer's Gov Service tenant has the AI visual policy disabled \u2014 "
            "answer is no. Approval: Copilot is available in the tenant but the customer's "
            "governance policy hasn't cleared it for production reports yet \u2014 answer is no. "
            "Residency: an Azure ML endpoint is in Commercial cloud but the report is in a Gov "
            "tenant \u2014 answer is no.",
            "The fallback question is the one people skip. Make students say the fallback out "
            "loud: 'If Copilot isn't available, we'll ship documented DAX templates.' 'If "
            "forecasting isn't approved, we'll ship rolling averages and YoY comparisons.' A "
            "delivery without a stated fallback is a delivery with a hidden dependency.",
            "Do the exercise from the footer live: pick forecasting or Copilot and walk the four "
            "questions with the class contributing answers. The muscle memory of using the "
            "framework is more valuable than memorizing it.",
            "Transition into the lab review with a clear statement: 'This framework is what you "
            "should use in the lab as you decide which optional exercises to actually do hands-on "
            "vs. treat conceptually.'",
        ]
    )
    page += 1

    # 14. Topic 12 - Lab review (module walkthrough)
    checklist_slide(
        prs, "Module Lab Walkthrough", kicker="Topic 12 \u2014 What you'll build", page=page,
        items=[
            "Exercise 1: What-if parameter 'Margin Adjustment %' + adjusted margin DAX measure "
            "(Gov-ready, required)",
            "Exercise 2: Decomposition tree on Sales Amount / Gross Margin (where available)",
            "Exercise 3: Forecast on a Sales Amount line chart with confidence intervals (where "
            "available)",
            "Exercise 4: Key influencers on a target outcome + Top segments review (where "
            "available)",
            "Exercise 5: Python or R visual with approved runtime and packages (optional, "
            "conceptual)",
            "Exercise 6: Azure ML integration \u2014 architecture, identity, network, residency "
            "review (conceptual)",
            "Exercise 7: Copilot workflows mapped to non-AI fallbacks (conceptual)",
            "For every optional exercise: label the feature status and document the Gov-safe "
            "alternate path",
        ],
        script=[
            "This slide is the bridge from lecture into the lab. Walk it as the literal "
            "checklist students will follow at the keyboard.",
            "Anchor them to Exercise 1 first: it's the one exercise that runs everywhere, is fully "
            "Gov-ready, and delivers a real business capability (scenario sliders). If a student "
            "runs out of time, this is the exercise they cannot skip.",
            "For Exercises 2-4, tell students the pattern is identical: confirm the AI visual "
            "works in the tenant, if yes build it as described, if no use the Gov-safe alternate "
            "documented in the README \u2014 and label the artifact either way. The label is not "
            "optional.",
            "For Exercises 5-7, set expectations that in most classrooms these will be "
            "conceptual: read the section, discuss governance implications, and document the non-"
            "AI fallback. Nobody should be installing Python packages or standing up an Azure ML "
            "endpoint in the classroom environment.",
            "Close with the labeling requirement one more time: every optional exercise's output "
            "should carry a visible status (Gov-ready, Verify for Gov, Commercial-focused) and a "
            "documented fallback \u2014 that's how governance sees this work land.",
        ]
    )
    page += 1

    # 15. Knowledge check
    checklist_slide(
        prs, "Knowledge Check & Discussion", kicker="Wrap-up", page=page,
        items=[
            "What-if parameter works and scenario measures respond to the slicer.",
            "Optional AI/advanced visuals are labeled with an availability status.",
            "Gov-safe alternate path is documented for each optional feature used.",
            "Python/R prerequisites are documented if the exercise was attempted.",
            "Azure ML architecture dependencies (identity, network, residency) are documented.",
            "Copilot content is treated as conceptual unless tenant availability was confirmed.",
            "Every AI-generated or ML-driven output includes human-review guidance.",
            "Walk the four-question delivery decision framework against one feature out loud.",
        ],
        script=[
            "Use this as a discussion, not a quiz. The goal is to surface *reasoning* \u2014 whether "
            "students can defend the choices they made in the lab, not whether they can recite a "
            "definition.",
            "Pick two or three items to press on. The 'label the availability status' item is a "
            "good one \u2014 ask a student to name any optional exercise they did and state the "
            "label they attached to it and why.",
            "For the delivery decision framework item, actually do it: pick a feature (Copilot is "
            "usually the most productive), and walk the four questions with the class "
            "contributing answers. If they can do this smoothly, they've internalized the "
            "framework.",
            "For the human-review guidance item, ask what that looks like in practice \u2014 the "
            "answer should include some combination of: a documented reviewer, a review cadence, "
            "a way to challenge a specific AI output, and a rollback plan if a scored dataset "
            "turns out to be wrong.",
            "Close by connecting forward: the governance instincts practiced here \u2014 label the "
            "feature, document the fallback, verify residency \u2014 are exactly the instincts Module "
            "7 (Security Design) will build on next.",
        ]
    )
    page += 1

    # 16. Closing
    closing_slide(
        prs, MODULE_NO,
        "Module 07: Security Design \u2014 row-level security, object-level security, and "
        "workspace/tenant security patterns that govern who sees what in the models we've built.",
        page=page,
        subtitle=("Learners can now build Gov-ready scenario analytics and make defensible "
                  "delivery decisions about every AI-assisted feature Power BI ships \u2014 with a "
                  "documented, working fallback for each one."),
        script=[
            "Congratulate the class on completing what is genuinely the most nuanced module of "
            "the workshop \u2014 not because the features are hard, but because deciding when to use "
            "them is.",
            "Recap the two deliverables of the day: a working what-if scenario built by every "
            "student, and a defended set of decisions (labeled features, documented fallbacks) "
            "for every optional AI-assisted exercise.",
            "Take final questions especially on the Verify-for-Gov topics \u2014 forecasting, Key "
            "influencers, Azure ML, Copilot \u2014 since those are where lingering confusion is most "
            "likely and where students will get real customer questions after the workshop.",
            "Transition into Module 7: with the analytics and AI story settled, the next question "
            "is 'who is allowed to see what?' That's row-level security, object-level security, "
            "and the workspace/tenant boundary conversation \u2014 all built on the same models we've "
            "been extending all week.",
        ]
    )

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    prs.save(str(OUT_PATH))
    print(f"Saved: {OUT_PATH} ({len(prs.slides.__iter__.__self__._sldIdLst)} slides)")


if __name__ == "__main__":
    build()
