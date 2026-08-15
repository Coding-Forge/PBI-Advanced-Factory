// Jeopardy data for Module 4: Report Design and UX
// Sourced from modules/04-report-design-ux/knowledge-check.md
window.JEOPARDY_DATA = {
  boardId: "lab04",
  title: "Module 4: Report Design and UX",
  categories: [
    {
      name: "Audience-Driven Design",
      clues: [
        { value: 100, question: "Designing pages around this and the task at hand helps users answer their specific questions faster.", answer: "The audience (who will use the page)." },
        { value: 200, question: "Reach for this navigation feature when users need detail about a selected entity like a customer, product, or transaction group.", answer: "Drillthrough." },
        { value: 300, question: "These solve the problem of letting report users switch between approved measures or dimensions in a visual without duplicating pages or spawning uncontrolled self-service.", answer: "Field parameters." },
      ],
    },
    {
      name: "Tooltips & Bookmarks",
      clues: [
        { value: 100, question: "A good page tooltip has these four qualities — and importantly does not duplicate what's already on the main page.", answer: "Focused, compact, contextual, and non-duplicative." },
        { value: 200, question: "Capturing these three things unintentionally can make bookmarks change filters or navigation in surprising ways.", answer: "Data, display, and current page." },
        { value: 300, question: "Every guided report experience should include this so users can recover from complex filter or bookmark states.", answer: "A reset path (a reset bookmark or button)." },
      ],
    },
    {
      name: "Visual Craft & Mobile",
      clues: [
        { value: 100, question: "Overusing this makes important exceptions less visible and can distract users with noise.", answer: "Conditional formatting." },
        { value: 200, question: "Mobile layouts need these three things that differ from desktop: fewer visuals, larger touch targets, and this.", answer: "Different prioritization of content (what shows first)." },
        { value: 300, question: "Alt text, tab order, contrast, descriptive titles, keyboard navigation, and avoiding this last one are all part of an accessibility checklist.", answer: "Color-only meaning (relying on color alone to convey information)." },
      ],
    },
    {
      name: "Gov-Aware Features",
      clues: [
        { value: 100, question: "These user-driven visual changes are marked Verify for Gov because they depend on Service availability and tenant settings that can differ in Azure Government.", answer: "Personalized visuals (personalize visuals feature)." },
        { value: 200, question: "For Azure Government delivery these visuals should be optional, because their availability may lag, vary by tenant, or be unavailable in sovereign clouds.", answer: "AI visuals (e.g., Q&A, Key influencers, Smart Narrative)." },
        { value: 300, question: "For every Gov lab that showcases an AI or personalization feature, you must always provide this alongside it.", answer: "A non-AI (non-personalized) fallback path." },
      ],
    },
  ],
};
