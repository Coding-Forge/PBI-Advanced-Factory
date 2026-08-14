// Jeopardy data for Module 3: Advanced Power Query
// Sourced from modules/03-advanced-power-query/knowledge-check.md
window.JEOPARDY_DATA = {
  boardId: "lab03",
  title: "Module 3: Advanced Power Query",
  categories: [
    {
      name: "Staging & Structure",
      clues: [
        { value: 100, question: "Complex Power Query solutions use these intermediate queries to make transformation logic easier to read, reuse, test, and troubleshoot.", answer: "Staging queries." },
        { value: 200, question: "Do this to a staging query when it's just an intermediate step and shouldn't appear in the semantic model.", answer: "Disable load (uncheck \"Enable load\")." },
        { value: 300, question: "Folder-combine solutions should filter by extension or file pattern to avoid these three kinds of problems.", answer: "Hidden files, temp files, unrelated files, and schema mismatches." },
      ],
    },
    {
      name: "Query Folding",
      clues: [
        { value: 100, question: "This is the Power Query capability that translates transformation steps back into a native query against the source system.", answer: "Query folding." },
        { value: 200, question: "Folding depends on this — every one supports a different set of operations, so not every step can be pushed to the source.", answer: "The connector and source system." },
        { value: 300, question: "Adding an index, buffering data too early, or changing to an unsupported type will typically do this to a query.", answer: "Break (stop) query folding." },
      ],
    },
    {
      name: "Parameters & Reuse",
      clues: [
        { value: 100, question: "These solve the problem of hard-coded values like source paths, server names, and environment names scattered across queries.", answer: "Parameters." },
        { value: 200, question: "This kind of reusable M artifact encapsulates transformation logic that can be invoked across rows, files, or queries.", answer: "A custom function." },
        { value: 300, question: "These two DateTime parameters have reserved names in Power Query because they filter data for incremental refresh policies.", answer: "RangeStart and RangeEnd." },
      ],
    },
    {
      name: "Types, Dataflows & Gov",
      clues: [
        { value: 100, question: "Apply these explicitly instead of relying on auto-detection so errors are easier to identify and results are predictable.", answer: "Data types." },
        { value: 200, question: "Dataflows are marked Verify for Gov because availability and behavior can vary by these factors.", answer: "Cloud, tenant, license, and admin settings." },
        { value: 300, question: "This Fabric-related dataflow generation is flagged Commercial-focused / Verify for Gov because it may be commercial-first or unavailable in sovereign clouds.", answer: "Dataflows Gen2." },
      ],
    },
  ],
};
