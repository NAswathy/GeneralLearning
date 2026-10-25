# Product Requirements Document

## Antibody Product Subtypes: Primary Antibody, Secondary Antibody, Proteins and Peptides, Isotype Controls, and ELISA Kits

| Field | Value |
|---|---|
| Product scope | Primary Antibody, Secondary Antibody, Proteins and Peptides, Isotype Controls, ELISA Kits |
| Prepared for | Business, Product, Commercial, Scientific Content, Support, Compliance, Analytics, and Digital Platform stakeholders |
| Source rules folder | `BusinessRules-Vedas-Search_PDP_NoTaqman.zip` |
| Template references | `Business_User_PRD_Genomics_Tools v2.docx`; `Functional PRD - Catalog Admin to Storefront: Products, Entitlements, Pricing, and Access.doc` |
| Repository reference requested | `https://github.com/orgs/thermofisher/teams/de-magellan/repositories` |
| Repository validation status | Pending. No accessible repositories were returned for the de-magellan team search in the current GitHub connector context. |
| Date | 2026-06-05 |
| Status | Draft PRD |

## 1. Product Overview

### Name

Antibody Product Subtypes Product Experience.

### Owner

Digital Product Owner / Product Management owner for Magellan Search and PDP experiences. Named business owner by product subtype to be confirmed.

### Purpose

The product experience helps customers and internal teams search for, evaluate, and purchase antibody-related products across Primary Antibody, Secondary Antibody, Proteins and Peptides, Isotype Controls, and ELISA Kits. The experience must preserve the correct product subtype, search route, result filters, product detail content, package selection, pricing, availability, Add to Cart behavior, documents, related products, Q&A behavior, and analytics context for each product family.

### Business Goals

- Make product discovery reliable across antibody-related search entry points.
- Keep product search results restricted to the selected product subtype.
- Present product details, specifications, images, references, documents, related products, and Q&A only when supported by available product data and enabled subtype rules.
- Ensure commerce actions are based on the selected package, selected SKU/web ID, orderability, lifecycle state, country eligibility, and pricing/availability response.
- Reduce customer confusion caused by stale result cards, missing filters, stale prices, incorrect package context, or unavailable product lifecycle states.
- Give business and support teams clear analytics and monitoring signals for search quality, PDP engagement, pricing/availability friction, related-product usage, and content gaps.

### Scope

In scope:

- Search entry, keyword handling, typeahead/suggestions, wildcard browse, result count, filters, sorting, badges, promotions, zero-result behavior, and product-card routing.
- PDP product identity, selected catalog/package behavior, title banners, lifecycle and replacement messaging, commerce card, price, availability, Add to Cart, data sheets, structured data, image gallery, references, Q&A, related products, technical support, and analytics.
- Functional architecture diagrams, data flow diagrams, API/integration capability summary, similarities, differences, workflows, acceptance criteria, KPIs, risks, operations, and support needs.

Out of scope:

- TaqMan assay search and PDP rules.
- New scientific assay-design logic.
- Replacement of search, pricing, availability, cart, catalog, document, image, related-product, Q&A, or analytics systems.
- Manual correction of source catalog data outside approved product-data governance.
- New product claims or diagnostic-use claims.

## 2. Users and Stakeholders

### Personas

| Persona | User Need | Success Outcome |
|---|---|---|
| Research customer | Find products by target, species, host, class, conjugate, application, kit format, protein name, expression system, or sample type. | Can select a suitable product and continue to PDP, price/availability, or cart. |
| Sales / Commercial user | Recommend appropriate products and explain price, availability, lifecycle, and alternatives. | Can identify product fit and customer next steps without manual lookup. |
| Field Application Scientist | Validate scientific fit for applications, targets, controls, kit types, and protein/peptide needs. | Can review specifications, references, documents, Bioinformatics, Target Information, and related products where available. |
| Customer Support | Resolve search, PDP, price, availability, discontinued/replacement, document, Q&A, and related-product questions. | Can reproduce behavior using product subtype, route, SKU, package, user context, and enabled configuration. |
| Product Manager | Monitor adoption, content completeness, conversion, and product-family gaps. | Can identify zero-result terms, missing filters, missing content, lifecycle issues, and commerce friction. |
| Scientific Content Owner | Maintain specifications, references, product descriptions, documents, images, target data, and kit/protein attributes. | Product content appears accurately and empty values are not shown as real content. |
| Compliance / Legal | Review research-use, diagnostic-use, resale, lifecycle, and claim-sensitive messaging. | Required notices and restrictions are consistently displayed. |
| Engineering / QA | Build and test shared and subtype-specific behavior. | Has clear acceptance criteria by product family. |
| Analytics / Operations | Monitor service health, product engagement, and error patterns. | Can report by product subtype, SKU/catalog, country, login state, and module. |

### Decision Makers

- Product owner for antibody search and PDP.
- Business owners for Primary Antibody, Secondary Antibody, Proteins and Peptides, Isotype Controls, and ELISA Kits.
- eCommerce product owner.
- Search/PDP platform owner.
- Commercial operations leadership.
- Customer support leadership.
- Compliance and legal stakeholders.
- Analytics and data governance owner.

## 3. Architecture

### Tech Stack and Functional Components

The rules documents do not name every implementation technology. The PRD therefore describes the functional components evidenced by the rules rather than assuming missing repository details.

| Component | Functional Role From Rules |
|---|---|
| Product-family search entry | Routes the user to the correct family-specific search page and subtype context. |
| Search result service / search response | Returns matching product records, result counts, result cards, filters, selected filters, zero-result behavior, and sort behavior. |
| Typeahead / suggestion capability | Provides product-area suggestions when configured for the subtype. |
| Solr re-query behavior | Applies only when the relevant subtype is included in the enabled-subtype configuration. |
| Keep-my-filters behavior | Preserves selected filters only when enabled for the relevant subtype. |
| Metadata handler | Applies to ELISA and Proteins and Peptides only when the subtype is enabled. |
| Product detail page shell | Renders title, selected catalog number, product URL route, breadcrumbs/category paths, citation text, and subtype-specific modules. |
| Commerce card | Uses selected package details to determine catalog number, package size, web ID/SKU, orderability, entitlement, price state, lifecycle state, lead time, parent SKU status, and Add to Cart behavior. |
| Pricing API | Called only for eligible products and eligible countries; responses populate price, user price, currency, and visibility; missing/failing data must not leave stale prices visible. |
| Availability lookup | Displays availability and estimates only when enabled and relevant to the selected package/SKU and user context. |
| Add to Cart integration | Submits selected SKU/web ID, quantity, and product identity only when the selected product is orderable and not lifecycle-blocked. |
| Data sheet / document capability | Refreshes document context when selected package changes. |
| Image gallery and structured data | Uses product images or no-image/default placeholders and omits invalid structured offers. |
| Related products capability | Applies only when enabled for the subtype and product data supports related products. |
| Q&A capability | Applies only when Q&A is enabled for the subtype and must fail safely. |
| Analytics | Receives subtype-specific context for search, PDP, commerce, content, related products, Q&A, and errors. |

### Shared Functional Architecture

```mermaid
flowchart LR
    A[User Search or PDP Entry] --> B[Product Family Route]
    B --> C[Subtype Context]
    C --> D[Search Results or PDP Shell]
    D --> E[Filters, Results, Zero Result State]
    D --> F[Product Details and Content Sections]
    F --> G[Commerce Card]
    G --> H[Pricing, Availability, Cart]
    F --> I[Documents, Images, References, Q&A, Related Products]
    D --> J[Analytics and Monitoring]
```

### Shared Data Flow

```mermaid
flowchart LR
    A[Keyword / Product URL / Selected Package] --> B[Subtype and Route Context]
    B --> C[Search or Product Data]
    C --> D[Product Records and Package Details]
    D --> E[Displayed Results or PDP]
    E --> F[Pricing and Availability Decisions]
    F --> G[Purchase Action or Alternate Message]
    E --> H[Content Modules]
    H --> I[Documents, Images, References, Q&A, Related Products]
    E --> J[Business Events]
```

### Primary Antibody Functional Architecture

```mermaid
flowchart LR
    A[Primary Antibody Search] --> B[Primary Antibody Product Set]
    B --> C[Primary Result Cards]
    C --> D[Primary Antibody PDP]
    D --> E[Package, Price, Availability, Add to Cart]
    D --> F[Specifications, Images, Bioinformatics, Target Information]
    D --> G[References and Q&A]
    D --> H[Secondary, Isotype, Alternative, ELISA, Matched Pair Related Products]
```

### Primary Antibody Data Flow

```mermaid
flowchart LR
    A[Keyword or PDP URL] --> B[Primary Antibody Subtype]
    B --> C[Matching Primary Records]
    C --> D[Product Card or PDP]
    D --> E[Selected Package SKU]
    E --> F[Price / Availability / Banner / Data Sheet Refresh]
    D --> G[Bioinformatics, Target, References, Related Products, Q&A]
    F --> H[User Action: Check Price, View Availability, Add to Cart, Contact Support]
```

### Secondary Antibody Functional Architecture

```mermaid
flowchart LR
    A[Secondary Antibody Search] --> B[Secondary Antibody Subtype]
    B --> C[Secondary Result Cards]
    C --> D[Secondary Antibody PDP]
    D --> E[Package, Price, Availability, Add to Cart]
    D --> F[Specifications, Images, References, Data Sheets]
    D --> G[Q&A when Enabled]
    D --> H[Related Products when Enabled]
```

### Secondary Antibody Data Flow

```mermaid
flowchart LR
    A[Keyword or PDP URL] --> B[Secondary Antibody Context]
    B --> C[Matching Secondary Records]
    C --> D[Result Card or PDP]
    D --> E[Selected Package SKU]
    E --> F[Price / Availability / Banner / Data Sheet Refresh]
    D --> G[Documents, References, Q&A, Related Products]
    F --> H[User Action: Add to Cart or Alternate Purchase Path]
```

### Proteins and Peptides Functional Architecture

```mermaid
flowchart LR
    A[Proteins and Peptides Search] --> B[ANTIBODY_PROTEIN Context]
    B --> C[Protein / Peptide Result Cards]
    C --> D[Proteins PDP]
    D --> E[Package, Price, Availability, Add to Cart]
    D --> F[Specifications, Documents, References, Images]
    D --> G[Structured Product Data and Optional Scholarly Article Data]
    D --> H[Related Products / Support Paths]
```

### Proteins and Peptides Data Flow

```mermaid
flowchart LR
    A[Keyword or /proteins/product URL] --> B[Protein Subtype Context]
    B --> C[Protein / Peptide Records]
    C --> D[Search Result or PDP]
    D --> E[Selected Package]
    E --> F[Price, Availability, Data Sheet, Banner]
    D --> G[Specifications, Documents, References, Structured Data]
    F --> H[Commerce Action or Alternate Path]
```

### Isotype Controls Functional Architecture

```mermaid
flowchart LR
    A[Isotype Controls Search] --> B[ANTIBODY_CONTROL Context]
    B --> C[Isotype Control Result Cards]
    C --> D[Isotype Control PDP]
    D --> E[Package, Price, Availability, Add to Cart]
    D --> F[Specifications, Images, Data Sheets]
    D --> G[Q&A and Technical Support Context]
    D --> H[Related Products]
```

### Isotype Controls Data Flow

```mermaid
flowchart LR
    A[Keyword or Control PDP URL] --> B[Isotype Control Subtype]
    B --> C[Antibody Control Records]
    C --> D[Search Result or PDP]
    D --> E[Selected Package]
    E --> F[Price, Availability, Data Sheet, Banner]
    D --> G[Q&A, Related Products, Technical Support]
    F --> H[Add to Cart or Alternate Message]
```

### ELISA Kits Functional Architecture

```mermaid
flowchart LR
    A[ELISA Kits Search] --> B[ELISA Subtype]
    B --> C[ELISA Kit Result Cards]
    C --> D[ELISA PDP]
    D --> E[Package, Price, Availability, Add to Cart]
    D --> F[Specifications, Documents, References, Images]
    D --> G[Related Products]
    D --> H[Structured Data and Citation]
```

### ELISA Kits Data Flow

```mermaid
flowchart LR
    A[Keyword or /elisa/product URL] --> B[ELISA Product Context]
    B --> C[ELISA Kit Records]
    C --> D[Search Result or PDP]
    D --> E[Selected Package]
    E --> F[Price, Availability, Data Sheet, Banner]
    D --> G[Documents, References, Related Products, Structured Data]
    F --> H[Commerce Action or Alternate Path]
```

### Dependencies

- Product subtype classification and route configuration.
- Search index and search-result data quality.
- Typeahead and suggestion configuration.
- Solr re-query and keep-my-filters subtype configuration.
- Package-level catalog, SKU/web ID, entitlement, orderability, lifecycle, lead-time, and parent-SKU data.
- Pricing API eligibility, batching configuration, country eligibility, and response quality.
- Availability eligibility by country, SKU, quantity, login state, and dealer context where applicable.
- Data sheet and document availability by selected package.
- Product images and default/no-image placeholder configuration.
- Related-product enablement and source data.
- Q&A enablement and keyword/filter data.
- Analytics event capture by product subtype and user action.

## 4. APIs and Integration Capabilities

The rules documents identify capabilities and routes, but they do not provide complete API endpoint contracts for every module. The table below therefore lists only evidenced or directly required API/integration capabilities.

| Capability | Applies To | Business Requirement |
|---|---|---|
| Product-family query routes | All search families | Keyword searches must route to the product-family path: `/antibody/primary/query/{keyword}`, secondary antibody query path, `/proteins/query/{keyword}`, `/antibody/control/query/{keyword}`, and `/elisa/query/{keyword}`. |
| Product PDP routes | Proteins and Peptides, ELISA, antibody PDP families | Product cards must route to their family PDP routes, including `/proteins/product/...` and `/elisa/product/...`; antibody PDP routes must retain correct subtype context. |
| Typeahead URL / suggestions | Primary, Secondary legacy, Proteins and Peptides, ELISA; not Isotype unless configured | Typeahead must pass the correct subtype where configured; Isotype Controls must not call a product-area-specific typeahead endpoint when no typeahead URL is configured. |
| Search/filter response | All search families | Search responses must return subtype-restricted results, result counts, current filter facets, selected filters, and zero-result states without stale product cards. |
| Solr re-query behavior | Enabled subtypes only | Re-query behavior must apply only when the subtype appears in the enabled-subtype configuration. |
| Pricing API | PDP commerce families | Pricing lookup must call the configured pricing API only for eligible products and countries, must respect SKU batch limits, and must clear stale prices on failure or missing data. |
| Availability lookup | PDP commerce families | Availability must be shown only when availability is enabled for the current context and selected package/SKU is eligible. |
| Add to Cart integration | PDP commerce families | Add to Cart must submit only when the selected SKU is orderable and not long-term unavailable or discontinued. |
| Data sheet / document retrieval | PDP commerce families | Data sheet or document context must refresh when selected catalog package changes. |
| Image gallery / structured data | PDP families | Structured data must use available image or configured default/no-image placeholder and must omit invalid offer data. |
| Related products | Primary, Secondary when enabled, Isotype, Proteins/Peptides, ELISA | Related-product modules must receive the correct subtype and render only when related-product data is available and enabled. |
| Q&A | Primary, Secondary when enabled, Isotype | Q&A must use subtype-specific enablement and fail safely with zero/empty results when unavailable. |
| Analytics | All families | Analytics context must receive the correct product subtype and business action state. |

## 5. Similarities Across Product Subtypes

| Similarity | Applies To | Requirement |
|---|---|---|
| Product subtype drives behavior | All | Search, PDP modules, commerce, documents, image gallery, related products, Q&A, technical support, and analytics must receive the correct subtype context. |
| Search result restriction | All search families | Results must be limited to the selected product family/subtype. |
| Keyword limit | All search families with explicit rule | Keyword input must honor the configured 250-character limit. |
| Wildcard browse | ELISA, Isotype, Proteins and Peptides, and antibody search defaults | `*` behaves as a browse request/default keyword, not as a literal catalog-number search. |
| Current-result filters | All search families | Filters must come from the current result set, counts must update, and selected filters must be removable. |
| Zero-result safety | Search families | Zero-result handling must show the configured message and must not show stale cards from previous searches. |
| Package-based commerce | PDP families | The selected package drives catalog number, package size, web ID/SKU, price, availability, data sheet, and banner context. |
| Lifecycle gating | PDP families | Long-term unavailable and discontinued products must not expose the normal purchase path. |
| Pricing fallback | PDP families | Pricing failures or missing prices must show configured fallback messaging and must not leave stale prices visible. |
| Quantity validation | PDP families | Invalid quantities must trigger validation messaging and must not be submitted. |
| Structured offer omission | PDP families | Offer data must be omitted when the product is discontinued, long-term unavailable, not orderable, missing final price, or missing availability. |
| Analytics context | All | Search, PDP, commerce, related-products, Q&A, and content actions must be reported with product subtype context. |

## 6. Differences Across Product Subtypes

| Area | Primary Antibody | Secondary Antibody | Proteins and Peptides | Isotype Controls | ELISA Kits |
|---|---|---|---|---|---|
| Search entry | Antibody search using primary target type | Antibody search using secondary target type | Popular Product Area: Proteins and Peptides | Popular Product Area: Isotype Controls | Popular Product Area: ELISA Kits |
| Route | Primary antibody query page for keyword | Secondary antibody query path | `/proteins/query/{keyword}` | `/antibody/control/query/{keyword}` | `/elisa/query/{keyword}` |
| Result page size | 50 in QA/default rules | 50 | 100 | 50 | 50 |
| Typeahead | Limited to antibody products and primary filter; max 15 suggestions | Legacy typeahead filters to antibody products and secondary filter; max 15 suggestions | Uses configured Proteins and Peptides typeahead URL and PRANT-filtered suggestion source | No product-area-specific typeahead unless configured | Uses configured ELISA typeahead URL and passes ELISA subtype |
| Core filters | Configured primary antibody filters, including New when enabled | Configured secondary antibody filters | Protein Name, Species, Expression System, Product Type, Application, Product Grade, Tag, New, Activity, Promotion | Host, Clonality/Class, Conjugate, Application, Format, Target Class, Recombinant | Protein Target, Species, Kit Format, Research Area, Sample Type, Instrument, High Sensitivity, New |
| PDP route | Antibody product PDP with primary subtype | Antibody product PDP with secondary subtype | `/proteins/product/...` | Antibody product PDP with antibody_control subtype | `/elisa/product/...` |
| Special content | Bioinformatics, Target Information, References, Q&A, related product matching rules | Alexa Fluor Plus package banner example; Q&A/related products only when enabled | Protein category/subtype, optional scholarly article structured data | Isotype Control category, Q&A/technical support context | ELISA Kits category, immunoassay product type, documents/references/related products |
| Sample package examples from rules | Package options vary by product | A32723TR and A32723 | 10 ug, 50 ug, 100 ug, 250 ug, 500 ug, 1 mg | 50 µg, 100 µg, 500 µg | 96 Tests and 5 x 96 Tests |

## 7. Core Features and Requirements

### Shared Search Workflow

| ID | Requirement | Acceptance Criteria |
|---|---|---|
| SRCH-001 | User must enter or select a keyword for product-family search, except where wildcard browse/default keyword is used. | Search submits only when allowed by that family’s search rules and routes to the correct product-family query page. |
| SRCH-002 | Search must use the selected product subtype context. | Results, filters, Q&A enablement, related-products behavior, commerce calls, metadata, and analytics do not use another subtype. |
| SRCH-003 | Search results must be restricted to the selected product family. | Primary returns only primary antibodies; secondary returns only secondary antibodies; Proteins and Peptides returns only protein/peptide products; Isotype returns only antibody control products; ELISA returns only ELISA kit products. |
| SRCH-004 | Filters must reflect current results. | Facet counts update after filters are applied or removed, and selected filters are visible and removable. |
| SRCH-005 | Zero-result behavior must be safe. | Configured zero-result messaging appears and stale product cards from prior searches are not displayed. |
| SRCH-006 | Sort-by-price must be region-controlled. | Sort by price is available only in configured countries. |
| SRCH-007 | Promotional ads must be subtype-controlled. | Promotional ads appear only when enabled for the product subtype. |

### Product-Family Search Requirements

| Product Family | Requirements |
|---|---|
| Primary Antibody | Search uses the primary antibody target type; typeahead is limited to antibody products and primary filter; typeahead returns no more than 15 suggestions; duplicate suggestions are shown once; trademark marker is removed before search; default sort is Relevance; default keyword is wildcard; result count is 50 in QA/default rules; newer filters and newer typeahead apply only when primary antibody is enabled in the relevant subtype list. |
| Secondary Antibody | Search uses secondary antibody target type and secondary query path; legacy typeahead filters to antibody products and secondary filter; typeahead returns no more than 15 suggestions; suggested searches include Qdot 585, Alexa Fluor 594, and HRP; default sort is Relevance; result count is 50; newer filters apply only when enabled; newer typeahead is not enabled unless the subtype is configured. |
| Proteins and Peptides | Search entry is Proteins and Peptides; route is `/proteins/query/{keyword}`; page size is 100; wildcard is browse; typeahead uses configured protein/peptide suggestion source; new typeahead and spell-check do not apply unless `ANTIBODY_PROTEIN` is configured; filters may include Protein Name, Species, Expression System, Product Type, Application, Product Grade, Tag, New, Activity, and Promotion. |
| Isotype Controls | Search entry is Isotype Controls; route is `/antibody/control/query/{keyword}`; page size is 50; wildcard is browse; product-area-specific typeahead must not be called when no typeahead URL is configured; filters may include Host, Clonality/Class, Conjugate, Application, Format, Target Class, Recombinant; conjugate filters group child conjugates under configured parent families when those families have results. |
| ELISA Kits | Search entry is ELISA Kits; route is `/elisa/query/{keyword}`; page size is 50; wildcard is browse; typeahead passes ELISA subtype; new typeahead and spell-check may apply because ELISA is enabled; filters may include Protein Target, Species, Kit Format, Research Area, Sample Type, Instrument, High Sensitivity, and New. |

### Shared PDP and Commerce Workflow

| ID | Requirement | Acceptance Criteria |
|---|---|---|
| PDP-001 | PDP must render product title from display name and selected catalog number from selected package. | Product title and selected catalog number update from product/package data. |
| PDP-002 | PDP modules must receive the correct subtype. | Commerce, data sheets, image gallery, references, related products, documents, structured data, Q&A, technical support, and analytics use family-specific subtype context. |
| PDP-003 | Multi-package products must allow package selection. | Selected package updates product size, SKU/web ID, pricing, availability, data-sheet link, and banner context. |
| PDP-004 | Product title banner must evaluate lifecycle and product-specific message states. | Long-term unavailable, discontinued, replacement, and product/package banner messages display when conditions exist. |
| PDP-005 | Closing a dismissible banner must not change orderability. | Banner visibility changes only; product lifecycle, orderability, and purchase behavior remain unchanged. |
| PDP-006 | Pricing must be package-based. | Valid pricing populates price, user price, currency, and visibility for the selected package. |
| PDP-007 | Pricing failures must clear stale price. | Fallback price prompt or unavailable-price message appears and old prices are not retained. |
| PDP-008 | Normal Add to Cart must be lifecycle- and orderability-gated. | Add to Cart appears only when selected SKU is orderable and not long-term unavailable or discontinued. |
| PDP-009 | Supplier/dealer commerce paths must replace normal Add to Cart when applicable. | Learn Where to Buy or dealer-specific path is shown instead of normal Add to Cart. |
| PDP-010 | Structured offer data must be omitted when invalid. | Discontinued, long-term unavailable, not orderable, missing final price, or missing availability states suppress offer data. |

### Product-Family PDP Requirements

| Product Family | Requirements |
|---|---|
| Primary Antibody | Product records are primary antibody records with search status 1; package banners update when package changes; pricing can remove child package SKUs with specific pricing error messages while retaining parent SKU for rendering; Add to Cart quantity is constrained from 1 to 9,999; Aspire link applies only when antibody type/subtype and US/Canada country rules match; Bioinformatics, Target Information, References, Related Products, and Q&A have family-specific display and matching rules. |
| Secondary Antibody | Product records load as secondary antibody records only when the source row type is Secondary Antibody; generated product documents and data sheets use secondary antibody subtype; Q&A applies only when secondary subtype is enabled; related products apply only when secondary subtype is enabled; secondary example package banner promotes Alexa Fluor Plus and provides a Learn more link. |
| Proteins and Peptides | PDP identifies product category as Protein, product subtype as Protein, and downstream subtype as `antibody_protein`; PDP route uses `/proteins/product/...`; product-level scholarly article structured data may be generated when enabled for `ANTIBODY_PROTEIN`; sample package options include 10 ug, 50 ug, 100 ug, 250 ug, 500 ug, and 1 mg. |
| Isotype Controls | PDP identifies product as antibody product subtype `antibody_control` / Isotype Control; breadcrumbs keep product in Isotype Controls category when data is available; citation includes RRID when available; sample package options are 50 µg, 100 µg, and 500 µg. |
| ELISA Kits | PDP identifies product category as ELISA, product type as immunoassay, and subtype as ELISA; route uses `/elisa/product/...`; breadcrumbs keep product in ELISA Kits category when available; sample package options are 96 Tests and 5 x 96 Tests; sample product displays a product-specific banner promoting another ProQuantum immunoassay kit. |

### Scientific Content and Related Modules

| ID | Requirement | Acceptance Criteria |
|---|---|---|
| CNT-001 | Specifications must display only when values exist. | Empty specification values are not presented as real product content. |
| CNT-002 | Product images must use configured fallback behavior. | Structured data and PDP image modules use product images where available and configured default/no-image placeholders where permitted. |
| CNT-003 | References must load and sort when present. | Reference cards and publication tables follow product-family rules for display, sorting, and expand/collapse behavior. |
| CNT-004 | Bioinformatics and Target Information must appear only when visible content exists. | Section navigation includes these sections only when data is visible. |
| CNT-005 | Q&A must fail safely. | Q&A failures return zero counts or empty result sets rather than breaking PDP. |
| CNT-006 | Related products must follow subtype enablement and matching rules. | Related products display only when enabled and when related data exists for the selected product/subtype. |

## 8. Data and Analytics

### KPIs

| KPI | Definition | Business Use |
|---|---|---|
| Search volume by product family | Searches by Primary, Secondary, Proteins and Peptides, Isotype Controls, and ELISA Kits. | Understand demand by portfolio. |
| Search-to-result rate | Percentage of searches returning at least one product. | Measure search and catalog coverage quality. |
| Zero-result rate | Percentage of searches returning no products. | Identify synonym gaps, product gaps, or misrouted searches. |
| Filter usage | Filter applies/removes by family and facet. | Understand how users narrow product choices. |
| Product card click-through | Result clicks to PDP. | Measure product discovery effectiveness. |
| PDP engagement | Views of specifications, references, Bioinformatics, Target Information, documents, Q&A, and related products. | Identify content value and content gaps. |
| Package-change rate | Package selector changes by product family. | Identify where package choice affects decision-making. |
| Price visibility rate | Valid price, user price, fallback prompt, or unavailable-price states. | Track commerce friction. |
| Availability engagement | Availability checks, stock states, estimates, and pending estimate display. | Track purchase confidence and stock concerns. |
| Add-to-cart rate | Orderable PDP sessions that add selected SKU to cart. | Measure conversion. |
| Related-product click-through | Impressions and clicks for related-product modules. | Measure recommendation usefulness. |
| Q&A usage | Q&A counts, searches, filters, result clicks, and empty/error states. | Measure support self-service value. |
| Error rate by module | Search, typeahead, pricing, availability, cart, documents, images, related products, Q&A. | Prioritize operational fixes. |

### Reporting Events

- Product family selected.
- Keyword searched.
- Wildcard browse submitted.
- Typeahead suggestion shown and selected.
- Search results loaded.
- Zero-result message shown.
- Filter applied and removed.
- Sort changed.
- Product card clicked.
- PDP opened.
- Package changed.
- Product banner shown, closed, or replacement clicked.
- Price lookup succeeded, failed, or returned unavailable state.
- Check price or check price/availability clicked.
- Availability requested and shown.
- Quantity changed and invalid quantity message shown.
- Add to Cart clicked, succeeded, or failed.
- Supplier/dealer purchase path clicked.
- Data sheet or document opened.
- Image gallery opened.
- Specifications viewed.
- Bioinformatics viewed.
- Target Information expanded or collapsed.
- References loaded, sorted, expanded, or collapsed.
- Related product shown and clicked.
- Q&A count loaded, search performed, filter applied, result opened, or error state returned.

### Reporting Dimensions

Product family, product subtype, keyword, route, selected filters, sort option, result count, catalog number, selected SKU/web ID, selected package size, lifecycle state, price state, availability state, country, login state, product target, host, class/isotype, conjugate, application, kit format, expression system, sample type, Q&A state, related-product type, and cart outcome.

## 9. Risks and Constraints

| Risk / Constraint | Impact | Mitigation |
|---|---|---|
| Repository validation is unavailable in the current environment. | PRD cannot be source-confirmed against the de-magellan repositories. | Restore GitHub access and map each PRD requirement to source files/services before final sign-off. |
| Product subtype mapping drifts across modules. | Wrong filters, routes, Q&A, related products, commerce behavior, or analytics may appear. | Maintain subtype mapping tests and product-owner review. |
| Search index or product data is stale. | Results, counts, filters, and product cards may be incorrect. | Monitor index freshness and result-count anomalies. |
| Typeahead enablement differs by subtype. | Users may expect suggestions where product-area typeahead is not enabled. | Make subtype typeahead behavior explicit in support documentation. |
| Pricing API returns missing or failing data. | Users may see fallback prompts or cannot confidently purchase. | Track pricing failures and clear stale price values. |
| Availability rules depend on country, SKU, login, and configuration. | Support teams may not reproduce customer availability states. | Capture country, login state, selected SKU, and availability response in support diagnostics. |
| Package changes fail to refresh dependent context. | Price, availability, banner, or data sheet may refer to the wrong SKU. | Add regression tests for package-change refresh. |
| Related-product matching data is incomplete. | Recommendations may be missing or weak. | Review related-product quality by subtype and track click-through. |
| Q&A enablement differs by subtype. | Users may see Q&A for some product families and not others. | Document Q&A-enabled subtype rules and monitor empty/error states. |
| Compliance-sensitive messages are missing or stale. | Research-use, diagnostic-use, resale, discontinued, or replacement messaging risk. | Include compliance review in release readiness. |

## 10. Operations and Support

### Monitoring

- Search latency and error rate by product family.
- Typeahead/suggestion latency and error rate by product family.
- Result-count anomalies and zero-result spikes.
- Filter/facet failures and selected-filter state errors.
- PDP load success and section visibility by subtype.
- Pricing API success, failure, fallback, and batch-limit behavior.
- Availability lookup success, estimate/pending states, and region-specific behavior.
- Add to Cart success and failure by SKU/web ID and product family.
- Package-change refresh failures.
- Banner display frequency by lifecycle state.
- Document/data sheet link failures.
- Image/default image failures.
- Related-product empty/error response rate and click-through.
- Q&A count/search failure and empty-result rates.
- Analytics event completeness by product subtype.

### Incident Scenarios

| Incident | Business Impact | Support Response |
|---|---|---|
| Search route returns wrong product family. | User may evaluate incorrect products. | Validate route, subtype context, and selected search entry. |
| Filters disappear or counts are wrong. | User cannot narrow results confidently. | Check current result set, enabled filter configuration, and re-query behavior. |
| Price is missing or stale. | User cannot assess purchase cost. | Check eligibility, country, selected SKU, pricing response, and fallback state. |
| Add to Cart is not available. | User cannot purchase. | Check orderability, lifecycle state, quantity, selected SKU, pricing action, and supplier/dealer path. |
| Availability shows Pending or missing. | User cannot assess delivery timing. | Check availability eligibility, selected SKU, quantity, country, and estimate state. |
| Related products are missing. | User may miss required controls, kits, or alternatives. | Check subtype enablement and related-product data. |
| Q&A is empty or unavailable. | User may require support escalation. | Check Q&A enablement, SKU match, keyword filters, and service status. |
| Product banner conflicts with purchase action. | User may misunderstand availability or replacement status. | Check selected package lifecycle and banner source. |

### Common Support Needs

- Explain which search entry to use for each product family.
- Explain why typeahead exists for some families and not others.
- Explain why a product appears or does not appear in a filtered result set.
- Explain wildcard browse behavior.
- Confirm selected SKU/web ID and package size.
- Explain price prompt, no-price, View price in cart, Contact Us, Learn Where to Buy, or dealer-specific paths.
- Confirm product lifecycle state and replacement messaging.
- Confirm why related products or Q&A appear or do not appear.
- Help users refine searches when zero results appear.

## 11. Acceptance Criteria

| ID | Scenario | Expected Result |
|---|---|---|
| AC-001 | Submit a keyword search for each family. | Search routes to the correct product-family page and returns only that family’s products. |
| AC-002 | Submit `*` for ELISA, Isotype Controls, and Proteins and Peptides. | Wildcard browse returns product-family coverage rather than treating `*` as a literal catalog number. |
| AC-003 | Use typeahead where configured. | Suggestions are subtype-appropriate; duplicate suggestions are shown once where specified. |
| AC-004 | Apply and remove filters. | Filter counts, selected filters, and result counts update to match the current result set. |
| AC-005 | Search with no matching products. | Zero-result message appears and prior product cards are not shown. |
| AC-006 | Open a multi-package PDP. | Package selector appears and package change refreshes SKU/web ID, price, availability, data sheet, and banner context. |
| AC-007 | Open a long-term unavailable product. | Normal Add to Cart is not shown and configured alternate/contact behavior appears. |
| AC-008 | Open a discontinued product. | Normal Add to Cart is not shown and discontinued messaging appears. |
| AC-009 | Pricing fails or returns missing data. | Stale prices are cleared and fallback prompt/unavailable message appears. |
| AC-010 | Enter invalid quantity. | Validation message appears and invalid quantity is not submitted. |
| AC-011 | Open a primary antibody with Bioinformatics. | Protein aliases, gene aliases, UniProt ID, Entrez Gene ID, Function(s), and Process(es) appear when data exists. |
| AC-012 | Open References on a primary antibody with references. | Reference cards load and sorting/expand-collapse behavior works according to rules. |
| AC-013 | Open Q&A where enabled. | Q&A count and result behavior follow subtype rules; failures return safe zero/empty states. |
| AC-014 | Open related products where enabled and data exists. | Related products display only for eligible subtype/data combinations. |
| AC-015 | Open ELISA PDP. | Product category is ELISA, product type is immunoassay, route is `/elisa/product/...`, and selected package drives commerce behavior. |
| AC-016 | Open Proteins and Peptides PDP. | Product category/subtype is Protein, route is `/proteins/product/...`, and selected package drives commerce behavior. |

## 12. Release Readiness Checklist

| Area | Readiness Requirement |
|---|---|
| Repository traceability | Restore GitHub access and map requirements to de-magellan source repositories. |
| Rule coverage | Confirm every source rule document in the NoTaqMan ZIP is represented. |
| Search routing | Validate Primary, Secondary, Proteins and Peptides, Isotype Controls, and ELISA routes. |
| Search filters | Product-owner sign-off on filter labels, order, counts, empty/disabled filters, and selected-filter behavior. |
| Typeahead | Validate enabled and disabled subtype behavior. |
| PDP identity | Validate product type, subtype, title, catalog number, route, breadcrumb/category, and citation. |
| Commerce | Validate selected package, SKU/web ID, pricing, availability, quantity, Add to Cart, and alternate purchase paths. |
| Lifecycle banners | Validate long-term unavailable, discontinued, replacement, and product-specific banner behavior. |
| Structured data | Validate non-empty specifications, images/default images, and offer omission rules. |
| Content modules | Validate documents, images, references, Bioinformatics, Target Information, related products, and Q&A where applicable. |
| Analytics | Validate required reporting events and dimensions end to end. |
| Operations | Confirm dashboards and alerts by product family and module. |
| Support | Publish support playbook for routing, search, pricing, availability, lifecycle, Q&A, and related-products issues. |
| Compliance | Review research-use, diagnostic-use, resale, lifecycle, and product-specific banner messaging. |

## 13. Open Questions

- Who is the named business owner for each product family?
- Which exact repositories are authoritative for search UI, PDP UI, product data, pricing, availability, cart, Q&A, related products, documents, images, and analytics?
- Should this PRD remain a single parent PRD, or should each product family have a child PRD?
- Which product families should support compare, export, or email in future scope?
- What are the target SLAs for search, typeahead, pricing, availability, documents, related products, and Q&A?
- What analytics platform is the source of truth for reporting events?
- Should support users have a diagnostic view showing subtype, route, selected SKU/web ID, package size, country, login state, price action, availability result, Q&A enablement, and related-product state?

## 14. Source Rule Documents Used

| Rule Document From ZIP | Scope Used |
|---|---|
| `Primary_Antibody_Search_Business_Rules_Copy.docx` | Primary antibody search, typeahead, default searches, filters, sort, wildcard/default behavior, result count, and search constraints. |
| `Primary_Antibody_Product_Series_Business_Rules.docx` | Primary antibody PDP, commerce, price, availability, specifications, images, Bioinformatics, Target Information, References, Related Products, and Q&A. |
| `Secondary_Antibody_Search_Business_Rules.docx` | Secondary antibody search, legacy typeahead, result limits, filters, sort, and subtype enablement. |
| `Secondary_Antibody_Product_Series_Business_Rules.docx` | Secondary antibody PDP, classification, banners, commerce, price, availability, Q&A enablement, related-products enablement, and documents/data sheets. |
| `Proteins_Peptides_Search_Business_Rules.docx` | Proteins and Peptides search entry, route, page size, typeahead, filters, metadata, image search exclusion, sort, and promotions. |
| `Proteins_Peptides_Product_Series_Business_Rules.docx` | Protein/peptide PDP identity, route, commerce, package examples, structured data, documents, references, and scholarly article structured data. |
| `Isotype_Controls_Search_Business_Rules.docx` | Isotype Controls search entry, route, page size, typeahead constraints, filters, conjugate grouping, selected filters, zero-result handling, sort, badges, and promotions. |
| `Isotype_Controls_Product_Series_Business_Rules.docx` | Isotype Control PDP identity, commerce, packages, structured data, banner behavior, Q&A, related products, technical support, and analytics. |
| `ELISA_Search_Business_Rules.docx` | ELISA search entry, route, page size, typeahead, filters, metadata, image search exclusion, sort, promotions, and zero-result behavior. |
| `ELISA_Product_Series_Business_Rules.docx` | ELISA PDP identity, route, commerce, package examples, structured data, banner behavior, references, related products, documents, and analytics. |

## 15. Repository Validation Note

The user requested review of the de-magellan team repositories. In the current environment, the GitHub connector returned no accessible repositories for the searched terms, so repository-level validation could not be completed. The PRD is grounded in the supplied rule documents and the uploaded PRD templates. Final sign-off should include a follow-up source traceability pass after GitHub access is restored.
