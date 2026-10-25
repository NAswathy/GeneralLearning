# TaqMan Assays and Arrays Business Rules

## Business Rules

### Search Entry and Keyword Handling

- A blank TaqMan search keyword is treated as a wildcard search.
- The wildcard keyword `*` is allowed for SNP Genotyping assay search.
- Search keywords keep letters, numbers, hyphens, underscores, periods, commas, colons, semicolons, parentheses, and spaces. Other unsupported characters are removed before search is submitted.
- The SNP Genotyping assay search page searches SNP assay results.
- When SNP assay search results are loaded, previously selected comparison products are cleared.
- If a SNP assay search returns no results because selected filters removed all matches, the page shows filter-specific zero-results behavior.
- If a SNP assay search returns no unfiltered results, the page redirects to the broader TaqMan results experience for the same keyword and product family.

### SNP Search Filters

- SNP assay results expose five filter groups: Species, Attributes, Genes, SNP type, and Assay type.
- Species filter values are driven by the search result payload. In the wildcard example, Species includes Human and Mouse.
- Attributes filter values are driven by the search result payload. In the wildcard example, Attributes includes Allele frequency known and Inventoried.
- Genes filter values are driven by gene-symbol facets returned for the current search result set.
- SNP type filter values are driven by SNP-type facets returned for the current search result set. In the wildcard example, values include Intragenic, Intergenic/unknown, Intron, UTR 5, and UTR 3.
- Assay type filter values are driven by assay subtype facets returned for the current search result set. In the wildcard example, values include Functionally tested, DME, Validated, and Qualified.
- Filter values include counts and checked state.
- Selected filters are carried into the search request and change the returned result set.

### SNP Result Table Columns

- SNP assay result rows use these business columns: SNP ID, Gene, Assay ID, Allele, Dye/Size, Price, and selection.
- SNP ID is sortable.
- Gene is sortable.
- Assay ID is sortable.
- Allele is sortable.
- Dye/Size is displayed as a product configuration control and is not implemented as a sortable table column.
- Price is displayed for the selected catalog number and is not implemented as a sortable table column.
- The selection column lets users select individual products for comparison and bulk actions.
- The header selection control selects or clears the currently loaded SNP products.

### SNP Result Row Fields

- SNP ID links to the corresponding NCBI SNP page using the result product ID.
- Assay ID links to the genotyping product detail page for the result assay ID.
- In Fisher Scientific context, the Assay ID detail link adds the Fisher Scientific plugin parameter.
- Gene values are displayed as a comma-separated list when more than one gene is returned.
- Allele values are displayed from the result allele field.
- Each row carries the result species, assay type, selected catalog number, selected size, selected dye, selected availability, and dye-size options.
- A functionally tested indicator is shown only when the result assay type is Functionally tested.
- The functionally tested message states that Functionally Tested Assays meet minimum functionality criteria in 20 genomic DNA samples from three ethnic populations and both genders before shipment on first order, and that minor allele frequency is not calculated.
- A discontinued assay warning is shown when the assay is discontinued.
- The discontinued assay message states that the assay may not function as expected in all samples, that users may still order it if they verified performance in their experiments, and otherwise should search for a replacement or design a custom assay.

### Dye, Size, Catalog, and Availability

- SNP assay rows default to the result payload's default dye, size, catalog number, and availability.
- Dye-size choices are grouped by dye.
- Size choices are sorted by reaction count in ascending order.
- When the dye changes, the selected catalog number, selected size, selected dye, selected availability, and saved-list item are updated.
- If the selected dye is the default dye, the default catalog number is retained when it is available in that dye's size options.
- If the selected dye is not the default dye, the first available size option for that dye is selected.
- When the size changes, the selected catalog number, selected size, selected availability, and saved-list item are updated.
- Selected availability is tied to the selected size/catalog configuration, not only to the assay.
- Price is requested for the selected catalog number.
- If the pricing response does not provide an add-to-cart price, the page displays either View price in cart or Price not available.

### Copy, Citations, Details, and Related Content

- Copy-to-clipboard for a SNP assay copies the selected catalog number and assay ID together.
- The copy helper message states that both catalog number and Assay ID are required for ordering the selected assay configuration.
- After a successful copy, the page confirms that the catalog number and Assay ID were copied to the clipboard.
- Citation content is shown only when citation data exists for the assay.
- Allele frequency content is shown for non-mouse SNP assays.
- Allele frequency content is hidden for mouse SNP assays.
- SNP row details may include Product Details, Assay Map, Gene details, Allele frequency, Related products, Citations, and Details when the backing data exists.

### Add to Cart

- SNP result-row add to cart uses the selected catalog number.
- Thermo Fisher add to cart uses the assay ID, selected catalog number, quantity one, selected size or default size, price, and SNP product subtype.
- Fisher Scientific add to cart uses the selected catalog number, quantity one, unit EA, assay ID, and first gene symbol when available.
- If Fisher Scientific add to cart fails, the row shows Unable to add to cart.

### Compare Selection

- The compare panel is shown when at least one product is selected.
- The compare panel displays up to the first three selected products.
- When fewer than three products are selected, the compare panel shows a placeholder inviting users to select up to three products.
- When more than three products are selected, the compare panel shows the count above three as additional items.
- Compare is enabled only when two or three assay products are selected.
- Compare is disabled when fewer than two products are selected.
- Compare is disabled when more than three products are selected.
- Compare is disabled for array products unless custom-array comparison is enabled.
- SNP compare submits assay IDs for comparison.
- SNP compare uses SNP as the compare product type.
- If compare fails, the page shows an error telling the user to try again later.

### Compare Panel Actions

- Users can remove a selected product from the compare panel.
- Removing a product updates the selected product set.
- Add to cart from the compare panel adds the selected product configurations.
- Compare-panel add to cart uses the selected catalog number when present; otherwise it uses the default catalog number.
- Compare-panel add to cart uses selected quantity when present; otherwise it uses quantity one.
- Compare-panel add to cart records the action as coming from the Compare Panel.
- Download List is available from the compare panel.
- Email List is available from the compare panel.
- When all assay results are selected, Download List indicates a limit of up to 1000 assays.
- When all assay results are selected, Email List indicates a limit of up to 4000 assays.
- When all array results are selected, Download List and Email List indicate a limit of up to 100 arrays.
- If the selected result set is too large to export, the user is told the selected result set is too large to export.
- If the selected result set is too large to email, the user is told the selected result set is too large to email.
- Email List requires the user to enter an email address.

### Compare Modal

- The compare modal includes Product Information.
- The compare modal supports searching within the comparison.
- SNP Product Information comparison includes assay ID, availability, gene symbol, location, assay type, polymorphism, and SNP type.
- The compare modal displays the notice: For Research Use Only. Not for use in diagnostic procedures. Not for resale without express authorization.

### Multiple-Target Search

- Search multiple targets is available from the SNP assay search page in Thermo Fisher context.
- Search multiple targets routes users to the TaqMan target-list product chooser.
- Search multiple targets is hidden in Fisher Scientific context.

## Conflicts Found

- No deployed-behavior conflicts were found in the reviewed SNP search and compare evidence.

## Possible Inferences

- Source-repository enforcement of the same rules could not be confirmed because the requested GitHub repositories were not accessible in this session.
