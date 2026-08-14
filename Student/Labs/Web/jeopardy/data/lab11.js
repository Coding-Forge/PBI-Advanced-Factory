// Jeopardy data for Module 11: Automation and DevOps
// Sourced from modules/11-automation-devops/knowledge-check.md
window.JEOPARDY_DATA = {
  boardId: "lab11",
  title: "Module 11: Automation and DevOps",
  categories: [
    {
      name: "PBIP & Source Control",
      clues: [
        { value: 100, question: "This project format is preferred over PBIX as the source of record because it is git-friendly and reviewable.", answer: "PBIP (Power BI Project)." },
        { value: 200, question: "Name three things a pull request reviewer should inspect in a Power BI source change.", answer: "Model changes, report definitions, parameters, security, measures, data sources, and unintended generated changes." },
        { value: 300, question: "This Fabric feature is marked Commercial-focused / Verify for Gov because it may be commercial-first or delayed in sovereign clouds.", answer: "Fabric workspace Git integration." },
      ],
    },
    {
      name: "REST APIs & Endpoints",
      clues: [
        { value: 100, question: "Before calling Power BI REST APIs, validate this endpoint, permissions, tenant settings, authentication, workspace access, and API availability.", answer: "The cloud endpoint (commercial vs sovereign)." },
        { value: 200, question: "This is why CI/CD endpoint behavior must be validated separately for Azure Government.", answer: "Commercial and sovereign cloud endpoints can differ, and API behavior/availability must match the target tenant." },
        { value: 300, question: "When automation is unavailable in a target cloud, this is the Gov-safe alternate delivery path.", answer: "Use PBIP and git for source control, perform reviewed manual deployment, and record deployment evidence." },
      ],
    },
    {
      name: "Service Principals & Secrets",
      clues: [
        { value: 100, question: "This identity type lets pipelines authenticate to Power BI without a user account.", answer: "A service principal." },
        { value: 200, question: "This is why service principals require admin approval before being used against a tenant.", answer: "They can automate access to tenant resources, so they need tenant settings, app registration, scoping, and governance approval." },
        { value: 300, question: "Storing this artifact in a CI/CD pipeline is a common risk; the mitigation is an approved secret store and least privilege.", answer: "Secrets (client secrets, API keys, connection strings)." },
      ],
    },
    {
      name: "External Tools & Evidence",
      clues: [
        { value: 100, question: "These two external tools for semantic model editing are marked Verify for Gov due to XMLA, tenant policy, workstation policy, and cloud support.", answer: "Tabular Editor and ALM Toolkit." },
        { value: 200, question: "Name three items that should be recorded as deployment evidence.", answer: "Commit/version, workspace, deployer, date, validation results, refresh status, and rollback plan." },
        { value: 300, question: "This is the specific reason external XMLA tooling may work in commercial but fail in Gov even with the same license.", answer: "XMLA endpoint availability, tenant policy, and workstation/tooling connectivity may differ by sovereign cloud and must be validated." },
      ],
    },
  ],
};
