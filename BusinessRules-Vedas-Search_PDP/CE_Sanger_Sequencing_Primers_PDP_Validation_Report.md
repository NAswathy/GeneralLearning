# CE/Sanger Sequencing Primers PDP Validation Report

## Scope

This report validates the captured CE/Sanger sequencing primers PDP rules for the example page:

- https://www.thermofisher.com/order/genome-database/details/ceprimer/Hs00710994_CE?CID=&ICID=srch-uc-cesanger1&subtype=&pluginName=

Requested repository:

- https://github.com/thermofisher/magellan-search

## Validation Status

Repository validation could not be completed in this session.

- The GitHub connector returned an expired authentication-token error.
- `git ls-remote` reported the requested repository as unavailable from the current environment.
- Because repository content was inaccessible, the rules were validated against the deployed PDP HTML and deployed JavaScript bundle instead of source files.

This report should therefore be treated as deployed-behavior validation, not final source-code validation.

## Evidence Reviewed

1. The deployed CE primer PDP HTML for assay `Hs00710994_CE`.
2. The deployed `fullDetailsUnifiedJavaScript.js` asset used by the PDP.
3. The rendered purchase card fields for Assay ID, Purification, Size, Availability, Catalog number, Price, and Add To Cart.
4. The rendered Related Products section.
5. The deployed CE primer SKU-selection and cart-selection behavior in the shared JavaScript bundle.
6. The rendered genomic map initialization block for the CE primer PDP.

## Validation Findings

### Product Identity

Status: Validated against deployed PDP HTML.

The reviewed PDP identifies the product by Assay ID `Hs00710994_CE`. The page stores that assay ID for ordering and product-detail behavior. The deployed data identifies the product type as `ceprimer` and product subtype as `Primer`.

### Purification and Size

Status: Validated against deployed PDP HTML and JavaScript behavior.

The reviewed PDP displays Purification and Size controls. DS and HPLC were present as purification choices, with DS selected by default. The reviewed page included 25 nmol and 50 nmol size choices.

The deployed CE primer SKU behavior updates catalog number, availability, price area, and cart data when the user changes the selected configuration.

### Catalog Number and Availability

Status: Validated against deployed PDP HTML and JavaScript behavior.

The reviewed PDP defaulted to catalog number A15629 and displayed Made To Order availability. The shared CE primer logic maps non-inventoried configurations to Made To Order and inventoried configurations to Inventoried.

### Pricing

Status: Validated against deployed PDP HTML and JavaScript behavior.

The PDP includes a Price area and a Check your price link when account-specific pricing is not displayed. The CE primer pricing behavior retrieves pricing for the current catalog number. For primer-pair configurations, the deployed script supports comma-separated catalog numbers and comma-separated prices.

### Add To Cart

Status: Validated against deployed PDP HTML and JavaScript behavior.

The default Add To Cart action uses quantity 1 and submits selected catalog number, assay ID, size, product type, and product subtype. The shared CE primer logic supports single-SKU and two-SKU pair configurations. When two SKUs are selected, the button text changes to Add pair to cart and both SKUs are submitted.

### Assay Details and More Information

Status: Partially validated against deployed PDP HTML.

The page rendered Assay Details and More Information sections, and the page navigation included the Assay Details anchor. In the reviewed anonymous response, those sections did not contain populated detail fields. Source validation or authenticated-page validation is needed to determine whether that is expected for the assay.

### Genomic Map

Status: Validated against deployed PDP HTML and JavaScript behavior.

The PDP initializes genomic map behavior for product type CE primer, assay `Hs00710994_CE`, and Human species. The map section is hidden unless map readiness succeeds. If a user selects a different assay on the map, the PDP opens the other assay's details page.

### Related Products

Status: Validated against deployed PDP HTML and JavaScript behavior.

The reviewed PDP displayed five related products: POP-6 Polymer, POP-7 Polymer, BigDye Terminator v1.1 Cycle Sequencing Kit, BigDye Terminator v3.1 Cycle Sequencing Kit, and BigDye Direct Cycle Sequencing Kit. Each linked to a catalog product page and opened in a new tab or window.

The deployed click handler records recommendation position, recommendation type, and recommendation location for related-product clicks.

## Issues and Risks

1. Source repository access is blocked.

   The rule set cannot be signed off as repository-derived until GitHub access to `thermofisher/magellan-search` is restored.

2. The request referenced multi-repo extraction, but only one repository URL was provided.

   The multi-repo comparison workflow from the prompt could not be executed because there was no second accessible repository for the same behavior.

3. Assay Details content could not be fully validated.

   The reviewed anonymous PDP response rendered the Assay Details section without populated field rows. Authenticated behavior or source review may reveal additional fields such as sequence or assay-specific detail fields.

4. Primer-pair controls were only partially visible on the reviewed page.

   The deployed script supports pair-based behavior, but the reviewed PDP HTML clearly displayed Purification and Size controls only. Source review is needed to confirm exactly when pair controls are rendered.

5. Backend enforcement was not confirmed.

   The validation confirms deployed frontend and rendered-page behavior. It does not confirm backend source rules for assay lookup, package lookup, pricing lookup, availability, or related-product selection.

## Suggested Improvements

1. Restore GitHub access and repeat validation directly against `thermofisher/magellan-search`.
2. Add source-level traceability for each rule, including the source template, JavaScript behavior, and backend endpoint or service when applicable.
3. Confirm whether Assay Details should be empty for `Hs00710994_CE` or whether content depends on login, region, service response, or data availability.
4. Document the official CE primer configuration model, including purification, size, tailing, forward/reverse selection, and pair ordering.
5. Add regression tests for DS and HPLC selection to verify catalog number, size, availability, price, and cart payload updates.
6. Add regression tests for single-primer versus primer-pair add-to-cart behavior.
7. Add validation tests for related products to confirm expected product list, link targets, and click tracking position.
8. Add tests for the genomic map readiness behavior and alternate-assay click behavior.
9. Confirm whether the recently viewed label `HONEY assay` is the intended customer-facing naming for CE/Sanger primer PDPs.
10. Create a traceability matrix mapping PDP fields to data source, display rule, cart payload field, and downstream ordering impact.

## Final Assessment

The captured rules are consistent with the deployed CE/Sanger sequencing primer PDP and shared JavaScript behavior reviewed in this session.

Final sign-off should wait for restored repository access and source-code validation.
