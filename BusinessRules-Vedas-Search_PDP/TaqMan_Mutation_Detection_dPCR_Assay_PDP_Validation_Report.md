# TaqMan Mutation Detection dPCR Assay PDP Validation Report

## Validation Summary

| Field | Value |
|---|---|
| Requested repository | `https://github.com/thermofisher/magellan-search` |
| Requested example URL | `https://www.thermofisher.com/order/genome-database/details/DPCR/Hs000000035_rm?CID=&ICID=&subtype=` |
| Lowercase PDP URL checked | `https://www.thermofisher.com/order/genome-database/details/dpcr/Hs000000035_rm?CID=&ICID=&subtype=` |
| Redirect destination checked | `https://www.thermofisher.com/in/en/home/life-science/pcr/real-time-pcr/real-time-pcr-assays/taqman-mutation-detection-assays.html` |
| Validation date | 2026-05-22 |
| Overall result | Partially validated against deployed pages; source-code validation blocked by repository access |

## Access and Evidence Review

The GitHub connector was unavailable because the configured authentication token had expired. Direct `git ls-remote` access to `https://github.com/thermofisher/magellan-search.git` also failed. Because source access was blocked, the generated business rules were validated against the deployed Thermo Fisher pages and downloaded page JavaScript.

The supplied uppercase route `/details/DPCR/Hs000000035_rm` redirected to the broader TaqMan Mutation Detection content page. The lowercase route `/details/dpcr/Hs000000035_rm` rendered the old genome-database assay PDP. This distinction is important: several requested sections, including Documentation, Specifications, Related products/categories/applications, and View All Sizes, are present on the redirected Mutation Detection content page, while assay-specific fields and commerce details are present on the lowercase assay PDP.

## Validation Findings

| Area | Result | Notes |
|---|---|---|
| Repository access | Not validated | GitHub token was expired and direct repository access failed. |
| Uppercase supplied URL | Validated with issue | The URL redirects to the Mutation Detection content page, not the assay PDP. |
| Lowercase assay PDP | Validated | The lowercase `dpcr` route renders the assay PDP for `Hs000000035_rm`. |
| Assay ID and gene details | Validated | PDP shows `Hs000000035_rm`, `ERBB2`, transcript `NM_004448.3`, assay name `ERBB2_14062`, and COSMIC ID `14062`. |
| Mutation fields | Validated | PDP shows nucleotide mutation `c.2329G>T`, amino acid change `p.V777L`, genomic location, assay gene location, and context sequence. |
| Commerce card | Validated | PDP shows Standard size `S: 450 rxns`, catalog `A44177`, availability `Made To Order`, and pricing link context `DPCR_rare_mutation`. |
| Add to Cart payload | Validated in markup | Handler payload uses SKU, assay ID, assay name, quantity, selected size, and product type `dpcr`. Live cart submission was not executed. |
| Genomic map | Validated in markup and JavaScript | Alignment map initializes for product `Hs000000035_rm`, product type `dpcr`, species Human, and gene `ERBB2`; visible behavior was not browser-tested. |
| More Information | Validated | Set Membership and Gene Ontology categories were present. |
| PDP related products | Validated | Old PDP lists TaqMan Digital PCR Chip Kit and TaqMan Digital PCR Master Mix. |
| Documentation tab | Validated | Redirected content page lists protocol, quick reference cards, software guide, index file, and product literature assets. |
| Related products/categories/applications tab | Validated | Redirected content page lists Mutation Detection With Real-Time PCR, TaqMan Genotyping Master Mix, TaqMan Mutation Detection IPC Reagent Kit, and Mutation Detector Software. |
| Specifications tab | Validated | Redirected content page includes discrimination, assay components, reaction counts, expiration, assay information file, documentation, barcode, shipping, and storage rules. |
| View All Sizes tab | Validated | Redirected content page lists catalog numbers `4465804`, `4465805`, `4465807`, and `4467538`. |
| Research-use notice | Validated | Redirected content page includes the research-use-only notice. |

## Rules Requiring Source Confirmation

| Rule Area | Why Source Confirmation Is Needed |
|---|---|
| Route normalization and redirect logic | The case-sensitive route difference should be confirmed in controller/router code. |
| Pricing and availability | The page markup shows current rendered values, but live pricing and availability can vary by region, authentication, entitlement, and service response. |
| Add to Cart visibility | Markup showed hidden add-to-cart controls; source or browser execution is needed to confirm all enabling conditions. |
| Genomic map readiness | JavaScript initialization was captured, but source and browser-level testing are needed to confirm map service behavior. |
| Related product eligibility | Rendered related products were captured, but the service/source rule that selects these products was not accessible. |
| Documentation and View All Sizes maintenance | The AEM content page was validated, but content-authoring source and ownership were not available. |

## Correctness Assessment

The generated rule set is correct for the observed deployed behavior. It separates assay-specific PDP rules from redirected Mutation Detection content-page rules so the document does not incorrectly claim that every requested section is present on the old assay PDP. The most important validation note is that the user's exact uppercase URL does not render the same experience as the lowercase assay PDP; this should be treated as a routing or canonicalization concern.

## Suggested Improvements

| Improvement | Rationale |
|---|---|
| Normalize `DPCR` and `dpcr` route handling | Users and internal links should not receive different experiences based only on route casing. |
| Add a canonical redirect rule for assay PDPs | The route should consistently land on either the assay PDP or an intentional content page, with canonical metadata aligned to the rendered page. |
| Add automated route tests for DPCR assay IDs | Tests should cover uppercase, lowercase, query-string, and canonical mutation-detection paths. |
| Add browser validation for commerce-card readiness | Verify when price, availability, Your Price, and Add to Cart controls become visible after JavaScript and service calls complete. |
| Add contract tests for related products | Confirm expected related-product recommendations for DPCR assays, including Digital PCR Chip Kit and Master Mix. |
| Clarify ownership between AEM content and genome-database PDP | Documentation, specifications, and View All Sizes appear on the AEM content page, while assay-specific commerce data appears on the genome-database PDP. |
| Improve source traceability in rules | Once repository access is restored, each rule should be tied to component, template, service, or data-source references. |
| Review copy label consistency | More Information category labels should be checked for accurate Function/Process grouping and user-facing wording. |

## Validation Limitation

This report does not claim repository-level verification. It validates rendered behavior and page JavaScript available from Thermo Fisher pages on 2026-05-22. A follow-up source-code review should be performed after GitHub access is restored.
