# ELISA Product Series Business Rules

## Business Rules

### Product Eligibility And Identity

1. An ELISA product page must identify the product as product category "ELISA" with product type "immunoassay" and product subtype "ELISA".
2. Product-page modules that depend on subtype must receive the ELISA subtype consistently for commerce, data sheets, image gallery, references, related products, documents, structured data, and analytics.
3. The product title must be rendered from the product display name, and the selected catalog number must be rendered from the selected package.
4. The selected product URL must use the ELISA PDP route under `/elisa/product/...`.
5. Product breadcrumb/category links must keep the product in the ELISA Kits category when category data is available.
6. Product citation text must include the product display name, Thermo Fisher Scientific attribution, and catalog number when citation behavior is present.
7. Structured product data must use the product name, image, brand, SKU, manufacturer, description, and non-empty product specifications.
8. If no product image is available for structured product data, the configured ELISA default product image may be used.
9. Structured offer data must be omitted when the product is discontinued, long-term unavailable, not orderable, lacks a final price, or lacks availability.

### Product Title Banner

10. The product title banner region must evaluate long-term unavailable, discontinued, replacement, and product-specific banner-message states.
11. Long-term unavailable products must show long-term unavailable messaging and must not expose a normal purchase path.
12. Discontinued products must show discontinued messaging and must not expose a normal purchase path.
13. Replacement product messaging must be shown when replacement-product data is present.
14. Product-specific banner messages must be shown only when banner messages are enabled and a banner message exists for the product/package.
15. Banner content must refresh when the selected catalog package changes.
16. Closing a dismissible banner must not change product/orderability data.
17. The sample product displays a product-specific banner message promoting another ProQuantum immunoassay kit.

### Product Commerce Card, Price, And Availability

18. The commerce card must use selected package details as the source of catalog number, package size, web ID, orderability, entitlement, priced state, long-term unavailable state, discontinued state, banner message, and parent-SKU status.
19. For a multi-package ELISA product, the commerce card must let the user select among available package sizes and must update product-size, SKU/web ID, pricing, availability, data-sheet link, and banner context after selection.
20. The sample product has package options for 96 Tests and 5 x 96 Tests; the selected package in the QA page is 96 Tests / catalog `A35613`.
21. Price lookup must call the configured pricing API only for eligible products and eligible countries.
22. Pricing requests must be batched within the configured maximum SKU count.
23. Pricing responses with valid final price data must populate price, user price where applicable, currency, and price visibility.
24. Pricing failures or missing price data must fall back to the configured price prompt or unavailable-price message; stale prices must not remain visible.
25. If a pricing response marks a SKU as not orderable, the normal Add to Cart action must be disabled or hidden for that SKU.
26. If a product is long-term unavailable, the commerce card must not show a normal Add to Cart path and must show the configured contact/availability alternative where applicable.
27. If a product is discontinued, the commerce card must not show a normal Add to Cart path.
28. If a product uses a supplier/dealer commerce path, the commerce card must show the configured learn-where-to-buy or dealer-specific path instead of normal Add to Cart.
29. Add to Cart must be available only when the selected SKU is orderable and not long-term unavailable or discontinued.
30. Quantity must be constrained to the allowed commerce range; invalid quantities must trigger validation messaging and must not be submitted.
31. Add to Cart payloads for ELISA products must use the selected web ID/SKU and product identity from the commerce model.
32. Check price/availability behavior must be shown for anonymous users only when the current country and SKU are eligible for the configured pricing/availability flow.
33. Logged-in price/availability behavior must use authenticated user context when available.
34. Availability lookup must call the configured availability API only when availability is enabled for the current user/country and SKU.
35. Availability must be recalculated when selected package or quantity changes.
36. Availability status must be derived from the availability response; positive available quantity must show in-stock behavior, missing/pending data must show pending or estimated availability behavior, and unavailable/order-blocked states must not show as in stock.
37. Estimated availability may be shown when estimated availability is enabled and exact availability is not returned.
38. Shipping condition and lead-time values must be shown from package or availability data when available for the current region.

### Product Details And Specifications

39. Product Specifications must render only product attributes that have values.
40. Product Specifications for ELISA may include Analytical Sensitivity, Assay Range, Sample Type/Volume, Hands-On Time, Time-To-Result, Homogeneous/No-Wash Indicator, Instrument, Product Size, Contents, Shipping Conditions, Storage, Protein Name, Species Tested, Assay Kit Format, and Label or Dye.
41. The sample product specifications include analytical sensitivity below 0.05 pg/mL, assay range 0.064-1,000 pg/mL, serum/plasma/supernatant sample volume of 2-5 uL, 30 minutes hands-on time, 2 hours time-to-result, homogeneous no-wash workflow, qPCR instruments, 96 tests, seven kit components, dry-ice shipping, -20C storage, IL-18 protein name, human tested species, proximity-based immunoassay format, and FAM label/dye.
42. Product description must render when product-specific descriptive content exists.
43. Product-specific content for the sample product must describe quantitative measurement of human IL-18 in small sample volumes using proximity-based amplification technology.
44. Product-specific content may state high sensitivity, broad dynamic range, small sample consumption, 2-hour workflow, no-wash workflow, and no proprietary-instrument requirement when those statements exist in product content.
45. Product-specific workflow content may describe antibody-conjugate binding, ligation, qPCR amplification, standard-curve setup, plate layout, 5PL weighted analysis, and cloud-based ProQuantum analysis when those statements exist in product content.
46. Regulatory statements such as research-use-only and resale restrictions must be shown when present in product content.

### Target Information

47. The Target Information section must render when target-information content exists for the ELISA product.
48. The sample product renders Target Information for IL-18.
49. Target Information must describe the selected target only from stored product content and must not be generated from the search keyword at runtime.
50. Target Information must remain separate from Product Specifications and Product Specific Information even when it appears adjacent to those sections.

### Bioinformatics

51. The Bioinformatics section must render when bioinformatics content exists for the product.
52. Bioinformatics fields must render only non-empty values.
53. The sample ELISA product renders Gene Aliases, Gene ID, Gene Symbol, Protein Aliases, and UniProt ID.
54. Gene ID and UniProt ID must include the species context when that context is available.
55. Protein and gene aliases must be shown as delimited alias lists when alias data exists.
56. Bioinformatics content must not be shown on ELISA products that do not have bioinformatics values.

### Images, Video, And Testing Data

57. The image gallery must render tabs based on available media categories.
58. The sample product includes a video and Testing Data media.
59. Gallery media counts must match the media data for the product and active gallery filters.
60. Video media must include video metadata when video data exists.
61. Full-size image behavior must be available only when full-size images are enabled.
62. Published image limits must respect configured maximum image counts.

### References And Published Figures

63. References must be read from product-page reference data.
64. The sample product has one reference record.
65. When references exist, the References section must render reference content instead of the zero-reference message.
66. Reference entries may include title, authors, journal, journal abbreviation, species, year, PubMed link, summary, sort order, and BenchSci status when those values exist.
67. Published Figures must be shown only when published-figure data exists.

### Questions And Answers

68. Questions & Answers must not be shown for ELISA products unless the Q&A module is enabled for `ELISA`.
69. The sample product page does not render a Q&A link or Q&A widget because the configured Q&A enabled subtype list excludes `ELISA`.
70. Ask-AI or Q&A companion widgets must display only when their configured feature flag is enabled for the page and the product subtype is eligible.

### Related And Recommended Products

71. ELISA related-products behavior may be shown when ELISA related-products behavior is enabled and the related-products widget returns products.
72. The product page must pass product type, product subtype, product ID, country, and language into the ELISA related-products widget.
73. The related-products section must not show an empty related-products shell when the widget has no products.
74. Recommended products may be shown when recommendation data exists for the product.
75. The sample product displays a recommended product card for an IL-6 Human Matched Antibody Pair, including size, price, catalog number, and Add to Cart action.

## Possible Inferences

1. The sample QA product confirms active Product Specifications, Product Description, Target Information, Bioinformatics, video/testing-data media, References, related-products bootstrap, recommended-product card, multi-package commerce data, title banner, and Product Schema behavior for ELISA.
2. Price and availability values are runtime commerce-service responses. The downloaded QA page confirms package/orderability flags and configured API behavior, not a stable live price or availability promise.
