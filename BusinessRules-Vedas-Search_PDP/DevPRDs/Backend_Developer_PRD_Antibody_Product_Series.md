# Backend Developer PRD: Antibody Product Series

Document date: July 23, 2026  
Audience: Backend developers, service owners, QA engineers, UI developers, product owners, and integration teams  
Scope: Primary Antibodies, Secondary Antibodies, Isotype Controls, Proteins and Peptides, and ELISA Kits search and product detail services  
Primary repositories reviewed: `thermofisher/magellan-search`, `thermofisher/tfcom-magellan-product-service`, `thermofisher/tfcom-magellan-related-products-service`, `thermofisher/tfcom-magellan-qanda-service`  
Template reference: `UI_Developer_PRD_Antibody_Product_Series_Tables.docx`

## 1. Document Purpose

This PRD defines the backend behavior needed to support antibody product series search pages and product detail pages. It focuses on backend modules, service boundaries, API contracts, request and response rules, data flow, error handling, caching, feature flags, and validation responsibilities.

The document uses the previously generated UI Developer PRD as the formatting template and uses the business rules package plus available repository evidence. Where a repo or internal controller could not be fully reviewed, this document marks the item as a validation point rather than treating it as confirmed behavior.

## 2. Source Evidence and Review Boundary

| Evidence type | Reviewed evidence | Backend relevance |
| --- | --- | --- |
| Business rules | Business rules documents for Primary Antibody, Secondary Antibody, Isotype Controls, Proteins and Peptides, and ELISA Kits | Source of product, commerce, banner, specification, related product, bioinformatics, reference, and Q and A rules |
| UI PRD | `UI_Developer_PRD_Antibody_Product_Series_Tables.docx` | Formatting and structure reference; UI behavior dependency map |
| Search and PDP orchestration repo | `thermofisher/magellan-search` | Product subtype routing, PDP view model assembly, search behavior, AEO markdown builder, config-driven backend integrations |
| Product service repo | `thermofisher/tfcom-magellan-product-service` | Related product detail aggregation endpoint, catalog and Magellan SKU separation, Spring Boot service stack |
| Related products service repo | `thermofisher/tfcom-magellan-related-products-service` | Dynamic related product lookup, related product cache, SKU/type validation, catalog enrichment |
| Q and A service repo | `thermofisher/tfcom-magellan-qanda-service` | Question retrieval, keyword filtering, answer retrieval, submit question, submit answer, voting, Solr/JPA integration |
| Prompt file | `business-rule-extraction-prompt-v3.1.md` | Multi-repo extraction and evidence-driven rule discipline |

### 2.1 Access limitation

The exact GitHub team repository page for `de-magellan` was not fully available as a structured team repository list in this environment. This PRD uses accessible repository evidence and configuration references. Service ownership and final repository assignment should be validated with the de-magellan GitHub team owners.

## 3. Product Overview

| Area | Backend PRD definition |
| --- | --- |
| Product name | Antibody Product Series Search and PDP backend capabilities |
| Product families | Primary Antibodies, Secondary Antibodies, Isotype Controls, Proteins and Peptides, ELISA Kits |
| Purpose | Provide reliable product search, product detail, pricing, availability, lifecycle banner, specifications, bioinformatics, references, related products, and Q and A data to the frontend |
| Business goal | Help customers find scientifically relevant products and complete purchase decisions with correct product, content, price, availability, support, and related product data |
| Backend goal | Keep business rules centralized, feature-flagged, country-aware, subtype-aware, and resilient to partial service failures |
| In scope | Search data orchestration, PDP model assembly, pricing and availability integration, related products, Q and A, references, bioinformatics, target details, product specifications, banners |
| Out of scope | UI component implementation, visual design, catalog authoring workflows, and non-antibody/TaqMan product pages |

## 4. Product Subtypes and Backend Mapping

| Product family | Example search route | Example PDP route | ProductSubType enum | Product type | Product subtype value | Backend routing notes |
| --- | --- | --- | --- | --- | --- | --- |
| Primary Antibody | `/antibody/primary/query/*` | `/antibody/product/.../MA5-14520` | `ANTIBODY_PRIMARY` | `antibody` | `antibody_primary` | Citation, bioinformatics, image search, antigen search, protocols, related products, Q and A, pricing, availability |
| Secondary Antibody | `/antibody/secondary/query/*` | `/antibody/product/.../A-11008` | `ANTIBODY_SECONDARY` | `antibody` | `antibody_secondary` | Citation, target availability, related products, Q and A, pricing, availability |
| Isotype Control | `/antibody/control/query/*` | `/antibody/product/.../02-6102` | `ANTIBODY_CONTROL` | `antibody` | `antibody_control` | Citation, bioinformatics, related products, Q and A, pricing, availability |
| Proteins and Peptides | `/proteins/query/*` | `/proteins/product/.../100-18B-50UG` | `ANTIBODY_PROTEIN` | `antibody` | `antibody_protein` | New protein routes when enabled, protein-specific specs, bioinformatics, related products, pricing, availability |
| ELISA Kits | `/elisa/query/*` | `/elisa/product/.../A35613` | `ELISA` | `immunoassay` | `ELISA` | Immunoassay details, About This Kit, target info, bioinformatics, ELISA related products, pricing, availability |

## 5. Repository and Backend Module Map

| Repository | Tech stack evidence | Important modules or classes | Backend responsibility |
| --- | --- | --- | --- |
| `thermofisher/magellan-search` | Java/Spring Magellan web application code, config-driven integrations | `ProductSubType`, `AntibodyProductDetailViewModel`, `PdpAeoMarkdownBuilder`, `ProductDetailConstants`, `UnifiedCardProductTypeCountAction`, `AntibodySearchResultsViewModelTest`, `PdpAeoMarkdownBuilderTest` | Search/PDP orchestration, subtype feature rules, AEO content output, endpoint configuration, view model data transformations |
| `thermofisher/tfcom-magellan-product-service` | Spring Boot `2.3.2.RELEASE`, Java `1.8`, Maven artifact `tfcom-magellan-product-service` | `MagellanRelatedProductsSearchController`, `RelatedProductService`, `SiteSearchCatalogService`, `ValidationService`, `MagellanRelatedProductsSearchRequest`, `CatalogRelatedProductsSearchRequest` | Fetch related product detail payloads by combining Magellan SKU details and catalog SKU details |
| `thermofisher/tfcom-magellan-related-products-service` | Spring Boot `3.5.6`, Java `21`, Spring Web/JPA/JDBC, MySQL connector, ShedLock | `DynamicRelatedProductsController`, `RelatedProductsCachingService`, `DynamicRelatedProductsService`, `DataService`, `ValidSku`, `AntibodyType`, `AssayType` | Dynamic related product lookup, SKU/type validation, Redis/cache access, data science result retrieval, catalog enrichment |
| `thermofisher/tfcom-magellan-qanda-service` | Spring Boot `3.5.6`, Java `21`, Spring Web/JPA/JDBC/Security/Actuator/Mail/Thymeleaf, Solr artifact | `MagellanActionController`, `MagellanSubmitQuestionAnswerController`, `MagellanSolrService`, `MagellanQuestionListFromKeywordBuilderService`, `MagellanAnswerBuilderService`, `MagellanSubmitQAndAService` | Q and A retrieval, keyword filtering, highlighting, question/answer submission, answer voting, scheduled indexing controls |

## 6. Backend Functional Architecture

### 6.1 System context

```text
Level 0: Product discovery and PDP backend

Browser / UI
  |
  +-- Magellan Search / PDP Orchestration
        |
        +-- Search index and product search services
        +-- Product detail model builder
        +-- Pricing service
        +-- Availability service
        +-- Promotion service
        +-- Related products service
        +-- Product service detail aggregator
        +-- Q and A service
        +-- CiteAb / references sources
        +-- Documents / certificates sources
        +-- Catalog service
```

### 6.2 Backend workflow - Search, 2 levels deeper

```text
Search request
  |
  +-- L1: Route and subtype resolution
  |     |
  |     +-- L2: Parse route family
  |     |     +-- /antibody/primary/query/*
  |     |     +-- /antibody/secondary/query/*
  |     |     +-- /antibody/control/query/*
  |     |     +-- /proteins/query/*
  |     |     +-- /elisa/query/*
  |     |
  |     +-- L2: Resolve ProductSubType
  |           +-- product type
  |           +-- subtype value
  |           +-- display label
  |           +-- enabled features
  |
  +-- L1: Search model assembly
  |     |
  |     +-- L2: Validate keyword
  |     |     +-- preserve wildcard
  |     |     +-- enforce max length
  |     |     +-- escape output values
  |     |
  |     +-- L2: Apply runtime context
  |     |     +-- country
  |     |     +-- language
  |     |     +-- mobile or desktop
  |     |     +-- family page context
  |     |
  |     +-- L2: Apply subtype configuration
  |           +-- result count
  |           +-- spellcheck
  |           +-- typeahead
  |           +-- new filters
  |           +-- keep-my-filters
  |           +-- image or antigen search
  |
  +-- L1: Search execution
  |     |
  |     +-- L2: SearchResultsService.getResults
  |     +-- L2: Solr re-query when enabled
  |     +-- L2: product search count API when needed
  |     +-- L2: alternate search count requests
  |
  +-- L1: Response construction
        |
        +-- L2: product cards
        +-- L2: result header
        +-- L2: filter metadata
        +-- L2: alternate subtype links
        +-- L2: no-result or error state
```

### 6.3 Backend workflow - PDP, 2 levels deeper

```text
PDP request
  |
  +-- L1: Product identity and context
  |     |
  |     +-- L2: Resolve sku/webId from route
  |     +-- L2: Resolve product type and subtype
  |     +-- L2: Resolve country, language, login, and cookies
  |     +-- L2: Resolve canonical and breadcrumb paths
  |
  +-- L1: Product detail model
  |     |
  |     +-- L2: Load product detail payload
  |     +-- L2: Build ProductDetailViewModel
  |     +-- L2: Build subtype-specific view model
  |           +-- antibody detail view model
  |           +-- protein antibody detail view model
  |           +-- ELISA immunoassay detail view model
  |
  +-- L1: Content rules
  |     |
  |     +-- L2: product specifications map
  |     +-- L2: bioinformatics availability check
  |     +-- L2: target information
  |     +-- L2: references and scholarly articles
  |     +-- L2: documents and data sheet links
  |
  +-- L1: Commerce rules
  |     |
  |     +-- L2: selected package lookup
  |     +-- L2: price lookup
  |     +-- L2: availability lookup
  |     +-- L2: lifecycle banner rules
  |     +-- L2: add-to-cart eligibility
  |
  +-- L1: External widgets and enrichment
        |
        +-- L2: related products service
        +-- L2: Q and A service
        +-- L2: CiteAb reference source
        +-- L2: promotions service
        +-- L2: certificates/documents service
```

### 6.4 Backend workflow - Commerce card, 2 levels deeper

```text
Selected package
  |
  +-- L1: Package resolution
  |     |
  |     +-- L2: match package by webId
  |     +-- L2: fallback match by sku
  |     +-- L2: bind package size and child SKUs
  |     +-- L2: refresh document and banner context
  |
  +-- L1: Price resolution
  |     |
  |     +-- L2: call pricing API when product type and country allow it
  |     +-- L2: map PricingDetails to currency and list price
  |     +-- L2: handle no-price, not-orderable, anonymous, and pricing error states
  |
  +-- L1: Availability resolution
  |     |
  |     +-- L2: call availability API when enabled for runtime context
  |     +-- L2: evaluate available quantity
  |     +-- L2: evaluate estimated/pending status
  |     +-- L2: apply country, login, and dealer-specific behavior
  |
  +-- L1: Add to Cart contract
        |
        +-- L2: require active/orderable package
        +-- L2: block discontinued and long-term unavailable states
        +-- L2: enforce quantity 1 through 9999
        +-- L2: pass selected webId/SKU to cart integration
```

### 6.5 Backend workflow - Related products, 2 levels deeper

```text
PDP related product request
  |
  +-- L1: Magellan search config
  |     |
  |     +-- L2: relatedProductsEnabled
  |     +-- L2: relatedProductsEnabledProductSubTypes
  |     +-- L2: elisaRelatedProductsEnabled
  |     +-- L2: widget V2 URL selection
  |
  +-- L1: Related products service lookup
  |     |
  |     +-- L2: validate SKU
  |     +-- L2: validate antibody or immunoassay type
  |     +-- L2: check cache by sku and country
  |     +-- L2: retrieve data science results when cache misses
  |     +-- L2: enrich with catalog API in parallel
  |     +-- L2: cache response by sku and country
  |
  +-- L1: Product service detail aggregation
        |
        +-- L2: validate request
        +-- L2: split Magellan SKUs by type m
        +-- L2: split catalog SKUs by type c
        +-- L2: call related product detail service
        +-- L2: call catalog SKU details service
        +-- L2: return merged detail response
```

### 6.6 Backend workflow - Q and A, 2 levels deeper

```text
Q and A request
  |
  +-- L1: PDP gating
  |     |
  |     +-- L2: qnaModuleEnabled
  |     +-- L2: qandaEnabledProductSubTypes
  |     +-- L2: qnaEnabledCountries
  |     +-- L2: page and limit defaults
  |
  +-- L1: Question retrieval
  |     |
  |     +-- L2: get SKU keywords from Solr
  |     +-- L2: query questions by SKU and keyword map
  |     +-- L2: build paginated QuestionList
  |     +-- L2: support keyword filtered retrieval
  |
  +-- L1: Keyword filtering and highlighting
  |     |
  |     +-- L2: HTML encode input keywords
  |     +-- L2: replace special characters for Solr
  |     +-- L2: remove trailing wildcard where needed
  |     +-- L2: add Greek-symbol variants
  |     +-- L2: dedupe and sort keywords by length descending
  |     +-- L2: highlight matched question and answer content
  |
  +-- L1: Submission and voting
        |
        +-- L2: validate SKU or assay product ID
        +-- L2: validate content
        +-- L2: validate hidden state when user key is present
        +-- L2: submit question or answer through service
        +-- L2: increment or decrement answer votes
```

## 7. Backend API and Service Contracts

| API area | Repository | Endpoint or function | Method | Request inputs | Response or side effect |
| --- | --- | --- | --- | --- | --- |
| Search count | `magellan-search` | `productSearchCountAPI` | GET | keyword, subtype, country/language context | Product search counts for cards or alternate search |
| Search execution | `magellan-search` | `SearchResultsService.getResults` | Internal service | `SearchModel` with keyword, subtype, filters, result count | Search results, filters, counts, no-result state |
| Related product detail aggregation | `tfcom-magellan-product-service` | `/fetchRelatedProductDetails` | POST | JSON body `MagellanRelatedProductsSearchRequest`, optional `x-host-header`, cookies | Merged Magellan and catalog product details |
| Dynamic antibody related products | `tfcom-magellan-related-products-service` | `/v2/relatedProducts/antibody/sku/{sku}/type/{type}` | GET | sku, antibody type, countryCode, languageCode, `CK_CUSTOMER_INFO` cookie | `TargetProduct` related product response |
| Dynamic immunoassay related products | `tfcom-magellan-related-products-service` | `/v2/relatedProducts/immunoassays/sku/{sku}` | GET | sku, countryCode, languageCode, `CK_CUSTOMER_INFO` cookie | ELISA/immunoassay related product response |
| Related product count | `tfcom-magellan-related-products-service` | `/v2/relatedProducts/antibody/fetchCount/sku/{sku}/type/{type}` | GET | sku, antibody type, countryCode, languageCode, user cookie | `TargetProductCount` with application count |
| Q and A list | `tfcom-magellan-qanda-service` | `magellan/sku/{sku}/questions` | GET | sku, page, limit | Paginated `QuestionList` |
| Q and A keyword list | `tfcom-magellan-qanda-service` | `/magellan/sku/{sku}/questions/keywords` | GET | sku, keywords, page, limit | Keyword-filtered and highlighted `QuestionList` |
| Q and A single question position | `tfcom-magellan-qanda-service` | `magellan/sku/{sku}/questions/{id}` | GET | sku, question id, limit | Question page containing requested question |
| Q and A answers | `tfcom-magellan-qanda-service` | `/magellan/questions/{questionId}/answers` | GET | question id | Question with answers |
| Q and A highlighted answers | `tfcom-magellan-qanda-service` | `/magellan/questions/{questionId}/answers/keywords` | GET | question id, keywords | Question with highlighted answers |
| Submit question | `tfcom-magellan-qanda-service` | `/magellan/questions` | POST | `QuestionRequest` | Created response or validation/post-processing error |
| Submit answer | `tfcom-magellan-qanda-service` | `/magellan/answers` | POST | `AnswerSubmitRequest` | Created response or validation/post-processing error |
| Vote answer up | `tfcom-magellan-qanda-service` | `/magellan/answers/{id}/incrementVotes` | PUT | answer id | Updated vote count |
| Vote answer down | `tfcom-magellan-qanda-service` | `/magellan/answers/{id}/decrementVotes` | PUT | answer id | Updated vote count |
| Pricing | `magellan-search` config | `/api/magellan/pricing/` | Service call | selected SKU/webId, product type, country/session context | Price, currency, not-orderable, no-price, or error state |
| Availability | `magellan-search` config | `/api/store/sku/availability/` | Service call | selected SKU/webId, quantity, country/session context | Stock, estimate, pending, or unavailable state |
| Promotions | `magellan-search` config | `/api/store/promotions/engine/v1/suggestions` or `/api/store/coupons/eligiblePromos` | Service call | part number/product id, quantity, country | Promotion suggestions or eligible promotions |

## 8. Backend Business Rules

### 8.1 Subtype and route rules

| Rule ID | Backend rule | Primary module evidence |
| --- | --- | --- |
| BR-SUB-001 | Resolve all search and PDP behavior through `ProductSubType` instead of hard-coded URL strings. | `ProductSubType.java` |
| BR-SUB-002 | Antibody product subtypes use product type `antibody`; ELISA uses product type `immunoassay`. | `ProductSubType.java` |
| BR-SUB-003 | Proteins and Peptides must switch to `/proteins/` search and PDP URLs when new protein URL flags are enabled. | `ProductSubType.getBaseUrl`, `ProductSubType.getSearchURL` |
| BR-SUB-004 | ELISA target links must switch based on `elisaTFPEnabled`. | `ProductSubType`, `PdpAeoMarkdownBuilder.resolveBreadcrumbPath` |
| BR-SUB-005 | Backend responses must preserve country and language context for search, PDP, related products, Q and A, pricing, and availability. | `config.yaml`, controllers |

### 8.2 Product commerce card, price, and availability

| Rule ID | Backend rule | Primary module evidence |
| --- | --- | --- |
| BR-COM-001 | Selected package must drive price, availability, documents, banner, package SKU, and cart identity. | Business rules, `appendPricingDetails` |
| BR-COM-002 | Price lookup must match selected package by `webId` or `sku`. | `PdpAeoMarkdownBuilder.appendPricingDetails` |
| BR-COM-003 | Pricing must return currency and list price when `PricingDetails` is present. | `appendPricingDetails` |
| BR-COM-004 | Pricing integration is enabled for `ANTIBODY` and `IMMUNOASSAY` product types by config. | `newPricingApiEnabledProducts` |
| BR-COM-005 | Pricing error states must not incorrectly mark non-orderable child SKUs as available. | Business rules |
| BR-COM-006 | Availability must be checked using selected package and quantity. | Business rules, availability config |
| BR-COM-007 | Available quantity greater than zero means in-stock; missing exact quantity may map to estimated or pending state. | Business rules |
| BR-COM-008 | Add to Cart must be blocked for discontinued and long-term unavailable products. | Business rules, `ProductDetailConstants` status labels |
| BR-COM-009 | Add to Cart must enforce quantity range 1 through 9999. | Business rules |

### 8.3 Banner near product title

| Rule ID | Backend rule | Primary module evidence |
| --- | --- | --- |
| BR-BAN-001 | Product lifecycle state must be available to the PDP response so the UI can render status banners. | Business rules, status constants |
| BR-BAN-002 | Package-specific lifecycle messages must refresh when package selection changes. | Business rules |
| BR-BAN-003 | Backend banner messages are controlled by `bannerMessagesEnabled` and `backendBannerEnabled`. | `config.yaml` |
| BR-BAN-004 | Discontinued and long-term unavailable statuses must be represented consistently across banner and commerce rules. | `ProductDetailConstants` |

### 8.4 Product specifications

| Rule ID | Backend rule | Primary module evidence |
| --- | --- | --- |
| BR-SPEC-001 | Specification maps must omit empty values. | `getABPopulateMap`, `appendProductSpecifications` |
| BR-SPEC-002 | Product specifications must use subtype-specific labels and omissions. | `getAntibodyProductSpecificationsTableMap` |
| BR-SPEC-003 | Proteins and Peptides must use `Species` label and omit host/isotype. | `getAntibodyProductSpecificationsTableMap` |
| BR-SPEC-004 | RRID must be emitted as an Antibody Registry link when present. | `appendProductSpecifications`, tests |
| BR-SPEC-005 | Shipping condition must be included only when `enableShippingCondition` is enabled. | `getAntibodyProductSpecificationsTableMap` |
| BR-SPEC-006 | ELISA product properties must come from immunoassay/ELISA view model data. | `appendElisaProductDetails` |

### 8.5 Bioinformatics and target information

| Rule ID | Backend rule | Primary module evidence |
| --- | --- | --- |
| BR-BIO-001 | Bioinformatics must render only when the subtype flag and `isShowBio` content checks pass. | `isBioInformaticDisplayed`, `isShowBio` |
| BR-BIO-002 | Antibody/protein bioinformatics may include protein aliases, gene aliases, UniProt, Entrez Gene ID, functions, and processes. | `appendBioinformaticsDetails` |
| BR-BIO-003 | ELISA bioinformatics may include gene aliases, gene ID, gene symbol, protein aliases, and UniProt. | `appendBioinformaticsDetails` |
| BR-BIO-004 | UniProt and Entrez entries must include links when URLs are available. | `extractLinkedBioinformaticsEntries` |
| BR-BIO-005 | Panther function/process URLs must encode values and retain plugin parameters. | `buildPantherBioinformaticsUrl` |
| BR-TGT-001 | Target URL generation must normalize target name and subtype path consistently. | `getTargetNameLink`, `resolveBreadcrumbPath` |
| BR-TGT-002 | ELISA target information must include target name, target list, and product description when present. | `appendElisaTargetInfo` |

### 8.6 References and scholarly articles

| Rule ID | Backend rule | Primary module evidence |
| --- | --- | --- |
| BR-REF-001 | Reference count must prefer CiteAb count when citation display is enabled and count is positive. | `resolveReferenceCount` |
| BR-REF-002 | If CiteAb count is unavailable, fallback to product detail reference count and then view model reference count. | `resolveReferenceCount` |
| BR-REF-003 | JSON-LD scholarly articles must be emitted when available. | `PdpAeoMarkdownBuilderTest` |
| BR-REF-004 | CiteAb titles may be used as fallback when JSON-LD is unavailable and citation display is enabled. | `PdpAeoMarkdownBuilderTest` |
| BR-REF-005 | Product references and published figures counts must be exposed to PDP output where present. | `appendHeroDetails` |

### 8.7 Questions and Answers

| Rule ID | Backend rule | Primary module evidence |
| --- | --- | --- |
| BR-QNA-001 | Q and A module must be gated by global config, subtype config, and enabled country list. | `isQuestionsAndAnswersEnabled`, `isQuestionsAndAnswersEnabledCountries` |
| BR-QNA-002 | Q and A service defaults use page `1` and limit `20` from config unless overridden by request. | `config.yaml` |
| BR-QNA-003 | Q and A keyword search must encode HTML and escape characters before Solr lookup. | `MagellanActionController` |
| BR-QNA-004 | Keyword highlighting must add Greek variants, dedupe, sort longest-first, and highlight question/answer content. | `getKeywordsList`, `highlightQuestions`, `highlightAnswers` |
| BR-QNA-005 | Submit question requires SKU or assay product ID and non-empty content. | `MagellanSubmitQuestionAnswerController.submitQuestion` |
| BR-QNA-006 | Submit answer requires SKU or assay product ID, non-empty content, and question ID. | `submitAnswer` |
| BR-QNA-007 | When user key is present, hidden state must be present and must be `yes` or `no`. | `submitQuestion`, `submitAnswer` |

### 8.8 Related products

| Rule ID | Backend rule | Primary module evidence |
| --- | --- | --- |
| BR-RP-001 | Related products must be globally enabled and subtype-enabled before the PDP calls related product modules. | `relatedProductsEnabled`, `relatedProductsEnabledProductSubTypes` |
| BR-RP-002 | ELISA related products use ELISA-specific related product flags and module URL. | `elisaRelatedProductsEnabled`, `elisaRelatedProductsModuleURL` |
| BR-RP-003 | Dynamic related product service must validate SKU format and product type. | `DynamicRelatedProductsController`, `ValidSku`, `AntibodyType`, `AssayType` |
| BR-RP-004 | Dynamic related product service must check cache by SKU and country before data retrieval. | `cacheService.getRelatedProductsForSkuCountry` |
| BR-RP-005 | On cache miss, service retrieves source results, enriches via catalog API, then caches by SKU/country. | `dataService.retrieveResults`, `callCatalogAPIParallelRequest`, `cacheRelatedProductsForSkuCountry` |
| BR-RP-006 | Product service must split related SKU details into Magellan SKUs of type `m` and catalog SKUs of type `c`. | `createMagellanRelatedProductsRequest`, `createCatalogRelatedProductsRequest` |

## 9. Configuration and Feature Flags

| Config key | Known value or behavior | Backend impact |
| --- | --- | --- |
| `resultCountForProductSubTypes` | Primary 25, Secondary 25, Control 50, ELISA 50, Protein 50 | Search result pagination and counts |
| `resultCountForProductSubTypesForMobileAndTFP` | Primary 10 | Mobile/TFP result count override |
| `maxKeywordLength` | 250 | Search input validation |
| `newFilterEnabledProductSubTypes` | All five subtypes | Enables backend filter metadata for search |
| `newTypeAheadEnabledProductSubTypes` | Primary, Protein, ELISA | Typeahead eligibility |
| `spellCheckEnabledSubTypes` | Primary, Secondary, Control, ELISA | Spellcheck eligibility |
| `solrReQueryEnabledSubTypes` | All five subtypes | Re-query eligibility |
| `newPricingApiEnabledProducts` | `ANTIBODY;IMMUNOASSAY` | Pricing API eligibility |
| `newPricingApi` | `/api/magellan/pricing/` | Pricing endpoint |
| `newAvailabilityAPI` | `/api/store/sku/availability/` | Availability endpoint |
| `qnaModuleEnabled` | true | Global Q and A gate |
| `qnaEnabledCountries` | CA, US | Q and A country gate |
| `qandaEnabledProductSubTypes` | Primary, Secondary, Control | Q and A subtype gate from config |
| `relatedProductsEnabled` | true | Global related products gate |
| `relatedProductsEnabledProductSubTypes` | Primary, Secondary, Control, Protein | Antibody related products gate |
| `elisaRelatedProductsEnabled` | true | ELISA related products gate |
| `promotionSuggestionsApiEnabled` | true by default when blank or true | Promotion API selection |
| `bannerMessagesEnabled` | true | Banner message eligibility |
| `backendBannerEnabled` | true | Backend banner eligibility |
| `newProteinUrlEnabled` | true | Protein route switching |
| `newTFPProteinUrlEnabled` | true | Protein target family route behavior |
| `elisaTFPEnabled` | true | ELISA target family route behavior |

## 10. Data Model Responsibilities

| Data object or model | Repository | Backend responsibility |
| --- | --- | --- |
| `ProductSubType` | `magellan-search` | Encapsulate subtype URLs, product type, display labels, feature behavior, alternate search behavior |
| `ProductDetailViewModel` | `magellan-search` | Base PDP response model for product identity, packages, references, and common fields |
| `AntibodyProductDetailViewModel` | `magellan-search` | Antibody/protein subtype specifications, properties, links, bioinformatics, related products and Q and A gates |
| `ElisaProductDetailViewModel` | `magellan-search` | Immunoassay/ELISA details, About This Kit, target information, product properties |
| `PricingDetails` | `magellan-search` | Currency and list price for selected package |
| `RelatedProductsResponse` | `magellan-search` | Related products passed into AEO/PDP output |
| `MagellanRelatedProductsSearchRequest` | `tfcom-magellan-product-service` | Request body containing related SKU details, country, language |
| `CatalogRelatedProductsSearchRequest` | `tfcom-magellan-product-service` | Catalog SKU request created from type `c` SKUs |
| `TargetProduct` | `tfcom-magellan-related-products-service` | Related product response grouped by applications |
| `TargetProductCount` | `tfcom-magellan-related-products-service` | Related product count response |
| `QuestionList` | `tfcom-magellan-qanda-service` | Paginated list of Q and A questions |
| `QuestionWithAnswers` | `tfcom-magellan-qanda-service` | Single question with answers |
| `QuestionRequest` | `tfcom-magellan-qanda-service` | Submit-question request |
| `AnswerSubmitRequest` | `tfcom-magellan-qanda-service` | Submit-answer request |

## 11. Error Handling and Resilience

| Area | Expected backend handling | Evidence |
| --- | --- | --- |
| Invalid related product request | Validate request before downstream calls and return validation response when status is set. | `ValidationService.requestValidate` |
| Related product invalid SKU/type | Throw invalid input for empty SKU/type, invalid type, or invalid SKU pattern. | `DynamicRelatedProductsController.commonsRetrieveRelatedProducts` |
| Related product not found | Allow `RelatedProductNotFoundException` to surface as a not-found flow. | `DynamicRelatedProductsController` |
| Related product service error | Log sanitized SKU and return HTTP 500. | `Utility.sanitizeFields`, controller catch block |
| Q and A invalid input | Throw invalid input for missing SKU/content/question ID/hidden state. | `MagellanSubmitQuestionAnswerController` |
| Q and A submit persistence failure | Throw post-processing exception when entity is null or DB access fails. | `submitQuestion`, `submitAnswer` |
| Q and A retrieval invalid question | Throw invalid input when question ID does not resolve. | `retrieveAnswers`, `retrieveQuestionsWithoutPageNumber` |
| Pricing errors | Preserve product/package state while representing no-price, not-orderable, and pricing error states. | Business rules |
| Availability errors | Avoid showing stale availability; use pending/estimated/error state when exact data is unavailable. | Business rules |
| Optional content missing | Omit empty sections instead of emitting empty headings. | `appendProductSpecifications`, `appendBioinformaticsDetails`, ELISA tests |

## 12. Caching and Performance

| Area | Backend behavior | Performance expectation |
| --- | --- | --- |
| Related products | Check `RelatedProductsCachingService` by SKU and country before data retrieval. | Reduce repeated data source and catalog enrichment calls |
| Related products cache miss | Retrieve data source results, call catalog API in parallel, then cache response. | Keep PDP related products responsive on subsequent calls |
| Pricing | Uses pricing API timeout and cache settings from config. | Avoid blocking PDP indefinitely |
| Search counts | Async or parallel count processing is used in search count action where configured. | Avoid slow subtype cards and alternate search counts |
| Q and A | Uses Solr for keyword lookup and JPA for stored Q and A entities. | Keyword search and paginated retrieval should be bounded by page/limit |
| Core Redis caches | Config lists cache TTLs for pricing, citations, and related behaviors. | Validate TTLs before production changes |

## 13. Security and Compliance Notes

| Area | Requirement |
| --- | --- |
| User/session context | Backend calls must preserve relevant cookies and customer context where services require personalization. |
| Related products user info | Dynamic related products reads `CK_CUSTOMER_INFO` cookie when available. |
| Product service forwarding | Product service forwards cookie header and optional `x-host-header` to downstream services. |
| Q and A input handling | Q and A keyword filtering must HTML-encode input and escape Solr/special characters. |
| Logging | Sensitive fields such as SKU should be sanitized when included in error logs where utility support exists. |
| Dependency safety | Product, related-products, and Q and A service POMs include Log4Shell dependency enforcement. |
| Authentication/authorization | Q and A service includes Spring Security dependency; final endpoint security behavior should be validated in app config. |

## 14. Acceptance Criteria

| Area | Acceptance criteria |
| --- | --- |
| Search subtype routing | Backend resolves all five search routes to the correct product subtype, result count, filters, spellcheck/typeahead behavior, and alternate search behavior. |
| PDP subtype routing | Backend resolves PDP route SKU/webId and subtype, and creates correct canonical/breadcrumb/target links. |
| Product specifications | Backend omits empty specification fields and applies subtype-specific labels and omissions. |
| Bioinformatics | Backend exposes bioinformatics only when feature flags and content checks pass. |
| Target information | Backend emits target information and route links according to subtype-specific rules. |
| References | Backend returns reference count using CiteAb/product detail/view model fallback order and scholarly article fallback behavior. |
| Commerce | Backend returns price, availability, lifecycle status, and cart eligibility consistently for selected package. |
| Banner | Backend provides lifecycle/banner data that updates when package changes. |
| Related products | Backend enforces global/subtype gates, validates SKU/type, uses cache, enriches catalog data, and returns usable related product data. |
| Q and A | Backend enforces global/subtype/country gates, validates input, supports question listing, keyword filtering, answer retrieval, submission, and voting. |
| Errors | Backend returns controlled validation, not-found, pending, no-data, or service-error states without causing incomplete UI render failures. |

## 15. Backend Test Strategy

| Test area | Required tests |
| --- | --- |
| Product subtype mapping | Unit tests for enum mapping, URL generation, display labels, feature flags, alternate search links |
| Search model | Tests for keyword wildcard, blank keyword, keyword escaping, max length, result count, filters, spellcheck, typeahead |
| PDP view model | Tests for selected package, specs map, product-specific information, target info, bioinformatics visibility |
| Pricing | Tests for selected webId/SKU matching, currency/list price, no-price, not-orderable, pricing errors |
| Availability | Tests for package/quantity lookup, in-stock, pending, estimated, login/country-specific behavior |
| Banner | Tests for discontinued, long-term unavailable, package-specific message refresh |
| Related products | Tests for SKU validation, type validation, cache hit, cache miss, catalog enrichment, invalid input, not found, service error |
| Q and A | Tests for SKU keyword lookup, pagination, keyword escaping, Greek variants, highlighting, submit validation, answer vote updates |
| AEO/PDP content | Tests for sections omitted when empty, RRID link, UniProt/Entrez links, CiteAb fallback, JSON-LD scholarly articles |

## 16. Operational Requirements

| Operation area | Backend requirement |
| --- | --- |
| Monitoring | Track response time and error rate for search, PDP, pricing, availability, related products, Q and A, and product-service detail aggregation |
| Logs | Include subtype, SKU/webId, country, language, feature gate outcome, and sanitized identifiers where appropriate |
| Alerts | Alert on pricing/availability/Q and A/related-products error spikes and slow service calls |
| Runbooks | Provide triage steps for missing price, unavailable inventory, missing related products, missing Q and A, incorrect specs, incorrect lifecycle banner |
| Feature flags | Document owner and rollout process for pricing, availability, related products, Q and A, banner, protein URL, and ELISA TFP flags |
| Backward compatibility | Preserve existing routes and redirect behavior while new protein/ELISA route flags are enabled |

## 17. Risks and Validation Items

| Item | Risk or open question | Recommendation |
| --- | --- | --- |
| Full de-magellan repo inventory | Team repo page was not fully available as structured evidence. | Validate all owned backend repos with GitHub team admins. |
| Pricing service internals | Only consuming configuration and business rules were reviewed. | Validate pricing API contract, error codes, cache behavior, and entitlement behavior with pricing service owner. |
| Availability service internals | Only consuming configuration and business rules were reviewed. | Validate country gating and dealer-specific behavior with availability service owner. |
| Product detail controller path | Search/PDP orchestration modules were reviewed, but not every controller/template path. | Trace final request mapping before implementation estimates. |
| Secondary bioinformatics | Reviewed subtype evidence does not clearly confirm secondary bioinformatics enablement. | Validate current production behavior before adding or removing secondary bioinformatics output. |
| Q and A subtype coverage | Config evidence lists Primary, Secondary, and Control; user requested all five subtype areas. | Confirm whether Protein and ELISA Q and A should be intentionally disabled or enabled separately. |
| Related product response schema | Controller evidence confirms `TargetProduct`, but complete schema was not fully reviewed. | Pull OpenAPI/schema or POJOs before backend implementation. |
| Table of contents | Generated Word file may not include dynamic Word TOC fields. | Add or update TOC in Word if formal page numbering is required. |

## 18. Appendix: Example Pages

| Product family | Search example | PDP example |
| --- | --- | --- |
| Primary Antibody | `https://www.thermofisher.com/antibody/primary/query/*` | `https://www.thermofisher.com/antibody/product/Ki-67-Antibody-clone-SP6-Recombinant-Monoclonal/MA5-14520` |
| Secondary Antibody | `https://www.thermofisher.com/antibody/secondary/query/*` | `https://www.thermofisher.com/antibody/product/Goat-anti-Rabbit-IgG-H-L-Cross-Adsorbed-Secondary-Antibody-Polyclonal/A-11008` |
| Isotype Control | `https://www.thermofisher.com/antibody/control/query/*` | `https://www.thermofisher.com/antibody/product/Rabbit-IgG-Isotype-Control/02-6102` |
| Proteins and Peptides | `https://www.thermofisher.com/proteins/query/*` | `https://www.thermofisher.com/proteins/product/Human-FGF-basic-FGF-2-bFGF-154-aa-Recombinant-Protein/100-18B-50UG` |
| ELISA Kits | `https://www.thermofisher.com/elisa/query/*` | `https://www.thermofisher.com/elisa/product/Human-IL-18-ProQuantum-Immunoassay-Kit/A35613` |

