// Jeopardy data for Module 6: Advanced Analytics and AI
// Sourced from modules/06-advanced-analytics-ai/knowledge-check.md
window.JEOPARDY_DATA = {
  boardId: "lab06",
  title: "Module 6: Advanced Analytics and AI",
  categories: [
    {
      name: "Built-in Analytics",
      clues: [
        { value: 100, question: "These Desktop modeling features are considered Gov-ready because they don't call any AI service.", answer: "What-if parameters." },
        { value: 200, question: "This AI-style visual is great for exploring the drivers behind a metric across multiple explanatory dimensions.", answer: "The decomposition tree." },
        { value: 300, question: "Forecast lines in Power BI must be interpreted with care because they depend on these four things.", answer: "Data quality, history length, seasonality, and the underlying assumptions — forecasts aren't guarantees." },
      ],
    },
    {
      name: "No-AI Alternatives",
      clues: [
        { value: 100, question: "When AI visuals aren't available, these DAX / formatting techniques still let you spot exceptions in a trend.", answer: "DAX thresholds, rolling averages, standard deviation bands, and conditional formatting." },
        { value: 200, question: "Key influencers gets a Verify for Gov flag because availability can differ across these dimensions.", answer: "Cloud, tenant settings, and Service support — it's an AI visual." },
        { value: 300, question: "A Gov-safe alternate path in your lesson plan should include these four elements.", answer: "The learning goal, the unavailable feature, the alternate manual/native approach, and validation notes." },
      ],
    },
    {
      name: "Python, R & Azure ML",
      clues: [
        { value: 100, question: "Before you drop a Python or R visual into a customer report, validate these five things.", answer: "Local runtime, package policy, Service support, data privacy, and customer workstation rules." },
        { value: 200, question: "Integrating Azure Machine Learning into Power BI requires validating this laundry list of items.", answer: "Azure cloud/region, identity, network, workspace, endpoint, data residency, and governance requirements." },
        { value: 300, question: "This is why AI-generated output — whether from Copilot, AutoML, or a script — always needs a human in the loop.", answer: "It can be incomplete or incorrect and must be checked against trusted data and business context." },
      ],
    },
    {
      name: "Copilot Readiness",
      clues: [
        { value: 100, question: "Until you've validated it in the target tenant, this is how Copilot should be taught in class.", answer: "Conceptually only — don't demo it live if you haven't confirmed availability." },
        { value: 200, question: "Copilot availability hinges on these six tenant/service factors.", answer: "Cloud, tenant, capacity, licensing, region, and admin settings." },
        { value: 300, question: "When a Gov customer can't use an AI feature, this is the safest teaching approach instead of skipping the topic.", answer: "Teach the concept, then demonstrate a Gov-safe alternate path with a manual or native equivalent and note validation gaps." },
      ],
    },
  ],
};
