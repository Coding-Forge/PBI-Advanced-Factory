# Labs

Lab content should be organized by lab. Each numbered folder (01-12) is one **Lab**, covering a major topic. Within each lab's `README.md`, numbered subsections (`### Exercise 1`, `### Exercise 2`, ...) walk learners through the individual hands-on steps for that lab. Avoid calling a subsection a "lab" to prevent confusion with the top-level lab numbering.

Suggested structure:

```text
Student\Labs\Source\
  01-advanced-semantic-modeling\    Lab 01
  02-advanced-dax\                  Lab 02
  03-advanced-power-query\          Lab 03
  04-report-design-ux\              Lab 04
  05-performance-optimization\      Lab 05
  06-advanced-analytics-ai\         Lab 06
  07-security-design\               Lab 07
  08-service-enterprise-deployment\ Lab 08
  09-monitoring-governance\         Lab 09
  10-premium-fabric-capacity\       Lab 10
  11-automation-devops\             Lab 11
  12-capstone\                      Capstone Lab
```

Each lab folder should include:

- `README.md` - learner-facing instructions
- `instructor-notes.md` - instructor setup, timing, and talking points
- `starter\` - starter files, using PBIP for Power BI artifacts
- `solution\` - completed files, using PBIP for Power BI artifacts
- `data\` - sample data, if safe to commit
- `images\` - screenshots used by the lab

Power BI work should be developed as PBIP projects so source files can be reviewed and checked into git. PBIX files are optional generated deliverables and should not be the source of record.

Every lab should include an **Azure Government readiness note** that identifies whether the lab is Gov-ready, requires tenant validation, or is commercial-focused with an alternate Gov-safe path.


