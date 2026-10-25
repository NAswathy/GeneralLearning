# TaqMan pri-miRNA Assays and Arrays Validation Report

## Scope

This validation report evaluates the business rules captured for the TaqMan miRNA search experience, with emphasis on Pri-miRNA assays, related miRNA tabs, table columns, and compare behavior.

Repositories requested for validation:

- https://github.com/thermofisher/tfcom-magellan-product-service
- https://github.com/thermofisher/magellan-search-taqman-ui

Example page reviewed:

- https://www.thermofisher.com/taqman/microrna/assay/microrna-primary?keyword=*

## Validation Status

Direct repository validation could not be completed in this session.

- The GitHub connector returned an expired authentication-token error.
- `git ls-remote` could not access either requested repository.
- Because source access was unavailable, the rules were validated against deployed page assets and public API behavior instead of repository source.

This report therefore classifies the rule set as a deployed-behavior validation, not a final source-code validation.

## Evidence Reviewed

1. The deployed Pri-miRNA page shell at `https://www.thermofisher.com/taqman/microrna/assay/microrna-primary?keyword=*`.
2. Downloaded Angular UI bundles used by the TaqMan search page.
3. The deployed search API response for Pri-miRNA wildcard search.
4. The deployed product-count API response for miRNA product-family tabs.
5. The deployed compare-panel UI bundle used by TaqMan search results.

## Validation Findings

### Product Family and Tabs

Status: Validated against deployed UI behavior.

The deployed miRNA search experience exposes tabs for Advanced miRNA Assays, Classic miRNA Assays, Pri-miRNA Assays, and miRNA Arrays. Tab availability is count-driven, and keyword context is preserved when navigating between tabs.

The product-count response confirmed Pri-miRNA count data for the reviewed wildcard query. The same response also included additional miRNA-related categories that are not surfaced as the four primary tabs, which should be confirmed with product ownership.

### Pri-miRNA Search Behavior

Status: Validated against deployed UI and API behavior.

The Pri-miRNA page maps the public page route to the Pri-miRNA search subtype. Wildcard search returns Pri-miRNA assay results and supports keyword sanitization before search execution.

For the reviewed wildcard request, the API returned 3,077 Pri-miRNA results.

### Filters

Status: Validated against deployed API behavior.

The wildcard Pri-miRNA API response returned Species as the available facet. The reviewed response included Human, Mouse, and Rat options with counts.

This supports the captured rule that Species is the active refinement facet for the reviewed Pri-miRNA wildcard state.

### Result Table Columns

Status: Validated against deployed UI behavior.

The Pri-miRNA result table contains Assay ID, Assay name, Product type, Species, Size, Price, and Select columns.

Assay ID and Assay name are sortable. The other reviewed columns function as display or action columns.

### Row-Level Behavior

Status: Validated against deployed UI and API behavior.

Each Pri-miRNA result row displays assay identity, assay name, subtype, species, selectable size, catalog number, availability, price, and selection controls. The row also supports copy, details, related products, related arrays where available, citations where available, shared-list actions, and cart actions.

The reviewed API response showed Pri-miRNA products with multiple size and catalog-number combinations, supporting the captured size/catalog rules.

### Pricing, Availability, and Catalog Configuration

Status: Validated against deployed UI and API behavior.

Size selection drives selected catalog number, selected size, selected availability, and pricing. The reviewed Pri-miRNA product example included S, M, and L configurations with made-to-order availability.

The captured rules correctly reflect that catalog number and availability are configuration-specific.

### Compare Feature

Status: Validated against deployed compare UI bundle.

The compare panel appears when results are selected, displays up to three selected products, and enables compare only when two or three products are selected. More than three selected products disables compare.

Export and email limits were validated from the compare bundle:

- Assay export limit: 1,000 selected results
- Assay email limit: 4,000 selected results
- Array export and email limit: 100 selected results

### Arrays and Related Arrays

Status: Partially validated against deployed UI behavior.

The miRNA Arrays tab and related-arrays chip behavior are present in deployed assets. Related arrays are shown only when the related-array count for an assay is greater than zero.

Array-specific product rules require source or additional page validation for full confidence.

## Issues and Risks

1. Source repository access was unavailable.

   The requested multi-repo source validation could not be completed until GitHub access is restored.

2. The Pri-miRNA no-results implementation should be reviewed.

   The deployed Pri-miRNA bundle appears to contain a no-results branch that checks the Classic miRNA subtype when deciding whether to route to the global search state. This may be an implementation defect or an artifact of shared code generation.

3. Product taxonomy needs product-owner confirmation.

   The count API returned miRNA-related categories beyond the four displayed tabs. The business rule set assumes the displayed tabs are the intended customer-facing taxonomy.

4. Backend rule enforcement could not be confirmed.

   API behavior was observed, but validation could not determine whether subtype mapping, filter eligibility, compare limits, and availability mappings are enforced in backend source, frontend source, or both.

5. Pri-miRNA product-detail behavior was not fully source validated.

   Row-level details and related-product behavior were validated from the search UI bundle. Deeper product-detail service rules require repository access or additional API contract review.

## Suggested Improvements

1. Restore repository access and re-run validation directly against `tfcom-magellan-product-service` and `magellan-search-taqman-ui`.
2. Add source-level traceability for each rule, including file path, component or service name, and method name.
3. Confirm whether the Pri-miRNA no-results branch should reference Pri-miRNA rather than Classic miRNA.
4. Document the official miRNA subtype taxonomy and explain why some count API categories are not displayed as tabs.
5. Add automated UI tests for tab enablement, count display, keyword preservation, Species filtering, and Pri-miRNA table columns.
6. Add automated tests for size changes to confirm selected catalog number, availability, price, shared-list payload, and cart payload stay synchronized.
7. Add compare tests covering one selected item, two selected items, three selected items, and more than three selected items.
8. Add contract tests for the Pri-miRNA search API response, especially `dyeSizeData`, `defaultSize`, `defaultCatalogNum`, `species`, and `productSubType`.
9. Add accessibility validation for table headers, row selection, chip toggles, compare modal focus handling, and disabled compare states.
10. Create a formal traceability matrix that maps business rules to source code, API fields, and user-visible behavior.

## Final Assessment

The captured business rules are consistent with the deployed Pri-miRNA search page, deployed API responses, and downloaded UI bundles reviewed in this session.

The rule set should be treated as accurate for observed deployed behavior, with final sign-off pending restored GitHub repository access and source-code traceability.
