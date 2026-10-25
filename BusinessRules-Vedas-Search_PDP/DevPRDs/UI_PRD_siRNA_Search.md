# UI Developer PRD - siRNA Search

| Field | Details |
|---|---|
| Product / Tool | siRNA Search |
| Tool URL | https://www.thermofisher.com/order/rnai/siRNA/result?keyword=* |
| Audience | UI developers, QA engineers, product owners, business analysts |
| Document Type | UI rules document / developer PRD |
| Source Date | 2026-07-31 |
| Primary Verified Repos | thermofisher/tfcom-magellan-etools, thermofisher/magellan-search |
| Supporting Repos Reviewed | thermofisher/tfcom-magellan-product-service, thermofisher/magellan-data-scripts, thermofisher/magellan-core |
| Style Reference | UI_Developer_PRD table-heavy format used for earlier developer PRDs |

## 1. Document Purpose

| Item | Description |
|---|---|
| Purpose | Capture UI-facing rules, repository ownership, modules, functions, workflows, and validation observations for the siRNA Search tool. |
| Developer Focus | Identify source repos, PHP modules, JavaScript functions, shared UI helpers, search form behavior, product detail tab behavior, result table rules, shopping-list behavior, and API/service dependencies. |
| Business Focus | Explain how users search for siRNA products by keyword, gene, transcript, assay ID, siRNA ID, species, and application, then select ranked products for order workflows. |
| Scope | User-facing search entry, GeneAssist siRNA search form, result table, select-assays product detail tab, alignment map, size and purity selection, quantity, shopping list, and UI handoff to order tabs. |
| Out of Scope | Backend SQL implementation details except where they directly shape UI behavior; live production data values not visible in source. |

## 2. Source Evidence and Review Boundary

| Evidence Type | Repo | File / Module | What Was Verified |
|---|---|---|---|
| siRNA landing workflow | thermofisher/tfcom-magellan-etools | `src/tools/ga_apps/sirna/index.php` | GeneAssist siRNA landing page, direct URL variable routing, product family labels, search database link, feature-gated product options, document title, launch logging. |
| siRNA search form and result page | thermofisher/tfcom-magellan-etools | `src/tools/ga_apps/sirna/search/search.php` | Search fields, species options, criteria options, application option, recent search history, direct ID routing, result table columns, single siRNA result handling, target selection rules. |
| siRNA product details tab | thermofisher/tfcom-magellan-etools | `src/tools/ga_apps/sirna/search/select_assays.php` | Gene details, transcripts, pathways, alignment map section, Silencer Select coding products, noncoding products, table columns, add buttons, warnings, shopping-list state. |
| siRNA UI interaction logic | thermofisher/tfcom-magellan-etools | `src/tools/ga_apps/sirna/sirna.js` | Search submission, result selection, tab navigation, add-to-list functions, add-all, size selection parsing, quantity handling, shopping-list hooks, alignment-map selection, order tab enablement. |
| Shared GeneAssist UI shell | thermofisher/tfcom-magellan-etools | `src/tools/shared/js/core.js`, `src/tools/ga/ga.js` | Navigation, tab-click patterns, selected product page state, shared progress/help behavior. |
| Search route and result shell | thermofisher/magellan-search | `RedirectInterceptor.java`, `searchResults.jsp`, `UnifiedCardProductTypeCountAction.java` | Route normalization into `/order/rnai/siRNA/result`, product type label mapping, unified-card count link behavior. |
| Product count and Solr service | thermofisher/tfcom-magellan-product-service | `SirnaSiteSearchService`, `SirnaSiteSearchQueryDecorator`, `SIRNASiteSearchSearcherFactory`, product type enums | Site-search count behavior supporting siRNA result card discovery. |
| Shared field constants | thermofisher/magellan-core | `MagellanSearchConstants.java`, `MagellanTranslations.properties` | siRNA FAST field mappings and shared translated product labels. |
| Data support | thermofisher/magellan-data-scripts | `siRNA_setup.prop`, `ld_sirna_rank.ctl`, `SiRNA.rb` | Design/rank/alignment-map inputs that explain UI ranking and alignment-map fields. |

## 3. Product Overview

| Area | Details |
|---|---|
| Product Name | siRNA Search |
| Main Route | `/order/rnai/siRNA/result?keyword=*` |
| GeneAssist Search Route | `/order/rnai/siRNA/search` |
| Primary Purpose | Help users find predesigned, validated, noncoding, in vivo, and related assay products for gene silencing workflows. |
| Main Product Families Seen in UI Source | Silencer Select siRNAs, Silencer siRNAs, Ambion In Vivo siRNAs, related TaqMan Gene Expression Assays. |
| Business Goal | Let users identify the right siRNA target, compare available siRNA and assay products, choose size and purity, add selections to a shopping list, and proceed into ordering workflows. |
| Developer Goal | Maintain predictable routing, feature-gated fields, tab state, product row rendering, cart object construction, map selection, and order tab enablement. |

## 4. Users and Stakeholders

| Persona / Stakeholder | Need | UI Implication |
|---|---|---|
| Research scientist | Search by gene, transcript, siRNA ID, assay ID, OMIM ID, or RNAdb identifiers. | Search form must support multiple fields, criteria, species, recent searches, and direct ID routing. |
| Scientist planning in vivo work | Distinguish cells use from animal use. | Application radio buttons must expose cells versus animals when Ambion In Vivo features are enabled. |
| Buyer / procurement user | Choose size, purity, quantity, and add items to an order workflow. | Product rows must display availability, size and purity controls, quantity fields, Add and Add All actions, and shopping-list updates. |
| Product owner | Preserve business rules for feature-gated products, noncoding options, and minimum order warnings. | UI must respect BabelFish and diehard feature gates and show 1 nmol minimum-order warnings. |
| UI developer | Understand module boundaries and function-level behavior. | PRD maps PHP modules, JavaScript functions, UI elements, state changes, and integration points. |
| QA engineer | Test search fields, direct routing, target selection, product tables, add-to-list, and navigation. | Acceptance criteria and validation matrix define testable UI scenarios. |

## 5. Repository and Module Map

| Repo | Primary Role | Key Files / Modules | Confirmed UI Responsibility |
|---|---|---|---|
| thermofisher/tfcom-magellan-etools | Primary siRNA GeneAssist UI implementation | `index.php`, `search/search.php`, `search/select_assays.php`, `sirna.js` | Landing page, search form, result rendering, detail tab, product group tables, shopping-list updates, workflow navigation. |
| thermofisher/magellan-search | Search route shell and product-count integration | `RedirectInterceptor.java`, `searchResults.jsp`, `UnifiedCardProductTypeCountAction.java` | Routes siRNA search requests to canonical RNai siRNA result URL and labels siRNA result category. |
| thermofisher/tfcom-magellan-product-service | Supporting product count/search service | `SirnaSiteSearchService`, `SirnaSiteSearchQueryDecorator`, `SIRNASiteSearchSearcherFactory` | Supplies siRNA site-search counts used by the broader search experience. |
| thermofisher/magellan-data-scripts | Data and rank support | `siRNA_setup.prop`, `ld_sirna_rank.ctl`, `SiRNA.rb` | Provides design/ranking/alignment-map data shape that drives product rows and map behavior. |
| thermofisher/magellan-core | Shared constants and labels | `MagellanSearchConstants.java`, translations | Provides siRNA field names and shared labels used by backend result objects and UI-facing result labels. |

## 6. Confirmed UI Modules and Functions

| Module / Function | Type | File | Main Responsibility |
|---|---|---|---|
| `index.php` | PHP page | `tfcom-magellan-etools/src/tools/ga_apps/sirna/index.php` | Render siRNA workflow landing page, route direct URL variables, and expose Search Database entry. |
| `search.php` | PHP page | `tfcom-magellan-etools/src/tools/ga_apps/sirna/search/search.php` | Render search form, recent searches, application selector, results, target tables, and direct siRNA result rows. |
| `select_assays.php` | PHP page | `tfcom-magellan-etools/src/tools/ga_apps/sirna/search/select_assays.php` | Render product detail tab, gene details, transcripts, pathways, alignment map, and product group tables. |
| `sirnaSearch` | JavaScript function | `tfcom-magellan-etools/src/tools/ga_apps/sirna/sirna.js` | Build post data from the search form and navigate to the search tab or selected product page. |
| `sirnaSelectProduct` | JavaScript function | `sirna.js` | Select a target row and navigate to product details with gene, RNAdb, species, search type, and selected result context. |
| `sirnaSelectProductByAssayId` | JavaScript function | `sirna.js` | Navigate from a known assay/siRNA ID to the product details tab. |
| `jumpTosiRNA` | JavaScript function | `sirna.js` | Re-run search for a related siRNA ID from multi-target or related-hit rows. |
| `sirnaAddToList` | JavaScript function | `sirna.js` | Add one selected product row to the shopping list. |
| `sirnaAddAllToList` | JavaScript function | `sirna.js` | Add all visible addable product rows in a product group to the shopping list. |
| `sirnaGetProdObjByRow` | JavaScript function | `sirna.js` | Build the shopping-list product object from a selected product row. |
| `sirnaAddSirnaFromSearch` | JavaScript function | `sirna.js` | Add a single direct-search result row to the shopping list. |
| `toggleAdditionalProducts` | JavaScript function | `sirna.js` | Show or hide rows beyond the initial visible product limit. |
| `toggleAlignmentMap` | JavaScript function | `sirna.js` | Show or hide the alignment map block. |
| `sirna_product_selected` | Event hook | `sirna.js` | Enable order tabs when shopping-list count becomes greater than zero. |
| `sirna_product_deselected` | Event hook | `sirna.js` | Recheck warnings, remove product from map, and disable order tabs if the shopping list is empty. |
| `checkErrors` | JavaScript function | `sirna.js` | Maintain the warning for fewer than four 1 nmol Silencer Select selections. |
| `RedirectInterceptor` | Java web interceptor | `magellan-search` | Normalize older siRNA genome-database requests into RNai siRNA result URLs. |

## 7. Functional Architecture

| Level | Layer | Components | Responsibility |
|---|---|---|---|
| 1 | User entry | `/order/rnai/siRNA/result?keyword=*`, `/order/rnai/siRNA/search` | Users enter through canonical result URLs or GeneAssist search workflow. |
| 1 | Search shell | `magellan-search` route handling and result JSP | Normalize route and expose siRNA as a product category. |
| 2 | GeneAssist UI | `index.php`, `search.php`, `select_assays.php` | Render landing, search, result, and product-detail tabs. |
| 2 | JavaScript navigation | `sirna.js`, `Nav.tabClickWithPostData`, selected product page state | Move between search and product-details tabs while preserving search context. |
| 2 | Shopping list | GeneAssist shopping list panel and `sirna.js` product object builders | Add, remove, and track products before order handoff. |
| 3 | Data and service dependencies | `Sirna` model, product-service count, Magellan core constants, data scripts | Supply result rows, rank, product details, alignment-map objects, and product counts. |
| 3 | External destinations | NCBI Gene, NCBI Nucleotide, RNAdb, validation popups, citations, order form | Provide supporting biology links, validation evidence, references, and order workflow handoff. |

## 8. Workflow Diagram - Entry and Routing

| Step | Layer | Module / Function | Action | Output |
|---|---|---|---|---|
| 1 | Level 1 route | Browser | User opens `/order/rnai/siRNA/result?keyword=*`. | siRNA search route is requested. |
| 2 | Level 1 route | `RedirectInterceptor` | Older genome-database siRNA requests are normalized to `/order/rnai/siRNA/result`. | Canonical RNai siRNA route. |
| 3 | Level 2 page shell | `searchResults.jsp` | Product type `sirna` is labelled as `siRNA`. | Search result page can display the siRNA category. |
| 4 | Level 2 GeneAssist entry | `index.php` | Search Database link points users to `/order/rnai/siRNA/search`. | GeneAssist siRNA workflow opens. |
| 5 | Level 2 direct variable handling | `index.php` | URL variables such as gene ID, accession, RNAdb ID, siRNA ID, and gene-expression assay ID trigger the relevant search/product-details navigation. | User bypasses the landing page when enough context is supplied. |
| 6 | Level 3 launch instrumentation | `index.php` | `logLaunchOnLoad('siRNA')` runs on page load. | Launch event is recorded. |

```text
User URL
  -> Magellan route normalization
    -> siRNA result shell
      -> GeneAssist siRNA entry
        -> Search form or direct product-details tab
```

## 9. Workflow Diagram - Search Form Submission

| Step | Layer | Module / Function | Action | Output |
|---|---|---|---|---|
| 1 | Level 1 user action | Search form | User enters search term, field, criteria, species, and optional application. | Search form state. |
| 2 | Level 2 client validation | `sirnaSearch` | Empty search term displays `No search term was specified. Enter a term and retry search.` | Search does not execute. |
| 3 | Level 2 post data | `sirnaSearch` | Adds `search_type`, `search_species`, `search_criteria`, `search_term`, and `invivo` to post data. | Structured tab post data. |
| 4 | Level 2 special ID flow | `sirnaSearch` | For `sirna_id` or `assay_id`, selected product page state is stored before tab navigation. | Product context is cached. |
| 5 | Level 2 navigation | `Nav.tabClickWithPostData` | Posts data to the `sirna.search.search` tab. | `search.php` receives request. |
| 6 | Level 3 server-rendered UI | `search.php` | Normalizes field labels, updates recent searches, executes the search, and renders results or target selection. | Search result UI is shown. |

```text
Search form
  -> sirnaSearch
    -> postData
      -> Nav.tabClickWithPostData
        -> search.php result rendering
```

## 10. Workflow Diagram - Target Selection to Product Details

| Step | Layer | Module / Function | Action | Output |
|---|---|---|---|---|
| 1 | Level 1 user action | Result target table | User selects a primary or secondary target. | Gene/RNAdb/species context. |
| 2 | Level 2 JavaScript | `sirnaSelectProduct` | Builds post data for gene ID or RNAdb ID, search species, criteria, and in vivo value. | Product-details post data. |
| 3 | Level 2 state | `setSelectedProductPage` | Stores selected search-result context for later tab state. | Selected context is retained. |
| 4 | Level 2 navigation | `Nav.sirna.workflows[1].tabs[2].enable` | Product details tab is enabled. | Product-details tab becomes accessible. |
| 5 | Level 2 navigation | `Nav.tabClickWithPostData` | Navigates to `sirna.search.productdetails`. | `select_assays.php` loads. |
| 6 | Level 3 server-rendered UI | `select_assays.php` | Renders gene details, transcripts, pathways, alignment map, and product group tables. | User can select products for shopping list. |

```text
Target row Select
  -> sirnaSelectProduct
    -> productdetails tab enabled
      -> select_assays.php
        -> gene details and product groups
```

## 11. Workflow Diagram - Product Selection and Shopping List

| Step | Layer | Module / Function | Action | Output |
|---|---|---|---|---|
| 1 | Level 1 user action | Product group table | User chooses size/purity, quantity, and Add or Add All. | Selected row state. |
| 2 | Level 2 JavaScript | `sirnaAddToList` or `sirnaAddAllToList` | Finds visible product rows and delegates product-object creation. | One or more product objects. |
| 3 | Level 2 object builder | `sirnaGetProdObjByRow` | Reads product ID, selected size, purity, part number, quantity, validity, availability, species, category, subtype, and detail link. | Shopping-list product object. |
| 4 | Level 2 shopping list | `listPanel.shoppingList.add_product` or `add_product_mult` | Adds selected product object to shopping list. | Shopping list count updates. |
| 5 | Level 3 event hook | `sirna_product_selected` | If shopping list count is greater than zero, order tabs and Next actions are enabled. | User can proceed in workflow. |
| 6 | Level 3 map state | `map.selectFeature` or `removeFromMap` | Product map selection is synchronized with shopping-list add/remove actions when map exists. | Alignment map reflects selected products. |

```text
Product table row
  -> Add or Add All
    -> sirnaGetProdObjByRow
      -> shoppingList.add_product
        -> order tabs enabled
```

## 12. Search Form Rules

| Rule ID | Area | Rule | Source |
|---|---|---|---|
| UI-SIRNA-001 | Page title | The GeneAssist page title is set to `GeneAssist siRNA Workflow Builder`. | `index.php` |
| UI-SIRNA-002 | Search entry | Search Database link navigates to `/order/rnai/siRNA/search`. | `index.php` |
| UI-SIRNA-003 | URL variable routing | Incoming `geneid` is converted to `gene_id` and navigates to the product details tab. | `index.php` |
| UI-SIRNA-004 | Direct target routing | URL variables `geneid`, `gene_id`, `acc`, and `rnadbid` navigate to product details when enough context is provided. | `index.php`, `search.php` |
| UI-SIRNA-005 | Direct ID routing | URL variables `sirnaid` and `gex` navigate into search/result handling. | `index.php`, `search.php` |
| UI-SIRNA-006 | Feature gate | RNAdb and noncoding features are gated by BabelFish visibility. | `search.php`, `select_assays.php` |
| UI-SIRNA-007 | Feature gate | Ambion In Vivo application options are gated by diehard visibility. | `search.php`, `index.php` |
| UI-SIRNA-008 | Application option | When diehard is visible, users can choose cells use or animals use. Cells maps to `invivo=no`; animals maps to `invivo=yes`. | `search.php` |
| UI-SIRNA-009 | In vivo default | If no in vivo value is provided, the UI defaults to `no`. | `search.php` |
| UI-SIRNA-010 | Numeric in vivo handling | Numeric value `1` is treated as `yes`; other numeric values are treated as `no`. | `search.php` |
| UI-SIRNA-011 | Search field options | Field options include All Fields, Gene Name, Gene Symbol, Gene ID, NCBI Transcript, OMIM ID, TaqMan Assay ID, and siRNA ID. | `search.php` |
| UI-SIRNA-012 | RNAdb field options | RNAdb ID and RNAdb Gene Symbol options are shown only when BabelFish is visible. | `search.php` |
| UI-SIRNA-013 | Search criteria options | Criteria options are Contains, Matches, Starts with, and Ends with. | `search.php` |
| UI-SIRNA-014 | Species options | Species options are All Species, Homo sapiens, Mus musculus, and Rattus norvegicus. | `search.php` |
| UI-SIRNA-015 | Search submission | The search term input submits on Enter by calling `sirnaSearch`. | `search.php` |
| UI-SIRNA-016 | Search validation | Blank search term shows a form error and hides previous result content. | `sirna.js` |
| UI-SIRNA-017 | Recent searches | Recent searches are stored in session only when search type, criteria, and term are not blank. | `search.php` |
| UI-SIRNA-018 | Recent search uniqueness | A recent search is unique by type, clean type, criteria, clean criteria, term, and species. | `search.php` |
| UI-SIRNA-019 | Recent search limit | Recent searches are limited to five entries. | `search.php` |
| UI-SIRNA-020 | Recent search replay | Recent search links repopulate the form with `fillHistory`. | `search.php` |
| UI-SIRNA-021 | Next button state | Search Next button is active only when the shopping list contains at least one product. | `search.php`, `sirna.js` |

## 13. Search Result Rules

| Rule ID | Area | Rule | Source |
|---|---|---|---|
| UI-SIRNA-022 | Search result title | Search results are rendered under the `Search Results` heading. | `search.php` |
| UI-SIRNA-023 | Target grouping | When a search returns target records, the UI displays Primary Target and Secondary Targets tables where applicable. | `search.php` |
| UI-SIRNA-024 | Target columns | Target tables show Gene ID or RNAdb ID, Gene Symbol or RNAdb Gene Symbol, Gene Name or Description, Species, Count where available, and Select action. | `search.php` |
| UI-SIRNA-025 | External links | Gene ID links open NCBI Gene; RNAdb ID links open RNAdb. | `search.php`, `select_assays.php` |
| UI-SIRNA-026 | Target select | Select action calls `sirnaSelectProduct` with gene ID, RNAdb ID, species, search type, and selected search-result context. | `search.php`, `sirna.js` |
| UI-SIRNA-027 | Single siRNA result | A direct siRNA ID result renders a product table without requiring target selection first. | `search.php` |
| UI-SIRNA-028 | Direct result columns | Direct result product table shows siRNA ID, Type, Availability, Size/Purity, Quantity, and Add action. | `search.php` |
| UI-SIRNA-029 | Important information | Important Information help link appears only when the product has important information text. | `search.php`, `select_assays.php` |
| UI-SIRNA-030 | Validated type link | Validated rows display validation procedure text as a popup link. | `search.php`, `select_assays.php` |
| UI-SIRNA-031 | Predesigned type | Nonvalidated rows display predesigned coding or noncoding type text. | `search.php` |
| UI-SIRNA-032 | Associated assay text | If a validated result has an associated assay ID, the UI displays `Validated by Assay` followed by the assay ID. | `search.php`, `select_assays.php` |
| UI-SIRNA-033 | Citation text | If a citation is available, the UI displays `Product Citation found` as a popup link. | `search.php`, `select_assays.php` |
| UI-SIRNA-034 | Obsolete result message | If product status is not active, the UI warns that the siRNA no longer meets design criteria and suggests choosing another siRNA. | `search.php` |
| UI-SIRNA-035 | Availability label | Product rows display `Inventoried` or `Made to Order` based on inventory logic. | `search.php`, `select_assays.php` |
| UI-SIRNA-036 | Made-to-order rule | In vivo products and noncoding siRNAs are treated as made to order in the UI logic. | `search.php`, `select_assays.php` |
| UI-SIRNA-037 | Silencer exception | Non-select Silencer siRNA direct results can force inventoried availability. | `search.php` |
| UI-SIRNA-038 | Quantity field | Quantity inputs default to `1`, are limited to three characters in product detail tables, and use numeric-only keydown validation. | `search.php`, `select_assays.php` |
| UI-SIRNA-039 | Direct result add | Direct result Add calls `sirnaAddSirnaFromSearch`. | `search.php`, `sirna.js` |

## 14. Product Details and Product Group Rules

| Rule ID | Area | Rule | Source |
|---|---|---|---|
| UI-SIRNA-040 | Product details entry | Product details tab is reached through selected gene, RNAdb, accession, siRNA ID, or assay ID context. | `index.php`, `sirna.js`, `select_assays.php` |
| UI-SIRNA-041 | Gene details table | Gene Details table shows Gene ID or RNAdb ID, Gene Symbol or RNAdb Gene Symbol, Gene Name or Description, Species, and Product Count. | `select_assays.php` |
| UI-SIRNA-042 | Gene alias | Gene Alias is displayed below the Gene Details table when present. | `select_assays.php` |
| UI-SIRNA-043 | Transcript links | Transcripts are displayed with links to NCBI Nucleotide and an Additional Information popup when transcript data is available. | `select_assays.php` |
| UI-SIRNA-044 | Pathway links | Pathways display a `View N pathway(s)` popup link when pathway data exists. | `select_assays.php` |
| UI-SIRNA-045 | Alignment map | Alignment Map section is expandable and hidden by default. | `select_assays.php`, `sirna.js` |
| UI-SIRNA-046 | Alignment map guidance | Map section text instructs users to click products in map view to add them to the Shopping List. | `select_assays.php` |
| UI-SIRNA-047 | Custom design link | Alignment Map section includes a Custom Designed siRNA link that navigates to the custom design input tab. | `select_assays.php` |
| UI-SIRNA-048 | Coding Silencer Select section | Silencer Select coding products display when ranked coding Silencer Select results exist. | `select_assays.php` |
| UI-SIRNA-049 | In vivo title | When in vivo is selected, the coding product group title changes to Ambion In Vivo siRNAs for coding transcripts. | `select_assays.php` |
| UI-SIRNA-050 | Noncoding section | Silencer Select noncoding products display only when BabelFish is visible and noncoding ranked results exist. | `select_assays.php` |
| UI-SIRNA-051 | Product group columns | Product group tables show siRNA ID, Type, Availability, Size/Purity, Quantity, and Add/Add All actions. | `select_assays.php` |
| UI-SIRNA-052 | Initial row limit | Product groups show the first three siRNA rows by default. Rows after the third are hidden until the user expands the group. | `select_assays.php`, `toggleAdditionalProducts` |
| UI-SIRNA-053 | TaqMan assay row limit | Gene-expression assay groups use one initial visible assay row before show/hide additional behavior. | `toggleAdditionalProducts` |
| UI-SIRNA-054 | Show/hide additional | Additional product link text toggles between Show Additional and Hide Additional based on visibility state. | `toggleAdditionalProducts` |
| UI-SIRNA-055 | Add All | Add All adds all currently visible addable rows in the product group. | `sirnaAddAllToList` |
| UI-SIRNA-056 | Size and purity value | Size/Purity selections carry part number, purity, size, label, and inventory flag values for JavaScript parsing. | `select_assays.php`, `sirna.js` |
| UI-SIRNA-057 | Size change handling | Silencer Select size changes call `updateSelectedSiSelProduct` from the size selector onchange handler. | `select_assays.php` |
| UI-SIRNA-058 | One nmol warning | If fewer than four 1 nmol Silencer Select products are selected, the UI shows a warning requiring at least four siRNAs or scale change to 5 nmol. | `select_assays.php`, `checkErrors` |
| UI-SIRNA-059 | Related genes | Rows can display related gene hit links that re-run search through `jumpTosiRNA`. | `select_assays.php`, `sirna.js` |
| UI-SIRNA-060 | Related noncoding genes | Noncoding rows can display related noncoding gene hit links when present. | `select_assays.php` |

## 15. Shopping List and Order Navigation Rules

| Rule ID | Area | Rule | Source |
|---|---|---|---|
| UI-SIRNA-061 | Product object construction | `sirnaGetProdObjByRow` builds product objects with product ID, species, in vivo flag, coding text, validity, availability, part number, size, quantity, category, subcategory, display text, product type, and detail link. | `sirna.js` |
| UI-SIRNA-062 | Silencer Select category | Non-in vivo Silencer Select rows use category `Silencer Select siRNAs` and product type `sise`. | `sirna.js` |
| UI-SIRNA-063 | Ambion In Vivo category | In vivo rows use category `Ambion In Vivo siRNAs` and product type `diehard`. | `sirna.js` |
| UI-SIRNA-064 | Silencer category | Silencer rows use category `Silencer siRNAs` and product type `sirna`. | `sirna.js` |
| UI-SIRNA-065 | Gene-expression assay category | Related gene-expression assay rows use TaqMan coding or noncoding Gene Expression Assays based on coding text. | `sirna.js` |
| UI-SIRNA-066 | Species normalization | Shopping-list link generation defaults missing species to Homo sapiens and normalizes species names through `getSpeciesScientificName`. | `sirna.js` |
| UI-SIRNA-067 | Order tab enablement | Order tabs and Next actions are enabled when shopping-list count is greater than zero. | `sirna_product_selected`, `sirnaEnableOrderTabs` |
| UI-SIRNA-068 | Order tab disablement | Order tabs and Next actions are disabled when shopping list becomes empty. | `sirna_product_deselected`, `sirnaDisableOrderTabs` |
| UI-SIRNA-069 | Map selection | Adding a siRNA product selects the matching `siRNA_` feature on the alignment map when the map exists. | `sirnaGetProdObjByRow` |
| UI-SIRNA-070 | Map deselection | Removing a product unselects matching `siRNA_` or `GeXassay_` map feature. | `removeFromMap` |
| UI-SIRNA-071 | Print list | Application load adds a `Print List` link that calls `printOrderForm`. | `sirnaOnApplicationLoad` |
| UI-SIRNA-072 | Shopping-list empty event | Empty shopping-list event disables order tabs and clears all map selections. | `sirnaShopListEmpty`, `removeAllFromMap` |

## 16. Field and Column Requirements

| UI Section | Field / Column | Required Behavior |
|---|---|---|
| Search form | Application | Show cells and animals radio choices only when Ambion In Vivo feature is visible. |
| Search form | Field to be searched | Default to All Fields and allow gene, transcript, OMIM, RNAdb, assay ID, and siRNA ID options based on feature gates. |
| Search form | Criteria | Allow contains, matches, starts with, and ends with. |
| Search form | Species | Allow All Species, Homo sapiens, Mus musculus, and Rattus norvegicus. |
| Search form | Search term | Required before executing a search. |
| Recent searches | Recent search link | Replay type, term, criteria, and species into the form. |
| Target table | Gene ID / RNAdb ID | Link to external reference page and preserve selected context. |
| Target table | Gene Symbol / RNAdb Gene Symbol | Display the symbol value returned for the selected target type. |
| Target table | Product Count | Display count where available. |
| Target table | Select | Trigger `sirnaSelectProduct`. |
| Direct result table | siRNA ID | Display selected siRNA ID and optional important information help link. |
| Direct result table | Type | Display validated, predesigned, coding, noncoding, or in vivo text. |
| Direct result table | Availability | Display Inventoried or Made to Order. |
| Direct result table | Size/Purity | Populate selector from product part, purity, size, label, and inventory metadata. |
| Direct result table | Quantity | Default to 1 and restrict entry to numeric values. |
| Direct result table | Add | Add selected product to shopping list through `sirnaAddSirnaFromSearch`. |
| Product details | Gene Details | Display target identifiers, symbol, description, species, and product count. |
| Product details | Transcripts | Display NCBI transcript links and Additional Information popup when available. |
| Product details | Pathways | Display pathway count popup when available. |
| Product group | Add All | Add all currently visible addable products in a group. |
| Product group | Show Additional | Reveal hidden rows and related rows for validation, citations, and related hits. |
| Product group | Warning | Show 1 nmol minimum-order warning when selection count is below four. |
| Alignment map | Product selection | Allow map-backed product selection and synchronize shopping-list state. |

## 17. API and Integration Touchpoints

| Integration | Owning Repo / Module | UI Usage | Validation Notes |
|---|---|---|---|
| RNai siRNA result route | `magellan-search` | Canonical tool URL for result entry. | Validate active production rewrite behavior for wildcard keyword. |
| GeneAssist siRNA search route | `tfcom-magellan-etools` | Search Database entry point and tabbed workflow. | Confirm route remains active for current production UI. |
| Product-service SIRNA count | `tfcom-magellan-product-service` | Supports broader search category count and unified-card linking. | UI PRD does not assume direct browser call from eTools. |
| GeneAssist PHP model and SQL | `tfcom-magellan-etools` | Supplies rendered rows for search, gene details, ranked products, assays, citations, and size/purity options. | Backend contract should be regression tested when UI fields are changed. |
| Alignment map data | `magellan-data-scripts`, eTools map plugins | Displays map and product features. | Validate that current map assets load over secure production URLs. |
| External reference links | NCBI Gene, NCBI Nucleotide, RNAdb | Opens supporting gene/transcript/ncRNA references. | Validate link freshness and accessibility. |
| Shopping-list/order flow | GeneAssist shared UI | Enables order tabs after product selection. | Validate cart object fields with downstream order form. |

## 18. Acceptance Criteria

| ID | Scenario | Acceptance Criteria |
|---|---|---|
| AC-SIRNA-001 | Open siRNA search | Opening `/order/rnai/siRNA/search` displays the Search Database form and application option when feature flags allow. |
| AC-SIRNA-002 | Blank search | Submitting an empty term displays the configured error and does not leave stale search results visible. |
| AC-SIRNA-003 | Search options | Search field, criteria, and species selectors show the configured options, with RNAdb options gated by BabelFish. |
| AC-SIRNA-004 | Application option | Choosing animals sends `invivo=yes`; choosing cells sends `invivo=no`. |
| AC-SIRNA-005 | Recent search | A completed nonblank search appears in Recent Searches and the list never exceeds five entries. |
| AC-SIRNA-006 | Direct siRNA ID result | Searching by siRNA ID can render a direct product table with size/purity, quantity, availability, and Add action. |
| AC-SIRNA-007 | Target selection | Selecting a target opens product details with gene details, transcripts, pathways, and product groups for that target. |
| AC-SIRNA-008 | Product groups | Coding Silencer Select, noncoding Silencer Select, Silencer, and related TaqMan assay groups display only when source results exist and feature gates allow. |
| AC-SIRNA-009 | Show additional | Product groups hide rows beyond the initial limit and reveal them through Show Additional. |
| AC-SIRNA-010 | Add one product | Clicking Add creates one shopping-list product with correct product ID, part number, size, quantity, category, species, and availability. |
| AC-SIRNA-011 | Add all products | Clicking Add All adds all currently visible addable product rows in that product group. |
| AC-SIRNA-012 | One nmol warning | Selecting fewer than four 1 nmol Silencer Select products shows the minimum-order warning. |
| AC-SIRNA-013 | Order navigation | Order tabs and Next actions remain disabled while the shopping list is empty and become enabled after at least one product is added. |
| AC-SIRNA-014 | Map behavior | When alignment map exists, added products are selected on the map and removed products are unselected. |
| AC-SIRNA-015 | Supporting links | NCBI, RNAdb, transcript, pathway, validation, and citation links open the correct supporting content. |

## 19. QA Matrix

| Test Area | Test Case | Expected Result |
|---|---|---|
| Routing | Open canonical siRNA wildcard route. | Result route loads or redirects into active siRNA search experience. |
| Routing | Open with `geneid` URL variable. | Page navigates to product details for that gene. |
| Routing | Open with `sirnaid` URL variable. | Page navigates to search result handling for that siRNA ID. |
| Feature gate | Hide BabelFish. | RNAdb options and noncoding sections are not displayed. |
| Feature gate | Hide diehard. | In vivo application radio group is not displayed. |
| Search form | Submit All Fields with human species. | Search executes with selected species. |
| Search form | Submit TaqMan Assay ID. | Selected product page context is stored and search/detail behavior is triggered. |
| Results | Result has important information. | Help icon/link is displayed. |
| Results | Result is validated. | Validation popup link is displayed. |
| Results | Result has citation. | Product Citation found link is displayed. |
| Product details | Target has transcripts. | Transcript links and Additional Information appear. |
| Product details | Target has pathways. | Pathway count popup link appears. |
| Product groups | More than three siRNA rows. | Only first three show initially; Show Additional reveals the rest. |
| Shopping list | Add one coding Silencer Select product. | Product appears in shopping list and order tabs enable. |
| Shopping list | Remove last product. | Order tabs disable and map selection clears. |
| Quantity | Type nonnumeric value in quantity. | Numeric-only keydown validation blocks invalid entry. |
| Alignment map | Toggle map. | Map section opens and closes without losing selected products. |

## 20. Validation Observations

| Severity | Observation | Impact | Recommendation |
|---|---|---|---|
| High | The UI is largely server-rendered PHP with inline HTML and inline JavaScript handlers. | Changes can create regressions across markup, script, and session behavior. | Add automated browser regression coverage around search, target select, product details, and add-to-list workflows. |
| High | Size/Purity option values are delimiter-encoded strings parsed by JavaScript. | A malformed option value can break cart object construction. | Replace with structured data attributes or JSON payloads when modernizing. |
| Medium | Search form validation is split between JavaScript and PHP-generated state. | Different paths can show inconsistent validation or stale result behavior. | Centralize required-term validation and add tests for direct URL variable paths. |
| Medium | Feature gates such as BabelFish and diehard deeply affect UI fields and sections. | Product owners and QA can miss hidden combinations. | Maintain a feature-gate test matrix for RNAdb, noncoding, and in vivo scenarios. |
| Medium | 1 nmol minimum warning depends on UI-maintained selection count. | Warning can become inconsistent if add/remove events are missed. | Recalculate from shopping-list contents after each add/remove instead of relying only on incremental state. |
| Medium | Some external links and help URLs appear legacy or hardcoded. | Broken links can reduce scientific confidence and supportability. | Validate NCBI, RNAdb, help, citation, and tutorial links in scheduled link checks. |
| Low | Previous and Next button image state is manually toggled. | Accessibility and keyboard behavior may be weak. | Convert image buttons to accessible button controls during UI modernization. |
| Low | Product group rows and supplemental rows are hidden by inline style. | Dynamic row groups can be hard to test and maintain. | Use explicit CSS classes and ARIA-expanded state for expandable groups. |

## 21. Areas for Improvement

| Area | Current State | Suggested Improvement |
|---|---|---|
| UI architecture | Legacy PHP renders significant markup and JavaScript handlers. | Move search form, result rows, product groups, and shopping-list actions toward componentized UI modules with testable state. |
| Data contracts | Product row values are encoded into select option values and hidden fields. | Introduce structured row metadata with clear schema for SKU, part number, size, purity, inventory, validity, and species. |
| Accessibility | Image buttons, inline links, and popup-only help are used in several places. | Add semantic buttons, accessible labels, keyboard navigation, focus management, and ARIA states. |
| Validation | Quantity and search-term validation are partially client-side and partially server-rendered. | Add shared validation utility and unit/browser tests for invalid inputs. |
| Observability | Launch logging exists, but UI error and event visibility is limited in reviewed source. | Add structured analytics and frontend error logging for search failure, add-to-list failure, and map load failure. |
| Feature flags | BabelFish and diehard gates change field and section visibility. | Document feature-flag defaults and expected production/QA combinations. |
| Link maintenance | External science and help links are embedded in page templates. | Centralize link configuration and run automated link validation. |
| Regression safety | Product groups contain complex row-hiding and add-all behavior. | Add browser tests for show additional, Add All, map sync, and 1 nmol warning behavior. |

## 22. Developer Traceability Matrix

| Requirement | Primary Module | Key Function / Element | Notes |
|---|---|---|---|
| Load siRNA landing page | `index.php` | document ready block, Search Database link | Sets title and launch logging. |
| Route direct URL vars | `index.php`, `search.php` | URL var checks for gene, accession, RNAdb, siRNA ID, and assay ID | Supports deep links into search or product details. |
| Render search form | `search.php` | `sirnaSearchForm`, `searchType`, `searchCriteria`, `searchSpecies`, `searchTerm` | Form is server-rendered. |
| Submit search | `sirna.js` | `sirnaSearch` | Builds post data and calls tab navigation. |
| Render target results | `search.php` | Primary Target and Secondary Targets tables | Select calls `sirnaSelectProduct`. |
| Open product details | `sirna.js`, `select_assays.php` | `sirnaSelectProduct`, `Nav.tabClickWithPostData` | Enables productdetails tab. |
| Render gene details | `select_assays.php` | Gene Details table | Includes aliases, transcripts, pathways. |
| Render product group | `select_assays.php` | `sise`, `ncsise`, `sirna`, `ge` groups | Displays product rows when result arrays have records. |
| Toggle hidden products | `sirna.js` | `toggleAdditionalProducts` | Initial row limits differ by product type. |
| Add one row | `sirna.js` | `sirnaAddToList`, `sirnaGetProdObjByRow` | Builds product object and adds to shopping list. |
| Add all rows | `sirna.js` | `sirnaAddAllToList` | Adds visible addable rows only. |
| Handle direct result add | `sirna.js` | `sirnaAddSirnaFromSearch` | Used by direct siRNA ID result table. |
| Enable order tabs | `sirna.js` | `sirna_product_selected`, `sirnaEnableOrderTabs` | Depends on shopping-list count. |
| Disable order tabs | `sirna.js` | `sirna_product_deselected`, `sirnaDisableOrderTabs` | Runs when cart is empty after remove. |
| Maintain map state | `sirna.js` | `map.selectFeature`, `removeFromMap`, `removeAllFromMap` | Applies when map object exists. |

## 23. Open Validation Items

| ID | Item | Owner / Follow-up |
|---|---|---|
| VAL-SIRNA-001 | Confirm whether the production URL currently uses the legacy GeneAssist eTools UI, a Magellan wrapper, or a newer UI shell before implementation planning. | UI owner / platform owner |
| VAL-SIRNA-002 | Confirm production defaults for BabelFish and diehard feature gates. | Product owner / release owner |
| VAL-SIRNA-003 | Confirm whether `updateSelectedSiSelProduct` is still maintained in shared scripts and whether it handles all size/purity selector variants. | UI developer |
| VAL-SIRNA-004 | Confirm active behavior for custom design and custom synthesis ID flows, including `xsirna_id`. | Product owner / QA |
| VAL-SIRNA-005 | Validate all external reference, help, tutorial, citation, NCBI, and RNAdb links. | QA / content owner |
| VAL-SIRNA-006 | Validate that shopping-list product object fields match downstream order form requirements. | UI and backend developers |
| VAL-SIRNA-007 | Validate wildcard keyword behavior for `/order/rnai/siRNA/result?keyword=*` against production search infrastructure. | Search platform owner |

