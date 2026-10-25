# Primary Antibody Product Series Business Rules

## Business Rules

### Product Eligibility And Classification

- Primary antibody products are identified by the Antibody product subtype.
- Primary antibody search results are drawn from the primary antibody product set.
- Primary antibody product records are marked as primary antibody records.
- Primary antibody product records are assigned a search status of 1.
- Primary antibody search returns products only when matching product records are available.
- When no matching product records are available, no primary antibody product result set is returned.

### Product Title Banner

- A product banner is available on the product detail page when at least one package has a long-term-unavailable status, a discontinued status, or a package banner message.
- When a package has a banner message, the product page displays that banner message.
- When the selected package changes, the product banner message changes to the selected package's banner message.
- When the selected package is long-term unavailable, discontinued, or replaced, the product page displays the package-specific availability or replacement banner.
- When a product is temporarily unavailable and has a replacement product, the banner identifies the requested catalog number, links to the replacement catalog number, and directs the user to Technical Support for other replacement options.
- When a product is temporarily unavailable and has no replacement product, the banner identifies the requested catalog number and directs the user to Technical Support for suitable replacement options.
- When a product has been discontinued and replaced, the banner identifies the original catalog number, identifies or links to the replacement catalog number, and directs the user to Technical Support for questions.
- When a product has been discontinued without a replacement, the banner identifies the discontinued catalog number and directs the user to Technical Support for questions.
- Users can close a product banner after it is displayed.

### Product Commerce Card, Price, And Availability

- The product commerce card displays the selected catalog number.
- When a primary antibody product has more than one package size, the commerce card lets the user select the package size.
- When a primary antibody product has one package size, the commerce card uses that package.
- When a package size is selected, the selected SKU is used for the commerce card, data sheet selection, catalog refresh, availability check, and product banner refresh.
- For a multipack product, the selected package is the package whose web ID or SKU matches the product SKU.
- For a single-package product with package details, the commerce card uses the first package SKU.
- Price lookup is performed for the product package SKUs.
- Child package SKUs that return an ERR#1100 or ERR#1200 pricing message are removed from the package selector, except that the parent SKU remains available so the product page can render.
- When pricing data is available for multiple packages, each package receives its own price, user price, bulk quote path, and orderable status.
- When pricing data is available for a single package, the product receives the package price, user price, bulk quote path, and orderable status.
- When pricing is unavailable or fails, the commerce card defaults to View price in cart with an Add to Cart action and USD as the currency before product availability rules are applied.
- A package is not orderable when the pricing action or pricing action name is Error.
- A long-term-unavailable package is not orderable, displays Contact Us as the action, and uses a sales-support contact link for the selected SKU.
- A discontinued package is not orderable and does not display the contact-link action.
- A package with Learn Where To Buy pricing action is treated as a supplier purchase path rather than a normal Add to Cart path.
- A package with No Price pricing action displays the translated no-price message for signed-in users when the package is not discontinued and not long-term unavailable.
- A package with Price View Not Orderable pricing action is treated as price-visible but not normally orderable.
- The Add to Cart action is available only when the selected package is orderable and not long-term unavailable.
- Add to Cart accepts only quantities from 1 through 9,999.
- If the user enters a quantity below 1, the quantity is reset to 1.
- If the user enters a quantity above 9,999, the quantity is reset to 9,999.
- If Add to Cart is attempted with a quantity outside the allowed range, the product page displays the invalid-quantity alert.
- For antibody products, the Add to Cart payload uses the selected web ID as both the SKU and the item identifier.
- Anonymous users see Check Your Price and Availability when the selected package is orderable and availability is not enabled for the current context.
- Anonymous users see Check Your Price when the selected package is orderable and availability is enabled for the current context.
- Selecting Check Your Price sends the user through sign-in and returns the user to the same product page with a from-login marker.
- The Request Bulk or Custom Format action is displayed when the selected package is orderable.
- Primary antibody products are eligible for the Aspire link when the product type is antibody, the product subtype is primary antibody, and the country is the United States or Canada.
- Availability details are shown only when availability is enabled for the user's country or login context and the selected package is orderable.
- When availability is requested, the product page checks availability for the selected SKU.
- When the selected package changes after availability has been requested, the product page resets the availability status and rechecks availability for the new package.
- When the selected quantity changes, the product page rechecks availability for the selected package.
- When the availability response shows available quantity greater than zero, the product page displays the in-stock status.
- When the availability response shows no available quantity, the product page displays estimated availability details.
- When estimated availability is pending or missing, the product page displays Pending as the estimated availability date.
- Estimated availability date is displayed only when estimated availability is enabled, the selected package is orderable, availability status requires an estimate, and availability is enabled for the current context.
- For dealer-enabled signed-in users, the product page can display partial stock, default availability label, domestic stock quantity, overseas stock quantity, and estimated availability date from the dealer availability result.

### Product Data And Specifications

- Target verification uses the first value before a pipe delimiter when a target verification value is present.
- Target verification is set to No when no target verification value is present.
- Availability is shown as Inventoried when the default inventory status is Y.
- Availability is shown as Made to Order when the default inventory status is anything other than Y.
- Important information is flagged Yes only for important-information comment types 5 and 6.
- Important information is flagged No for all other important-information comment types.
- A product is flagged as having assay comments when at least one assay comment exists.
- A product is flagged as having a critical alert when at least one critical alert comment exists.
- A product is marked as having multiple applications only when it has more than one application and Flow Cytometry is one of those applications.
- Cross-adsorption species are split into separate values when provided as pipe-delimited text.
- Cross-adsorption is set to No when no cross-adsorption species are provided.
- Package sizes are split into separate values when provided as pipe-delimited text.
- Alternate SKUs are split into separate values when provided as pipe-delimited text.
- Laser compatibility values are split into separate values when provided as pipe-delimited text.
- Repeated GenBank mRNA IDs are deduplicated before product data is used.
- Repeated RefSeq accessions are deduplicated before product data is used.
- Repeated GenBank mRNA accessions are deduplicated before product data is used.
- Repeated protein IDs are deduplicated before product data is used.
- Repeated protein aliases are deduplicated before product data is used.
- Protein aliases from product properties are split into separate values when provided as pipe-delimited text.
- UniProt protein aliases are split into separate values when provided as pipe-delimited text.
- Reactivity species, predicted reactivity species, applications, application abbreviations, and reactivity species abbreviations are retained as grouped product values.

### Product Detail Specifications

- Primary antibody product detail pages display tested applications and dilution values when they are available.
- Primary antibody product detail pages display product specifications when specification values are available.
- Primary antibody product specifications can include species reactivity, published species, host/isotype, expression system, class, type, clone, immunogen, conjugate, form, concentration, amount, purification, storage buffer, contents, storage conditions, shipping conditions, and RRID.
- Primary antibody product detail pages display product-specific information when it is available.
- Primary antibody product detail pages display Target Information when target information is available.
- Primary antibody product pages display the For Research Use Only notice when present.
- Primary antibody product pages display the Not for diagnostic procedures notice when present.
- Primary antibody product pages display the not-for-resale notice when present.

### Product Structured Data

- Product structured data includes product specifications only when specification values are present.
- Product structured data omits empty specification values.
- Product structured data uses the first available product image when one exists.
- Product structured data uses the default antibody no-image asset when no product image is available.
- Product structured data removes offer information when the selected product is discontinued, long-term unavailable, missing a final price, missing availability data, or not orderable.
- When product offer structured data is valid, it includes normalized final price, price currency when present, stock availability, product URL, selected SKU, and new-condition item status.
- When a special-offer end date or web-only-price end date is available, product offer structured data uses that date as the price-valid-until date.

### Images And Published Figures

- Regular product image count includes only non-BenchSci external images.
- BenchSci published figure count is capped at 40.
- When BenchSci images exceed 40, total image count uses the capped BenchSci count plus regular product images.
- When BenchSci images do not exceed 40, total image count uses the full external-link count.
- The validation image prefers a non-BenchSci image with nonnegative sort order and the lowest available sort order.
- If no non-BenchSci image has nonnegative sort order, the validation image uses the non-BenchSci image with the highest negative sort order.
- The thumbnail image prefers the first BenchSci image by sort order.
- If no BenchSci image exists, the thumbnail image prefers the first non-BenchSci image with nonnegative sort order.
- If no BenchSci image exists and no non-BenchSci image has nonnegative sort order, the thumbnail image uses the non-BenchSci image with the highest negative sort order.
- When a product has no regular images and no BenchSci published figures, the product displays a no-image placeholder.
- When both regular images and BenchSci published figures exist, the regular product image is used as the thumbnail.
- When only BenchSci published figures exist, the BenchSci published figure flow is used for the thumbnail and image count.
- When more than one image is available, the product displays the number of additional images beyond the thumbnail.
- Image source URLs remove the .qa marker before display.

### Product Detail Content

- Primary antibody product results display product identity, thumbnail, description, product type, product subtype, reference count, and image count.
- Primary antibody product results display antibody-specific details when available, including applications, assay sets, availability, BenchSci image count, citations, clonality, clone, conjugate, cross-adsorption, host, important information, lifecycle, package sizes, product badge, product name, product size, protein target, publication count, reactivity species, source, spectra ID, target, target class, target verification, and web name.
- Primary antibody product results display genomic details when available, including chromosome, chromosome start, chromosome end, build, common RefSeq values, and metadata.

### Bioinformatics

- Primary antibody product detail pages display a Bioinformatics section header.
- Primary antibody Bioinformatics displays protein aliases.
- Primary antibody Bioinformatics displays gene aliases.
- Primary antibody Bioinformatics displays the UniProt ID.
- Primary antibody Bioinformatics displays the Entrez Gene ID.
- Primary antibody Bioinformatics displays Function(s).
- Primary antibody Bioinformatics displays Process(es).
- Bioinformatics is available as a product detail page section destination only when the Bioinformatics section is visible.
- The active product detail page section is determined only from visible sections.

### Target Information

- Primary antibody target family pages display target information for Gene, Protein, Panther, and Gene Ontology target families.
- Gene target family pages display Antibodies and by Gene anchor links.
- Protein target family pages display Antibodies, by Gene, and by Protein anchor links.
- Panther and Gene Ontology target family pages display Antibodies, by Panther Class, and by Gene Ontology anchor links.
- Target family pages display the selected target title.
- Target family pages display target information for the selected target.
- Gene and Protein target family descriptions display truncated text ending with an ellipsis before expansion.
- Gene and Protein target family pages display View More when the target description is truncated.
- Selecting View More displays the expanded target information and changes the control to View Less.
- Selecting View Less returns the description to the collapsed state and changes the control to View More.

### References

- When a primary antibody product detail page has reference cards, loading the References section loads all reference cards.
- BenchSci reference cards display an image.
- BenchSci reference cards display published figures with a BenchSci icon.
- BenchSci reference cards display a disclaimer section.
- Reference cards display source, title, and year.
- Non-BenchSci reference cards display species, dilution, description, and authors.
- References can be sorted by Species in ascending order.
- References can be sorted by Dilution in ascending order.
- References can be sorted by Title in ascending order.
- References can be sorted by Authors in ascending order.
- References can be sorted by Journal in ascending order.
- References can be sorted by Most Recent using year in descending order.
- Publication tables initially show the first five rows and hide remaining rows.
- Selecting View More on a publication table displays all hidden rows.
- Selecting View Less on a publication table returns the publication table to the first five visible rows.
- References is available as a product detail page section destination only when the References section is visible.

### Related Products

- Primary antibodies are loaded as related-product records only when the source row type is Antibody.
- Secondary antibodies are loaded as related-product records only when the source row type is Secondary Antibody.
- Isotype controls are loaded as related-product records only when the source row type is Isotype Control.
- Primary antibody target species relationships exclude blank, All, Not Applicable, and Many species values.
- Primary antibody target species values are split into separate species when the source value contains comma-separated species.
- Primary antibody target isotype values are split into separate isotypes when the source value contains slash-separated isotypes.
- Primary antibody conjugate values are split into separate conjugates when the source value contains comma-separated conjugates.
- Primary antibody application values are split on pipe delimiters, and dilution text in parentheses is removed before the application is related to the antibody.
- Secondary antibody recommendations for a primary antibody are matched by the primary antibody host species to the secondary antibody target species and by the primary antibody target isotype to the secondary antibody target class.
- Secondary antibody recommendations are prioritized in this order: cross-adsorption with clone and conjugate, cross-adsorption with conjugate, cross-adsorption with clone, clone with conjugate, cross-adsorption only, conjugate only, clone only, then all others.
- Isotype control recommendations for a primary antibody are matched by host species and target isotype.
- When the primary antibody has a conjugate, recommended isotype controls must have the same conjugate.
- Isotype control recommendations are prioritized by clone with conjugate, then clone only, then conjugate only, then all others.
- Isotype control recommendations are ordered by size.
- Related primary antibody alternatives are matched to the original primary antibody by target protein and target isotype.
- The original primary antibody is excluded from related primary antibody alternatives.
- Related primary antibody alternatives are prioritized by clone availability, then conjugate value, then size.
- ELISA kit recommendations are returned only when the primary antibody supports the ELISA application.
- ELISA kit recommendations are matched to the primary antibody by target protein and tested species.
- ELISA kit recommendations exclude kits whose assay kit format is Matched Antibody Pair.
- ELISA kit recommendations are ordered by size, coated value, and assay kit format.
- Matched antibody pair recommendations are returned only when the primary antibody supports the ELISA application.
- Matched antibody pair recommendations are matched to the primary antibody by target protein and tested species.
- Matched antibody pair recommendations include only ELISA kits whose assay kit format is Matched Antibody Pair.
- Matched antibody pair recommendations are ordered by size, coated value, and assay kit format.
- Application-level related products are created only when both application and SKU are present.
- Application-level related products are grouped by subapplication when related-product counts are returned for an application.
- Application-level related products can be filtered by both application and subapplication.

### Questions And Answers

- Primary antibody question-and-answer keyword generation always sets the product subtype to Antibody.
- Primary antibody question-and-answer keywords are generated from protein target, application, host species, conjugate, clonality, clone, brand, target species, product subtype, format, and recombinant values.
- For list-based keyword inputs, the default keyword is used when the list is missing or empty.
- For list-based keyword inputs that contain values, each value is included and the default keyword is also added.
- For single-value keyword inputs, the value is included when it is present and not blank, and the default keyword is always added.
- Keyword values remove the nonbreaking-space marker before they are used.
- Default keyword values include AnyProteinTarget, AnyApplication, AnySpecies, AnyConjugate, AnyClonality, AnyClone, AnyBrand, AnyTargetSpecies, AnyProductSubType, AnyFormat, and AnyRecombinant.
- Question-and-answer matching includes records for the exact SKU.
- Question-and-answer matching also includes records that match product keyword filters.
- Primary antibody question-and-answer product filters include host, clonality, protein target, conjugate, clone, brand, target species, format, and recombinant values.
- Application filters are included when application keywords are present.
- Empty format keyword values are removed before question-and-answer matching.
- Product subtype filters are included only when a product subtype is present.
- Counting question-and-answer records returns the number of matched records without returning question rows.
- A failed question-and-answer count returns zero.
- Paged question-and-answer results start at `(page - 1) * limit` and return at most `limit` records.
- Paged question-and-answer results are sorted by answer count descending, then submitted date descending.
- Unpaged question-and-answer results are sorted by vote count descending, then answer count descending, then submitted date descending.
- Filtered question-and-answer search uses all matched questions when the filter keyword is `*`.
- Filtered question-and-answer results are sorted by vote count descending, then answer count descending, then submitted date descending.
- Question-and-answer search returns an empty result set when an error occurs.
- Question-and-answer lookup by IDs returns an empty result set when the ID list is missing or empty.
