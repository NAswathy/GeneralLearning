# Proteins & Peptides Product Series Business Rules

## Business Rules

### Product Eligibility And Identity

1. A Proteins & Peptides product page must identify the product as product category "Protein" with product subtype "Protein" and downstream subtype `antibody_protein`.
2. Product-page modules that depend on subtype must receive the protein subtype consistently for commerce, data sheets, image gallery, references, documents, structured data, and analytics.
3. The product title must be rendered from the product display name, and the selected catalog number must be rendered from the selected package.
4. The selected product URL must use the Proteins & Peptides PDP route under `/proteins/product/...`.
5. Product citation text must include the product display name, Thermo Fisher Scientific attribution, and catalog number.
6. Structured product data must use the product name, image, brand, SKU, manufacturer, description, and non-empty product specifications.
7. If no product image is available for structured product data, the configured no-image placeholder may be used.
8. Product-level scholarly article structured data may be generated for protein products when scholarly-article structured data is enabled for `ANTIBODY_PROTEIN`.
9. Structured offer data must be omitted when the product is discontinued, long-term unavailable, not orderable, lacks a final price, or lacks availability.

### Product Title Banner

10. The product title banner region must evaluate long-term unavailable, discontinued, replacement, and product-specific banner-message states.
11. Long-term unavailable products must show long-term unavailable messaging and must not expose a normal purchase path.
12. Discontinued products must show discontinued messaging and must not expose a normal purchase path.
13. Replacement product messaging must be shown when replacement-product data is present.
14. Product-specific banner messages must be shown only when banner messages are enabled and a banner message exists for the product/package.
15. Banner content must refresh when the selected catalog package changes.
16. Closing a dismissible banner must not change product/orderability data.

### Product Commerce Card, Price, And Availability

17. The commerce card must use selected package details as the source of catalog number, package size, web ID, orderability, entitlement, priced state, long-term unavailable state, discontinued state, lead-time information, and parent-SKU status.
18. For a multi-package Proteins & Peptides product, the commerce card must let the user select among available package sizes and must update product-size, SKU/web ID, pricing, availability, data-sheet link, and banner context after selection.
19. The sample product has package options for 10 ug, 50 ug, 100 ug, 250 ug, 500 ug, and 1 mg; the selected package in the QA page is 50 ug / catalog `100-18B-50UG`.
20. Price lookup must call the configured pricing API only for eligible products and eligible countries.
21. Pricing requests must be batched within the configured maximum SKU count.
22. Pricing responses with valid final price data must populate price, user price where applicable, currency, and price visibility.
23. Pricing failures or missing price data must fall back to the configured price prompt or unavailable-price message; stale prices must not remain visible.
24. If a pricing response marks a SKU as not orderable, the normal Add to Cart action must be disabled or hidden for that SKU.
25. If a product is long-term unavailable, the commerce card must not show a normal Add to Cart path and must show the configured contact/availability alternative where applicable.
26. If a product is discontinued, the commerce card must not show a normal Add to Cart path.
27. If a product uses a supplier/dealer commerce path, the commerce card must show the configured learn-where-to-buy or dealer-specific path instead of normal Add to Cart.
28. Add to Cart must be available only when the selected SKU is orderable and not long-term unavailable or discontinued.
29. Quantity must be constrained to the allowed commerce range; invalid quantities must trigger validation messaging and must not be submitted.
30. Add to Cart payloads for protein products must use the selected web ID/SKU and product identity from the commerce model.
31. Check price/availability behavior must be shown for anonymous users only when the current country and SKU are eligible for the configured pricing/availability flow.
32. Logged-in price/availability behavior must use authenticated user context when available.
33. Availability lookup must call the configured availability API only when availability is enabled for the current user/country and SKU.
34. Availability must be recalculated when selected package or quantity changes.
35. Availability status must be derived from the availability response; positive available quantity must show in-stock behavior, missing/pending data must show pending or estimated availability behavior, and unavailable/order-blocked states must not show as in stock.
36. Estimated availability may be shown when estimated availability is enabled and exact availability is not returned.
37. Shipping condition and lead-time values must be shown from package or availability data when available for the current region.

### Product Details And Specifications

38. The product page must show applications, tested dilution values, and publication counts when application data is available.
39. The sample product displays application rows for Control, In vitro Assay, Miscellaneous PubMed, Western blot control, ELISA standard, Binding assay, Bioactivity, Cell differentiation, Cell stimulation, Cell induction, Cell expansion, PSC/iPSC, and Cell culture.
40. Application rows with publication counts must provide a references link for that application.
41. Application rows without publication counts must not show a publication link.
42. Product Specifications must render only product attributes that have values.
43. Product Specifications for Proteins & Peptides may include Species, Published Species, Expression System, Amino Acid Sequence, Molecular Weight, Class, Type, Purity, Endotoxin Concentration, Activity, Conjugate, Form, Purification, Contains, Storage Conditions, Shipping Conditions, and Amount.
44. The sample product specifications include Human species, E. coli expression system, 17.2 kDa molecular weight, Recombinant class, Protein type, at least 95% purity, less than 1 EU/ug endotoxin, unconjugated format, lyophilized form, purified material, no preservative, -20C storage, ambient shipping, and 50 ug amount.
45. Product Specific Information must render when product-specific descriptive content exists.
46. Product-specific content for the sample product must state that recombinant Human FGF-basic is a 17.2 kDa protein consisting of 154 amino acid residues and is qualified for stem cell use.
47. Product-specific storage/handling content must direct users to the lot-specific Certificate of Analysis when that instruction is present.
48. Regulatory statements such as research-use-only and resale restrictions must be shown when present in product content.

### Target Information

49. The Target Information section must render when target-information content exists for the protein product.
50. The sample product renders Target Information for FGF2 / FGF-basic.
51. Target Information must describe the selected target only from stored product content and must not be generated from the search keyword at runtime.
52. Target Information must remain separate from Product Specifications and Product Specific Information even when it appears adjacent to those sections.

### Bioinformatics

53. The Bioinformatics section must render when bioinformatics content exists for the product.
54. Bioinformatics fields must render only non-empty values.
55. The sample protein product renders Protein Aliases, Gene Aliases, UniProt ID, and Entrez Gene ID.
56. Protein and gene aliases must be shown as delimited alias lists when alias data exists.
57. UniProt ID and Entrez Gene ID must include the species context when that context is available.
58. View more / View less behavior must be available when a bioinformatics text block exceeds the collapsed display threshold.
59. Bioinformatics content must not be shown on Proteins & Peptides products that do not have bioinformatics values.

### Images And Testing Data

60. The image gallery must render tabs based on available media categories.
61. The sample product renders a Testing Data tab with one image.
62. Gallery filtering by application must be available when application filter data exists.
63. Gallery image counts must match the media data for the product and active gallery filters.
64. Full-size image behavior must be available only when full-size images are enabled.
65. Published image limits must respect configured maximum image counts.

### References And Published Figures

66. Reference count and Published Figures count must be read from product-page data.
67. The sample product has `referenceCount = 1694` and `publishedFiguresCount = 0`.
68. When references exist, the References section must render reference cards instead of the zero-reference message.
69. The References section must pass the Protein subtype into reference behavior for protein products.
70. The References section must default to the configured display-card limit; the sample page passes a default display-card limit of 3.
71. Application-specific reference links must filter users to the selected application's references.
72. Reference entries may include citation title, authors, literature ID, journal, volume, page, publication date, URL, species, application name, dilution/citation status, and summary when those values exist.
73. Reference filtering must be available when reference filtering is enabled.
74. Published Figures must be shown only when published-figure data exists.
75. ScholarlyArticle structured data may be emitted for protein references when structured scholarly articles are enabled for `ANTIBODY_PROTEIN`.

### Questions And Answers

76. Questions & Answers must not be shown for Proteins & Peptides products unless the Q&A module is enabled for `ANTIBODY_PROTEIN`.
77. The sample product page does not render a Q&A link or Q&A widget because the configured Q&A enabled subtype list excludes `ANTIBODY_PROTEIN`.
78. Ask-AI or Q&A companion widgets must display only when their configured feature flag is enabled for the page and the product subtype is eligible.

### Related Products

79. Related-products behavior must not be treated as enabled for Proteins & Peptides from the shared related-products subtype configuration unless `ANTIBODY_PROTEIN` is present in the enabled subtype list.
80. A product page may expose a related-products module URL, but related-products results must not be shown unless the product subtype is eligible and the service returns related products.

## Possible Inferences

1. The sample QA product confirms active Product Specifications, Product Specific Information, Target Information, Bioinformatics, Testing Data, References, multi-package commerce data, and Product Schema behavior for Proteins & Peptides.
2. Price and availability values are runtime commerce-service responses. The downloaded QA page confirms package/orderability flags and configured API behavior, not a stable live price or availability promise.
