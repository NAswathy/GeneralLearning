# Product Requirements Document

## Primary Antibody Product Series

| Field | Value |
|---|---|
| Product name | Primary Antibody Product Series |
| Product area | Thermo Fisher antibody search and product detail experience |
| Prepared for | Business, Product, Commercial, Support, Scientific Content, Compliance, and Digital Platform stakeholders |
| Source business rules | `Primary_Antibody_Product_Series_Business_Rules.docx` and local Markdown rules extraction |
| Template references | Catalog Admin PRD; Business User PRD Genomics Tools v2 |
| Repository reference requested | `https://github.com/orgs/thermofisher/teams/de-magellan/repositories` |
| Repository validation status | Pending. GitHub access failed because the configured token was expired. |
| Date | 2026-06-01 |
| Status | Draft PRD |

## 1. Product Overview

### Product Name

Primary Antibody Product Series.

### Business Owner

Product Management / Digital Product Owner for Antibody discovery and PDP experience. Named owner to be confirmed.

### Purpose

The Primary Antibody Product Series experience enables customers, commercial teams, support teams, and scientific stakeholders to discover, evaluate, compare, select, and purchase primary antibody products. The experience must present scientifically relevant product details while preserving commercial correctness for price, availability, package selection, entitlement, product lifecycle state, related products, references, and question-and-answer content.

### Business Problem

Primary antibody products contain many scientific and commercial attributes: host, clone, clonality, species reactivity, application, dilution, conjugate, immunogen, target information, bioinformatics, published images, references, package sizes, pricing, availability, related products, and Q&A content. If these are inconsistent across search, PDP, commerce, and related-product modules, users may select the wrong antibody, miss an appropriate alternative, or contact support unnecessarily.

### Goals

- Provide a reliable product detail experience for primary antibody products.
- Make core scientific selection attributes easy to find and compare.
- Enforce correct package, price, availability, lifecycle, and Add to Cart behavior.
- Support research evaluation through specifications, images, Bioinformatics, Target Information, References, and Q&A.
- Recommend relevant secondary antibodies, isotype controls, primary alternatives, ELISA kits, matched antibody pairs, and application-level related products.
- Capture analytics that help business teams understand product engagement, conversion friction, missing content, and support needs.

### Scope

In scope:

- Primary antibody search result and product series behavior.
- Product banner, commerce card, package selection, price, availability, Add to Cart, and bulk/custom format behavior.
- Product data, product specifications, structured data, images, published figures, and PDP content sections.
- Bioinformatics, Target Information, References, Related Products, and Questions and Answers.
- Analytics, operational monitoring, support needs, acceptance criteria, and release readiness.

Out of scope:

- New scientific antibody-design algorithms.
- Manual correction of source catalog records outside approved catalog governance.
- Replacement of pricing, cart, authentication, Q&A, related-products, BenchSci, or catalog services.
- Regulatory or diagnostic-use claims beyond approved product notices.

## 2. Users and Stakeholders

### Primary Personas

| Persona | Need | Success Outcome |
|---|---|---|
| Research customer | Find a primary antibody that matches target, species, host, clone, application, and format needs. | Can evaluate product fit and purchase or save the correct SKU. |
| Commercial / Sales user | Recommend appropriate primary antibodies and related products for customer use cases. | Can identify product, package, price state, availability, related products, and support options quickly. |
| Field Application Scientist | Validate antibody fit for applications such as Flow Cytometry, WB, IHC, ICC/IF, ELISA, or other assays. | Can review tested applications, dilution, target information, references, and published figures. |
| Customer Support | Resolve questions about product selection, availability, discontinued products, replacements, and Q&A. | Can reproduce PDP behavior and explain commerce or lifecycle state. |
| Product Manager | Monitor portfolio engagement, content completeness, conversion, and related-product performance. | Can identify missing content, high-friction SKUs, zero-result patterns, and recommendation gaps. |
| Compliance / Legal reviewer | Ensure product notices and claims are shown correctly. | Research-use, diagnostic-use, resale, lifecycle, and banner messaging are consistently applied. |
| Engineering / Platform teams | Maintain search, PDP, pricing, availability, Q&A, related-products, and analytics integrations. | Can test clear requirements and monitor service-level behavior. |

### Decision Makers

- Antibody product owner.
- eCommerce product owner.
- Search/PDP platform owner.
- Commercial operations leadership.
- Support operations leadership.
- Compliance and legal stakeholders.
- Data and analytics owner.

## 3. Architecture

### Business Architecture Summary

The Primary Antibody Product Series experience is a multi-service product discovery and commerce flow. Search and PDP components present product identity, specifications, content sections, and related products. Commerce services determine package selection, pricing action, user price, availability, Add to Cart eligibility, and support/bulk quote paths. Content services provide images, BenchSci figures, references, Q&A, target information, and Bioinformatics metadata.

### High-Level Flow

| Step | Business Action | System Outcome |
|---|---|---|
| 1 | User searches or opens a primary antibody PDP. | Product subtype is resolved as primary antibody and matching product records are loaded. |
| 2 | Product identity and banner state are evaluated. | Product title, selected SKU, lifecycle, replacement, and package banner messages are shown as applicable. |
| 3 | Commerce card loads. | Package selector, price state, availability state, Add to Cart, Check Your Price, and bulk/custom actions are determined. |
| 4 | Scientific details render. | Specifications, tested applications, target information, product information, images, published figures, and structured data are built from available values. |
| 5 | Deep content sections render. | Bioinformatics, References, Related Products, and Q&A sections appear only when data is visible or available. |
| 6 | User acts. | User changes package, checks price, views availability, adds to cart, reviews references, opens related products, or reads Q&A. |
| 7 | Events and support signals are captured. | Analytics and monitoring record product engagement, commerce outcomes, errors, and missing-data conditions. |

### Technical Stack and Integrations

| Area | Expected / Referenced Capability |
|---|---|
| Frontend | Magellan search/PDP UI components for antibody search and product details. |
| Product data | Product catalog/search records for antibody product subtype and primary antibody attributes. |
| Pricing | Pricing service returns package-level price, user price, pricing action, currency, bulk quote path, and orderability. |
| Availability | Availability service returns stock, estimated availability, dealer availability, and selected SKU availability state. |
| Cart | Add to Cart service accepts selected package SKU/web ID, quantity, and product context. |
| Related products | Related-products service generates secondary antibody, isotype control, primary alternative, ELISA, matched antibody pair, and application-level recommendations. |
| Q&A | Q&A service generates product keywords, counts matched records, and returns paged or filtered questions. |
| Images and references | Product media and BenchSci/reference sources provide images, published figures, cards, publication tables, and disclaimers. |
| Target/Bioinformatics | Target family and bioinformatics data sources provide aliases, UniProt, Entrez, function, process, and target descriptions. |
| Analytics | Event collection for product view, package change, price/availability, Add to Cart, related-product click, references, Q&A, and support paths. |

### Dependencies

- Accurate product subtype classification for primary antibodies.
- Product search records with status and visibility flags.
- Package-level product data and SKU/web ID mapping.
- Pricing and availability service reliability.
- Related-product matching data for host species, target species, isotype, clone, conjugate, application, target protein, tested species, size, coated value, and kit format.
- Q&A keyword and product-filter data quality.
- BenchSci and reference content availability.
- Target information and Bioinformatics data completeness.
- Country, login state, entitlement, and dealer context.

## 4. Core Features and Requirements

### 4.1 Product Eligibility and Search

| ID | Requirement | Acceptance Criteria |
|---|---|---|
| PA-REQ-001 | The system must identify primary antibody products by antibody subtype and primary antibody product records. | Search and PDP load only matching primary antibody records when the product set contains matching records. |
| PA-REQ-002 | Primary antibody product records must use the active search status required by the search experience. | Records marked with active status are included; unavailable matching records do not create a result set. |
| PA-REQ-003 | Search results must display product identity, thumbnail, description, product type, product subtype, reference count, image count, and antibody-specific details when available. | Results show relevant product details such as applications, citations, clonality, clone, conjugate, host, package sizes, protein target, reactivity, target, target verification, and lifecycle. |

### 4.2 Product Title Banner and Lifecycle Messaging

| ID | Requirement | Acceptance Criteria |
|---|---|---|
| PA-REQ-004 | PDP must show a banner when a selected package has long-term unavailable, discontinued, replaced, or package-specific banner messaging. | Correct message appears for selected package and updates when package changes. |
| PA-REQ-005 | Replacement banners must identify the requested catalog number and replacement catalog number when available. | Replacement link or text is visible and Technical Support guidance appears. |
| PA-REQ-006 | Users must be able to close a displayed product banner. | Closing the banner hides it from the current view. |

### 4.3 Commerce Card, Price, Availability, and Add to Cart

| ID | Requirement | Acceptance Criteria |
|---|---|---|
| PA-REQ-007 | Commerce card must display selected catalog number and package size selection where multiple packages exist. | Package selector appears for multi-package products and selected SKU drives price, availability, data sheet, banner, and catalog refresh. |
| PA-REQ-008 | Pricing must be resolved at package level. | Each package receives price, user price, bulk quote path, and orderability where pricing data exists. |
| PA-REQ-009 | Pricing failures must fall back to a safe purchase action state before availability rules are applied. | View price in cart with Add to Cart and USD fallback is used when pricing is unavailable or fails. |
| PA-REQ-010 | Add to Cart must be available only when selected package is orderable and not long-term unavailable. | Error, discontinued, and long-term unavailable packages suppress normal Add to Cart. |
| PA-REQ-011 | Quantity must be constrained from 1 through 9,999. | Values below 1 reset to 1; values above 9,999 reset to 9,999; invalid attempts show an alert. |
| PA-REQ-012 | Anonymous users must see correct price-check actions. | Check Your Price and Availability or Check Your Price appears based on orderability and availability enablement. |
| PA-REQ-013 | Availability details must be shown only when enabled for user context and package is orderable. | Availability checks are performed for selected SKU and rechecked after package or quantity changes. |
| PA-REQ-014 | Estimated availability must show Pending when estimate is required but missing or pending. | Pending appears only when estimated availability conditions are met. |
| PA-REQ-015 | Dealer-enabled signed-in users may see dealer-specific availability details. | Partial stock, domestic stock, overseas stock, default label, and estimated date appear when returned by dealer availability. |
| PA-REQ-016 | Aspire link must be shown only for eligible primary antibody products in the United States or Canada. | Link appears only when product type, subtype, and country rules match. |

### 4.4 Product Data, Specifications, and Structured Data

| ID | Requirement | Acceptance Criteria |
|---|---|---|
| PA-REQ-017 | PDP must display tested applications and dilution values when available. | Application and dilution data are visible on product details. |
| PA-REQ-018 | PDP must display product specifications when values are available. | Specifications can include species reactivity, host/isotype, class, type, clone, immunogen, conjugate, form, concentration, amount, purification, storage buffer, contents, storage conditions, shipping conditions, and RRID. |
| PA-REQ-019 | Target verification must use the first value before a pipe delimiter; missing values must show No. | Target verification is normalized consistently. |
| PA-REQ-020 | Pipe-delimited and repeated values must be split or deduplicated before display. | Cross-adsorption, package sizes, alternate SKUs, laser compatibility, protein aliases, GenBank, RefSeq, and UniProt values render without duplicate or unsplit artifacts. |
| PA-REQ-021 | Structured data must include only present product specifications and valid offer information. | Empty specs are omitted; offers are removed when product is discontinued, long-term unavailable, missing final price, missing availability, or not orderable. |
| PA-REQ-022 | Structured data must use a product image when available and no-image asset when absent. | Image fallback is deterministic and valid for product schema. |
| PA-REQ-023 | Product pages must display research-use, diagnostic-use, and resale notices when present. | Approved notices appear in PDP content. |

### 4.5 Images and Published Figures

| ID | Requirement | Acceptance Criteria |
|---|---|---|
| PA-REQ-024 | Image counts must distinguish regular product images from BenchSci published figures. | Regular count excludes BenchSci external images; BenchSci figure count is capped at 40. |
| PA-REQ-025 | Thumbnail selection must follow the product image priority rules. | Regular product image is used when both regular and BenchSci images exist; BenchSci flow is used when only BenchSci figures exist; no-image placeholder appears when no images exist. |
| PA-REQ-026 | Product image display must show additional image count when more than one image exists. | Additional count equals images beyond the selected thumbnail. |
| PA-REQ-027 | QA markers must be removed from image URLs before display. | Displayed image source URLs do not contain `.qa` marker. |

### 4.6 Bioinformatics and Target Information

| ID | Requirement | Acceptance Criteria |
|---|---|---|
| PA-REQ-028 | PDP must display Bioinformatics section when visible content exists. | Section header appears and is included as a destination only when visible. |
| PA-REQ-029 | Bioinformatics must display protein aliases, gene aliases, UniProt ID, Entrez Gene ID, Function(s), and Process(es) when available. | Fields appear only when data is present and section navigation reflects visible sections. |
| PA-REQ-030 | Target family pages must display target information for Gene, Protein, Panther, and Gene Ontology target families. | Correct anchor links and target title appear for each family type. |
| PA-REQ-031 | Gene and Protein target descriptions must support collapsed and expanded views. | View More expands truncated description; View Less collapses it. |

### 4.7 References

| ID | Requirement | Acceptance Criteria |
|---|---|---|
| PA-REQ-032 | References section must load all reference cards when available. | Section appears as a destination only when visible. |
| PA-REQ-033 | BenchSci reference cards must display image, published figures icon, and disclaimer. | BenchSci card-specific content is visible. |
| PA-REQ-034 | Non-BenchSci reference cards must show source, title, year, species, dilution, description, and authors when available. | Cards render required metadata without empty placeholders. |
| PA-REQ-035 | Reference tables must sort by Species, Dilution, Title, Authors, Journal, and Most Recent. | Sort behavior follows ascending values except Most Recent, which uses year descending. |
| PA-REQ-036 | Publication tables must initially show five rows with View More and View Less behavior. | User can expand to all rows and collapse back to five. |

### 4.8 Related Products

| ID | Requirement | Acceptance Criteria |
|---|---|---|
| PA-REQ-037 | Related secondary antibodies must match primary antibody host species to secondary target species and primary target isotype to secondary target class. | Recommendations follow matching rules and exclude invalid species values. |
| PA-REQ-038 | Secondary antibody recommendations must be prioritized by cross-adsorption, clone, and conjugate combinations. | Highest-priority matches appear before lower-priority matches. |
| PA-REQ-039 | Isotype controls must match host species and target isotype, and match conjugate when primary antibody has a conjugate. | Isotype controls are ordered by clone/conjugate priority and size. |
| PA-REQ-040 | Related primary antibody alternatives must match target protein and target isotype while excluding the original product. | Alternatives prioritize clone availability, conjugate value, and size. |
| PA-REQ-041 | ELISA kits and matched antibody pairs must be recommended only when primary antibody supports ELISA. | ELISA recommendations match target protein and tested species; matched antibody pairs include only matched-pair kit format. |
| PA-REQ-042 | Application-level related products must require both application and SKU. | Related products group by subapplication when application counts are returned and can be filtered by application and subapplication. |

### 4.9 Questions and Answers

| ID | Requirement | Acceptance Criteria |
|---|---|---|
| PA-REQ-043 | Q&A keyword generation must set product subtype to Antibody for primary antibody products. | Generated keywords include protein target, application, host species, conjugate, clonality, clone, brand, target species, product subtype, format, and recombinant values. |
| PA-REQ-044 | Q&A matching must include exact SKU and product keyword filters. | Product filters include host, clonality, protein target, conjugate, clone, brand, target species, format, recombinant, product subtype, and application filters when present. |
| PA-REQ-045 | Q&A counts and results must fail safely. | Failed counts return zero; failed searches return empty result sets. |
| PA-REQ-046 | Paged and filtered Q&A results must follow deterministic sorting. | Paged results sort by answer count and submitted date; unpaged and filtered results sort by vote count, answer count, and submitted date. |

## 5. Data and Analytics

### Business KPIs

| KPI | Definition | Business Use |
|---|---|---|
| Primary antibody PDP views | Number of primary antibody PDP views. | Measure portfolio engagement. |
| Search-to-PDP rate | Percentage of search users opening a primary antibody PDP. | Measure discovery effectiveness. |
| Package change rate | Frequency of package selector changes. | Identify products where size selection matters. |
| Price-check rate | Check Your Price / Check Price and Availability actions. | Identify pricing friction for anonymous or region-specific users. |
| Add-to-cart rate | Percentage of orderable PDP sessions that add product to cart. | Measure commercial conversion. |
| Availability check rate | Availability detail requests by product/SKU. | Identify demand and stock concerns. |
| Banner exposure rate | Sessions with long-term unavailable, discontinued, replacement, or custom banner messages. | Track lifecycle and replacement impact. |
| Related-product click-through | Clicks on secondary antibody, isotype control, alternatives, ELISA, or application-level recommendations. | Measure recommendation value. |
| References engagement | Reference sorting, View More, and reference-card interactions. | Measure scientific evidence usage. |
| Bioinformatics engagement | Views/clicks into Bioinformatics and Target Information sections. | Measure depth of scientific evaluation. |
| Q&A engagement | Q&A count, search, filter, and question views. | Understand support/self-service usage. |
| Error and fallback rate | Pricing, availability, Q&A, related-products, images, and reference failures. | Prioritize reliability improvements. |

### Minimum Reporting Events

- Product search performed.
- Primary antibody result returned.
- Primary antibody PDP opened.
- Product banner shown, closed, or replacement clicked.
- Package size changed.
- Price lookup started, succeeded, failed, or returned no price.
- Check Your Price clicked.
- Availability requested and availability response shown.
- Quantity changed and invalid quantity alert shown.
- Add to Cart clicked, succeeded, or failed.
- Bulk/custom format requested.
- Aspire link displayed and clicked.
- Specifications section viewed.
- Bioinformatics section viewed.
- Target Information expanded or collapsed.
- References section loaded, sorted, expanded, or collapsed.
- Related product viewed and clicked.
- Q&A count loaded, search performed, filter applied, result clicked, or error returned.
- Product image gallery opened and BenchSci figure viewed.

## 6. Risks and Constraints

| Risk / Constraint | Impact | Mitigation |
|---|---|---|
| Repository source access unavailable. | PRD cannot be source-confirmed against de-magellan repositories. | Restore GitHub access and run source traceability review before final sign-off. |
| Product data is incomplete or stale. | Incorrect specifications, target information, references, or related products may appear. | Add data-quality checks and ownership for catalog, Bioinformatics, target, Q&A, and related-product feeds. |
| Pricing service fails or returns error actions. | Users may see fallback pricing or cannot purchase. | Track pricing failures and show clear View price in cart, Contact Us, or no-price messages. |
| Availability varies by country, login, quantity, and dealer context. | Users may see inconsistent purchase confidence. | Monitor availability checks and test by country/login/dealer scenarios. |
| Lifecycle banners may be missed after package change. | Users may order or evaluate replaced/discontinued products incorrectly. | Recompute banner after every selected package change. |
| Related-product matching may recommend weak matches. | Users may select inappropriate secondary antibodies, controls, or kits. | Add recommendation test sets for host, isotype, clone, conjugate, target protein, tested species, and ELISA application. |
| Q&A keyword defaults may over-match. | Irrelevant questions may appear. | Review keyword generation and sort quality with support/product owners. |
| BenchSci/reference content may be unavailable. | Users lose scientific evidence signals. | Fail gracefully and monitor reference/image availability. |
| Compliance notices may be missing. | Regulatory and claims risk. | Include compliance notice checks in release readiness. |
| Country and entitlement differences may affect visible commerce behavior. | Business users may not reproduce customer view. | Provide support tooling or context capture for country, login state, and selected SKU. |

## 7. Operations and Support

### Monitoring Requirements

- Search result count and zero-result rate for primary antibody queries.
- PDP load success, latency, and section visibility.
- Pricing lookup latency, error rate, and pricing-action distribution.
- Availability request success, error rate, and Pending estimate frequency.
- Add to Cart success and failure rate by SKU and package.
- Banner display frequency for unavailable, discontinued, replaced, and custom messages.
- Related-products service response rate, empty response rate, and click-through.
- Q&A count/search response rate, empty response rate, and error rate.
- BenchSci/reference image load errors.
- Bioinformatics and Target Information missing-data rates.
- Structured data validity and offer suppression conditions.

### Common Support Scenarios

| Scenario | Support Handling |
|---|---|
| User cannot find a primary antibody. | Check keyword, target, species, application, product subtype, and active search status. |
| Product has no visible price. | Check login state, pricing action, country, selected package, and pricing service response. |
| Product cannot be added to cart. | Check selected package orderability, lifecycle state, quantity, price action, and long-term unavailable status. |
| Availability is missing or Pending. | Check country enablement, selected SKU, quantity, and estimated availability settings. |
| Replacement banner appears. | Confirm discontinued or unavailable package state and replacement product path. |
| Related secondary antibody or isotype control looks wrong. | Validate host species, target species, target isotype/class, clone, conjugate, and cross-adsorption data. |
| References or figures are missing. | Check BenchSci/reference feed and image-count rules. |
| Q&A does not show expected questions. | Check exact SKU match, generated keywords, application filters, and Q&A service errors. |

### Business Admin Needs

- Maintain primary antibody product subtype mapping.
- Review product specifications and target information completeness.
- Review lifecycle and replacement messages.
- Review related-product quality and priority rules.
- Review Q&A keyword quality and support deflection value.
- Review compliance notices.
- Review analytics dashboards and operational alerts.

## 8. Acceptance Test Scenarios

| Scenario | Expected Result |
|---|---|
| Open a primary antibody PDP with one package. | Commerce card uses the first/only package and displays selected catalog number. |
| Open a primary antibody PDP with multiple packages. | User can change package size and price, availability, banner, SKU, and data sheet context update. |
| Select a long-term unavailable package. | Add to Cart is suppressed and Contact Us path appears. |
| Select a discontinued package with replacement. | Banner identifies discontinued SKU and replacement catalog number. |
| Enter quantity 0. | Quantity resets to 1 and invalid quantity behavior is shown if Add to Cart is attempted. |
| Enter quantity 10000. | Quantity resets to 9999. |
| Anonymous user views orderable product. | Check Your Price or Check Your Price and Availability appears according to availability enablement. |
| Product has Bioinformatics data. | Bioinformatics section appears with aliases, UniProt, Entrez, Function(s), and Process(es) where available. |
| Product has references. | References section loads cards and supports sorting and View More/View Less. |
| Product supports ELISA application. | ELISA kit and matched antibody pair recommendations can be returned according to rules. |
| Product has no images or BenchSci figures. | No-image placeholder appears. |
| Q&A service fails. | Count returns zero or results return empty set without breaking PDP. |

## 9. Release Readiness Checklist

| Area | Readiness Requirement |
|---|---|
| Source traceability | Repository access restored and PRD requirements mapped to code/services. |
| Product eligibility | Primary antibody subtype and active search status validated. |
| Commerce | Package, price, quantity, Add to Cart, Check Your Price, and bulk/custom actions tested. |
| Availability | Country, login, dealer, quantity, and estimated availability scenarios tested. |
| Banner | Unavailable, discontinued, replacement, and custom package banner scenarios tested. |
| Specifications | Key specification fields and normalization rules tested. |
| Images | Regular image, BenchSci image, mixed image, and no-image scenarios tested. |
| Bioinformatics | Section visibility and field-level rendering tested. |
| Target Information | Target family pages and View More/View Less behavior tested. |
| References | BenchSci, non-BenchSci, sorting, and publication expansion tested. |
| Related Products | Secondary antibody, isotype control, alternative, ELISA, matched pair, and application-level recommendations tested. |
| Q&A | Keyword generation, exact SKU matching, paged results, filtered results, and error handling tested. |
| Analytics | Required events validated end to end. |
| Support | Support playbook and escalation owners documented. |
| Compliance | Research-use, diagnostic-use, resale, and lifecycle messaging reviewed. |

## 10. Open Questions

- Who is the named business owner for Primary Antibody Product Series?
- Which de-magellan repositories are authoritative for search, PDP, related products, Q&A, pricing, availability, and target data?
- Should the PRD cover primary antibody search and PDP together, or should search have a separate PRD?
- Which analytics platform is the source of truth for PDP section engagement and commerce events?
- What SLA should apply to pricing, availability, Q&A, related products, and reference service responses?
- Should support users have a diagnostic view showing country, login state, selected SKU, pricing action, availability status, and generated Q&A keywords?
- What product-owner review cadence should be used for related-product recommendation quality?

## 11. References

- Primary Antibody Product Series Business Rules.
- Catalog Admin PRD - Products, Entitlements, Pricing, and Price Access.
- Business User PRD Genomics Tools v2.
- PRD template screenshot dated 2026-06-01.
- de-magellan team repositories: access pending due to expired GitHub token.
