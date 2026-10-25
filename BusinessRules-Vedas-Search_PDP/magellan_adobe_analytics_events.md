# Magellan UI Adobe Analytics Event Inventory

Source inspected:

- `thermofisher/magellan-search/src/main/javascript/modules/legacy-scripts/scripts/adobeLaunch.js`
- `thermofisher/magellan-search/src/main/webapp/assets/js/assay_Details.js`
- `thermofisher/tfcom-magellan-test-suite/src/test/java/com/thermofisher/Testing/Analytics/BID/PrimaryAntibodiesAnalyticsEventsTests.java`

Note: The UI code populates `window.digitalData` and dispatches Adobe Launch `CustomEvent`s. Exact Adobe Analytics report-suite variables such as `eVar`, `prop`, and `eventN` are normally configured in Adobe Launch rules, not in this UI repository. The variable names below are therefore the source-side data-layer variable paths and Launch event names found in the UI code.

| # | Scenario / user action | Source event binding | Adobe Launch event dispatched | Variable name / path | Value |
|---|---|---|---|---|---|
| 1 | TaqMan search wizard view results | `wizardPopupViewResultsClicked` | `quiz:responseRecorded` | `digitalData.page.name` | `taqman-search-wizard : results` |
| 2 | TaqMan search wizard view results | `wizardPopupViewResultsClicked` | `quiz:responseRecorded` | `digitalData.widgets.quiz.responses` | `{1: productType, 2: species, 3: format, 4: target}` |
| 3 | TaqMan search wizard view results | `wizardPopupViewResultsClicked` | `quiz:responseRecorded` | `digitalData.widgets.quiz.totalQuestions` | `4` |
| 4 | Antibody / ELISA SERP loaded | `magellan-serp-loaded` | `digitalDataLoaded` when delayed tracking applies | `digitalData.page.type` | `magellan search results` |
| 5 | Antibody / ELISA SERP loaded | `magellan-serp-loaded` | `digitalDataLoaded` when delayed tracking applies | `digitalData.search.term` | `params.keyword` |
| 6 | Antibody / ELISA SERP loaded | `magellan-serp-loaded` | `digitalDataLoaded` when delayed tracking applies | `digitalData.search.totalResults` | `String(params.noOfResults)` |
| 7 | Antibody / ELISA SERP loaded | `magellan-serp-loaded` | `digitalDataLoaded` when delayed tracking applies | `digitalData.search.type` | Search type mapping by `productType` / `productSubType`, e.g. `Primary Antibody Search`, `Secondary Antibody Search`, `Isotype Controls Search`, `Proteins and Peptides Search`, `ELISA` |
| 8 | Antibody / ELISA SERP loaded | `magellan-serp-loaded` | `digitalDataLoaded` when delayed tracking applies | `digitalData.search.filters` | `params.filterMapping`; when toggle is true, appends `{name: "keepFilters", values: ["ON"]}` |
| 9 | Antibody / ELISA SERP loaded | `magellan-serp-loaded` | `digitalDataLoaded` when delayed tracking applies | `digitalData.search.sid` | URL query parameter `SID` |
| 10 | Antibody / ELISA SERP loaded | `magellan-serp-loaded` | `digitalDataLoaded` when delayed tracking applies | `digitalData.search.sortType` | `params.currentSort` |
| 11 | TaqMan PDP loaded | `taqMan-pdpLoaded` | `digitalDataLoaded` when delayed tracking applies | `digitalData.page.type` | `taqman assay product` |
| 12 | TaqMan PDP loaded | `taqMan-pdpLoaded` | `digitalDataLoaded` when delayed tracking applies | `digitalData.products[].id` | SKU/product id from `params.id` split by comma |
| 13 | TaqMan PDP loaded | `taqMan-pdpLoaded` | `digitalDataLoaded` when delayed tracking applies | `digitalData.products[].name` | `params.name`, or SKU when name is invalid |
| 14 | TaqMan PDP loaded | `taqMan-pdpLoaded` | `digitalDataLoaded` when delayed tracking applies | `digitalData.products[].price` | Numeric price from `params.price`, normalized; blank when invalid |
| 15 | TaqMan PDP loaded | `taqMan-pdpLoaded` | `digitalDataLoaded` when delayed tracking applies | `digitalData.products[].uom` | `params.uom` |
| 16 | TaqMan PDP loaded | `taqMan-pdpLoaded` | `digitalDataLoaded` when delayed tracking applies | `digitalData.products[].lineName` | `getProductLine(params.productType, params.productSubType)`, e.g. `TaqMan`, `Invitrogen`, `Applied Biosystems` |
| 17 | TaqMan PDP loaded | `taqMan-pdpLoaded` | `digitalDataLoaded` when delayed tracking applies | `digitalData.products[].categoryName` | `getCategoryName(params.productType, params.productSubType)`, e.g. `digital PCR`, `siRNA`, `CRISPR`, `Primary Antibody`, `ELISA` |
| 18 | Antibody / ELISA PDP loaded | `magellan-pdp-loaded` | `digitalDataLoaded` when delayed tracking applies | `digitalData.page.type` | `magellan product` |
| 19 | Antibody / ELISA PDP loaded | `magellan-pdp-loaded` | `digitalDataLoaded` when delayed tracking applies | `digitalData.products[0].id` | `params.id` |
| 20 | Antibody / ELISA PDP loaded | `magellan-pdp-loaded` | `digitalDataLoaded` when delayed tracking applies | `digitalData.products[0].name` | `params.name` |
| 21 | Antibody / ELISA PDP loaded | `magellan-pdp-loaded` | `digitalDataLoaded` when delayed tracking applies | `digitalData.products[0].price` | `params.price` when valid; otherwise blank |
| 22 | Antibody / ELISA PDP loaded | `magellan-pdp-loaded` | `digitalDataLoaded` when delayed tracking applies | `digitalData.products[0].uom` | `params.uom` |
| 23 | Antibody / ELISA PDP loaded | `magellan-pdp-loaded` | `digitalDataLoaded` when delayed tracking applies | `digitalData.products[0].categoryName` | `params.productSubType` |
| 24 | Antibody / ELISA PDP loaded | `magellan-pdp-loaded` | `digitalDataLoaded` when delayed tracking applies | `digitalData.products[0].lineName` | `params.lineName` |
| 25 | Product link clicked from Antibody / ELISA SERP | `magellan-product-link-event` | `searchResultClick` | `detail.search.resultPosition` | `String(params.rowNo)` |
| 26 | Filter applied on Antibody / ELISA SERP | `magellan-search-event` | `searchResultsUpdated` | `detail.search.term` | `params.keyword` |
| 27 | Filter applied on Antibody / ELISA SERP | `magellan-search-event` | `searchResultsUpdated` | `detail.search.totalResults` | `String(params.totalResults)` |
| 28 | Filter applied on Antibody / ELISA SERP | `magellan-search-event` | `searchResultsUpdated` | `detail.search.type` | Search type mapping by product type/subtype |
| 29 | Filter applied on Antibody / ELISA SERP | `magellan-search-event` | `searchResultsUpdated` | `detail.search.filters` | `params.filterMapping` |
| 30 | Filter applied on Antibody / ELISA SERP | `magellan-search-event` | `searchResultsUpdated` | `detail.search.sid` | URL query parameter `SID` |
| 31 | Filter applied on Antibody / ELISA SERP | `magellan-search-event` | `searchResultsUpdated` | `detail.search.sortType` | `params.currentSort` |
| 32 | Product added to shared list from PDP or compare modal | `product-added-to-shared-list` | `saveToList` | `detail.products[0].designId` | `params.id` |
| 33 | Product added to shared list from PDP or compare modal | `product-added-to-shared-list` | `saveToList` | `detail.products[0].title` | `params.name` |
| 34 | Product added to shared list from PDP or compare modal | `product-added-to-shared-list` | `saveToList` | `detail.products[0].price` | `params.price` when valid; otherwise blank |
| 35 | Product added to shared list from PDP or compare modal | `product-added-to-shared-list` | `saveToList` | `detail.products[0].uom` | `params.uom` |
| 36 | Product added to shared list from PDP or compare modal | `product-added-to-shared-list` | `saveToList` | `detail.products[0].catalogNumber` | `params.sku` |
| 37 | Product added to shared list from PDP or compare modal | `product-added-to-shared-list` | `saveToList` | `detail.products[0].categoryName` | `params.productSubType` |
| 38 | Product added to shared list from PDP or compare modal | `product-added-to-shared-list` | `saveToList` | `detail.products[0].lineName` | `params.lineName` |
| 39 | Sort changed on Antibody / ELISA SERP | `magellan-sort-action` | `searchResultsUpdated` | `detail.search.term` | `params.keyword` |
| 40 | Sort changed on Antibody / ELISA SERP | `magellan-sort-action` | `searchResultsUpdated` | `detail.search.sortType` | `params.currentSort` |
| 41 | Sort changed on Antibody / ELISA SERP | `magellan-sort-action` | `searchResultsUpdated` | `detail.search.totalResults` | `String(params.totalResults)` |
| 42 | Sort changed on Antibody / ELISA SERP | `magellan-sort-action` | `searchResultsUpdated` | `detail.search.type` | Search type mapping by product type/subtype |
| 43 | Sort changed on Antibody / ELISA SERP | `magellan-sort-action` | `searchResultsUpdated` | `detail.search.sid` | URL query parameter `SID` |
| 44 | Sort changed on Antibody / ELISA SERP | `magellan-sort-action` | `searchResultsUpdated` | `detail.search.filters` | `params.filterMapping` |
| 45 | Add to cart from PDP, compare modal, GSD PDP, or compare page | `addToCart` | `cartAdd` | `detail.products[0].designId` | `params.productId` if present, else `params.sku` |
| 46 | Add to cart from PDP, compare modal, GSD PDP, or compare page | `addToCart` | `cartAdd` | `detail.products[0].title` | `getProductTitle(params)` |
| 47 | Add to cart from PDP, compare modal, GSD PDP, or compare page | `addToCart` | `cartAdd` | `detail.products[0].price` | Valid `params.price`, otherwise normalized `getPrice(params.price)` |
| 48 | Add to cart from PDP, compare modal, GSD PDP, or compare page | `addToCart` | `cartAdd` | `detail.products[0].quantity` | `params.quantity.toString()` |
| 49 | Add to cart from PDP, compare modal, GSD PDP, or compare page | `addToCart` | `cartAdd` | `detail.products[0].catalogNumber` | `params.sku` |
| 50 | Add to cart from PDP, compare modal, GSD PDP, or compare page | `addToCart` | `cartAdd` | `detail.products[0].uom` | `params.uom` |
| 51 | Add to cart from PDP, compare modal, GSD PDP, or compare page | `addToCart` | `cartAdd` | `detail.products[0].lineName` | `params.lineName` or `getProductLine(params.productType, params.productSubType)` |
| 52 | Add to cart from PDP, compare modal, GSD PDP, or compare page | `addToCart` | `cartAdd` | `detail.products[0].categoryName` | `getCategoryName(params.productType, params.productSubType)` |
| 53 | Add to cart from PDP, compare modal, GSD PDP, or compare page | `addToCart` | `cartAdd` | `detail.products[0].addMethod` | `params.loc`, except omitted for `gsd-pdp` |
| 54 | Add to cart from old GSD / non-TaqMan SERP | `gsdSERPAddToCart` | `cartAdd` | `detail.products[]` | Product array with `designId`, `title`, `price`, `quantity`, `catalogNumber`, `uom`, `lineName`, `categoryName`, optional `addMethod` |
| 55 | Add to cart from new TaqMan SERP | `taqManSERPAddToCart` | `cartAdd` | `detail.products[].categoryName` | `cartItem.categoryName` with final character removed |
| 56 | Add to cart from new TaqMan SERP | `taqManSERPAddToCart` | `cartAdd` | `detail.products[].lineName` | `TaqMan` |
| 57 | Add to cart from new TaqMan SERP | `taqManSERPAddToCart` | `cartAdd` | `detail.products[].price` | Valid `cartItem.price`, otherwise blank |
| 58 | Add to cart from new TaqMan SERP | `taqManSERPAddToCart` | `cartAdd` | `detail.products[].quantity` | `cartItem.qty.toString()` |
| 59 | Add to cart from new TaqMan SERP | `taqManSERPAddToCart` | `cartAdd` | `detail.products[].catalogNumber` | `cartItem.sku` |
| 60 | Add to cart from new TaqMan SERP | `taqManSERPAddToCart` | `cartAdd` | `detail.products[].uom` | `cartItem.uom` |
| 61 | Add to cart from new TaqMan SERP | `taqManSERPAddToCart` | `cartAdd` | `detail.products[].title` | `getProductTitle(cartItem)` |
| 62 | Add to cart from new TaqMan SERP | `taqManSERPAddToCart` | `cartAdd` | `detail.products[].designId` | `cartItem.assayid` if present, else `cartItem.sku` |
| 63 | Add to cart from new TaqMan SERP | `taqManSERPAddToCart` | `cartAdd` | `detail.products[].addMethod` | `cartItem.loc`, omitted when `loc` is `Standard` |
| 64 | Compare modal opened | `compare-action-clicked` | `customLinkClicks` | `detail.CustomLink.linkName` | `{getType(params)} | compare model opened` |
| 65 | Compare page opened | `compare-open-page-clicked` | `customLinkClicks` | `detail.CustomLink.linkName` | `{getType(params)} | compare page opened` |
| 66 | Email action clicked | `email-action-clicked` | `customLinkClicks` | `detail.CustomLink.linkName` | `{getType(params)} | emailed` |
| 67 | Reference link clicked | `reference-clicked` | `customLinkClicks` | `detail.CustomLink.linkName` | `{params.type} | {params.linkClicked}` |
| 68 | Search result row clicked | `searchRowclick` | `searchRowclick` | `detail.Search.searchRowclick` | `params.searchRowclick` |
| 69 | Search result row clicked | `searchRowclick` | `searchRowclick` | `detail.Search.searchResluts` | `params.searchResluts` or current `digitalData.search.totalResults`; source uses typo `searchResluts` |
| 70 | Export selected | `export-action-clicked` | `customDownloads` | `detail.Downloads.fileName` | `{getType(params)} | {params.exportFileName}` |
| 71 | Custom link clicked | `custom-link-clicked` | `customLinkClicks` | `detail.CustomLink.linkName` | `{searchTypeMapping[params.type]} | {params.linkClicked}` |
| 72 | SERP landing after cross-search suggestion | `cross-search-landing` | `customLinkClicks` | `detail.CustomLink.linkName` | `Cross-check Suggestions : {resultLabel} - {params.totalHits} Results`; ELISA label forced to `ELISA Kits` |
| 73 | Spell-check link clicked | `spell-check-link-clicked` | `customLinkClicks` | `detail.CustomLink.linkName` | `spellcheck | {typeDetails} | {params.linkClicked}` |
| 74 | Cross-search link clicked | `cross-search-link-clicked` | `customLinkClicks` | `detail.CustomLink.linkName` | `cross-search | {typeDetails} | {params.linkClicked} | {destTypeDetails without "Search"}` |
| 75 | Epitope slider clicked | `epitope-slider-clicked` | `customLinkClicks` | `detail.CustomLink.linkName` | `{params.type} | {params.keyword} | {params.value}` |
| 76 | Product added to favorites | `addToFavourite` | `favoritesAdd` | `detail.products[]` | Product array with `designId`, `title`, `price`, `uom`, `catalogNumber`, `lineName`, `categoryName` |
| 77 | Old UI search results loaded | `searchResult` | `searchResultsUpdated`; `digitalDataLoaded` when initial load applies | `digitalData.page.type` | `taqman search results` |
| 78 | New UI search results loaded without filters | `elcanosearchResult` | `searchResultsUpdated`; `digitalDataLoaded` when initial load applies | `digitalData.search.term` | `params.keyword`, blank when `NO_KEYWORD` |
| 79 | Search results loaded | `searchResult` / `elcanosearchResult` | `searchResultsUpdated` | `digitalData.search.type` / `detail.search.type` | `getType(params)` |
| 80 | Search results loaded | `searchResult` / `elcanosearchResult` | `searchResultsUpdated` | `detail.search.filters` | Formatted filters from `params.filters` |
| 81 | Search results loaded | `searchResult` / `elcanosearchResult` | `searchResultsUpdated` | `detail.search.sid` | URL query parameter `SID` |
| 82 | Search results loaded | `searchResult` / `elcanosearchResult` | `searchResultsUpdated` | `detail.search.totalResults` | `String(params.totalHits)` |
| 83 | Search results loaded | `searchResult` / `elcanosearchResult` | `searchResultsUpdated` | `detail.search.searchLocation` | `Bottom Search` when `fromBottomSearch` and not toggle; `Search Toggle` when `searchToggleClicked` |
| 84 | Search results loaded | `searchResult` / `elcanosearchResult` | `searchResultsUpdated` | `detail.search.focusarea` | `taqman pathways`, `taqman arrays`, or `taqman assays` from search type |
| 85 | TaqMan filter search | `filterSearch` | `searchResultsUpdated` | `detail.search.term` | `params.keyword` |
| 86 | TaqMan filter search | `filterSearch` | `searchResultsUpdated` | `detail.search.type` | `getType(params)` |
| 87 | TaqMan filter search | `filterSearch` | `searchResultsUpdated` | `detail.search.totalResults` | `String(params.totalResults)` |
| 88 | TaqMan filter search | `filterSearch` | `searchResultsUpdated` | `detail.search.filters` | Formatted filters for `TAQMAN_SERP` / `V1_TAQMAN_SERP`, otherwise `params.filters` |
| 89 | TaqMan filter search | `filterSearch` | `searchResultsUpdated` | `detail.search.sid` | URL query parameter `SID` |
| 90 | TaqMan filter search | `filterSearch` | `searchResultsUpdated` | `detail.search.sortType` | `params.currentSort` |
| 91 | TaqMan filter search | `filterSearch` | `searchResultsUpdated` | `detail.search.focusarea` | Derived from search type |
| 92 | Recommendation / related-product click | `recommendationClick` | `recommendationClick` | `detail.products.id` | `params.id` |
| 93 | Recommendation / related-product click | `recommendationClick` | `recommendationClick` | `detail.products.recommendationLocation` | `params.recommendationLocation`; DPCR related-products source sends `taqman assay product` |
| 94 | Recommendation / related-product click | `recommendationClick` | `recommendationClick` | `detail.products.recommendationPosition` | `params.recommendationPosition.toString()` |
| 95 | Recommendation / related-product click | `recommendationClick` | `recommendationClick` | `detail.products.recommendationType` | `params.recommendationType`; DPCR related-products source sends `related products` |
| 96 | Reset TaqMan filters | `taqman-reset-filters` | `searchResultsUpdated` | `detail.search.term` | `params.keyword` |
| 97 | Reset TaqMan filters | `taqman-reset-filters` | `searchResultsUpdated` | `detail.search.type` | `searchTypeMapping[params.type]` |
| 98 | Reset TaqMan filters | `taqman-reset-filters` | `searchResultsUpdated` | `detail.search.totalResults` | `String(params.totalResults)` |
| 99 | Reset TaqMan filters | `taqman-reset-filters` | `searchResultsUpdated` | `detail.search.sid` | URL query parameter `SID` |
| 100 | Reset TaqMan filters | `taqman-reset-filters` | `searchResultsUpdated` | `detail.search.sortType` | `params.currentSort` |
| 101 | Reset TaqMan filters | `taqman-reset-filters` | `searchResultsUpdated` | `detail.search.focusarea` | Derived from search type |
| 102 | TaqMan sort changed | `taqman-sort-event` | `searchResultsUpdated` | `detail.search.term` | `params.keyword` |
| 103 | TaqMan sort changed | `taqman-sort-event` | `searchResultsUpdated` | `detail.search.type` | `searchTypeMapping[params.type]` |
| 104 | TaqMan sort changed | `taqman-sort-event` | `searchResultsUpdated` | `detail.search.totalResults` | `String(params.totalResults)` |
| 105 | TaqMan sort changed | `taqman-sort-event` | `searchResultsUpdated` | `detail.search.filters` | Formatted filters when `params.loc == "TAQMAN_SERP"` |
| 106 | TaqMan sort changed | `taqman-sort-event` | `searchResultsUpdated` | `detail.search.sid` | URL query parameter `SID` |
| 107 | TaqMan sort changed | `taqman-sort-event` | `searchResultsUpdated` | `detail.search.sortType` | `params.currentSort` |
| 108 | Change dye for all | `change-dye-for-all-event` | `searchResultsUpdated` | `detail.search.searchUpdate` | `params.dye` |
| 109 | Change size for all | `change-size-for-all-event` | `searchResultsUpdated` | `detail.search.searchUpdate` | `params.size` |
| 110 | Change dye for individual item | `change-dye-for-individual-event` | `searchResultsUpdated` | `detail.search.searchUpdate` | `params.dye` |
| 111 | Change size for individual item | `change-size-for-individual-event` | `searchResultsUpdated` | `detail.search.searchUpdate` | `params.size` |
| 112 | TaqMan product header link clicked | `productHeaderLinkClicked` | `searchResultClick` | `detail.search.resultPosition` | `String(data.row)`; skipped when `productType == "crspr"` |
| 113 | Pathways link clicked | `pathways` | `searchResultsUpdated` | `detail.search.term` | `params.keyword`, blank when `NO_KEYWORD` |
| 114 | Pathways link clicked | `pathways` | `searchResultsUpdated` | `detail.search.type` | `pathwaysNameMapping[params.productTypeSelect.toUpperCase()]`, e.g. `Gene Expression Pathways`, `SNP Genotyping Pathways` |
| 115 | Pathways link clicked | `pathways` | `searchResultsUpdated` | `detail.search.searchLocation` | `Search Toggle` |
| 116 | Pathways link clicked | `pathways` | `searchResultsUpdated` | `detail.search.totalResults` | `String(params.totalHits)` |
| 117 | Initial TaqMan load | `onLoadEventForTaqman` | `digitalDataLoaded` when initial load applies | `digitalData.page.type` | `taqman search results` |
| 118 | Initial TaqMan load | `onLoadEventForTaqman` | `digitalDataLoaded` when initial load applies | `digitalData.page.name` | `taqman search results: ALL` |
| 119 | Initial TaqMan load | `onLoadEventForTaqman` | `digitalDataLoaded` when initial load applies | `digitalData.page.nameWithoutCountry` | `taqman search results: ALL` |
| 120 | Unified TaqMan card/search updated | `unifiedUpdated` | `searchResultsUpdated`; `digitalDataLoaded` when initial load applies | `digitalData.page.type` | `taqman search results` |
| 121 | Unified TaqMan card/search updated | `unifiedUpdated` | `searchResultsUpdated` | `digitalData.search.term` / `detail.search.term` | `params.keyword`, blank when `NO_KEYWORD` |
| 122 | Unified TaqMan card/search updated | `unifiedUpdated` | `searchResultsUpdated` | `digitalData.search.type` / `detail.search.type` | `unifiedCardNameMapping[params.productTypeSelect]`, e.g. `taqman search results: ALL`, `taqman search results: miRNA`, `taqman search results: Mutation Detection` |
| 123 | Unified TaqMan card/search updated | `unifiedUpdated` | `searchResultsUpdated` | `detail.search.totalResults` | `String(params.totalHits)` |
| 124 | Unified TaqMan card/search updated | `unifiedUpdated` | `searchResultsUpdated` | `detail.search.searchLocation` | `Bottom Search` when `fromBottomSearch` |
| 125 | No-result search | `noResult` | `searchResultsUpdated`; `digitalDataLoaded` when initial load applies | `digitalData.page.type` | `taqman search results` |
| 126 | No-result search | `noResult` | `searchResultsUpdated` | `digitalData.search.term` / `detail.search.term` | `params.keyword`, blank when `NO_KEYWORD` |
| 127 | No-result search | `noResult` | `searchResultsUpdated` | `digitalData.search.type` / `detail.search.type` | `getType(params)` |
| 128 | No-result search | `noResult` | `searchResultsUpdated` | `detail.search.totalResults` | `String(params.totalHits)` |
| 129 | No-result search | `noResult` | `searchResultsUpdated` | `detail.search.searchLocation` | `Bottom Search` when `fromBottomSearch` |

## Search type / category mappings referenced by the events

| Mapping | Example values |
|---|---|
| Antibody search type | `Primary Antibody Search`, `Secondary Antibody Search`, `Isotype Controls Search`, `Proteins and Peptides Search` |
| TaqMan search type | `Gene Expression`, `Gene Expression Arrays`, `SNP Genotyping`, `SNP Genotyping Arrays`, `Copy Number`, `Mutation Detection`, `Sirna`, `Crispr`, `CEPRIMER`, `Mimics/Inhibitors` |
| miRNA / mutation subtype search type | `taqman search results: mirna : TaqMan Advanced miRNA assays`, `taqman search results: mirna : TaqMan miRNA assays`, `taqman search results: mirna : TaqMan Pri-miRNA assays`, `taqman search results: mutation detection : TaqMan Digital PCR assays`, `taqman search results: mutation detection: TaqMan castPCR assays` |
| Category name | `Primary Antibody`, `Secondary Antibody`, `Isotype Controls`, `Proteins and Peptides`, `ELISA`, `digital PCR`, `castPCR`, `siRNA`, `CRISPR`, `PCR/Sanger sequencing primers`, `Gene expression assays` |
| Focus area | `taqman pathways`, `taqman arrays`, `taqman assays` |
