# TaqMan Mutation Detection dPCR Assay PDP Business Rules

## Document Control

| Field | Value |
|---|---|
| Product family | TaqMan Mutation Detection dPCR Assay PDP |
| Example URL supplied | `https://www.thermofisher.com/order/genome-database/details/DPCR/Hs000000035_rm?CID=&ICID=&subtype=` |
| Product evidence URL validated | `https://www.thermofisher.com/order/genome-database/details/dpcr/Hs000000035_rm?CID=&ICID=&subtype=` |
| Related content page validated | `https://www.thermofisher.com/in/en/home/life-science/pcr/real-time-pcr/real-time-pcr-assays/taqman-mutation-detection-assays.html` |
| Rule source | Deployed Thermo Fisher pages and downloaded page JavaScript; repository access was unavailable during validation |
| Generated date | 2026-05-22 |

## Scope

This document captures observed business rules for the TaqMan Mutation Detection digital PCR assay product detail experience for assay `Hs000000035_rm`, including assay identity, commerce card, genomic details, More Information, documentation, related products, categories and applications, specifications, View All Sizes, and Mutation Detection informational content.

## Route and Page Selection Rules

| Rule ID | Business Rule | Evidence |
|---|---|---|
| DPCR-PDP-001 | The uppercase `/details/DPCR/{assayId}` route redirects to a Mutation Detection informational page rather than rendering the old assay details PDP directly. | Supplied uppercase URL redirected to the AEM Mutation Detection page. |
| DPCR-PDP-002 | The lowercase `/details/dpcr/{assayId}` route renders the genome-database assay PDP for the same assay ID. | Lowercase URL returned the assay PDP for `Hs000000035_rm`. |
| DPCR-PDP-003 | The assay PDP stores the product type as `dpcr` for page data, commerce actions, and genomic-map initialization. | Page script sets `productType: 'dpcr'` and initializes the alignment map with `productType: 'DPCR'.toLowerCase()`. |
| DPCR-PDP-004 | The canonical schema-style dataset URL for this assay references the mutation-detection detail path. | Page metadata lists `www.thermofisher.com/order/genome-database/details/mutation-detection/Hs000000035_rm`. |

## Assay Identity and Header Rules

| Rule ID | Business Rule | Evidence |
|---|---|---|
| DPCR-PDP-005 | The PDP must display the assay as `DPCR assay Hs000000035_rm` in recently viewed or product-history context. | Recently viewed item title is `DPCR assay Hs000000035_rm`. |
| DPCR-PDP-006 | The product breadcrumb must place the assay under Digital PCR and end with the assay ID. | Breadcrumb contains Digital PCR and `Hs000000035_rm`. |
| DPCR-PDP-007 | The assay product metadata must identify the gene as `ERBB2`. | Product description and page data identify gene `ERBB2`. |
| DPCR-PDP-008 | The assay name must render as `ERBB2_14062`. | Product form add-to-cart payload and assay detail data use `ERBB2_14062`. |
| DPCR-PDP-009 | The transcript must render as `NM_004448.3`. | Assay details section includes transcript `NM_004448.3`. |
| DPCR-PDP-010 | The COSMIC ID must render as `14062` and link to the COSMIC mutation overview. | COSMIC ID field links to the Sanger COSMIC mutation overview for ID `14062`. |

## Assay Detail Rules

| Rule ID | Business Rule | Evidence |
|---|---|---|
| DPCR-PDP-011 | The nucleotide mutation must be shown as `c.2329G>T`. | Assay detail field displays `c.2329G>T`. |
| DPCR-PDP-012 | The amino acid change must be shown as `p.V777L`. | Assay detail field displays `p.V777L`. |
| DPCR-PDP-013 | The mutation genome location must be shown as chromosome 17 position `39724747` on build `GRCh38`. | Assay detail field displays `chr.17 39724747 on build GRCh38`. |
| DPCR-PDP-014 | The assay gene location must indicate that the assay overlaps intron 24 and exon 25. | Assay detail field displays `Overlaps Intron 24 - Exon 25`. |
| DPCR-PDP-015 | The context sequence must render the variant base pair as `[G/T]` and label the probe dyes as `[VIC/FAM]`. | Context sequence displays the `[G/T]` marker with `[VIC/FAM]`. |
| DPCR-PDP-016 | The gene symbol must link to a COSMIC gene overview when available. | `ERBB2` links to the COSMIC gene overview. |
| DPCR-PDP-017 | A gene-scoped navigation link must allow users to view other ERBB2 DPCR assays. | PDP renders a link to `/order/genome-database/DPCR/gene/ERBB2` with “See other ERBB2 DPCR Assay's”. |

## Commerce Card, Price, Availability, and Size Rules

| Rule ID | Business Rule | Evidence |
|---|---|---|
| DPCR-PDP-018 | The commerce card must display the assay ID `Hs000000035_rm`. | Product purchase table displays the assay ID. |
| DPCR-PDP-019 | The PDP must expose a single Standard size option for this assay: `S: 450 rxns`. | Hidden SKU select contains one selected Standard option with label `S: 450 rxns`. |
| DPCR-PDP-020 | The catalog number for the selected size must be `A44177`. | Selected option value and catalog row both show `A44177`. |
| DPCR-PDP-021 | Availability must render as `Made To Order` for the selected size. | Availability row displays `Made To Order`. |
| DPCR-PDP-022 | The base price row may be empty when online pricing is not directly available. | Price cell is present but empty in the captured PDP. |
| DPCR-PDP-023 | The Your Price row must remain hidden until pricing is retrieved or explicitly requested. | Your Price row uses hidden classes in the captured PDP. |
| DPCR-PDP-024 | The “Check your price” action must call the pricing handler with product type `DPCR` and pricing context `DPCR_rare_mutation`. | Link invokes `yourPriceLinkClicked(this,'DPCR','DPCR_rare_mutation',true)`. |
| DPCR-PDP-025 | Add to Cart must submit SKU `A44177`, assay ID `Hs000000035_rm`, name `ERBB2_14062`, quantity `1`, location `Full Assay Details`, selected size text, product type `dpcr`, and blank product subtype. | Add-to-cart handler payload includes those values. |
| DPCR-PDP-026 | Add to Cart controls may be hidden until commerce readiness conditions are satisfied. | Add-to-cart table row has a hidden class in the captured PDP. |

## Genomic Map Rules

| Rule ID | Business Rule | Evidence |
|---|---|---|
| DPCR-PDP-027 | The Genomic Map anchor is initially hidden and should only be shown when alignment-map initialization succeeds. | Page link is hidden and ready handler hides it when map readiness fails. |
| DPCR-PDP-028 | The alignment map must initialize for product `Hs000000035_rm`, product type `dpcr`, species Human taxonomy ID `9606`, and gene `ERBB2`. | AlignmentMap configuration contains those values. |
| DPCR-PDP-029 | The current assay must be registered as an available assay in the map. | `availableAssays` includes `Hs000000035_rm: true`. |
| DPCR-PDP-030 | Clicking a different assay entity in the map must open that assay details page in a new browser tab. | AlignmentMap click handler opens `/order/genome-database/details/{productType}/{entity.id}` when the selected entity is not the current assay. |

## More Information Rules

| Rule ID | Business Rule | Evidence |
|---|---|---|
| DPCR-PDP-031 | The More Information section must render Set Membership when available. | Section displays `Coding - Overlap Exon/Intron`. |
| DPCR-PDP-032 | Gene Ontology categories must be grouped into expandable/collapsible lists. | More Information renders toggle sections for Gene Ontology categories. |
| DPCR-PDP-033 | Gene Ontology terms must be shown as linked terms when a term URL is available. | Captured terms link to AmiGO or GO-term destinations. |
| DPCR-PDP-034 | Process/function category content must not be used as commerce eligibility; it is informational metadata. | Terms are rendered under More Information, not in purchase-card logic. |

## PDP Related Product Rules

| Rule ID | Business Rule | Evidence |
|---|---|---|
| DPCR-PDP-035 | The old assay PDP secondary rail must render a Related Products section when related product data exists. | PDP secondary section has heading `Related Products`. |
| DPCR-PDP-036 | Related product links must open in a new browser tab. | Related product anchors use `target="_blank"`. |
| DPCR-PDP-037 | The old assay PDP must include `TaqMan Digital PCR Chip Kit` as a related product for this assay. | Related Products section links to catalog product `A26316`. |
| DPCR-PDP-038 | The old assay PDP must include `TaqMan Digital PCR Master Mix` as a related product for this assay. | Related Products section links to catalog product `A26358`. |
| DPCR-PDP-039 | Related product clicks must trigger recommendation analytics before navigation. | Links call `recommendedClick(...)`. |
| DPCR-PDP-040 | Recommendation analytics must classify DPCR-related clicks as related products from a TaqMan assay product location when assay type is eligible. | Shared JavaScript sends `recommendationLocation: 'taqman assay product'` and `recommendationType: 'related products'`. |

## Mutation Detection Content Page Rules

| Rule ID | Business Rule | Evidence |
|---|---|---|
| DPCR-PDP-041 | The redirected Mutation Detection page must position the page as somatic mutation detection using TaqMan and castPCR technologies. | Page heading and content describe somatic mutation detection. |
| DPCR-PDP-042 | The page must describe higher specificity as blocking wild-type amplification and amplifying the mutant allele. | Specificity bullet describes blocking wild type and amplifying mutant target. |
| DPCR-PDP-043 | The page must describe higher sensitivity as detecting somatic mutations down to 1 cancer cell in 1,000 normal cells. | Sensitivity bullet states the 1-in-1,000 level. |
| DPCR-PDP-044 | The page must describe a faster workflow as approximately 3 hours from sample to result. | Workflow bullet states 3 hours from sample to result. |
| DPCR-PDP-045 | The page must state that hundreds of assays are available for known cancer research genes. | Content states 819 assays for 47 known cancer research genes. |
| DPCR-PDP-046 | The page must provide a workflow link for somatic mutation detection. | Page includes a link to learn more about the somatic mutation detection workflow. |
| DPCR-PDP-047 | The page must describe optional internal positive control usage through the TaqMan Mutation Detection IPC Reagent Kit. | “All formats and custom designed assays” section describes IPC reagent kit usage. |
| DPCR-PDP-048 | The page must describe custom plating availability for 96- or 384-well Fast or standard plates. | Content describes pre-plating through TaqMan Custom Plating Service. |
| DPCR-PDP-049 | The page must describe Mutation Detector Software as a data-analysis option for real-time PCR system output. | Content describes software determining mutation status from assay data. |

## Documentation Tab Rules

| Rule ID | Business Rule | Evidence |
|---|---|---|
| DPCR-PDP-050 | The Documentation tab must direct users to the TaqMan assay files location for assay documentation. | Documentation tab links to `/taqmanfiles`. |
| DPCR-PDP-051 | Documentation must include a TaqMan Mutation Detection Assays protocol. | Manuals and Protocols list includes the protocol PDF. |
| DPCR-PDP-052 | Documentation must include a TaqMan Mutation Detection Assays quick reference card. | Manuals and Protocols list includes the quick reference card PDF. |
| DPCR-PDP-053 | Documentation must include a Mutation Detector Software user guide. | Manuals and Protocols list includes the user guide PDF. |
| DPCR-PDP-054 | Documentation must include a Mutation Detector Software quick reference card. | Manuals and Protocols list includes the software quick reference PDF. |
| DPCR-PDP-055 | Documentation must include the TaqMan Mutation Detection Assay Index File. | Manuals and Protocols list includes the index file spreadsheet. |
| DPCR-PDP-056 | Product literature must include the product bulletin, mutation detection/quantitation application note, and cancer biomarker research poster. | Product Literature list contains those three assets. |

## Related Products, Categories, and Applications Tab Rules

| Rule ID | Business Rule | Evidence |
|---|---|---|
| DPCR-PDP-057 | The related applications subsection must include Mutation Detection With Real-Time PCR. | Related tab lists that application. |
| DPCR-PDP-058 | The related products subsection must include TaqMan Genotyping Master Mix. | Related tab links to catalog product `4371355`. |
| DPCR-PDP-059 | The related products subsection must include TaqMan Mutation Detection IPC Reagent Kit. | Related tab links to catalog product `4467538`. |
| DPCR-PDP-060 | The data analysis tools subsection must include Mutation Detector Software. | Related tab links to the Mutation Detector Software registration page. |

## Specifications Tab Rules

| Rule ID | Business Rule | Evidence |
|---|---|---|
| DPCR-PDP-061 | Specifications must describe castPCR discrimination as allele-specific TaqMan qPCR combined with an allele-specific MGB blocker. | Specifications tab describes this mechanism. |
| DPCR-PDP-062 | Mutant and wild-type allele assays must be described as 10X mixes containing unlabeled PCR primers, a FAM-labeled TaqMan MGB probe, and an MGB blocker. | Specifications tab lists those assay components. |
| DPCR-PDP-063 | Gene reference assays must be described as 10X mixes containing unlabeled PCR primers and a FAM-labeled TaqMan MGB probe. | Specifications tab lists those gene-reference components. |
| DPCR-PDP-064 | Reaction count must be stated as sufficient for 150 10 uL reactions in 384-well format or 75 20 uL reactions in 96-well format. | Specifications tab provides these reaction counts. |
| DPCR-PDP-065 | Expiration must be stated as 2 years from date of manufacture. | Specifications tab includes the expiration statement. |
| DPCR-PDP-066 | The assay information file must be described as containing sales order number, part number, assay ID, NCBI gene name, Entrez gene ID, Sanger COSMIC ID, nucleotide mutation, amino acid change, and mutation type. | Specifications tab lists these fields. |
| DPCR-PDP-067 | Documentation availability must include protocol, quick reference card, product insert, assay information files, shipment document, SDS, datasheet, and certificate of analysis. | Specifications tab lists those documentation types. |
| DPCR-PDP-068 | Tracking and identification must describe a 2D barcode on each assay tube and a 1D barcode on each rack. | Specifications tab includes those barcode rules. |
| DPCR-PDP-069 | Shipping and storage must state ambient-temperature shipping and storage at -15 degrees C to -25 degrees C. | Specifications tab includes shipping and storage guidance. |

## View All Sizes Rules

| Rule ID | Business Rule | Evidence |
|---|---|---|
| DPCR-PDP-070 | View All Sizes must render a tabular view with columns Catalog #, Product Name, and Availability. | Captured table has these columns. |
| DPCR-PDP-071 | Catalog `4465804` must be listed as TaqMan Mutation Detection Assays and availability Inventoried. | View All Sizes table includes this row. |
| DPCR-PDP-072 | Catalog `4465805` must be listed as TaqMan EGFR Exon 19 Deletions Assay and availability Inventoried. | View All Sizes table includes this row. |
| DPCR-PDP-073 | Catalog `4465807` must be listed as TaqMan Mutation Detection Reference Assays and availability Inventoried. | View All Sizes table includes this row. |
| DPCR-PDP-074 | Catalog `4467538` must be listed as TaqMan Mutation Detection IPC Reagent Kit and availability Inventoried. | View All Sizes table includes this row. |

## Research Use and Compliance Rule

| Rule ID | Business Rule | Evidence |
|---|---|---|
| DPCR-PDP-075 | The Mutation Detection content page must display the research-use-only notice: not for diagnostic procedures. | Page footer/content includes the research-use-only notice. |

## Source Access Limitation

The requested GitHub repository could not be accessed with the available credentials and `git ls-remote` also failed for the repository URL. These rules are therefore validated against deployed page behavior and downloaded page JavaScript, not against repository implementation source. Rules that depend on inaccessible backend services, production personalization, authentication, live pricing, or source-level conditions should be considered behaviorally validated but not source-confirmed.
