# UI Developer PRD: Antibody Product Series

Document date: July 23, 2026  
Audience: UI developers, QA engineers, product owners, business analysts, and integration teams  
Scope: Primary Antibodies, Secondary Antibodies, Isotype Controls, Proteins and Peptides, and ELISA Kits search and product detail pages  
Primary repo evidence: `thermofisher/magellan-search`  
Supporting repo and service evidence: de-magellan repository list, local business rules documents, and service URLs configured in `magellan-search`

## 1. Document Purpose

This PRD describes the UI behavior, business rules, functional architecture, workflow layers, module touchpoints, and integration expectations for the antibody product series search and product detail experiences.

The document is written from a UI developer perspective. It identifies the repository, Java modules, view models, constants, configuration keys, service endpoints, feature flags, and important functions that drive the user interface.

This document uses the previously generated business rules for the five product subtypes and code evidence from `thermofisher/magellan-search`. Rules or architectural details that were not directly visible in the available repo evidence are marked as validation items or assumptions instead of being invented.

## 2. Source Evidence and Review Boundary

### 2.1 Reviewed local documents

- `Primary_Antibody_Product_Series_Business_Rules.docx`
- `Secondary_Antibody_Product_Series_Business_Rules.docx`
- `Isotype_Controls_Product_Series_Business_Rules.docx`
- `Proteins_Peptides_Product_Series_Business_Rules.docx`
- `ELISA_Product_Series_Business_Rules.docx`
- Search business rules documents for the same product subtypes where present in the attached business rules package
- `business-rule-extraction-prompt-v3.1.md`

### 2.2 Reviewed repo

Primary code evidence was available from:

- Repository: `thermofisher/magellan-search`
- Branch observed: `master`

Important reviewed files:

- `src/main/java/com/lifetech/magellan/constants/ProductSubType.java`
- `src/main/resources/config.yaml`
- `src/main/java/com/lifetech/magellan/v2/productdetail/model/AntibodyProductDetailViewModel.java`
- `src/main/java/com/lifetech/magellan/v2/productdetail/util/PdpAeoMarkdownBuilder.java`
- `src/main/java/com/lifetech/magellan/v2/productdetail/constants/ProductDetailConstants.java`
- `src/main/java/com/lifetech/magellan/action/UnifiedCardProductTypeCountAction.java`
- `src/test/java/com/lifetech/magellan/v2/productdetail/util/PdpAeoMarkdownBuilderTest.java`
- `src/test/java/com/lifetech/magellan/v2/search/model/AntibodySearchResultsViewModelTest.java`

### 2.3 Access limitation

The exact `de-magellan` team repository membership page was not directly available as a full machine-readable team list from the environment. The PRD therefore uses the accessible Magellan repo evidence, local rules package, and configured service integration names. Any implementation assignment across other de-magellan repos should be validated by repository owners before delivery planning.

## 3. Product Overview

### 3.1 Product name

Antibody Product Series Search and Product Detail UI

### 3.2 Owner

Owner is not explicitly defined in the reviewed repo evidence. The functional ownership appears to sit across Magellan search, product detail, commerce, related products, Q and A, pricing, availability, and content service teams.

### 3.3 Purpose

The experience helps customers discover, compare, evaluate, and purchase antibody-related products. It supports search workflows, filters, product detail content, commerce actions, references, target biology information, related products, and support information.

### 3.4 Business goals

- Allow customers to find relevant antibody-related products by keyword, target, application, species, host, conjugate, and subtype.
- Present PDP content that supports scientific selection and purchase confidence.
- Show correct package-specific price, availability, cart eligibility, lifecycle messages, and documentation.
- Provide subtype-specific biological content such as bioinformatics, target information, citations, and product specifications.
- Support cross-sell and discovery through related products and alternate search.
- Enable country, language, login, entitlement, and configuration-based UI behavior.

### 3.5 In scope

- Search pages for:
  - Primary Antibodies
  - Secondary Antibodies
  - Isotype Controls
  - Proteins and Peptides
  - ELISA Kits
- PDP pages for the same product subtypes
- Commerce card behavior including price, availability, quantity, orderability, and Add to Cart eligibility
- Banner behavior near product title
- Product specifications and product-specific content
- Bioinformatics and target information
- References and scholarly article rendering
- Questions and Answers
- Related products
- Developer-facing architecture, modules, functions, service endpoints, and data flow

### 3.6 Out of scope

- TaqMan assay and array pages
- Admin catalog authoring screens
- Backend service implementation details outside interfaces/configuration visible from reviewed code
- Final UX copy approval and visual design token decisions unless explicitly stated in business rules

## 4. Product Subtypes and Routes

| Subtype | Search example | PDP example | ProductSubType enum | Product type | Product subtype value | Main URL behavior |
| --- | --- | --- | --- | --- | --- | --- |
| Primary Antibody | `/antibody/primary/query/*` | `/antibody/product/Ki-67-Antibody-clone-SP6-Recombinant-Monoclonal/MA5-14520` | `ANTIBODY_PRIMARY` | `antibody` | `antibody_primary` | Search path `/antibody/primary/`; PDP base `/antibody/product/` |
| Secondary Antibody | `/antibody/secondary/query/*` | `/antibody/product/Goat-anti-Rabbit-IgG-H-L-Cross-Adsorbed-Secondary-Antibody-Polyclonal/A-11008` | `ANTIBODY_SECONDARY` | `antibody` | `antibody_secondary` | Search path `/antibody/secondary/`; PDP base `/antibody/product/` |
| Isotype Control | `/antibody/control/query/*` | `/antibody/product/Rabbit-IgG-Isotype-Control/02-6102` | `ANTIBODY_CONTROL` | `antibody` | `antibody_control` | Search path `/antibody/control/`; PDP base `/antibody/product/` |
| Proteins and Peptides | `/proteins/query/*` | `/proteins/product/Human-FGF-basic-FGF-2-bFGF-154-aa-Recombinant-Protein/100-18B-50UG` | `ANTIBODY_PROTEIN` | `antibody` | `antibody_protein` | Uses `/proteins/product/` and `/proteins/` when new protein URL flags are enabled |
| ELISA Kits | `/elisa/query/*` | `/elisa/product/Human-IL-18-ProQuantum-Immunoassay-Kit/A35613` | `ELISA` | `immunoassay` | `ELISA` | Uses `/elisa/product/`, `/elisa/`, and target URL switching based on ELISA TFP flag |

## 5. Users and Stakeholders

### 5.1 User personas

| Persona | Need |
| --- | --- |
| Research scientist | Find scientifically appropriate products quickly using target, species, application, host, conjugate, assay, validation, and reference evidence. |
| Procurement user | Confirm catalog number, package size, price, availability, orderability, and cart eligibility. |
| Lab manager | Compare options, evaluate related products, validate target and application fit, and ensure purchasing continuity. |
| Support specialist | Explain product lifecycle, availability, technical resources, Q and A, protocols, and documentation. |
| SEO/AEO consumer | Receive structured, complete PDP content through schema, canonical URLs, and markdown/JSON-LD outputs. |

### 5.2 Stakeholders

- Product owner for antibody search and PDP
- UI engineering team
- Search engineering team
- Product detail and catalog service owners
- Pricing and availability service owners
- Q and A service owner
- Related products service owner
- Content, SEO, and AEO stakeholders
- QA automation and regression teams
- Customer support and technical support teams

## 6. Repository and Module Map

### 6.1 Primary repository

| Repository | Role in this PRD |
| --- | --- |
| `thermofisher/magellan-search` | Main evidence source for product subtype routing, search behavior, PDP view model logic, markdown/AEO content generation, feature flags, endpoint configuration, and tests. |

### 6.2 Supporting services inferred from configuration

| Service or component | Evidence | UI relevance |
| --- | --- | --- |
| Product service | `productSearchCountAPI`, `newCatalogAPI`, `fetchRelatedProductDetailsUrl` | Search counts, catalog data, related product details, PDP package data. |
| Pricing API | `newPricingApi`, `useMagellanPricingAPI`, `newPricingApiEnabledProducts` | Product commerce card price rendering and orderability messaging. |
| Availability API | `newAvailabilityAPI`, `inventoryDataServiceUrl`, `enableEstimatedAvailability` | Availability panel and delivery/stock messaging. |
| Related products service/UI | `relatedSkuListApiUrl`, `relatedProductsModuleURL`, `relatedProductsWidgetV2` | Related products widgets on PDP. |
| Q and A service/UI | `qAndAServiceApiUrl`, `qnaWidgetAPI`, `aeoQnaApiBaseUrl`, `qnaModuleEnabled` | Questions and Answers module and AEO content. |
| Promotions APIs | `promotionAvailabilityAPI`, `promoSuggestionApiPath`, `promotionSuggestionsApiEnabled` | Promo banners and commerce recommendations. |
| CiteAb integration | `CiteAbService`, citation display functions | References count and scholarly article fallback. |
| Documents/certificates service | `CertificatesDocumentsResponse` | Data sheet, certificates, and documents sections. |

### 6.3 Important Java modules and functions

| Module | Important functions | Developer purpose |
| --- | --- | --- |
| `ProductSubType.java` | enum values, `getBaseUrl`, `getSearchURL`, `getDisplayText`, `getLinkUrl`, `isCitationDisplayed`, `isBioInformaticDisplayed`, `isQnAEnabled`, `isRelatedProductsEnabled`, `isBidProduct`, `isTargetAvailable` | Defines subtype routing, labels, alternate search, feature eligibility, and subtype-specific behavior. |
| `AntibodyProductDetailViewModel.java` | `getAntibodyProductPropertiesDefaultMap`, `getAntibodyProductSpecificationsTableMap`, `isShowBio`, `isQuestionsAndAnswersEnabled`, `isQuestionsAndAnswersEnabledCountries`, `isV2RelatedProductsEnabled`, `getRelatedProductsModuleURL`, `getShowProtocolsLink`, `getAdvancedVerificationLink`, `getTargetNameLink` | Main PDP view model logic for antibody, protein, isotype, secondary, and primary product sections. |
| `PdpAeoMarkdownBuilder.java` | `build`, `appendCoreSections`, `appendPricingDetails`, `appendPromotionsSection`, `appendHeroDetails`, `appendProductSpecifications`, `appendProductDetailSection`, `appendBioinformaticsDetails`, `appendRelatedProducts`, `appendQuestionsAndAnswers`, `resolveBreadcrumbPath` | Builds structured PDP content for AEO/SEO and mirrors many sections the UI must render. |
| `ProductDetailConstants.java` | section labels, status labels, URL prefixes, config keys | Single source of text constants and path fragments used by PDP output. |
| `UnifiedCardProductTypeCountAction.java` | `execute`, `createProductDetails`, `getSearchModel`, `updateCountBySiteSearchService`, `processUnifiedCardForSearchCount` | Search landing and unified product count behavior. |
| `PdpAeoMarkdownBuilderTest.java` | tests for RRID, Advanced Verification, ELISA content, bioinformatics, citations, CiteAb fallback | Confirms important PDP rules and expected rendering behavior. |
| `AntibodySearchResultsViewModelTest.java` | tests for result text, target pages, filters, canonical URLs, image search, antigen search, alternate search | Confirms search page and target family behavior. |

## 7. Functional Architecture

### 7.1 High-level architecture

```text
Level 0: Customer-facing experience

Customer Browser
  |
  +-- Search Pages
  |     |
  |     +-- Primary Antibody Search
  |     +-- Secondary Antibody Search
  |     +-- Isotype Control Search
  |     +-- Proteins and Peptides Search
  |     +-- ELISA Search
  |
  +-- Product Detail Pages
        |
        +-- PDP Header and Banner
        +-- Product Content Tabs and Sections
        +-- Commerce Card
        +-- References and Bioinformatics
        +-- Related Products
        +-- Questions and Answers
```

```text
Level 1 and Level 2: UI to backend flow

Browser route
  |
  +-- Route parser / controller
  |     |
  |     +-- Resolve product type and subtype
  |     |     +-- ProductSubType enum
  |     |     +-- Feature flags from config.yaml
  |     |     +-- Country/language/session context
  |     |
  |     +-- Search page path
  |     |     |
  |     |     +-- Build SearchModel
  |     |     |     +-- keyword
  |     |     |     +-- subtype
  |     |     |     +-- filters
  |     |     |     +-- pagination and result count
  |     |     |
  |     |     +-- Call SearchResultsService
  |     |     |     +-- Solr/product index
  |     |     |     +-- spellcheck
  |     |     |     +-- alternate subtype search counts
  |     |     |
  |     |     +-- Render UI
  |     |           +-- result header
  |     |           +-- filters
  |     |           +-- product cards
  |     |           +-- alternate results
  |     |           +-- image or antigen search entry points
  |     |
  |     +-- PDP path
  |           |
  |           +-- Build ProductDetailViewModel
  |           |     +-- product identity
  |           |     +-- package list
  |           |     +-- specifications
  |           |     +-- bioinformatics
  |           |     +-- references
  |           |
  |           +-- Enrich sections
  |           |     +-- price and availability
  |           |     +-- documents and certificates
  |           |     +-- related products
  |           |     +-- Q and A
  |           |     +-- promotions
  |           |
  |           +-- Render PDP UI
  |                 +-- title/banner
  |                 +-- package selector
  |                 +-- commerce card
  |                 +-- product details
  |                 +-- specifications
  |                 +-- target and bioinformatics
  |                 +-- references
  |                 +-- related products
  |                 +-- Q and A
```

### 7.2 Search workflow diagram

```text
Search route: /antibody/{subtype}/query/*, /proteins/query/*, /elisa/query/*
  |
  +-- L1: Request interpretation
  |     |
  |     +-- L2: Resolve subtype
  |     |     +-- ANTIBODY_PRIMARY
  |     |     +-- ANTIBODY_SECONDARY
  |     |     +-- ANTIBODY_CONTROL
  |     |     +-- ANTIBODY_PROTEIN
  |     |     +-- ELISA
  |     |
  |     +-- L2: Validate keyword
  |     |     +-- allow wildcard example *
  |     |     +-- enforce maxKeywordLength = 250
  |     |     +-- escape output keyword before response
  |     |
  |     +-- L2: Apply country/language context
  |           +-- current country
  |           +-- current language
  |           +-- login state where relevant
  |
  +-- L1: Search assembly
  |     |
  |     +-- L2: Result count configuration
  |     |     +-- primary: 25 desktop, 10 mobile/TFP
  |     |     +-- secondary: 25
  |     |     +-- isotype: 50
  |     |     +-- protein: 50
  |     |     +-- ELISA: 50
  |     |
  |     +-- L2: Feature flags
  |     |     +-- new filters enabled for all five subtypes
  |     |     +-- spellcheck enabled for primary, secondary, control, ELISA
  |     |     +-- typeahead enabled for primary, protein, ELISA
  |     |     +-- keep-my-filters enabled for all five subtypes
  |     |
  |     +-- L2: Search service call
  |           +-- SearchResultsService.getResults
  |           +-- product/service count APIs where configured
  |           +-- Solr re-query for enabled subtypes
  |
  +-- L1: UI response
        |
        +-- L2: Header
        |     +-- blank keyword shows generic result count
        |     +-- wildcard keyword shows results for "*"
        |     +-- target context adds target/application postfix
        |
        +-- L2: Filter panel
        |     +-- subtype-specific filters
        |     +-- selected filter state
        |     +-- no-exact-match preselected filter handling
        |
        +-- L2: Result list
        |     +-- cards
        |     +-- pagination
        |     +-- sorting where available
        |
        +-- L2: Empty or alternate search
              +-- show alternate subtype links when counts are available
              +-- show no-result state when no alternate model is available
```

### 7.3 PDP workflow diagram

```text
PDP route: /antibody/product/{slug}/{sku}, /proteins/product/{slug}/{sku}, /elisa/product/{slug}/{sku}
  |
  +-- L1: Product identity
  |     |
  |     +-- L2: Resolve sku/webId
  |     +-- L2: Resolve ProductSubType
  |     +-- L2: Resolve canonical URL
  |     +-- L2: Resolve breadcrumbs and target URL
  |
  +-- L1: Product content model
  |     |
  |     +-- L2: Product title, brand, target, host, clone, conjugate
  |     +-- L2: Package list and selected package
  |     +-- L2: Product specifications table
  |     +-- L2: Product-specific information
  |     +-- L2: Target information
  |     +-- L2: Bioinformatics
  |     +-- L2: References and images/figures
  |
  +-- L1: Commerce model
  |     |
  |     +-- L2: Pricing request for selected package
  |     +-- L2: Availability request for selected package and quantity
  |     +-- L2: Lifecycle status check
  |     +-- L2: Add to Cart eligibility
  |     +-- L2: Promotions
  |
  +-- L1: External PDP modules
  |     |
  |     +-- L2: Related products
  |     +-- L2: Questions and Answers
  |     +-- L2: Documents and certificates
  |     +-- L2: Technical support or protocols links
  |
  +-- L1: Rendered page
        |
        +-- L2: Product title and lifecycle/banner area
        +-- L2: Package selector
        +-- L2: Price, availability, quantity, cart panel
        +-- L2: Details/specifications/content tabs
        +-- L2: Scientific validation and support sections
```

### 7.4 Commerce card workflow diagram

```text
Selected PDP package
  |
  +-- L1: Package selection state
  |     |
  |     +-- L2: selected catalog number/webId
  |     +-- L2: package size and child SKU list
  |     +-- L2: data sheet/catalog link refresh
  |     +-- L2: package-specific banner refresh
  |
  +-- L1: Price
  |     |
  |     +-- L2: call pricing API when product type and country are enabled
  |     +-- L2: display currency and list price when available
  |     +-- L2: handle no-price state for anonymous or entitled users
  |     +-- L2: remove child SKUs for configured pricing error codes while preserving parent display
  |
  +-- L1: Availability
  |     |
  |     +-- L2: call new availability API when enabled
  |     +-- L2: show in-stock when available quantity is greater than zero
  |     +-- L2: show estimated or pending states when exact quantity is not present
  |     +-- L2: vary behavior by login/country/dealer state where configured
  |
  +-- L1: Add to Cart
        |
        +-- L2: require orderable selected package
        +-- L2: block discontinued and long-term unavailable products
        +-- L2: enforce quantity 1 through 9999
        +-- L2: use selected webId as cart item identity
```

### 7.5 Scientific content workflow diagram

```text
ProductDetailViewModel
  |
  +-- L1: Product specifications
  |     |
  |     +-- L2: Build ordered map from subtype view model
  |     +-- L2: Remove empty values
  |     +-- L2: Apply subtype rules
  |     |     +-- proteins use Species instead of Species Reactivity
  |     |     +-- proteins omit host/isotype
  |     |     +-- target/cross adsorption/antibody form require target availability
  |     |
  |     +-- L2: Render RRID as Antibody Registry link when present
  |
  +-- L1: Bioinformatics
  |     |
  |     +-- L2: Check subtype bioinformatics flag
  |     +-- L2: Check isShowBio content availability
  |     +-- L2: Render protein aliases, gene aliases, UniProt, Entrez Gene ID
  |     +-- L2: Render functions/processes and Panther URLs where present
  |
  +-- L1: Target information
  |     |
  |     +-- L2: target name
  |     +-- L2: target list
  |     +-- L2: product description
  |     +-- L2: target-family URL when enabled
  |
  +-- L1: References
  |     |
  |     +-- L2: display product reference count
  |     +-- L2: prefer CiteAb count when eligible and count is positive
  |     +-- L2: render JSON-LD scholarly articles when available
  |     +-- L2: fallback to CiteAb titles when JSON-LD is unavailable and citation display is enabled
  |
  +-- L1: Q and A
        |
        +-- L2: require qnaModuleEnabled
        +-- L2: require subtype Q and A enabled
        +-- L2: require enabled country list
        +-- L2: load widget/API content using configured endpoints
```

## 8. Core Search Requirements

### 8.1 Common search requirements

| Requirement ID | Requirement | Source evidence |
| --- | --- | --- |
| SR-001 | The UI must resolve each search route to the correct `ProductSubType` and display label. | `ProductSubType.java` |
| SR-002 | The search keyword must be carried into the search model and escaped before rendering in user-visible response text. | `UnifiedCardProductTypeCountAction.execute` |
| SR-003 | The maximum keyword length must follow `maxKeywordLength`, configured as `250`. | `config.yaml` |
| SR-004 | Result count per page must use subtype configuration. | `resultCountForProductSubTypes`, `resultCountForProductSubTypesForMobileAndTFP` |
| SR-005 | New filters must be enabled for Primary, Secondary, Isotype Control, Proteins and Peptides, and ELISA when configured. | `newFilterEnabledProductSubTypes` |
| SR-006 | Keep-my-filters behavior must be available for all five subtypes when configured. | `keepMyFiltersEnabledSubTypes` |
| SR-007 | Spellcheck must be available for Primary, Secondary, Isotype Control, and ELISA when configured. | `spellCheckEnabledSubTypes` |
| SR-008 | Typeahead must be available for Primary, Proteins and Peptides, and ELISA when configured. | `newTypeAheadEnabledProductSubTypes` |
| SR-009 | Alternate search links must be displayed when zero or low-result conditions have available alternate subtype counts. | `ProductSubType.java`, `AntibodySearchResultsViewModelTest.java` |
| SR-010 | Search result header text must adapt for blank keyword, wildcard keyword, normal keyword, and target/application context. | `AntibodySearchResultsViewModelTest.java` |

### 8.2 Subtype search behavior

| Subtype | Search result count | Typeahead | Spellcheck | Special search behavior |
| --- | ---: | --- | --- | --- |
| Primary Antibody | 25 desktop; 10 mobile/TFP | Enabled | Enabled | Image search and antigen/epitope search entry points are enabled when family page and config allow them. |
| Secondary Antibody | 25 | Not enabled through new typeahead list | Enabled | CiteAb widget is enabled at subtype level; target availability is true. |
| Isotype Control | 50 | Not enabled through new typeahead list | Enabled | CiteAb widget is enabled at subtype level; alternate search to antibodies/proteins/ELISA is configured. |
| Proteins and Peptides | 50 | Enabled | Not listed in spellcheck config | Uses new protein URLs when flags are enabled; protein family search count is required when TFP protein flag is enabled. |
| ELISA Kits | 50 | Enabled | Enabled | Uses immunoassay collection and ELISA target URL switching when ELISA TFP flag is enabled. |

### 8.3 Search acceptance criteria

- Given a user opens `/antibody/primary/query/*`, the UI loads Primary Antibody search results using `ANTIBODY_PRIMARY`.
- Given a user opens `/proteins/query/*`, the UI loads Proteins and Peptides results and uses the new protein URL behavior when enabled.
- Given a wildcard keyword is used, the header text includes results for `"*"`.
- Given a blank keyword is used, the header shows a generic count without a keyword phrase.
- Given no exact match is available but preselected filters exist, the UI preserves and displays relevant filter state.
- Given alternate subtype counts exist, the UI displays links to alternate product categories with formatted counts.
- Given no results and no alternate model, the UI displays a no-result state rather than an empty product list.

## 9. Core PDP Requirements

### 9.1 PDP page frame

| Requirement ID | Requirement | Source evidence |
| --- | --- | --- |
| PDP-001 | The PDP must resolve product identity by SKU/webId and subtype. | Product detail view model usage |
| PDP-002 | The PDP must render canonical and breadcrumb URLs using subtype-specific route rules. | `resolveBreadcrumbPath`, `getCanonicalHrefPath` |
| PDP-003 | Product title, brand, product ID, package options, and selected package must be visible or available to the UI. | Business rules, `AntibodyProductDetailViewModel` |
| PDP-004 | Lifecycle banner messages must respond to product/package status such as discontinued and long-term unavailable. | Business rules, status constants |
| PDP-005 | Banner dismissal must hide the banner on the client without changing product/package selection state. | Business rules |

### 9.2 Product commerce card

| Requirement ID | Requirement | Source evidence |
| --- | --- | --- |
| COM-001 | The selected package must drive SKU, data sheet, catalog links, price, availability, and banner refresh. | Business rules |
| COM-002 | Pricing must use the selected package webId/SKU and display currency and list price when pricing details are present. | `appendPricingDetails` |
| COM-003 | Pricing is enabled for antibody and immunoassay product types through config. | `newPricingApiEnabledProducts` |
| COM-004 | Anonymous users may see sign-in driven price/availability prompts when exact price is unavailable. | Business rules |
| COM-005 | Long-term unavailable products must not allow normal ordering and should show Contact Us behavior where defined. | Business rules |
| COM-006 | Discontinued products must not allow ordering. | Business rules, status constants |
| COM-007 | Add to Cart requires a valid selected package, orderable status, and quantity within allowed limits. | Business rules |
| COM-008 | Quantity must be constrained to 1 through 9999. | Business rules |
| COM-009 | Availability must be refreshed when package or quantity changes. | Business rules, availability config |
| COM-010 | Availability must respect country/login/dealer rules where configured. | Business rules, availability config |

### 9.3 Banner near product title

| Requirement ID | Requirement | Source evidence |
| --- | --- | --- |
| BAN-001 | The PDP must display lifecycle messages near the product title when product or package status requires it. | Business rules |
| BAN-002 | Package-specific messages must change when package selection changes. | Business rules |
| BAN-003 | The banner must support close/dismiss behavior without mutating underlying product state. | Business rules |
| BAN-004 | Backend banner messages are feature-flag controlled. | `bannerMessagesEnabled`, `backendBannerEnabled` |

### 9.4 Product specifications

| Requirement ID | Requirement | Source evidence |
| --- | --- | --- |
| SPEC-001 | The product specifications table must omit empty values. | `getABPopulateMap`, `appendProductSpecifications` |
| SPEC-002 | Primary, Secondary, and Isotype products must use antibody-specific labels such as Species Reactivity where applicable. | `getAntibodyProductSpecificationsTableMap` |
| SPEC-003 | Proteins and Peptides must use `Species` instead of `Species Reactivity`. | `getAntibodyProductSpecificationsTableMap` |
| SPEC-004 | Proteins and Peptides must omit host and isotype. | `getAntibodyProductSpecificationsTableMap` |
| SPEC-005 | Shipping condition must appear only when `enableShippingCondition` is enabled. | `getAntibodyProductSpecificationsTableMap` |
| SPEC-006 | RRID must render as an Antibody Registry link when present. | `appendProductSpecifications`, tests |
| SPEC-007 | Target, cross adsorption, and antibody form must render only when the subtype marks target as available. | `productSubType.isTargetAvailable` logic |
| SPEC-008 | ELISA product details must use immunoassay view model product properties and ELISA-specific sections. | `appendProductDetailSection`, `appendElisaProductDetails` |

### 9.5 Bioinformatics

| Requirement ID | Requirement | Source evidence |
| --- | --- | --- |
| BIO-001 | Bioinformatics must render only when the subtype has bioinformatics enabled and `isShowBio` has content. | `isBioInformaticDisplayed`, `isShowBio`, `appendBioinformaticsDetails` |
| BIO-002 | Antibody/protein bioinformatics may include protein aliases, gene aliases, UniProt, Entrez Gene ID, Functions, and Processes. | `appendBioinformaticsDetails` |
| BIO-003 | ELISA bioinformatics may include gene aliases, gene ID, gene symbol, protein aliases, and UniProt. | `appendBioinformaticsDetails` |
| BIO-004 | UniProt and Entrez entries must render as linked entries when URLs are available. | `extractLinkedBioinformaticsEntries` |
| BIO-005 | Panther function/process URLs must be generated with encoded values and plugin parameters when applicable. | `buildPantherBioinformaticsUrl` |

### 9.6 Target information

| Requirement ID | Requirement | Source evidence |
| --- | --- | --- |
| TGT-001 | Target name and target URL must be generated consistently from subtype and target name. | `getTargetNameLink`, `resolveBreadcrumbPath` |
| TGT-002 | Primary and Secondary breadcrumb target URLs must use `/antibody/{subtype}/target/{target}`. | `resolveBreadcrumbPath` |
| TGT-003 | Proteins and Peptides target behavior must switch based on new TFP protein URL flag. | `resolveBreadcrumbPath` |
| TGT-004 | ELISA target behavior must switch based on ELISA TFP flag. | `resolveBreadcrumbPath` |
| TGT-005 | ELISA target section must include target name, target list, and product description when present. | `appendElisaTargetInfo` |

### 9.7 References and scholarly articles

| Requirement ID | Requirement | Source evidence |
| --- | --- | --- |
| REF-001 | Reference count must prefer CiteAb count when citation display is enabled and CiteAb count is positive. | `resolveReferenceCount` |
| REF-002 | If CiteAb count is not available, use product detail reference count or view model reference count. | `resolveReferenceCount` |
| REF-003 | JSON-LD scholarly article data must render when available. | `PdpAeoMarkdownBuilderTest` |
| REF-004 | When JSON-LD is unavailable and citation display is enabled, CiteAb titles may be used as fallback. | `PdpAeoMarkdownBuilderTest` |
| REF-005 | Citation display is enabled by subtype, including Primary, Secondary, and Isotype Control. | `ProductSubType.java` |

### 9.8 Questions and Answers

| Requirement ID | Requirement | Source evidence |
| --- | --- | --- |
| QNA-001 | Q and A must render only when `qnaModuleEnabled` is true. | `isQuestionsAndAnswersEnabled`, config |
| QNA-002 | Q and A must render only for subtypes that enable Q and A. | `productSubType.isQnAEnabled` |
| QNA-003 | Q and A must respect enabled countries, configured as `CA,US`. | `isQuestionsAndAnswersEnabledCountries`, config |
| QNA-004 | Q and A service API page and limit default to page `1` and limit `20`. | `qAndAServiceApiPage`, `qAndAServiceApiLimit` |
| QNA-005 | Q and A UI must use configured widget/API endpoints and support lazy loading threshold when configured. | `qnaWidgetAPI`, `aeoQnaApiBaseUrl`, `qnaLoaderThreshold` |

### 9.9 Related products

| Requirement ID | Requirement | Source evidence |
| --- | --- | --- |
| RP-001 | Related products are globally enabled by `relatedProductsEnabled`. | config |
| RP-002 | Related products must also be enabled by subtype. | `isV2RelatedProductsEnabled`, `ProductSubType.java` |
| RP-003 | Primary, Secondary, Isotype Control, and Proteins and Peptides are enabled in `relatedProductsEnabledProductSubTypes`. | config |
| RP-004 | ELISA related products are controlled by ELISA-specific related products config. | `elisaRelatedProductsEnabled`, `elisaRelatedProductsModuleURL` |
| RP-005 | The related products module URL must append `v2/` when the V2 widget flag is enabled. | `getRelatedProductsModuleURL`, `relatedProductsWidgetV2` |
| RP-006 | Related product details should be fetched through configured related SKU and product detail service endpoints. | `relatedSkuListApiUrl`, `fetchRelatedProductDetailsUrl` |

## 10. Subtype-Specific UI Requirements

### 10.1 Primary Antibody

Primary Antibody pages must emphasize target, application, validation, species reactivity, citations, bioinformatics, images, and supporting documents.

Important implementation references:

- `ProductSubType.ANTIBODY_PRIMARY`
- `PrimaryAntibodyProductDetailViewModel`
- `AntibodyProductDetailViewModel.getShowProtocolsLink`
- `AntibodyProductDetailViewModel.getAdvancedVerificationLink`
- `PdpAeoMarkdownBuilder.appendHeroDetails`
- `PdpAeoMarkdownBuilder.appendBioinformaticsDetails`

Rules:

- Search supports typeahead, spellcheck, new filters, keep-my-filters, image search, antigen/epitope search, alternate search, and Solr re-query when enabled.
- PDP shows citation/reference counts and bioinformatics when configured and content exists.
- Protocols link is available only for primary antibody subtype when citation display and protocol flag allow it.
- Advanced Verification link appears only when available.
- Green badge appears only for configured countries.
- RRID must link to Antibody Registry when present.

### 10.2 Secondary Antibody

Secondary Antibody pages must emphasize host species, target species, cross adsorption, conjugate, application, references, and commerce package details.

Important implementation references:

- `ProductSubType.ANTIBODY_SECONDARY`
- `SecondaryAntibodyProductDetailViewModel`
- `AntibodyProductDetailViewModel.getAntibodyProductSpecificationsTableMap`
- `PdpAeoMarkdownBuilder.resolveReferenceCount`

Rules:

- Search supports spellcheck, filters, keep-my-filters, alternate search, and Solr re-query when enabled.
- Subtype has target availability set to true.
- CiteAb widget behavior is enabled at subtype level.
- Product specifications must include secondary-relevant fields when values exist, including host/isotype, target, cross adsorption, conjugate, and antibody form.
- References count may come from CiteAb when available and positive.

### 10.3 Isotype Controls

Isotype Control pages must help users match control products by species, host/isotype, conjugate, format, and application.

Important implementation references:

- `ProductSubType.ANTIBODY_CONTROL`
- `ControlAntibodyProductDetailViewModel`
- `AntibodyProductDetailViewModel.isShowBio`
- `PdpAeoMarkdownBuilder.appendProductSpecifications`

Rules:

- Search supports spellcheck, filters, keep-my-filters, alternate search, and Solr re-query when enabled.
- Subtype has citation display and bioinformatics display enabled.
- Related products are enabled through the configured subtype list.
- Commerce rules follow the common antibody pricing/availability/add-to-cart model.

### 10.4 Proteins and Peptides

Proteins and Peptides pages must support protein-specific search and PDP behavior while reusing antibody product type infrastructure.

Important implementation references:

- `ProductSubType.ANTIBODY_PROTEIN`
- `ProteinAntibodyProductDetailViewModel`
- `ProductSubType.getBaseUrl`
- `ProductSubType.getSearchURL`
- `AntibodyProductDetailViewModel.getProductHomePageUrl`

Rules:

- Search uses `/proteins/` routes when new protein URL flags are enabled.
- Product specifications label species as `Species`, not `Species Reactivity`.
- Host and isotype must be omitted for protein subtype.
- Bioinformatics is enabled when content is present.
- Data sheet link must be skipped for `antibody_protein` subtype in the AEO link URL section.
- Related products are enabled through the configured related products subtype list.

### 10.5 ELISA Kits

ELISA pages use the immunoassay product type and must render kit-specific details, target information, product description, and commerce behavior.

Important implementation references:

- `ProductSubType.ELISA`
- `ElisaProductDetailViewModel`
- `PdpAeoMarkdownBuilder.appendElisaProductDetails`
- `PdpAeoMarkdownBuilder.appendElisaAboutThisKit`
- `PdpAeoMarkdownBuilder.appendElisaTargetInfo`

Rules:

- Search supports typeahead, spellcheck, filters, keep-my-filters, alternate search, and Solr re-query when enabled.
- ELISA TFP target URLs switch based on `elisaTFPEnabled`.
- PDP Product Details use immunoassay properties.
- About This Kit renders description and rigorous validation when present.
- Target Information renders target name, target list, and product description when present.
- ELISA bioinformatics renders gene aliases, gene ID, gene symbol, protein aliases, and UniProt when `isShowBio` is true.
- ELISA related products use ELISA-specific related product module configuration.

## 11. API and Integration Requirements

| Area | Config key or module | Endpoint or behavior |
| --- | --- | --- |
| Search count | `productSearchCountAPI` | `/api/magellan/product-service/getProductSearchCount?keyword=` |
| Catalog | `newCatalogAPI` | Catalog API base configured externally |
| Pricing | `newPricingApi` | `/api/magellan/pricing/` |
| Pricing products | `newPricingApiEnabledProducts` | `ANTIBODY;IMMUNOASSAY` |
| Availability | `newAvailabilityAPI` | `/api/store/sku/availability/` |
| Inventory data | `inventoryDataServiceUrl` | Inventory data service URL from config |
| Related SKU list | `relatedSkuListApiUrl` | `/api/magellan/related-products-service/v2/relatedProducts/antibody/sku` |
| Related product details | `fetchRelatedProductDetailsUrl` | `/api/magellan/product-service/fetchRelatedProductDetails` |
| Related products UI | `relatedProductsModuleURL` | `/api/magellan/related-products-ui/widget/` |
| ELISA related products UI | `elisaRelatedProductsModuleURL` | `/api/magellan/related-products-ui/widget/v2/` |
| Q and A service | `qAndAServiceApiUrl` | `/api/magellan/qanda-service/magellan/sku` |
| Q and A widget | `qnaWidgetAPI` | `/api/magellan/qanda-ui/qna/widget/` |
| AEO Q and A | `aeoQnaApiBaseUrl` | `/api/magellan/qanda-ui/qna` |
| Promotions availability | `promotionAvailabilityAPI` | `/api/store/coupons/eligiblePromos` |
| Promotions suggestions | `promoSuggestionApiPath` | `/api/store/promotions/engine/v1/suggestions` |
| Data sheet | `DATA_SHEET_PATH` | `/order/genome-database/dataSheetPdf` |
| PubMed references | `PUBMED_URL_PREFIX` | `http://www.ncbi.nlm.nih.gov/pubmed/` |
| RRID | `ANTIBODY_REGISTRY_URL_PREFIX` | `https://www.antibodyregistry.org/` |
| Panther | `PANTHER_PATH_SEGMENT` | `/panther/` path segment in generated URLs |

## 12. UI State and Error Handling

### 12.1 Search states

- Loading results
- Results found
- Results found with selected filters
- No exact match with filter preservation
- No results with alternate search links
- No results with no alternate links
- Spellcheck suggestion available
- Service error or timeout state

### 12.2 PDP states

- Product active and orderable
- Product active but price unavailable
- Product active but availability pending
- Product long-term unavailable
- Product discontinued
- Product replaced or package-specific lifecycle state
- Anonymous user requiring sign-in for price/availability
- Dealer or country-specific inventory display
- Related products unavailable
- Q and A disabled by country/subtype/config
- Bioinformatics absent or disabled
- References unavailable

### 12.3 Developer notes

- Empty values should be omitted from product details, specifications, bioinformatics, promotions, and ELISA sections.
- Client-side modules must not assume all services return data.
- Package selection must be treated as a primary PDP state driver.
- Feature flags and country/language context must be resolved before deciding whether to render optional modules.

## 13. Data and Analytics Requirements

The reviewed code exposes configuration and behavior but does not define a complete analytics event taxonomy. The following analytics requirements should be validated with the analytics owner before implementation.

| Area | Suggested event | Required dimensions |
| --- | --- | --- |
| Search | Search submitted | keyword, subtype, country, language, result count, filters |
| Search | Filter applied | subtype, filter group, filter value, result count |
| Search | Alternate search clicked | source subtype, target subtype, keyword, alternate count |
| Search | Product card clicked | subtype, product ID, SKU/webId, position, keyword |
| PDP | Package selected | product ID, previous SKU, selected SKU, subtype |
| PDP | Price displayed | product ID, SKU, currency, price availability, user login state |
| PDP | Availability displayed | product ID, SKU, availability status, quantity, country |
| PDP | Add to Cart clicked | product ID, SKU, quantity, orderability status |
| PDP | Related product clicked | source product ID, related product ID, widget version |
| PDP | Q and A interaction | product ID, action type, question ID where available |
| PDP | Reference clicked | product ID, reference source, URL/domain |

KPIs:

- Search success rate
- Search zero-result rate
- Filter usage rate
- Product card click-through rate
- PDP package selection rate
- Price availability rate
- Availability success rate
- Add-to-cart conversion rate
- Related product engagement
- Q and A engagement
- References and documentation engagement

## 14. Acceptance Criteria Summary

### 14.1 Search

- The five subtype search routes load the correct subtype and label.
- Configured result counts, spellcheck, typeahead, filters, and keep-my-filters behavior match subtype configuration.
- Result headers match blank keyword, wildcard keyword, normal keyword, and target/application contexts.
- Alternate search links display only when alternate subtype counts are available.
- Product cards and result counts do not show stale subtype data after navigation or filter changes.

### 14.2 PDP

- PDP route resolves correct product, SKU/webId, subtype, breadcrumb, and canonical URL.
- Product title/banner area reflects product and selected package lifecycle state.
- Commerce card updates price, availability, quantity, and cart eligibility when package changes.
- Product specifications omit empty fields and apply subtype-specific labels and omissions.
- Bioinformatics renders only when enabled and content exists.
- Target information renders subtype-appropriate target content and URLs.
- References follow CiteAb/product detail/view model fallback order.
- Q and A appears only when subtype, country, and global flags allow it.
- Related products appear only when subtype and global flags allow them.

## 15. Similarities Across Product Subtypes

- All five subtypes use subtype-driven route, label, feature, and search behavior.
- All five subtypes depend on product/package identity for PDP rendering.
- All five subtypes require defensive rendering of optional content.
- Commerce behavior is selected-package driven.
- Search experiences share keyword, filter, count, empty-state, and alternate-search patterns.
- PDP experiences share title/banner, package selection, commerce, specifications, related products, and support module patterns.
- Country, language, login, and feature flags influence UI rendering across the experience.

## 16. Differences Across Product Subtypes

| Area | Primary | Secondary | Isotype | Proteins and Peptides | ELISA |
| --- | --- | --- | --- | --- | --- |
| Product type | antibody | antibody | antibody | antibody | immunoassay |
| Search route | `/antibody/primary/` | `/antibody/secondary/` | `/antibody/control/` | `/proteins/` when enabled | `/elisa/` |
| Typeahead | Enabled | Not in new typeahead list | Not in new typeahead list | Enabled | Enabled |
| Spellcheck | Enabled | Enabled | Enabled | Not listed | Enabled |
| Bioinformatics | Enabled | Not shown as enabled in subtype enum evidence | Enabled | Enabled | Enabled through immunoassay view model |
| References | Citation display enabled | Citation display enabled | Citation display enabled | Scholarly article JSON-LD enabled by config | Protein schema JSON-LD enabled for ELISA |
| Product specs | Antibody-specific | Secondary-specific with target availability | Control-specific | Protein-specific, omits host/isotype | Immunoassay product details |
| Related products | Enabled | Enabled | Enabled | Enabled | ELISA-specific enabled path |
| Protocols link | Primary only | Not primary-only eligible | Not primary-only eligible | Data sheet link skipped in AEO | Not antibody protocol behavior |

## 17. Risks, Constraints, and Validation Items

| Item | Risk or constraint | Recommendation |
| --- | --- | --- |
| Repo access | Exact de-magellan team repo list was not fully available from the environment. | Confirm final repo ownership list with GitHub team admins. |
| Service ownership | PRD infers supporting services from config names and endpoints. | Confirm service owner and SLA for pricing, availability, related products, Q and A, and product service. |
| Availability config nuance | Config contains both enabled-country and not-enabled-country values that may look contradictory without runtime context. | Validate actual country gating logic before UI test signoff. |
| Analytics | Full event taxonomy was not present in reviewed evidence. | Align proposed analytics with enterprise analytics owner. |
| Banner rules | Local business rules identify lifecycle banner behavior, but exact UI component names were not visible in reviewed source. | Trace template/component implementation before development estimates. |
| Secondary bioinformatics | Subtype enum evidence did not show secondary bioinformatics enabled, while user requested bioinformatics coverage across pages. | Validate current production behavior for secondary PDP before adding UI assumptions. |
| Word TOC page numbers | Generated Word files can include a manual TOC; dynamic Word page numbers may need field update in Microsoft Word. | Use Word `Update Field` if a dynamic TOC is required. |

## 18. Operations and Support

### 18.1 Monitoring needs

- Search service success/failure rate by subtype.
- Product service response time and failure rate.
- Pricing API response time, timeout rate, and error-code distribution.
- Availability API response time and pending/no-data rate.
- Related products widget load success rate.
- Q and A widget load success rate.
- PDP package-switch errors.
- Client-side rendering errors by route/subtype.

### 18.2 Common support needs

- Customer cannot see price.
- Customer sees pending or unavailable inventory.
- Add to Cart disabled or unavailable.
- Package-specific lifecycle message differs from expected.
- Product specifications missing or unexpected.
- References count differs from known citation count.
- Related products not visible.
- Q and A not visible due to country/subtype/config.

### 18.3 Incident triage signals

- Confirm subtype and route.
- Confirm country, language, and login state.
- Confirm selected package SKU/webId.
- Confirm product lifecycle status.
- Check feature flags for pricing, availability, related products, Q and A, banner messages, and subtype-specific modules.
- Check upstream service status and response payloads.
- Compare PDP rendering with `PdpAeoMarkdownBuilder` output where applicable.

## 19. Developer Implementation Checklist

- Map each route to `ProductSubType` and verify display label.
- Verify search count, spellcheck, typeahead, filter, image search, antigen search, alternate search, and keep-my-filters flags by subtype.
- Implement or validate package-selection state as the driver for SKU, price, availability, data sheet, banner, and cart behavior.
- Render empty optional sections defensively.
- Validate RRID, UniProt, Entrez, PubMed, Panther, data sheet, protocols, and technical support links.
- Confirm Q and A country/subtype/global gating.
- Confirm related products subtype/global gating and widget version path.
- Add automated tests for at least route resolution, selected package commerce updates, bioinformatics visibility, references fallback, Q and A gating, and related products gating.

## 20. Appendix: Example Pages

| Subtype | Search example | PDP example |
| --- | --- | --- |
| Primary Antibody | `https://www.thermofisher.com/antibody/primary/query/*` | `https://www.thermofisher.com/antibody/product/Ki-67-Antibody-clone-SP6-Recombinant-Monoclonal/MA5-14520` |
| Secondary Antibody | `https://www.thermofisher.com/antibody/secondary/query/*` | `https://www.thermofisher.com/antibody/product/Goat-anti-Rabbit-IgG-H-L-Cross-Adsorbed-Secondary-Antibody-Polyclonal/A-11008` |
| Isotype Control | `https://www.thermofisher.com/antibody/control/query/*` | `https://www.thermofisher.com/antibody/product/Rabbit-IgG-Isotype-Control/02-6102` |
| Proteins and Peptides | `https://www.thermofisher.com/proteins/query/*` | `https://www.thermofisher.com/proteins/product/Human-FGF-basic-FGF-2-bFGF-154-aa-Recombinant-Protein/100-18B-50UG` |
| ELISA Kits | `https://www.thermofisher.com/elisa/query/*` | `https://www.thermofisher.com/elisa/product/Human-IL-18-ProQuantum-Immunoassay-Kit/A35613` |

