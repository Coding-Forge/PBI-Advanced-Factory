// Jeopardy data for Module 5: Performance Optimization
// Sourced from modules/05-performance-optimization/knowledge-check.md
window.JEOPARDY_DATA = {
  boardId: "lab05",
  title: "Module 5: Performance Optimization",
  categories: [
    {
      name: "Measure First",
      clues: [
        { value: 100, question: "Before tuning a slow report, this is the very first thing you should do rather than start changing DAX at random.", answer: "Measure — establish a baseline so you know where the actual bottleneck is." },
        { value: 200, question: "This built-in Power BI Desktop tool breaks a page's slowness down into visual display time, DAX query time, and other rendering overhead.", answer: "Performance Analyzer." },
        { value: 300, question: "After you make a tuning change, these five things belong in the change record.", answer: "The baseline, the change made, the result, the tradeoff, and any remaining validation needed." },
      ],
    },
    {
      name: "Model Slimming",
      clues: [
        { value: 100, question: "These kinds of columns compress poorly in VertiPaq and are notorious for bloating memory and query cost.", answer: "High-cardinality columns." },
        { value: 200, question: "Leaving unused columns in a semantic model costs you these three things.", answer: "Larger model size, higher refresh cost, and user confusion." },
        { value: 300, question: "This kind of table answers summary-level queries from a small Import table while still letting detailed questions fall through to DirectQuery.", answer: "An aggregation table." },
      ],
    },
    {
      name: "DAX & Visuals",
      clues: [
        { value: 100, question: "Using these in a DAX measure improves readability and can avoid recomputing the same expensive expression twice.", answer: "Variables (VAR)." },
        { value: 200, question: "This is why cramming a page full of visuals slows it down, even if each visual looks simple.", answer: "Each visual issues its own queries and has to render, so more visuals mean more query and render work per interaction." },
        { value: 300, question: "DirectQuery isn't automatically faster than Import — its speed hinges on these four things.", answer: "Source system performance, network latency, query folding, and the visual query patterns being issued." },
      ],
    },
    {
      name: "Refresh & Gov Readiness",
      clues: [
        { value: 100, question: "This refresh feature processes only recent partitions instead of reloading the entire fact table.", answer: "Incremental refresh." },
        { value: 200, question: "DAX Studio and VertiPaq Analyzer are flagged Verify for Gov because of these kinds of dependencies.", answer: "They're external tools whose access depends on workstation policy, tenant settings, XMLA endpoint availability, and cloud support." },
        { value: 300, question: "The Capacity Metrics app and its telemetry are marked Verify for Gov because availability varies by these factors.", answer: "Cloud (Commercial vs Gov), capacity type, tenant settings, and permissions." },
      ],
    },
  ],
};
