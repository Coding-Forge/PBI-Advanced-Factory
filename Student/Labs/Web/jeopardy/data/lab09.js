// Jeopardy data for Module 9: Monitoring and Governance
// Sourced from modules/09-monitoring-governance/knowledge-check.md
window.JEOPARDY_DATA = {
  boardId: "lab09",
  title: "Module 9: Monitoring and Governance",
  categories: [
    {
      name: "Usage & Adoption",
      clues: [
        { value: 100, question: "These built-in reports help answer questions about adoption, active users, and report views.", answer: "Usage metrics reports." },
        { value: 200, question: "Usage metrics can surface these two lifecycle candidates — reports that need attention and reports that should go away.", answer: "Candidates for improvement and candidates for retirement." },
        { value: 300, question: "Beyond raw views, this consumption pattern from usage metrics helps prioritize optimization work.", answer: "Consumption trends over time, which highlight growing or declining reports and heavy vs light users." },
      ],
    },
    {
      name: "Refresh Troubleshooting",
      clues: [
        { value: 100, question: "This component's failure is a very common root cause of dataset refresh errors when data lives on-premises.", answer: "The on-premises data gateway." },
        { value: 200, question: "Name three refresh-failure causes beyond credentials.", answer: "Gateway issues, source downtime, privacy settings, schema changes, unsupported connectors, or query failures." },
        { value: 300, question: "A previously working refresh suddenly fails after a source team renames a column — this is the category of failure.", answer: "A schema change (source-side breaking change to the query)." },
      ],
    },
    {
      name: "Tenant & Capacity Monitoring",
      clues: [
        { value: 100, question: "This app helps diagnose capacity workload pressure, refresh impact, and throttling symptoms.", answer: "The Capacity Metrics app." },
        { value: 200, question: "These tenant-level controls govern sharing, export, certification, and external users.", answer: "Tenant settings." },
        { value: 300, question: "This workspace, useful for tenant-wide monitoring, may be unavailable due to cloud, tenant configuration, role, or rollout status.", answer: "The Admin monitoring workspace." },
      ],
    },
    {
      name: "Compliance & Runbooks",
      clues: [
        { value: 100, question: "These two log sources are marked Verify for Gov because they require admin permissions, audit configuration, and cloud support.", answer: "Activity logs and audit logs." },
        { value: 200, question: "These two data-protection features depend on M365/Purview cloud support, licensing, label policies, and tenant configuration.", answer: "Microsoft Purview information protection and DLP (Data Loss Prevention)." },
        { value: 300, question: "Name four items that belong in a Power BI operations runbook.", answer: "Owners, sources, refresh schedule, access model, monitoring cadence, incident response, escalation paths, and validation notes." },
      ],
    },
  ],
};
