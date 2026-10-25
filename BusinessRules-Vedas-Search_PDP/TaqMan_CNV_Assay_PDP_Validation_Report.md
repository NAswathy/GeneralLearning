# TaqMan CNV Assay PDP Validation Report

## Scope

This report validates the captured TaqMan CNV assay PDP rules for the example page:

- https://www.thermofisher.com/order/genome-database/details/cnv/Hs00602382_cn?CID=&ICID=&subtype=

Repository context from the prior request:

- https://github.com/thermofisher/magellan-search

## Validation Status

Repository validation could not be completed in this session.

- The GitHub connector returned an expired authentication-token error.
- `git ls-remote` reported the requested repository as unavailable from the current environment.
- Because repository content was inaccessible, the rules were validated against the deployed PDP HTML and deployed JavaScript bundle instead of source files.

This report should therefore be treated as deployed-behavior validation, not final source-code validation.

## Evidence Reviewed

1. The deployed CNV PDP HTML for assay `Hs00602382_cn`.
2. The deployed `fullDetailsUnifiedJavaScript.js` asset used by the PDP.
3. The rendered product identity, gene summary, purchase card, Assay Details, More Information, Genomic Map initialization, and Related Products sections.
4. The shared PDP behavior for size selection, pricing, add-to-cart, related-product click tracking, and genomic map routing.

## Validation Findings

### Product Identity

Status: Validated against deployed PDP HTML.

The reviewed PDP identifies the product by Assay ID `Hs00602382_cn`. The page stores that assay ID for ordering and product-detail behavior. The deployed data identifies the product type as CNV and the product subtype as Functionally Tested.

### Gene and Assay Summary

Status: Validated against deployed PDP HTML.

The reviewed PDP displays Gene Symbol HIVEP3, assay reference genome location Chr.1:41583968 on build GRCh38, and cytoband 1p34.2. The PDP also provides a link to view other HIVEP3 CNV assays.

### Purchase Configuration

Status: Validated against deployed PDP HTML and JavaScript behavior.

The reviewed PDP displays a Size selector with S, M, and L configurations. These map to catalog numbers 4400291, 4400292, and 4400293 respectively. The default displayed catalog number is 4400291, and the default availability is Made To Order.

The shared PDP script supports updating the displayed catalog number, selected size, price, and cart payload when the selected size changes.

### Pricing

Status: Validated against deployed PDP HTML and JavaScript behavior.

The PDP includes a Price area and a Check your price link when account-specific pricing is not shown. Pricing behavior is tied to the selected catalog number.

### Add To Cart

Status: Validated against deployed PDP HTML and JavaScript behavior.

The Add To Cart action submits quantity 1, selected catalog number, assay ID, selected size, product type CNV, and product subtype Functionally Tested.

### Assay Details

Status: Validated against deployed PDP HTML.

The Assay Details section includes Target Gene Details. The reviewed page displays Entrez Gene ID, Gene Name, Gene Aliases, gene location, assay gene location, and a transcript table.

The transcript table displays Gene Symbol, Transcript Accession, Exon Location, Assay Transcript Location, and Protein ID. NCBI links are present for transcript accession and protein IDs when values exist. Blank protein IDs render as blank cells.

### Genomic Map

Status: Validated against deployed PDP HTML and JavaScript behavior.

The PDP initializes the genomic map with CNV product type, assay `Hs00602382_cn`, Human species, and gene HIVEP3. The map is shown only when map readiness succeeds. CNV map behavior is gene-based and uses the copy-number details route when opening a different assay from the map.

The shared map script also shows CNV-specific behavior for DGV display and pretested-assay marking.

### More Information

Status: Validated against deployed PDP HTML.

The reviewed PDP displays Set Membership values Intragenic, Exonic, and non-DGV Variation. The page also displays Gene Ontology Categories with expandable Function(s) and Process(es) links. Gene Ontology terms link to AmiGO records.

### Related Products

Status: Validated against deployed PDP HTML and JavaScript behavior.

The reviewed PDP displays six related products and links each to a catalog product page. The related-product click handler records catalog number, recommendation location, recommendation position, and recommendation type.

## Issues and Risks

1. Source repository access is blocked.

   The rule set cannot be signed off as repository-derived until GitHub access to `thermofisher/magellan-search` is restored.

2. The request referenced multi-repo extraction, but only one repository context was available from the prior request.

   The multi-repo comparison workflow from the prompt could not be executed because there was no second accessible repository for the same behavior.

3. Backend enforcement was not confirmed.

   The validation confirms deployed frontend and rendered-page behavior. It does not confirm backend source rules for assay lookup, package lookup, pricing lookup, availability, Assay Details, More Information, genomic map data, or related-product selection.

4. Gene Ontology labels should be reviewed.

   The reviewed More Information section displays Gene Ontology groups as Function(s) and Process(es). Source or product-owner validation should confirm that the displayed group labels align with the underlying terms.

5. Map behavior requires source-level traceability.

   The deployed script confirms CNV map routing, DGV control, and pretested-assay visual distinction. Source review is needed to confirm the exact data rules that determine DGV inclusion and pretested status.

## Suggested Improvements

1. Restore GitHub access and repeat validation directly against `thermofisher/magellan-search`.
2. Add source-level traceability for each rule, including the source template, JavaScript behavior, and backend endpoint or service when applicable.
3. Confirm the official CNV PDP data contract for Gene Symbol, reference genome location, cytoband, gene details, transcript rows, Set Membership, and Gene Ontology sections.
4. Add regression tests for S, M, and L size selection to verify catalog number, availability, price, and cart payload updates.
5. Add tests for Add To Cart payload fields: assay ID, catalog number, selected size, quantity, product type, and product subtype.
6. Add tests for the See other gene-specific CNV assays link.
7. Add tests for Assay Details rendering, including blank Protein ID behavior.
8. Add tests for More Information rendering and Gene Ontology toggle labels.
9. Add tests for genomic map readiness, hidden-map fallback, DGV toggle behavior, and alternate-assay routing.
10. Add tests for related products to confirm expected product list, link targets, and click tracking position.

## Final Assessment

The captured rules are consistent with the deployed TaqMan CNV assay PDP and shared JavaScript behavior reviewed in this session.

Final sign-off should wait for restored repository access and source-code validation.
