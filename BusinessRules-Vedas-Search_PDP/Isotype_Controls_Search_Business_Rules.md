# Isotype Controls Search Business Rules

## Business Rules

### Search Entry And Eligibility

1. Isotype Controls search must be exposed as a Popular Product Area entry named "Isotype Controls".
2. The Isotype Controls search entry must route keyword searches to `/antibody/control/query/{keyword}`.
3. The Isotype Controls search entry must be activated for control-antibody content pages, Isotype Control product pages, `/antibody/control/` search pages, and Control Antibodies sitemap pages.
4. The Isotype Controls search entry must be available from antibody-related, protein/peptide-related, immunoassay-related, ELISA product, genome-database, and antibody-immunoassay order contexts when those contexts match the configured include patterns.
5. The Isotype Controls search entry must be excluded from document-support persona pages.
6. Isotype Controls search must use the antibody control product subtype (`antibody_control`) for search result behavior, filters, Q&A enablement, related products, commerce calls, and analytics context.
7. Keyword input for Isotype Controls search must honor the configured maximum keyword length of 250 characters.
8. Search requests for `*` must act as wildcard browse requests for Isotype Controls rather than as literal catalog-number searches.
9. Isotype Controls search must use the configured per-page result size for `antibody_control`; the QA configuration sets this to 50 results.
10. Isotype Controls search must participate in Solr re-query behavior when the configured enabled-subtype list includes `ANTIBODY_CONTROL`.
11. Isotype Controls search must preserve selected filters when keep-my-filters behavior is enabled for `ANTIBODY_CONTROL`.

### Typeahead And Search Suggestions

12. New typeahead behavior must not be applied to Isotype Controls unless `ANTIBODY_CONTROL` is added to the configured `newTypeAheadEnabledProductSubTypes` list.
13. When the Isotype Controls search entry has no typeahead URL, the global search UI must not call a product-area-specific Isotype Controls typeahead endpoint for that entry.
14. Spell-check behavior may apply to Isotype Controls only when the configured spell-check subtype list includes `ANTIBODY_CONTROL`.

### Search Results And Filters

15. Isotype Controls search results must be restricted to antibody control products.
16. The search results page must show Isotype Control product cards using the antibody search-result card model.
17. Search result filters must use the new filter experience when the enabled-subtype list includes `ANTIBODY_CONTROL`.
18. Available-format and all-conjugate behavior must be enabled for Isotype Controls when `ANTIBODY_CONTROL` is included in the all-conjugate enabled subtype list.
19. Isotype Controls filter facets must include antibody-control-relevant facets such as Host, Clonality/Class, Conjugate, Application, Format, Target Class, Recombinant, and other configured antibody facets when those values are present in indexed product data.
20. Conjugate filters must group child conjugates under parent conjugate families such as All Conjugates, Unconjugated, Functional Grade, Alexa Fluor, Brilliant UV, Brilliant Violet, eFluor, FITC, HRP, PE, Qdot, and other configured parent families when those families have results.
21. Filter result counts must be calculated from the current search result set and must update when filters are applied or removed.
22. Selected filters must be shown in the selected-filter region and must be removable by the user.
23. The result count displayed to the user must match the filtered result set returned by the search service.
24. Zero-result handling must show the configured zero-results message and must not display stale product cards from a previous result set.
25. Inline zero-result-product handling must apply to Isotype Controls when the inline ZRP enabled subtype list includes `ANTIBODY_CONTROL`.

### Sorting, Badges, And Compare

26. Isotype Controls search must support the configured antibody search sort options.
27. Sort by price must be enabled only in countries configured for price sorting.
28. Product badges must not be displayed when `enableBadges` is configured as `false`.
29. Promotional ads may be shown on Isotype Controls search when promo-ad behavior is enabled for `ANTIBODY_CONTROL`.
30. Compare behavior must be available when the new compare panel is enabled and the selected product cards satisfy the compare requirements.
31. Compare analytics must be emitted when compare analytics are enabled and a user performs compare actions.

### Product Card Commerce

32. Isotype Controls search result cards must request price data through the configured Magellan pricing API only when dynamic pricing is enabled and the product/category is eligible for the pricing API.
33. Pricing calls must respect the configured maximum number of SKUs per pricing call; the QA configuration sets this to 20 SKUs.
34. Search result cards must display price or price prompts only from the current pricing response for the card SKU/package.
35. If price is unavailable for a SKU, the product card must display the configured price-unavailable message or price prompt rather than a stale numeric price.
36. Search result cards must request availability through the configured availability API only when availability is enabled for the current user/country and SKU.
37. Availability text on search cards must be based on the current selected SKU/package and quantity context where applicable.
38. Search result Add to Cart behavior must be available only for products/SKUs that are orderable in the current commerce response.
39. Long-term unavailable, discontinued, unentitled, or non-orderable SKUs must not expose a normal Add to Cart path.

### Search Product Links

40. Product links from Isotype Controls search results must route to Isotype Control PDP URLs under `/antibody/product/...`.
41. Product cards must preserve the catalog number/web ID needed by the PDP, Q&A widget, related-products widget, image gallery, pricing, availability, and data-sheet links.
42. Search result product cards must show image/gallery counts only from indexed image data available for that product.
43. Search result cards must not show Bioinformatics, Target Information, References, or Q&A details inline unless the search UI explicitly has a supported summary field for that data.

### Q&A And Related Products From Search Context

44. Isotype Controls are eligible for Q&A behavior when `ANTIBODY_CONTROL` is present in the configured Q&A enabled subtype list and the current country is Q&A-enabled.
45. Isotype Controls are eligible for related-products behavior when `ANTIBODY_CONTROL` is present in the configured related-products enabled subtype list.
46. Search results must pass the correct product subtype (`antibody_control`) into downstream product, Q&A, and related-product URLs or widgets.

## Possible Inferences

1. The QA wildcard page confirms the Isotype Controls route, control subtype configuration, new filters, related-products enablement, Q&A enablement, all-conjugate enablement, and 50-result page size. Runtime result counts, price values, and availability values remain service-response dependent.
2. New typeahead is not active for Isotype Controls in the QA configuration because the enabled subtype list contains `ANTIBODY_PRIMARY` and `ELISA`, not `ANTIBODY_CONTROL`.
