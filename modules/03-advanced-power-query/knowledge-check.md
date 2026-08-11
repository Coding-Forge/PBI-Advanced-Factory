# Knowledge Check

## Questions

1. Why should complex Power Query solutions use staging queries?
2. When should a staging query have load disabled?
3. What is query folding?
4. Why does query folding depend on the connector and source system?
5. What is one common transformation that can stop query folding?
6. Why should folder-combine solutions filter by extension or file pattern?
7. What problem do parameters solve in Power Query?
8. What is a custom function useful for?
9. Why should data types be applied explicitly?
10. What are `RangeStart` and `RangeEnd` used for?
11. Why are dataflows marked **Verify for Gov**?
12. Why is Dataflows Gen2 marked **Commercial-focused / Verify for Gov**?

## Answer key

1. Staging queries make transformation logic easier to read, reuse, test, and troubleshoot.
2. Disable load when the query is an intermediate step and does not need to appear in the semantic model.
3. Query folding is the ability for Power Query to translate transformation steps back to the source system query.
4. Each connector and source system supports different operations, so not every step can be translated to the source.
5. Examples include adding an index, using some custom functions, changing to an unsupported type, or buffering data too early.
6. Folder-combine solutions should avoid hidden files, temp files, unrelated files, and schema mismatches.
7. Parameters support reusable values such as source paths, environment names, server names, and incremental refresh boundaries.
8. Custom functions encapsulate reusable transformation logic and can be invoked across rows, files, or queries.
9. Explicit types avoid unpredictable auto-detection and make errors easier to identify.
10. `RangeStart` and `RangeEnd` are DateTime parameters used to filter data for incremental refresh policies.
11. Dataflow availability and behavior can vary by cloud, tenant, license, and admin settings.
12. Dataflows Gen2 is Fabric-related and may be commercial-first or unavailable in some sovereign cloud environments unless validated.

