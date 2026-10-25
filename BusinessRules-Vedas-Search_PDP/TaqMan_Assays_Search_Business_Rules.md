# TaqMan Assays Search Business Rules

## Business Rules

### Search Family Selection

- A blank search term is treated as a wildcard search.
- A wildcard search is allowed and returns broad TaqMan search coverage.
- Search terms may retain letters, numbers, spaces, hyphens, underscores, periods, commas, colons, semicolons, and parentheses. Other unsupported characters are removed before search is submitted.
- TaqMan search results are grouped into five assay families: Gene Expression, SNP Genotyping, Copy Number, MicroRNA, and Microbe Detection.
- Gene Expression counts include Gene Expression Assays and Gene Expression Arrays.
- SNP Genotyping counts include Genotyping Assays.
- Copy Number counts include Copy Number Assays.
- MicroRNA counts include Advanced miRNA Assays, Classic MicroRNA Assays, Pri-miRNA Assays, and miRNA Arrays.
- Microbe Detection counts include Microbe Detection assays and Antibiotic Resistance assays.
- If the selected family has no results for the searched term but another TaqMan family has results, the user is treated as being in the wrong application for that term.
- If the searched term is not found but suggested terms are returned, the user is shown suggested keyword behavior instead of normal results.
- If the searched term is not found and no suggestions are returned, the user is shown zero-results behavior.

### Search Result Actions

- Search result rows support product selection for comparison, add to cart, export, or email actions.
- A maximum of three selected products may be compared at one time.
- If a user attempts to select products beyond the compare limit, the page warns that only three items can be compared at a time.
- Selected assay configurations must carry both the catalog number and assay ID for ordering.
- When a user changes the size or dye-size configuration, the selected catalog number, selected size, and selected availability are updated to match that configuration.
- Availability is shown for the selected configuration, not only for the assay family.
- Price information is retrieved for the selected catalog number.
- If pricing cannot return an add-to-cart price, the result may display "View price in cart" or "Price not available."
- If a result is discontinued, the result identifies it as discontinued and explains that the assay may not function as expected in all samples.
- Discontinued assays remain orderable only when the user has verified performance in their experiments; otherwise the user is directed to search for a replacement or design a custom assay.

### Result Row Detail Sections

- A result row may show Citations only when citation data exists for that assay.
- A result row may show Related Arrays only when related-array data exists for that assay.
- A result row may show Details and Related Products when those sections are available for the assay subtype.
- Selecting Related Arrays from a qualifying miRNA result routes the user to the miRNA array search using the selected assay ID.
- Copy-to-clipboard behavior for assay rows copies the catalog number and assay ID together because both are required for ordering.
- Shared-list entries for TaqMan search results use the selected design ID, selected catalog number, product type, product subtype, quantity, and source as the saved business item.

### Gene Expression Assay Search

- Gene Expression Assay results include filters for Species, Attributes, Genes, Assay Type, and Remove Cross-Reactivity.
- Gene Expression Assay result rows expose the assay ID, gene symbol, species, assay subtype, amplicon length when available, selected catalog number, selected size, selected availability, and dye-size options.
- Gene Expression Assay result rows support multiple dye configurations when available, including FAM-MGB and other supported reporter configurations.
- Gene Expression Assay result rows default to the catalog number, size, and availability provided by the result payload.
- Gene Expression Assay results may identify Recommended Products, Related Products, Citations, Details, or Related Arrays when the required backing data exists.
- Microbe Detection and Antibiotic Resistance assays can appear within Gene Expression assay results when the matching keyword belongs to those assay subtypes.

### SNP Genotyping Assay Search

- SNP Genotyping search uses Genotyping Assay result behavior.
- SNP Genotyping results include filters for Species, Attributes, Genes, SNP Type, and Assay Type.
- SNP Genotyping result rows expose the assay or SNP identifier, species, gene when available, allele, allele-frequency availability, selected catalog number, selected size, selected availability, and dye-size options.
- SNP Genotyping result rows support assay-map details and gene details when available.
- SNP Genotyping result rows can expose Related Products, Citations, and Details when available.

### Copy Number Assay Search

- Copy Number search uses Copy Number Assay result behavior.
- Copy Number results include filters for Species, Attributes, Genes, and Assay Location.
- Copy Number result rows expose the assay ID, gene symbol when available, species, assay location, cytoband, target variation IDs, amplicon length, selected catalog number, selected size, selected availability, and size options.
- Copy Number result rows support CNV Details, Gene Details, Related Products, Citations, and Details when available.
- Copy Number result rows include required non-assay package information for human CNV ordering when that package data is returned with the results.

### MicroRNA Search

- MicroRNA search is split into Advanced miRNA Assays, Classic MicroRNA Assays, Pri-miRNA Assays, and miRNA Arrays.
- Advanced miRNA results include filters for Species Compatible, Species Assay Design, and Attributes.
- Advanced miRNA result rows expose assay ID, assay name, product type, species assay design, selected catalog number, selected size, selected availability, and related-array eligibility.
- Classic MicroRNA results include filters for Species and Attributes.
- Classic MicroRNA result rows expose assay ID, assay name, product type, species, selected catalog number, selected size, selected availability, and RT/PCR reaction-size options.
- Pri-miRNA results include a Species filter.
- Pri-miRNA result rows expose assay ID, assay name, product type, species assay design, selected catalog number, selected size, selected availability, and concentration/reaction-size options.
- miRNA Array results include filters for Instrument, Species, Array Format, and Type.
- miRNA Array result rows expose the product ID, product name, product format, species, samples per plate, selected catalog number, and availability.

### Microbe Detection Search

- Microbe Detection is counted as a separate TaqMan assay family.
- Microbe Detection and Antibiotic Resistance are distinct subtypes within the Microbe Detection family count.
- Microbe Detection assay result rows use Gene Expression assay ordering behavior, including assay ID, dye-size options, selected catalog number, selected availability, and add-to-cart behavior.
- Microbe Detection assay examples can appear on Gene Expression product-detail URLs even when the assay subtype is Microbe Detection.
