# ELISA Search Business Rules

## Business Rules

### Search Entry And Eligibility

1. ELISA search must be exposed as a Popular Product Area entry named "ELISA Kits".
2. ELISA keyword searches must route to `/elisa/query/{keyword}`.
3. The ELISA search entry must use the ELISA product subtype context.
4. The ELISA search entry must be activated on ELISA kit content pages, ELISA product pages, ELISA query pages, ELISA target pages, immunoassay ELISA query pages, immunoassay target pages, and ELISA target pages.
5. The ELISA search entry must be excluded from document-support persona pages.
6. Keyword input must honor the configured maximum keyword length of 250 characters.
7. Search requests for `*` must act as wildcard browse requests for ELISA kits rather than literal catalog-number searches.
8. The ELISA search page must use the active page result count of 50 results.
9. ELISA search must participate in Solr re-query behavior when the enabled-subtype list includes `ELISA`.
10. ELISA search must preserve selected filters when keep-my-filters behavior is enabled for `ELISA`.
11. Inline zero-result-product behavior must apply to ELISA when the inline ZRP enabled-subtype list includes `ELISA`.

### Typeahead And Suggestions

12. ELISA search must use the configured ELISA typeahead URL for product-area suggestions.
13. The ELISA typeahead request must pass the ELISA product subtype.
14. New typeahead behavior may apply to ELISA because the enabled-subtype list includes `ELISA`.
15. Spell-check behavior may apply to ELISA because the spell-check enabled-subtype list includes `ELISA`.

### Search Results And Filters

16. ELISA search results must be restricted to ELISA kit products.
17. ELISA product cards must route users to product pages under `/elisa/product/...`.
18. The new filter experience must be used when the enabled-subtype list includes `ELISA`.
19. The search page must show filter facets from the current result set.
20. ELISA filters may include Protein Target, Species, Kit Format, Research Area, Sample Type, Instrument, High Sensitivity, and New when those values exist in the result data.
21. Filter counts must be calculated from the current result set and must update when filters are applied or removed.
22. Selected filters must be shown to the user and must be removable.
23. The result count shown to the user must match the current filtered result set returned by search.
24. Zero-result handling must show the configured ELISA zero-results message and must not display stale product cards from a previous result set.
25. Metadata handling must apply to ELISA when the metadata handler enabled-subtype list includes `ELISA`.
26. Image search behavior must not apply to ELISA unless `ELISA` is added to the image-search enabled subtype list.

### Sorting, Promotions, Badges, And Compare

27. ELISA search must support the configured ELISA search sort options.
28. Sort by price must be available only in countries configured for price sorting.
29. Promotional ad behavior may be shown on ELISA search when promo-ad behavior is enabled for `ELISA`.
30. Product badges must not be displayed when `enableBadges` is configured as `false`.
31. Compare behavior must be available only when the compare panel is enabled and selected product cards satisfy compare requirements.
32. Compare analytics must be emitted when compare analytics are enabled and a user performs compare actions.

### Commerce From Search Results

33. ELISA search result cards must request price data through the configured pricing API only when dynamic pricing is enabled and the product/category is pricing-eligible.
34. Pricing calls must respect the configured maximum number of SKUs per pricing call; the QA configuration sets this to 20 SKUs.
35. Search result cards must display price or price prompts only from the current pricing response for the card SKU/package.
36. If price is unavailable for a SKU, the card must display the configured price-unavailable message or price prompt instead of a stale numeric price.
37. Search result cards must request availability only when availability is enabled for the current user/country and SKU.
38. Availability text must be based on the current SKU/package and quantity context where applicable.
39. Add to Cart must be available only for products/SKUs that are orderable in the current commerce response.
40. Long-term unavailable, discontinued, unentitled, or non-orderable SKUs must not expose a normal Add to Cart path.

### Product-Link And Downstream Context

41. Product cards must preserve the catalog number/web ID needed by the product page, data sheet, image gallery, pricing, availability, reference, related-products, and structured-data behavior.
42. Search result product cards must not show full Product Specifications, Bioinformatics, Target Information, References, or Q&A content inline unless the search UI has a supported summary field for that data.
43. ELISA products are not eligible for Q&A from search context unless the Q&A enabled subtype list includes `ELISA`.
44. ELISA products may be eligible for ELISA-specific related-products behavior when ELISA related-products behavior is enabled.

## Possible Inferences

1. The QA search page confirms the ELISA route, ELISA subtype configuration, active 50-result page size, new-filter eligibility, new-typeahead eligibility, spell-check eligibility, promo/inline-ZRP eligibility, metadata handling, and lack of Q&A subtype enablement for ELISA.
