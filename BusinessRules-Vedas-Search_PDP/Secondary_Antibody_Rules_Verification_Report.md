# Secondary Antibody Rules Verification Report

## Verification Scope

- Search example reviewed: `https://www.qa.thermofisher.com/antibody/secondary/query/*`
- Product example reviewed: `https://www.qa.thermofisher.com/antibody/product/Goat-anti-Mouse-IgG-H-L-Highly-Cross-Adsorbed-Secondary-Antibody-Polyclonal/A32723TR`
- Both QA URLs returned page content on May 11, 2026.
- Verification used QA page HTML, QA page configuration values, and repository evidence from the Magellan search, Q&A, BID, and related-products repositories.

## Overall Assessment

- The generated secondary antibody search rules are mostly correct and align with the QA search page and shared antibody search implementation.
- The generated secondary antibody product rules are mostly correct for the product title banner, commerce card, price and availability behavior, product details, specifications, target information, references, published figures, Q&A, and related-products enablement.
- The secondary antibody product example does not display a Bioinformatics section. No explicit secondary antibody Bioinformatics rule was confirmed from the reviewed page or the reviewed Bioinformatics feature evidence.
- Secondary antibody Q&A rules are different from primary antibody Q&A rules and were adjusted accordingly.
- Some behaviors should remain conditional because the live QA configuration differs from older legacy JavaScript and because price/availability values are populated through dynamic commerce calls.

## Search Page Verification

### Confirmed On The QA Search Page

- The page is a secondary antibody wildcard search page.
- The page title identifies the result set as Secondary Antibodies.
- The page displays 2,216 results for the wildcard query.
- Secondary antibody search uses the secondary antibody query route.
- The page configuration includes secondary antibody in the newer-filter subtype list.
- The page configuration sets secondary antibody result count to 50.
- The page configuration sets the maximum antibody search keyword length to 250.
- The page configuration includes secondary antibody in Q&A-enabled product subtypes.
- The page configuration includes secondary antibody in related-products-enabled product subtypes.
- The page configuration has product badges disabled.
- The page includes compare functionality.

### Supported By Repository Logic, Not Fully Proven By Static Page HTML

- Secondary antibody legacy typeahead uses the secondary antibody filter value.
- Secondary antibody legacy typeahead returns no more than 15 suggestions.
- Duplicate typeahead suggestion values are shown only once.
- Typeahead removes registered-trademark markers from selected values.
- The secondary antibody search tab uses Qdot 585, Alexa Fluor 594, and HRP as suggested searches.
- Selecting a filter resets the result offset to the first page.
- Sorting resets the result offset to the first page.
- Load More appends additional rows.
- Compare allows up to three selected products and enables Compare only when at least two products are selected.

### Search Rules Needing Review Or Rewording

- Newer typeahead is not enabled for secondary antibody in the QA configuration; only `ANTIBODY_PRIMARY` and `ELISA` are listed. Any secondary typeahead rule should be labeled as legacy typeahead or revalidated against the active runtime path.
- Product badge rules should be conditional because the QA configuration has `enableBadges:false`.
- FisherSci pricing batch size should be tied to active configuration. The live QA configuration exposes a batch-size setting, while older legacy JavaScript used a fixed batch size.
- The search rules should avoid saying secondary search has Bioinformatics behavior; Bioinformatics belongs to product pages and was not confirmed for the secondary example.

## Product Page Verification

### Confirmed On The QA Product Page

- The product page is for A32723TR, a Goat anti-Mouse IgG secondary antibody.
- The page identifies the product type as Secondary Antibody.
- The page title identifies the product as Goat anti-Mouse IgG (H+L) Highly Cross-Adsorbed, Alexa Fluor Plus 488, catalog number A32723TR.
- The product order model uses product type antibody and product subtype antibody_secondary.
- The product order model includes two package options: A32723TR for 100 µg and A32723 for 1 mg.
- Both package options include the Alexa Fluor Plus banner message.
- Both package options include a Learn more link in the banner message.
- Both package options are not marked long-term unavailable.
- Both package options are not marked discontinued.
- The page configuration has banner messages enabled.
- The page configuration has dynamic price enabled.
- The page configuration enables the new pricing API for antibody products.
- The page configuration enables the new availability API.
- The page configuration enables estimated availability.
- The page configuration enables the OAuth2 availability API.
- The page configuration enables shipping-condition display.
- The Product Details section is present.
- Product Details displays tested applications and dilution values.
- Product Specifications are present.
- Product Specifications include species reactivity, host/isotype, class, type, immunogen, conjugate, excitation/emission maximum, form, concentration, amount, purification, storage buffer, contents, storage conditions, shipping conditions, RRID, target, cross adsorption, and antibody form.
- The page displays View additional formats for conjugate options.
- The page displays Request custom conjugation.
- The page displays Product Specific Information.
- The page displays Target Information.
- The page displays For Research Use Only, Not for use in diagnostic procedures, and not-for-resale notices.
- The page displays References (0).
- The page asks users to report publications citing the product when references are zero.
- The page provides a Cite this product action.
- The page exposes `referenceCount = 0`.
- The page exposes `publishedFiguresCount = 76`.
- The page exposes the Q&A widget configuration.
- The page exposes related-products widget configuration.
- The page configuration includes secondary antibody in Q&A-enabled and related-products-enabled product subtypes.

### Supported By Repository Logic, Not Fully Proven By Static Page HTML

- Product banners are shown when a package is long-term unavailable, discontinued, or has a banner message.
- The generic banner message updates when the selected package changes.
- Long-term-unavailable and discontinued banners use different user-facing messages and Technical Support paths.
- Multipack commerce cards use the selected package for SKU, price, availability, data-sheet selection, and banner refresh.
- Child package SKUs with ERR#1100 or ERR#1200 price messages are removed from the package selector, except for the parent SKU.
- Pricing failures default to View price in cart with Add to Cart before long-term-unavailable, discontinued, and error rules are applied.
- Long-term-unavailable packages are not orderable and use Contact Us.
- Discontinued packages are not orderable.
- Pricing Error action values make a package not orderable.
- Add to Cart is allowed only for orderable packages and valid quantities from 1 through 9,999.
- Quantity entry below 1 is reset to 1, and quantity entry above 9,999 is reset to 9,999.
- Availability display depends on country or login context, the selected package, and the availability API result.
- In-stock availability is displayed when available quantity is greater than zero.
- Estimated availability is displayed when availability is enabled, the package is orderable, estimated availability is enabled, and the availability result requires an estimate.
- Pending estimated availability is displayed when the availability date is pending or missing.
- Dealer-enabled signed-in availability can show partial stock, domestic stock, overseas stock, and estimated availability.
- Product structured data removes offer data when price, availability, or orderable status is not valid.
- BenchSci reference cards display images and published figures with a BenchSci icon when secondary antibody reference cards exist.
- Non-BenchSci reference cards display species, dilution, description, and authors when secondary antibody reference cards exist.
- Secondary antibody related-product graph records are created only from source rows whose type is Secondary Antibody.
- Secondary antibody related-product relationships split target species, target class, isotype, conjugate, and application values according to the configured parsing rules.
- Secondary antibody Q&A matching includes exact SKU matches and keyword-filter matches.
- Secondary antibody Q&A sorting and error behavior follow the shared Q&A service rules.

### Product Rules Needing Review Or Rewording

- The product example does not display Bioinformatics. Do not include Bioinformatics display rules for secondary antibodies unless another current secondary product page or active implementation evidence confirms them.
- The older Bioinformatics feature evidence includes primary antibodies, isotype controls, and proteins/peptides, but not secondary antibodies.
- The QA page static HTML confirms the product order model and banner message, but live commerce price and availability values require browser execution and commerce API responses.
- The product order model marks both A32723TR and A32723 as not orderable before dynamic pricing is applied; the final Add to Cart state should be verified after pricing resolves in the browser.
- The product page exposes lead-time fields for EU and CN package data, but the reviewed evidence did not confirm a visible secondary PDP lead-time rule for this example.
- Reference sorting rules were not confirmed on the secondary product example. The QA configuration includes `referenceSortByFilterRemoved:true`, so reference-sort rules should not be presented as active secondary PDP behavior without further active implementation evidence.
- The product page shows 76 published figures while the configuration exposes a maximum published-image value of 40. Published-figure count versus display cap should be verified in the active image-gallery implementation.
- The secondary product page has zero references, so detailed reference-card field behavior was not visible on this example.

## Suggested Improvements

- Add a rule-level verification status to future outputs: Confirmed on QA page, Supported by repository logic, Configuration-supported, Requires interaction test, or Needs recheck.
- Keep secondary antibody Q&A rules separate from primary antibody Q&A rules because the keyword fields differ.
- Do not copy primary antibody Bioinformatics rules into secondary antibody product-series documents unless active secondary evidence exists.
- Add Playwright verification for search filters, sorting, Load More, compare selection limits, typeahead behavior, Q&A widget loading, related-products rendering, and product detail section navigation.
- Add Playwright verification for PDP package-size switching, commerce card price states, Add to Cart enablement, quantity bounds, Check Your Price links, banner close behavior, and estimated availability display.
- Add authenticated and anonymous commerce checks because price and availability behavior changes by login context.
- Add country-specific checks for US, CN, JP, and one country outside the new availability list to verify availability and dealer-display branches.
- Add current configuration rules when they affect behavior, including result count, keyword length, filter-enabled subtypes, typeahead-enabled subtypes, Q&A-enabled subtypes, related-products-enabled subtypes, badge enablement, and published-image limits.
- Recheck reference sorting on a secondary antibody product with nonzero references before documenting it as active behavior.
- Recheck the published-figure cap by comparing the displayed count, loaded gallery items, and configured image limits.
- Recheck FisherSci search-result pricing batch behavior against the active runtime bundle and configuration.
- Recheck PDP commerce pricing against the active pricing API and user entitlement responses.
- Add an example-specific evidence appendix outside the final business-rule documents for traceability.

## Recommended Rule Updates

- Do not include a Secondary Antibody Bioinformatics section in the business-rule document unless an active secondary Bioinformatics implementation is found.
- Add `Secondary antibody search result count is configured as 50 results for the secondary antibody subtype`.
- Add `Secondary antibody search keyword length is constrained by the configured keyword limit of 250 characters`.
- Add `Newer typeahead is not enabled for secondary antibody unless the secondary antibody subtype is included in the newer-typeahead subtype list`.
- Add `When a secondary antibody package has a banner message, the product page displays that banner message`.
- Add `When a secondary antibody package size is selected, the commerce card, availability check, data sheet selection, and banner message use the selected package`.
- Add `Add to Cart is available only when the selected secondary antibody package is orderable and the quantity is between 1 and 9,999`.
- Add `Estimated availability is displayed only when estimated availability is enabled, availability is enabled for the current context, the selected package is orderable, and the availability result requires an estimate`.
- Add `When a secondary antibody product has zero references, the product page displays References (0)`.
- Add `When a secondary antibody product has zero references, the product page asks users to report publications citing the product`.
- Add `When a secondary antibody product has zero references, the product page provides a Cite this product action`.
- Mark Reference sorting rules as requiring active secondary implementation confirmation.
- Mark published-figure cap behavior as requiring active implementation confirmation for secondary antibody PDPs.
