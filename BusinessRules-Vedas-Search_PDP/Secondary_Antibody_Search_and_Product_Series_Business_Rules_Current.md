# Secondary Antibody Search And Product Series Business Rules

## Business Rules

### Search Entry And Product Eligibility

- Secondary antibody search results are limited to products whose product subtype is Secondary Antibody.
- Secondary antibody search uses the secondary antibody search route.
- Secondary antibody search uses the secondary antibody Solr collection.
- Secondary antibody search applies product search status rules before results are returned.
- Secondary antibody search applies entitlement rules before results are returned.
- Secondary antibody search uses the request keyword, selected filters, country, page offset, product type, product subtype, search type, sort selection, and site-search context when building the result set.
- Secondary antibody search has spell-check behavior enabled for the secondary antibody collection.
- Secondary antibody search is eligible for alternate-search behavior across Primary Antibody, Isotype Controls, Proteins and Peptides, and ELISA products.
- Secondary antibody search uses the display title Secondary Antibodies.
- Secondary antibody search is configured as a tab-enabled antibody subtype.
- Secondary antibody search is configured as a BID product subtype.

### Search Filters And Result Counts

- Secondary antibody search displays only filters configured for the Secondary Antibody subtype.
- When exact facet search is enabled and a field facet is requested, only the matching requested facet is returned.
- When exact facet search is not active, all configured secondary antibody facets are returned.
- Facet results are limited by the configured default facet maximum.
- Secondary antibody search result count is configured as 25 results per page for the secondary antibody subtype.
- Secondary antibody search keyword length is constrained by the configured maximum keyword length of 250 characters.
- Search filters can be included from selected navigators and preselected navigators.
- When a filter search returns no products, the page can still return filters and total-hit information for the filtered state.
- If a user keeps filters and the filtered result set has no products, the system checks whether clearing filters would produce results and marks that condition for the search experience.
- Filter-search requests can request filter data for one source field and source value.
- A site-search filter is added only when a site-search filter value is present.

### Search Sorting And Requery

- Secondary antibody search uses the secondary antibody sort configuration.
- The search sort value and sort order are converted into a secondary-antibody sort option.
- If secondary antibody requery is enabled, the first search uses keyword matching and the follow-up requery uses the stricter keyword matching path.
- If secondary antibody requery is not enabled, the search uses the normal keyword matching path.
- When the TPP end-cap feature is enabled and the selected sort is not Relevance, a TPP ascending sort is added before the selected sort.
- Promotion fields are included in the search query only when the promotion-filter feature is enabled.
- Promotion filter results are added only when the search has product results, the request is not site search, and promotion filtering is enabled.

### Search Results Page Display

- The secondary antibody result table displays Product, Images, Host, Target Species, Conjugate, Application, Price, and Compare columns.
- The price column header uses login state, country, language, and total result count to determine the displayed price heading.
- Product rows display brand, product link, image thumbnail, host, target species, conjugate, application abbreviations, price, catalog number, package size, and compare selection.
- Secondary antibody rows display the product catalog number as the SKU.
- If a result has multiple packages, the row displays a package-size selector.
- If a result has one package, the row displays the product size directly.
- Changing package size in a search result uses the selected package data to update the result context.
- Product links route to the product URL for the selected result.
- The result page fetches antibody prices after the page loads.
- Price lookup on the result page is performed for antibody products in the visible result container.
- The image count available to client-side result behavior is set from the total image count returned by search.

### Search Badges, References, And Image Drawer

- The Previously Purchased badge is rendered only for signed-in users.
- The green badge is rendered only when green-badge display is enabled and the product is marked with a green badge.
- Advanced Verification is shown only when the product is target verified and the advanced-verification tag is enabled.
- The Advanced Verification link opens the image gallery for the product using the Advanced Verification application context.
- References are shown in the result row only when the product reference count is greater than zero and reference-count display is enabled.
- The reference label is singular for one reference and plural for more than one reference.
- The image thumbnail opens the product image gallery when image content is available.
- The image drawer receives product subtype, product type, product ID, product link, product image ID, selected tab, gallery type, and application context.

### Compare Behavior

- Secondary antibody results include compare selection.
- The compare panel module is available on antibody search results when the compare module is loaded.
- Compare checkboxes are rendered for both desktop and mobile result layouts.
- Compare selections use the product ID as the comparison identifier.
- Applying a filter or loading a new result context should be tested to confirm whether compare selections are retained or cleared in the current active bundle.

### Zero Results And Alternate Results

- When search returns no products for a non-filter search and spell check is enabled, the system requests spell-check suggestions unless results would appear after clearing filters.
- When search returns no products for a non-filter search and alternate search is enabled, alternate results are requested.
- When no results are returned and the request is not an active product row display state, the zero-results experience is rendered.
- Search results are hidden when the active tab is Images or Antigens.
- Antigen search is rendered only when antigen search is enabled and the active tab is Antigens.
- Image search is rendered through the antibody image-search component.

### Product Detail Eligibility And Routing

- Secondary antibody product detail pages are identified by the Secondary Antibody product subtype.
- Secondary antibody PDP links use the secondary subtype value.
- Secondary antibody PDP search links use the `/antibody/secondary` path.
- Secondary antibody product subtype links route to `/antibody/secondary`.
- The PDP canonical path uses the product subtype, product details, and package details.
- For China and Chinese-language secondary antibody PDPs, page metadata title and description can be overridden from the metadata cache when product metadata exists.
- If no China/Chinese metadata override exists, the PDP uses the normal product title and description rules.

### Product Header And Banner Section

- The PDP header displays the product brand unless the current site-region rules hide it.
- For third-party antibody products, the PDP displays an about-brand message explaining that Thermo Fisher Scientific has partnered with select antibody manufacturers.
- The PDP title uses the product web name.
- The PDP displays the catalog number for the selected product.
- The PDP displays a copy control for the product name in the current hero layout.
- Advanced Verification is shown in the PDP hero only when first target-verification data exists.
- The Advanced Verification hero link routes to the antibody validation page for primary and secondary antibodies.
- Published Figures are shown in the PDP hero only when the published-figure count is greater than zero.
- References are shown in the PDP hero only when citation display is not active and the reference count is greater than zero.
- The PDP displays a "view other antibodies" link only when the protein-family page count exists and is greater than one.
- The "view other antibodies" link for secondary antibodies routes to the secondary-antibody target page.
- Promotion messaging in the header is shown only when promotion results exist for the product order context.
- Promotion messages include promotion code when the promotion is not a quote-free offer.
- Promotion messages include a Learn more link only when a promotion link is present.

### Commerce Card, Price, And Availability

- The commerce card displays the selected catalog number.
- Package selection is built from available package details.
- When a package option matches the product SKU, that package is selected by default.
- Package options carry the selected SKU, web ID, cart action, price-display link flag, contact link, regulatory statement, search status, entitlement status, online price applicability, long-term-unavailable status, list price, third-party flag, data sheet URL, lead-time data, and pricing submessage.
- The package selector is hidden while pricing is loading for signed-in users or FisherSci product-site regions.
- The Your Price message is hidden when the selected package uses a price-display link or cannot be added to cart.
- Signed-in users see the Your Price label when the selected package is eligible for price display.
- Anonymous users see Check your price when the selected package is eligible for price display.
- Selecting Check your price sends the user into the pricing sign-in flow and returns them to the product page.
- Quantity is shown only when the selected package does not use a price-display link and can be added to cart.
- Quantity accepts numeric input with a minimum of 1 and a maximum of 999 in the rendered input.
- The Request bulk or custom quote link is shown with the quantity control for non-FisherSci contexts.
- Add to Cart is hidden when the selected package is not searchable, not entitled, or long-term unavailable.
- In FisherSci product-site regions, the Add to Cart button uses the FisherSci button styling.
- If the selected package uses a price-display link, the commerce action links to the selected package contact link.
- If the selected package cannot be added to cart, the commerce action uses the package cart-action text.
- Otherwise, the commerce action is Add to Cart.
- Save to List is available only when the selected package can be added to cart and the user is eligible for Save to List.
- Signed-in users see Save to List only when shared-list data is available.
- Anonymous eligible users see a Save to List button that routes through the not-logged-in behavior.
- If a signed-in eligible user has shared lists, the Save to List menu shows the user's shared lists.
- If a signed-in eligible user has no shared lists, the Save to List menu shows the create-first-list message.
- The create-new-list field limits the new list name to 150 characters.
- Lead-time or shipping details display only when PDLT is applicable and lead-time mapping exists.
- Performance Guarantee is shown in the commerce area for non-FisherSci contexts.
- The live product example shows Datasheet, Certificates, Questions & Answers, and Tech Support actions near the product header.

### Availability Details

- New availability API behavior is enabled by configuration.
- Estimated availability behavior is enabled by configuration.
- New availability API behavior applies only to configured countries.
- Some countries can be configured as not enabled for the availability API.
- Availability details depend on selected package, country, login context, and availability service response.
- When a package size changes, availability must be re-evaluated for the selected package.
- When quantity changes, availability must be re-evaluated for the selected package.
- Availability behavior should not be hard-coded from static page HTML because final availability is populated by dynamic service responses.

### Product Details And Specifications

- Product Details are displayed when product detail data is available.
- Tested Applications are displayed only when tested application data exists.
- Tested Applications display application name, abbreviation, and dilution.
- Published Applications are displayed only when published application data exists.
- Published Applications link to the matching References section and show the number of related publications.
- Product specifications display only when the underlying value is present.
- Species Reactivity is shown only when reactivity species values exist.
- Published Species is shown only when published species is applicable and the published species list has values.
- Published Species excludes values whose common name starts with Not Applicable.
- Host / Isotype is shown only when host or isotype data exists.
- Recommended Isotype Control is shown only when a recommended isotype web name exists.
- Class is shown only when clonality exists.
- Type is shown only when product subtype exists.
- Clone is shown only when clone ID exists.
- Immunogen is shown only when immunogen exists.
- Conjugate is shown only when conjugate display exists.
- Additional Formats are shown only when additional formats exist.
- Additional Format links route to the antibody product page for the alternate SKU.
- Form is shown only when product form exists.
- Concentration is shown only when concentration exists.
- Purification is shown only when purification type exists.
- Storage Buffer is shown only when storage-buffer type exists.
- Contains is shown only when preservative type exists.
- Storage Conditions are shown only when storage-condition data exists.
- Shipping Condition is shown only when shipping-condition display is enabled and shipping-condition data exists.
- RRID is shown only when RRID exists.
- For Secondary Antibody products, Target is shown only when target-class data exists.
- For Secondary Antibody products, Cross Adsorption is shown only when cross-adsorption data exists.
- For Secondary Antibody products, Antibody Form is shown only when antibody-form data exists.
- Product Specific Information is displayed only when product-specific description exists.
- Target Information is displayed only when product description exists.
- The regulatory statement is displayed from product regulatory-statement data.

### Bioinformatics

- The Bioinformatics section displays only when at least one supported annotation group or allowed bioinformatics identifier is available.
- Panther Molecular Function links are displayed when Panther function data exists.
- GO Function links are displayed when GO process data exists.
- GO Process links are displayed when GO function data exists.
- Bioinformatics links route through the product type, subtype, and Panther content path.
- In the legacy Bioinformatics template, Secondary Antibody products suppress Protein Aliases, Gene Aliases, UniProt ID, and Entrez Gene ID even when those values exist.
- In the shared PDP view-model path, alias and identifier fields require the product subtype to have Bioinformatics display enabled; Secondary Antibody does not enable that subtype flag in the reviewed subtype configuration.
- The reviewed live secondary antibody product page did not show a Bioinformatics section, so Bioinformatics should remain conditional and should not be assumed for every secondary antibody PDP.

### References, Citations, And Published Figures

- Secondary antibody products are configured for citation display.
- Citation data is limited on first load so that only the first citation application keeps its first three citation records.
- Other citation applications keep their application abbreviation while their citation lists are cleared for the first-load payload.
- If a product has zero references, the PDP can display References (0).
- When a product has zero references, the PDP asks users whether they have cited the product in a publication.
- When a product has zero references, the PDP provides a Cite this product action.
- The create-citation modal builds citation text from product web name, Thermo Fisher Scientific, catalog number, and RRID when RRID exists.
- Published figure count can be displayed independently from reference count.
- The reviewed live product page displayed published figures and zero references for the same SKU.
- BenchSci content displays a disclaimer explaining that clicking images or links redirects to third-party scientific content.

### Questions And Answers

- The Questions and Answers module is enabled only when the global Q&A module flag is true and the product subtype is included in the configured Q&A-enabled subtype list.
- Secondary Antibody is included in the configured Q&A-enabled subtype list.
- Q&A is enabled only for countries included in the configured Q&A country list.
- The configured Q&A country list is US and CA.
- The PDP exposes the Q&A widget API path for the product page experience.
- The live secondary antibody PDP displays Questions & Answers as a product action.
- Detailed Q&A matching, sorting, and answer-ranking rules were not confirmed from the accessible search/PDP repository and should be validated against the Q&A service repository before being treated as final business rules.

### Related Products And Related Antibodies

- Related-products module behavior is enabled only when the global related-products flag is true and the product subtype is included in the configured related-products-enabled subtype list.
- Secondary Antibody is included in the configured related-products-enabled subtype list.
- The related-products widget uses the configured related-products module URL.
- When related-products widget V2 is enabled, the module URL uses the V2 path.
- Secondary antibody PDPs always mark related-antibody display as true in the secondary-antibody product detail view model.
- Secondary antibody related-antibody data uses the Secondary subtype value.
- In the secondary antibody related-antibody template, the related-antibody list contains links to See all Secondary Antibodies, Epitope tag antibodies, and Loading isotype controls.
- The legacy secondary antibody cross-sell section also renders Related Antibodies with those same three links.
- Primary antibody suggested-secondary cross-sell rules do not apply to secondary antibody PDPs.

### Technical Support, Data Sheets, And Compliance Messaging

- The Datasheet action links to the product data sheet when a data sheet exists.
- If a data sheet does not exist, the Datasheet action routes to the PDP manuals/documents area.
- Tech Support links to the Thermo Fisher technical support contact page for non-FisherSci contexts.
- FisherSci contexts use regional help-page behavior for Tech Support when allowed by the site-region rules.
- The technical-support modal is enabled only when the product subtype supports the modal and the user's country is in the configured technical-support country list.
- Secondary Antibody is included in the configured technical-support subtype list.
- The configured technical-support country list is US and CA.
- Secondary antibody products can display a For Research Use Only statement when product data contains that regulatory statement.
- Secondary antibody products can display not-for-diagnostic and not-for-resale restrictions when product data contains those statements.

## Possible Inferences

- The live product page displays the Questions & Answers action, but the full Q&A retrieval, ranking, and filtering rules require the Q&A service repository for complete verification.
- The live product page exposes dynamic price and availability areas, but final price, Add to Cart, and availability outcomes require browser execution and commerce-service responses for the selected country and login state.
- The de-magellan team URL itself could not be used to prove exact team membership through the connector; the rules above are based on accessible installed Magellan repositories and live Thermo Fisher product/search pages.
