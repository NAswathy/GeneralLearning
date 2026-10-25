# TaqMan Assays Product Series Business Rules

## Business Rules

### Assay Product Commerce

- TaqMan assay product pages use the selected assay configuration to determine the catalog number, size, availability, price area, and add-to-cart action.
- A TaqMan assay product page must carry both the assay ID and the selected catalog number for ordering.
- The selected size determines the selected catalog number.
- The selected catalog number determines the availability shown to the user.
- Product pages show list price, your price, online offer, or check-price behavior according to available pricing data for the selected catalog number.
- Add to Cart uses the selected catalog number, assay ID, quantity, selected size, product type, and product subtype.
- TaqMan assay pages show "Made To Order" or "Inventoried" availability based on the selected assay configuration.
- Assay product pages may show Genomic Map, Assay Details, and More Information sections when those data sections are available.
- Assay product pages may show Related Products when related product data is available.

### Gene Expression And Microbe Detection Product Pages

- Gene Expression assay pages show gene symbol, gene name, gene aliases, chromosome location, species, species-specific ID when available, assay ID, best coverage, size options, selected availability, catalog number, and commerce actions.
- Gene Expression assay pages can represent Microbe Detection assays when the assay subtype is Microbe Detection.
- Microbe Detection assay pages use Gene Expression assay commerce rules for size, catalog number, availability, price, and add to cart.
- Gene Expression and Microbe Detection pages show updated mapping information when mapping data exists.
- Gene Expression and Microbe Detection pages show set membership when the assay belongs to a set such as Recommended Assay.
- Gene Expression and Microbe Detection pages show related products such as master mixes or cDNA synthesis kits when configured.

### SNP Genotyping Product Pages

- SNP Genotyping product pages show SNP ID, gene, gene name, set membership, chromosome location, polymorphism, context sequence, assay ID, size options, selected availability, catalog number, and commerce actions.
- SNP Genotyping size options can differ by reporter dye pair and reaction count.
- SNP Genotyping assay details may show species, dbSNP submissions, phenotype, PubMed literature links, allele nomenclature, and minor allele frequency.
- SNP Genotyping pages show set membership when available, such as HapMap.
- SNP Genotyping pages show related products such as TaqMan Genotyping Master Mix when configured.

### Copy Number Product Pages

- Copy Number product pages show links to other CNV assays for the same gene when available.
- Copy Number product pages show gene symbol, assay reference genome location, cytoband, assay ID, size options, selected availability, catalog number, and commerce actions.
- Copy Number assay details include Target Gene Details when available.
- Target Gene Details include Entrez Gene ID, gene name, gene aliases, genomic location, assay gene location, transcript accession, exon location, assay transcript location, and protein ID when those data values exist.
- Copy Number product pages include Target Copy Number Variation Details when variation data exists.
- Target Copy Number Variation Details include DGV version, target variation, location, CNV subtype, and genes when those data values exist.
- Copy Number product pages show Important Information when assay-specific ordering or interpretation guidance exists.
- Copy Number product pages show Additional Information, set membership, and Gene Ontology categories when those data values exist.
- Copy Number product pages show related products such as genotyping or PCR master mixes when configured.

### Advanced miRNA Product Pages

- Advanced miRNA product pages show assay name, stem-loop accession number, miRBase version, chromosome location, mature miRNA sequence, species, product type, assay ID, selected size, selected availability, catalog number, and commerce actions.
- Advanced miRNA product pages show a specificity-testing statement when anti-target specificity testing data exists.
- Advanced miRNA assay details show Gene Family ID and Mature miRNA Sequence when available.
- Advanced miRNA pages show miRBase details with species, miRBase ID, and miRBase accession number.
- Advanced miRNA pages show Stem-loop Details when stem-loop data exists.
- Advanced miRNA pages show related assay and reagent products when configured.

### Classic MicroRNA Product Pages

- Classic MicroRNA product pages show assay name, miRBase accession number, miRBase version, chromosome location, mature miRNA sequence, species, product type, assay ID, selected size, selected availability, catalog number, and commerce actions.
- Classic MicroRNA size options can include XS, S, M, and L options expressed as RT and PCR reaction counts.
- Classic MicroRNA assay details show Gene Family ID and Mature miRNA Sequence when available.
- Classic MicroRNA pages show Mature miRNA Details with species, miRBase ID, and miRBase accession number.
- Classic MicroRNA pages show Stem-loop Details when stem-loop data exists.
- Classic MicroRNA pages show related assay and reagent products when configured.

### Pri-miRNA Product Pages

- Pri-miRNA product pages show assay name, stem-loop ID, mapped miRBase version, chromosome location, stem-loop location, mature miRNA ID, species, product type, assay ID, selected size, selected availability, catalog number, and commerce actions.
- Pri-miRNA size options can include S, M, and L options with concentration and reaction-count details.
- Pri-miRNA assay details show amplicon length, chromosome location, species, miRBase details, and stem-loop details when available.
- Pri-miRNA pages show related assay and reagent products when configured.

### miRNA Array Catalog Product Pages

- miRNA Array catalog product pages use the catalog product commerce layout instead of the genome-database assay layout.
- miRNA Array catalog product pages show product title, catalog number, price, unit size, and add-to-cart action.
- miRNA Array catalog product pages show product description and product image when available.
- miRNA Array catalog product pages show Product Specifications when catalog specification data exists.
- Product Specifications can include sample type, shipping condition, supported equipment, detection method, content and storage, PCR method, product line, reaction speed, GC-rich PCR performance, product type, application, quantity, format, volume, and unit size.
- miRNA Array catalog product pages show Frequently Asked Questions when FAQ content exists.
- FAQ content can include minimum order quantities, instrument compatibility, and documentation-file guidance when those questions are configured for the product.

### Bioinformatics, Target Information, References, And Q&A

- Genomic Map is shown on assay product pages when map data is available.
- Target Gene Details are shown for Copy Number products when target gene data is available.
- miRBase Details are shown for MicroRNA products when miRBase data is available.
- Stem-loop Details are shown for MicroRNA products when stem-loop data is available.
- PubMed literature links are shown for SNP Genotyping products when literature-link data is available.
- Frequently Asked Questions are shown on catalog product pages when FAQ content is available.
