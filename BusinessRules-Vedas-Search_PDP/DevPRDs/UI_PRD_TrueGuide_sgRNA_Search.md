# UI Developer PRD: TrueGuide sgRNA Search

## Document Control

| Field | Value |
|---|---|
| Document title | UI Developer PRD: TrueGuide sgRNA Search |
| Tool URL | https://www.thermofisher.com/crispr/invitrogen/query/* |
| Product area | CRISPR Guide RNA Search |
| Main product family | TrueGuide sgRNA Search |
| Document type | UI rules document / developer PRD |
| Requested perspective | UI developer perspective with repo names, module names, important function names, workflows, and validation notes |
| Repositories reviewed | thermofisher/magellan-search; thermofisher/tfcom-magellan-search-engine; thermofisher/magellan-core; thermofisher/magellan-data-scripts |
| Primary UI evidence repository | thermofisher/magellan-search |
| Source handling | Rules are limited to behavior observed in source files and repo evidence. Where backend behavior is referenced, it is identified as a supporting dependency rather than a UI-owned rule. |

## 1. Executive Summary

The TrueGuide sgRNA Search tool is the CRISPR search results experience available under `/crispr/invitrogen/query/*`. The UI is implemented primarily in `thermofisher/magellan-search` using AngularJS modules embedded inside JSP-rendered search results. The search page supports keyword entry, typeahead suggestions, faceted filtering, result rows, scoring badges, price display, add-to-cart/contact-us actions, compare selection, and expandable row sections for Details, Reagents, Controls, and related Antibodies.

The UI is not a standalone single page application. It is a hybrid page:

| Layer | Responsibility |
|---|---|
| JSP server-rendered layer | Emits search result rows, common variables, product fields, `$mangular` JSON payloads, and Angular bindings. |
| AngularJS CRISPR SERP layer | Controls search box, filter updates, load more, row interactions, lazy-loaded modules, pricing, compare, analytics, details, reagents, and controls. |
| Shared services layer | Provides typeahead, filters, search manager, mangular/object config access, pricing library integration, compare panel integration, cart integration, and analytics events. |
| Search/index layer | Supplies CRISPR search documents, fields, sorting, filtering, and product result data used by the UI. |

## 2. Scope

| In Scope | Out of Scope |
|---|---|
| TrueGuide sgRNA Search UI behavior at `/crispr/invitrogen/query/*` | PDP implementation for individual CRISPR products |
| Search form, keyword entry, autocomplete, and navigation | Business ownership or roadmap ownership not present in code |
| Result row layout and actions | Pricing service internals beyond UI integration behavior |
| Price, SKU, package size, add-to-cart, contact-us | Search relevance tuning beyond fields/sort rules visible in supporting repos |
| Compare checkbox and compare panel integration | Unverified live-site browser behavior requiring QA credentials |
| Details, Reagents, Controls, and Antibodies chips | Backend implementation details already covered in backend PRD except where needed for UI dependencies |
| UI acceptance criteria, validation findings, improvements | Invented personas, metrics, or support processes not present in source |

## 3. Source Evidence Summary

| Repository | Source file / module | Evidence used in this PRD |
|---|---|---|
| thermofisher/magellan-search | `src/main/javascript/modules/crispr/serp/modules/search-form/src/components/tf-crispr-search-form/tf-crispr-search-form.controller.js` | Search URL base, search handler, Enter key handler, typeahead call, mobile search class toggle, header search button visibility. |
| thermofisher/magellan-search | `src/main/javascript/modules/crispr/serp/modules/search-form/src/components/tf-crispr-search-form/tf-crispr-search-form.component.js` | Angular component name `tfCrisprSearchForm`, template binding, optional keyword binding. |
| thermofisher/magellan-search | `src/main/javascript/modules/crispr/serp/modules/search-form/src/components/tf-crispr-search-form/tf-crispr-search-form.template.html` | UI labels, placeholder, min typeahead characters, search button, mobile search icon. |
| thermofisher/magellan-search | `src/main/javascript/modules/crispr/serp/modules/search-form/src/services/typeAheadService.js` | Typeahead endpoint, request parameters, JSON parse, empty/invalid response handling, duplicate suppression. |
| thermofisher/magellan-search | `src/main/webapp/WEB-INF/content/search-results/crispr/components/crispr-serp-result-rows.jsp` | Result row fields, badges, compare checkbox, price area, SKU, size, Add to Cart, Contact Us, Details/Reagents/Controls/Antibodies chips. |
| thermofisher/magellan-search | `src/main/javascript/modules/crispr/serp/modules/main/src/controllers/crisprSerpMainController.js` | Page initialization, filter setup, load more, search result update, analytics, lazy embedded search form modal, selected filter URL refresh. |
| thermofisher/magellan-search | `src/main/javascript/modules/crispr/serp/modules/main/src/directives/crispr-result-row/crispr-result-row-controller.js` | Row lifecycle, price loading, package size, scoring badge checks, section toggling, compare checkbox, cart action, contact-us link. |
| thermofisher/magellan-search | `src/main/javascript/modules/crispr/serp/modules/main/src/services/crisprScoringService.js` | TrueGuide and LentiArray top scoring calculation by product subtype, gene, species, and score. |
| thermofisher/magellan-search | `src/main/javascript/modules/crispr/serp/modules/main/src/services/packageDataService.js` | Package size lookup from `$mangular.packageData` by package ID and SKU. |
| thermofisher/magellan-search | `src/main/javascript/modules/crispr/serp/modules/main/src/services/crisprPriceManagerService.js` | Pricing batch behavior, display price rules, Add to Cart eligibility, price header, contact-us URL. |
| thermofisher/magellan-search | `src/main/javascript/modules/crispr/serp/modules/main/src/services/pricingLibraryIntegratorService.js` | Integration with `@thermofisher/magellan-pricing` and pricing configuration values. |
| thermofisher/magellan-search | `src/main/javascript/modules/crispr/serp/modules/main/src/services/compareManagerService.js` | Compare panel lazy loading, selected product model, compare max of 3, disable when only one result. |
| thermofisher/magellan-search | `src/main/javascript/modules/crispr/serp/modules/main/src/services/crisprCartService.js` | Cart payload sent to `$m.addItemToCart`. |
| thermofisher/magellan-search | `src/main/javascript/modules/crispr/serp/modules/main/src/services/crisprAnalyticsService.js` | Onload/search update/add-to-cart analytics events. |
| thermofisher/magellan-search | `src/main/javascript/modules/crispr/serp/modules/main/src/services/urlManagerService.js` | Browser filter URL parsing for Product Type, Gene, and Species. |
| thermofisher/magellan-search | `src/main/javascript/modules/crispr/serp/modules/details/src/components/tf-crispr-view-details/*` | Details expansion payload, design details, reference sequence table, targeted gene table. |
| thermofisher/magellan-search | `src/main/javascript/modules/crispr/serp/modules/reagents-controls/src/components/tf-crispr-reagents-controls/*` | Reagents/controls expandable table, close action, item list, shared product row behavior. |
| thermofisher/magellan-search | `src/main/javascript/modules/crispr/serp/modules/reagents-controls/src/components/tf-crispr-reagents-controls-product/*` | Related reagent/control product name, PDP URL, size select, price, SKU, Add to Cart, Contact Us. |
| thermofisher/tfcom-magellan-search-engine | Solr request handlers and schema evidence | Supporting dependency for CRISPR result fields, status filtering, sorting, facets, and searchable fields. |
| thermofisher/magellan-data-scripts | `setup_CRSPR.pl` | Supporting dependency for CRISPR document fields, SKU subtype mapping, and data validation status. |
| thermofisher/magellan-core | Product subtype/constants evidence | Supporting dependency for CRISPR product type and subtype constants used by UI mappings. |

## 4. Product Overview

| Item | Description |
|---|---|
| Product name | TrueGuide sgRNA Search |
| User-facing category | CRISPR Guide RNA |
| Purpose | Help users search for CRISPR guide RNA products by keyword, gene symbol, Entrez ID, assay ID, and related identifiers, then compare, view details, price, and add eligible products to cart. |
| Primary page URL | `/crispr/invitrogen/query/*` |
| Core UI experience | Search form plus search results list with filters, scoring badges, pricing, compare, and expandable details/reagents/controls. |
| Product owner | Not identified in reviewed source. |
| Business goals observed from behavior | Enable product discovery, expose CRISPR scoring signals, guide users toward compatible reagents and controls, support pricing and cart conversion, and track analytics events. |
| Primary technical owner | Not identified in reviewed source. |

## 5. Users and Stakeholders

| Persona / stakeholder | Need supported by the UI | Source-backed behavior |
|---|---|---|
| Research scientist / buyer | Search for CRISPR guide RNA products by gene, Entrez ID, or assay ID. | Search form placeholder: `Entrez ID, Gene Symbol, Assay ID`; typeahead min input of 2 characters. |
| Research scientist / buyer | Identify better candidates quickly. | Result rows display Top Scoring and High Scoring badges using scoring rules. |
| Research scientist / buyer | Understand product detail before purchase. | Details chip opens design details, reference sequence, and targeted gene sections. |
| Research scientist / buyer | Add eligible products to cart. | Row controller builds cart payload with SKU, assay ID, location `CRISPR_SERP`, and quantity 1. |
| Research scientist / buyer | Find related reagents, controls, and antibodies. | Row chips open Reagents and Controls and link Antibodies using product related antibody URL. |
| Returning customer / procurement user | See customer-specific price messaging when available. | Price header changes from `Price` to `Your Price` when login state is available. |
| Merchandising / product content team | Ensure correct data fields and product subtype labels appear in result rows. | JSP binds product fields including product ID, product subtype, gene symbol, species, package ID, SKU, price, and related links. |
| Analytics / business reporting team | Track search result loads, filter updates, and add-to-cart events. | `crisprAnalyticsService` dispatches `digitalDataLoaded`, `searchResultsUpdated`, and `cartAdd`. |
| UI developer | Maintain AngularJS CRISPR modules and lazy-loaded row submodules. | Modules under `src/main/javascript/modules/crispr/serp/modules/*`. |

## 6. Repository and Module Map

| Repo | UI relevance | Important modules / files |
|---|---|---|
| thermofisher/magellan-search | Primary UI implementation for CRISPR SERP. | `crispr/serp/modules/search-form`; `crispr/serp/modules/main`; `crispr/serp/modules/details`; `crispr/serp/modules/reagents-controls`; JSP rows under `WEB-INF/content/search-results/crispr`. |
| thermofisher/tfcom-magellan-search-engine | Search engine configuration that determines fields, facets, sort order, and query handlers consumed by UI results. | CRISPR request handlers such as `/Search`, `/CRSPR-SiteSrch`, schema fields such as Species, GeneNames, Applications, GeneIDs, ProductSubtype, crisprScore. |
| thermofisher/magellan-core | Shared constants and product subtype definitions used across UI/back-end contracts. | CRISPR product type/subtype constants including `crispr_trueguide`, `crispr_lentiarray`, and display subtype names. |
| thermofisher/magellan-data-scripts | Data preparation rules feeding the CRISPR index. | CRISPR data fields, subtype/SKU mapping, score and coordinate inputs, validation status flags. |

## 7. Confirmed UI Component Inventory

| Component / service | File | Module name | Key functions | UI responsibility |
|---|---|---|---|---|
| Search form component | `tf-crispr-search-form.component.js` | Search form module | `tfCrisprSearchForm` | Wraps the search form template and controller; accepts optional `keyword` binding. |
| Search form controller | `tf-crispr-search-form.controller.js` | Search form module | `getKeywordSuggestion`; `keyPressHandler`; `onTypeAheadChangeHandler`; `onSearchHandler`; `addOrRemoveClassToContainer`; `hideOrShowHeaderSearchButton` | Handles keyword input, typeahead requests, Enter key, search button click, and mobile search container behavior. |
| Search form template | `tf-crispr-search-form.template.html` | Search form module | Template bindings | Displays `CRISPR Guide RNA`, typeahead input, placeholder, search button, and mobile search icon. |
| Typeahead service | `typeAheadService.js` | Search form module | `getSuggestions` | Calls autocomplete endpoint, parses response JSON, rejects invalid data, removes duplicate suggestion values. |
| SERP main controller | `crisprSerpMainController.js` | `tfCrisprMain` | `$onInit`; `loadMore`; `updateSearchResults`; `getSearchResultsMessage`; `searchMultipleTargetsOnClickHandler`; `updateScoringInfo`; `isTopScoring` | Initializes SERP data, filters, search manager, analytics, load more, filter updates, batch search modal, and scoring service bindings. |
| Result row JSP | `crispr-serp-result-rows.jsp` | JSP + Angular directive | `crispr-result-row` attributes and bindings | Emits result row fields and Angular bindings for price, badges, compare, details, reagents, controls, and antibodies. |
| Result row controller | `crispr-result-row-controller.js` | `tfCrisprMain` directive | `$onInit`; `getPricingInfo`; `toggleResultSection`; `isHighScoringProduct`; `getPackageSize`; `addToCart`; `compareCheckBoxOnChangeHandler`; `shouldCheckBoxBeDisabled` | Drives row-level pricing, score badges, section expansion, package size display, cart, contact-us, and compare. |
| Scoring service | `crisprScoringService.js` | `tfCrisprMain` | `updateScoringInfo`; `isTopScoring` | Tracks highest score by product family, gene, and species to identify Top Scoring products. |
| Package data service | `packageDataService.js` | `tfCrisprMain` | `getPackageSize` | Reads `$mangular.packageData` and returns package scale size by package ID and SKU. |
| Price manager | `crisprPriceManagerService.js` | `tfCrisprMain` | `getPricingInfo`; `fetchPricingData`; `getPriceHeader`; `getDisplayPrice`; `isAddToCartEnabled`; `getContactUsLink` | Batches SERP price calls, formats pricing state, controls Add to Cart eligibility, and builds Contact Us link. |
| Pricing integrator | `pricingLibraryIntegratorService.js` | `tfCrisprMain` | `retrievePrice` | Calls `@thermofisher/magellan-pricing` using page config values. |
| Compare manager | `compareManagerService.js` | `tfCrisprMain` | `compareProduct`; `isProductSelected`; `isCheckBoxDisabled`; `updatePricingData` | Lazy-loads compare panel, manages selected products, disables fourth selection, and updates compare pricing. |
| Cart service | `crisprCartService.js` | `tfCrisprMain` | `addToCart` | Sends cart items to global `$m.addItemToCart`. |
| Analytics service | `crisprAnalyticsService.js` | `tfCrisprMain` | `triggerOnload`; `triggerSearchResultUpdated`; `triggerAddToCart` | Updates digitalData and dispatches search/cart analytics events. |
| URL manager | `urlManagerService.js` | `tfCrisprMain` | `captureFilterFromURL`; `parseBrowserFilterUrlToGetFilterStr` | Reads browser filter URL and syncs Product Type, Gene, and Species filters. |
| Details component | `tf-crispr-view-details.component.js` | Details module | `tfCrisprViewDetails` | Lazy-loaded Details section component bound by product ID. |
| Details controller | `tf-crispr-view-details.controller.js` | Details module | `onInit`; `buildPayload`; `close` | Requests details with `{ productType: "crispr", productId }` and exposes design, reference sequence, and targeted gene sections. |
| Details template | `tf-crispr-view-details.template.html` | Details module | Template tables | Shows design details table, reference sequence table, and targeted gene table. |
| Reagents/controls component | `tf-crispr-reagents-controls.component.js` | Reagents/controls module | `tfCrisprReagentsControls` | Shared expandable section for reagents and controls. |
| Reagents/controls controller | `tf-crispr-reagents-controls.controller.js` | Reagents/controls module | `onInit`; `getItemsList`; `close` | Requests list data for feature/product type/product subtype/species and renders items. |
| Reagents/controls data service | `reagentsAndControlsDataService.js` | Reagents/controls module | `getData`; `processReagents`; `processControls`; `makeKey` | Maps CRISPR subtype to `$mangular.reagents` or `$mangular.controls`, includes species-specific and all-species controls. |
| Reagents/controls product component | `tf-crispr-reagents-controls-product.component.js` | Reagents/controls module | `tfCrisprReagentsControlsProduct` | Displays related reagent/control product row. |
| Reagents/controls product controller | `tf-crispr-reagents-controls-product.controller.js` | Reagents/controls module | `onInit`; `getUrlPdp`; `onSizeChange`; `addToCart` | Handles pack-size selection, per-SKU pricing, product PDP link, Add to Cart, and Contact Us. |

## 8. Functional Architecture

### 8.1 Level 1: Page Architecture

```text
User browser
  -> Thermo Fisher CRISPR search URL
    -> Server-rendered JSP search results page
      -> AngularJS CRISPR search form module
      -> AngularJS CRISPR main SERP module
      -> Shared filter/search/data services
      -> Lazy-loaded compare, details, reagents-controls modules
      -> Pricing library, cart integration, analytics events
```

### 8.2 Level 2: UI Module Decomposition

```text
CRISPR SERP UI
  Search Form Module
    - tfCrisprSearchForm component
    - tf-crispr-search-form.controller.js
    - typeAheadService.js

  Main SERP Module: tfCrisprMain
    - crisprSerpMainController.js
    - crispr-result-row-controller.js
    - crisprScoringService.js
    - crisprPriceManagerService.js
    - pricingLibraryIntegratorService.js
    - compareManagerService.js
    - packageDataService.js
    - crisprCartService.js
    - crisprAnalyticsService.js
    - urlManagerService.js

  Lazy Modules
    Details Module
      - tfCrisprViewDetails component
      - detailsDataService dependency
      - design, ref sequence, targeted gene tables
    Reagents/Controls Module
      - tfCrisprReagentsControls component
      - reagentsAndControlsDataService
      - tfCrisprReagentsControlsProduct component

  JSP Integration
    - crispr-serp-result-rows.jsp
    - common mangular variables
    - product model fields from search results
```

### 8.3 Level 3: Search, Render, and Interaction Flow

```text
Search input
  User enters at least 2 characters
    -> tf-type-ahead calls $ctrl.getKeywordSuggestion($keyword)
      -> typeAheadService.getSuggestions("crspr", keyword)
        -> GET /order/genome-database/keywordTypeAutoComplete
          params: keyword, productTypeSelect=crspr
        -> parse jsonAutoComplete
        -> remove duplicate values
        -> return suggestions to typeahead

Search submit
  User clicks search or presses Enter
    -> onSearchHandler()
      -> keyword defaults to empty string when null
      -> window.location.href = /crispr/invitrogen/query/{keyword}
      -> server renders CRISPR SERP
        -> JSP emits product rows and mangular data
        -> crisprSerpMainController initializes filters, search manager, analytics
```

### 8.4 Level 3: Result Row Interaction Flow

```text
Result row render
  crispr-serp-result-rows.jsp emits crispr-result-row
    -> on-init-custom updates scoring map
    -> is-top-score checks scoring map
    -> row controller initializes
      -> compare selected state restored
      -> pricing request registered
      -> row event listeners attached

Row actions
  Price
    -> crisprPriceManagerService batches displayed SKUs
    -> pricingLibraryIntegratorService.retrievePrice()
    -> displayPrice and Add to Cart eligibility set

  Details chip
    -> lazy load details module if needed
    -> tfCrisprViewDetails(productId)
    -> detailsDataService.getDetailsData({ productType: "crispr", productId })
    -> render design details, reference sequence, targeted gene

  Reagents or Controls chip
    -> lazy load reagents-controls module if needed
    -> tfCrisprReagentsControls(feature, productType, productSubType, species)
    -> reagentsAndControlsDataService.getData()
    -> render related product rows with size, price, cart/contact-us

  Compare checkbox
    -> compareManagerService lazy-loads compare panel
    -> selected product { id: sku, name: geneSymbol + ", " + prodId, productId: prodId }
    -> fourth unselected checkbox disabled when three products are already selected
```

## 9. Page and UI Behavior Requirements

| Area | UI requirement | Source evidence |
|---|---|---|
| Search page URL | The CRISPR search form submits to `/crispr/invitrogen/query/{keyword}`. | `searchURLBase = '/crispr/invitrogen/query/'` in `tf-crispr-search-form.controller.js`. |
| Empty keyword handling | If keyword is null at submit time, the UI navigates to `/crispr/invitrogen/query/`. | `onSearchHandler()` assigns empty string when `$ctrl.keyword === null`. |
| Search input label | The visible product type text is `CRISPR Guide RNA`. | `tf-crispr-search-form.template.html`. |
| Search input placeholder | Placeholder is `Entrez ID, Gene Symbol, Assay ID`. | `tf-crispr-search-form.template.html`. |
| Typeahead threshold | Suggestions begin after 2 input characters. | `min-input-char="2"` in search form template. |
| Typeahead product type | CRISPR typeahead requests use product type selector `crspr`. | `getKeywordSuggestion()` calls `typeAheadService.getSuggestions('crspr', keyword)`. |
| Typeahead endpoint | Suggestions are retrieved from `/order/genome-database/keywordTypeAutoComplete`. | `typeAheadService.js`. |
| Typeahead dedupe | Duplicate suggestion values and empty values are removed before resolving suggestions. | `typeAheadService.js`. |
| Enter key | Pressing Enter triggers the same search handler as the search button. | `keyPressHandler()` checks key code 13. |
| Mobile search | The mobile search container class toggles when mobile search icon is clicked. | `addOrRemoveClassToContainer()` and template `ng-class`. |
| Filter drawer interaction | Header mobile search button is hidden while the mobile filters drawer container is present. | `hideOrShowHeaderSearchButton()`. |
| Initial page setup | Main controller initializes search manager, filters manager, listeners, analytics, URL state, and scoring notice template. | `$onInit()` in `crisprSerpMainController.js`. |
| Filter updates | Filter change events fetch new HTML, compile it, replace row container, refresh analytics, and update URL. | `updateSearchResults()` in `crisprSerpMainController.js`. |
| Load more | Load more appends compiled HTML to the result rows container. | `loadMore()` in `crisprSerpMainController.js`. |
| Search result message | Non-batch searches show `Your search for "{keyword}" returned {formattedTotalHits} gRNAs`. Batch searches show `Your search returned {formattedTotalHits} gRNAs`. | `getSearchResultsMessage()`. |
| Browser back/forward | On `popstate`, filters are captured from URL and results are updated. | `setUpListeners()` and `urlManagerService.js`. |

## 10. Result Row Requirements

| Result row section | Required UI behavior | Source evidence |
|---|---|---|
| Product name | Product display name is shown in the result row. | `${product.productName}` in `crispr-serp-result-rows.jsp`. |
| Assay ID | Label is `Assay ID`; value uses `${product.productId}`. | Result row JSP. |
| Gene | Label is `Gene`; value uses `${product.geneSymbol}`. | Result row JSP. |
| Species | Label is `Species`; value uses `${product.speciesName}`. | Result row JSP. |
| Price | Displays loading spinner while price is loading, then HTML-bound display price. | Result row JSP and row controller. |
| Price header | Header is `Price` for anonymous users and `Your Price` for logged-in users, with currency appended when pricing data contains currency. | `crisprPriceManagerService.getPriceHeader()`. |
| SKU / catalog number | Displays `Cat # {partNumber}`. | Result row JSP. |
| Package size | Displays package size returned by `packageDataService.getPackageSize(packageId, sku)` and converts comma to line break. | Result row JSP and row controller `getPackageSize()`. |
| Compare checkbox | Checkbox is bound to row selected state and calls compare manager on change. | Result row JSP and row controller. |
| Add to Cart | Add to Cart button appears when pricing action supports carting; click sends SKU, assay ID, location, and quantity to cart. | Row controller and price manager. |
| Contact Us | Contact Us link appears when product is not add-to-cart eligible. | Row JSP and `getContactUsLink()`. |
| Details chip | Opens a row-level details panel and closes other open row sections. | Result row JSP and row controller. |
| Reagents chip | Opens shared reagents/controls panel with `feature="reagents"`. | Result row JSP and reagents/controls component. |
| Controls chip | Opens shared reagents/controls panel with `feature="controls"`. | Result row JSP and reagents/controls component. |
| Antibodies chip | Links to `${product.relatedAntibodyLink}`. | Result row JSP. |

## 11. Scoring and Badge Rules

| Rule ID | UI rule | Source evidence |
|---|---|---|
| CRISPR-UI-SCORE-001 | Result rows call `updateScoringInfo(productSubType, geneSymbol, speciesName, crisprScore)` on initialization. | `on-init-custom` binding in `crispr-serp-result-rows.jsp`. |
| CRISPR-UI-SCORE-002 | Result rows call `isTopScoring(productSubType, geneSymbol, speciesName, crisprScore)` to determine Top Scoring state. | `is-top-score` binding in result row JSP. |
| CRISPR-UI-SCORE-003 | TrueGuide scoring applies to product subtypes `Invitrogen TrueGuide sgRNA Modified` and `TrueGuide Synthetic sgRNA`. | `crisprScoringService.js`. |
| CRISPR-UI-SCORE-004 | LentiArray scoring applies to product subtype `LentiArray Lentiviral sgRNA`. | `crisprScoringService.js`. |
| CRISPR-UI-SCORE-005 | The highest score is stored per product family using key `geneSymbol + species`. | `crisprScoringService.js`. |
| CRISPR-UI-SCORE-006 | Top Scoring badge displays when row score equals the stored highest score for the row product family, gene, and species. | Row JSP plus `isTopScoringProduct()` in row controller. |
| CRISPR-UI-SCORE-007 | High Scoring badge displays only when product is not Top Scoring and score is greater than 70. | `isHighScoringProduct(score)` in row controller. |
| CRISPR-UI-SCORE-008 | Unknown product subtypes are not treated as top scoring by the UI scoring service. | Default false behavior in `crisprScoringService.js`. |

## 12. Pricing, Availability, Cart, and Contact Rules

| Rule ID | UI rule | Source evidence |
|---|---|---|
| CRISPR-UI-PRICE-001 | Each displayed result row registers a pricing promise keyed by product ID and SKU. | `crisprPriceManagerService.getPricingInfo(sku, productId)`. |
| CRISPR-UI-PRICE-002 | Pricing is fetched once the number of registered row pricing promises equals the displayed result count. | `Object.keys(serpPromises).length === searchManagerService.getDisplayCount()`. |
| CRISPR-UI-PRICE-003 | Duplicate SKUs are de-duplicated before pricing retrieval. | `getSkus()` in price manager. |
| CRISPR-UI-PRICE-004 | Pricing calls are delegated to `@thermofisher/magellan-pricing`. | `pricingLibraryIntegratorService.js`. |
| CRISPR-UI-PRICE-005 | Price displays final price when action is `Add To Cart` or `Price View Not Orderable`. | `getDisplayPrice()`. |
| CRISPR-UI-PRICE-006 | Price displays `Price not available` when pricing action is `No Price`. | `getDisplayPrice()`. |
| CRISPR-UI-PRICE-007 | Price displays `Not orderable online` when the pricing message contains `not entitled`. | `getDisplayPrice()`. |
| CRISPR-UI-PRICE-008 | If pricing service errors, row price displays `View price in cart`. | `getDisplayPrice()`. |
| CRISPR-UI-PRICE-009 | Add to Cart is disabled while price is loading. | `ng-disabled="$ctrl.isPriceLoading"` in result row JSP. |
| CRISPR-UI-PRICE-010 | Add to Cart remains available only when pricing action is allowed by `isAddToCartEnabled()`. | Price manager and row controller. |
| CRISPR-UI-PRICE-011 | Contact Us link is `/us/en/home/technical-resources/contact-us.{sku}.html?supportType=SL`. | `getContactUsLink(sku)`. |
| CRISPR-UI-CART-001 | Result row cart payload uses `sku`, `aid` as product ID, `loc` as `CRISPR_SERP`, and quantity 1. | `addToCart()` in row controller. |
| CRISPR-UI-CART-002 | Cart integration calls global `$m.addItemToCart(cartItems)`. | `crisprCartService.js`. |
| CRISPR-UI-CART-003 | Reagents and controls Add to Cart uses selected SKU, quantity 1, section-specific location, selected pack size, and product name for analytics. | `tf-crispr-reagents-controls-product.controller.js`. |

## 13. Compare Feature Rules

| Rule ID | UI rule | Source evidence |
|---|---|---|
| CRISPR-UI-COMPARE-001 | The compare module is lazy-loaded from `serp-compare/src/index` only when a compare action requires it. | `compareManagerService.loadModule()`. |
| CRISPR-UI-COMPARE-002 | Compare panel product type is set from `$mangular.productType`. | `compareProductsService.setProductType(mangularService.getValue('productType'))`. |
| CRISPR-UI-COMPARE-003 | Compare product model uses `{ id: sku, name: geneSymbol + ", " + prodId, productId: prodId }`. | `compareProduct()` and `getComparePanelLabel()`. |
| CRISPR-UI-COMPARE-004 | Compare panel is meaningful only when total result count is greater than 1. | `shouldDisplayPanel()` returns `searchManagerService.getTotalCount() > 1`. |
| CRISPR-UI-COMPARE-005 | Compare checkbox is disabled when total result count is 1. | `shouldCheckBoxBeDisabled()`. |
| CRISPR-UI-COMPARE-006 | A fourth unselected result checkbox is disabled once 3 products are already selected. | `isCheckBoxDisabled()` checks selected keys length equals 3. |
| CRISPR-UI-COMPARE-007 | When a product is removed from compare panel, matching result row checkbox is reset. | Row controller listens for `tf-compare-product-removed`. |
| CRISPR-UI-COMPARE-008 | Browser `pageshow` resets compare checkboxes in result rows. | `resetCheckboxes()` in main controller. |
| CRISPR-UI-COMPARE-009 | Compare pricing is fetched through the same CRISPR price manager and displayed using compare-specific display formatting. | `compareManagerService.updatePricingData()` and `getDisplayPriceForCompare()`. |

## 14. Details, Reagents, Controls, and Antibodies Rules

| Section | Rule | Source evidence |
|---|---|---|
| Details | Details panel opens through `tf-crispr-view-details` with `product-id` binding. | Result row JSP. |
| Details | Details module is lazy-loaded before opening if not already loaded. | `toggleResultSection('details')` in row controller. |
| Details | Details payload uses `{ productType: "crispr", productId }`. | `buildPayload()` in details controller. |
| Details | Details view renders Design, Reference Sequence, and Targeted Gene sections. | `tf-crispr-view-details.template.html`. |
| Details | Reference Sequence table renders dynamic headers and rows. | Details template. |
| Details | Targeted Gene rows may display outbound links when `hasExternalLink` is true. | Details template. |
| Reagents | Reagents chip opens `tf-crispr-reagents-controls` with `feature="reagents"`. | Result row JSP. |
| Controls | Controls chip opens `tf-crispr-reagents-controls` with `feature="controls"`. | Result row JSP. |
| Reagents/Controls | Reagents/controls module is lazy-loaded before opening if not already loaded. | Row controller. |
| Reagents/Controls | Only one of details, reagents, or controls can be open in a row at a time. | `toggleSection()` closes other sections. |
| Reagents/Controls | Section header columns are Product Name, Size, Price, and actions. | `tf-crispr-reagents-controls.template.html`. |
| Reagents/Controls | Each related product row links to `urlPrefix + selectedProduct.sku`. | `getUrlPdp()`. |
| Reagents/Controls | Multi-size related products render a size selector; single-size products render static size text. | Product template and `isMultiSize()`. |
| Reagents/Controls | Changing selected pack size refetches price for the selected SKU. | `onSizeChange()` and `updatePricingInfo()`. |
| Reagents/Controls | Add to Cart sends source location as `Reagents section` or `Controls section`. | Related product controller. |
| Antibodies | Antibodies chip is a direct link to product related antibody URL. | Result row JSP. |

## 15. Reagents and Controls Data Mapping Rules

| Rule ID | UI rule | Source evidence |
|---|---|---|
| CRISPR-UI-RC-001 | Product type `CRSPR` maps to key prefix `crispr`. | `productTypeMap` in `reagentsAndControlsDataService.js`. |
| CRISPR-UI-RC-002 | Product subtype `Invitrogen TrueGuide sgRNA Modified` maps to `crispr_trueguide`. | `productSubTypeMap`. |
| CRISPR-UI-RC-003 | Product subtype `TrueGuide Synthetic sgRNA` maps to `crispr_trueguide`. | `productSubTypeMap`. |
| CRISPR-UI-RC-004 | Product subtype `LentiArray Lentiviral sgRNA` maps to `crispr_lentiarray`. | `productSubTypeMap`. |
| CRISPR-UI-RC-005 | Data key format is `{mapped product type}-{mapped product subtype}`. | `makeKey()`. |
| CRISPR-UI-RC-006 | Reagents are read from `$mangular.reagents[key].reagentsDetails`. | `processReagents()`. |
| CRISPR-UI-RC-007 | Controls are read from `$mangular.controls[key].controlsDetails`. | `processControls()`. |
| CRISPR-UI-RC-008 | Controls lookup lowercases species before matching species-specific controls. | `species.toLowerCase()` in `processControls()`. |
| CRISPR-UI-RC-009 | Controls include controls for the specific species plus controls under `all`. | `processControls()`. |
| CRISPR-UI-RC-010 | Invalid product type rejects with `INVALID_PRODUCT_TYPE`. | `makeKey()`. |
| CRISPR-UI-RC-011 | Invalid product subtype rejects with `INVALID_PRODUCT_SUBTYPE`. | `makeKey()`. |
| CRISPR-UI-RC-012 | Invalid feature rejects with `INVALID_FEATURE`. | `getDataFromMangular()`. |

## 16. UI Column and Field Requirements

The source uses a result-row/card layout rather than a single pure HTML results table. On large screens, the row behaves like a structured table; on small screens, labels become visible inside each row.

| UI column / field | Source binding | Rule / expected behavior |
|---|---|---|
| Product | `${product.productName}` | Display product name returned by the CRISPR result model. |
| Assay ID | `${product.productId}` | Display product ID under the `Assay ID` label. |
| Gene | `${product.geneSymbol}` | Display gene symbol. |
| Species | `${product.speciesName}` | Display species name. |
| Price / Your Price | `$ctrl.getPriceHeader()` and `$ctrl.displayPrice` | Header depends on login state and currency; price depends on pricing action or error state. |
| Catalog number | `${product.partNumber}` | Display as `Cat # {partNumber}`. |
| Size | `$ctrl.getPackageSize()` | Display scale size for package ID and SKU; comma in size is converted to line break. |
| Compare | `$ctrl.isCheckboxChecked` | Checkbox selects/removes product from compare panel, subject to compare limits. |
| Cart / Contact | `$ctrl.isAddToCart()` and `$ctrl.getContactUsLink()` | Show Add to Cart when eligible; otherwise show Contact Us. |
| Details chip | `toggleResultSection('details')` | Opens details section and closes other open row sections. |
| Reagents chip | `toggleResultSection('reagents')` | Opens reagents section using product type, subtype, and species. |
| Controls chip | `toggleResultSection('controls')` | Opens controls section using product type, subtype, and species. |
| Antibodies chip | `${product.relatedAntibodyLink}` | Direct link to antibody search/gene page for the product gene/species. |
| Top Scoring badge | `$ctrl.isTopScoringProduct()` | Display only for top score by product family/gene/species. |
| High Scoring badge | `$ctrl.isHighScoringProduct(crisprScore)` | Display only when not top scoring and score is greater than 70. |

## 17. API and Integration Contracts

| Integration | Caller | Request / payload | UI handling |
|---|---|---|---|
| Search route | Search form controller | Browser navigation to `/crispr/invitrogen/query/{keyword}` | Full page route update; server returns CRISPR SERP. |
| Typeahead API | `typeAheadService.getSuggestions(productType, keyword)` | GET `/order/genome-database/keywordTypeAutoComplete` with `keyword` and `productTypeSelect=crspr` | Parse `jsonAutoComplete`, require `response.docs`, remove duplicate non-empty values. |
| Search manager | `crisprSerpMainController` | `searchManagerService.init()`, `getNewData()`, `loadMore()`, `generateUrl()` | Compile returned HTML and replace/append rows. |
| Mangular data | Multiple UI services | `keyword`, `totalHits`, `formattedTotalHits`, `filters`, `searchType`, `packageData`, `reagents`, `controls`, `productType` | Drives initialization, display text, filters, package size, related items, and compare product type. |
| Pricing library | `pricingLibraryIntegratorService.retrievePrice(skus)` | SKU CSV for result rows; single SKU array for related products | Uses config values such as cache max age, protocol, Comergent host, Magellan pricing API path, timeout, login state, and build date. |
| Cart | `crisprCartService.addToCart()` | `[{ sku, aid, loc, qty, blockSeachEvent: true }]` | Calls global `$m.addItemToCart(cartItems)`. |
| Compare panel | `compareManagerService` | Lazy load `serp-compare/src/index`; product `{ id, name, productId }` | Updates shared compare panel, caps selections at 3. |
| Details data | `tf-crispr-view-details.controller.js` | `{ productType: "crispr", productId }` | Renders design, reference sequence, and targeted gene sections after promise resolves. |
| Analytics onload | `crisprAnalyticsService.triggerOnload()` | `digitalData.search` with total results, keyword, type `Crispr`, filters, SID | Sets page type `crispr search results` and dispatches `digitalDataLoaded` if delayed. |
| Analytics result update | `triggerSearchResultUpdated()` | Custom event `searchResultsUpdated` with total results, keyword, filters, SID | Sent after filter-driven result update. |
| Analytics add-to-cart | `triggerAddToCart()` | Custom event `cartAdd` with product catalog number, category, design ID, line name, price, quantity, title, UOM | Sent after row or related product Add to Cart. |

## 18. Supporting Search and Data Rules

These are supporting rules from backend/search/data repos that directly affect UI behavior. They should be validated in backend ownership, but UI developers need them because result fields and filters depend on them.

| Area | Supporting rule | UI impact |
|---|---|---|
| Product family | CRISPR product type is represented as `CRSPR` or `crispr` depending on layer. | UI mapping services must preserve correct product type casing for each integration. |
| Product subtype | TrueGuide subtypes include `Invitrogen TrueGuide sgRNA Modified` and `TrueGuide Synthetic sgRNA`; LentiArray subtype is `LentiArray Lentiviral sgRNA`. | Scoring and reagents/controls mapping depend on exact subtype strings. |
| Search route | CRISPR SERP URL base is configured as `/crispr/invitrogen/query/`. | UI search navigation must match this route. |
| Solr collection / fields | CRISPR fields include Species, GeneNames, Applications, GeneIDs, GeneAliases, crisprScore, partnumber, PrimaryGeneSymbolCaps. | UI result row and filters must use available indexed fields. |
| Sorting | Search engine configuration sorts CRISPR results by primary gene symbol ascending, CRISPR score descending, and LentiViral subtype term frequency ascending. | UI scoring badges should be tested against actual row order because scoring is computed as rows initialize. |
| Status filtering | Search handlers exclude documents where `SearchStatus:0`. | UI should not expect hidden/inactive rows. |
| Data scripts | CRISPR data preparation maps SKUs and IDs for sgRNA, crRNA, and lentiviral products. | UI subtype-specific behavior must be regression-tested when data source introduces or changes subtype strings. |

## 19. Acceptance Criteria

| ID | Acceptance criterion | Validation approach |
|---|---|---|
| AC-001 | The search page displays a CRISPR Guide RNA search form with placeholder `Entrez ID, Gene Symbol, Assay ID`. | UI render test for `/crispr/invitrogen/query/*`. |
| AC-002 | Typeahead calls autocomplete only after 2 characters and sends `productTypeSelect=crspr`. | Unit test `typeAheadService.getSuggestions`; network mock. |
| AC-003 | Duplicate typeahead suggestions are removed and empty suggestion values are not displayed. | Unit test with duplicate `response.docs`. |
| AC-004 | Pressing Enter and clicking the search button navigate to `/crispr/invitrogen/query/{keyword}`. | Controller unit test and browser test. |
| AC-005 | Keywords with spaces or special characters do not break navigation. | Browser test; improvement recommended to encode keyword. |
| AC-006 | Result rows display product, assay ID, gene, species, price, catalog number, size, compare, and cart/contact actions. | DOM test against server-rendered row fixture. |
| AC-007 | Price spinner appears while pricing is loading and final display message follows pricing action mapping. | Unit test price manager with action permutations. |
| AC-008 | Add to Cart is disabled while pricing is loading. | DOM test for disabled state. |
| AC-009 | If a product is not add-to-cart eligible, Contact Us is displayed using the SKU-specific contact-us URL. | Unit test price action and link generation. |
| AC-010 | Top Scoring badge appears for highest score per TrueGuide product family, gene, and species. | Scoring service unit test. |
| AC-011 | High Scoring badge appears when a non-top product has score greater than 70. | Row controller unit test. |
| AC-012 | Details, Reagents, and Controls chips are mutually exclusive within a row. | Row controller test for `toggleSection()`. |
| AC-013 | Details section renders design details, reference sequence, and targeted gene sections after data loads. | Component test with mocked details data. |
| AC-014 | Reagents and controls render Product Name, Size, Price, and action columns. | Component DOM test. |
| AC-015 | Controls combine species-specific products with `all` controls. | Unit test `reagentsAndControlsDataService.processControls`. |
| AC-016 | Compare checkbox is disabled when there is only one result. | Row controller test with search manager count 1. |
| AC-017 | Compare allows up to 3 selected products and disables fourth unselected checkbox. | Compare manager unit test. |
| AC-018 | Filter changes replace current result rows, reset pricing promises, update analytics, and regenerate URL. | Integration test around `updateSearchResults()`. |
| AC-019 | Load More appends additional compiled result rows instead of replacing the current list. | Integration test around `loadMore()`. |
| AC-020 | Onload and filter updates send the expected digitalData/custom events. | Analytics mock test. |

## 20. Validation Findings

| Finding | Severity | Evidence | Impact | Recommendation |
|---|---|---|---|---|
| Search keyword is concatenated into URL without visible encoding. | Medium | `onSearchHandler()` builds `searchURLBase + $ctrl.keyword`. | Keywords with spaces, slashes, ampersands, or special characters may produce fragile URLs. | Apply `encodeURIComponent` or a shared route builder before navigation. |
| `keyPressHandler()` relies on global `event` rather than an explicit handler argument. | Medium | Function references `event.which` OR `event.keyCode`; template calls `on-key-press="$ctrl.keyPressHandler($event)"`. | Unit tests and strict browser contexts may fail or behave inconsistently. | Change function signature to `keyPressHandler(event)` and use the passed event. |
| Mobile container property is misspelled as `mobileConatinerClass`. | Low | Controller and template use `mobileConatinerClass`. | Works because both sides match, but increases maintenance risk. | Introduce correctly spelled alias or rename with regression test. |
| Header search visibility expression is difficult to read and depends on coercion. | Low | `return !angular.element('.tf-filters-drawer-mobile-ctnr').length > 0`. | Behavior works by boolean/number coercion but is fragile and confusing. | Replace with `return angular.element(...).length === 0`. |
| Top scoring key uses `geneSymbol + species` without a separator. | Medium | `crisprScoringService.js`. | Rare key collisions are possible if concatenated values overlap. | Use a delimited or structured key such as `${geneSymbol}::${species}`. |
| Scoring comparison does not visibly coerce score to number. | Medium | `score > crisprScoringMap...` and score passed from JSP as string literal. | Numeric comparisons can become fragile if score is not consistently typed. | Coerce scores with `Number(score)` and handle invalid values. |
| Reagents/controls data processing lacks defensive guards for missing `$mangular` data or missing keys. | Medium | `processReagents()` and `processControls()` access `data[key]` directly. | Missing payload can cause runtime errors rather than empty section messaging. | Guard missing data/key and render an empty state. |
| Reagents/controls product subtype map does not include crRNA subtype. | Medium | `productSubTypeMap` includes two TrueGuide sgRNA strings and LentiArray only. | If crRNA rows appear on the same experience, Reagents/Controls would reject subtype. | Confirm intended scope; add explicit map if crRNA is supported. |
| Typeahead and package data JSON parse failures reject promises but visible user-facing fallback is not evident. | Low | `typeAheadService.js`; `packageDataService.js`. | User may see no suggestions or blank size without clear error state. | Add graceful empty-state behavior and logging. |
| Row Add to Cart button has static `disabled` attribute in JSP along with `ng-disabled`. | Medium | `<button ... ng-disabled="$ctrl.isPriceLoading" ... disabled>`. | Static disabled may keep button disabled after Angular state changes depending on browser/Angular handling. | Remove static `disabled` and rely on `ng-disabled` after verifying behavior. |
| Pricing batch fetch waits for registered row count to equal display count. | Medium | `getPricingInfo()` compares promise count to `searchManagerService.getDisplayCount()`. | Missing row init or mismatch in display count can prevent pricing from resolving. | Add timeout/fallback or trigger pricing after rows are linked. |
| Browser filter parser handles Product Type, Gene, and Species only. | Low | `filterParserMapping` in `urlManagerService.js`. | Additional filters require parser changes to support back/forward URL sync. | Keep mapping in sync with CRISPR filter set. |

## 21. Areas for Improvement

| Area | Improvement | Expected benefit |
|---|---|---|
| URL safety | Encode search keyword before setting `window.location.href`. | More reliable navigation for special characters and copied search terms. |
| Event handling | Pass event into `keyPressHandler(event)`. | Better testability and browser compatibility. |
| Scoring service | Use numeric score coercion and structured keys. | More reliable Top Scoring behavior. |
| Reagents/controls robustness | Add null guards and empty states for missing `$mangular.reagents` or `$mangular.controls`. | Avoid row expansion errors and give users clear feedback. |
| Product subtype coverage | Confirm whether TrueGuide crRNA should appear on this search experience; if yes, add mapping and tests. | Prevent missing related sections for supported subtype rows. |
| Pricing resilience | Add diagnostic logging and fallback behavior when the number of initialized rows does not match display count. | Reduces risk of perpetual price loading. |
| Compare UX | Surface selected count and max selection feedback in a visible/helpful way if not already handled by compare panel. | Reduces user confusion when fourth checkbox is disabled. |
| Test coverage | Add focused unit tests for typeahead parse/dedupe, scoring, price display, compare limit, section toggling, and reagents/controls mapping. | Protects core search conversion flows. |
| Accessibility | Replace SVG-only controls with accessible labels or `aria-label`, especially search, close, and compare controls. | Improves keyboard and screen-reader usability. |
| Observability | Track typeahead errors, pricing failures, and empty reagents/controls payloads. | Better support and faster incident diagnosis. |

## 22. UI Test Matrix

| Test case | Scenario | Expected result |
|---|---|---|
| TC-001 | Open `/crispr/invitrogen/query/*`. | Search form renders with CRISPR Guide RNA label and placeholder. |
| TC-002 | Enter one character in search box. | Typeahead should not request suggestions. |
| TC-003 | Enter two characters in search box. | Typeahead sends autocomplete request with `productTypeSelect=crspr`. |
| TC-004 | Autocomplete returns duplicate values. | Duplicates are removed from suggestion list. |
| TC-005 | Press Enter after entering a keyword. | Browser navigates to `/crispr/invitrogen/query/{keyword}`. |
| TC-006 | Click search button with null keyword. | Browser navigates to `/crispr/invitrogen/query/`. |
| TC-007 | Filter Species, Gene, or Product Type. | Results are refreshed, price promises reset, analytics update event fires, URL updates. |
| TC-008 | Click browser back after filter update. | Filters are restored from URL and results refresh. |
| TC-009 | Click Load More. | Additional rows append under existing rows. |
| TC-010 | Result row pricing returns Add To Cart. | Final price displays and Add to Cart becomes available. |
| TC-011 | Result row pricing returns No Price. | Price displays `Price not available`. |
| TC-012 | Result row pricing returns not-entitled message. | Price displays `Not orderable online`; Contact Us may replace Add to Cart when action is not allowed. |
| TC-013 | Pricing service fails. | Price displays `View price in cart`. |
| TC-014 | Result count is 1. | Compare checkbox is disabled. |
| TC-015 | Three products are already selected. | Fourth unselected compare checkbox is disabled. |
| TC-016 | Remove a product from compare panel. | Matching result row checkbox is unchecked. |
| TC-017 | Open Details chip. | Details module loads and displays design details, reference sequence, and targeted gene. |
| TC-018 | Open Reagents chip. | Reagents panel opens with product name, size, price, and action columns. |
| TC-019 | Open Controls chip for species-specific row. | Controls include species-specific controls plus all-species controls. |
| TC-020 | Select another size for a related product. | Price refreshes for selected SKU and Add to Cart uses selected SKU. |
| TC-021 | Click Antibodies chip. | Browser navigates to product related antibody link. |
| TC-022 | Add result row product to cart. | `$m.addItemToCart` receives SKU, aid/product ID, location `CRISPR_SERP`, quantity 1. |
| TC-023 | Add related reagent/control to cart. | `$m.addItemToCart` receives selected SKU and section-specific location; analytics includes selected UOM. |
| TC-024 | Product has highest score in TrueGuide gene/species group. | Top Scoring badge displays. |
| TC-025 | Product score is greater than 70 but not top scoring. | High Scoring badge displays. |

## 23. Developer Notes

| Topic | Note |
|---|---|
| Framework style | The CRISPR SERP UI uses AngularJS modules and JSP-rendered Angular directives/components. |
| Lazy loading | Embedded form, compare panel, details, and reagents/controls are lazy-loaded through dynamic import and `$ocLazyLoad`. |
| Data bootstrap | `$mangular` is a major contract. Missing or malformed `$mangular` values can break UI services. |
| Search result refresh | Filter updates return HTML, not JSON-only data; Angular compiles the returned HTML and injects it into the result rows container. |
| Pricing | Result-row pricing is batched; related product pricing is per selected SKU. |
| Compare limit | Compare selection is limited to 3 selected products. |
| Business language caveat | Product owner, explicit KPI targets, and operational SLA are not visible in reviewed source and should be filled by product/business owners. |

## 24. Open Questions

| Question | Why it matters |
|---|---|
| Should TrueGuide crRNA products appear in this specific `/crispr/invitrogen/query/*` UI flow? | UI reagents/controls mapping currently does not include crRNA subtype strings. |
| What is the intended max keyword length for this page? | Backend config references max keyword length in prior evidence, but UI source does not visibly enforce it. |
| Should empty keyword search be allowed intentionally? | Current source navigates to the base query route when keyword is null. |
| Should Add to Cart be statically disabled before pricing, or should `ng-disabled` fully control it? | The result row button has both a static `disabled` attribute and Angular disabled binding. |
| What are the required analytics field names for compare actions? | Add-to-cart and search analytics are visible; compare analytics were not confirmed in the reviewed UI source. |
