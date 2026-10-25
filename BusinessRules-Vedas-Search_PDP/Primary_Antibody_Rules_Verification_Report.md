# Primary Antibody Rules Verification Report

## Verification Scope

- Search example reviewed: `https://www.qa.thermofisher.com/antibody/primary/query/*`
- Product example reviewed: `https://www.qa.thermofisher.com/antibody/product/ACE2-Antibody-clone-SN0754-Recombinant-Monoclonal/MA5-32307`
- Both QA URLs returned page content on May 11, 2026.
- Verification used the QA page HTML, page configuration values, and the repository evidence used to create the business-rule documents.

## Overall Assessment

- The rule sets are directionally correct and many rules are supported by the QA examples.
- The product page strongly confirms the product detail, product specifications, Bioinformatics, image/publication counts, References, Questions & Answers, target-information content, product order model, and commerce configuration areas.
- The search page confirms the primary antibody result context, wildcard query behavior, result count display, filter availability, compare module availability, and configuration for primary antibody filters, typeahead, result count, keyword length, Q&A, related products, and badge enablement.
- Some rules should be tightened because they are supported by repository logic but were not directly verifiable from the static QA examples.
- A few rules should be revised or marked as conditional because the live QA configuration suggests newer behavior or disabled behavior.

## Search Page Verification

### Confirmed On The QA Search Page

- The page is a primary antibody search page for the wildcard keyword.
- The page title and metadata identify the result set as Primary Antibodies.
- The page displays a large result count for the wildcard query.
- The page metadata displays 232,180 Primary Antibodies for the wildcard page.
- Primary antibody is configured as a supported subtype for the newer filter experience.
- Primary antibody is configured as a supported subtype for newer typeahead.
- The page configuration sets primary antibody result count to 50.
- The page configuration sets the maximum antibody search keyword length to 250.
- The page configuration includes primary antibody in Q&A-enabled product subtypes.
- The page configuration includes primary antibody in related-products-enabled product subtypes.
- The page configuration has product badges disabled.
- The page configuration sets `maxSKUsInPricingCall` to 20.
- The compare panel is enabled on the page.
- The page includes product result and filter data for the primary antibody result set.
- The page configuration includes primary antibody result count configuration.

### Supported By Repository Logic, Not Fully Proven By Static Page HTML

- Typeahead returns up to 15 suggestions.
- Duplicate typeahead suggestion values are shown only once.
- The registered-trademark marker is removed from selected typeahead values.
- Search button enablement depends on the search input having a value.
- Selecting a recent search submits the search.
- Filters reset the result offset to the first page.
- Sorting resets the result offset to the first page.
- Load More appends additional rows.
- Compare supports up to three selected products and enables the Compare button only after at least two products are selected.

### Search Rules Needing Review Or Rewording

- The FisherSci pricing batch rule should be configuration-based rather than fixed at 25 SKUs. The QA page configuration contains `maxSKUsInPricingCall` set to 20.
- The badge rules are implemented in legacy search JavaScript, but the QA page configuration has `enableBadges` set to false. Badge rules should remain conditional and should not be described as always active on the QA search page.
- Primary search price and availability values on search result cards still need browser execution or API-level checks to confirm the final displayed values for selected package sizes.

## Product Page Verification

### Confirmed On The QA Product Page

- The example product is the ACE2 Recombinant Rabbit Monoclonal Antibody, catalog number MA5-32307.
- The page identifies the product as an Invitrogen primary antibody product.
- The page title identifies the product as ACE2 Recombinant Rabbit Monoclonal Antibody (SN0754), Invitrogen, catalog number MA5-32307.
- The product order model uses product type antibody and product subtype antibody_primary.
- The product order model includes one package option: MA5-32307 for 100 µL.
- The product order model uses MA532307 as the web ID.
- The product package is not marked long-term unavailable.
- The product package is not marked discontinued.
- The product order model does not include a package banner message for this example.
- The page configuration has banner messages enabled.
- The page configuration has dynamic price enabled.
- The page configuration enables the new pricing API for antibody products.
- The page configuration enables the new availability API.
- The page configuration enables estimated availability.
- The page configuration enables the OAuth2 availability API.
- The page configuration enables shipping-condition display.
- The page shows 41 References and 30 Published Figures.
- The Product Details section displays tested applications, product specifications, product-specific information, and target information.
- Product specifications include species reactivity, published species, host/isotype, expression system, class, type, clone, immunogen, conjugate, form, concentration, amount, purification, storage buffer, contents, storage conditions, shipping conditions, and RRID.
- The Bioinformatics section is present.
- Bioinformatics displays Protein Aliases, Gene Aliases, UniProt ID, Entrez Gene ID, Function(s), and Process(es).
- Bioinformatics long-value groups include View more and View less controls.
- Questions & Answers is present as a product-page section/action.
- The page exposes the Q&A widget endpoint configuration.
- The page exposes related-products module configuration and primary antibody as a related-products-enabled subtype.
- The page exposes the maximum published-image value of 40.
- The page exposes citation/reference data that includes titles, authors, journals, published dates, species, and dilution mappings.
- The page contains a Disclaimer element.

### Supported By Repository Logic, Not Fully Proven By Static Page HTML

- Product banners are shown when a package is long-term unavailable, discontinued, or has a banner message.
- The generic banner message updates when the selected package changes.
- Long-term-unavailable and discontinued banners use different user-facing messages and Technical Support paths.
- Single-package commerce cards use the first package SKU.
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
- BenchSci reference cards display images and published figures with a BenchSci icon.
- Non-BenchSci reference cards display species, dilution, description, and authors.
- Reference sorting by Species, Dilution, Title, Authors, Journal, and Most Recent.
- Related-product matching and ranking rules for secondary antibodies, isotype controls, related primary antibodies, ELISA kits, and matched antibody pairs.
- Q&A matching by exact SKU and product keyword filters.
- Q&A sorting by answer count, vote count, and submitted date.
- Q&A error behavior returning zero counts or empty result sets.

### Product Rules Needing Review Or Rewording

- The rule saying Bioinformatics displays molecular function should be revised. The QA product page label is Function(s), while the earlier feature evidence used Molecular Function. The safer business wording is: Bioinformatics displays Function(s) and Process(es).
- The generated Target Information section focuses mostly on target family pages. The QA product example also has Target Information inside Product Details. Add a separate rule for product-page Target Information.
- The QA page static HTML confirms the product order model and commerce configuration, but live commerce price and availability values require browser execution and commerce API responses.
- The product order model marks MA5-32307 as not orderable before dynamic pricing is applied; the final Add to Cart state should be verified after pricing resolves in the browser.
- The product page exposes lead-time fields for EU and CN package data, but the reviewed evidence did not confirm a visible primary PDP lead-time rule for this example.
- The References sort rules should be revalidated. The QA page configuration includes `referenceSortByFilterRemoved:true`, and the older reference-sort feature file was tagged ignored. These sort rules should not be treated as confirmed for the current QA product page unless active implementation evidence is reviewed.
- The no-image placeholder rule is not confirmed by the ACE2 example. The page schema contains a no-image URL, but the product also has antibody testing data and published figures. Keep the no-image rule only as repository-supported behavior, not as verified by this specific example.
- The related-product rules are supported by the related-products repository logic and page configuration, but the static product HTML does not prove the recommendation ordering or eligibility outcomes for this specific product.

## Suggested Improvements

- Add a verification status to each generated rule during extraction: Confirmed on QA page, Supported by repository logic, Configuration-supported, Requires interaction test, or Needs recheck.
- Separate active QA behavior from legacy or ignored test behavior. Rules from ignored feature files should be kept only when live code or page output confirms the behavior.
- Add a small evidence appendix outside the final business-rule document that lists the exact page, repository, or configuration source used for each rule.
- Add Playwright-based verification for interactive rules such as filter selection, sort changes, Load More, compare selection limits, Q&A widget loading, reference expansion, and related-product rendering.
- Add Playwright verification for PDP package-size switching, commerce card price states, Add to Cart enablement, quantity bounds, Check Your Price links, banner close behavior, and estimated availability display.
- Add authenticated and anonymous commerce checks because price and availability behavior changes by login context.
- Add country-specific checks for US, CN, JP, and one country outside the new availability list to verify availability and dealer-display branches.
- Add current-page configuration rules where they affect behavior, including primary antibody result count, keyword length, enabled typeahead subtypes, enabled filter subtypes, Q&A-enabled subtypes/countries, related-products-enabled subtypes, and published-image cap.
- Revise labels in the product rule document to match current UI labels: Function(s), Process(es), Questions & Answers, Published Figures, Product Specifications, and Target Information.
- Split Product Series rules into page-level groups: Search result product card rules, PDP product details rules, PDP Bioinformatics rules, PDP References rules, PDP Q&A rules, PDP Related Products rules, and Target Family Page rules.
- Recheck FisherSci search-result pricing batch behavior against the active QA bundle and configuration.
- Recheck PDP commerce pricing against the active pricing API and user entitlement responses.
- Recheck Reference sorting before keeping those rules as current behavior because the QA product page indicates the reference sort filter may be removed.
- Add example-specific validation notes for MA5-32307, including 41 references, 30 published figures, ACE2 target information, and visible Bioinformatics fields.

## Recommended Rule Updates

- Replace `Primary antibody Bioinformatics displays molecular function` with `Primary antibody Bioinformatics displays Function(s)`.
- Replace `Primary antibody Bioinformatics displays processes` with `Primary antibody Bioinformatics displays Process(es)`.
- Add `Primary antibody product detail pages display Target Information in Product Details when target information is available`.
- Add `Primary antibody wildcard search displays a primary antibody result count for the wildcard keyword`.
- Add `Primary antibody search uses the configured primary antibody result count when determining result-page size`.
- Add `Primary antibody newer typeahead is enabled only when the primary antibody subtype is included in the configured newer typeahead subtype list`.
- Add `Primary antibody search keyword length is constrained by the configured keyword limit`.
- Add `When a primary antibody package has a banner message, the product page displays that banner message`.
- Add `When a primary antibody package size is selected, the commerce card, availability check, data sheet selection, and banner message use the selected package`.
- Add `Add to Cart is available only when the selected primary antibody package is orderable and the quantity is between 1 and 9,999`.
- Add `Estimated availability is displayed only when estimated availability is enabled, availability is enabled for the current context, the selected package is orderable, and the availability result requires an estimate`.
- Mark Reference sorting rules as requiring current implementation confirmation before treating them as active QA behavior.
- Mark live PDP price and availability values as requiring browser/API confirmation.
