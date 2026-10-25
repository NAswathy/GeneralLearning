# TaqMan CNV Assay PDP Business Rules

## Business Rules

### Product Identity

1. A TaqMan CNV assay PDP is identified by an Assay ID.
2. The Assay ID is displayed in the purchase card.
3. The displayed Assay ID is retained as the assay identifier used for ordering.
4. The reviewed PDP is for assay `Hs00602382_cn`.
5. The reviewed PDP classifies the product type as CNV.
6. The reviewed PDP classifies the product subtype as Functionally Tested.
7. The CNV product family is mapped to copy-number details pages.
8. The product is added to recently viewed items when recently viewed tracking is available.
9. The recently viewed entry uses the assay ID as the product identifier.
10. The recently viewed entry labels the product as a CNV assay.

### Gene and Assay Summary

1. The PDP displays Gene Symbol for the CNV assay.
2. The reviewed PDP displays Gene Symbol as HIVEP3.
3. The PDP displays assay reference genome location.
4. The reviewed PDP displays assay reference genome location as Chr.1:41583968 on build GRCh38.
5. The PDP displays cytoband when available.
6. The reviewed PDP displays cytoband as 1p34.2.
7. The PDP provides a See other link for additional CNV assays for the same gene.
8. The reviewed PDP links to other HIVEP3 CNV assays.

### Purchase Configuration

1. The PDP displays Size as a purchase configuration.
2. Size choices are tied to catalog-number choices.
3. The reviewed PDP includes S, M, and L size choices.
4. The reviewed S size choice is 360 reactions and uses catalog number 4400291.
5. The reviewed M size choice is 750 reactions and uses catalog number 4400292.
6. The reviewed L size choice is 2,900 reactions and uses catalog number 4400293.
7. The default selected size for the reviewed PDP is S: 360 rxns.
8. The default displayed catalog number for the reviewed PDP is 4400291.
9. Changing size changes the selected catalog number.
10. The selected catalog number is the catalog number submitted for cart actions.
11. The selected size text is submitted with the cart action.
12. The PDP displays availability for the selected configuration.
13. The reviewed PDP displays Made To Order availability.

### Pricing

1. The PDP displays a Price area for the selected CNV assay configuration.
2. If account-specific pricing is not displayed, the PDP offers a Check your price action.
3. Price lookup is performed for the currently selected catalog number.
4. The price submitted with add-to-cart is based on the selected configuration.

### Add To Cart

1. The PDP displays Add To Cart for the selected CNV assay configuration.
2. Add-to-cart uses quantity 1 by default.
3. Add-to-cart submits the selected catalog number.
4. Add-to-cart submits the displayed Assay ID.
5. Add-to-cart submits the selected size.
6. Add-to-cart submits product type CNV.
7. Add-to-cart submits product subtype Functionally Tested.
8. Add-to-cart identifies the action location as Full Assay Details.

### Assay Details

1. The PDP includes an Assay Details section when assay detail data is available.
2. The reviewed PDP displays Target Gene Details inside Assay Details.
3. Target Gene Details displays Entrez Gene ID when available.
4. The reviewed PDP displays Entrez Gene ID 59269 and links it to NCBI Gene.
5. Target Gene Details displays Gene Name when available.
6. The reviewed PDP displays Gene Name as human immunodeficiency virus type I enhancer binding protein 3.
7. Target Gene Details displays Gene Aliases when available.
8. The reviewed PDP displays Gene Aliases as KBP-1, KBP1, KRC, SHN3, Schnurri-3, ZAS3, and ZNF40C.
9. Target Gene Details displays gene location when available.
10. The reviewed PDP displays gene location as Chr.1:41506365-42035925 on Build GRCh38.
11. Target Gene Details displays assay gene location when available.
12. The reviewed PDP displays assay gene location as Within Exon 8.
13. Assay Details includes a transcript table when transcript data is available.
14. The transcript table displays Gene Symbol, Transcript Accession, Exon Location, Assay Transcript Location, and Protein ID.
15. Transcript accession values link to NCBI nucleotide records when available.
16. Protein ID values link to NCBI protein records when available.
17. If a protein ID value is blank, the Protein ID cell is left blank.

### Genomic Map

1. The PDP includes a Genomic Map section only when map data is available and passes the map readiness check.
2. If the map readiness check fails, the Genomic Map section is hidden.
3. The reviewed PDP initializes map context for product type CNV, assay `Hs00602382_cn`, gene HIVEP3, and Human species.
4. The reviewed PDP marks the current assay as an available assay on the map.
5. CNV maps are gene-based maps.
6. CNV map details links use the copy-number details route.
7. Selecting a different assay on the map opens that assay's copy-number details page.
8. Selecting the current assay on the map does not open a duplicate details page.
9. The CNV genomic map includes a Show DGVs control.
10. CNV assays marked as pretested are visually distinguished on the map.

### More Information

1. The PDP includes a More Information section.
2. The reviewed PDP displays Set Membership in More Information.
3. The reviewed Set Membership values are Intragenic, Exonic, and non-DGV Variation.
4. The PDP displays Gene Ontology Categories when available.
5. Gene Ontology category groups are shown as expandable links.
6. The reviewed PDP includes a Function(s) group.
7. The reviewed PDP includes a Process(es) group.
8. Gene Ontology terms link to AmiGO records.

### Related Products

1. The PDP displays a Related Products section.
2. The reviewed PDP displays six related products:
   - TaqMan Genotyping Master Mix
   - TaqPath ProAmp Master Mix
   - TaqMan Universal Master Mix II, no UNG
   - TaqMan Gene Expression Master Mix
   - TaqMan Universal PCR Master Mix
   - TaqMan Universal PCR Master Mix, No AmpErase UNG
3. Each related product links to its catalog product page.
4. Related product links open in a new browser tab or window.
5. Clicking a related product records the related product catalog number.
6. Related product click tracking records the recommendation position starting at 1.
7. Related product click tracking identifies the recommendation location as the TaqMan assay product page.
8. Related product click tracking identifies the recommendation type as related products.

## Conflicts Found

No business-rule conflicts were confirmed from the deployed page and script evidence reviewed.

## Possible Inferences

1. Direct source validation was not available, so repository-level enforcement of the PDP rules could not be confirmed.
2. The reviewed More Information markup labels one Gene Ontology toggle as Function(s) and another as Process(es). Source validation is needed to confirm whether the displayed labels match the intended Gene Ontology grouping.
