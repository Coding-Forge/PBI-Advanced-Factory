// Jeopardy data for Module 10: Premium, Fabric, and Capacity
// Sourced from modules/10-premium-fabric-capacity/knowledge-check.md
window.JEOPARDY_DATA = {
  boardId: "lab10",
  title: "Module 10: Premium, Fabric, and Capacity",
  categories: [
    {
      name: "Licensing & Capacity",
      clues: [
        { value: 100, question: "This license model is primarily per-user for standard sharing, versus dedicated capacity which provides reserved resources.", answer: "Power BI Pro." },
        { value: 200, question: "This app is the go-to for diagnosing capacity pressure, refresh vs interactive workload, and throttling.", answer: "The Capacity Metrics app." },
        { value: 300, question: "This capacity feature that adds compute on demand is marked Commercial-focused / Verify for Gov because it depends on licensing, capacity model, and cloud availability.", answer: "Autoscale." },
      ],
    },
    {
      name: "Fabric & OneLake",
      clues: [
        { value: 100, question: "Conceptually, this Fabric component is intended as a unified logical data lake for all Fabric workloads.", answer: "OneLake." },
        { value: 200, question: "This storage mode reads Delta tables directly from OneLake and is marked Commercial-focused / Verify for Gov.", answer: "Direct Lake." },
        { value: 300, question: "When Direct Lake is not validated in a sovereign cloud, this is the Gov-safe fallback modeling approach.", answer: "Import mode with incremental refresh and aggregations where validated, or DirectQuery only when source performance and connector support are validated." },
      ],
    },
    {
      name: "Report Formats",
      clues: [
        { value: 100, question: "Pixel-perfect operational reports, printable invoices, and formal statements are the classic fit for this report type.", answer: "Paginated reports." },
        { value: 200, question: "This capacity-scoped endpoint enables external tools like Tabular Editor and SSMS to connect to a semantic model, and is marked Verify for Gov.", answer: "The XMLA endpoint (read/write)." },
        { value: 300, question: "Before recommending a capacity-dependent feature, these are the things you should document.", answer: "Licensing, tenant settings, cloud availability, capacity requirements, admin ownership, security, and fallback path." },
      ],
    },
    {
      name: "Architecture Decisions",
      clues: [
        { value: 100, question: "Architecture decisions in Power BI should start from this instead of from a favorite feature.", answer: "Workload requirements." },
        { value: 200, question: "Name three workload dimensions that drive whether Pro, Premium, or Fabric capacity is the right fit.", answer: "User scale, refresh, data size, latency, governance, or integration." },
        { value: 300, question: "The XMLA endpoint depends on these tenant and capacity prerequisites — name three.", answer: "Compatible capacity, workspace configuration (XMLA read/write enabled), tenant settings, tooling support, and cloud availability." },
      ],
    },
  ],
};
