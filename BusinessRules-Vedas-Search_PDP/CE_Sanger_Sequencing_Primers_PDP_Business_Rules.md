# CE/Sanger Sequencing Primers PDP Business Rules

## Business Rules

### Product Identity

1. A CE/Sanger sequencing primer PDP is identified by an Assay ID.
2. The Assay ID is displayed in the purchase card.
3. The displayed Assay ID is also retained as the assay identifier used for ordering.
4. The reviewed primer PDP is classified as a CE primer product.
5. The reviewed primer PDP is classified under the Primer product subtype.
6. The CE/Sanger primer product family is labeled as PCR/Sanger sequencing primers in the search and product-family mapping.
7. The product detail page records the reviewed product as assay `Hs00710994_CE`.
8. The reviewed assay is associated with Human species context.

### Purchase Configuration

1. The PDP displays Purification as a required purchase configuration.
2. The available purification choices shown for the reviewed PDP are DS and HPLC.
3. DS is the default selected purification for the reviewed PDP.
4. The PDP displays Size as a purchase configuration.
5. Size options are tied to catalog-number choices.
6. The reviewed PDP includes 25 nmol and 50 nmol size choices.
7. The selected size determines the catalog number shown in the purchase card.
8. The default displayed catalog number for the reviewed PDP is A15629.
9. The selected catalog number is the catalog number submitted for cart actions.
10. The selected size text is submitted with the cart action.
11. When the configuration changes, the displayed catalog number, price area, availability, and cart payload are updated to match the selected configuration.
12. The PDP displays availability for the selected configuration.
13. The reviewed PDP displays the selected configuration as Made To Order.
14. Configurations with non-inventoried inventory status are displayed as Made To Order.
15. Configurations with inventoried inventory status are displayed as Inventoried.

### Pricing

1. The PDP displays a Price area for the selected primer configuration.
2. If the account-specific price is not already displayed, the PDP offers a Check your price action.
3. Price lookup is performed for the currently selected catalog number.
4. When multiple catalog numbers are selected as one primer-pair configuration, prices are displayed as a comma-separated set.
5. The price submitted with add-to-cart is based on the selected configuration.

### Add To Cart

1. The PDP displays Add To Cart for the selected primer configuration.
2. Add-to-cart uses quantity 1 by default.
3. Add-to-cart submits the selected catalog number.
4. Add-to-cart submits the displayed Assay ID.
5. Add-to-cart submits the selected size.
6. Add-to-cart submits the CE primer product type and Primer subtype.
7. If the selected configuration contains two primer SKUs, the cart button changes to Add pair to cart.
8. If the selected configuration contains two primer SKUs, both SKUs are submitted together.
9. If a single primer SKU is selected, the cart button displays Add to cart.
10. The Favorites action follows the same single-item versus pair distinction as Add to Cart.

### Assay Details Section

1. The PDP includes an Assay Details page section.
2. The page navigation includes an Assay Details anchor when the section is present.
3. For the reviewed anonymous PDP response, no populated Assay Details fields were rendered inside the Assay Details section.
4. The page also includes a More Information section.
5. For the reviewed anonymous PDP response, no populated More Information fields were rendered inside the More Information section.

### Genomic Map

1. The PDP includes a Genomic Map section only when map data is available and passes the map readiness check.
2. If the map readiness check fails, the Genomic Map section is hidden.
3. The reviewed PDP initializes map context for the CE primer assay and Human species.
4. The reviewed PDP marks the current assay as an available assay on the map.
5. Selecting a different assay on the map opens that assay's details page.
6. Selecting the current assay on the map does not open a duplicate details page.

### Related Products

1. The PDP displays a Related Products section.
2. The reviewed PDP displays five related products:
   - POP-6 Polymer
   - POP-7 Polymer
   - BigDye Terminator v1.1 Cycle Sequencing Kit
   - BigDye Terminator v3.1 Cycle Sequencing Kit
   - BigDye Direct Cycle Sequencing Kit
3. Each related product links to its catalog product page.
4. Related product links open in a new browser tab or window.
5. Clicking a related product records the related product catalog number.
6. Related product click tracking records the recommendation position starting at 1.
7. Related product click tracking identifies the recommendation location as the TaqMan assay product page.
8. Related product click tracking identifies the recommendation type as related products.

### Recently Viewed

1. When recently viewed tracking is available, the PDP adds the reviewed assay to the user's recently viewed list.
2. The recently viewed entry uses the assay ID as the product identifier.
3. The recently viewed entry labels the product as a HONEY assay.
4. The recently viewed entry uses the product details URL for the assay.
5. The recently viewed entry uses a default brand image when a product-specific image is not available.

## Conflicts Found

No business-rule conflicts were confirmed from the deployed page and script evidence reviewed.

## Possible Inferences

1. Direct source validation was not available, so repository-level enforcement of the PDP rules could not be confirmed.
2. The reviewed page renders Assay Details and More Information section headers without populated details. Source validation is needed to determine whether those sections are intentionally empty for this assay, hidden by user state, or dependent on unavailable backend data.
3. The deployed script contains logic for primer-pair configurations and tail, purification, and pair selections. The reviewed anonymous PDP response clearly showed Purification and Size controls, but did not visibly render every primer-pair control from the shared script.
