// Jeopardy data for Module 2: Advanced DAX
// Sourced from modules/02-advanced-dax/knowledge-check.md
window.JEOPARDY_DATA = {
  boardId: "lab02",
  title: "Module 2: Advanced DAX",
  categories: [
    {
      name: "Evaluation Contexts",
      clues: [
        { value: 100, question: "This is the set of filters applied to a DAX expression by visuals, slicers, relationships, and explicit DAX filters.", answer: "Filter context." },
        { value: 200, question: "Calculated columns and iterator functions commonly create this kind of context, representing the current row being evaluated.", answer: "Row context." },
        { value: 300, question: "This is the name for what happens when row context gets converted into filter context, most often via CALCULATE.", answer: "Context transition." },
      ],
    },
    {
      name: "CALCULATE & Filter Modifiers",
      clues: [
        { value: 100, question: "This DAX function evaluates an expression in a modified filter context and also performs context transition, earning it \"most important function\" status.", answer: "CALCULATE." },
        { value: 200, question: "Reach for this modifier when your intent is to clear filters from a table or column entirely.", answer: "REMOVEFILTERS." },
        { value: 300, question: "This modifier intersects a new filter with existing filters instead of replacing them the way a plain CALCULATE filter argument would.", answer: "KEEPFILTERS." },
      ],
    },
    {
      name: "Measures & Time Intelligence",
      clues: [
        { value: 100, question: "Authoring these first centralizes core logic and makes derived measures easier to read, test, and maintain.", answer: "Base measures." },
        { value: 200, question: "A reliable date table needs to be continuous, have one row per date, include useful attributes, and do this with fact tables.", answer: "Relate correctly to them (one row per date, active relationship to the fact date key)." },
        { value: 300, question: "Inventory on hand and account balances are classic examples of this kind of measure — additive across some dimensions but not simply across time.", answer: "A semi-additive measure." },
      ],
    },
    {
      name: "Advanced Patterns & Tools",
      clues: [
        { value: 100, question: "In a ranking measure, prefer this function over ALL when you want to preserve the user's outer slicer selections while ranking inside them.", answer: "ALLSELECTED." },
        { value: 200, question: "In a measure-switching pattern, this kind of table captures a user selection that drives DAX logic without directly filtering the model.", answer: "A disconnected table." },
        { value: 300, question: "These centralize repeated logic like current period, prior period, and YoY — and are marked Verify for Gov because native authoring depends on Desktop version and TMDL/XMLA workflows.", answer: "Calculation groups." },
      ],
    },
  ],
};
