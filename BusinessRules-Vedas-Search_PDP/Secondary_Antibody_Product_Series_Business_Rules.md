# Secondary Antibody Product Series Business Rules

## Business Rules

### Product Eligibility And Classification

- Secondary antibody products are identified by the Secondary Antibody product subtype.
- Secondary antibody product records are loaded as secondary antibody records only when the source row type is Secondary Antibody.
- Secondary antibody product detail pages use the secondary antibody product subtype in generated product documents and product data sheets.
- Secondary antibody products are included in Q&A behavior when the secondary antibody subtype is included in the Q&A-enabled subtype list.
- Secondary antibody products are included in related-products behavior when the secondary antibody subtype is included in the related-products-enabled subtype list.

### Product Title Banner

- A product banner is available on the product detail page when at least one package has a long-term-unavailable status, a discontinued status, or a package banner message.
- When a package has a banner message, the product page displays that banner message.
- The secondary antibody example package banner states that Alexa Fluor Plus provides high sensitivity, optimized multiplexing, and detection of low-abundance targets, and it provides a Learn more link.
- When the selected package changes, the product banner message changes to the selected package's banner message.
- When the selected package is long-term unavailable, discontinued, or replaced, the product page displays the package-specific availability or replacement banner.
- When a product is temporarily unavailable and has a replacement product, the banner identifies the requested catalog number, links to the replacement catalog number, and directs the user to Technical Support for other replacement options.
- When a product is temporarily unavailable and has no replacement product, the banner identifies the requested catalog number and directs the user to Technical Support for suitable replacement options.
- When a product has been discontinued and replaced, the banner identifies the original catalog number, identifies or links to the replacement catalog number, and directs the user to Technical Support for questions.
- When a product has been discontinued without a replacement, the banner identifies the discontinued catalog number and directs the user to Technical Support for questions.
- Users can close a product banner after it is displayed.

### Product Commerce Card, Price, And Availability

- The product commerce card displays the selected catalog number.
- When a secondary antibody product has more than one package size, the commerce card lets the user select the package size.
- The secondary antibody example offers package sizes for catalog numbers A32723TR and A32723.
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
- Secondary antibody products are eligible for the Aspire link when the product type is antibody, the product subtype is secondary antibody, and the country is the United States or Canada.
- Availability details are shown only when availability is enabled for the user's country or login context and the selected package is orderable.
- When availability is requested, the product page checks availability for the selected SKU.
- When the selected package changes after availability has been requested, the product page resets the availability status and rechecks availability for the new package.
- When the selected quantity changes, the product page rechecks availability for the selected package.
- When the availability response shows available quantity greater than zero, the product page displays the in-stock status.
- When the availability response shows no available quantity, the product page displays estimated availability details.
- When estimated availability is pending or missing, the product page displays Pending as the estimated availability date.
- Estimated availability date is displayed only when estimated availability is enabled, the selected package is orderable, availability status requires an estimate, and availability is enabled for the current context.
- For dealer-enabled signed-in users, the product page can display partial stock, default availability label, domestic stock quantity, overseas stock quantity, and estimated availability date from the dealer availability result.

### Product Details And Specifications

- Secondary antibody product detail pages display tested applications and dilution values when they are available.
- Secondary antibody product detail pages display product specifications when specification values are available.
- Secondary antibody product specifications can include species reactivity, host/isotype, class, type, immunogen, conjugate, excitation/emission maximum, form, concentration, amount, purification, storage buffer, contents, storage conditions, shipping conditions, RRID, target, cross adsorption, and antibody form.
- When additional conjugate formats are available, the product page displays a View additional formats option.
- When custom conjugation is available, the product page displays a Request custom conjugation option.
- Secondary antibody product detail pages display product-specific information when it is available.
- Secondary antibody product detail pages display Target Information when target information is available.
- Secondary antibody target information describes the target antibody specificity and secondary-antibody usage.
- Secondary antibody product pages display the For Research Use Only notice when present.
- Secondary antibody product pages display the Not for diagnostic procedures notice when present.
- Secondary antibody product pages display the not-for-resale notice when present.

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
- BenchSci published figure count is controlled by the configured published-image limit.
- The product page can display published figures even when citation references are zero.
- When a product has no regular images and no BenchSci published figures, the product displays a no-image placeholder.
- When both regular images and BenchSci published figures exist, the regular product image is used as the thumbnail.
- When only BenchSci published figures exist, the BenchSci published figure flow is used for the thumbnail and image count.
- When more than one image is available, the product displays the number of additional images beyond the thumbnail.
- Image source URLs remove the .qa marker before display.

### References

- When a secondary antibody product detail page has reference cards, loading the References section loads all reference cards.
- BenchSci reference cards display an image.
- BenchSci reference cards display published figures with a BenchSci icon.
- BenchSci reference cards display a disclaimer section.
- Reference cards display source, title, and year.
- Non-BenchSci reference cards display species, dilution, description, and authors.
- When a secondary antibody product has zero references, the product page displays References (0).
- When a secondary antibody product has zero references, the product page asks users to report publications citing the product.
- When a secondary antibody product has zero references, the product page provides a Cite this product action.

### Related Products

- Secondary antibodies are loaded as related-product records only when the source row type is Secondary Antibody.
- Secondary antibody host species relationships are created only when host species is present and is not N/A.
- Secondary antibody target species relationships exclude blank, All, Not Applicable, and Many species values.
- Secondary antibody target species values are split into separate species when the source value contains comma-separated species.
- Secondary antibody target class values are split into separate target classes when the source value contains slash-separated values.
- Secondary antibody isotype values are split into separate isotypes when the source value contains slash-separated values.
- Secondary antibody conjugate values are split into separate conjugates when the source value contains comma-separated conjugates.
- Secondary antibody application values are split on pipe delimiters, and dilution text in parentheses is removed before the application is related to the antibody.
- Secondary antibody related-product records retain secondary-specific properties such as target antibody, host, class, clone, isotype, immunogen, emission, excitation, antibody form, cross adsorption, target class, species, applications, conjugates, size, units, and US price when those values are provided.

### Questions And Answers

- Secondary antibody question-and-answer keyword generation always sets the product subtype to Secondary Antibody.
- Secondary antibody question-and-answer keywords are generated from application, host species, target species, target class, conjugate, product subtype, format, and recombinant values.
- For list-based keyword inputs, the default keyword is used when the list is missing or empty.
- For list-based keyword inputs that contain values, each value is included and the default keyword is also added.
- For single-value keyword inputs, the value is included when it is present and not blank, and the default keyword is always added.
- Keyword values remove the nonbreaking-space marker before they are used.
- Default keyword values include AnyApplication, AnySpecies, AnyTargetSpecies, AnyTargetClass, AnyConjugate, AnyProductSubType, AnyFormat, and AnyRecombinant.
- Question-and-answer matching includes records for the exact SKU.
- Question-and-answer matching also includes records that match product keyword filters.
- Secondary antibody question-and-answer product filters include host, conjugate, target species, target class, format, and recombinant values.
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
