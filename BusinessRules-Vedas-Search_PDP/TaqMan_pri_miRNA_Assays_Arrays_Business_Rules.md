# TaqMan pri-miRNA Assays and Arrays Business Rules

## Scope

This document captures business rules for the TaqMan miRNA search experience, with emphasis on the Pri-miRNA assays tab, related miRNA tabs, result table columns, catalog and availability behavior, and compare behavior.

Primary example reviewed:

- https://www.thermofisher.com/taqman/microrna/assay/microrna-primary?keyword=*

The rules below are based on deployed page behavior, public API responses, and downloaded UI assets. Direct source repository validation was unavailable because the GitHub repositories could not be accessed in the current session.

## Business Rules

### Search Entry and Product Family

1. The Pri-miRNA search page searches within the TaqMan miRNA product family and defaults to the Pri-miRNA assay subtype.
2. A wildcard keyword search using `*` is allowed and returns the full available Pri-miRNA result set.
3. Search keywords are decoded from the URL query string before search execution.
4. Search keywords allow letters, numbers, spaces, hyphens, underscores, periods, commas, colons, semicolons, and parentheses.
5. Unsupported special characters are removed from the search keyword before search execution, except that `*` remains valid as a wildcard.
6. Starting a new search resets prior search state and result selections before loading the new result set.
7. If no results are returned for the active search and filter state, the page presents the no-results flow instead of showing an empty result table.
8. Pri-miRNA search requests use the miRNA search service subtype that corresponds to Pri-miRNA assays.

### miRNA Product Tabs

1. The miRNA search experience displays product-family tabs for Advanced miRNA Assays, Classic miRNA Assays, Pri-miRNA Assays, and miRNA Arrays.
2. Each tab displays a result count when that product subtype has matches.
3. Tab counts are formatted with thousands separators when needed.
4. A tab is disabled when its result count is zero or unavailable.
5. Selecting an enabled tab routes the user to that subtype while preserving the current keyword.
6. Advanced miRNA Assays route to the Advanced miRNA assay search page.
7. Classic miRNA Assays route to the Classic miRNA assay search page.
8. Pri-miRNA Assays route to the Pri-miRNA assay search page.
9. miRNA Arrays route to the miRNA array search page.
10. The product-type help drawer explains each subtype:
    - Advanced miRNA Assays use a universal reverse transcription reaction and support mature miRNA detection.
    - Classic miRNA Assays use miRNA-specific stem-loop primers for reverse transcription and mature miRNA specificity.
    - Pri-miRNA Assays quantitate primary microRNA transcripts in the miRNA biogenesis pathway.
    - miRNA Arrays contain popular TaqMan miRNA assays on preconfigured plates or cards and are available in Advanced and Classic chemistries.

### Pri-miRNA Filters

1. For wildcard Pri-miRNA search results, the available refinement facet is Species.
2. Species filter options include Human, Mouse, and Rat when result counts are available for those species.
3. Each Species filter value displays the count of matching results.
4. Selecting a Species filter narrows the Pri-miRNA result set to assays compatible with that species.
5. Filter state is applied as part of the search request and affects both displayed results and result counts.

### Pri-miRNA Result Table Columns

1. The Pri-miRNA result table displays the following columns:
    - Assay ID
    - Assay name
    - Product type
    - Species
    - Size
    - Price
    - Select
2. The Assay ID column is sortable.
3. The Assay name column is sortable.
4. Product type, Species, Size, Price, and Select are display or action columns and are not sortable in the reviewed implementation.
5. The Select header checkbox selects all currently loaded result rows when checked.
6. The Select header checkbox clears all selected result rows when unchecked.
7. The Select header shows a partial state when only a subset of the loaded rows is selected.
8. Row selection drives compare-panel visibility and compare eligibility.

### Pri-miRNA Result Row

1. Each Pri-miRNA result row displays the assay ID from the product identifier.
2. The assay ID links to the miRNA genome-database detail page for the assay.
3. On Thermo Fisher pages, the assay ID detail link uses the `/order/genome-database/details/microrna/{assayId}` pattern.
4. On Fisher Scientific pages, the assay ID detail link uses the `/order/genome-database/details/mirna/{assayId}` pattern.
5. Each row displays assay name, product subtype, species, size, price, catalog number, availability, and row-level selection.
6. Product subtype displays as Pri-miRNA for Pri-miRNA assay results.
7. Species displays the species associated with the assay design.
8. The row provides a copy action that copies catalog number and assay ID together.
9. The copy helper states that both catalog number and assay ID are required for ordering the selected assay configuration.
10. After a successful copy action, the page confirms that catalog number and assay ID were copied to the clipboard.

### Size, Catalog Number, Availability, and Price

1. Size choices are derived from the product size and catalog-number data returned for the assay.
2. The default size is selected from the product's default size value.
3. Changing the selected size changes the selected catalog number.
4. Changing the selected size changes the selected availability label.
5. Changing the selected size changes the selected size stored for cart and shared-list actions.
6. Price is requested and displayed for the selected catalog number.
7. A size option with availability equal to Made to order is displayed as a made-to-order item.
8. Any non-made-to-order size option is treated as an inventoried item for display purposes.
9. Pri-miRNA wildcard results can include multiple catalog configurations for one assay, such as S, M, and L package sizes.
10. The catalog number shown in the row must match the currently selected size.

### Row Detail Sections

1. Each Pri-miRNA row can expose additional sections through row chips.
2. The Details section is available for Pri-miRNA rows.
3. The Related products section is available for Pri-miRNA rows.
4. The Citations section is shown only when citation data exists for the assay.
5. The Related arrays section is shown only when related array count is greater than zero.
6. Selecting one row chip activates that section and deactivates the other row sections.
7. The Details section opens the Pri-miRNA assay details module for the selected product.
8. The Related products section uses the assay ID and species to retrieve related miRNA products.
9. The Related arrays section is based on related-array count data for the assay ID.
10. The Citations section retrieves Bioz citation content using the assay ID.

### Discontinued Assays

1. If a Pri-miRNA assay is marked discontinued, the row displays a discontinued warning.
2. The discontinued warning states that evidence indicates the assay may not function as expected in all samples.
3. The discontinued warning directs users to search for a replacement, design a custom assay, or contact technical support.
4. Discontinued assay messaging does not remove the need to display assay identity and supporting context.

### Add to Cart and Shared List

1. Add-to-cart actions use the selected catalog number for the selected Pri-miRNA assay configuration.
2. Add-to-cart actions use quantity 1 by default from the result row.
3. Thermo Fisher add-to-cart requests include the assay ID, selected catalog number, selected size, quantity, and product subtype.
4. Fisher Scientific add-to-cart requests include part number, quantity, unit of measure, and assay ID.
5. If add-to-cart fails, the row displays an unable-to-add-to-cart error and disables add-to-cart for that row until the configuration changes.
6. Adding to a shared list sends the assay ID as the design ID and the selected catalog number as the item ID.
7. Shared-list payloads identify the source as the TaqMan search results page.
8. After a successful shared-list action, the page confirms that the product was added to the shared list.

### Compare Panel

1. The compare panel is displayed when at least one result is selected.
2. The compare panel displays the number of selected items.
3. The compare panel displays up to the first three selected products.
4. When more than three products are selected, the panel shows the additional selected count separately.
5. Compare is enabled only when at least two and no more than three products are selected.
6. Compare is disabled when fewer than two products are selected.
7. Compare is disabled when more than three products are selected.
8. For Pri-miRNA assays, compare uses the assay product ID as the assay identifier.
9. If compare fails, the page displays a generic error asking the user to try again later.
10. The compare panel supports removing selected products from the comparison list.

### Compare Export and Email

1. The compare panel supports downloading selected results.
2. The compare panel supports emailing selected results.
3. Assay result export is limited to 1,000 selected results.
4. Assay result email is limited to 4,000 selected results.
5. Array result export and email actions are limited to 100 selected results.
6. If the selected result set is too large to email, the page displays a size-limit error.
7. If the selected result set is too large to export, the page displays a size-limit error.
8. Emailing selected results requires the user to enter an email address.

### Compare Modal

1. Compare opens a modal view for eligible selected products.
2. The compare modal includes Product Information.
3. The compare modal supports searching within the comparison.
4. The compare modal displays the selected products' assay identifiers.
5. The compare modal supports add-to-cart using the selected catalog number and selected size when those values exist.
6. The compare modal displays the For Research Use Only disclaimer.
7. The compare modal can identify fields with matching values across compared products.

### miRNA Arrays Related Rules

1. The miRNA Arrays tab is part of the same miRNA product-family search experience.
2. miRNA array availability is represented separately from assay availability.
3. Related arrays are surfaced from Pri-miRNA rows only when a related-array count exists for the selected assay.
4. Array compare and export behavior uses stricter result limits than assay compare and export behavior.
5. Array-related compare behavior may require array-specific configurability checks before cart submission.

## Conflicts Identified

No business-rule conflicts were confirmed from the deployed page and API evidence reviewed.

## Open Validation Notes

1. Direct source-code validation against `tfcom-magellan-product-service` and `magellan-search-taqman-ui` could not be completed because repository access was unavailable in the current session.
2. The deployed UI bundle includes a no-results navigation check on the Pri-miRNA page that appears to inspect the Classic miRNA subtype instead of the Pri-miRNA subtype. This should be reviewed in source before treating it as an intended business rule.
3. The product-count response includes additional miRNA-related categories beyond the four displayed miRNA tabs. The displayed taxonomy should be confirmed with product ownership.
