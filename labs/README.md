# Labs

Lab content should be organized by module.

Suggested structure:

```text
labs\
  01-advanced-semantic-modeling\
  02-advanced-dax\
  03-advanced-power-query\
  04-report-design-ux\
  05-performance-optimization\
  06-advanced-analytics-ai\
  07-security-design\
  08-service-enterprise-deployment\
  09-monitoring-governance\
  10-premium-fabric-capacity\
  11-automation-devops\
  12-capstone\
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

