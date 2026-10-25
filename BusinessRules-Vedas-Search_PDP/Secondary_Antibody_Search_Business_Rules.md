# Secondary Antibody Search Business Rules

## Business Rules

### Search Entry And Eligibility

- Secondary antibody search is selected through the antibody search experience using the secondary antibody target type.
- Secondary antibody search uses the secondary antibody query path for the entered keyword.
- The secondary antibody search entry is activated for secondary antibody pages, secondary antibody product pages, and secondary antibody sitemap pages.
- Secondary antibody search is excluded from document-support search routing.
- Secondary antibody legacy typeahead, when used, filters suggestions to antibody products and the secondary antibody filter.
- Secondary antibody legacy typeahead returns no more than 15 suggestions.
- Duplicate typeahead suggestion values are shown only once.
- Typeahead suggestion values remove the registered-trademark marker before the selected value is used for search.
- The secondary antibody search tab displays the suggested searches Qdot 585, Alexa Fluor 594, and HRP.
- When a user selects a different antibody search tab outside the search results page, the current search term is cleared.
- When a user selects a different antibody search tab outside the search results page, the Search button is disabled until a new search term is entered.
- The Search button is enabled only when the antibody search term has a value.
- Recent searches are shown only when the search input is empty.
- Selecting a recent search uses that recent search value and submits the search.
- Keyword search runs when the user submits the keyword search action or presses Enter.

### Search Results

- Secondary antibody search results are limited to secondary antibody products.
- Secondary antibody search uses the request country, page position, product type, product subtype, keyword, and selected search field as search inputs.
- Secondary antibody search returns product results only when matching product records are available.
- When no matching product records are available, no secondary antibody result set is returned.
- The default antibody search sort is Relevance.
- The default antibody search keyword is the wildcard keyword.
- The default antibody search species is treated as all species when the selected species value contains the all-species marker.
- Search result count text includes the searched keyword when a keyword is present.
- Secondary antibody result count is configured as 50 results for the secondary antibody subtype.
- Secondary antibody search keyword length is constrained by the configured keyword limit of 250 characters.
- Newer search filters are enabled for secondary antibody results when the secondary antibody subtype is included in the newer-filter subtype list.
- Newer typeahead is not enabled for secondary antibody results unless the secondary antibody subtype is included in the newer-typeahead subtype list.

### Filters And Sorting

- Secondary antibody filters are displayed in the configured order for secondary antibodies.
- Filters with no name are excluded from the active filter list.
- A missing configured filter remains in its configured position as disabled and empty.
- Filters with no available values are disabled.
- Selecting a filter resets the result offset to the first page.
- Selecting a filter adds it to the selected-filter list.
- Clearing a selected filter removes it from the selected-filter list.
- Clear All clears all selected filters, refreshes the results, clears the selected-filter list, and closes the expanded filter area.
- Reset clears all selected filters, refreshes the results, and clears the selected-filter list.
- The first four filter groups are shown in the primary filter row.
- Remaining filter groups are shown under View More Filters.
- Within a filter group, the first four filter values are shown before expanded values.
- A filter value title uses the parent modifier display when one exists; otherwise it combines the filter group name and filter value.
- Filter names shown to users replace SPACE markers with spaces.
- Changing the sort value resets the result offset to the first page.
- Changing the sort value refreshes results using the selected sort.
- Back-button restoration uses the saved selected filters and saved sort value from the prior antibody search state.

### Load More

- Load More is shown only when the total result count is greater than the number of results currently displayed.
- Selecting Load More advances the result offset by one page of results.
- Load More appends the next page of results instead of replacing the existing visible results.
- After a new filter or sort refresh, Load More resets to the first page of results.
- Load More is hidden when the displayed result count reaches the total result count.

### Product Cards And Badges

- Changing a package size updates the displayed SKU for that result.
- Changing a package size updates the product link to use the selected SKU.
- Changing a package size refreshes the displayed price for the selected SKU.
- When pricing is unavailable for a selected SKU, the result displays See in cart.
- FisherSci pricing requests use SKU values with hyphens removed.
- FisherSci pricing is requested in batches by the active pricing batch-size configuration.
- A valid FisherSci price result is treated as Add To Cart.
- An invalid FisherSci price result is treated as Contact Us.
- A FisherSci Unknown Part Number message is displayed as N/A.
- A FisherSci SKU with no returned price data displays N/A.
- Product badges are shown only when product badges are enabled.
- Best Seller is displayed when badges are enabled and a result is marked as Best Seller.
- Search result badges are evaluated separately for non-third-party products and third-party products.
- Most Images is displayed only when product badges are enabled and a result has more than three images and the highest image count in its product group.
- Most References is displayed only when product badges are enabled and a result has more than three references and the highest reference count in its product group.
- Most Images and References is displayed when product badges are enabled and the same result has the highest image count and highest reference count in its product group.

### Result Drawers And Compare

- Only one result drawer can be open at a time.
- Selecting the currently open drawer closes it.
- While a result drawer is loading, additional drawer-open requests are ignored.
- A drawer opens only after its content has loaded.
- Published-figure drawers are tracked separately from other drawer types.
- A maximum of three products can be selected for comparison.
- When three products are selected for comparison, all unselected compare checkboxes are disabled.
- The Compare button is enabled only when at least two products are selected.
- Removing a compared product frees its comparison slot.
- Removing the last compared product hides the comparison bar.
- On mobile, the compare label changes to Remove when the product is selected for comparison and changes back to Compare when it is removed.
- Loading more results preserves existing compare selections.
- Applying a filter clears existing compare selections.
