# Isotype Controls Business Rules Verification Report

## Scope

Verified on May 11, 2026 using:

- QA search example: `https://www.qa.thermofisher.com/antibody/control/query/*`
- QA product example: `https://www.qa.thermofisher.com/antibody/product/Mouse-IgG1-kappa-clone-P3-6-2-8-1-Isotype-Control/14-4714-82`
- Prompt: `/Users/aswathy.n/Downloads/business-rule-extraction-prompt-v3.md`
- Multi-repo evidence from `thermofisher/magellan-search`, `thermofisher/tfcom-magellan-qanda-service`, and `thermofisher/magellan-related-products`

## Verification Summary

The captured Isotype Controls rules are broadly correct and consistent with the QA pages and repository-level feature ownership. The most important correction versus a generic antibody ruleset is that Isotype Controls do have active Target Information and Bioinformatics sections on the sampled PDP, while References and Published Figures are zero for the sampled product.

## Confirmed Search Rules

- The search entry is configured as "Isotype Controls" and routes to `/antibody/control/query/{keyword}`.
- The Isotype Controls search route uses the control subtype context (`antibody_control` / `ANTIBODY_CONTROL`).
- QA configuration confirms 50 results per page for `antibody_control`.
- QA configuration confirms maximum keyword length of 250.
- New filters are enabled for `ANTIBODY_CONTROL`.
- New typeahead is not enabled for `ANTIBODY_CONTROL`; the configured list contains `ANTIBODY_PRIMARY` and `ELISA`.
- Related products and Q&A are enabled for `ANTIBODY_CONTROL`.
- Badges are disabled in the QA configuration (`enableBadges=false`).
- All-conjugate behavior is enabled for `ANTIBODY_CONTROL`.
- Price batching is configured with a maximum of 20 SKUs per pricing call.

## Confirmed Product Rules

- The sample PDP identifies the product as product category `Control`, product type `antibody`, product subtype `Isotype Control`, and widget subtype `antibody_control`.
- The selected product is `14-4714-82`, display name "Mouse IgG1 kappa Isotype Control (P3.6.2.8.1), eBioscience™".
- Product-order data includes package choices `14-4714-81` (50 µg), `14-4714-82` (100 µg), and `14-4714-85` (500 µg).
- Product-order data marks the sampled package as not discontinued and not long-term unavailable.
- Product-order data marks the sample package as not orderable in the downloaded QA context, so rules must not assume Add to Cart is always shown.
- Product Specifications are present and include Host/Isotype, Class, Type, Clone, Conjugate, Form, Concentration, Purification, Storage Buffer, Contains, Storage Conditions, Shipping Conditions, Amount, and RRID.
- Product Specific Information is present and includes Isotype Control use, reported applications, tested applications, same-concentration usage guidance, purity, aggregation, and filtration statements.
- Target Information is present for Mouse IgG1.
- Bioinformatics is present and shows Protein Aliases.
- The image gallery is present with Testing Data (34).
- References count is 0 and Published Figures count is 0.
- The References zero-state and "Cite this product" action are present.
- The Q&A widget bootstrap is present and passes product ID `14-4714-82`, product name "Mouse IgG1 kappa", and subtype `antibody_control`.
- The related-products module bootstrap is present and uses the v2 related-products widget URL.
- Product Schema JSON includes product name, no-image placeholder, brand Invitrogen, SKU `14-4714-82`, manufacturer Thermo Fisher Scientific, description, and selected non-empty properties.

## Areas To Improve

1. Add automated PDP checks for Isotype Controls that assert Target Information and Bioinformatics render when data exists.
2. Add a negative PDP test where an Isotype Control product has no Bioinformatics values, to confirm the section is hidden cleanly.
3. Add search-page tests proving new typeahead remains disabled for `ANTIBODY_CONTROL` unless the configuration is changed.
4. Add commerce-card tests for non-orderable Isotype Control packages, since the sampled product is not orderable in the downloaded QA context.
5. Add explicit tests for multi-package package switching on Isotype Controls, including SKU, data sheet, banner, price, and availability refresh.
6. Add Q&A service tests for control-product filters: application, host, clonality/class, conjugate, target class, format, recombinant status, and product subtype.
7. Add related-products tests that cover Isotype Control source-row ingestion, multi-value conjugate/isotype parsing, and empty-result UI suppression.
8. Add reference-section tests for both zero-reference and non-zero-reference Isotype Control products.
9. Add an accessibility check for the Testing Data gallery and View more / View less behavior in Bioinformatics.
10. Document which fields are authoritative for "Isotype Control" classification across search index, PDP model, Q&A service, and related-products ingestion to reduce future subtype drift.

## Residual Risks

- Live price and availability cannot be treated as fixed business rules because they come from runtime commerce APIs and user/country context.
- QA page configuration may differ from production configuration; production should be checked before signing off on country-specific commerce, Q&A, and availability behavior.
- Repository code search confirmed relevant ownership areas, but exact runtime service responses still require API or browser validation for full end-to-end proof.
