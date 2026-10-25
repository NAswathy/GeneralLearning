# TaqMan Assays and Arrays Validation Report

## Validation Summary

The TaqMan SNP Genotyping assay search rules were validated against the production example page, deployed TaqMan UI bundles, live product search-count payloads, live SNP search-result payloads, and the previously generated local TaqMan rule material. The rules are consistent with the deployed behavior for filters, result table columns, row actions, catalog/size/availability selection, add to cart, and compare.

The requested GitHub repositories could not be accessed, so this validation is deployed-behavior validation rather than full repository-source validation.

## Repository Access Status

- `https://github.com/thermofisher/tfcom-magellan-product-service`: not accessible. The GitHub connector returned an expired authentication-token error, and unauthenticated Git access returned Repository not found.
- `https://github.com/thermofisher/magellan-search-taqman-ui`: not accessible. The GitHub connector returned an expired authentication-token error, and unauthenticated Git access returned Repository not found.

Because of this blocker, backend source enforcement in `tfcom-magellan-product-service` and frontend source implementation in `magellan-search-taqman-ui` could not be directly reviewed.

## Evidence Reviewed

- Prompt: `/Users/aswathy.n/Downloads/business-rule-extraction-prompt-v3.md`
- Example page: `https://www.thermofisher.com/taqman/snp/assay/query?keyword=*`
- Deployed TaqMan main bundle: `/taqman/gene-expression/main.7646826942d6dc82.js`
- Deployed SNP search chunk: `/taqman/gene-expression/730.b98e0f13fa3a3ca7.js`
- Deployed compare chunk: `/taqman/gene-expression/204.df69cb362841d680.js`
- Live search-count API: `/api/magellan/product/productSearchCount`
- Live SNP search API: `/api/magellan/product/taqmanSearch`
- Local prior reference: `TaqMan_Assays_Search_Business_Rules.md`
- Local prior reference: `TaqMan_Assays_Rules_Verification_Report.md`

## Validation Results

### Search and Filters

- Validated that wildcard SNP search returns SNP Genotyping product-count coverage.
- Validated that the live SNP search payload returns five filters: Species, Attributes, Genes, SNP type, and Assay type.
- Validated Species values from the wildcard payload: Human and Mouse.
- Validated Attributes values from the wildcard payload: Allele frequency known and Inventoried.
- Validated SNP type values from the wildcard payload include Intragenic, Intergenic/unknown, Intron, UTR 5, and UTR 3.
- Validated Assay type values from the wildcard payload: Functionally tested, DME, Validated, and Qualified.
- Validated that filter values include counts, query values, navigator names, facet names, and checked state.

### Table Columns

- Validated that SNP result table headers are SNP ID, Gene, Assay ID, Allele, Dye/Size, Price, and selection.
- Validated sortable column keys:
  - SNP ID uses `snpID`.
  - Gene uses `SnpGene`.
  - Assay ID uses `SnpAssayID`.
  - Allele uses `allele`.
- Validated that Dye/Size is configuration behavior and not a sortable column in the header.
- Validated that Price is displayed through the price component and is not a sortable column in the header.

### Result Row

- Validated that the live payload returns fields used by the row, including product ID, assay ID, product type, product subtype, species, allele, SNP type, dye-size data, default dye, default size, default catalog number, and availability.
- Validated that SNP ID links to NCBI SNP using the product ID.
- Validated that Assay ID links to the genotyping details page using the assay ID.
- Validated that size options are sorted by reaction count.
- Validated that changing dye or size updates selected catalog number, selected size, selected availability, and saved-list item.
- Validated that copy-to-clipboard copies catalog number and Assay ID together.
- Validated the user-facing copy helper and copy success messages.
- Validated the discontinued-assay warning text.
- Validated the functionally tested assay message.

### Compare

- Validated that the compare panel appears when selected product count is greater than zero.
- Validated that the compare panel displays at most the first three selected products.
- Validated that compare is enabled only for two or three selected assay products.
- Validated that compare is disabled for fewer than two products and more than three products.
- Validated that SNP comparison sends assay IDs and product type SNP.
- Validated compare error behavior: the user is shown an error and asked to try again later.
- Validated compare panel actions: remove, compare, add to cart, download list, and email list.
- Validated list limits shown for all-selected states:
  - Download up to 1000 assays.
  - Email up to 4000 assays.
  - Up to 100 arrays.
- Validated the compare modal Product Information and Research Use Only notice.
- Validated SNP Product Information ordering evidence: assay ID, availability, gene symbol, location, assay type, polymorphism, and SNP type.

## Issues and Risks

- **Source verification blocked:** the requested repositories could not be accessed, so repository-level completeness cannot be claimed.
- **Typo in deployed page metadata:** the deployed bundle contains `TaqMan SNP Genotpying Assays` instead of `TaqMan SNP Genotyping Assays`.
- **Route parameter inconsistency:** the public route redirects SNP assay entry using `gt` query parameters, while the working search API payload uses SNP as the product type/subtype. This should be clarified in source and documentation.
- **Compare limit user experience:** selecting all loaded results can select more than three products, but Compare is disabled above three. The panel communicates the limit, but the selection action itself is not capped.
- **Assay and array compare behavior differs:** compare is available for two or three assays, while array comparison is disabled unless custom-array comparison is enabled. This difference should be documented in product taxonomy guidance.
- **Fisher Scientific behavior differs:** Search multiple targets is hidden in Fisher Scientific context, and add to cart uses Fisher Scientific cart payload rules. These market/channel differences should be source-verified once access is restored.

## Suggested Improvements

1. Refresh GitHub authentication and rerun the extraction directly against both requested repositories.
2. Confirm backend enforcement for SNP filter names, filter values, result payload fields, and compare/add-to-cart payloads in `tfcom-magellan-product-service`.
3. Confirm frontend implementation in `magellan-search-taqman-ui` against the deployed bundle evidence captured here.
4. Correct the deployed metadata typo from `Genotpying` to `Genotyping`.
5. Document the canonical mapping between SNP URL family, UI product type, API product type, and backend product code.
6. Add automated regression coverage for the five SNP filter groups.
7. Add automated regression coverage for the SNP table columns and sortable column keys.
8. Add automated regression coverage for compare enablement at zero, one, two, three, and four selected products.
9. Add automated regression coverage for selected dye/size changing catalog number, availability, price lookup, and saved-list item.
10. Clarify whether select all should remain allowed when it disables Compare, or whether selection should cap at three when the user’s intent is comparison.

## Final Assessment

The generated business rules are valid as deployed-page rules for the SNP Genotyping assay search and compare workflow. They should be treated as provisional until the two requested repositories are accessible and the rules are reconciled with source implementation.
