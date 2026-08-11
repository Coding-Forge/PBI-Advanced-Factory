# Slide Outline

## 1. Why advanced DAX matters

- Measures define trusted business logic.
- Context mistakes create wrong answers.
- Complex DAX should be composed from simple, tested measures.

## 2. Evaluation context

- Filter context
- Row context
- Query context
- Visual totals vs. row-level calculations

## 3. Context transition

- What `CALCULATE` does
- Calculated columns vs. measures
- Iterators and row context

## 4. Filter modification

- `ALL`
- `REMOVEFILTERS`
- `ALLEXCEPT`
- `KEEPFILTERS`
- `TREATAS`

## 5. Measure branching

- Base measures
- Derived measures
- Formatting and naming
- Reuse and testing

## 6. Time intelligence

- Date table requirements
- Year-to-date
- Prior year
- Year-over-year change
- Rolling periods

## 7. Semi-additive measures

- Inventory and balance-style calculations
- Last non-blank concept
- Snapshot facts

## 8. Ranking and Top N

- `RANKX`
- `ALL` vs. `ALLSELECTED`
- Top N plus "Other" concept
- Visual-level filters

## 9. Dynamic report logic

- Dynamic titles
- Selected values
- Disconnected tables
- Measure switching

## 10. Debugging and optimization

- Variables
- Reducing repeated calculations
- Testing measures in simple visuals
- Performance Analyzer
- DAX Studio as optional validated tooling

## 11. Azure Government considerations

- Core DAX is Gov-ready.
- External tools are policy-dependent.
- Service model diagnostics require tenant and XMLA validation.

## 12. Knowledge check and lab review

- Common mistakes
- Validation strategies
- Production readiness checklist

