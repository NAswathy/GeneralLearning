# Proteins & Peptides Business Rules Verification Report

## Scope

Verified on May 11, 2026 using:

- QA search example: `https://www.qa.thermofisher.com/proteins/query/*`
- QA product example: `https://www.qa.thermofisher.com/proteins/product/Human-FGF-basic-FGF-2-bFGF-154-aa-Recombinant-Protein/100-18B-50UG`
- Prompt: `/Users/aswathy.n/Downloads/business-rule-extraction-prompt-v3.md`
- Multi-repo evidence from `thermofisher/magellan-search`, `thermofisher/tfcom-magellan-qanda-service`, and `thermofisher/magellan-related-products`

## Verification Summary

The captured Proteins & Peptides rules are consistent with the QA pages and repo/config evidence. The largest difference from Primary/Secondary/Isotype antibody pages is that Proteins & Peptides uses the `antibody_protein` subtype, has active Bioinformatics and Target Information, has a large References section, but does not expose Questions & Answers in the sampled QA PDP because Q&A subtype configuration excludes `ANTIBODY_PROTEIN`.

## Confirmed Search Rules

- The search entry is configured as "Proteins & Peptides" and routes to `/proteins/query/{keyword}`.
- The search entry has a configured product-area typeahead URL for PRANT-filtered protein/peptide suggestions.
- The search entry activates on proteins paths and protein query paths for recombinant protein, synthetic peptide, and native protein.
- QA configuration confirms `proteinPageSize = 100`.
- QA configuration confirms maximum keyword length of 250.
- New filters are enabled for `ANTIBODY_PROTEIN`.
- New typeahead is not enabled for `ANTIBODY_PROTEIN`; the configured list contains `ANTIBODY_PRIMARY` and `ELISA`.
- Spell check is not enabled for `ANTIBODY_PROTEIN`; the configured list contains primary, secondary, control, and ELISA.
- Q&A and related-products subtype lists do not include `ANTIBODY_PROTEIN`.
- Metadata handling is enabled for `ANTIBODY_PROTEIN`.
- Image search is not enabled for `ANTIBODY_PROTEIN`.
- Promo ads, inline zero-result-product behavior, Solr re-query, and keep-my-filters behavior are enabled for `ANTIBODY_PROTEIN`.
- Search filters on the QA page include Protein Name, Species, Expression System, Product Type, Application, Product Grade, Tag, New, Activity, and Promotion.

## Confirmed Product Rules

- The sample PDP identifies product category as Protein, product type as antibody, display subtype as Protein, and downstream subtype as `antibody_protein`.
- The selected product is catalog `100-18B-50UG`, display name "Human FGF-basic (FGF-2/bFGF) (154 aa) Recombinant Protein, PeproTech®".
- Product-order data includes package choices `100-18B-10UG`, `100-18B-50UG`, `100-18B-100UG`, `100-18B-250UG`, `100-18B-500UG`, and `100-18B-1MG`.
- The sampled package is not discontinued and not long-term unavailable.
- The sampled package is not orderable in the downloaded QA context, so the rule set correctly avoids assuming Add to Cart is always shown.
- Product Details include applications, tested dilution values, and publication counts.
- Product Specifications include Species, Published Species, Expression System, Amino Acid Sequence, Molecular Weight, Class, Type, Purity, Endotoxin Concentration, Activity, Conjugate, Form, Purification, Contains, Storage Conditions, Shipping Conditions, and Amount.
- Product Specific Information is present and includes protein size, amino acid residue count, stem-cell qualification, shipping temperature, and Certificate of Analysis guidance.
- Target Information is present for FGF2 / FGF-basic.
- Bioinformatics is present and includes Protein Aliases, Gene Aliases, UniProt ID, and Entrez Gene ID.
- Image gallery is present with Testing Data (1).
- References count is 1,694 and Published Figures count is 0.
- The References component passes subtype "Protein" and default display-card limit 3.
- Product Schema JSON includes product name, no-image placeholder, brand Gibco, SKU `100-18B-50UG`, manufacturer Thermo Fisher Scientific, description, and selected non-empty properties.
- Scholarly article structured data is present for many reference records and is enabled by configuration for `ANTIBODY_PROTEIN`.
- No Q&A link or Q&A widget is present on the sampled PDP.

## Areas To Improve

1. Add automated PDP tests that assert Proteins & Peptides Bioinformatics renders Protein Aliases, Gene Aliases, UniProt ID, and Entrez Gene ID when present.
2. Add a negative PDP test where a protein product has no bioinformatics values, to confirm the section is hidden cleanly.
3. Add automated tests for References count, application-specific reference links, default display-card limit, and zero-published-figures behavior.
4. Add tests proving Q&A stays hidden for `ANTIBODY_PROTEIN` unless the Q&A enabled subtype list changes.
5. Add search tests for the Proteins & Peptides typeahead URL and the separate "new typeahead not enabled" condition.
6. Add search filter tests for Protein Name, Species, Expression System, Product Type, Application, Product Grade, Tag, New, Activity, and Promotion counts.
7. Add commerce-card tests for non-orderable protein packages, since the sampled product is not orderable in the downloaded QA context.
8. Add package-switching tests for SKU, package size, data sheet, banner, price, and availability refresh across the six sample package sizes.
9. Add structured-data validation tests for Product schema and ScholarlyArticle schema on protein PDPs.
10. Document the difference between display subtype "Protein" and downstream subtype `antibody_protein` so future Q&A, related-products, and search-filter changes do not drift.

## Residual Risks

- Live price and availability cannot be treated as fixed business rules because they come from runtime commerce APIs and user/country context.
- QA page configuration may differ from production configuration; production should be checked before final sign-off on country-specific commerce, availability, Q&A, and related-products behavior.
- GitHub code search confirmed relevant ownership areas, but exact private file contents could not be downloaded directly through raw GitHub URLs in this environment. The final rules therefore rely on QA page runtime evidence plus GitHub connector search evidence for repository ownership and configuration areas.
