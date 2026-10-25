# Isotype Controls Product Series Business Rules

## Business Rules

### Product Eligibility And Identity

1. An Isotype Controls product page must identify the product as an antibody product with product subtype `antibody_control` / "Isotype Control".
2. Product-page modules that depend on subtype must receive the Isotype Control subtype consistently for commerce, data sheets, image gallery, related products, Q&A, technical support, and analytics.
3. The product title must be rendered from the product display name, and the selected catalog number must be rendered from the selected package.
4. The product page must expose breadcrumb/navigation paths that keep the product in the Isotype Controls category when category data is available.
5. Product citation text must include the product display name, Thermo Fisher Scientific attribution, catalog number, and RRID when the RRID is available.
6. Structured product data must use the product name, image, brand, SKU, manufacturer, description, and non-empty product specifications.
7. If a product has no product image, structured product data may use the configured no-image placeholder.
8. Structured offer data must be omitted when the product is discontinued, long-term unavailable, not orderable, lacks a final price, or lacks availability.

### Product Title Banner

9. The product title banner region must evaluate long-term unavailable, discontinued, replacement, and product-specific banner-message states.
10. A long-term unavailable product must show long-term unavailable messaging and must not expose the normal orderable purchase path.
11. A discontinued product must show discontinued messaging and must not expose the normal orderable purchase path.
12. Replacement product messaging must be shown when replacement-product data is present.
13. Product-specific banner messages must be shown only when banner messages are enabled and a banner message exists for the product/package.
14. Banner content must refresh when the selected catalog package changes.
15. Dismissible banner behavior must close only the current visible banner state and must not change product/orderability data.

### Product Commerce Card, Price, And Availability

16. The commerce card must use the selected package details as the source of catalog number, package size, web ID, orderability, entitlement, priced state, long-term unavailable state, discontinued state, lead-time information, and parent-SKU status.
17. For a multi-package Isotype Controls product, the commerce card must let the user select among available package sizes and must update product-size, SKU/web ID, pricing, availability, data-sheet link, and banner context after selection.
18. The sample Isotype Control product has package options for 50 µg, 100 µg, and 500 µg; the selected package in the QA page is 100 µg / catalog `14-4714-82`.
19. Price lookup must call the configured pricing API only for eligible products and eligible countries.
20. Pricing requests must be batched within the configured maximum SKU count.
21. Pricing responses with valid final price data must populate price, user price where applicable, currency, and price visibility.
22. Pricing failures or missing price data must fall back to the configured price prompt or unavailable-price message; stale prices must not remain visible.
23. If a pricing response marks a SKU as not orderable, the normal Add to Cart action must be disabled or hidden for that SKU.
24. If a product is long-term unavailable, the commerce card must not show a normal Add to Cart path and must show the configured contact/availability alternative where applicable.
25. If a product is discontinued, the commerce card must not show a normal Add to Cart path.
26. If a product uses a supplier/dealer commerce path, the commerce card must show the configured learn-where-to-buy or dealer-specific path instead of normal Add to Cart.
27. Add to Cart must be available only when the selected SKU is orderable and not long-term unavailable or discontinued.
28. Quantity must be constrained to the allowed commerce range; invalid quantities must trigger validation messaging and must not be submitted.
29. Add to Cart payloads for antibody products must use the selected web ID/SKU and product identity from the commerce model.
30. Check price/availability behavior must be shown for anonymous users only when the current country and SKU are eligible for the configured availability/pricing flow.
31. Logged-in price/availability behavior must use the authenticated user context when available.
32. Availability lookup must call the configured availability API only when availability is enabled for the current user/country and SKU.
33. Availability must be recalculated when the selected package or quantity changes.
34. Availability status must be derived from the availability response; positive available quantity must show in-stock behavior, missing/pending data must show pending or estimated availability behavior, and unavailable/order-blocked states must not show as in stock.
35. Estimated availability may be shown when estimated availability is enabled and exact availability is not returned.
36. Shipping condition and lead-time values must be shown from package or availability data when available for the current region.
37. Request Bulk or Custom Format behavior may be shown only when the selected product/SKU is eligible and orderable under the configured custom-format rules.
38. Aspire program messaging may apply to Isotype Controls when the product type/subtype and country match the configured antibody Aspire eligibility.

### Product Details And Specifications

39. The product page must show tested applications and tested dilution values when application data is available.
40. The sample Isotype Control product displays tested applications for Western Blot, Immunohistochemistry (Paraffin), Immunocytochemistry, Flow Cytometry, Immunoprecipitation, and Control, each with assay-dependent dilution.
41. Product Specifications must render only product attributes that have values.
42. Product Specifications for Isotype Controls may include Host/Isotype, Class, Type, Clone, Conjugate, Form, Concentration, Purification, Storage Buffer, Contains, Storage Conditions, Shipping Conditions, Amount, and RRID.
43. The sample product specifications include Mouse / IgG1, kappa; Monoclonal; Isotype Control; clone P3.6.2.8.1; Unconjugated; Liquid; 0.5 mg/mL; Affinity chromatography; PBS pH 7.2; 0.09% sodium azide; 4°C storage; ambient/wet-ice shipping; 100 µg amount; and RRID AB_470111.
44. Additional conjugate formats must be displayed when alternate-format data exists for the product series.
45. The "View additional formats" behavior must expose alternate conjugates such as Alexa Fluor, APC, Biotin, Brilliant UV, Brilliant Violet, eFluor, FITC, Functional Grade, Pacific Orange, PE, and other available formats from product data.
46. Product Specific Information must be rendered when descriptive product-specific content exists.
47. Product-specific Isotype Control text must state supported/reported/tested use based on the product content, including whether the item is useful as an isotype control and how it should be used relative to the experimental antibody.
48. Purity, aggregation, and filtration statements must be displayed only when present in product-specific content.
49. Regulatory statements such as "For Research Use Only" and resale restrictions must be shown when present in product content.

### Target Information

50. The Target Information section must render when target-information content exists for the Isotype Control product.
51. The sample Isotype Control product renders Target Information for Mouse IgG1.
52. Target Information content must describe the selected target/isotype only from stored product content and must not be generated from search keywords at runtime.
53. Target Information must remain separate from Product Specifications and Product Specific Information even when it appears adjacent to those sections.

### Bioinformatics

54. The Bioinformatics section must render when bioinformatics content exists for the product.
55. The sample Isotype Control product renders Bioinformatics content for Protein Aliases.
56. Bioinformatics fields must render only non-empty values.
57. Protein Aliases must be shown as a delimited alias list when alias data exists.
58. View more / View less behavior must be available when a bioinformatics text block exceeds the collapsed display threshold.
59. Bioinformatics content must not be shown on Isotype Controls products that do not have bioinformatics values.

### Images And Testing Data

60. The image gallery must render tabs based on available media categories.
61. The sample Isotype Control product renders a Testing Data tab with 34 images.
62. Gallery filtering by application must be available when application filter data exists.
63. Gallery image counts must match the media data for the product and active gallery filters.
64. Full-size image behavior must be available only when full-size images are enabled.
65. Published image limits must respect configured maximum image counts.

### References And Published Figures

66. Reference count and Published Figures count must be read from product-page data.
67. The sample Isotype Control product has `referenceCount = 0` and `publishedFiguresCount = 0`.
68. When the reference count is zero, the References section must show the zero-result reference message and the "Cite this product" action instead of a reference list.
69. Reference lists must be shown only when references exist.
70. Published Figures must be shown only when published-figure data exists.
71. CiteAb links must include the product catalog number when product citation support is enabled.

### Questions And Answers

72. The Q&A widget must be enabled for Isotype Controls only when Q&A is enabled, the country is enabled, and `ANTIBODY_CONTROL` is present in the configured Q&A enabled subtype list.
73. The product page must pass product ID, product name, host app, user/login state, Q&A base URL, and subtype `antibody_control` into the Q&A widget.
74. The sample product passes product ID `14-4714-82`, product name "Mouse IgG1 kappa", and subtype `antibody_control` to the Q&A widget.
75. Q&A retrieval for Isotype Controls must include exact product ID/SKU matching when an exact product context is supplied.
76. Q&A filtering for control products must include control-relevant product attributes such as application, host, clonality/class, conjugate, target class, format, recombinant status, and product subtype when those attributes are available.
77. Q&A count requests must return counts without loading full question-answer payloads.
78. Q&A list requests must sort and page results according to the configured Q&A service sort rules.
79. Q&A service failures must return an empty or zero-result Q&A state rather than blocking the product page.
80. Ask-AI or Q&A companion widgets must display only when their configured feature flag is enabled for the page.

### Related Products

81. Related Products must be enabled for Isotype Controls only when the related-products module is enabled and `ANTIBODY_CONTROL` is present in the enabled product-subtype list.
82. The product page must pass the selected product ID and subtype `antibody_control` to the related-products module.
83. Related-product records for Isotype Controls must be created only from source rows whose type is Isotype Control.
84. Related-product ingestion must reject or skip source rows that do not satisfy required Isotype Control fields, such as usable catalog number and host/isotype data.
85. Host species, isotype, conjugate, application, clone, size, unit, and price fields must be normalized from source data before related-product matching.
86. Multi-value source fields such as applications, conjugates, and isotypes must be split into discrete values for matching and display.
87. Application values used for related products must remove dilution-only text before matching.
88. Related Isotype Controls must preserve catalog number and product URL so the user can navigate from a related product to its PDP.
89. Related-products UI must not show an empty related-products shell when the service returns no related products.

## Possible Inferences

1. The sample QA product confirms active Product Specifications, Target Information, Bioinformatics, Testing Data, References-zero-state, Q&A, related-products bootstrap, multi-package commerce data, and Product Schema behavior for Isotype Controls.
2. Price and availability values are runtime commerce-service responses. The downloaded QA page confirms package/orderability flags and configured API behavior, not a stable live price or availability promise.
