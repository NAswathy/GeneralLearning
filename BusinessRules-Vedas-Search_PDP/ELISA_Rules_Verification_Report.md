# ELISA Business Rules Verification Report

## Scope

Verified on May 11, 2026 using:

- QA search example: `https://www.qa.thermofisher.com/elisa/query/*`
- QA product example: `https://www.qa.thermofisher.com/elisa/product/Human-IL-18-ProQuantum-Immunoassay-Kit/A35613`
- Prompt: `/Users/aswathy.n/Downloads/business-rule-extraction-prompt-v3.md`
- Multi-repo evidence from `thermofisher/magellan-search`, `thermofisher/tfcom-magellan-qanda-service`, and related-products repositories

## Verification Summary

The captured ELISA rules are consistent with the QA pages and repo/config evidence. ELISA differs from antibody product types in three important ways: it uses product type `immunoassay`, Q&A is not enabled for ELISA in the sampled configuration, and ELISA related-products behavior is controlled by an ELISA-specific flag even though the shared antibody related-products subtype list does not include ELISA.

## Confirmed Search Rules

- The search entry is configured as "ELISA Kits" and routes to `/elisa/query/{keyword}`.
- The search entry uses a typeahead URL with `productSubType=elisa`.
- The search entry activates on ELISA kit pages, ELISA product pages, ELISA query pages, ELISA target pages, immunoassay ELISA query pages, and immunoassay target pages.
- QA configuration confirms maximum keyword length of 250.
- The active search page model sets result count to 50.
- The broader QA configuration also contains `elisaPageSize=80`; this appears separate from the active page model for the sampled wildcard page.
- New filters are enabled for `ELISA`.
- New typeahead is enabled for `ELISA`.
- Spell check is enabled for `ELISA`.
- Q&A subtype configuration does not include `ELISA`.
- Metadata handling is enabled for `ELISA`.
- Image search is not enabled for `ELISA`.
- Promo ads, inline zero-result-product behavior, Solr re-query, and keep-my-filters behavior are enabled for `ELISA`.
- Search filters on the QA page include Protein Target, Species, Kit Format, Research Area, Sample Type, Instrument, High Sensitivity, and New.
- The sampled wildcard search shows 2,402 results.

## Confirmed Product Rules

- The sample PDP identifies product category as ELISA, product type as immunoassay, and product subtype as ELISA.
- The selected product is catalog `A35613`, display name "Human IL-18 ProQuantum Immunoassay Kit".
- Product-order data includes package choices `A35613` (96 Tests) and `A356135` (5 x 96 Tests).
- The sampled package is not discontinued and not long-term unavailable.
- The sampled package is not orderable in the downloaded QA context, so the rule set correctly avoids assuming Add to Cart is always shown.
- The sampled package includes a product-specific banner message linking to another ProQuantum immunoassay kit.
- Product Specifications include Analytical Sensitivity, Assay Range, Sample Type/Volume, Hands-On Time, Time-To-Result, Homogeneous/No-Wash Indicator, Instrument, Product Size, Contents, Shipping Conditions, Storage, Protein Name, Species Tested, Assay Kit Format, and Label or Dye.
- Product Description is present and describes ProQuantum IL-18 quantitation, proximity-based amplification, qPCR detection, small sample volume, 2-hour workflow, and ProQuantum analysis software.
- Target Information is present for IL-18.
- Bioinformatics is present and includes Gene Aliases, Gene ID, Gene Symbol, Protein Aliases, and UniProt ID.
- Image gallery/media includes video and Testing Data.
- References data is present with one reference record.
- Product Schema JSON includes product name, ELISA default image, brand Invitrogen, SKU `A35613`, manufacturer Thermo Fisher Scientific, description, and selected non-empty properties.
- No Q&A link or Q&A widget is present on the sampled PDP.
- Related-products bootstrap is present for product type `immunoassays`, product subtype `elisa`, product ID `A35613`, country `in`, and language `en`.
- A recommended product card is present for IL-6 Human Matched Antibody Pair.

## Areas To Improve

1. Add automated search tests that assert active ELISA page result count is 50 and clarify how `elisaPageSize=80` is intended to be used.
2. Add search filter tests for Protein Target, Species, Kit Format, Research Area, Sample Type, Instrument, High Sensitivity, and New.
3. Add PDP tests for ELISA banner messages, including package-switch behavior when a banner is present only on one package.
4. Add commerce-card tests for non-orderable ELISA packages, since the sampled product is not orderable in the downloaded QA context.
5. Add package-switching tests for SKU, package size, data sheet, banner, price, and availability refresh across `A35613` and `A356135`.
6. Add PDP tests that assert Target Information and Bioinformatics render when data exists and hide when data is absent.
7. Add reference-section tests for one-reference and zero-reference ELISA products.
8. Add media-gallery tests that cover video plus Testing Data on ELISA PDPs.
9. Add tests proving Q&A stays hidden for ELISA unless the Q&A enabled subtype list changes.
10. Document the split between shared related-products subtype configuration and ELISA-specific related-products enablement to reduce future configuration drift.

## Residual Risks

- Live price and availability cannot be treated as fixed business rules because they come from runtime commerce APIs and user/country context.
- QA page configuration may differ from production configuration; production should be checked before final sign-off on country-specific commerce, availability, Q&A, and related-products behavior.
- GitHub code search confirmed relevant ownership areas, but exact private file contents could not be downloaded directly through raw GitHub URLs in this environment. The final rules therefore rely on QA page runtime evidence plus GitHub connector search evidence for repository ownership and configuration areas.
