# Proteins & Peptides Search Business Rules

## Business Rules

### Search Entry And Eligibility

1. Proteins & Peptides search must be exposed as a Popular Product Area entry named "Proteins & Peptides".
2. Proteins & Peptides keyword searches must route to `/proteins/query/{keyword}`.
3. The Proteins & Peptides entry must be available from proteins, antibody, ELISA product, genome-database, antibody-immunoassay order, and immunoassay contexts when those contexts match the configured include patterns.
4. The Proteins & Peptides entry must be excluded from document-support persona pages.
5. The Proteins & Peptides entry must be activated on `/proteins/` pages and on protein query URLs for recombinant protein, synthetic peptide, and native protein result paths.
6. Proteins & Peptides search must use the antibody protein subtype context (`ANTIBODY_PROTEIN` / `antibody_protein`) for search-result behavior, filters, product links, and downstream PDP context.
7. Keyword input must honor the configured maximum keyword length of 250 characters.
8. Search requests for `*` must act as wildcard browse requests for Proteins & Peptides rather than literal catalog-number searches.
9. Proteins & Peptides search must use the configured protein page size; the QA configuration sets this to 100.
10. Proteins & Peptides search must participate in Solr re-query behavior when the enabled-subtype list includes `ANTIBODY_PROTEIN`.
11. Proteins & Peptides search must preserve selected filters when keep-my-filters behavior is enabled for `ANTIBODY_PROTEIN`.
12. Inline zero-result-product behavior must apply to Proteins & Peptides when the inline ZRP enabled subtype list includes `ANTIBODY_PROTEIN`.

### Typeahead And Suggestions

13. Proteins & Peptides search must use the configured Proteins & Peptides typeahead URL for product-area suggestions.
14. The configured Proteins & Peptides typeahead request must search the PRANT-filtered protein/peptide suggestion source.
15. New typeahead behavior must not be applied to Proteins & Peptides unless `ANTIBODY_PROTEIN` is added to the configured `newTypeAheadEnabledProductSubTypes` list.
16. Spell-check behavior must not apply to Proteins & Peptides unless `ANTIBODY_PROTEIN` is added to the configured spell-check enabled subtype list.

### Search Results And Filters

17. Proteins & Peptides search results must be restricted to protein/peptide products represented by the antibody protein subtype.
18. Proteins & Peptides product cards must route users to product pages under `/proteins/product/...`.
19. The new filter experience must be used when the enabled-subtype list includes `ANTIBODY_PROTEIN`.
20. The search page must show filter facets from the current result set.
21. Proteins & Peptides filters may include Protein Name, Species, Expression System, Product Type, Application, Product Grade, Tag, New, Activity, and Promotion when those values exist in the result data.
22. Filter counts must be calculated from the current result set and must update when filters are applied or removed.
23. Selected filters must be shown to the user and must be removable.
24. The result count shown to the user must match the current filtered result set returned by search.
25. Zero-result handling must show the configured zero-results message and must not display stale product cards from a prior result set.
26. Metadata handling must apply to Proteins & Peptides when the metadata handler enabled-subtype list includes `ANTIBODY_PROTEIN`.
27. Image search behavior must not apply to Proteins & Peptides unless `ANTIBODY_PROTEIN` is added to the image-search enabled subtype list.

### Sorting, Promotions, Badges, And Compare

28. Proteins & Peptides search must support the configured antibody/protein search sort options.
29. Sort by price must be available only in countries configured for price sorting.
30. Promotional ad behavior may be shown on Proteins & Peptides search when promo-ad behavior is enabled for `ANTIBODY_PROTEIN`.
31. Product badges must not be displayed when `enableBadges` is configured as `false`.
32. Compare behavior must be available only when the compare panel is enabled and the selected product cards satisfy compare requirements.
33. Compare analytics must be emitted when compare analytics are enabled and a user performs compare actions.

### Commerce From Search Results

34. Proteins & Peptides search result cards must request price data through the configured pricing API only when dynamic pricing is enabled and the product/category is pricing-eligible.
35. Pricing calls must respect the configured maximum number of SKUs per pricing call; the QA configuration sets this to 20 SKUs.
36. Search result cards must display price or price prompts only from the current pricing response for the card SKU/package.
37. If price is unavailable for a SKU, the card must display the configured price-unavailable message or price prompt instead of a stale numeric price.
38. Search result cards must request availability only when availability is enabled for the current user/country and SKU.
39. Availability text must be based on the current SKU/package and quantity context where applicable.
40. Add to Cart must be available only for products/SKUs that are orderable in the current commerce response.
41. Long-term unavailable, discontinued, unentitled, or non-orderable SKUs must not expose a normal Add to Cart path.

### Product-Link And Downstream Context

42. Product cards must preserve the catalog number/web ID needed by the product page, data sheet, image gallery, pricing, availability, reference, and structured-data behavior.
43. Search result product cards must not show full Product Specifications, Bioinformatics, Target Information, References, or Q&A content inline unless the search UI has a supported summary field for that data.
44. Proteins & Peptides products are not eligible for Q&A from search context unless the Q&A enabled subtype list includes `ANTIBODY_PROTEIN`.
45. Proteins & Peptides products are not eligible for related-products behavior from the shared related-products configuration unless the enabled subtype list includes `ANTIBODY_PROTEIN`.

## Possible Inferences

1. The QA search page confirms the Proteins & Peptides route, protein subtype configuration, 100-result page size, new-filter eligibility, promo/inline-ZRP eligibility, and lack of new-typeahead, spell-check, Q&A, related-products, and image-search enablement for `ANTIBODY_PROTEIN`.
