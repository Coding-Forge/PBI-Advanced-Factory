# Learner Guide

## What you will learn

You will learn how to apply layered Power BI security controls, including static RLS, dynamic RLS, role testing, Build permission, optional object-level security, and sensitivity label considerations.

## Scenario

Contoso Advanced Manufacturing wants regional managers to see only their assigned territories while executives can see all territories. Analysts may build thin reports from certified semantic models, but only when they have appropriate Build permission.

## Prerequisites

- Power BI Desktop
- PBIP report/model from earlier modules
- Basic understanding of relationships and DAX filters
- Optional Power BI Service workspace for role assignment and Build permission labs

## Azure Government readiness

Static and dynamic RLS are **Gov-ready**. OLS, sensitivity labels, Purview integration, external sharing, and B2B behavior are **Verify for Gov**.

## Power BI project format

Save report and model work as PBIP projects. PBIP is the source-controlled format for this workshop. PBIX can be generated from PBIP later if a packaged file is needed.

## Lab files

| File | Purpose |
|---|---|
| `security-user-territory.csv` | Maps synthetic user principal names to territory keys. |
| `security-role-matrix.csv` | Documents intended access by persona and role. |

## Tasks

1. Import security mapping data.
2. Create a static RLS role.
3. Create a dynamic RLS role.
4. Test roles in Desktop.
5. Assign and test roles in Service where available.
6. Review Build permission behavior.
7. Review optional OLS and sensitivity label controls.
8. Complete the security review checklist.

## Validate your work

Your completed work should include:

- Static RLS role.
- Dynamic RLS role using `USERPRINCIPALNAME()`.
- Security mapping table.
- Role testing notes.
- Build permission notes.
- Gov validation notes for OLS, sensitivity labels, Purview, external sharing, and B2B.

