# Backend Developer PRD - siRNA Search

| Field | Details |
|---|---|
| Product / Tool | siRNA Search |
| Tool URL | https://www.thermofisher.com/order/rnai/siRNA/result?keyword=* |
| Audience | Backend developers, API developers, QA engineers, business analysts, product owners |
| Document Type | Backend rules document / developer PRD |
| Source Date | 2026-07-31 |
| Primary Verified Repos | thermofisher/magellan-search, thermofisher/tfcom-magellan-etools, thermofisher/tfcom-magellan-product-service, thermofisher/magellan-data-scripts, thermofisher/magellan-core |
| Style Reference | BE_Developer_PRD table-heavy format used for earlier developer PRDs |

## 1. Document Purpose

| Item | Description |
|---|---|
| Purpose | Capture backend rules, repository ownership, modules, functions, APIs, data mappings, and validation observations for the siRNA Search tool. |
| Developer Focus | Identify the source files, classes, methods, query paths, Solr count flow, FAST result mapping, eTools search model, data-script inputs, and cart-related backend rules. |
| Business Focus | Explain how the backend supports siRNA discovery by keyword, gene, transcript, assay ID, siRNA ID, species, application, related products, rankings, and order workflow needs. |
| Scope | Backend routing, result construction, product count service, eTools siRNA model/search workflow, data load/design/ranking support, and cart storage rules. |
| Out of Scope | Frontend rendering details except where backend values directly drive UI state; live production behavior not visible in source. |

## 2. Source Evidence and Review Boundary

| Evidence Type | Repo | File / Module | What Was Verified |
|---|---|---|---|
| Request redirect and canonical route handling | thermofisher/magellan-search | `src/main/java/com/lifetech/magellan/interceptor/RedirectInterceptor.java` | siRNA request detection, subtype normalization, route redirect to `/order/rnai/siRNA/result`, assay ID redirect behavior. |
| Search result object creation | thermofisher/magellan-search | `src/main/java/com/lifetech/magellan/search/results/postprocess/MagellanQueryObjectCreator.java` | `PRODUCT_SIRNA` result path, `SiRNAProduct` creation, shared genomic/gene attributes, siRNA-specific FAST field population. |
| siRNA product bean | thermofisher/magellan-search | `src/main/java/com/lifetech/magellan/bean/SiRNAProduct.java` | Backend result fields for status, rank, pathways, library sets, associated siRNA assay, associated GE assay, and Stealth three-pack data. |
| Result post-processing | thermofisher/magellan-search | `src/main/java/com/lifetech/magellan/search/results/postprocess/MagellanProductIteratorFilter.java` | Package ID prefixing for in vivo / in vitro siRNA, Stealth product sorting and three-pack filtering, inventory enrichment. |
| Search result JSP behavior | thermofisher/magellan-search | `src/main/webapp/jsp/searchResults.jsp` | Product type mapping for `sirna`, search result header behavior, gene-detail inclusion for gene-family style results. |
| Product type count / unified card | thermofisher/magellan-search | `src/main/java/com/lifetech/magellan/action/UnifiedCardProductTypeCountAction.java` | Unified-card link construction, special query separator behavior for SIRNA, product-service count usage. |
| FAST / Solr field constants | thermofisher/magellan-core | `magellan-core/src/main/java/com/lifetech/magellan/core/genomic/MagellanSearchConstants.java` | `SIRNA_PRODUCT_FAST_FIELDS` mapping for siRNA status, rank, pathways, library sets, associated assay fields. |
| Site search count service | thermofisher/tfcom-magellan-product-service | `src/main/java/com/thermofisher/productsearchservice/v2/service/SirnaSiteSearchService.java` | Site-search count rules, keyword quoting/sanitization, assay ID detection, Solr search execution. |
| Site search query decorator | thermofisher/tfcom-magellan-product-service | `SirnaSiteSearchQueryDecorator.java` | AND keyword query behavior for siRNA site search. |
| Site search Solr factory | thermofisher/tfcom-magellan-product-service | `SIRNASiteSearchSearcherFactory.java` | `Sirna` Solr collection searcher creation and query binding. |
| Product-service enums | thermofisher/tfcom-magellan-product-service | `SiteSearchProductTypeEnum.java`, `CollectionTypeEnum.java` | SIRNA label/type mapping to `SIRNA`, `Sirna` collection, and `/siRNA-SiteSrch` request handler. |
| eTools siRNA landing/search workflow | thermofisher/tfcom-magellan-etools | `src/tools/ga_apps/sirna/index.php`, `src/tools/ga_apps/sirna/search/search.php` | Legacy GeneAssist siRNA workflow entry, search field options, application option, search-type routing, history, and error handling. |
| eTools siRNA model | thermofisher/tfcom-magellan-etools | `src/tools/ga_apps/sirna/Models/Sirna.class.php` | Search methods by all fields, gene name, gene symbol, gene ID, assay ID, transcript accession, OMIM ID, RNAdb ID, siRNA ID, ranked products, TaqMan GE info, size/purity/options. |
| eTools SQL | thermofisher/tfcom-magellan-etools | `src/tools/ga_apps/sirna/SQL/Sirna_sql.inc.php`, `src/tools/ga_apps/sirna/SQL/sirna_oci_sql.inc.php` | GeneAssist SQL query structure and citations query by product ID. |
| eTools cart storage | thermofisher/tfcom-magellan-etools | `general_mods/cart/class.Cart_SiRna.php` | siRNA cart transcript grouping, species rules, duplicate prevention, pre-designed / validated counts, order-form query-string construction. |
| Data scripts | thermofisher/magellan-data-scripts | `computes/ABAssays/SIRNA_SETUP/siRNA_setup.prop`, `airflow/code/apps/AsRank/sql/ld_sirna_rank.ctl`, `perlmodules/alignMap3/SiRNA.rb` | siRNA design/ranking configuration, rank data load columns, alignment-map siRNA object fields. |

## 3. Product Overview

| Area | Details |
|---|---|
| Product Name | siRNA Search |
| Main Route | `/order/rnai/siRNA/result?keyword=*` |
| Primary Purpose | Allow users to search siRNA-related products and assays by keyword, gene identifiers, transcripts, assay IDs, siRNA IDs, species, and application-related options. |
| Main Product Families Seen in Source | Stealth siRNA, Silencer siRNA, Silencer Select siRNA, Ambion In Vivo siRNA. |
| Backend Goal | Normalize incoming requests, map product subtype/search terms, retrieve product counts/results, enrich result objects, preserve ranking/related product data, and support cart/order workflows. |
| Business Goal | Help users find relevant siRNA products for gene silencing workflows, distinguish coding/noncoding and in vivo/in vitro options, and move selected products into ordering workflows. |

## 4. Users and Stakeholders

| Persona / Stakeholder | Need | Backend Implication |
|---|---|---|
| Research scientist | Search by gene, transcript, assay ID, siRNA ID, or species. | Backend must support multiple search types and fallback behavior. |
| Buyer / procurement user | Add selected siRNAs to cart/order forms. | Cart backend must retain transcript, species, siRNA ID, design code, validation, and catalog number. |
| Product owner | Ensure search supports application choices such as cells vs animals. | Backend must preserve in vitro/in vivo subtype and package ID rules. |
| Backend developer | Understand route, service, model, Solr, FAST, and SQL responsibilities. | PRD maps repositories, files, classes, and key methods. |
| QA engineer | Build API/regression tests for search types, subtype redirects, ranking, and cart rules. | Acceptance criteria and test matrix define expected outcomes. |
| Data engineering owner | Maintain siRNA rank/design data and alignment-map inputs. | Data scripts and load files must match backend field expectations. |

## 5. Repository and Module Map

| Repo | Primary Role | Key Files | Confirmed Backend Responsibility |
|---|---|---|---|
| thermofisher/magellan-search | Magellan search web app and result processing | `RedirectInterceptor`, `MagellanQueryObjectCreator`, `MagellanProductIteratorFilter`, `SiRNAProduct`, `searchResults.jsp`, `UnifiedCardProductTypeCountAction` | Route normalization, result object creation, FAST field mapping, post-processing, product count cards, result page integration. |
| thermofisher/tfcom-magellan-product-service | Site-search product count service | `SirnaSiteSearchService`, `SirnaSiteSearchQueryDecorator`, `SIRNASiteSearchSearcherFactory`, `SiteSearchProductTypeEnum`, `CollectionTypeEnum` | Product-service count/search support for SIRNA using Solr collection/request handler. |
| thermofisher/tfcom-magellan-etools | Legacy GeneAssist siRNA workflow and model | `index.php`, `search/search.php`, `Sirna.class.php`, `Sirna_sql.inc.php`, `sirna_oci_sql.inc.php`, `class.Cart_SiRna.php` | Search form workflow, GeneAssist SQL model, ranked product lookups, size/purity/options, citations, cart/order workflow data. |
| thermofisher/magellan-data-scripts | Data load, rank, design, and alignment-map support | `siRNA_setup.prop`, `ld_sirna_rank.ctl`, `SiRNA.rb` | Design thresholds/tools, rank load columns, siRNA alignment-map object fields. |
| thermofisher/magellan-core | Shared constants and Solr/FAST field mappings | `MagellanSearchConstants.java` | Shared FAST field constants used by result construction and product-service search infrastructure. |

## 6. High-Level Backend Architecture

| Level | Layer | Components | Responsibility |
|---|---|---|---|
| 1 | External route | `/order/rnai/siRNA/result?keyword=*` | User-facing siRNA search result route. |
| 1 | Request normalization | `RedirectInterceptor` | Detect siRNA search inputs and redirect older genome-database requests to the RNai siRNA route. |
| 2 | Search result engine | Magellan search action/services and FAST/Solr result pipeline | Execute product search and create backend result objects. |
| 2 | Product count service | `SirnaSiteSearchService` in product-service | Return site-search counts for SIRNA cards using Solr searcher factory. |
| 2 | eTools workflow | `src/tools/ga_apps/sirna` PHP modules | Support GeneAssist siRNA search, product details, related product and order/cart workflows. |
| 3 | Result object mapping | `MagellanQueryObjectCreator.populateSiRNAProductAttributes` | Populate siRNA fields from FAST fields into `SiRNAProduct`. |
| 3 | Result post-processing | `MagellanProductIteratorFilter` | Apply inventory, package ID prefixing, Stealth three-pack grouping/filtering. |
| 3 | Data support | Data scripts and load control files | Produce rank/design/alignment data consumed by search/detail workflows. |

## 7. Workflow Diagram - Route Normalization

| Step | Module / Method | Condition | Backend Action | Output |
|---|---|---|---|---|
| 1 | Incoming request | Request includes `productTypeSelect` containing `sirna`, `targetTypeSelect` containing `sirna`, or `assayType=sirna`. | `RedirectInterceptor.intercept` enters siRNA redirect logic. | siRNA route processing begins. |
| 2 | `RedirectInterceptor` | Request URL contains `order/genome-database/`. | Reads `productTypeSelect`, `keyword`, `species`, and host config. | Prepares redirect target. |
| 3 | `sirnaProductType` map | Product subtype is one of `sirna_stealth`, `sirna_silencer`, `sirna_silencer_select`, `sirna_in_vivo`. | Maps to `stealth`, `silencer`, `silencerSelect`, or `ambion`. | Normalized subtype string. |
| 4 | Standard siRNA redirect | Not an assay ID detail request. | Builds `/order/rnai/siRNA/result?keyword={keyword} {productSubType} {species}`. | Permanent redirect result. |
| 5 | Assay ID siRNA redirect | `assayType=sirna` and `assayId` is present. | Builds `/order/rnai/siRNA/result?keyword={assayId} {assayType}`. | Permanent redirect result. |
| 6 | Action context | Redirect location set on value stack. | Returns `permRedirectRequest`. | Browser moves to siRNA result route. |

## 8. Workflow Diagram - Magellan Search Result Construction

| Step | Module / Method | Action | Data Used | Output |
|---|---|---|---|---|
| 1 | Search action pipeline | Executes product search and receives query result. | FAST/Solr document summaries. | `IQueryResult`. |
| 2 | `MagellanQueryObjectCreator.populateResult` | Checks `currentSearch.PRODUCT_TYPE`. | `CurrentSearch.PRODUCT_TYPE`. | Enters `PRODUCT_SIRNA` branch. |
| 3 | `PRODUCT_SIRNA` branch | Creates a new `SiRNAProduct` for each document. | `IDocumentSummary`. | Product bean initialized. |
| 4 | `populateProductAttributes` | Populates shared product attributes such as product ID, product type, subtype, package ID, species, availability, and publication fields. | `PRODUCT_FAST_FIELDS`. | Shared product fields set. |
| 5 | `populateGenomicProductAttributes` | Populates genomic fields such as chromosome/build/locations/status. | `GENOMIC_PRODUCT_FAST_FIELDS`. | Genomic fields set. |
| 6 | `populateNonMiRNAProductAttributes` | Populates gene/protein/refseq/alias fields for non-miRNA products. | `NON_MIRNA_PRODUCT_FAST_FIELDS`. | Gene and alias context set. |
| 7 | `populateGeneBasedProductAttributes` | Populates gene-based data such as product coding status, RefSeq coverage, NCBI GI IDs, GenBank IDs, GO/PANTHER values, and RNA DB fields. | `GENE_BASED_PRODUCT_FAST_FIELDS`. | Gene-based context set. |
| 8 | `populateSiRNAProductAttributes` | Populates siRNA-specific status, rank, pathways, library sets, associated assay/package fields. | `SIRNA_PRODUCT_FAST_FIELDS`. | `SiRNAProduct` ready for post-processing. |
| 9 | Result list | Adds result to `MagellanQueryObject`. | Product list. | Search result list returned to the web layer. |

## 9. Workflow Diagram - Product-Service Site Search Counts

| Step | Module / Method | Rule | Result |
|---|---|---|---|
| 1 | `SirnaSiteSearchService.getSiteSearchResults` | Initializes count map for product type `SIRNA`. | Empty count map. |
| 2 | Keyword normalization | If keyword contains a space and is not already quoted, wrap it in double quotes and encode it. | Phrase-style keyword for Solr. |
| 3 | Request model | Builds `SiteSearchRequest` with keyword, ISO country, and product type `SIRNA`. | Site search model. |
| 4 | Special character handling | If keyword is not an assay ID search and contains special characters, replace non-alphanumeric, hyphen, or wildcard characters with spaces and collapse whitespace. | Sanitized keyword. |
| 5 | AND behavior | Sets AND operator true. | Query builder uses logical AND. |
| 6 | `getProductResultsFromSolr` | Builds `SiteSearchParameters` with product type/subtype `SIRNA`, search type `KEYWORD`, row count `0`, query, country, and AND flag. | Count-only search parameters. |
| 7 | `SIRNASiteSearchSearcherFactory` | Uses `TaqManSolrContextFactory` and `ProductCollectionSettings(productSubType)` to create search context. | Solr searcher for `Sirna` collection. |
| 8 | `SirnaSiteSearchQueryDecorator.byKeyword` | Adds logical AND keyword query decorator when AND flag is true. | Solr query. |
| 9 | Query result | Reads `getStatistics().getNumberOfDocumentsFound()`. | Count stored under `SIRNA`. |

## 10. Workflow Diagram - eTools GeneAssist siRNA Search

| Step | Module / Method | Action | Output |
|---|---|---|---|
| 1 | `src/tools/ga_apps/sirna/index.php` | Loads GeneAssist siRNA workflow, sets Magellan/content hosts, handles incoming URL vars, and exposes Search Database entry. | User enters `/order/rnai/siRNA/search` workflow. |
| 2 | `search/search.php` | Reads session/POST state including `search_type`, `search_species`, `search_criteria`, `search_term`, and in vivo option. | Search request variables. |
| 3 | Application option | If diehard feature is not hidden, user can choose cells (`invivo=no`) or animals (`invivo=yes`). | In vivo flag stored in session/request. |
| 4 | Search type cleanup | Maps raw search type to display labels such as Keyword, Gene Name, Gene Symbol, Gene ID, NCBI Transcript, OMIM ID, RNAdb ID, siRNA ID, or TaqMan Assay ID. | Clean history/display metadata. |
| 5 | Search history | Adds unique recent search entries to session history, up to five entries. | Recent Searches list. |
| 6 | Type detection | If search type is `all`, calls `getSearchTypeByTerm` to infer a more specific type where possible. | Search may be changed before querying. |
| 7 | Search routing | Switches by search type and calls the matching `Sirna` model method. | Search result array. |
| 8 | RNAdb enrichment | Many gene-based results call `sirnaSearchRNAdbByGeneId` to attach `ncrna_acc`, `ncrna_gene`, and `ncrna_desc`. | Enriched results. |
| 9 | Sorting / de-dupe | Uses `ranksearch`, `usort`, and `search_result_unique` where applicable. | Deduplicated ranked results. |
| 10 | Error handling | Model error payloads populate warning/error messages. | Warning logged/displayed. |

## 11. Search Type Rules

| Rule ID | Search Type | Backend Method(s) | Rule |
|---|---|---|---|
| BE-SIRNA-ST-001 | All / Keyword | `sirnaSearchAll`, `sirnaSearchRNAdbGeneSymbolAndDesc`, `search_result_unique` | All-field searches check gene symbol, gene name, gene alias, and RNAdb fields; results may be merged, sorted, and deduplicated. |
| BE-SIRNA-ST-002 | Gene Name | `sirnaSearchGeneName` or `sirnaSearchAll` when inferred | Searches gene name and enriches results with RNAdb data by gene ID. |
| BE-SIRNA-ST-003 | Gene Symbol | `sirnaSearchGeneSymbol` | Searches gene symbol and gene alias with species criteria. |
| BE-SIRNA-ST-004 | Gene ID | `sirnaSearchGeneId` | Searches by gene ID and can fall back to OMIM ID or siRNA ID when the original all-field search was inferred. |
| BE-SIRNA-ST-005 | TaqMan Assay ID | `sirnaSearchAssayId` | Searches assay/product ID; may hide noncoding assay records when the `ncassay` feature is hidden. |
| BE-SIRNA-ST-006 | Transcript Accession | `sirnaSearchTranscriptAccession` | Searches transcript accession and enriches results with RNAdb data. |
| BE-SIRNA-ST-007 | OMIM ID | `sirnaSearchOmimId` | Searches OMIM values with species filtering and RNAdb enrichment. |
| BE-SIRNA-ST-008 | RNAdb ID | `sirnaSearchRNAdbId` | Runs only when the BabelFish feature is not hidden. |
| BE-SIRNA-ST-009 | RNAdb Gene Symbol | `sirnaSearchRNAdbGeneSymbol` | Runs only when the BabelFish feature is not hidden. |
| BE-SIRNA-ST-010 | siRNA ID | `sirnaSearchSirnaId`, custom design/synthesis lookups | Handles custom design/synthesis prefixes and regular siRNA IDs; noncoding IDs may be suppressed when BabelFish is hidden. |

## 12. Backend Business Rules

| Rule ID | Area | Rule | Source |
|---|---|---|---|
| BE-SIRNA-001 | Route detection | siRNA redirect logic applies when `productTypeSelect` contains `sirna`, `targetTypeSelect` contains `sirna`, or `assayType` equals `sirna`. | `RedirectInterceptor` |
| BE-SIRNA-002 | Subtype normalization | `sirna_stealth` maps to `stealth`, `sirna_silencer` maps to `silencer`, `sirna_silencer_select` maps to `silencerSelect`, and `sirna_in_vivo` maps to `ambion`. | `RedirectInterceptor.sirnaProductType` |
| BE-SIRNA-003 | Standard redirect | Genome database siRNA search requests redirect to `/order/rnai/siRNA/result?keyword={keyword} {productSubType} {species}`. | `RedirectInterceptor` |
| BE-SIRNA-004 | Assay redirect | Genome database requests with `assayType=sirna` and `assayId` redirect to `/order/rnai/siRNA/result?keyword={assayId} {assayType}`. | `RedirectInterceptor` |
| BE-SIRNA-005 | Result branch | When `CurrentSearch.PRODUCT_TYPE` is `PRODUCT_SIRNA`, the result pipeline creates `SiRNAProduct` objects. | `MagellanQueryObjectCreator.populateResult` |
| BE-SIRNA-006 | Shared fields | siRNA products receive shared product, genomic, non-miRNA, and gene-based attributes before siRNA-specific fields. | `MagellanQueryObjectCreator` |
| BE-SIRNA-007 | siRNA status | `SIRNASTATUS` comes from FAST field `productsearchstatus`. | `SIRNA_PRODUCT_FAST_FIELDS`, `populateSiRNAProductAttributes` |
| BE-SIRNA-008 | Ranking | siRNA rank comes from FAST field `genericsort1`. | `SIRNA_PRODUCT_FAST_FIELDS.RANK` |
| BE-SIRNA-009 | Pathways | siRNA pathways come from FAST field `genericsep7`. | `SIRNA_PRODUCT_FAST_FIELDS.SIRNAPATHWAYS` |
| BE-SIRNA-010 | Library sets | Library sets come from FAST field `genericsep4`. | `SIRNA_PRODUCT_FAST_FIELDS.LIBRARYSETS` |
| BE-SIRNA-011 | Stealth associated products | If product subtype contains `stealth`, associated three-pack ID/package ID are populated and associated siRNA assay fields are set to `-`. | `populateSiRNAProductAttributes` |
| BE-SIRNA-012 | Non-Stealth associated products | If product subtype is not Stealth, associated siRNA assay/package fields are populated and associated three-pack fields are set to `-`. | `populateSiRNAProductAttributes` |
| BE-SIRNA-013 | Associated GE assay | Associated GE assay and package ID are populated for all siRNA products from configured FAST fields. | `populateSiRNAProductAttributes` |
| BE-SIRNA-014 | In vivo package prefix | For subtype `SIRNA_IV`, package ID is prefixed with `invivo`. | `MagellanProductIteratorFilter` |
| BE-SIRNA-015 | In vitro package prefix | For subtype `SIRNA_SS`, package ID is prefixed with `invitro`. | `MagellanProductIteratorFilter` |
| BE-SIRNA-016 | Restful no-subtype package correction | When subtype is `NULL_NULL`, product subtype from FAST can drive package prefix: Silencer Select gets `invitro`, Ambion In Vivo gets `invivo`. | `MagellanProductIteratorFilter` |
| BE-SIRNA-017 | Stealth sort | For all siRNA or Stealth subtype searches, product list is sorted by product ID before Stealth grouping. | `MagellanProductIteratorFilter` |
| BE-SIRNA-018 | Stealth three-pack grouping | Stealth products with associated three-pack IDs are grouped; only full three-packs of three products are retained. | `MagellanProductIteratorFilter.StealthProduct` |
| BE-SIRNA-019 | Stealth single retention | Stealth singles with associated three-pack ID `-` are retained as single products. | `MagellanProductIteratorFilter` |
| BE-SIRNA-020 | UK inventory enrichment | Non-plate product results can be enriched with inventory locations from cached `inventoryDataObject-{productType}`. | `MagellanProductIteratorFilter.setUpUKInventoryFilter` |
| BE-SIRNA-021 | Obsolete issue flag | If a product is an assay and obsolete value equals `0`, search issue `obsolete` is set. | `MagellanProductIteratorFilter` |
| BE-SIRNA-022 | Product-service type | Product-service treats siRNA site search product type as `SIRNA`. | `SirnaSiteSearchService` |
| BE-SIRNA-023 | Product-service collection | `CollectionTypeEnum.SIRNA` maps to label `SIRNA`, collection `Sirna`, and request handler `/siRNA-SiteSrch`. | `CollectionTypeEnum` |
| BE-SIRNA-024 | Product-service count | Product-service returns only count rows by setting `MagellanPageParameter.noOfRows(0)`. | `SirnaSiteSearchService.getProductResultsFromSolr` |
| BE-SIRNA-025 | Product-service phrase search | Multi-word keywords are quoted and encoded unless already quoted. | `SirnaSiteSearchService.getSiteSearchResults` |
| BE-SIRNA-026 | Product-service special characters | Non-assay searches replace special characters outside `[a-zA-Z0-9-*]` with spaces and collapse whitespace. | `SirnaSiteSearchService` |
| BE-SIRNA-027 | Product-service AND behavior | siRNA site search sets AND operator true and the query decorator uses logical AND keyword query logic. | `SirnaSiteSearchService`, `SirnaSiteSearchQueryDecorator` |
| BE-SIRNA-028 | Product-service assay ID detection | A keyword is treated as assay/product ID search if it has no comma/space and is either 13 characters with underscore or passes `Product.isProductID(keyword, "SIRNA")`. | `SirnaSiteSearchService.isAssayIDSearch` |
| BE-SIRNA-029 | eTools application option | eTools search can distinguish cells (`invivo=no`) and animals (`invivo=yes`) when the diehard feature is visible. | `search/search.php` |
| BE-SIRNA-030 | eTools species options | eTools search supports All Species, Homo sapiens, Mus musculus, and Rattus norvegicus. | `search/search.php` |
| BE-SIRNA-031 | eTools criteria | eTools search criteria support contains, matches, starts with, and ends with. | `search/search.php`, `Sirna.applyCriteria` |
| BE-SIRNA-032 | eTools recent search | eTools stores unique recent search metadata in session history with a maximum of five entries. | `search/search.php` |
| BE-SIRNA-033 | eTools all-field merge | All-field search merges gene-based and RNAdb results, sorts with `ranksearch`, and deduplicates by gene ID / RNAdb ID. | `search/search.php`, `Sirna.search_result_unique` |
| BE-SIRNA-034 | eTools noncoding feature gate | RNAdb searches and noncoding siRNA behavior depend on the BabelFish feature visibility. | `search/search.php` |
| BE-SIRNA-035 | Cart transcript grouping | siRNA cart data is organized by transcript ID with transcript name, species, gene, and siRNA entries. | `class.Cart_SiRna.php` |
| BE-SIRNA-036 | Cart species validation | Cart species accepts human, mouse, and rat; other values return species undefined error. | `Cart_SiRna.setSpecies` |
| BE-SIRNA-037 | Cart duplicate prevention | `addSirna` does not add a siRNA ID if `sirna_id_exists` finds the same ID anywhere in cart storage. | `Cart_SiRna.addSirna`, `sirna_id_exists` |
| BE-SIRNA-038 | Cart order counts | Cart distinguishes pre-designed and validated orders by the `validated` flag. | `Cart_SiRna.getNumOrders`, `getNumOrderBlocks` |
| BE-SIRNA-039 | Data rank load | siRNA rank load expects `assayInfo.txt` columns including assay product ID, select flag, target gene ID, validated, inventoried, RefSeq/GenBank values, and design rank. | `ld_sirna_rank.ctl` |
| BE-SIRNA-040 | Design configuration | Data scripts configure GC limits, toxicity/potency cutoffs, off-target limits, species/tax ID, BLAST/CDNAS/RNAfold tooling, and desired siRNAs per gene. | `siRNA_setup.prop` |

## 13. FAST / Solr Field Mapping

| Backend Field | FAST / Source Field | Populated By | Notes |
|---|---|---|---|
| `siRNAStatus` | `productsearchstatus` | `SIRNASTATUS` | Search status / lifecycle-like field. |
| `rank` | `genericsort1` | `RANK` | Used for ranked siRNA display/ordering. |
| `sirnaPathways` | `genericsep7` | `SIRNAPATHWAYS` | Pathway associations. |
| `librarySets` | `genericsep4` | `LIBRARYSETS` | Library set associations. |
| `associatedSirnaAssay` | `genericsep9` | `ASSOCIATEDSIRNAASSAY` | Used for non-Stealth product associations. |
| `associatedSirnaAssayPkgId` | `generic5` | `ASSOCIATEDSIRNAASSAYPKGID` | Package ID for associated siRNA assay. |
| `associatedThreePackId` | `genericsep9` | `ASSOCIATEDTHREEPACKID` | Used for Stealth three-pack grouping. |
| `associatedThreePackPkgId` | `generic5` | `ASSOCIATEDTHREEPACKPKGID` | Package ID for Stealth three-pack. |
| `associatedGEAssay` | `generic1` | `ASSOCIATEDGEASSAY` | Associated gene-expression assay. |
| `associatedGEAssayPkgID` | `oh-snap-there-is-no-field-for-this` | `ASSOCIATEDGEASSAYPKGID` | Field constant indicates a questionable placeholder; validate source mapping. |

## 14. eTools Model Method Map

| Method | Search / Functionality | Key Inputs | Output |
|---|---|---|---|
| `sirnaSearchAll` | All-field gene search | Search type, keyword, criteria, species | Gene rows with siRNA/GEX counts. |
| `sirnaSearchGeneName` | Gene name search | Gene name, criteria, species | Gene rows. |
| `sirnaSearchGeneSymbol` | Gene symbol / alias search | Gene symbol, criteria, species | Gene rows. |
| `sirnaSearchGeneId` | Gene ID search | Gene ID, criteria, species, optional match | Gene rows. |
| `sirnaGeneInfo` | Gene details | Gene ID, criteria, species | Transcript/gene/detail rows. |
| `sirnaSearchAssayId` | Assay/product ID search | Assay ID, criteria, hide noncoding flag | Product/gene rows. |
| `sirnaSearchTranscriptAccession` | NCBI transcript accession search | Transcript accession, criteria, species | Gene/transcript rows. |
| `sirnaSearchOmimId` | OMIM search | OMIM ID, criteria, species | Gene rows. |
| `sirnaSearchRNAdbByGeneId` | RNAdb lookup by gene ID | Gene ID | Noncoding RNA rows. |
| `sirnaSearchRNAdbId` | RNAdb ID search | Search type, criteria, RNAdb ID, species | RNAdb gene rows. |
| `sirnaSearchSirnaId` | siRNA ID search | siRNA ID, criteria, species, select flag | siRNA product rows. |
| `sirnaRankedSilencerSelect` | Ranked Silencer Select products | Gene ID or RNAdb ID | Ranked siRNA rows. |
| `sirnaRankedCodingSilencerSelect` | Coding Silencer Select products | Gene ID or RNAdb ID | Ranked coding rows. |
| `sirnaRankedNoncodingSilencerSelect` | Noncoding Silencer Select products | Gene ID or RNAdb ID | Ranked noncoding rows. |
| `sirnaRankedSilencer` | Ranked Silencer products | Gene ID | Ranked siRNA rows. |
| `sirnaTaqmanGEInfo` | Coding TaqMan GE related info | Gene ID | Related GE rows. |
| `sirnaNoncodingTaqmanGEInfo` | Noncoding TaqMan GE related info | Gene ID or RNAdb ID | Related GE rows. |
| `sirnaCodingAndNoncodingTaqmanGEInfo` | Combined TaqMan GE info | Gene ID or RNAdb ID | Related GE rows. |
| `sirnaGetPartPuritySizeLabel` | Product part / purity / size options | Product subtype ID, validation, select, inventory, IVGN, in vivo flags | Part option rows. |
| `sirnaGetValidationProcedure` | Validation procedure | siRNA product ID | Validation rows. |
| `sirnaGetMultiGene` | Multi-gene target info | siRNA product ID | Multi-gene rows. |
| `applyCriteria` | SQL condition builder | Search type, criteria, value | SQL comparison fragment. |
| `search_result_unique` | De-duplication | Search result array | Deduplicated results by gene/RNAdb pairing. |

## 15. API / Endpoint / Data Contract Summary

| Flow | Endpoint / Method | Request Inputs | Response / Output | Owning Repo |
|---|---|---|---|---|
| siRNA result page | `/order/rnai/siRNA/result?keyword=*` | Keyword query string | Search result page for siRNA | magellan-search |
| Redirect from genome database | `RedirectInterceptor.intercept` | `productTypeSelect`, `targetTypeSelect`, `assayType`, `assayId`, `keyword`, `species` | Permanent redirect to siRNA RNai route | magellan-search |
| Product-service count | `SirnaSiteSearchService.getSiteSearchResults` | Keyword, species, search mode, country, broad/FSCI flags | Map containing `SIRNA` count | tfcom-magellan-product-service |
| Solr searcher | `SIRNASiteSearchSearcherFactory.createSearcher` | `SiteSearchParameters` | `Searcher<DocumentDAO>` | tfcom-magellan-product-service |
| eTools search POST | `search/search.php` | `search_type`, `search_species`, `search_criteria`, `search_term`, `invivo` | HTML/search result arrays and workflow navigation | tfcom-magellan-etools |
| GeneAssist SQL | `Sirna.class.php` methods | Search-specific arguments | Rows from `geneassist` tables | tfcom-magellan-etools |
| Citations | `SQL_SIRNA_CITATIONS_BY_PRODUCT_ID` | Product/assay ID criterion | Literature/citation rows ordered by ranking | tfcom-magellan-etools |
| Cart storage | `Cart_SiRna.addSirna` | siRNA ID, design code, transcript, validation, catalog number | Transcript-grouped cart array | tfcom-magellan-etools |
| Rank load | `ld_sirna_rank.ctl` | `assayInfo.txt` | `sirna_target_rank` table load | magellan-data-scripts |

## 16. Acceptance Criteria

| ID | Requirement | Acceptance Criteria |
|---|---|---|
| AC-BE-SIRNA-001 | Route normalization | Genome-database siRNA requests redirect to `/order/rnai/siRNA/result` with keyword, subtype, and species preserved according to redirect rules. |
| AC-BE-SIRNA-002 | Subtype mapping | `sirna_stealth`, `sirna_silencer`, `sirna_silencer_select`, and `sirna_in_vivo` normalize to expected route keyword subtype tokens. |
| AC-BE-SIRNA-003 | Result creation | `PRODUCT_SIRNA` searches produce `SiRNAProduct` instances with shared product, genomic, non-miRNA, gene-based, and siRNA-specific fields populated. |
| AC-BE-SIRNA-004 | Stealth rules | Stealth products are sorted by product ID, grouped by associated three-pack ID, and incomplete three-packs are excluded while standalone Stealth singles remain. |
| AC-BE-SIRNA-005 | Package prefixes | In vivo and in vitro package prefixes are applied according to subtype rules. |
| AC-BE-SIRNA-006 | Product-service count | Site-search count requests for siRNA use product type `SIRNA`, collection `Sirna`, request handler `/siRNA-SiteSrch`, and return count under key `SIRNA`. |
| AC-BE-SIRNA-007 | Keyword handling | Multi-word product-service keywords are quoted/encoded, non-assay special-character searches are sanitized, and AND query behavior is applied. |
| AC-BE-SIRNA-008 | eTools search types | eTools search supports all documented search types and calls corresponding `Sirna` model methods. |
| AC-BE-SIRNA-009 | Feature gates | BabelFish and diehard feature gates control noncoding RNAdb and in vivo option behavior. |
| AC-BE-SIRNA-010 | Cart rules | Cart storage prevents duplicate siRNA IDs and distinguishes pre-designed vs validated orders by validation flag. |
| AC-BE-SIRNA-011 | Data dependencies | Rank/design data files populate fields expected by backend result mapping and ranking behavior. |

## 17. QA Test Matrix

| Test Area | Scenario | Expected Result |
|---|---|---|
| Redirect | `productTypeSelect=sirna_stealth`, keyword and species present | Redirect keyword includes `stealth` and species. |
| Redirect | `assayType=sirna` and `assayId` present | Redirect keyword includes assay ID and `sirna`. |
| Result mapping | FAST document has Stealth subtype | Associated three-pack fields populated; associated siRNA assay fields set to `-`. |
| Result mapping | FAST document has non-Stealth subtype | Associated siRNA assay fields populated; associated three-pack fields set to `-`. |
| Post-processing | `PRODUCT_SIRNA` with `SIRNA_IV` | Package ID is prefixed with `invivo`. |
| Post-processing | `PRODUCT_SIRNA` with `SIRNA_SS` | Package ID is prefixed with `invitro`. |
| Post-processing | Stealth three-pack with only two products | Incomplete three-pack products are excluded from final list. |
| Product-service | Keyword contains spaces and is unquoted | Keyword is quoted/encoded before search. |
| Product-service | Keyword is a 13-character ID with underscore | Treated as assay ID search and not special-character sanitized. |
| eTools | Blank search term submitted | Error message says no search term was specified. |
| eTools | Search type all with gene/RNAdb matches | Results are merged, sorted, and deduplicated. |
| eTools | RNAdb search while BabelFish hidden | RNAdb/noncoding search is suppressed. |
| Cart | Add same siRNA ID twice | Duplicate is not added. |
| Cart | Set unsupported species | Species undefined error returned. |

## 18. Validation Observations and Suggested Improvements

| ID | Observation | Risk | Suggested Improvement |
|---|---|---|---|
| VAL-BE-SIRNA-001 | `ASSOCIATEDGEASSAYPKGID` maps to field string `oh-snap-there-is-no-field-for-this`. | Associated GE assay package ID may never be populated correctly or may depend on a placeholder. | Confirm actual FAST/Solr source field and replace placeholder constant. |
| VAL-BE-SIRNA-002 | `SirnaSiteSearchService` logs `Error while getting the results from CRISPR solr` in the siRNA service catch block. | Misleading logs can slow production troubleshooting. | Update log message to say siRNA Solr. |
| VAL-BE-SIRNA-003 | eTools `applyCriteria` builds SQL fragments by string concatenation. | SQL injection and escaping risk if upstream input is not strictly controlled. | Move to parameterized SQL or central escaping/validation before query construction. |
| VAL-BE-SIRNA-004 | eTools `sirnaTargetCount` returns `$rs['TARGET_COUNT']`, while other methods treat SQL rows as arrays indexed by row. | Possible incorrect count retrieval depending on `getSqlRows` return shape. | Verify return structure and add regression test. |
| VAL-BE-SIRNA-005 | Product-service `isAssayIDSearch` assumes 13-character underscore IDs for one assay pattern. | Valid siRNA IDs outside that shape may be sanitized as keyword searches. | Add test cases for known siRNA, assay, and catalog ID patterns. |
| VAL-BE-SIRNA-006 | Stealth three-pack logic removes incomplete groups. | Product disappearance may surprise users if data feed has missing group members. | Add monitoring/report for incomplete three-pack groups in data pipeline. |
| VAL-BE-SIRNA-007 | Data-script config references absolute environment paths and older tool versions. | Portability and environment drift risk. | Document runtime environment and migrate to managed config/secrets where feasible. |
| VAL-BE-SIRNA-008 | `magellan-search` and eTools both contain siRNA search logic. | Duplicate rules can diverge between modern result pages and legacy workflow pages. | Create an ownership matrix and automated parity tests for overlapping search types. |

## 19. Developer Implementation Checklist

| Area | Checklist Item |
|---|---|
| Routing | Verify `RedirectInterceptor` handles all legacy siRNA entry points and preserves keyword/species/subtype. |
| Product-service | Verify `SirnaSiteSearchService` count behavior for plain keywords, phrases, special characters, assay IDs, and product IDs. |
| Result mapping | Add unit coverage around `populateSiRNAProductAttributes`, especially Stealth vs non-Stealth associated fields. |
| Post-processing | Add regression tests for in vivo/in vitro package prefixes and Stealth three-pack grouping. |
| eTools search | Test all search types and feature gates in `search/search.php`. |
| SQL/model | Review `applyCriteria` and query construction for escaping and parameterization risk. |
| Cart | Test duplicate prevention, species handling, validated vs pre-designed counts, and order form query-string output. |
| Data pipeline | Validate rank load fields and design configuration align with search result rank expectations. |
| Monitoring | Add targeted logs/metrics for redirect counts, Solr count failures, incomplete Stealth groups, and eTools search errors. |

## 20. Open Questions

| ID | Question | Suggested Owner |
|---|---|---|
| OQ-BE-SIRNA-001 | Is `/order/rnai/siRNA/result` backed fully by Magellan Search, or does it bridge into eTools for some workflows? | Magellan Search / eTools owners |
| OQ-BE-SIRNA-002 | What is the authoritative source field for associated GE assay package ID? | Search data / FAST-Solr owner |
| OQ-BE-SIRNA-003 | Are Stealth incomplete three-packs intentionally hidden from users, or should they be visible as singles with a warning? | Product owner |
| OQ-BE-SIRNA-004 | Which path is considered strategic: Magellan Java search result route, eTools PHP workflow, or both? | Architecture owner |
| OQ-BE-SIRNA-005 | Are diehard and BabelFish feature names still active business toggles, or legacy flags? | eTools owner |

