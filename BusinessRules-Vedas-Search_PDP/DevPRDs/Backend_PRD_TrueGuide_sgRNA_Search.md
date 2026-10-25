# Backend Developer PRD - TrueGuide sgRNA Search

| Field | Details |
|---|---|
| Product / Tool | TrueGuide sgRNA Search |
| Tool URL | https://www.thermofisher.com/crispr/invitrogen/query/* |
| Audience | Backend developers, API developers, data engineers, QA engineers, product owners |
| Document Type | Backend rules document / developer PRD |
| Source Date | 2026-07-31 |
| Primary Verified Repos | thermofisher/magellan-search, thermofisher/tfcom-magellan-search-engine |
| Supporting Repos Reviewed | thermofisher/magellan-core, thermofisher/magellan-data-scripts |
| Style Reference | BE_Developer_PRD table-heavy format used for earlier developer PRDs |

## 1. Document Purpose

| Item | Description |
|---|---|
| Purpose | Capture backend rules, repository ownership, modules, functions, APIs, Solr fields, data-load contracts, and validation observations for the TrueGuide sgRNA Search tool. |
| Developer Focus | Identify Java services, search parameter builders, Solr searchers, query decorators, result models, product subtype mappings, related control logic, Solr request handlers, schema fields, and CRISPR data scripts. |
| Business Focus | Explain how the backend supports discovery of Invitrogen TrueGuide CRISPR guide products by keyword, gene, species, application, product subtype, SKU, and batch search. |
| Scope | CRISPR search route, TrueGuide subtype grouping, Solr search execution, facets, re-query behavior, result mapping, packaging data, related controls/reagents, data load, and product-count behavior. |
| Out of Scope | UI rendering details except where backend data directly drives UI behavior; live production data values not visible in source. |

## 2. Source Evidence and Review Boundary

| Evidence Type | Repo | File / Module | What Was Verified |
|---|---|---|---|
| Product type and route config | thermofisher/magellan-search | `src/main/resources/config.yaml` | `crsprEnabled`, `crsprTrueguideEnabled`, `crisprV2Enabled`, `SolrEnabledProducts`, `crisprSERPURL`, and route `/crispr/invitrogen/query/`. |
| Product type enum | thermofisher/magellan-search | `ProductType.java` | `CRISPR_TF` maps product type `crispr` to Thermo Fisher site region and enables recent searches. |
| Product subtype enum | thermofisher/magellan-search | `ProductSubType.java` | CRISPR subtypes include `crispr_all`, `crispr_trueguide`, and `crispr_lentiarray`; TrueGuide search URL is `/crispr/invitrogen/trueguide`. |
| CRISPR constants | thermofisher/magellan-search | `CrsprConstants.java` | TrueGuide product strings, batch search type, CRISPR FAST/Solr field mapping, product type labels, navigator sort fields, size constants. |
| Search service | thermofisher/magellan-search | `CrisprSolrSearchResultsService.java` | Builds search parameters, executes Solr search, re-queries spaced keyword searches, maps Solr documents, creates navigators, and attaches packaging data. |
| Search parameters | thermofisher/magellan-search | `CrisprSearchParameters.java` | Keyword, product subtype, search type, site region, first-search flag, facets, preselected facets, page offset, and ISO country. |
| Searcher factory | thermofisher/magellan-search | `CrisprSolrSearcherFactory.java` | Initializes CRISPR Solr context and creates `CrisprSearcher` with decorated query. |
| Solr query builder | thermofisher/magellan-search | `CrisprQuery.java`, `CrisprQueryBuilder.java`, `CrisprQueryDecorator.java`, `CrisprFacetOptionsQueryDecorator.java` | Request-handler selection, keyword versus logical AND query decoration, entitlement, facet options, selected facet filters. |
| Solr result model | thermofisher/magellan-search | `SolrCrisprProduct.java`, `SolrCrisprProductResult.java`, `CrisprFields.java` | CRISPR collection name, field bindings, product result adapter behavior, product name cleanup, species processing, related antibody link. |
| Search JSON bridge | thermofisher/magellan-search | `SearchJsonAction.java` | Search execution bridge and SKU search redirect to `/crispr/invitrogen/query/{sku}` for CRISPR SKUs. |
| Package data and pricing | thermofisher/magellan-search | `PackageDataAction.java`, `CRSPRControls.java` | CRISPR subtype normalization for package data, cross-sell package retrieval, related control list, Magellan pricing or Comergent pricing branch. |
| Product detail constants | thermofisher/magellan-search | `CrisprProductDetailConstants.java` | CRISPR design detail labels, related reagents, related controls, package sizes, and related product table headers. |
| Genomic product count | thermofisher/magellan-search | `GenomicProductTypeQueryAction.java` | Product type count grouping for TrueGuide and LentiArray CRISPR subtypes. |
| Solr collection config | thermofisher/tfcom-magellan-search-engine | `magellan-search/solr/Collections/CRISPR/conf/solrconfig.xml` | CRISPR request handlers, boosted search fields, sort rules, status filters, import handlers, update processor chain. |
| Solr schema | thermofisher/tfcom-magellan-search-engine | `magellan-search/solr/Collections/CRISPR/conf/managed-schema` | CRISPR fields, copy fields, field types, unique key, facets, and stored/indexed attributes. |
| Solr update script | thermofisher/tfcom-magellan-search-engine | `update-script.js` | Species keyword mapping enrichment during Solr add processing. |
| Shared product definitions | thermofisher/magellan-core | `ProductDefinitions.java`, `CurrentSearch.java` | Numeric product type and subtype IDs for CRSPR and TrueGuide subtypes; current search maps product type string `CRSPR` to product type. |
| Data ingestion scripts | thermofisher/magellan-data-scripts | `setup_CRSPR.pl`, `LoadCRSPRStarterLoad.pl` | Starter-file columns, SKU-to-subtype mapping, suffix generation, validation statuses, staging files, SQL Loader staging table load. |

## 3. Product Overview

| Area | Details |
|---|---|
| Product Name | TrueGuide sgRNA Search |
| Main Route | `/crispr/invitrogen/query/*` |
| CRISPR Product Type | `crispr` in Magellan V2 and `CRSPR` in older genomic product constants. |
| Main TrueGuide Subtype | `crispr_trueguide` in `ProductSubType`. |
| Backend Product Families Seen in Source | Invitrogen TrueGuide sgRNA, Invitrogen TrueGuide sgRNA Modified, Invitrogen TrueGuide crRNA, LentiArray Lentiviral sgRNA. |
| Business Goal | Help users discover CRISPR guide products by gene, species, application, product subtype, score, and catalog/SKU terms. |
| Backend Goal | Normalize route and subtype state, execute CRISPR Solr search, apply entitlement and facets, map Solr documents to search-result objects, attach packaging data, and support related controls/reagents. |

## 4. Users and Stakeholders

| Persona / Stakeholder | Need | Backend Implication |
|---|---|---|
| Research scientist | Search for TrueGuide guides by gene symbol, gene ID, species, application, product ID, or SKU. | Solr query fields must include gene names, gene IDs, primary gene symbols, species, applications, product subtype, part number, ProductID, and CRISPR constants. |
| Buyer / procurement user | See package, availability, pricing, and related controls/reagents. | Backend must attach package data and support related control/reagent pricing flows. |
| Product owner | Treat TrueGuide as an umbrella while retaining specific product families. | Product-count logic groups crRNA, sgRNA Modified, and sgRNA into `CRISPR_TRUEGUIDE`, while result data keeps individual subtype names. |
| Backend developer | Understand service and Solr flow. | PRD maps services, factories, query builders, decorators, models, constants, and Solr config. |
| Data engineer | Maintain CRISPR starter/load scripts. | Data contract lists starter-file columns, SKU subtype maps, suffix rules, validation statuses, and staging outputs. |
| QA engineer | Build regression tests for keyword, batch, SKU, filters, counts, packaging, controls, and Solr data. | Acceptance criteria and QA matrix provide testable backend scenarios. |

## 5. Repository and Module Map

| Repo | Primary Role | Key Files | Confirmed Responsibility |
|---|---|---|---|
| thermofisher/magellan-search | Search application backend and route integration | `CrisprSolrSearchResultsService`, `CrisprSearchParameters`, `CrisprSolrSearcherFactory`, `CrisprQueryDecorator`, `SolrCrisprProduct`, `CrsprConstants`, `PackageDataAction`, `CRSPRControls` | Build CRISPR search parameters, execute Solr search, map products, build facets, retrieve package/pricing data, and expose related controls. |
| thermofisher/tfcom-magellan-search-engine | Solr collection configuration | `Collections/CRISPR/conf/solrconfig.xml`, `managed-schema`, `update-script.js` | Define CRISPR request handlers, searchable fields, sort rules, schema fields, copy fields, import/update processors, and species keyword enrichment. |
| thermofisher/magellan-core | Shared product constants and translations | `ProductDefinitions.java`, `CurrentSearch.java`, `MagellanTranslations.properties` | Define CRSPR numeric product and subtype IDs, current-search mapping, and shared search labels/messages. |
| thermofisher/magellan-data-scripts | CRISPR data ingestion | `setup_CRSPR.pl`, `LoadCRSPRStarterLoad.pl` | Parse CRISPR starter files, generate assay/staging files, map SKU to subtype and suffix, load staging tables. |

## 6. High-Level Backend Architecture

| Level | Layer | Components | Responsibility |
|---|---|---|---|
| 1 | External route | `/crispr/invitrogen/query/*` | User-facing TrueGuide CRISPR search route. |
| 1 | Search application config | `config.yaml`, `ProductType`, `ProductSubType` | Enable CRISPR, map route and product/subtype identifiers, configure Solr-enabled products. |
| 2 | Search result service | `CrisprSolrSearchResultsService` | Build `CrisprSearchParameters`, query Solr, optionally re-query, map results, create navigators, attach packaging data. |
| 2 | Searcher and query stack | `CrisprSolrSearcherFactory`, `CrisprSearcher`, `CrisprQueryDecorator`, `CrisprQueryBuilder` | Create Solr searcher and decorate query with keyword, logical AND retry, entitlement, facet options, and selected facets. |
| 2 | Solr collection | CRISPR collection in `tfcom-magellan-search-engine` | Execute `/Search`, `/KeywordSearch`, `/CRSPR-SiteSrch`, and related handlers over CRISPR fields. |
| 3 | Result mapping | `SolrCrisprProduct`, `SolrCrisprProductResult`, `CrisprFields` | Map Solr fields into backend product objects and UI-facing product result adapter fields. |
| 3 | Commerce support | `PackageDataAction`, `CRSPRControls`, `CrisprProductDetailConstants` | Provide package SKU lists, related controls, related reagents, package sizes, and pricing data. |
| 3 | Data pipeline | `setup_CRSPR.pl`, `LoadCRSPRStarterLoad.pl`, Solr DIH handlers | Produce staging data and indexable fields for CRISPR search. |

## 7. Workflow Diagram - Search Request to Solr

| Step | Layer | Module / Method | Action | Output |
|---|---|---|---|---|
| 1 | Level 1 route | Browser / route layer | User opens `/crispr/invitrogen/query/*`. | CRISPR search request enters Magellan. |
| 2 | Level 1 config | `config.yaml` | CRISPR features are enabled through `crsprEnabled`, `crsprTrueguideEnabled`, `crisprV2Enabled`, and `SolrEnabledProducts`. | CRISPR V2 Solr path is available. |
| 3 | Level 2 model | `CrisprSolrSearchResultsService.buildSearchParameters` | Resolves `ProductSubType` from product type `crispr` and requested subtype. | `ProductSubType` object. |
| 4 | Level 2 search type | `buildSearchParameters` | Uses `SearchType.BATCH` when `searchType` equals `batchSearch`; otherwise uses `SearchType.KEYWORD`. | Search type selected. |
| 5 | Level 2 parameters | `CrisprSearchParametersBuilder` | Adds keyword or batch keywords, page offset, facets, preselected facets, ISO country, site region, and first-search flag. | `CrisprSearchParameters`. |
| 6 | Level 2 searcher | `CrisprSolrSearcherFactory.createSearcher` | Creates `CrisprSearcher` and sets decorated query. | Solr searcher ready. |
| 7 | Level 3 query | `CrisprQuery` | Selects Solr request handler from search type and `ProductType.getProductType("crispr", siteRegion)`. | Solr request handler. |
| 8 | Level 3 Solr | `SimpleSearcher.search` | Executes decorated query against CRISPR collection. | `QueryResult<SolrCrisprProduct>`. |

```text
Route /crispr/invitrogen/query/*
  -> CrisprSolrSearchResultsService
    -> CrisprSearchParameters
      -> CrisprSolrSearcherFactory
        -> CrisprQueryDecorator
          -> CRISPR Solr collection
```

## 8. Workflow Diagram - Query Decoration and Re-query

| Step | Layer | Module / Method | Rule | Result |
|---|---|---|---|---|
| 1 | Level 2 query decoration | `CrisprQueryDecorator.byKeyword` | If `firstSearch` is true, add normal keyword query. | `KeywordQueryDecorator` wraps query. |
| 2 | Level 2 query decoration | `CrisprQueryDecorator.byKeyword` | If not first search and search type is not batch, add logical AND keyword query. | `LogicalAndQueryDecorator` wraps query. |
| 3 | Level 2 entitlement | `CrisprQueryBuilder.addEntitlementToQuery` | Always add entitlement filter. | Entitled results only unless configuration allows otherwise. |
| 4 | Level 2 facets | `CrisprFacetOptionsQueryDecorator` | Add facet options for all CRISPR filters and limit facet values to default max. | Facet fields included in Solr query. |
| 5 | Level 2 selected facets | `FilterQueryDecorator` | Apply user-selected facets from request/model. | Filtered query. |
| 6 | Level 2 first result | `CrisprSolrSearchResultsService.getResults` | Execute first search. | Query result. |
| 7 | Level 2 re-query decision | `shouldReQuery` | Re-query only when not batch, first search, no documents, and keyword contains a space. | Search retries with logical AND keyword behavior. |
| 8 | Level 2 re-query state | `model.setFirstSearch(false)` | Marks second pass as non-first search. | Logical AND decorator is used on retry. |

```text
First search
  -> keyword query + entitlement + facets
    -> no documents and spaced keyword
      -> second search
        -> logical AND query + entitlement + facets
```

## 9. Workflow Diagram - Result Mapping and Packaging

| Step | Layer | Module / Method | Action | Output |
|---|---|---|---|---|
| 1 | Level 3 Solr document | `SolrCrisprProduct` | Binds CRISPR Solr fields to Java fields with `@Field`. | Raw CRISPR product model. |
| 2 | Level 2 result mapping | `mapToSearchResults` | Wraps each `SolrCrisprProduct` in `SolrCrisprProductResult`. | Product list for search results. |
| 3 | Level 2 navigator mapping | `MagellanNavigatorCreator.toMagellanGenomicNavigator` | Converts Solr facets into Magellan genomic navigators. | Filter navigator list. |
| 4 | Level 2 total count | `queryResult.getStatistics().getNumberOfDocumentsFound` | Reads Solr document count. | Total hits. |
| 5 | Level 2 packaging | `Pricing.getPackageData` | Retrieves package data for country, company, product type, cookies, and pricing context. | Packaging data attached to results. |
| 6 | Level 1 view model | `CrisprSearchResultsViewModel.getPackageDataJson` | Serializes package objects into JSON when package data exists. | Package object JSON available to result page. |

```text
Solr documents
  -> SolrCrisprProduct
    -> SolrCrisprProductResult
      -> SearchResults builder
        -> navigators + total hits + packaging data
```

## 10. Workflow Diagram - Data Load to Search Index

| Step | Layer | Script / Config | Action | Output |
|---|---|---|---|---|
| 1 | Level 3 source data | CRISPR starter file | Provides gene, assay, target, score, species, application, SKU, transcript, and location columns. | Input records. |
| 2 | Level 3 parsing | `setup_CRSPR.pl` | Parses tab-delimited input, skips header/blank rows, filters species, checks duplicate assays. | Parsed assay records. |
| 3 | Level 3 subtype mapping | `setup_CRSPR.pl` | Maps SKUs to CRISPR subtype IDs and suffixes. | Product subtype and assay product ID suffix. |
| 4 | Level 3 validation | `setup_CRSPR.pl` | Marks missing transcript, multiple genes, transcript not found, missing gene, and gene-transcript mismatch statuses. | Status text in assay output. |
| 5 | Level 3 staging output | `setup_CRSPR.pl` | Emits assay, identifier, long identifier, map location, product location, subtype mapping, gene, transcript, primary object, identifier relationship, and product application mapping files. | BCP staging files. |
| 6 | Level 3 staging load | `LoadCRSPRStarterLoad.pl` | Builds control files from templates and loads staging tables with SQL Loader. | Staging tables populated. |
| 7 | Level 2 Solr import | `solrconfig.xml` | Data import handlers use `CRISPR-dih.xml` and update processor chain. | CRISPR collection receives indexed data. |
| 8 | Level 2 update script | `update-script.js` | Enriches species keyword mapping during Solr add processing. | Searchable species aliases are updated. |

```text
Starter file
  -> setup_CRSPR.pl
    -> BCP staging files
      -> LoadCRSPRStarterLoad.pl
        -> staging tables
          -> Solr data import
            -> CRISPR collection
```

## 11. Backend Business Rules

| Rule ID | Area | Rule | Source |
|---|---|---|---|
| BE-TG-001 | Product enablement | CRISPR search is enabled by `crsprEnabled`, `crsprTrueguideEnabled`, and `crisprV2Enabled` in configuration. | `config.yaml` |
| BE-TG-002 | Solr enablement | CRISPR uses the Solr path when `CRISPR_TF` is listed in `SolrEnabledProducts`. | `config.yaml`, `ProductType` |
| BE-TG-003 | Route | The configured CRISPR SERP URL is `/crispr/invitrogen/query/`. | `config.yaml` |
| BE-TG-004 | Product type | CRISPR product type is `crispr` for Magellan V2 and maps to product type abbreviation `crispr`. | `ProductType.CRISPR_TF` |
| BE-TG-005 | Legacy type | Older genomic product constants use product type `CRSPR`. | `ProductDefinitions`, `CurrentSearch` |
| BE-TG-006 | TrueGuide subtype | TrueGuide search uses product subtype `crispr_trueguide`. | `ProductSubType` |
| BE-TG-007 | TrueGuide grouping | Genomic product counts group Invitrogen TrueGuide crRNA, Invitrogen TrueGuide sgRNA Modified, and Invitrogen TrueGuide sgRNA into `CRISPR_TRUEGUIDE`. | `GenomicProductTypeQueryAction` |
| BE-TG-008 | LentiArray grouping | LentiArray Lentiviral sgRNA is grouped separately as `CRISPR_LENTIVIRAL`. | `GenomicProductTypeQueryAction` |
| BE-TG-009 | Batch search | If model search type equals `batchSearch`, backend builds `SearchType.BATCH` parameters with batch keywords. | `CrisprSolrSearchResultsService`, `CrsprConstants` |
| BE-TG-010 | Keyword search | Non-batch searches use stripped keyword and `SearchType.KEYWORD`. | `CrisprSolrSearchResultsService` |
| BE-TG-011 | Pagination | Search parameters include page offset when provided by the model. | `CrisprSearchParametersBuilder.withPageParameter` |
| BE-TG-012 | Facets | Search parameters include explicit navigators converted to `FacetDAO`; otherwise preselected navigators from URL/model can be converted into facets. | `CrisprSearchParametersBuilder` |
| BE-TG-013 | ISO country | Search parameters carry ISO country for entitlement and regional behavior. | `CrisprSearchParametersBuilder.withIsoCountry` |
| BE-TG-014 | First query | First keyword query uses keyword query decoration. | `CrisprQueryDecorator` |
| BE-TG-015 | Retry query | Second non-batch query uses logical AND keyword decoration when the first spaced keyword search has no documents. | `CrisprQueryDecorator`, `shouldReQuery` |
| BE-TG-016 | Batch no retry | Batch search never triggers `shouldReQuery`. | `CrisprSolrSearchResultsService.shouldReQuery` |
| BE-TG-017 | Entitlement | CRISPR search query always adds entitlement decoration. | `CrisprQueryBuilder.addEntitlementToQuery` |
| BE-TG-018 | Facet options | CRISPR query adds facet options for filters by product type `crispr`. | `CrisprFacetOptionsQueryDecorator` |
| BE-TG-019 | Facet limit | CRISPR facet options use default facet max limit `200`. | `FilterConstants.DEFAULT_FACET_MAX_LIMIT` |
| BE-TG-020 | Selected facets | Selected facets are added to the query through filter query decoration. | `CrisprQueryBuilder.addSelectedFacetsToQuery` |
| BE-TG-021 | Collection | CRISPR result model is mapped to Solr collection `CRISPR`. | `CrisprFields`, `CrisprCollectionSettings` |
| BE-TG-022 | Result model | Search documents are mapped into `SolrCrisprProduct` and adapted as `SolrCrisprProductResult`. | `SolrCrisprProduct`, `SolrCrisprProductResult` |
| BE-TG-023 | Product name cleanup | Result adapter removes `Invitrogen`, converts TrueGuide and LentiArray brand text to branded display HTML. | `SolrCrisprProductResult.getProductName` |
| BE-TG-024 | Species processing | Result adapter passes species through `SpeciesProcessor` and returns the first processed value. | `SolrCrisprProductResult.getSpeciesName` |
| BE-TG-025 | Related antibody link | Related antibody link is built as `/antibody/gene/{geneSymbol}/filter/species/{speciesName}`. | `SolrCrisprProductResult.getRelatedAntibodyLink` |
| BE-TG-026 | Packaging | Search result mapping attaches package data from `Pricing.getPackageData`. | `CrisprSolrSearchResultsService.mapToSearchResults` |
| BE-TG-027 | Package JSON | CRISPR search result view model serializes package objects from `additionalProperties.packageData`. | `CrisprSearchResultsViewModel.getPackageDataJson` |
| BE-TG-028 | SKU redirect | SKU search route redirects CRISPR SKUs to `/crispr/invitrogen/query/{sku}`. | `SearchJsonAction.searchBySku` |
| BE-TG-029 | Package subtype normalization | Package data action maps subtype strings containing TrueGuide crRNA, sgRNA Modified, sgRNA, or lentiviral to CRSPR subtype constants. | `PackageDataAction` |
| BE-TG-030 | Related controls | Related controls exclude product subtype `crispr_trueguide_crrna` from `getControlDtls` in the search result view model. | `CrisprSearchResultsViewModel.getControlDtls` |
| BE-TG-031 | Control selection | `CRSPRControls` returns sgRNA controls when SKU is A35510 or A35511 or mode contains TrueGuide sgRNA. | `CRSPRControls.execute` |
| BE-TG-032 | Control species | Human sgRNA controls include AAVS1, CDK4, and HPRT1 positive controls; mouse sgRNA controls include Rosa26 positive control. | `CRSPRControls.execute` |
| BE-TG-033 | Negative control | sgRNA controls include non-targeting negative control A35526. | `CRSPRControls.execute` |
| BE-TG-034 | Control pricing | `CRSPRControls` uses Magellan pricing API when `useMagellanPricingAPI` is true; otherwise uses Comergent package data. | `CRSPRControls.execute` |
| BE-TG-035 | Solr status filter | CRISPR Solr handlers append filter `-SearchStatus:0`, excluding status zero documents. | `solrconfig.xml` |
| BE-TG-036 | Solr sort | CRISPR search sorts by primary gene symbol, CRISPR score, and LentiViral subtype term frequency for `/Search` and `/CRSPR-SiteSrch`. | `solrconfig.xml` |
| BE-TG-037 | Search boost | `/Search` boosts ID, gene names, gene IDs, product subtype, gene symbols, aliases, species, applications, part number, ProductID, CopyID, and CrisprConst. | `solrconfig.xml` |
| BE-TG-038 | Keyword boost | `/KeywordSearch` gives strong boost to primary gene symbol search and sorts by score, CRISPR score, and ID. | `solrconfig.xml` |
| BE-TG-039 | Schema unique key | CRISPR Solr schema uses `id` as unique key. | `managed-schema` |
| BE-TG-040 | Schema copy fields | Schema copies species, gene names, primary gene symbol, product subtype, id, gene IDs, and applications into search helper fields. | `managed-schema` |
| BE-TG-041 | Data subtype map | CRISPR starter load maps A47715 through A47721 to TrueGuide sgRNA subtype IDs, A47728 through A47731 to TrueGuide crRNA subtype ID, and A32042 to lentiviral subtype ID. | `setup_CRSPR.pl` |
| BE-TG-042 | Data suffix map | CRISPR starter load appends `_SG` for TrueGuide sgRNA SKUs, `_CR` for crRNA SKUs, and `_LV` for lentiviral SKU. | `setup_CRSPR.pl` |
| BE-TG-043 | Data validation status | Data load records missing transcript, multiple genes, transcript not found, missing gene, and gene-transcript mismatch statuses. | `setup_CRSPR.pl` |
| BE-TG-044 | Data staging files | Data load emits assay, identifier, long identifier, map location, product location, subtype mapping, gene, transcript, primary object, identifier relationship, and product application mapping files. | `setup_CRSPR.pl` |
| BE-TG-045 | Staging table load | `LoadCRSPRStarterLoad.pl` creates SQL Loader control files and loads corresponding staging tables when BCP files exist. | `LoadCRSPRStarterLoad.pl` |

## 12. Search Field and Result Mapping

| Backend Field | Solr Field | Java Model / Constant | Notes |
|---|---|---|---|
| Collection | `CRISPR` | `CrisprFields.CRISPR_COLLECTION` | Collection used by `CrisprCollectionSettings`. |
| Product ID | `id` | `SolrCrisprProduct.getProductId` | Unique key and result product ID. |
| Product type | `productType`, `ProductType` | inherited genomic product fields | Used for filtering and product family behavior. |
| Product subtype | `ProductSubtype` | `productSubType`, `CRSPR_PRODUCT_FAST_FIELDS.PRODUCTSUBTYPE` | Drives TrueGuide and LentiArray grouping. |
| Package ID | `PackageID` | `packageId`, `CRSPR_PRODUCT_FAST_FIELDS.PACKAGEID` | Used for package lookup. |
| Part number | `partnumber` | `CrisprFields.PART_NUMBER`, `CRSPR_PRODUCT_FAST_FIELDS.PARTNUMBER` | Searchable and displayed as catalog/SKU value. |
| Availability | `Availability` | `CRSPR_PRODUCT_FAST_FIELDS.AVAILABILITY` | Availability field. |
| Species | `Species`, `SpeciesSearch` | `CrisprFields.SPECIES` | Stored as multivalued species and copied to search helper field. |
| Applications | `Applications`, `ApplicationsSearch` | `CrisprFields.APPLICATIONS` | Used as facet and search field. |
| Gene names | `GeneNames`, `GeneNamesSearch` | `CrisprFields.GENE_NAMES` | Searchable gene names. |
| Gene IDs | `GeneIDs`, `GeneIDsSearch` | `CrisprFields.GENE_IDS` | Searchable gene IDs. |
| Gene aliases | `GeneAliases`, `GeneAliasesSearch` | `CrisprFields.GENE_ALIASES` | Searchable aliases. |
| Primary gene symbol | `PrimaryGeneSymbolCaps`, `PrimaryGeneSymbolCapsSearch` | `CrisprFields.GENE_SYMBOLS` | Facet and high-boost query field. |
| CRISPR score | `crisprScore` | `CrisprFields.CRISPR_SCORE`, `CRSPR_PRODUCT_FAST_FIELDS.SCORE` | Used in result object and sort rules. |
| Search status | `SearchStatus`, `productsearchstatus` | `CRSPR_PRODUCT_FAST_FIELDS.PRODUCTSEARCHSTATUS` | Status zero excluded by Solr handlers. |
| Entitlement | `EntitlementGroup` | Entitlement query decorator | Used to filter results by entitlement. |

## 13. Solr Request Handler Rules

| Handler | Purpose | Key Rules |
|---|---|---|
| `/query` | General JSON query handler | Default field `GeneNames`; appends `-SearchStatus:0`. |
| `/KeywordSearch` | Keyword search handler | Rows 500; edismax; minimum match 100 percent; boosts gene names, gene symbols, primary gene symbols, ID, product subtype, species, applications, part number, ProductID, CopyID, and CrisprConst; sorts by score, CRISPR score, and ID. |
| `/Search` | Main CRISPR search handler | Rows 25; edismax; OR query operator; boost function adds weight when ProductSubtypeSearch contains TrueGuide; appends status filter and sort by primary gene symbol, CRISPR score, and LentiViral term frequency. |
| `/CRSPR-SiteSrch` | Site-search style CRISPR handler | Similar to `/Search`; fields include ID, gene names, gene IDs, product subtype, product type, gene symbols, aliases, species, applications, part number, ProductID, CopyID, and CrisprConst. |
| `/browse` | Browse handler | Velocity response, facets on Species, PrimaryGeneSymbolCaps, and ProductSubtype; boosts modified TrueGuide subtype; appends status filter and sort. |
| `/dataimport-*` | Data import handlers | Use `CRISPR-dih.xml` and update chain `script`; handlers 00 through 04 support parallel import, 98 optimize, 99 delete/clean. |

## 14. Data Contract from CRISPR Starter Load

| Data Area | Source Column / Rule | Backend Outcome |
|---|---|---|
| Gene symbol | Column 0 | Used in gene/product staging. |
| Gene description | Column 1 | Used for gene description and staging output. |
| Gene alias | Column 2 | Identifier/search support. |
| Location | Column 3 | Map/location support. |
| Family | Column 4 | Long identifier type 148. |
| UniGene | Column 5 | Identifier type 26. |
| Gene ID | Column 6 | Gene matching and missing-gene validation. |
| Ensembl gene | Column 7 | Optional gene load support. |
| Gene type | Column 8 | Identifier type 149. |
| CRISPR ID | Column 9 | CRISPR assay identifier. |
| Full CRISPR ID | Column 10 | Base assay product ID before suffix. |
| Target sequence | Column 11 | Written into CRSPR assay output. |
| PAM | Column 12 | Identifier type 150. |
| Score | Column 13 | Identifier type 151 and later CRISPR score search field. |
| Percent GC | Column 14 | Identifier type 152. |
| Chromosome | Column 15 | Map location staging. |
| Strand | Column 16 | Converts plus to orientation 1 and minus to orientation -1. |
| Start and end | Columns 17 and 18 | Map location; values are swapped when start is greater than end. |
| Species | Column 19 | Mapped to Homo sapiens 9606 and Mus musculus 10090; records outside requested species map are skipped. |
| Transcript exon | Column 20 | Transcript and exon identifiers; missing/unmapped values create validation status. |
| Application | Column 21 | Mapped to application type and product application mapping. |
| SKU | Column 22 | Maps to subtype ID and product suffix. |
| Ensembl transcript | Column 23 | Optional transcript load support. |

## 15. Related Products, Controls, and Pricing

| Area | Backend Rule | Source |
|---|---|---|
| Related reagents | `getReagentsDtls` builds a map for all `CRISPR_PRODUCT_CONSTANT` entries by product type and subtype. | `CrisprSearchResultsViewModel` |
| Related controls | `getControlDtls` builds control details for CRISPR product constants except `crispr_trueguide_crrna`. | `CrisprSearchResultsViewModel` |
| Reagent product constants | Related reagents include TrueCut Cas9 Protein, Lipofectamine CRISPRMAX Cas9 Transfection reagent, GeneArt Genomic Cleavage Detection Kit, LentiArray Cas9 Lentivirus, and Puromycin Dihydrochloride depending on CRISPR product family. | `CrisprProductDetailConstants` |
| Related control constants | Related controls include TrueGuide sgRNA controls, TrueGuide crRNA controls, and LentiArray controls with product descriptions and species groupings. | `CrisprProductDetailConstants` |
| Related product headers | Related product table headers are Product Name, Size, and Price. | `CrisprProductDetailConstants` |
| sgRNA controls | Human sgRNA controls include A35522, A35523, A35524; mouse sgRNA control includes A35525; negative control includes A35526. | `CRSPRControls` |
| crRNA controls | CRISPR controls action supports crRNA control SKUs for A35509 or TrueGuide crRNA mode. | `CRSPRControls` |
| LentiArray controls | LentiArray controls include scrambled negative controls and HPRT positive controls with and without GFP. | `CRSPRControls` |
| Pricing branch | Uses Magellan pricing API when `useMagellanPricingAPI` is true; otherwise uses Comergent package data and pricing utility. | `CRSPRControls` |
| Package data | CRISPR and antibody package data use cross-sell package data retrieval from Comergent in `PackageDataAction`. | `PackageDataAction` |

## 16. Acceptance Criteria

| ID | Scenario | Acceptance Criteria |
|---|---|---|
| AC-TG-001 | Open TrueGuide search route | `/crispr/invitrogen/query/*` resolves to the CRISPR search experience when CRISPR and V2 flags are enabled. |
| AC-TG-002 | Keyword search | Non-batch keyword search builds `SearchType.KEYWORD`, uses stripped keyword, applies entitlement, facets, selected filters, and queries the CRISPR collection. |
| AC-TG-003 | Batch search | `batchSearch` builds `SearchType.BATCH`, uses batch keywords, and does not trigger re-query behavior. |
| AC-TG-004 | Re-query | A first keyword search with no documents and a spaced keyword triggers exactly one logical AND retry. |
| AC-TG-005 | Product grouping | Genomic product-count API groups crRNA, sgRNA Modified, and sgRNA product-subtype hits into `CRISPR_TRUEGUIDE`. |
| AC-TG-006 | Solr status | Search handlers exclude documents with `SearchStatus` equal to zero. |
| AC-TG-007 | Facets | CRISPR filters are requested with facet limit 200 and selected URL/model facets are applied to Solr query. |
| AC-TG-008 | Result mapping | Solr result documents expose product ID, subtype, package ID, species, gene names, applications, gene IDs, aliases, CRISPR score, part number, and primary gene symbol. |
| AC-TG-009 | Packaging | Search results include packaging data for product type and country/company context. |
| AC-TG-010 | SKU redirect | CRISPR SKU search redirects to `/crispr/invitrogen/query/{sku}`. |
| AC-TG-011 | Related controls | Related sgRNA controls return species-appropriate positive controls and negative control. |
| AC-TG-012 | Data load | Starter load maps supported SKUs to subtype IDs and suffixes and emits staging files for assay, identifiers, locations, subtype, gene/transcript, relationships, and application mapping. |

## 17. QA Matrix

| Test Area | Test Case | Expected Result |
|---|---|---|
| Feature flags | Disable `crisprV2Enabled`. | CRISPR V2 Solr path should not be used. |
| Route | Search wildcard route. | Backend resolves CRISPR search route and returns results or zero-result state. |
| Keyword | Search a known gene symbol. | Solr query returns TrueGuide rows sorted by configured rules. |
| Spaced keyword | Search a spaced gene/name term that returns zero on first pass. | Service performs one logical AND retry. |
| Batch | Submit batch search type. | Batch search executes without re-query. |
| Filters | Apply species filter. | Filter is converted to facet DAO and applied in Solr filter query. |
| Product subtype | Search TrueGuide umbrella. | Results may include sgRNA, sgRNA Modified, and crRNA subtypes while counts group as TrueGuide. |
| SKU | Search CRISPR SKU through SKU redirect. | Redirect URL points to `/crispr/invitrogen/query/{sku}`. |
| Packaging | Search results with package data. | Package object JSON is available from view model. |
| Controls | Request controls for sgRNA human. | AAVS1, CDK4, HPRT1, and non-targeting controls are returned with price data when available. |
| Controls | Request controls for sgRNA mouse. | Rosa26 and non-targeting controls are returned with price data when available. |
| Solr status | Index contains SearchStatus zero record. | Record is excluded from search handlers. |
| Data load | Starter file contains missing transcript. | Status includes missing transcript message. |
| Data load | Starter file contains duplicate assay product. | Duplicate warning is logged and duplicate count increments. |

## 18. Validation Observations

| Severity | Observation | Impact | Recommendation |
|---|---|---|---|
| High | Product type spelling varies between `crispr` and `CRSPR`. | Mapping errors can break route, package, or legacy genomic product-count behavior. | Keep explicit mapping tests for `ProductType`, `ProductSubType`, `CurrentSearch`, package lookup, and Solr field constants. |
| High | TrueGuide grouping combines three product subtypes in product-count logic. | Count and result rows can look inconsistent unless documented. | Document umbrella behavior in product owner and QA test cases. |
| Medium | CRISPR retry logic is disabled for batch search and only applies to spaced keyword searches. | Search recall can vary by input type. | Add tests for first search, logical AND retry, and batch no-retry behavior. |
| Medium | Solr config contains multiple handlers with similar but not identical boost and sort rules. | Result order can differ by endpoint. | Confirm which handler is used for the production route and align tests to that handler. |
| Medium | Data-load scripts include hardcoded SKU-to-subtype and suffix mappings. | New TrueGuide SKUs may not index correctly unless scripts are updated. | Add a SKU mapping checklist to data onboarding. |
| Medium | Species mappings in Solr update script are large and manually maintained. | Species keyword search quality can drift. | Move mappings to versioned structured data or validate periodically against taxonomy source. |
| Low | Related control logic has hardcoded SKU lists and descriptions. | Related control updates require code changes. | Externalize controls to configuration or product data where possible. |
| Low | Data-load status text is string-concatenated and semicolon-delimited. | Downstream consumers may parse inconsistent strings. | Consider structured validation status fields during pipeline modernization. |

## 19. Areas for Improvement

| Area | Current State | Suggested Improvement |
|---|---|---|
| Type naming | Mixed `CRSPR`, `crispr`, `CRISPR_TF`, and product subtype strings. | Define one canonical naming matrix and add unit tests across route, service, package, and data-load boundaries. |
| Search handler clarity | `/Search`, `/KeywordSearch`, `/CRSPR-SiteSrch`, and `/browse` have different boosts and sorts. | Document production handler selection and keep handler-specific regression expectations. |
| Data ingestion | Starter-file parsing and staging generation are Perl scripts with hardcoded columns and SKU maps. | Add schema validation, mapping tests, and onboarding documentation for new SKUs/subtypes. |
| Related controls | Controls and package sizes are hardcoded in Java constants/action logic. | Drive controls from product data or a managed configuration source. |
| Observability | Search service logs limited behavioral context in the inspected files. | Add structured logs for search type, handler, subtype, first search versus retry, total hits, and entitlement filter context. |
| Automated tests | Tests exist for several CRISPR classes, but full route-to-Solr behavior should be validated. | Add integration tests for keyword, batch, SKU redirect, facet, packaging, and TrueGuide grouping scenarios. |

## 20. Developer Traceability Matrix

| Requirement | Primary Module | Key Method / Constant | Notes |
|---|---|---|---|
| Enable CRISPR route | `config.yaml` | `crsprEnabled`, `crsprTrueguideEnabled`, `crisprV2Enabled`, `crisprSERPURL` | Controls availability and route path. |
| Resolve CRISPR product type | `ProductType.java` | `CRISPR_TF` | Product type `crispr`, Thermo Fisher region. |
| Resolve TrueGuide subtype | `ProductSubType.java` | `CRISPR_TRUEGUIDE`, `CRISPR_TRUEGUIDE_INV` | Both use subtype `crispr_trueguide`. |
| Build search parameters | `CrisprSolrSearchResultsService` | `buildSearchParameters` | Chooses keyword or batch search. |
| Apply query rules | `CrisprQueryDecorator` | `byKeyword` | Adds keyword or AND keyword plus entitlement and facets. |
| Build query chain | `CrisprQueryBuilder` | `addKeywordToQuery`, `addAndKeywordToQuery`, `addEntitlementToQuery`, `addFacetOptionsToQuery`, `addSelectedFacetsToQuery` | Decorator chain. |
| Select Solr handler | `CrisprQuery` | constructor | Uses search type and product type to choose handler. |
| Execute search | `CrisprSearcher` | constructor / inherited `search` | SimpleSearcher subclass. |
| Map results | `CrisprSolrSearchResultsService` | `mapToSearchResults` | Product adapter, navigators, total hits, packaging. |
| Bind Solr fields | `SolrCrisprProduct` | `@Field` annotations | Species, gene, application, score, part number. |
| Adapt display fields | `SolrCrisprProductResult` | getters | Product name cleanup, species processing, related antibody link. |
| Package data | `PackageDataAction` | `execute` | Normalizes CRISPR subtype and retrieves package data. |
| Related controls | `CRSPRControls` | `execute` | Builds control SKU list and pricing data. |
| Solr collection fields | `managed-schema` | field and copyField definitions | Defines indexed/stored CRISPR fields. |
| Solr search behavior | `solrconfig.xml` | `/Search`, `/KeywordSearch`, `/CRSPR-SiteSrch` | Boosts, filters, sorts. |
| Starter parse | `setup_CRSPR.pl` | main loop | Parses input and emits staging files. |
| Staging load | `LoadCRSPRStarterLoad.pl` | `loadStagingTable` | Creates SQL Loader control files and loads staging. |

## 21. Open Validation Items

| ID | Item | Owner / Follow-up |
|---|---|---|
| VAL-TG-001 | Confirm the exact controller/action that binds `/crispr/invitrogen/query/*` to `CrisprSolrSearchResultsService` in the deployed route configuration. | Backend owner |
| VAL-TG-002 | Confirm which Solr request handler is used for production TrueGuide SERP search: `/Search`, `/KeywordSearch`, or another mapped handler. | Search platform owner |
| VAL-TG-003 | Confirm whether `CRISPR_TRUEGUIDE_INV` and `CRISPR_TRUEGUIDE` duplicate subtype entries are both still required. | Backend owner / product owner |
| VAL-TG-004 | Confirm current supported TrueGuide SKUs and whether all are present in `setup_CRSPR.pl` subtype and suffix maps. | Data engineering |
| VAL-TG-005 | Confirm related control product SKU availability and pricing behavior for US and non-US countries. | Commerce / QA |
| VAL-TG-006 | Confirm whether CRISPR related reagents and controls should be configurable instead of hardcoded in constants/actions. | Product owner |
| VAL-TG-007 | Confirm Solr `CRISPR-dih.xml` location or replacement import job if the file is generated or managed outside the inspected repo path. | Search platform / data engineering |

