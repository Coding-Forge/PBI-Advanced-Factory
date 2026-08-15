// Jeopardy data for Module 1: Advanced Semantic Modeling
// Sourced from modules/01-advanced-semantic-modeling/knowledge-check.md
window.JEOPARDY_DATA = {
  boardId: "lab01",
  title: "Module 1: Advanced Semantic Modeling",
  categories: [
    {
      name: "Star Schema Basics",
      clues: [
        { value: 100, question: "This is the main reason a star schema is usually preferred over a single flat table in Power BI.", answer: "It reduces duplication, improves readability, simplifies DAX, and usually improves performance." },
        { value: 200, question: "This term describes the level of detail represented by each row in a fact table.", answer: "Grain (fact table grain) — it must be clear so measures aggregate correctly and relationships behave predictably." },
        { value: 300, question: "This lookup table sits between DimProduct and FactTargets because FactTargets is at product-category grain, not product grain.", answer: "DimProductCategory — it avoids a many-to-many relationship on ProductCategory." },
      ],
    },
    {
      name: "Relationships & Filtering",
      clues: [
        { value: 100, question: "You should avoid this type of relationship when it creates ambiguous filter paths or hides poor model design.", answer: "Bi-directional (bidirectional cross-filtering) relationships." },
        { value: 200, question: "These two techniques let you model both order date and ship date against the same date dimension.", answer: "Duplicated role-playing date tables, OR one active relationship plus an inactive relationship activated in a measure with USERELATIONSHIP." },
        { value: 300, question: "This is why many-to-many relationships can create unexpected totals.", answer: "They can duplicate filter paths or apply filters at the wrong grain, inflating or suppressing totals." },
      ],
    },
    {
      name: "Storage Modes",
      clues: [
        { value: 100, question: "This is the key difference between Import and DirectQuery storage.", answer: "Import stores data inside the model; DirectQuery sends queries to the source at interaction time." },
        { value: 200, question: "This storage mode can help a composite model by letting a shared dimension act as Import for performance while still participating in DirectQuery queries.", answer: "Dual storage mode." },
        { value: 300, question: "These Module 1 features should be validated before use in an Azure Government tenant.", answer: "Composite models, DirectQuery source behavior, hybrid tables, large semantic models, and Service behavior for newer modeling features." },
      ],
    },
    {
      name: "Bridge Tables & Date Tables",
      clues: [
        { value: 100, question: "This is the problem a bridge table solves.", answer: "It supports analysis where one entity can belong to multiple categories, such as customers with multiple segments." },
        { value: 200, question: "Use the Power Query date function instead of a simple DAX CALENDAR table when you need these things.", answer: "A date table that is reusable across reports, parameterized by start/end date, aligned to a configurable fiscal year, or enriched with optional holidays before load." },
        { value: 300, question: "Month names, year-month labels, and fiscal-period labels need this kind of extra column so they sort chronologically instead of alphabetically.", answer: "A numeric sort column." },
      ],
    },
  ],
};
