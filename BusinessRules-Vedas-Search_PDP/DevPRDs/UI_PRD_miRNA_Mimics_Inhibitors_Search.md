# UI Developer PRD - miRNA Mimics and Inhibitors Search

| Field | Details |
|---|---|
| Product / Tool | miRNA Mimics and Inhibitors Search |
| Tool URL | https://www.thermofisher.com/order/rnai/miRNA/result?keyword=* |
| Audience | UI developers, QA engineers, product owners, business analysts |
| Document Type | UI rules document / developer PRD |
| Source Date | 2026-07-31 |
| Primary Verified Repo | thermofisher/magellan-search |
| Related Repos Reviewed for Orientation | thermofisher/tfcom-magellan-product-service, thermofisher/tfcom-magellan-etools, thermofisher/magellan-core |
| Repo Requiring Follow-up | thermofisher/magellan-data-scripts metadata fetch returned a transient connector error during this review |

## 1. Document Purpose

| Item | Description |
|---|---|
| Purpose | Capture the UI-facing rules, component behavior, workflows, and validation observations for the miRNA Mimics and Inhibitors Search tool. |
| Developer Focus | Identify source repositories, Angular modules, component names, service names, key functions, UI conditions, API calls, and add-to-cart behavior. |
| Business Focus | Explain how search results expose assay details, related mimics/inhibitors, pricing, availability, related reagents, and supporting assay information. |
| Scope | Search result UI behavior for miRNA assays and the Mimics/Inhibitors tab shown from the miRNA result card. |
| Out of Scope | Backend implementation details beyond the APIs invoked by the UI; merchandising decisions not visible in the inspected UI source. |

## 2. Source Evidence and Review Boundary

| Evidence Type | Repo | File / Module | What Was Verified |
|---|---|---|---|
| UI search result component | thermofisher/magellan-search | `src/main/javascript/modules/elcano/main/src/components/mirna-search-result/mirna-search-result.component.js` | Main Angular component, bindings, tab logic, service calls, pricing rules, add-to-cart payload logic, popup text, analytics hooks. |
| UI search result template | thermofisher/magellan-search | `src/main/javascript/modules/elcano/main/src/components/mirna-search-result/mirna-search-result.template.html` | Result card layout, tab labels, field visibility, details panel, commerce card, Bioz component, tab child components. |
| Mimics/Inhibitors child component | thermofisher/magellan-search | `src/main/javascript/modules/elcano/main/src/components/mirna-search-result/components/mirna-mimics-inhibitors-single-tube/mirna-mimics-inhibitors-single-tube.component.js` | Child table row behavior, species limit, size dropdown, price calls, login refresh, add-to-cart trigger. |
| Mimics/Inhibitors child template | thermofisher/magellan-search | `src/main/javascript/modules/elcano/main/src/components/mirna-search-result/components/mirna-mimics-inhibitors-single-tube/mirna-mimics-inhibitors-single-tube.template.html` | Child row columns, assay link, species show more/less, size selector, price labels, login prompt, add-to-cart button. |
| Mimics/Inhibitors service | thermofisher/magellan-search | `src/main/javascript/modules/elcano/main/src/services/mimicsInhibitorsService.js` | API endpoint and request parameter used to fetch related mimic/inhibitor products. |
| Related services | thermofisher/magellan-search | `viewDetailsService.js`, `matureMirnaService.js`, `priMirnaService.js`, `relatedReagentsService.js`, `pricingService.js` | API endpoints used by detail, mature miRNA, pri-miRNA, related reagent, and price workflows. |
| Module registration | thermofisher/magellan-search | `src/main/javascript/modules/elcano/main/src/index.js` | Angular module registrations for UI components and services. |
| Related repo orientation | thermofisher/tfcom-magellan-product-service | Repository metadata | Verified repo access and default branch, but no UI-specific source file was inspected for this PRD. |
| Related repo orientation | thermofisher/tfcom-magellan-etools | Repository metadata | Verified repo access and default branch, but no UI-specific source file was inspected for this PRD. |
| Related repo orientation | thermofisher/magellan-core | Repository metadata | Verified repo access and default branch, but no UI-specific source file was inspected for this PRD. |
| Related repo orientation | thermofisher/magellan-data-scripts | Repository metadata | Metadata fetch failed during this review; validate data-script ownership separately. |

## 3. Product Overview

| Area | Details |
|---|---|
| Product Name | miRNA Mimics and Inhibitors Search |
| Primary Purpose | Help users discover miRNA-related assays and related mimic/inhibitor products, compare product details, check size and price, and add eligible products to cart. |
| User Entry Point | `/order/rnai/miRNA/result?keyword=*` |
| Main UI Surface | Search result cards rendered by `appMirnaSearchResult`. |
| Related UI Surface | Mimics/Inhibitors tab rendered through `appMirnaMimicsInhibitorsSingleTube`. |
| Business Goal | Surface relevant miRNA assay results and related mimic/inhibitor product options while preserving commerce rules for price visibility, login, availability, and add to cart. |
| Developer Goal | Maintain predictable tab visibility, service orchestration, SKU selection, pricing refresh, and cart payload behavior across miRNA assay subtypes. |

## 4. Users and Stakeholders

| Persona / Stakeholder | Need | UI Implication |
|---|---|---|
| Research scientist | Find miRNA assays and related mimic/inhibitor products quickly. | Result card must expose product ID, assay name, species, miRBase details, related tabs, and supporting details without requiring multiple searches. |
| Procurement / buyer | Check orderability, availability, size, list price, user price, and add-to-cart eligibility. | Commerce panel must show availability, size selector, price labels, login prompt, and Add to cart only when rules allow. |
| Product owner | Ensure the search experience supports miRNA assay discovery and related product cross-sell. | Tab visibility and related product sections must map to backend flags such as `hasMI`, `hasMature`, and `hasPri`. |
| UI developer | Understand module boundaries and function-level behavior. | PRD identifies Angular component, template, services, key functions, endpoints, and validation gaps. |
| QA engineer | Build test cases for result display, tabs, pricing, login, add-to-cart, and related products. | Acceptance criteria and validation matrix provide testable conditions. |
| Analytics stakeholder | Track result interactions and commerce actions. | UI must preserve Omniture calls for tab opening, PDP link clicks, map usage, size change, and add-to-cart. |

## 5. Repository and Module Map

| Repo | Role in This PRD | Confirmed Files / Modules | UI Relevance |
|---|---|---|---|
| thermofisher/magellan-search | Primary UI implementation repo | `advanced-taqman-search` Angular module; `mirna-search-result` component; miRNA child components; UI services | Owns the inspected search result UI behavior for the tool. |
| thermofisher/tfcom-magellan-product-service | Related service repo | Repo metadata verified only | Potential product/pricing/catalog dependency; no UI module verified in this pass. |
| thermofisher/tfcom-magellan-etools | Related eTools repo | Repo metadata verified only | Potential shared tool/service dependency; no UI module verified in this pass. |
| thermofisher/magellan-data-scripts | Related data scripts repo | Metadata fetch failed | Potential data ingestion or transformation dependency; validate separately. |
| thermofisher/magellan-core | Related shared/core repo | Repo metadata verified only | Potential shared constants/models dependency; no UI module verified in this pass. |

## 6. Confirmed UI Components and Services

| Component / Service | Type | File | Main Responsibility |
|---|---|---|---|
| `appMirnaSearchResult` | Angular component | `mirna-search-result.component.js` | Render each miRNA result, manage tabs, price refresh, commerce state, related products, and analytics events. |
| `mirna-search-result.template.html` | Angular template | `mirna-search-result.template.html` | Render result card, product links, product type, details tabs, commerce panel, Add to cart, Bioz block. |
| `appMirnaMimicsInhibitorsSingleTube` | Angular child component | `mirna-mimics-inhibitors-single-tube.component.js` | Render each mimic/inhibitor related product row, handle species expansion, SKU selection, price refresh, and Add to cart trigger. |
| `mirna-mimics-inhibitors-single-tube.template.html` | Angular child template | `mirna-mimics-inhibitors-single-tube.template.html` | Render columns for Mimic/Inhibitor, Assay ID, Species, Size, Price, Your Price, login prompt, and Add to cart. |
| `mimicsInhibitorsService` | Angular factory | `mimicsInhibitorsService.js` | Fetch mimic/inhibitor products from `/order/genome-database/mirnaAssayDropDowns` using `mirnainhib`. |
| `viewDetailsService` | Angular factory | `viewDetailsService.js` | Fetch assay details from `/order/genome-database/viewAssayDetails` and array details from `/order/genome-database/viewArrayDetails`. |
| `matureMirnaService` | Angular factory | `matureMirnaService.js` | Fetch mature miRNA assays from `/order/genome-database/mirnaAssayDropDowns` using `mirnamature`. |
| `priMirnaService` | Angular factory | `priMirnaService.js` | Fetch pri-miRNA assays from `/order/genome-database/mirnaAssayDropDowns` using `mirnaprimary`. |
| `relatedReagentsService` | Angular factory | `relatedReagentsService.js` | Fetch related reagents from `/order/genome-database/relatedReagents`. |
| `pricingService` | Angular factory | `pricingService.js` | Fetch list or user price from `/order/genome-database/price`. |
| `alignMapModuleManager` | Angular service dependency | Injected into `appMirnaSearchResult` | Lazy-load alignment map module for eligible assay subtypes. |
| `gsdOmnitureService` | Angular service dependency | Injected into `appMirnaSearchResult` | Track result abandonment, size changes, tab opens, PDP clicks, map usage, and Add to cart. |
| `sharedTaqManService` | Angular service dependency | Injected into main and child components | Share product type, login status, format, availability text, currency display, and trusted HTML helpers. |

## 7. Functional Architecture

| Level | Layer | Responsibility | Source Evidence |
|---|---|---|---|
| 1 | Browser route | User lands on miRNA search result URL with keyword query. | Tool URL supplied by user. |
| 1 | Search result page shell | Loads the advanced TaqMan / Elcano Angular module. | `advanced-taqman-search` registration in `index.js`. |
| 1 | Result card component | Renders each miRNA result card and its tabbed sections. | `appMirnaSearchResult`. |
| 2 | Main result template | Shows product ID, catalog number, assay name, species, mirBase data, product type, and commerce panel. | `mirna-search-result.template.html`. |
| 2 | Tab controller | Opens Details, Mimics/Inhibitors, Mature miRNA Assays, Pri-miRNA Assays, Reagents, Assay map, and Arrays based on data flags. | `setTab`, `isSet`, `showAlignmentMap`, `isRelatedArraysExist`. |
| 2 | Child tab components | Render related product rows and handle per-row SKU/pricing/cart interactions. | `appMirnaMimicsInhibitorsSingleTube`, `appMatureMirnaAssays`, `appMirnaPriMirnaSingleTube`, `appProductRelatedReagentsSingleTube`. |
| 3 | UI services | Fetch tab-specific details and pricing from backend endpoints. | `mimicsInhibitorsService`, `viewDetailsService`, `matureMirnaService`, `priMirnaService`, `relatedReagentsService`, `pricingService`. |
| 3 | Commerce integration | Convert selected product/SKU into cart item payload and invoke cart API. | `fnAddItemToCart`, `formItemfromProduct`, `formItemfromPriMirnaAssays`, `formItemfromRelatedRegent`. |
| 3 | Analytics integration | Track user interactions against the search result and tab modules. | `gsdOmnitureService` calls in `login`, `setDefaultSku`, `setTab`, `fnPDPOmniClick`, `fnMapThis`, `fnAddItemToCart`. |

## 8. Workflow Diagram - Search Result Rendering

| Step | Actor / Module | Action | Next Step |
|---|---|---|---|
| 1 | User | Opens `/order/rnai/miRNA/result?keyword=*`. | Search page loads result data. |
| 2 | Search page | Renders a result item through `appMirnaSearchResult`. | Component initializes. |
| 3 | `appMirnaSearchResult.fnInit` | Initializes state, listens to select-all events, watches quantity, login, and size models. | Price is initialized from default SKU. |
| 4 | `setPrice` | Calls `pricingService.async(sharedTaqManService.productType, packageId, sku, loginStatus)`. | Price fields and commerce flags are updated. |
| 5 | Template | Displays product ID, catalog number, product type, assay name, species, mirBase details, tab links, and commerce panel. | User can open tabs, select products, check price, or add to cart. |
| 6 | `getIsAddToCart` | Determines whether Add to cart is allowed. | Add to cart button is displayed only when eligibility rules pass. |

## 9. Workflow Diagram - Mimics/Inhibitors Tab

| Step | Actor / Module | Action | Data / Endpoint | UI Result |
|---|---|---|---|---|
| 1 | User | Clicks Mimics/Inhibitors tab. | `setTab('mimics-inhibitors', index)` | Existing tab closes if already active; otherwise workflow continues. |
| 2 | Main component | Records analytics for Mimics/Inhibitors module open. | `gsdOmnitureService.relatedProductsModuleOpened(...)` | Analytics event is fired. |
| 3 | Main component | Requests related mimic/inhibitor products. | `mimicsInhibitorsService.fnGetData(assayId, assayType)` | HTTP call begins. |
| 4 | Service | Calls backend. | GET `/order/genome-database/mirnaAssayDropDowns?mirnainhib={assayId}` | Response expected to include `mirnaProducts`. |
| 5 | Main component | Maps package IDs to package objects. | `product.data.packageObjs[packageId]` | Child rows receive product and SKU package metadata. |
| 6 | Template | Repeats child component. | `ng-repeat="objMimicsInhibitors in arrMimicsInhibitorsBase"` | Mimic/inhibitor table rows appear. |
| 7 | Child component | Initializes size dropdown and selected SKU. | `fnGetSize(packageId)` | First SKU detail becomes default selected option. |
| 8 | Child component | Refreshes price when selected option or login changes. | `setPrice(skuNumber.value)` -> `/order/genome-database/price` | Price / Your Price display updates. |
| 9 | User | Clicks Add to cart when allowed. | `onAddToCart` -> main `fnAddItemToCart(obj, 'mimic module')` | Cart item is created from selected related product SKU. |

## 10. Workflow Diagram - Commerce and Price

| Step | Main Result Commerce | Mimic/Inhibitor Child Commerce |
|---|---|---|
| Size source | `product.data.packageObject.skuList[0].skuDetails` | `packageObjects[packageId].skuList[0].skuDetails` |
| Default SKU rule | `getDefaultSku` matches selected `scaleModel` to SKU `scaleSize`; slash in scale size may be normalized to hyphen for comparison. | `fnGetSize` selects the first SKU detail as default child row option. |
| Price endpoint | `/order/genome-database/price` with `productType`, `package_id`, `thisSku`, `priceType`. | `/order/genome-database/price` with blank product type/package ID and selected SKU. |
| Login behavior | `priceType` is `your` when logged in, otherwise `list`. | Login watcher refreshes selected SKU price after login status changes. |
| Add-to-cart eligibility | Requires default SKU, pricing action not matching `Contact`, `Price View`, or `ERR`, and package ID not containing `Stealth3`. | Requires selected option pricing action not matching `Contact`, `Price View`, or `ERR`; template also hides price/actions when package ID contains `Stealth3`. |
| Cart payload | `formItemfromProduct` builds SKU, assay ID, name, price, quantity, symbol, UOM, category, and product name. | `formItemfromPriMirnaAssays` builds payload using `selectedSku` fields for mimic, inhibitor, mature, and pri-miRNA related rows. |
| Analytics | Add-to-cart and size-change events are recorded through `gsdOmnitureService`. | Child delegates add-to-cart to main component, which records analytics. |

## 11. Workflow Diagram - Supporting Tabs

| Tab | Display Rule | Service / Function | Endpoint / Destination | Result |
|---|---|---|---|---|
| Details | Always available as a tab link. | `viewDetailsService.fnGetData(assayId, assayType)` | GET `/order/genome-database/viewAssayDetails` | Displays species, miRBase, mature sequence, amplicon length, chromosome location, aliases, primer pools, cards, stem-loop details, and View Full Details links based on subtype. |
| Mimics/Inhibitors | Visible when `product.data.hasMI` is true. | `mimicsInhibitorsService.fnGetData(assayId, assayType)` | GET `/order/genome-database/mirnaAssayDropDowns?mirnainhib={assayId}` | Displays related mimic/inhibitor rows. |
| Mature miRNA Assays | Visible when product subtype is not `advanced` or `taqman` and `hasMature` is true. | `matureMirnaService.fnGetData(assayId, assayType)` | GET `/order/genome-database/mirnaAssayDropDowns?mirnamature={assayId}` | Displays mature miRNA related assay rows. |
| Pri-miRNA Assays | Visible when `product.data.hasPri` is true. | `priMirnaService.fnGetData(assayId)` | GET `/order/genome-database/mirnaAssayDropDowns?mirnaprimary={assayId}` | Displays pri-miRNA related assay rows. |
| Reagents | Always available as a tab link. | `relatedReagentsService.fnGetData(productType, productSubType)` | GET `/order/genome-database/relatedReagents` | Displays related reagent rows with platform/size and commerce controls. |
| Assay map | Visible when product is not a control assay and subtype is `primiRNA`, `taqman`, or `advanced`. | `alignMapModuleManager` and `fnMapThis` | Lazy-loaded alignment map module | Displays alignment map and records map analytics. |
| Arrays | Visible when `arrayCount > 0`. | `isRelatedArraysClicked` | `/order/genome-database/?pearUXVerSuffix=pearUX2&elcanoForm=true#!/microrna/arrays/microrna_all/?keyword={productID}&searchMethod=keyword` | Opens related array results. |

## 12. UI Business Rules

| Rule ID | Area | Rule | Source |
|---|---|---|---|
| UI-MIR-001 | Result card | Each miRNA result is rendered by `appMirnaSearchResult` using the product binding supplied by the search page. | `mirna-search-result.component.js` |
| UI-MIR-002 | Selection | The result checkbox is bound to `bolSelected`; changing it invokes `fnSelectProduct($event)` and delegates the selected state to `onSelectChange`. | `mirna-search-result.template.html`, `fnSelectProduct` |
| UI-MIR-003 | Best coverage | The UI marks a result as Best coverage when `product.data.recommended` is `Yes`. | `fnGetBoolean`, template |
| UI-MIR-004 | Most citations | The UI marks a result as Most citations when `product.data.citations` equals `maxCitationsNumber`. | `fnFindMaxRow`, template |
| UI-MIR-005 | Product ID link | The Product ID opens `/order/genome-database/details/microrna/{productID}?CID=&ICID=&subtype=` in a new tab and records PDP click analytics. | Template, `fnPDPOmniClick` |
| UI-MIR-006 | Catalog link | Catalog number links open `/order/catalog/product/{defaultSkus}` in a new tab. | Template |
| UI-MIR-007 | Product type display | Product subtype `advanced` or `Advanced Control miRNA Assay` displays Product type as Advanced miRNA Assay. | Template |
| UI-MIR-008 | Product type display | Product subtype `taqman` or `Control miRNA Assay` displays Product type as miRNA Assay. | Template |
| UI-MIR-009 | miRNA help popup | The product type question icon opens a popup explaining Advanced miRNA Assays, miRNA Assays, and Primary miRNA Assays. | `fnOpenMirnaPopup` |
| UI-MIR-010 | Mimics/Inhibitors help popup | The Mimics/Inhibitors tab question icon opens explanatory text for miRNA mimics and inhibitors. | `fnOpenPopup` |
| UI-MIR-011 | Assay design | For advanced target type, the UI displays assay design and prefixes `Advanced,` when `fnDisplayAdvanced(assayDesign)` returns true. | Template, `fnDisplayAdvanced` |
| UI-MIR-012 | Species display | Non-advanced results show species with collapse/expand behavior when the species value is long. | Template |
| UI-MIR-013 | mirBase display | Non-advanced results show miRBase Names with collapse/expand behavior when the value is long. | Template |
| UI-MIR-014 | Details tab | Details tab is always shown and fetches assay details on first open. | Template, `setTab`, `viewDetailsService` |
| UI-MIR-015 | Mimics/Inhibitors tab | Mimics/Inhibitors tab is shown only when `product.data.hasMI` is true. | Template |
| UI-MIR-016 | Mature miRNA tab | Mature miRNA Assays tab is shown only when product subtype is not `advanced` or `taqman` and `product.data.hasMature` is true. | Template |
| UI-MIR-017 | Pri-miRNA tab | Pri-miRNA Assays tab is shown only when `product.data.hasPri` is true. | Template |
| UI-MIR-018 | Reagents tab | Reagents tab is always shown and calls `relatedReagentsService` when opened. | Template, `setTab` |
| UI-MIR-019 | Assay map tab | Assay map is available only for non-control products with subtype `primiRNA`, `taqman`, or `advanced`. | Template |
| UI-MIR-020 | Arrays tab | Arrays link is available only when `arrayCount > 0`. | `isRelatedArraysExist`, template |
| UI-MIR-021 | Tab toggle | Clicking the active tab again closes the tab by setting the current tab to null. | `setTab` |
| UI-MIR-022 | Tab data retrieval | Each tab fetches its data only when the corresponding tab is opened. | `setTab` |
| UI-MIR-023 | Mimics/Inhibitors endpoint | Mimic/inhibitor related products are fetched from `/order/genome-database/mirnaAssayDropDowns` with parameter `mirnainhib={assayId}`. | `mimicsInhibitorsService.fnGetData` |
| UI-MIR-024 | Mimics/Inhibitors result binding | The response field `mirnaProducts` is expected and is assigned to `arrMimicsInhibitorsBase`. | `mimicsInhibitorsService`, `setTab` |
| UI-MIR-025 | Package mapping | Mimics/Inhibitors rows use `packageId` to map related product rows to `product.data.packageObjs`. | `setTab` |
| UI-MIR-026 | Mimics/Inhibitors columns | The Mimics/Inhibitors table displays Mimic/Inhibitor type, Assay ID, Species, Size, and commerce actions. | `mirna-search-result.template.html`, child template |
| UI-MIR-027 | Child assay link | Child assay ID links to `/order/genome-database/details/mirna/{assayId}?CID=&ICID=&subtype=`. | Child template |
| UI-MIR-028 | Child species limit | Mimics/Inhibitors child rows show the first three species by default and provide show more/show less when species count exceeds three. | `speciesLimit`, `fnToggleSpeciesLimit`, child template |
| UI-MIR-029 | Child size source | Child size selector is built from `packageObjects[packageId].skuList[0].skuDetails`. | `fnGetSize` |
| UI-MIR-030 | Child default size | The first SKU detail in the child size list is selected by default. | `fnGetSize` |
| UI-MIR-031 | Child price refresh | Child component refreshes price when selected option changes or login status changes. | `$scope.$watch`, `fnTrackSelectedOption`, `fnUpdateLogin`, `setPrice` |
| UI-MIR-032 | Main price refresh | Main card refreshes price at init and when selected SKU changes. | `fnInit`, `setDefaultSku`, `setPrice` |
| UI-MIR-033 | Price API | Price retrieval uses `/order/genome-database/price` with `priceType` set to `your` when logged in and `list` otherwise. | `pricingService.async` |
| UI-MIR-034 | Main add-to-cart rule | Main card Add to cart is allowed only when default SKU exists, pricing action is not Contact / Price View / ERR, and package ID does not contain `Stealth3`. | `getIsAddToCart` |
| UI-MIR-035 | Child add-to-cart rule | Child row Add to cart is allowed only when selected option pricing action is not Contact / Price View / ERR; the template also suppresses commerce actions for `Stealth3` package IDs. | Child `getIsAddToCart`, child template |
| UI-MIR-036 | Not orderable display | If the main product has no default SKU, the commerce card displays Not Orderable Online. | Template |
| UI-MIR-037 | Availability display | Main card availability is rendered from `sharedTaqManService.getAvailability(defaultSku.inventoryFlag)`. | Template |
| UI-MIR-038 | User price display | Your Price is shown only for logged-in users when the item is add-to-cart eligible. | Template |
| UI-MIR-039 | Check your price | Check your price is shown for unauthenticated users when the item is add-to-cart eligible and triggers login. | Template, `login` |
| UI-MIR-040 | Web-only price | Web-only price is shown only when `priceData.onlinePriceApplicable`, `priceData.showWebOnlyPrice`, and add-to-cart eligibility are true. | `fnSetPricingData` |
| UI-MIR-041 | Size change analytics | Changing size on the main card records size-change analytics when the selected SKU scale size changes. | `setDefaultSku` |
| UI-MIR-042 | Main cart payload | Main card cart item includes SKU, assay ID, name, price, quantity 1, gene symbol, validated flag, UOM, category name, and product name. | `formItemfromProduct` |
| UI-MIR-043 | Related cart payload | Mimics/Inhibitors, Mature miRNA, and Pri-miRNA related rows use selected SKU values from the related product object. | `formItemfromPriMirnaAssays` |
| UI-MIR-044 | Related reagent cart payload | Related reagent rows use selected SKU, reaction string as UOM, product name, and selected SKU price. | `formItemfromRelatedRegent` |
| UI-MIR-045 | Cart location | Mimics/Inhibitors related rows use location label `M/Inhibitor` when added to cart. | `fnAddItemToCart` |
| UI-MIR-046 | Bioz integration | Result card includes `app-bioz-info-v2` using product ID and callback flags for citations and best coverage. | Template |
| UI-MIR-047 | Copy tooltip | Copy option is shown only when selected browser text includes the product ID or default SKU. | `fnDisplayCopyOption` |
| UI-MIR-048 | Advanced specificity header | For advanced/advanced control products, species prefix in product name can drive specificity header text for mouse, human, or rat anti-targets. | `fnSetVariables` |

## 13. Field and Column Requirements

| UI Section | Field / Column | Required Behavior |
|---|---|---|
| Main result header | Best coverage | Display when recommended flag is `Yes`. |
| Main result header | Most citations | Display when citations equals max citations for the result set. |
| Main result body | Product ID | Link to miRNA detail route and trigger PDP click analytics. |
| Main result body | Catalog number | Link to catalog product route using default SKU. |
| Main result body | Product type | Show Advanced miRNA Assay or miRNA Assay based on product subtype. |
| Main result body | Assay design | Show for advanced target type; prefix Advanced when the design is human, mouse, or rat. |
| Main result body | Assay name | Render trusted HTML from product data. |
| Main result body | miRBase Names | Show for non-advanced products with collapse/expand behavior. |
| Main result body | Species | Show for non-advanced products with collapse/expand behavior. |
| Mimics/Inhibitors tab | Mimic/Inhibitor | Display related product type. |
| Mimics/Inhibitors tab | Assay ID | Link to miRNA details page. |
| Mimics/Inhibitors tab | Species | Display up to three by default; allow show more/show less. |
| Mimics/Inhibitors tab | Size | Display dropdown when SKU details exist. |
| Mimics/Inhibitors tab | Price | Display list price with currency when price is available. |
| Mimics/Inhibitors tab | Your Price | Display only after login and when add-to-cart eligible. |
| Mimics/Inhibitors tab | Check your price | Display when not logged in and add-to-cart eligible. |
| Mimics/Inhibitors tab | Add to cart | Display only when child row eligibility passes and package ID is not `Stealth3`. |
| Commerce card | Size | Show selector when more than one SKU detail exists; show static size when exactly one SKU detail exists. |
| Commerce card | Availability | Convert inventory flag through shared service. |
| Commerce card | Price | Display list price or message depending on pricing data and add-to-cart eligibility. |
| Commerce card | Your Price | Display for logged-in users when eligible. |
| Commerce card | Online Price | Display only when web-only price rules pass. |
| Commerce card | Add to cart | Display when main add-to-cart rules pass. |

## 14. API and Service Contract Summary

| UI Need | Service / Function | HTTP Method | Endpoint | Parameters | Expected Response |
|---|---|---|---|---|---|
| Fetch assay details | `viewDetailsService.fnGetData` | GET | `/order/genome-database/viewAssayDetails` | `assayid`, `assaytype` | `result`, optional `plateTargetResult`, parsed as objects. |
| Fetch array details | `viewDetailsService.fnGetArrayDetail` | GET | `/order/genome-database/viewArrayDetails` | `assayid`, `assaytype` | `plateResult`, `mirnaPlateResult`, `plateTargetResult`, `result`. |
| Fetch mimics/inhibitors | `mimicsInhibitorsService.fnGetData` | GET | `/order/genome-database/mirnaAssayDropDowns` | `mirnainhib` | `mirnaProducts`. |
| Fetch mature miRNA assays | `matureMirnaService.fnGetData` | GET | `/order/genome-database/mirnaAssayDropDowns` | `mirnamature` | `mirnaProducts`. |
| Fetch pri-miRNA assays | `priMirnaService.fnGetData` | GET | `/order/genome-database/mirnaAssayDropDowns` | `mirnaprimary` | `mirnaProducts`. |
| Fetch related reagents | `relatedReagentsService.fnGetData` | GET | `/order/genome-database/relatedReagents` | `rev`, `productType`, `productSubType`, `functionality`, `CID`, `ICID` | Related reagent result object with `arrSingleTubes`. |
| Fetch price | `pricingService.async` | GET | `/order/genome-database/price` | `productType`, `package_id`, `thisSku`, `priceType` | Price payload including list/user price fields, currency, action, online price flags. |
| Add to cart | `fnAddItemToCart` | Client cart call | `cart.addItemToCart` | Cart item payload and location metadata | Cart update and analytics event. |

## 15. Acceptance Criteria

| ID | Requirement | Acceptance Criteria |
|---|---|---|
| AC-UI-MIR-001 | Search result rendering | Given a result product, the UI renders Product ID, catalog number, product type, assay name, tabs, and commerce card without layout breakage. |
| AC-UI-MIR-002 | Product links | Product ID and catalog links open the expected detail/catalog routes and preserve analytics click handling. |
| AC-UI-MIR-003 | Tab visibility | Tabs are visible only when the corresponding product flags and subtype rules pass. |
| AC-UI-MIR-004 | Mimics/Inhibitors data | Clicking Mimics/Inhibitors calls `mimicsInhibitorsService.fnGetData` with the current assay ID and renders returned `mirnaProducts`. |
| AC-UI-MIR-005 | Mimics/Inhibitors columns | Each related row displays type, assay ID, species, size, and commerce actions according to template rules. |
| AC-UI-MIR-006 | Species expansion | Related rows with more than three species show a Show More control and can collapse back to Show Less. |
| AC-UI-MIR-007 | Size selection | Changing size updates selected SKU and triggers pricing refresh. |
| AC-UI-MIR-008 | Price display | List price, user price, web-only price, and login prompt display according to login and eligibility rules. |
| AC-UI-MIR-009 | Add-to-cart eligibility | Add to cart is hidden when pricing action is Contact, Price View, ERR, when SKU is missing, or when package ID contains `Stealth3` where applicable. |
| AC-UI-MIR-010 | Cart payload | Add-to-cart payload includes SKU, assay ID, product name, price, quantity, UOM, category, and validation fields expected by cart integration. |
| AC-UI-MIR-011 | Supporting tabs | Details, mature miRNA, pri-miRNA, related reagents, assay map, and arrays follow their documented visibility and data-fetch rules. |
| AC-UI-MIR-012 | Analytics | Tab opens, size changes, PDP clicks, map usage, and add-to-cart actions continue to call `gsdOmnitureService`. |

## 16. QA Test Matrix

| Test Area | Scenario | Expected Result |
|---|---|---|
| Route | Load miRNA result URL with wildcard keyword. | Result page renders without script errors. |
| Result badges | Product has `recommended = Yes`. | Best coverage indicator is displayed. |
| Result badges | Product citations equal `maxCitationsNumber`. | Most citations indicator is displayed. |
| Tabs | Product has `hasMI = true`. | Mimics/Inhibitors tab is visible. |
| Tabs | Product has `hasMI = false`. | Mimics/Inhibitors tab is hidden. |
| Tabs | Product subtype is `advanced`. | Mature miRNA Assays tab is hidden even when mature data exists. |
| Tabs | Product has `hasPri = true`. | Pri-miRNA Assays tab is visible. |
| Mimics/Inhibitors | User opens tab. | API call uses `mirnainhib={assayId}` and rows render from `mirnaProducts`. |
| Mimics/Inhibitors species | Row has more than three species. | Only three species are shown initially with show more/show less control. |
| Size dropdown | Row package has multiple SKU details. | Size dropdown renders and default option is first SKU detail. |
| Login | User is not logged in and product is eligible. | Check your price is shown. |
| Login | User logs in. | User price refreshes using `priceType=your`. |
| Commerce | Pricing action starts with Contact, Price View, or ERR. | Add to cart is hidden. |
| Commerce | Package ID contains `Stealth3`. | Commerce actions are hidden where template suppresses them. |
| Analytics | User clicks PDP link or opens Mimics/Inhibitors tab. | Corresponding Omniture calls execute. |

## 17. Validation Observations and Suggested Improvements

| ID | Observation | Risk | Suggested Improvement |
|---|---|---|---|
| VAL-UI-MIR-001 | `mirna-mimics-inhibitors-single-tube.template.html` calls `$ctrl.fnSetPrice()` on size change, but the child component exposes `setPrice`, not `fnSetPrice`. | Size dropdown changes may not refresh price correctly or may throw a runtime error. | Align template and component method names; add unit/UI test for size change price refresh. |
| VAL-UI-MIR-002 | Child template references `$ctrl.relatedReagents.data.prodDesc`, but the component bindings include `mimicsInhibitors`, `onLogin`, `onAddToCart`, and `packageObjects`. | Product description binding may be undefined or copied from another component. | Confirm intended field and update binding to a `mimicsInhibitors` field if needed. |
| VAL-UI-MIR-003 | `mimicsInhibitorsService.fnGetData(assayId, assayType)` accepts `assayType`, but the service does not use it in the API request. | Future developers may assume assay type affects related product retrieval when it does not. | Remove unused argument or document why it is intentionally unused. |
| VAL-UI-MIR-004 | Several services declare `var bolDone = bolDone;` and `bolWorking`, but caching / working-state protections are incomplete or unused. | Duplicate calls may occur and service state is harder to reason about. | Clean up queue/caching variables and add tests for repeated tab opens. |
| VAL-UI-MIR-005 | `relatedReagentsService` has `bolWorking = true` commented out. | Concurrent related reagent calls may not be suppressed as intended. | Reinstate or remove working-state logic after confirming desired behavior. |
| VAL-UI-MIR-006 | Child component `fnGetPrice` and `fnGetUserPrice` both return `priceStringWithoutCurrencyCode`. | Your Price may not be semantically different from list price if backend returns separate user price fields. | Confirm pricing response contract and update child display helpers if needed. |
| VAL-UI-MIR-007 | Related repos were verified only at metadata level for this UI PRD. | Hidden backend/shared rules may exist outside the inspected UI repo. | Run repository-wide searches for miRNA, mimics, inhibitors, `mirnainhib`, and endpoint controllers across all five repos before final implementation sign-off. |
| VAL-UI-MIR-008 | `magellan-data-scripts` metadata fetch failed during this review. | Data loading or product flag derivation rules may be missing from this PRD. | Re-run repo access and inspect scripts that populate `hasMI`, `hasMature`, `hasPri`, `packageObjs`, and pricing attributes. |

## 18. Developer Implementation Checklist

| Area | Checklist Item |
|---|---|
| Component behavior | Confirm `appMirnaSearchResult` still owns the result card and tab orchestration for the miRNA result route. |
| Tab rules | Add or update tests for `hasMI`, `hasMature`, `hasPri`, subtype, control, and array count visibility rules. |
| Mimics/Inhibitors | Fix or validate the child template size-change handler before enhancing related product behavior. |
| Price | Verify price response fields for list price, user price, web-only price, action, and currency display. |
| Commerce | Validate cart payloads for main result products, mimic/inhibitor rows, mature rows, pri-miRNA rows, and related reagent rows. |
| Login | Confirm login status watchers refresh prices and preserve selected SKU state. |
| Analytics | Confirm all major user interactions continue to report through `gsdOmnitureService`. |
| Accessibility | Validate keyboard access for tab links, dropdowns, popups, show more/show less, and add-to-cart controls. |
| Error handling | Add visible fallback behavior for failed tab service calls if not already handled by the parent page. |
| Multi-repo validation | Complete source searches in product-service, etools, data-scripts, and core before using this as a final engineering sign-off document. |

## 19. Traceability Matrix

| Requirement Area | Primary Function / Template | Service / Endpoint | Notes |
|---|---|---|---|
| Main result rendering | `appMirnaSearchResult`, `mirna-search-result.template.html` | Search result data provider outside inspected component | Product data must include `data`, `packageObject`, `packageObjs`, flags, and pricing fields. |
| Product ID and PDP analytics | `fnPDPOmniClick`, template link | `/order/genome-database/details/microrna/{productID}` | Opens detail page and records click. |
| Mimics/Inhibitors tab | `setTab('mimics-inhibitors')` | `/order/genome-database/mirnaAssayDropDowns?mirnainhib={assayId}` | Renders child component rows. |
| Child row pricing | `fnTrackSelectedOption`, `setPrice` | `/order/genome-database/price` | Triggered by selected SKU and login changes. |
| Main commerce | `setDefaultSku`, `getDefaultSku`, `getIsAddToCart`, `fnSetPricingData` | `/order/genome-database/price` | Controls size, availability, price, web-only price, and add-to-cart button. |
| Cart action | `fnAddItemToCart` | `cart.addItemToCart` | Builds payload depending on source module. |
| Details tab | `setTab('view-details')` | `/order/genome-database/viewAssayDetails` | Populates `arrViewDetails` and subtype flags. |
| Mature tab | `setTab('mature-mirna-assays')` | `/order/genome-database/mirnaAssayDropDowns?mirnamature={assayId}` | Maps package objects for child rows. |
| Pri-miRNA tab | `setTab('pri-mirna-assays')` | `/order/genome-database/mirnaAssayDropDowns?mirnaprimary={assayId}` | Maps package objects for child rows. |
| Related reagents | `setTab('related-reagents')` | `/order/genome-database/relatedReagents` | Uses product type and product subtype. |
| Assay map | `showAlignmentMap`, `loadAlignmentMap`, `fnMapThis` | Lazy alignment map module | Available only for eligible non-control subtypes. |

## 20. Open Questions

| ID | Question | Owner / Follow-up |
|---|---|---|
| OQ-UI-MIR-001 | Which repo owns the backend route that serves `/order/rnai/miRNA/result` in the current deployment? | Confirm with Magellan search/backend owner. |
| OQ-UI-MIR-002 | Should the Mimics/Inhibitors child row display a product description, and if yes, which field should it use? | Confirm product owner and UI developer. |
| OQ-UI-MIR-003 | Should child row Your Price use a separate user-price field rather than the same string returned by `fnGetPrice`? | Confirm pricing service contract. |
| OQ-UI-MIR-004 | Is `Stealth3` suppression required for both main result and all child related product rows? | Confirm commerce/product owner. |
| OQ-UI-MIR-005 | Which data scripts populate `hasMI`, `hasMature`, `hasPri`, `packageObjs`, and citation/recommended flags? | Validate in `magellan-data-scripts` after repo access succeeds. |

