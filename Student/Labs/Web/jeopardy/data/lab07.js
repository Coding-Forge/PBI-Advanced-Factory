// Jeopardy data for Module 7: Security Design
// Sourced from modules/07-security-design/knowledge-check.md
window.JEOPARDY_DATA = {
  boardId: "lab07",
  title: "Module 7: Security Design",
  categories: [
    {
      name: "Access vs RLS",
      clues: [
        { value: 100, question: "Workspace access controls this, while RLS controls that — name the split.", answer: "Workspace access controls who can access the content; RLS filters which rows of data they see once they're in." },
        { value: 200, question: "This permission is critical to watch because it lets users create downstream content or analyze the semantic model, potentially widening data access.", answer: "Build permission." },
        { value: 300, question: "These items belong in your RLS test evidence package.", answer: "Test user or group, expected access, actual result, date, tester, role assignment, and any exceptions." },
      ],
    },
    {
      name: "Static vs Dynamic RLS",
      clues: [
        { value: 100, question: "This flavor of RLS fits simple, stable scenarios like one role per sales region.", answer: "Static RLS." },
        { value: 200, question: "This flavor of RLS is preferred when access is user-specific, group-specific, or driven by a mapping table.", answer: "Dynamic RLS." },
        { value: 300, question: "Dynamic RLS with USERPRINCIPALNAME() can silently return blanks or wrong access when this happens.", answer: "The UPN in the model doesn't exactly match the signed-in user's identity — values must be validated." },
      ],
    },
    {
      name: "Object Security & Hiding",
      clues: [
        { value: 100, question: "Hiding a column in the field list is a usability trick, not this.", answer: "A security boundary — users with sufficient model permissions can still access hidden columns." },
        { value: 200, question: "This model-level security feature actually hides tables or columns from users who shouldn't see them.", answer: "Object-level security (OLS)." },
        { value: 300, question: "Sensitivity labels are marked Verify for Gov because they depend on these things being configured and supported.", answer: "Purview / MIP configuration plus the required cloud and tenant support." },
      ],
    },
    {
      name: "Gov & External Sharing",
      clues: [
        { value: 100, question: "External sharing tends to be more restricted for Gov customers because of these kinds of policies.", answer: "Stricter B2B, external collaboration, compliance, and data handling policies in Gov tenants." },
        { value: 200, question: "Before you promise a customer that a sensitivity label will flow to Excel export, you need to verify these two things.", answer: "That Purview/MIP is configured and that the target cloud/tenant supports the label behavior end-to-end." },
        { value: 300, question: "This is the mindset shift when designing security for a Gov tenant vs a Commercial one.", answer: "Assume features, sharing, and AI/label integrations must be explicitly validated — nothing is on by default just because it works in Commercial." },
      ],
    },
  ],
};
