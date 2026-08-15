# Instructor Guide

## Module summary

This module should be delivered as an "analytics options" module, not a promise that every AI or advanced analytics feature is available in every tenant. Keep what-if parameters as the required Gov-ready core, and treat AI visuals, Python/R, Azure ML, and Copilot as validation-dependent.

## Audience and prerequisites

Best fit for report authors, analysts, semantic model developers, data scientists, BI platform owners, and administrators responsible for feature governance.

Learners should understand basic visuals, measures, slicers, and report interaction patterns.

## Learning objectives

- Build what-if parameter scenarios.
- Use or explain decomposition tree, forecasting, key influencers, and anomaly detection.
- Provide non-AI alternate patterns for Gov delivery.
- Explain governance considerations for Python/R visuals.
- Explain Azure ML integration dependencies.
- Explain Copilot concepts and availability constraints.
- Document feature status before using AI-assisted experiences in customer labs.

## Delivery flow

1. Start with the distinction between analytical patterns and AI features.
2. Build a what-if parameter scenario as the required hands-on lab.
3. Demonstrate or discuss decomposition tree where available.
4. Demonstrate or discuss forecasting and anomaly detection where available.
5. Demonstrate or discuss key influencers where available.
6. Review Python/R visual prerequisites and governance.
7. Review Azure ML integration architecture and validation needs.
8. Discuss Copilot conceptually, with clear availability caveats.
9. Compare commercial-enhanced and Gov-safe delivery paths.

## Feature availability

| Feature | Status | Instructor note |
|---|---|---|
| What-if parameters | Gov-ready | Required core lab. |
| Decomposition tree | Verify for Gov | Demonstrate only if available. |
| Forecasting/anomaly detection | Verify for Gov | Demonstrate only if available. |
| Key influencers | Verify for Gov | AI feature; keep optional. |
| Python/R visuals | Verify for Gov | Requires approved runtime/packages and Service support. |
| Azure ML integration | Verify for Gov | Requires matching Azure cloud and network/identity validation. |
| Copilot | Commercial-focused / Verify for Gov | Treat conceptually unless confirmed. |

## Environment setup

- Power BI Desktop installed.
- A PBIP report/model from earlier modules.
- Optional: Tenant where decomposition tree, key influencers, forecasting, or anomaly detection are available.
- Optional: Approved Python/R runtime and packages.
- Optional: Azure ML workspace in an approved cloud/region.
- Optional: Power BI/Fabric tenant with Copilot confirmed available.

## Lab facilitation notes

- Do not require AI visuals for Gov customers unless validated.
- Provide explicit alternate non-AI analysis paths.
- Avoid customer or sensitive data in Python/R, Azure ML, and Copilot demos.
- Ask platform owners to validate tenant settings and data residency before enabling AI features.

## Common issues and fixes

| Issue | Likely cause | Fix |
|---|---|---|
| AI visual is unavailable | Tenant, cloud, license, or admin setting limitation | Use Gov-safe alternate path and mark feature **Verify for Gov**. |
| Python/R visual fails | Runtime, package, or policy issue | Validate Desktop configuration and approved packages. |
| Forecasting option is missing | Unsupported visual type or data shape | Use a line chart with a valid date axis and numeric value. |
| Copilot is unavailable | Cloud, capacity, tenant, or licensing limitation | Teach conceptually and do not include as required hands-on. |
| Azure ML integration fails | Identity, network, region, or cloud mismatch | Validate architecture before delivery. |

## Gov delivery notes

The required what-if parameter lab is Gov-ready. Decomposition tree, key influencers, forecasting, anomaly detection, Python/R visuals, Azure ML integration, and Copilot must be marked **Verify for Gov** or **Commercial-focused** and should remain optional until validated.

## Commercial-enhanced options

- Demonstrate AI visuals in a validated commercial tenant.
- Demonstrate Copilot in Power BI/Fabric if available.
- Demonstrate Azure ML integration with an approved workspace.

