// Jeopardy data for Module 8: Service Enterprise Deployment
// Sourced from modules/08-service-enterprise-deployment/knowledge-check.md
window.JEOPARDY_DATA = {
  boardId: "lab08",
  title: "Module 8: Service Enterprise Deployment",
  categories: [
    {
      name: "Workspaces & Access",
      clues: [
        { value: 100, question: "This workspace role can publish and edit content, while Viewers can only consume it.", answer: "Contributor." },
        { value: 200, question: "Grant this permission on a shared semantic model to allow downstream reporting and analysis from it.", answer: "Build permission — it expands reuse and also potential data exposure." },
        { value: 300, question: "This is why production content is usually distributed through Apps instead of by granting workspace access.", answer: "Apps provide a cleaner consumer experience and avoid granting broad workspace access." },
      ],
    },
    {
      name: "Sharing & Distribution",
      clues: [
        { value: 100, question: "A report that connects to an existing shared semantic model instead of containing its own model is called this.", answer: "A thin report." },
        { value: 200, question: "This endorsement label is owner-applied, versus the higher-tier one that requires a governance process.", answer: "Promoted (owner-endorsed); Certified is the authoritative, governance-approved label." },
        { value: 300, question: "This App feature is marked Verify for Gov because its availability and behavior can vary by cloud and Service parity.", answer: "App audiences." },
      ],
    },
    {
      name: "Refresh & Gateways",
      clues: [
        { value: 100, question: "This component securely connects the Power BI Service to on-premises or network-restricted data sources.", answer: "The on-premises data gateway." },
        { value: 200, question: "Name three common causes of scheduled refresh failure.", answer: "Credential issues, gateway mapping, source path changes, privacy settings, network failures, or unsupported connectors." },
        { value: 300, question: "Before trusting a nightly refresh in production, these gateway-related items should be reviewed alongside credentials and privacy settings.", answer: "Gateway mapping to the dataset, gateway cluster health, and supported connector coverage." },
      ],
    },
    {
      name: "Source of Record & Gov",
      clues: [
        { value: 100, question: "This file format should remain the source of record even when content is published to the Service, because it stores report and model source in a reviewable git-friendly form.", answer: "PBIP (Power BI Project)." },
        { value: 200, question: "This lifecycle feature is marked Verify for Gov because it requires compatible licensing/capacity and Service availability to be validated in the target cloud.", answer: "Deployment pipelines." },
        { value: 300, question: "This is the main governance reason PBIP is preferred over PBIX as the source of record.", answer: "PBIP stores report and model source files in a reviewable format suitable for git and lifecycle management, while PBIX is a packaged binary." },
      ],
    },
  ],
};
