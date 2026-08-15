// Jeopardy data - Cumulative Final Review (all 11 modules)
// One category per module, 6 clues each ($100-$600), sourced from each module's knowledge-check.md
window.JEOPARDY_DATA = {
  boardId: "final-review",
  title: "Final Review: Power BI Advanced Factory (All 11 Modules)",
  categories: [
    {
      name: "1. Semantic Modeling",
      clues: [
        { value: 100, question: "This modeling approach reduces duplication, improves readability, simplifies DAX, and usually improves performance versus a single flat table.", answer: "Star schema." },
        { value: 200, question: "This term describes the level of detail represented by each row in a fact table, and must be clear so measures aggregate correctly.", answer: "Grain." },
        { value: 300, question: "This storage mode lets a shared dimension act as Import for performance while still participating in DirectQuery queries in a composite model.", answer: "Dual storage mode." },
        { value: 400, question: "This type of table supports analysis where one entity, such as a customer, can belong to multiple categories at once, like several segments.", answer: "A bridge table." },
        { value: 500, question: "Relationships of this cardinality can duplicate filter paths or apply filters at the wrong grain, which can inflate or suppress totals.", answer: "Many-to-many relationships." },
        { value: 600, question: "This lab uses a small lookup table between `DimProduct` and `FactTargets` for this reason.", answer: "`DimProduct` is at product grain while `FactTargets` is at product-category grain, so `DimProductCategory` avoids a many-to-many relationship on `ProductCategory`." },
      ],
    },
    {
      name: "2. Advanced DAX",
      clues: [
        { value: 100, question: "This is the set of filters applied to a DAX expression by visuals, slicers, relationships, and explicit DAX filters.", answer: "Filter context." },
        { value: 200, question: "CALCULATE performs this operation that converts row context into filter context.", answer: "Context transition." },
        { value: 300, question: "This DAX function variant intersects a new filter with existing filters instead of replacing them, unlike a plain filter argument in CALCULATE.", answer: "KEEPFILTERS." },
        { value: 400, question: "This type of measure can be aggregated across some dimensions but not across time in a simple additive way, such as inventory or balance.", answer: "A semi-additive measure." },
        { value: 500, question: "In a measure-switching pattern, a table with no relationship to any other table is used for this purpose.", answer: "A disconnected table — it captures a user selection that drives DAX logic without filtering the model." },
        { value: 600, question: "This DAX feature centralizes repeated calculation logic, such as current period, prior period, and year-over-year, and is marked Verify for Gov.", answer: "Calculation groups." },
      ],
    },
    {
      name: "3. Power Query",
      clues: [
        { value: 100, question: "This query-design pattern separates raw source extraction from transformation logic so complex Power Query solutions are easier to maintain.", answer: "Staging queries." },
        { value: 200, question: "This term describes a data source engine executing Power Query transformation steps natively instead of Power BI processing them locally.", answer: "Query folding." },
        { value: 300, question: "This Power Query feature solves the problem of hardcoded values (like file paths or date ranges) scattered across multiple queries.", answer: "Parameters." },
        { value: 400, question: "This Power Query object encapsulates reusable transformation logic and can be invoked across rows, files, or queries.", answer: "A custom function." },
        { value: 500, question: "These two DateTime parameters are used to filter data for an incremental refresh policy.", answer: "RangeStart and RangeEnd." },
        { value: 600, question: "This Power Query Service feature's availability can vary by cloud, tenant, license, and admin settings, which is why it is marked Verify for Gov.", answer: "Dataflows." },
      ],
    },
    {
      name: "4. Report Design & UX",
      clues: [
        { value: 100, question: "Report pages should be designed around these two things so learners/users can find what they need quickly.", answer: "Audience and task." },
        { value: 200, question: "This report feature type lets a user click a visual to jump to a detail page filtered to that context.", answer: "Drillthrough." },
        { value: 300, question: "This is why every guided report experience (bookmarks, drillthrough, navigation buttons) should include one of these.", answer: "A reset path — so users can return to a known starting state." },
        { value: 400, question: "A report page tooltip should have these qualities to be effective.", answer: "Focused, compact, contextual, and not a duplicate of the main page." },
        { value: 500, question: "Name three of the accessibility checks every report should include.", answer: "Alt text, tab order, contrast, descriptive titles, keyboard navigation, or avoiding color-only meaning (any three)." },
        { value: 600, question: "This report feature lets users switch between approved measures or dimensions in a visual without duplicating report pages.", answer: "Field parameters." },
      ],
    },
    {
      name: "5. Performance Optimization",
      clues: [
        { value: 100, question: "Performance optimization should always start with this activity before making any changes.", answer: "Measurement (establishing a baseline)." },
        { value: 200, question: "This built-in Power BI Desktop tool helps identify which visuals, DAX queries, or Power Query steps are consuming the most time.", answer: "Performance Analyzer." },
        { value: 300, question: "This type of column (with many unique values, like a transaction ID or exact timestamp) can significantly increase model size and hurt compression.", answer: "A high-cardinality column." },
        { value: 400, question: "This type of table answers summary-level queries from smaller Import tables while still preserving detailed DirectQuery access when needed.", answer: "An aggregation table." },
        { value: 500, question: "This refresh feature reduces refresh effort by processing only the relevant recent partitions instead of the entire fact table.", answer: "Incremental refresh." },
        { value: 600, question: "After a performance optimization change, these five things should be documented.", answer: "The baseline, the change made, the result, the tradeoff, and any remaining validation needed." },
      ],
    },
    {
      name: "6. Analytics & AI",
      clues: [
        { value: 100, question: "This Power BI feature lets end users change a model input (like a discount rate) using a slider and see results recalculate live, and is considered Gov-ready.", answer: "What-if parameters." },
        { value: 200, question: "This AI visual splits a measure into high-value and low-value contributing segments, useful for root-cause exploration.", answer: "Decomposition tree." },
        { value: 300, question: "This is why key influencers, Python/R visuals, and Azure Machine Learning integrations are all marked Verify for Gov in this course.", answer: "Because their underlying AI services, runtimes, or endpoints may not be available or approved in an Azure Government tenant." },
        { value: 400, question: "Forecasting results in a line chart should be interpreted carefully for this reason.", answer: "Forecasts depend on data quality, history, seasonality, and assumptions — they are not guaranteed predictions." },
        { value: 500, question: "Name a non-AI way to identify exceptions in a trend.", answer: "DAX thresholds, rolling averages, standard deviation bands, or conditional formatting." },
        { value: 600, question: "This is why AI-generated output, such as a Copilot narrative or forecast, should always require this extra step before it is trusted.", answer: "Human review — AI-generated output can be incomplete or incorrect and must be checked against trusted data and business context." },
      ],
    },
    {
      name: "7. Security Design",
      clues: [
        { value: 100, question: "This is the key difference between workspace access and Row-Level Security (RLS).", answer: "Workspace access controls what a user can open/do; RLS filters the rows of data a user sees within content they can already access." },
        { value: 200, question: "This type of RLS uses a DAX filter expression like [UserPrincipalName] = USERPRINCIPALNAME() so one role works for every user instead of needing a role per user.", answer: "Dynamic RLS." },
        { value: 300, question: "This is why hidden columns or hidden report pages should never be treated as a real security boundary.", answer: "Because hiding a column/page only affects the UI — a user with model access (e.g., via Analyze in Excel or the XMLA endpoint) can still query the underlying data." },
        { value: 400, question: "This simpler form of RLS is appropriate for stable roles such as one role per region.", answer: "Static RLS." },
        { value: 500, question: "This security feature hides tables or columns from users and can protect sensitive model objects when supported.", answer: "Object-level security (OLS)." },
        { value: 600, question: "Name three things that should be included in RLS test evidence.", answer: "Test user/group, expected access, actual result, date, tester, role assignment, or exceptions (any three)." },
      ],
    },
    {
      name: "8. Enterprise Deployment",
      clues: [
        { value: 100, question: "Even after publishing to the Power BI Service, this artifact type should remain the source of record for a semantic model and report.", answer: "The PBIP project (source-controlled files)." },
        { value: 200, question: "This Power BI Service distribution mechanism is preferred over granting direct workspace access for delivering production content to end users.", answer: "Apps." },
        { value: 300, question: "This workspace-level permission is required for a report author to build new reports against someone else's shared semantic model.", answer: "Build permission." },
        { value: 400, question: "This is the key difference between workspace Contributor and Viewer roles.", answer: "Contributors can publish and edit content; Viewers consume content without editing workspace artifacts." },
        { value: 500, question: "This type of report connects to an existing shared semantic model instead of containing its own model.", answer: "A thin report." },
        { value: 600, question: "This is the difference between Promoted and Certified content endorsement.", answer: "Promoted indicates useful content endorsed by its owner; Certified indicates authoritative content approved through a governance process." },
      ],
    },
    {
      name: "9. Monitoring & Governance",
      clues: [
        { value: 100, question: "This Power BI Service report/dashboard tells you who viewed content, how often, and from where.", answer: "Usage metrics (usage metrics report)." },
        { value: 200, question: "This component is required to refresh Import-mode data from an on-premises or private network data source.", answer: "An on-premises data gateway." },
        { value: 300, question: "This is why activity logs, audit logs, Purview, and DLP are all marked Verify for Gov in this course.", answer: "Because their availability, retention, and admin API behavior can differ or be restricted in an Azure Government tenant." },
        { value: 400, question: "Name three common causes of scheduled refresh failure.", answer: "Credentials, gateway mapping, source path changes, privacy settings, network failures, or unsupported connectors (any three)." },
        { value: 500, question: "This Power BI Service tool helps diagnose capacity workload pressure, refresh impact, interactive performance, and throttling symptoms.", answer: "The capacity metrics app." },
        { value: 600, question: "Name three things that should be included in an operations runbook.", answer: "Owners, sources, refresh schedule, access model, monitoring cadence, incident response, escalation paths, or validation notes (any three)." },
      ],
    },
    {
      name: "10. Premium, Fabric & Capacity",
      clues: [
        { value: 100, question: "Any capacity or licensing architecture decision should always start by identifying these.", answer: "Workload requirements (concurrency, refresh needs, dataset size, feature needs)." },
        { value: 200, question: "This unit of consumption measures how much compute a Fabric/Premium capacity operation uses, and is central to throttling behavior.", answer: "A Capacity Unit (CU)." },
        { value: 300, question: "This storage mode reads data directly from OneLake Delta tables without a traditional Import/DirectQuery split, and is marked Commercial-focused/Verify for Gov.", answer: "Direct Lake." },
        { value: 400, question: "This type of reporting need — pixel-perfect, printable invoices, formal statements, or highly formatted exports — is a good fit for paginated reports.", answer: "Operational/formal document-style reporting." },
        { value: 500, question: "This Fabric concept is intended to provide a unified logical data lake for Fabric workloads.", answer: "OneLake." },
        { value: 600, question: "This capacity feature, which automatically adds compute during pressure, is marked Commercial-focused/Verify for Gov because it depends on licensing, capacity model, and cloud availability.", answer: "Autoscale." },
      ],
    },
    {
      name: "11. Automation & DevOps",
      clues: [
        { value: 100, question: "This file format (a folder of JSON/TMDL text files) is preferred over the binary PBIX as the source of record because it works with real version control.", answer: "PBIP (Power BI Project format)." },
        { value: 200, question: "This type of identity is used for unattended, non-interactive automation against the Power BI REST API instead of a personal user login.", answer: "A service principal." },
        { value: 300, question: "This is one major risk of storing connection strings, API keys, or credentials directly inside CI/CD pipeline YAML/scripts instead of a secret store.", answer: "Secrets can leak through logs, history, or unauthorized pipeline edits/forks." },
        { value: 400, question: "Name three things a pull request review should look for in Power BI source changes.", answer: "Model changes, report definitions, parameters, security, measures, data sources, or unintended generated changes (any three)." },
        { value: 500, question: "Name three things that must be validated before using Power BI REST APIs against a target tenant.", answer: "Cloud endpoint, permissions, tenant settings, authentication, workspace access, or API availability (any three)." },
        { value: 600, question: "Name three pieces of deployment evidence that should be recorded after a release.", answer: "Commit/version, workspace, deployer, date, validation results, refresh status, or rollback plan (any three)." },
      ],
    },
  ],
};
