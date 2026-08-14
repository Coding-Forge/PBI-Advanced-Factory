// Jeopardy data - Cumulative Final Review (all 11 modules)
// One category per module, 3 clues each, sourced from each module's knowledge-check.md
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
      ],
    },
    {
      name: "2. Advanced DAX",
      clues: [
        { value: 100, question: "This is the set of filters applied to a DAX expression by visuals, slicers, relationships, and explicit DAX filters.", answer: "Filter context." },
        { value: 200, question: "CALCULATE performs this operation that converts row context into filter context.", answer: "Context transition." },
        { value: 300, question: "This DAX function variant intersects a new filter with existing filters instead of replacing them, unlike a plain filter argument in CALCULATE.", answer: "KEEPFILTERS." },
      ],
    },
    {
      name: "3. Power Query",
      clues: [
        { value: 100, question: "This query-design pattern separates raw source extraction from transformation logic so complex Power Query solutions are easier to maintain.", answer: "Staging queries." },
        { value: 200, question: "This term describes a data source engine executing Power Query transformation steps natively instead of Power BI processing them locally.", answer: "Query folding." },
        { value: 300, question: "This Power Query feature solves the problem of hardcoded values (like file paths or date ranges) scattered across multiple queries.", answer: "Parameters." },
      ],
    },
    {
      name: "4. Report Design & UX",
      clues: [
        { value: 100, question: "Report pages should be designed around these two things so learners/users can find what they need quickly.", answer: "Audience and task." },
        { value: 200, question: "This report feature type lets a user click a visual to jump to a detail page filtered to that context.", answer: "Drillthrough." },
        { value: 300, question: "This is why every guided report experience (bookmarks, drillthrough, navigation buttons) should include one of these.", answer: "A reset path — so users can return to a known starting state." },
      ],
    },
    {
      name: "5. Performance Optimization",
      clues: [
        { value: 100, question: "Performance optimization should always start with this activity before making any changes.", answer: "Measurement (establishing a baseline)." },
        { value: 200, question: "This built-in Power BI Desktop tool helps identify which visuals, DAX queries, or Power Query steps are consuming the most time.", answer: "Performance Analyzer." },
        { value: 300, question: "This type of column (with many unique values, like a transaction ID or exact timestamp) can significantly increase model size and hurt compression.", answer: "A high-cardinality column." },
      ],
    },
    {
      name: "6. Analytics & AI",
      clues: [
        { value: 100, question: "This Power BI feature lets end users change a model input (like a discount rate) using a slider and see results recalculate live, and is considered Gov-ready.", answer: "What-if parameters." },
        { value: 200, question: "This AI visual splits a measure into high-value and low-value contributing segments, useful for root-cause exploration.", answer: "Decomposition tree." },
        { value: 300, question: "This is why key influencers, Python/R visuals, and Azure Machine Learning integrations are all marked Verify for Gov in this course.", answer: "Because their underlying AI services, runtimes, or endpoints may not be available or approved in an Azure Government tenant." },
      ],
    },
    {
      name: "7. Security Design",
      clues: [
        { value: 100, question: "This is the key difference between workspace access and Row-Level Security (RLS).", answer: "Workspace access controls what a user can open/do; RLS filters the rows of data a user sees within content they can already access." },
        { value: 200, question: "This type of RLS uses a DAX filter expression like [UserPrincipalName] = USERPRINCIPALNAME() so one role works for every user instead of needing a role per user.", answer: "Dynamic RLS." },
        { value: 300, question: "This is why hidden columns or hidden report pages should never be treated as a real security boundary.", answer: "Because hiding a column/page only affects the UI — a user with model access (e.g., via Analyze in Excel or the XMLA endpoint) can still query the underlying data." },
      ],
    },
    {
      name: "8. Enterprise Deployment",
      clues: [
        { value: 100, question: "Even after publishing to the Power BI Service, this artifact type should remain the source of record for a semantic model and report.", answer: "The PBIP project (source-controlled files)." },
        { value: 200, question: "This Power BI Service distribution mechanism is preferred over granting direct workspace access for delivering production content to end users.", answer: "Apps." },
        { value: 300, question: "This workspace-level permission is required for a report author to build new reports against someone else's shared semantic model.", answer: "Build permission." },
      ],
    },
    {
      name: "9. Monitoring & Governance",
      clues: [
        { value: 100, question: "This Power BI Service report/dashboard tells you who viewed content, how often, and from where.", answer: "Usage metrics (usage metrics report)." },
        { value: 200, question: "This component is required to refresh Import-mode data from an on-premises or private network data source.", answer: "An on-premises data gateway." },
        { value: 300, question: "This is why activity logs, audit logs, Purview, and DLP are all marked Verify for Gov in this course.", answer: "Because their availability, retention, and admin API behavior can differ or be restricted in an Azure Government tenant." },
      ],
    },
    {
      name: "10. Premium, Fabric & Capacity",
      clues: [
        { value: 100, question: "Any capacity or licensing architecture decision should always start by identifying these.", answer: "Workload requirements (concurrency, refresh needs, dataset size, feature needs)." },
        { value: 200, question: "This unit of consumption measures how much compute a Fabric/Premium capacity operation uses, and is central to throttling behavior.", answer: "A Capacity Unit (CU)." },
        { value: 300, question: "This storage mode reads data directly from OneLake Delta tables without a traditional Import/DirectQuery split, and is marked Commercial-focused/Verify for Gov.", answer: "Direct Lake." },
      ],
    },
    {
      name: "11. Automation & DevOps",
      clues: [
        { value: 100, question: "This file format (a folder of JSON/TMDL text files) is preferred over the binary PBIX as the source of record because it works with real version control.", answer: "PBIP (Power BI Project format)." },
        { value: 200, question: "This type of identity is used for unattended, non-interactive automation against the Power BI REST API instead of a personal user login.", answer: "A service principal." },
        { value: 300, question: "This is one major risk of storing connection strings, API keys, or credentials directly inside CI/CD pipeline YAML/scripts instead of a secret store.", answer: "Secrets can leak through logs, history, or unauthorized pipeline edits/forks." },
      ],
    },
  ],
};
