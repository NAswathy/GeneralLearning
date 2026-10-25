# TaqMan Assays Rules Verification Report

## Verification Summary

- The TaqMan Search rules were verified against the QA TaqMan search page, the deployed TaqMan UI bundle, live search-count and search-result payloads, and GitHub repository search evidence for the TaqMan UI/configuration repositories.
- The TaqMan Product Series rules were verified against the provided product examples for Microbe Detection/Gene Expression, SNP Genotyping, Copy Number, Advanced miRNA, Classic MicroRNA, Pri-miRNA, and miRNA Array catalog product pages.
- The captured rules are consistent with the examples reviewed. The main nuance is that Microbe Detection is counted as a separate search family, but the provided Microbe Detection product example is rendered under the Gene Expression product URL family.

## Evidence Reviewed

- Prompt file: `/Users/aswathy.n/Downloads/business-rule-extraction-prompt-v3.md`.
- GitHub repositories identified through the Thermo Fisher GitHub connector: `magellan-search-taqman-ui`, `magellan-search-taqman-ui-react`, `magellan-taqman-configurator`, and `magellan-search`.
- GitHub search evidence included TaqMan UI route, search service, product type selector, result row, analytics, store, and configurator assay-search files.
- Live QA/production example pages reviewed:
  - `https://www.qa.thermofisher.com/taqman/results?keyword=*`
  - `https://www.thermofisher.com/taqman-gene-expression/product/Ba07922347_s1?CID=&ICID=&subtype=`
  - `https://www.qa.thermofisher.com/order/genome-database/details/genotyping/C___1933671_10`
  - `https://www.qa.thermofisher.com/order/genome-database/details/cnv/Hs00010004_cn`
  - `https://www.qa.thermofisher.com/order/genome-database/details/microrna/478308_mir`
  - `https://www.qa.thermofisher.com/order/genome-database/details/microrna/477768_mat`
  - `https://www.qa.thermofisher.com/order/genome-database/details/microrna/Hs04350362_pri`
  - `https://www.qa.thermofisher.com/order/catalog/product/A31877?CID=&ICID=&subtype=`

## Correctness Checks

- The search-count payload confirms the five requested TaqMan families:
  - Gene Expression: `TAQMAN_GE`, `ARRAY_GX`
  - SNP Genotyping: `GT`
  - Copy Number: `CNV`
  - MicroRNA: `ADVANCED_MIRNA`, `MIRNA_CONTROL_ASSAY`, `PRI_MIRNA`, `ARRAY_MIRNA`
  - Microbe Detection: `MICROBE_DETECTION`, `ANTIBIOTIC_RESISTANCE`
- The deployed UI routing confirms subtype-specific search routes for Gene Expression Assays, Gene Expression Arrays, SNP Assays, SNP Custom Arrays, CNV Assays, Advanced miRNA Assays, Classic MicroRNA Assays, Pri-miRNA Assays, and miRNA Arrays.
- The deployed UI search service confirms the MicroRNA subtype normalization used by the search backend: `microrna_advanced` to `advanced_mirna`, `microrna_classic` to `classic_mirna`, `microrna_primary` to `pri_mirna`, and `microrna_array` to `mirna_arrays`.
- The search-result payloads confirm the captured filters:
  - Gene Expression: Species, Attributes, Genes, Assay type, Remove cross-reactivity
  - SNP Genotyping: Species, Attributes, Genes, SNP type, Assay type
  - Copy Number: Species, Attributes, Genes, Assay location
  - Advanced miRNA: Species compatible, Species assay design, Attributes
  - Classic MicroRNA: Species, Attributes
  - Pri-miRNA: Species
  - miRNA Arrays: Instrument, Species, Array format, Type
- The result-row bundles confirm the captured actions and limits: compare selection, add to cart, export/email toolbar use, three-item compare limit, price by selected catalog number, selected size changing catalog number and availability, related products, details, related arrays, and citations where data exists.
- The product examples confirm the captured product-page sections:
  - Gene Expression/Microbe Detection: commerce card, assay details, updated mapping information, set membership, and related products
  - SNP Genotyping: SNP metadata, allele data, PubMed literature links, minor allele frequency, set membership, and related products
  - Copy Number: target gene details, DGV variation details, important information, Gene Ontology categories, and related products
  - MicroRNA assays: miRBase details, mature miRNA sequence, stem-loop details, related assay products, and reagent related products
  - miRNA Array catalog product: catalog price, add to cart, specifications, and FAQ content

## Section-Specific Verification

- Product commerce card, price, and availability rules are supported for all provided product examples.
- Banner behavior near the product title was not consistently present as a distinct business banner in the reviewed examples. The catalog product shows "Have Questions?" near the commerce area, while the assay pages primarily show title metadata and commerce details.
- Product specifications are strongly present on the catalog product page. The genome-database assay pages expose assay-specific fields rather than a catalog-style specifications table.
- Bioinformatics-style sections are present as Genomic Map, Target Gene Details, miRBase Details, Stem-loop Details, DGV details, and Gene Ontology Categories, depending on subtype.
- Target information is strongest for Copy Number products and MicroRNA products; Gene Expression/Microbe and SNP products expose target or locus information in subtype-specific forms.
- References are present as PubMed literature links on the SNP product example. Citation behavior is also available in search result rows when citation data exists.
- Questions and Answers are present on the catalog product example as Frequently Asked Questions. They were not present on the reviewed genome-database assay detail pages.

## Areas For Improvement

- Create a canonical TaqMan taxonomy document that explicitly maps search families, backend product type codes, UI product types, URL families, and product-detail layouts.
- Clarify Microbe Detection handling because it is counted as its own search family but can appear as a Gene Expression assay subtype and product-detail URL.
- Standardize capitalization for availability values such as "Made To Order" and "Made to order" across search payloads, result rows, and product pages.
- Standardize label spelling in UI assets; one deployed label appears as "SNP Genotpying" instead of "SNP Genotyping."
- Add automated coverage that verifies each TaqMan search family returns the expected subtype filters and result-row fields.
- Add automated coverage that verifies each product subtype exposes its expected detail sections: commerce, specifications or assay details, related products, target/bioinformatics information, references, and FAQ/Q&A where applicable.
- Make Product Specifications behavior clearer for genome-database assay pages, since those pages expose assay details but not a catalog-style specifications table.
- Make Q&A behavior clearer by documenting that FAQ/Q&A is catalog-product content and is not consistently available on genome-database assay detail pages.
- Improve source traceability by linking each user-facing section to the owning repository/module and product-type code in internal documentation.
