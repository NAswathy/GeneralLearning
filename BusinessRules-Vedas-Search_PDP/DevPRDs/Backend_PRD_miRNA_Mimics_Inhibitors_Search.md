# Backend Developer PRD: miRNA Mimics and Inhibitors Search

| Field | Details |
| --- | --- |
| Document name | Backend Developer PRD: miRNA Mimics and Inhibitors Search |
| Version | 1.0 |
| Date | July 31, 2026 |
| Tool URL | `https://www.thermofisher.com/order/rnai/miRNA/result?keyword=*` |
| Audience | Backend developers, service owners, QA engineers, integration teams, and product owners |
| Repositories reviewed | `thermofisher/magellan-search`, `thermofisher/tfcom-magellan-product-service`, `thermofisher/tfcom-magellan-etools`, `thermofisher/magellan-data-scripts`, `thermofisher/magellan-core` |
| Prompt mode | Multi-repo review using the earlier business-rule extraction prompt as the evidence discipline |
| Template reference | Backend Developer PRD with tables created earlier |
| Evidence rule | Include only behavior supported by reviewed repository files. Mark gaps as validation pending. |

## 1. Document Purpose

| Area | Definition |
| --- | --- |
| Purpose | Define backend behavior and developer-facing implementation requirements for the miRNA Mimics and Inhibitors Search tool. |
| Primary user flow | A user searches for miRNA mimics and inhibitors using `/order/rnai/miRNA/result?keyword=*` or a keyword-specific version of that route. |
| Backend focus | URL routing, product type/subtype resolution, search query creation, product count grouping, search result transformation, miRNA result enrichment, related assay/reagent handling, product-service count integration, and legacy related-product support. |
| Out of scope | Visual design, frontend styling, copy not backed by reachable code, and unreviewed downstream services. |
| Validation stance | The document is a backend PRD with explicit repository evidence. It is not a claim that every repo was fully exhausted. Repos without direct evidence are listed in the validation report. |

## 2. Source Evidence and Review Boundary

| Repository | Reviewed files | Evidence depth | Backend relevance |
| --- | --- | --- | --- |
| `thermofisher/magellan-search` | `RelatedAssayAction.java`, `UnifiedCardProductTypeCountAction.java`, `RedirectInterceptor.java`, `MagellanQueryObjectCreator.java`, `GenomicProductTypeQueryAction.java`, `GenomicProductTypeQueryActionHelper.java`, `searchResults.jsp`, miRNA Angular component/template as backend contract clues | Method-level and route-level | Primary web/search orchestration for the miRNA result page, product type grouping, related assay lookup, search result model population, redirect behavior, and UI-backed data contract. |
| `thermofisher/magellan-core` | `MagellanSearchConstants.java`, `ProductConstants.java`, `ProductDefinitions.java`, `CurrentSearch.java`, `MagellanTranslations.properties` | Constants and mapping-level | Shared product type identifiers, subtype constants, FAST field mapping, display labels, assay type descriptions, and current-search state mapping. |
| `thermofisher/tfcom-magellan-product-service` | `CollectionTypeEnum.java`, Mercury Swagger `swagger.yaml` | API/enum-level | Product-count and collection mapping support for `MIRNA_MIMICS_INHIBITORS` / `miRNAMimics`. |
| `thermofisher/tfcom-magellan-etools` | `src/tools/ga_apps/miRNA/custommirna/otherproducts.php` | Legacy workflow-level | Legacy custom miRNA related-products workflow with inhibitor/mimic controls, quantity, package options, and related product add behavior. |
| `thermofisher/magellan-data-scripts` | Repository search for `miRNA`, `MIRNA`, `mimic`, `inhibitor`, `rnai`, `miRNAMimics`, `Solr`, and `FAST` | No direct evidence found | No directly reviewed implementation evidence for this tool. Keep as validation pending for data/load ownership. |

## 3. Product Overview

| Area | Backend PRD definition |
| --- | --- |
| Product/tool name | miRNA Mimics and Inhibitors Search |
| Route family | `/order/rnai/miRNA/result?keyword=` |
| Main product type | MicroRNA / miRNA |
| Main subtype | Mimics/Inhibitors |
| Search grouping key | `MIRNA_MIMICS_INHIBITORS` |
| Product-service collection evidence | `MIRNA_MIMICS_INHIBITORS` maps to collection `miRNAMimics` and request handler `/miRNAMimics-SiteSrch` in `CollectionTypeEnum`. |
| Business purpose | Allow customers to find miRNA mimic and inhibitor products, view product/assay details, compare related miRNA assay options, and access related reagents or controls where supported. |
| Backend goal | Route search requests consistently, resolve subtype correctly, group mimic/inhibitor product counts, populate miRNA-specific result data, and provide related assay/reagent data to the UI. |

## 4. Repository and Module Map

| Repository | Module / file | Important class / method / section | Responsibility |
| --- | --- | --- | --- |
| `magellan-search` | `src/main/java/com/lifetech/magellan/interceptor/RedirectInterceptor.java` | `intercept(...)` | Redirects genome-database miRNA Mimics/Inhibitors requests to `/order/rnai/miRNA/result?keyword=...`. |
| `magellan-search` | `src/main/java/com/lifetech/magellan/action/GenomicProductTypeQueryAction.java` | `execute()` | Builds product type count response, normalizes keyword, uses cache, and optionally returns gene data. |
| `magellan-search` | `src/main/java/com/lifetech/magellan/action/GenomicProductTypeQueryAction.java` | `mapGenomicProductsCounts(...)` | Builds FAST query, applies entitlement and status filters, and populates product type hit counts. |
| `magellan-search` | `src/main/java/com/lifetech/magellan/action/GenomicProductTypeQueryAction.java` | `getFastProductTypeHits(...)` | Reads product type and product subtype navigators; groups `mimic`, `inhibitor`, `antimir`, and `premir` into `MIRNA_MIMICS_INHIBITORS`. |
| `magellan-search` | `src/main/java/com/lifetech/magellan/action/GenomicProductTypeQueryAction.java` | `collectProductSubtypes(...)` | Stores miRNA subtype groups using `MirnaSubtypes`. |
| `magellan-search` | `src/main/java/com/lifetech/magellan/search/helper/GenomicProductTypeQueryActionHelper.java` | `MirnaSubtypes` enum | Defines ordered miRNA subtype grouping, with `MIRNA_MIMICS_INHIBITORS` ranked after advanced, TaqMan, and QuantiGene miRNA. |
| `magellan-search` | `src/main/java/com/lifetech/magellan/action/UnifiedCardProductTypeCountAction.java` | `UnifiedCardEnum.MIRNA_MIMICS_AND_INHIBITORS` | Defines unified card label, product type key, search URL, analytics parameter, and display order. |
| `magellan-search` | `src/main/java/com/lifetech/magellan/action/UnifiedCardProductTypeCountAction.java` | `execute()` | Builds unified card product details, links, counts, image link, and 404 behavior when total count is zero. |
| `magellan-search` | `src/main/java/com/lifetech/magellan/search/results/postprocess/MagellanQueryObjectCreator.java` | `populateResult(...)` | Creates `MiRNAProduct` instances for `PRODUCT_MIRNA` search results. |
| `magellan-search` | `src/main/java/com/lifetech/magellan/search/results/postprocess/MagellanQueryObjectCreator.java` | `populateMiRNAProductAttributes(...)` | Populates miRNA-specific result attributes including assay name, assay design, species, mature names/accessions, aliases, related products, target sequence, miRNA type, flags, and comments. |
| `magellan-search` | `src/main/java/com/lifetech/magellan/action/RelatedAssayAction.java` | `execute()` | Retrieves related miRNA products from assay details; for `mirnainhib`, requests `mimic/inhibitor` related products. |
| `magellan-search` | `src/main/webapp/jsp/searchResults.jsp` | `targetTypeSelect == microrna_mimics_inhibitors` branch | Displays the selected product type as `Mimics/Inhibitors` and sets search hidden fields. |
| `magellan-core` | `ProductDefinitions.java` | `PRODUCT_MIRNA`, `MIRNA_MI` | Defines numeric product type and subtype constants for miRNA and mimics/inhibitors. |
| `magellan-core` | `CurrentSearch.java` | `PRODUCT_MIRNA` branch | Maps `microrna_mimics_inhibitors` to `MIRNA_MI`. |
| `magellan-core` | `ProductConstants.java` | `STRING_PRODUCT_SUB_MIRNA_MIMICS_INHIBITORS`, miRNA assay type constants | Defines display label and assay type strings for mimic, inhibitor, antimir, premir, and related miRNA descriptions. |
| `magellan-core` | `MagellanSearchConstants.java` | `MIRNA_PRODUCT_FAST_FIELDS` | Defines FAST fields used to populate miRNA result cards. |
| `tfcom-magellan-product-service` | `CollectionTypeEnum.java` | `MIRNA_MIMICS_INHIBITORS` | Maps product-service type to collection `miRNAMimics` and request handler `/miRNAMimics-SiteSrch`. |
| `tfcom-magellan-product-service` | `swagger.yaml` | `/productSearchCount`, `/getProductSearchCount` | Documents product-count APIs and example responses containing `MIRNA_MIMICS_INHIBITORS`. |
| `tfcom-magellan-etools` | `otherproducts.php` | `custommirna` related products flow | Supports legacy custom miRNA related product selection for inhibitor and mimic controls. |

## 5. Backend Functional Architecture

### 5.1 System Context Diagram

| Level | Component | Level 2 module / function | Backend responsibility |
| --- | --- | --- | --- |
| Entry | Browser or client | `/order/rnai/miRNA/result?keyword=*` | Initiates miRNA Mimics/Inhibitors search request. |
| Routing | `magellan-search` | `RedirectInterceptor.intercept(...)` | Redirects genome-database miRNA mimic/inhibitor selections to the RNAi miRNA result route. |
| Search state | `magellan-core` | `CurrentSearch` and `ProductDefinitions` | Converts product type/subtype request strings into internal search constants. |
| Product counts | `magellan-search` | `GenomicProductTypeQueryAction.execute()` and `getFastProductTypeHits(...)` | Builds product type count map and groups mimic/inhibitor variants. |
| Search results | `magellan-search` | `MagellanQueryObjectCreator.populateResult(...)` | Converts FAST query documents into `MiRNAProduct` result objects. |
| Result enrichment | `magellan-search` | `populateMiRNAProductAttributes(...)` | Populates miRNA-specific attributes required by the search result page. |
| Unified cards | `magellan-search` | `UnifiedCardProductTypeCountAction` | Presents miRNA Mimics/Inhibitors in unified-card product count results. |
| Product count service | `tfcom-magellan-product-service` | `CollectionTypeEnum`, `/productSearchCount` | Supports collection/request-handler mapping and count API for miRNA mimic/inhibitor product counts. |
| Related assays | `magellan-search` | `RelatedAssayAction.execute()` | Fetches related mimic/inhibitor products from assay-details service when `mirnainhib` is supplied. |
| Legacy related products | `tfcom-magellan-etools` | `custommirna/otherproducts.php` | Provides legacy related product/control selection for custom miRNA flows. |

### 5.2 Search Request Workflow Diagram

| Flow step | Level 1 backend action | Level 2 method / condition | Expected outcome |
| --- | --- | --- | --- |
| 1 | Receive route | `/order/rnai/miRNA/result?keyword=*` | Request enters the miRNA result page flow. |
| 2 | Normalize redirected legacy route | `RedirectInterceptor.intercept(...)` checks `producttypeselect` contains `microrna` and `targettypeselect` contains `microrna_mimics_inhibitors` | Genome-database requests are permanently redirected to `/order/rnai/miRNA/result?keyword={keyword} {productSubType} {species}`. |
| 3 | Resolve search state | `CurrentSearch` maps product type `microrna` to `PRODUCT_MIRNA` | Search is treated as miRNA. |
| 4 | Resolve subtype | `CurrentSearch` maps `microrna_mimics_inhibitors` to `MIRNA_MI` | Search is scoped to Mimics/Inhibitors subtype. |
| 5 | Build FAST query | `GenomicProductTypeQueryAction.mapGenomicProductsCounts(...)` builds keyword query, product status filter, entitlement filter, and client-specific exclusions | Search counts are generated against active, entitled products unless configuration says otherwise. |
| 6 | Group product types | `getFastProductTypeHits(...)` reads `productsubtypenavigator` | `mimic`, `inhibitor`, `antimir`, and `premir` counts are grouped into `MIRNA_MIMICS_INHIBITORS`. |
| 7 | Sort and cache | `sortByHitCount(...)`, `MagellanCacheHandler` | Product type counts are sorted by count and cached only under implemented timing/error conditions. |
| 8 | Render result page contract | `searchResults.jsp` branch for `microrna_mimics_inhibitors` | Product type label is shown as `Mimics/Inhibitors`. |

### 5.3 Result Transformation Workflow Diagram

| Flow step | Level 1 backend action | Level 2 method / field source | Expected outcome |
| --- | --- | --- | --- |
| 1 | Read FAST documents | `MagellanQueryObjectCreator.populateResult(...)` | `PRODUCT_MIRNA` results are converted into `MiRNAProduct` objects. |
| 2 | Populate common product values | `populateProductAttributes(...)` | Product ID, web ID, species, availability, subtype, publication count, package ID, match keyword, recommended flag, badge, citations, and Bioz rating are populated. |
| 3 | Populate genomic values | `populateGenomicProductAttributes(...)` | Chromosome location, assay set, control flag, important info, obsolete/replaced status, validation, build, source, and document id are populated. |
| 4 | Populate miRNA values | `populateMiRNAProductAttributes(...)` with `MIRNA_PRODUCT_FAST_FIELDS` | Assay name, assay design, other species, stem-loop values, mature values, miRBase values, related products, target sequence, aliases, flags, and comments are populated. |
| 5 | Filter aliases by species | `populateMiRNAProductAttributes(...)` compares product aliases against `currentSearch.getSpeciesSet()` | Non-control aliases are retained only for selected species unless all species is selected. |
| 6 | Format miRNA type | `populateMiRNAProductAttributes(...)` transforms `mirnaType` text | miRNA type display is formatted for trademarks, Pri-miRNA, italic `mir`, advanced controls, and Advanced miRNA `NEW` callout. |
| 7 | Expose tab flags | `setHasMature`, `setHasPri`, `setHasMI`, `setHasComments` | UI can show or hide Mature miRNA Assays, Pri-miRNA Assays, Mimics/Inhibitors, and comment-related sections. |

### 5.4 Unified Card Count Workflow Diagram

| Flow step | Level 1 backend action | Level 2 method / condition | Expected outcome |
| --- | --- | --- | --- |
| 1 | Receive unified count request | `UnifiedCardProductTypeCountAction.execute()` | Product type count response is requested unless a filter is applied. |
| 2 | Map product hits to cards | Iterate `UnifiedCardEnum.values()` | `MIRNA_MIMICS_AND_INHIBITORS` uses product type key `MIRNA_MIMICS_INHIBITORS`. |
| 3 | Build miRNA mimic/inhibitor link | `UnifiedCardEnum.MIRNA_MIMICS_AND_INHIBITORS` | Link uses `/order/rnai/miRNA/result?keyword=` plus keyword and analytics. |
| 4 | Add analytics separator | `execute()` adds `&` for siRNA, miRNA Mimics/Inhibitors, and TaqMan cards | miRNA Mimics/Inhibitors receives analytics as an ampersand parameter after `keyword=`. |
| 5 | Set image identifier | `execute()` checks label `miRNA mimics and inhibitors` | Unified card image link is set to `miRNA2`. |
| 6 | Apply ordering | `UnifiedCardEnum` order value | miRNA Mimics/Inhibitors appears after siRNA and before no later enum items because its order is `12`. |
| 7 | Empty result behavior | `execute()` sets HTTP 404 when total count is zero | Empty total count produces an error result rather than a success card payload. |

### 5.5 Related Assay and Related Product Workflow Diagram

| Flow step | Level 1 backend action | Level 2 method / condition | Expected outcome |
| --- | --- | --- | --- |
| 1 | Request related miRNA products | `RelatedAssayAction.execute()` | Related assay lookup uses `assayDetailsServiceURL` with `AssayType=MIRNA` and `AssayId`. |
| 2 | Identify Mimics/Inhibitors module | `mirnainhib != null` branch | Action is treated as the Mimics/Inhibitors module on the miRNA results page. |
| 3 | Fetch related products | `SAXUtilities.getMirnaProducts(..., "mimic/inhibitor", assayDetailsURL)` | Related products are limited to mimic/inhibitor type from assay details. |
| 4 | Return action result | `return MIMIC` | Caller receives the mimic/inhibitor related-products result state. |
| 5 | Legacy related products | `custommirna/otherproducts.php` | Legacy custom miRNA flow can show popular controls and allow add actions with default quantity `1`. |

## 6. Backend Rules and Functional Requirements

### 6.1 Routing and URL Rules

| Rule ID | Source | Rule / requirement | Developer note |
| --- | --- | --- | --- |
| MIRNA-BE-001 | `RedirectInterceptor.intercept(...)` | If a genome-database request contains `producttypeselect` with `microrna` and `targettypeselect` with `microrna_mimics_inhibitors`, the backend redirects to `/order/rnai/miRNA/result?keyword={keyword} {productSubType} {species}`. | Redirect location is trimmed before returning `permRedirectRequest`. |
| MIRNA-BE-002 | `searchResults.jsp` | When `targetTypeSelect` is `microrna_mimics_inhibitors`, the result-page product type label is `Mimics/Inhibitors`. | This confirms the URL represents the Mimics/Inhibitors subtype. |
| MIRNA-BE-003 | `UnifiedCardProductTypeCountAction.UnifiedCardEnum` | The unified card for miRNA Mimics/Inhibitors uses route `/order/rnai/miRNA/result?keyword=`. | Analytics parameter key is `ICID=srch-uc-mirna1`. |
| MIRNA-BE-004 | `ProductConstants.RESTFUL_PRODUCT_TYPE_NAMES_` | Product type names `microrna` and `mirna` are normalized to readable miRNA route values. | Route normalization is shared from `magellan-core`. |

### 6.2 Product Type and Subtype Rules

| Rule ID | Source | Rule / requirement | Developer note |
| --- | --- | --- | --- |
| MIRNA-BE-005 | `ProductDefinitions` | miRNA is represented by `PRODUCT_MIRNA`; Mimics/Inhibitors is represented by `MIRNA_MI`. | Numeric constants are shared by search-state and result transformation code. |
| MIRNA-BE-006 | `CurrentSearch` | `microrna` and `mirna` are mapped to product type `PRODUCT_MIRNA`. | Product type conversion uses `LOOKUP_TABLE.PRODUCT_TYPE_IDENTIFIER_GENERAL`. |
| MIRNA-BE-007 | `CurrentSearch` | Product subtype `microrna_mimics_inhibitors` maps to `MIRNA_MI`. | If no supported miRNA subtype is matched, subtype falls back to `NULL_NULL`. |
| MIRNA-BE-008 | `ProductConstants` | `mirna-mimics-inhibitors` and `microrna-mimics-inhibitors` both display as `Mimics/Inhibitors`. | Both route spellings are supported in the shared subtype display map. |
| MIRNA-BE-009 | `ProductConstants` | miRNA assay types include `mimic`, `inhibitor`, `antimir`, and `premir`. | These are the assay-type values used around mimic/inhibitor grouping and descriptions. |
| MIRNA-BE-010 | `GenomicProductTypeQueryActionHelper.MirnaSubtypes` | `MIRNA_MIMICS_INHIBITORS` is an explicit miRNA subtype and has rank `4` in the miRNA subtype set. | Ordered after `ADVANCED_MIRNA`, `TAQMAN_MIRNA`, and `QUANTIGENE_MIRNA`. |

### 6.3 Search Query and Count Rules

| Rule ID | Source | Rule / requirement | Developer note |
| --- | --- | --- | --- |
| MIRNA-BE-011 | `GenomicProductTypeQueryAction.execute()` | If `taqManSearch=YES` and the keyword does not start with `*`, question marks are replaced with spaces; otherwise asterisks are removed and question marks are replaced with spaces. | This affects wildcard behavior for the tool URL `keyword=*`. |
| MIRNA-BE-012 | `GenomicProductTypeQueryAction.execute()` | The keyword string `anti-` is normalized to `anti ` before FAST escaping. | Applies globally in this action, including miRNA searches. |
| MIRNA-BE-013 | `GenomicProductTypeQueryAction.execute()` | Search mode defaults to `simpleall`; search modes `or`, `any`, `simpleany`, and `simple_any` are allowed to become `simpleany` only when the keyword length is less than `50`. | Prevents long `or` style FAST queries. |
| MIRNA-BE-014 | `mapGenomicProductsCounts(...)` | FAST query excludes `QuantiGene Singleplex miRNA Control`. | Implemented as an explicit `NOT productsubtype` condition. |
| MIRNA-BE-015 | `mapGenomicProductsCounts(...)` | FAST query includes only `productsearchstatus` value `1`. | This means counts are based on active/published search-status products in the reviewed code. |
| MIRNA-BE-016 | `mapGenomicProductsCounts(...)` | Unless `showUnentitled` is `ON`, the query applies entitlement using the request country code plus `all`. | Country entitlement comes through `EntitlementHelper.getEntitlementCountryCode(countryCode)`. |
| MIRNA-BE-017 | `mapGenomicProductsCounts(...)` | If the client contains `fishersci`, configurable products are excluded from genomic product count results. | Implemented with `genericsep13` configurable exclusion. |
| MIRNA-BE-018 | `getFastProductTypeHits(...)` | FAST product type `MIRNA` is initially counted as `TAQMAN_MIRNA`. | Later product subtype logic may subtract advanced miRNA from this count. |
| MIRNA-BE-019 | `getFastProductTypeHits(...)` | Product subtype values `mimic`, `inhibitor`, `antimir`, and `premir` are grouped into `MIRNA_MIMICS_INHIBITORS`. | Count is accumulated across those four modifier values. |
| MIRNA-BE-020 | `getFastProductTypeHits(...)` | Product subtype values for advanced miRNA can be removed from the broader `TAQMAN_MIRNA` count and counted under `ADVANCED_MIRNA`. | Prevents advanced miRNA from remaining double-counted in the broader miRNA bucket. |
| MIRNA-BE-021 | `getFastProductTypeHits(...)` | Advanced miRNA and advanced control miRNA counts are added together into `ADVANCED_MIRNA` when either key exists. | Implemented after navigator processing. |
| MIRNA-BE-022 | `getFastProductTypeHits(...)` | miRNA control assay and standard miRNA assay counts are added together into `MIRNA_CONTROL_ASSAY` when either key exists. | Implemented after navigator processing. |
| MIRNA-BE-023 | `GenomicProductTypeQueryAction.execute()` | Genomic search count results are cached under `genomicSearchResultsCache` only when no cache entry exists, no error is set, and total processing time is greater than configured `siteSearchProcessTimeout`. | The cache key includes country, keyword, mode, client-filter flag, and `fishersci` marker when applicable. |

### 6.4 Result Data Population Rules

| Rule ID | Source | Rule / requirement | Developer note |
| --- | --- | --- | --- |
| MIRNA-BE-024 | `MagellanQueryObjectCreator.populateResult(...)` | For `PRODUCT_MIRNA`, each returned FAST document is converted into a `MiRNAProduct`. | Product, genomic, and miRNA-specific attributes are populated in sequence. |
| MIRNA-BE-025 | `populateProductAttributes(...)` | Product results receive product type, product ID, web ID, species, availability, product subtype, publication count, package ID, batch search field, match keyword, recommendation flag, product badge, last published time, citations, and Bioz rating. | Common product attributes are shared across product types. |
| MIRNA-BE-026 | `populateGenomicProductAttributes(...)` | Products whose subtype contains `control` or whose species contains `Artificial Control` are marked as control assays. | This impacts UI sections and visibility. |
| MIRNA-BE-027 | `populateGenomicProductAttributes(...)` | If validation is missing, validation is set to `No`. | Null validation is normalized to a business-visible value. |
| MIRNA-BE-028 | `populateGenomicProductAttributes(...)` | Source value `NCBI` is suppressed to an empty source display value. | Other source values are preserved. |
| MIRNA-BE-029 | `populateMiRNAProductAttributes(...)` | For miRNA control subtypes, `Artificial Control;` is removed from the displayed species string. | Applies to control, advanced control, advanced assay control, and assay control subtype constants. |
| MIRNA-BE-030 | `populateMiRNAProductAttributes(...)` | Hyphen species values are replaced with an empty string. | Implemented with `replace("-", STRING_NULL)`. |
| MIRNA-BE-031 | `populateMiRNAProductAttributes(...)` | miRNA result records receive assay name, assay design, other species, stem-loop values, mature sequence/accession/name values, context sequence, related products, assay design abbreviation, pools flag, product aliases, gene family fields, target sequence, miRNA type, mature/Pri/MI flags, and comments flag. | Field names are defined in `MIRNA_PRODUCT_FAST_FIELDS`. |
| MIRNA-BE-032 | `populateMiRNAProductAttributes(...)` | Target sequence uses the first semicolon-separated target sequence value when any value is present. | Additional target sequence values are not used by this method. |
| MIRNA-BE-033 | `populateMiRNAProductAttributes(...)` | For non-control miRNA products with aliases, aliases are filtered to selected species unless all species is selected. | Species is inferred from the alias prefix through `SpeciesUtil`. |
| MIRNA-BE-034 | `populateMiRNAProductAttributes(...)` | miRBase version text in aliases is wrapped in parentheses. | Implemented with regex replacement for version patterns like `v...`. |
| MIRNA-BE-035 | `populateMiRNAProductAttributes(...)` | For Pri-miRNA subtype, stem-loop IDs and stem-loop accessions are recalculated through the names/accessions update logic. | Applies only when `targetTypeSelect == MIRNA_PRI`. |
| MIRNA-BE-036 | `populateMiRNAProductAttributes(...)` | miRNA type display is transformed to include registered/trademark markup, Pri formatting, and italic `mir` formatting. | Markup becomes part of display content. |
| MIRNA-BE-037 | `populateMiRNAProductAttributes(...)` | Advanced miRNA control display is changed to `TaqMan Advanced miRNA Assays (Recommended as Control)` with a `NEW` callout. | Directly implemented display rule. |
| MIRNA-BE-038 | `populateMiRNAProductAttributes(...)` | Advanced miRNA assay display receives a `NEW` callout. | Applies when normalized miRNA type contains `advancedmirnaassays`. |

### 6.5 Related Product and Related Assay Rules

| Rule ID | Source | Rule / requirement | Developer note |
| --- | --- | --- | --- |
| MIRNA-BE-039 | `RelatedAssayAction.execute()` | The action reads `assayDetailsServiceURL` and calls it with `AssayType=MIRNA` and the provided assay ID for miRNA branches. | Applies to primary, mature, and mimic/inhibitor related product flows. |
| MIRNA-BE-040 | `RelatedAssayAction.execute()` | If `mirnainhib` is present, the action retrieves related products using related type `mimic/inhibitor` and returns the `mimic` result state. | This is the explicit related-assay branch for Mimics/Inhibitors. |
| MIRNA-BE-041 | `RelatedAssayAction.execute()` | Mature miRNA related product lookup combines `advanced` products with `taqman` products. | Included because it is a nearby related miRNA branch shown on the same result experience. |
| MIRNA-BE-042 | `tfcom-magellan-etools/otherproducts.php` | Legacy custom miRNA related product selection shows only popular products according to page copy. | The file renders “Only the most popular products are shown.” |
| MIRNA-BE-043 | `tfcom-magellan-etools/otherproducts.php` | Related inhibitor and mimic controls default quantity input to `1` and limit entry to numeric-only input with `maxlength=3`. | Supports legacy related-product add flow. |
| MIRNA-BE-044 | `tfcom-magellan-etools/otherproducts.php` | mirVana inhibitor and mimic control product rows offer fixed package options by catalog number and size. | Examples include 5 nmol, 20 nmol, 50 nmol HPLC/InVivo Ready, and 250 nmol HPLC/InVivo Ready in reviewed rows. |

### 6.6 Product-Service API and Collection Rules

| Rule ID | Source | Rule / requirement | Developer note |
| --- | --- | --- | --- |
| MIRNA-BE-045 | `CollectionTypeEnum.MIRNA_MIMICS_INHIBITORS` | Product service maps `MIRNA_MIMICS_INHIBITORS` to label `Mimics_Inhibitor`, collection `miRNAMimics`, and request handler `/miRNAMimics-SiteSrch`. | This is the direct Mercury/product-service mapping for this tool family. |
| MIRNA-BE-046 | `CollectionTypeEnum.getCollectionName(...)` | Collection lookup matches enum name exactly or by containment; otherwise it throws `InvalidProductException`. | Important for product type/subtype lookup failures. |
| MIRNA-BE-047 | `CollectionTypeEnum.getRequestHandler(...)` | Request-handler lookup matches enum name exactly or by containment; otherwise it throws `InvalidProductException`. | Ensures unsupported type values fail explicitly. |
| MIRNA-BE-048 | Mercury Swagger | `/productSearchCount` supports keyword, product type, product subtype, and species in the request body. | Swagger examples include `MIRNA_MIMICS_INHIBITORS` in `productTypeHits`. |
| MIRNA-BE-049 | Mercury Swagger | `/getProductSearchCount` supports keyword and optional species as query parameters. | Used for quick product-count style lookup. |

## 7. API and Data Contracts

| Contract area | Endpoint / method | Inputs | Outputs / behavior |
| --- | --- | --- | --- |
| RNAi miRNA search route | `/order/rnai/miRNA/result?keyword=` | `keyword` | Search results page for miRNA products, including Mimics/Inhibitors when subtype is resolved accordingly. |
| Redirect source route | `RedirectInterceptor.intercept(...)` | `producttypeselect`, `targettypeselect`, `keyword`, `species`, request URL | Redirects genome-database miRNA Mimics/Inhibitors requests into the RNAi miRNA route. |
| Genomic count action | `GenomicProductTypeQueryAction.execute()` | `keyword`, `countryCode`, `client`, `searchMode`, `taqManSearch`, `geneData` | Product type hit map, product subtype sets, exact match, error/query status, timings, and optional gene detail. |
| FAST result conversion | `MagellanQueryObjectCreator.populateResult(...)` | `FASTQueryObject`, `MagellanSearchForm`, FAST `IQueryResult` | `MagellanQueryObject` containing product result models. |
| MiRNA result enrichment | `populateMiRNAProductAttributes(...)` | FAST document, `MiRNAProduct`, `CurrentSearch` | Populated miRNA product fields and flags used by the result UI. |
| Related assay lookup | `RelatedAssayAction.execute()` | `mirnainhib`, `mirnaprimary`, `mirnamature`, assay id values | Related miRNA product lists for primary, mature, or mimic/inhibitor modules. |
| Product service count | `/api/magellan/product/productSearchCount` | JSON criteria with `keyword`, `productType`, `productSubType`, `species` | Product count response; examples show `MIRNA_MIMICS_INHIBITORS` counts. |
| Product service quick count | `/api/magellan/product/getProductSearchCount` | `keyword`, optional `species` | Product count object. |

## 8. Data Field Mapping

| Data field group | Source enum / file | Fields used for miRNA result behavior |
| --- | --- | --- |
| Common product fields | `MagellanSearchConstants.PRODUCT_FAST_FIELDS` | `productid`, `assaysets`, `species`, `producttype`, `availability`, `productsubtype`, `publicationcount`, `packageid`, `batchidsrchfld`, `recommended`, critical comments, badge, last published time, citations, Bioz rating. |
| Genomic fields | `MagellanSearchConstants.GENOMIC_PRODUCT_FAST_FIELDS` | Chromosome begin/end, beta controlled, assay sets, important info, obsolete/search status, replaced assay, validation status, chromosome, build version, source. |
| miRNA fields | `MagellanSearchConstants.MIRNA_PRODUCT_FAST_FIELDS` | Assay name, assay design, other species, stem-loop names/sequence/accession, mature sequences/accession/names, family accessions/names, target sequence, product aliases, context sequence, related products, assay design abbreviation, miRNA type, comments, pools, mature/advanced/Pri/MI flags. |
| Product subtype display | `ProductConstants` | `Mimics/Inhibitors`, `Mature miRNA`, `Pri-miRNA`, `Controls`, `Advanced miRNA`, QuantiGene miRNA subtype labels. |
| Product-service collection | `CollectionTypeEnum` | `MIRNA_MIMICS_INHIBITORS` maps to `miRNAMimics` and `/miRNAMimics-SiteSrch`. |

## 9. Operations, Caching, and Error Handling

| Area | Implemented / evidenced behavior | Operational requirement |
| --- | --- | --- |
| Query timeout | `siteSearchProductApiTimeout` defaults to `5000` when not configured for FAST product-count query. | Validate timeout in environment config for production. |
| Process timeout | `siteSearchProcessTimeout` controls whether slow successful results are cached. | Confirm configured value and cache TTL outside this code path. |
| Cache key | `Genomic-Search{country}-{keyword}-{mode}-{clientFilterNeeded}` with `fishersci` suffix for FisherSci clients. | Cache keys must include country and keyword to avoid cross-country result bleed. |
| Empty unified-card count | `UnifiedCardProductTypeCountAction.execute()` sets HTTP 404 when total count is `0`. | QA should test zero-result keyword behavior. |
| Product-service invalid type | `CollectionTypeEnum` throws `InvalidProductException` when collection or handler is not found. | Product-service callers should handle invalid type/subtype errors clearly. |
| Search action exception | `GenomicProductTypeQueryAction.execute()` catches exceptions, logs, and still returns `success`. | Support teams need log correlation because user response may not expose internal failure. |
| Redirect | `RedirectInterceptor` returns `permRedirectRequest`. | SEO/canonical and browser behavior should be validated for legacy genome-database URLs. |

## 10. Acceptance Criteria

| ID | Scenario | Acceptance criteria |
| --- | --- | --- |
| AC-001 | Wildcard route | `/order/rnai/miRNA/result?keyword=*` reaches the miRNA result flow without treating the asterisk as a literal heavy FAST wildcard in `GenomicProductTypeQueryAction`. |
| AC-002 | Mimics/Inhibitors route label | When `targetTypeSelect` is `microrna_mimics_inhibitors`, the selected product type label is `Mimics/Inhibitors`. |
| AC-003 | Subtype mapping | `microrna_mimics_inhibitors` maps to `MIRNA_MI` in `CurrentSearch`. |
| AC-004 | Count grouping | FAST product subtype modifiers `mimic`, `inhibitor`, `antimir`, and `premir` are accumulated into `MIRNA_MIMICS_INHIBITORS`. |
| AC-005 | Unified card link | Unified-card miRNA Mimics/Inhibitors points to `/order/rnai/miRNA/result?keyword=` and uses analytics `ICID=srch-uc-mirna1`. |
| AC-006 | Product service mapping | Product-service lookup for `MIRNA_MIMICS_INHIBITORS` resolves to collection `miRNAMimics` and handler `/miRNAMimics-SiteSrch`. |
| AC-007 | Result object | `PRODUCT_MIRNA` search results produce `MiRNAProduct` records with miRNA-specific fields populated. |
| AC-008 | Related products | When `mirnainhib` is supplied to `RelatedAssayAction`, related products are fetched with type `mimic/inhibitor` and the action returns `mimic`. |
| AC-009 | Species alias filtering | Non-control miRNA aliases are filtered by selected species unless all species is selected. |
| AC-010 | Zero count | Unified-card count response returns HTTP 404/error state when total count is zero. |

## 11. Validation Report

| Validation item | Status | Evidence / action needed |
| --- | --- | --- |
| Multi-repo review performed | Completed | All five requested repositories were searched or reviewed for miRNA/RNAi evidence. |
| Primary backend implementation located | Completed | `magellan-search` contains route, search, count, related assay, result transformation, and result-page contract evidence. |
| Shared constants located | Completed | `magellan-core` contains product/subtype constants, current-search mapping, FAST field mapping, labels, and assay type descriptions. |
| Product-service evidence located | Completed | `tfcom-magellan-product-service` contains `MIRNA_MIMICS_INHIBITORS` collection mapping and count API swagger examples. |
| Legacy related-product evidence located | Completed | `tfcom-magellan-etools` contains custom miRNA related products/control selection evidence. |
| Data scripts evidence | Not confirmed | `magellan-data-scripts` searches did not return direct miRNA Mimics/Inhibitors search implementation evidence. Confirm with data owners whether ingestion/index feed scripts live elsewhere or use different terms. |
| Backend service ownership | Validation pending | The reviewed files show implementation behavior, not final service ownership or deployment ownership. |
| Full runtime endpoint chain | Partially confirmed | Product-service collection and search-count APIs are confirmed; exact live call path from the RNAi result page to Mercury count service should be validated in environment configuration. |
| Pricing/add-to-cart backend path for this exact tool | Partially confirmed | UI contract references pricing/add-to-cart services, but full backend pricing/add-to-cart implementation for this exact result page was not fully reviewed in this pass. |

## 12. Suggested Improvements

| Area | Current observation | Improvement |
| --- | --- | --- |
| Product subtype naming | Code uses several related forms: `microrna_mimics_inhibitors`, `MIRNA_MI`, `MIRNA_MIMICS_INHIBITORS`, `MIRNA_MIMICS_AND_INHIBITORS`, and `Mimics/Inhibitors`. | Add a single subtype mapping reference table in developer docs and tests. |
| Count grouping | Mimic/inhibitor count grouping depends on FAST product subtype modifier strings. | Add test coverage for `mimic`, `inhibitor`, `antimir`, and `premir` aggregation. |
| Redirect construction | Redirect keyword concatenates keyword, product subtype, and species using spaces. | Add URL encoding and regression tests for spaces, special characters, and empty species. |
| Error visibility | `GenomicProductTypeQueryAction.execute()` catches exceptions and returns `success`. | Consider exposing a structured error flag to callers while preserving backward compatibility. |
| Cache documentation | Cache key and timing behavior are implemented, but TTL/invalidation was not evident in reviewed files. | Document cache TTL, eviction, and invalidation ownership for genomic search count cache. |
| Product-service matching | `CollectionTypeEnum` supports containment matching. | Add tests to ensure ambiguous type strings do not resolve to an unintended collection. |
| Data ownership | `magellan-data-scripts` did not expose direct evidence for this tool. | Identify authoritative ingestion/indexing repo for `miRNAMimics` and link it to this PRD. |

## 13. Open Questions

| Question | Owner needed |
| --- | --- |
| Which repo owns the ingestion/index feed for `miRNAMimics` collection? | Data/search platform owner |
| Is `/miRNAMimics-SiteSrch` currently the production Solr/Mercury request handler for this result page? | Product-service owner |
| Should `premir` and `antimir` remain grouped with mimic/inhibitor in all UI and count experiences? | Product owner / scientific content owner |
| What is the expected behavior when `keyword=*` is submitted from the public tool URL after keyword normalization? | Search owner / QA |
| Is the legacy `tfcom-magellan-etools` custom miRNA related-products page still active or only retained for backward compatibility? | Etools owner |
| Should full pricing and add-to-cart backend rules for the miRNA result card be added as a second PRD section? | Commerce owner |

## 14. Source Artifacts

| Repository | Source artifact |
| --- | --- |
| `thermofisher/magellan-search` | `src/main/java/com/lifetech/magellan/interceptor/RedirectInterceptor.java` |
| `thermofisher/magellan-search` | `src/main/java/com/lifetech/magellan/action/GenomicProductTypeQueryAction.java` |
| `thermofisher/magellan-search` | `src/main/java/com/lifetech/magellan/search/helper/GenomicProductTypeQueryActionHelper.java` |
| `thermofisher/magellan-search` | `src/main/java/com/lifetech/magellan/action/UnifiedCardProductTypeCountAction.java` |
| `thermofisher/magellan-search` | `src/main/java/com/lifetech/magellan/search/results/postprocess/MagellanQueryObjectCreator.java` |
| `thermofisher/magellan-search` | `src/main/java/com/lifetech/magellan/action/RelatedAssayAction.java` |
| `thermofisher/magellan-search` | `src/main/webapp/jsp/searchResults.jsp` |
| `thermofisher/magellan-search` | `src/main/javascript/modules/elcano/main/src/components/mirna-search-result/mirna-search-result.component.js` |
| `thermofisher/magellan-search` | `src/main/javascript/modules/elcano/main/src/components/mirna-search-result/mirna-search-result.template.html` |
| `thermofisher/magellan-core` | `magellan-core/src/main/java/com/lifetech/magellan/core/misc/ProductDefinitions.java` |
| `thermofisher/magellan-core` | `magellan-core/src/main/java/com/lifetech/magellan/core/genomic/CurrentSearch.java` |
| `thermofisher/magellan-core` | `magellan-core/src/main/java/com/lifetech/magellan/core/genomic/ProductConstants.java` |
| `thermofisher/magellan-core` | `magellan-core/src/main/java/com/lifetech/magellan/core/genomic/MagellanSearchConstants.java` |
| `thermofisher/magellan-core` | `magellan-core/src/main/resources/com/lifetech/magellan/core/translation/MagellanTranslations.properties` |
| `thermofisher/tfcom-magellan-product-service` | `src/main/java/com/thermofisher/productsearchservice/v2/enums/CollectionTypeEnum.java` |
| `thermofisher/tfcom-magellan-product-service` | `src/main/resources/static/swagger-apis/mercury/swagger.yaml` |
| `thermofisher/tfcom-magellan-etools` | `src/tools/ga_apps/miRNA/custommirna/otherproducts.php` |

