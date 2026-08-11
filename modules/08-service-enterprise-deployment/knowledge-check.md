# Knowledge Check

## Questions

1. Why should PBIP remain the source of record even when content is published to the Service?
2. What is the difference between workspace Contributor and Viewer?
3. Why should production content usually be distributed through Apps instead of workspace access?
4. What can cause scheduled refresh to fail?
5. What is the purpose of an on-premises data gateway?
6. What is a thin report?
7. Why is Build permission important for shared semantic models?
8. What is the difference between Promoted and Certified content?
9. Why are App audiences marked **Verify for Gov**?
10. Why are deployment pipelines marked **Verify for Gov**?

## Answer key

1. PBIP stores report and model source files in a reviewable format for git and lifecycle management.
2. Contributors can publish and edit content; Viewers consume content without editing workspace artifacts.
3. Apps provide a cleaner consumer experience and reduce the need to grant broad workspace access.
4. Credential issues, gateway mapping, source path changes, privacy settings, network failures, or unsupported connectors can cause refresh failures.
5. The gateway securely connects Power BI Service to on-premises or network-restricted data sources.
6. A thin report connects to an existing shared semantic model instead of containing its own model.
7. Build permission allows downstream reporting and analysis from a semantic model, expanding reuse and potential data exposure.
8. Promoted indicates useful content endorsed by its owner; Certified indicates authoritative content approved through a governance process.
9. App audience availability and behavior can vary by cloud and Service parity in Azure Government.
10. Deployment pipelines require compatible licensing/capacity and Service availability, which must be validated in the target cloud.

