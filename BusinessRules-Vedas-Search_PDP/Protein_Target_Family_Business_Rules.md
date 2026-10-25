# Protein Target Family Business Rules

Generated from the Protein Target QA examples, deployed page state, deployed BDNA bundle behavior, and the provided business-rule extraction prompt.

Example pages:

- https://www.qa.thermofisher.com/tools/target/AKT1
- https://www.qa.thermofisher.com/tools/target/BRCA1

## 1. Page Scope and Routing

**PTF-BR-001 - Target page route**  
Protein Target Family pages are served from `/tools/target/{target}` where `{target}` is the requested gene/protein target symbol or keyword.

**PTF-BR-002 - Target normalization**  
The displayed target keyword is read from the route and any `*` characters are removed before the keyword is used in the page header and section titles.

**PTF-BR-003 - Product family classification**  
The target page is treated as the `genomic-portfolio` product family and uses product type `EBGPO` for page search-parameter state.

**PTF-BR-004 - Page metadata**  
The page title must follow `{TARGET} Antibodies, Proteins & Assays | Thermo Fisher Scientific`.

**PTF-BR-005 - Meta description**  
The page description must describe the target-specific collection of antibodies, proteins, ELISA kits, qPCR assays, bDNA assays, primers, and RNA products for detecting and analyzing the target gene and protein.

**PTF-BR-006 - Breadcrumb**  
The page breadcrumb must show `Home` followed by `{TARGET} protein / gene analysis`.

## 2. Header and Target Identity

**PTF-BR-007 - Header target symbol**  
The page header must show the requested target symbol prominently.

**PTF-BR-008 - Target subtitle**  
When a target-specific synonym or descriptive name is available, it should be displayed beside the target symbol. The synonym must be specific to the current target.

**PTF-BR-009 - Updated date**  
The page may show a content updated date. The date should represent the target-page content or data refresh date.

## 3. Category Cards

**PTF-BR-010 - Category-card source**  
The top category-card section is populated from the embedded unified results endpoint using the current target keyword and country context.

**PTF-BR-011 - Category-card validation**  
The category-card HTML is rendered only when it contains the expected unified-card structure and at least one card option block.

**PTF-BR-012 - Invalid category-card fallback**  
If the category-card HTML is missing or invalid after loading, the page redirects to `/search/results?query={TARGET}`.

**PTF-BR-013 - Category-card click behavior**  
Clicking a category-card block navigates to the first link in that card block unless the user directly clicked an internal link.

**PTF-BR-014 - Category-card analytics**  
Category-card clicks emit an analytics event using the normalized card label and card position, formatted as `TPP: {label} | {position}`.

**PTF-BR-015 - Category-card count display**  
Category cards display the product category label followed by the available product count in parentheses.

**PTF-BR-016 - Zero-count category-card behavior**  
Categories with zero available products are not displayed in the embedded category-card section.

**PTF-BR-017 - Category-card destination routes**  
Category cards route users to target-filtered product experiences, including:

- Antibodies: `/antibody/primary/target/{TARGET}`
- Recombinant proteins and peptides: `/proteins/target/{TARGET}`
- ELISA kits: `/elisa/target/{TARGET}`
- TaqMan assays and arrays: `/taqman/results?keyword={TARGET}`
- Branched DNA gene expression assays: `/bdna/gene-expression/primeflow/query/{TARGET}`
- PCR and Sanger sequencing primers: `/primers/pcr-sequencing-primers/query/{TARGET}`
- CRISPR guide RNA: `/crispr/invitrogen/query/{TARGET}`
- siRNA: `/order/rnai/siRNA/result?keyword={TARGET}`

## 4. Protein Details

**PTF-BR-018 - Protein Details source**  
Protein Details content is loaded from target XML data for the current target.

**PTF-BR-019 - Protein Details section visibility**  
The Protein Details area is hidden when target XML data is unavailable, loading, or produces no displayable tab content.

**PTF-BR-020 - Target XML parsing**  
The target XML parser recognizes overview, gene details, protein details, functions, epitope details, and Brightcove video IDs.

**PTF-BR-021 - Overview tab**  
When an overview is available, an `Overview` tab is shown with the overview text.

**PTF-BR-022 - Gene Details tab**  
When gene details are available, a `Gene Details` tab is shown. Supported labels include Official Symbol, Gene Name, Gene Aliases, Gene ID, Chromosome, Start Position, End Position, and Gene Summary.

**PTF-BR-023 - Protein Details tab fields**  
When protein details are available, a `Protein Details` tab is shown. Supported labels include Uniprot ID, Entry Name, Molecular Weight, Name, and Domain.

**PTF-BR-024 - Functions tab**  
When function details are available, a `Functions` tab is shown. XML field names are converted into readable labels.

**PTF-BR-025 - Empty field suppression**  
Empty target XML fields are not displayed in Protein Details tabs.

**PTF-BR-026 - Protein Details formatting**  
Protein Details tab rows display a bold option name followed by the field description.

## 5. Research Products

**PTF-BR-027 - Research Products source**  
The Research Products section is populated from the unified product-type count endpoint for the current target, country, and language.

**PTF-BR-028 - Research Products section title**  
The section title must be `{TARGET} Research Products`.

**PTF-BR-029 - Research Products category visibility**  
Research Products categories and options are shown only when their product count is greater than zero.

**PTF-BR-030 - Research Products ordering**  
Research Products categories are ordered using the lowest order value among their matching product details.

**PTF-BR-031 - Research Products tab categories**  
Research Products are grouped into these high-level categories when matching products exist:

- Gene Expression and Analysis
- Gene Editing and Silencing
- Proteins and Peptides
- Protein Detection Kits
- Antibodies

**PTF-BR-032 - Gene Expression and Analysis products**  
Gene Expression and Analysis can include target-specific TaqMan gene expression qPCR assays, TaqMan SNP genotyping qPCR assays, TaqMan copy number variation qPCR assays, PrimeFlow branched DNA assays, QuantiGene branched DNA assays, ViewRNA branched DNA assays, and CE/Sanger sequence detection primers.

**PTF-BR-033 - Gene Editing and Silencing products**  
Gene Editing and Silencing can include Silencer and/or Stealth siRNA and CRISPR guide RNA products.

**PTF-BR-034 - Proteins and Peptides products**  
Proteins and Peptides can include recombinant proteins and peptides, synthetic proteins and peptides, and native proteins and peptides when corresponding product counts are returned.

**PTF-BR-035 - Protein Detection Kits products**  
Protein Detection Kits can include matched pairs, coated ELISA kits, uncoated ELISA kits, and ProcartaPlex products when corresponding product counts are returned.

**PTF-BR-036 - Antibody products**  
Antibodies can include primary antibodies, monoclonal antibodies, polyclonal antibodies, and recombinant superclonal antibody products when corresponding product counts are returned.

**PTF-BR-037 - Product option naming**  
Research Product option names are prefixed with the current target symbol.

**PTF-BR-038 - Product option descriptions**  
Research Product descriptions are generated from category templates and replace `<target>` with the current target symbol.

**PTF-BR-039 - Product option links**  
Research Product option links use the route returned by the product-count data for the matching product category.

**PTF-BR-040 - Multiple options in genomics groups**  
Gene Expression and Analysis and Gene Editing and Silencing can render multiple options within a single tab when multiple matching product details have positive counts.

**PTF-BR-041 - Single section rule for non-genomics groups**  
Proteins and Peptides, Protein Detection Kits, and Antibodies render at most one section per high-level category even if multiple matching keys are present.

## 6. 3D Structure

**PTF-BR-042 - 3D viewer source fields**  
The 3D Structure component uses Uniprot ID, PDB ID, and antigen length parsed from target XML data.

**PTF-BR-043 - 3D viewer visibility**  
The 3D viewer is available only when Uniprot ID, PDB ID, and a positive antigen length are available.

**PTF-BR-044 - 3D viewer model retrieval**  
The 3D viewer retrieves model data through the AlphaFold API using the target Uniprot ID.

**PTF-BR-045 - 3D viewer enlarge behavior**  
When a 3D structure is available, the page provides an enlarge action that opens the structure in a modal viewer.

## 7. Learn More and Additional Resources

**PTF-BR-046 - Learn More source**  
The Learn More section is populated from keyword search Learn More results for the current target, country, and language.

**PTF-BR-047 - Learn More display limit**  
Although the Learn More request asks for three results, the page displays at most the first two Learn More results.

**PTF-BR-048 - Learn More empty-state behavior**  
The Learn More heading and cards are hidden when the Learn More API returns an error or no results.

**PTF-BR-049 - Learn More card fields**  
Each Learn More card uses title text, description, label, and title URL from the Learn More result.

**PTF-BR-050 - Additional Resources**  
The page displays an Additional Resources section with a `Documents & Support` item for the current target.

**PTF-BR-051 - Documents & Support route**  
The Documents & Support item routes to `/search/results?query={TARGET}&persona=DocSupport`.

## 8. Videos and External Links

**PTF-BR-052 - Brightcove video source**  
Target-specific video IDs are parsed from target XML `brightCoveIds`.

**PTF-BR-053 - Brightcove zero-value suppression**  
Brightcove video IDs with missing, nonnumeric, or zero values are ignored.

**PTF-BR-054 - Olink external link**  
The page includes an external link to the Olink Proteomics for Biomarker Analysis page.

## 9. Loading and Error Behavior

**PTF-BR-055 - Loading indicators**  
The page shows loading indicators while category cards, target data, product counts, or Learn More content are being fetched.

**PTF-BR-056 - Product-count error behavior**  
When product-count data returns an error, Research Products renders no product tabs.

**PTF-BR-057 - Target-data error behavior**  
When target XML fails to load, Protein Details and 3D Structure are hidden.

**PTF-BR-058 - Safe target encoding**  
Target keywords are URL-encoded before being sent to APIs or used in query-string routes.

## 10. Verified Example Outcomes

**PTF-BR-059 - AKT1 example product availability**  
For AKT1, the product-count API returned positive counts for Antibodies, Recombinant proteins and peptides, ELISA kits, TaqMan assays and arrays, Branched DNA gene expression assays, PCR and Sanger sequencing primers, CRISPR guide RNA, and siRNA.

**PTF-BR-060 - BRCA1 example product availability**  
For BRCA1, the product-count API returned positive counts for Antibodies, Recombinant proteins and peptides, TaqMan assays and arrays, Branched DNA gene expression assays, PCR and Sanger sequencing primers, CRISPR guide RNA, and siRNA. ELISA kits returned zero for this example and should not be displayed as an available product card.
