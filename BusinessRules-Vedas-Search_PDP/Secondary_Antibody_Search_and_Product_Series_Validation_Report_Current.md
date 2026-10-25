# Secondary Antibody Search And Product Series Validation Report

## Verification Scope

- Search example reviewed: `https://www.thermofisher.com/antibody/secondary/query/*`
- Product example reviewed: `https://www.thermofisher.com/antibody/product/Goat-anti-Rabbit-IgG-H-L-Cross-Adsorbed-Secondary-Antibody-Polyclonal/A-11008`
- Repository evidence reviewed through the GitHub connector:
  - `thermofisher/magellan-search`
  - supporting search hits from `thermofisher/magellan-core`
  - supporting proxy/config search hits from `thermofisher/tfcom-magellan-proxy`
- Prompt mode requested: multi-repo.
- Important limitation: the GitHub connector can search installed Thermo Fisher repositories and fetch source files, but it does not expose the exact repository list for the `de-magellan` team URL as a team-membership listing. The report therefore validates against accessible installed Magellan repository evidence, not a formally complete team-repository inventory.

## Overall Assessment

- The secondary antibody search rules are directionally correct and are supported by the Magellan search implementation.
- The secondary antibody PDP rules are mostly correct for product identity, title/header behavior, package selection, commerce card visibility, specifications, target information, references, Q&A enablement, and related-antibody display.
- The live A-11008 PDP confirms the product is a Secondary Antibody PDP and displays published figures, Questions & Answers, product image gallery, product-specific information, target information, references, performance guarantee, and support sections.
- The live A-11008 PDP shows References (0) while also showing 83 Published Figures, so references and published figures must remain separate rule areas.
- Bioinformatics should be treated carefully for secondary antibodies. The legacy template explicitly suppresses alias and ID fields for Secondary Antibody, and the reviewed live page did not show a Bioinformatics section.
- Detailed Q&A ranking/matching rules should not be treated as fully verified from `magellan-search` alone; those require the Q&A service repository.
- Dynamic price, Add to Cart, and availability outcomes require browser execution and commerce-service responses because static HTML does not prove final runtime state.

## Search Page Validation

### Confirmed Or Repository-Backed Rules

- Secondary antibody search applies a product subtype filter for Secondary Antibody.
- The secondary antibody search chain applies search-status and entitlement filters.
- Secondary antibody search uses a secondary antibody collection setting.
- Secondary antibody result rows include Product, Images, Host, Target Species, Conjugate, Application, Price, and Compare columns.
- Search result rows display package-size behavior differently for multi-package and single-package products.
- The search page fetches antibody prices after page load.
- References on result rows are shown only when reference count is greater than zero and reference-count display is enabled.
- Advanced Verification is shown only when the product is target verified and advanced-verification display is enabled.
- Green badge display is conditional on both feature enablement and product green-badge data.
- Secondary antibody is configured with spell-check behavior.
- Secondary antibody is configured with alternate-search behavior across other antibody-related subtypes and ELISA.

### Search Rules That Need Runtime Validation

- Compare selection limits and exact compare panel behavior should be validated in the browser.
- Filter application, Clear All, Reset, sort changes, and Load More should be validated with Playwright against the current production bundle.
- Typeahead behavior should be validated separately because the subtype configuration marks secondary antibody GSH typeahead as false, while older legacy code contains secondary typeahead paths.
- FisherSci price behavior and batch pricing should be validated with the active runtime configuration and API responses.

## Product Page Validation

### Confirmed On The Live Product Page

- The live PDP title is Goat anti-Rabbit IgG (H+L) Cross-Adsorbed Secondary Antibody, Alexa Fluor 488.
- The live PDP is for catalog number A-11008.
- The live PDP breadcrumb/category identifies Secondary Antibodies.
- The page displays a related higher-specification reagent message near the product title for catalog A32731.
- The page displays 83 Published Figures.
- The page displays "View all (249) Goat anti-Rabbit IgG antibodies".
- The page displays Datasheet, Certificates, Questions & Answers, and Tech Support actions.
- The page includes citation text using product name, Thermo Fisher Scientific, catalog number A-11008, and RRID AB_143165.
- The image gallery is present and includes antibody testing data and published-figure content.
- The page displays Target Information.
- The page displays References (0).
- The page asks users to report publications citing the product when references are zero.
- The page includes a Cite this product action.
- The page displays a BenchSci disclaimer for third-party scientific content.
- The page displays Performance Guarantee and We're here to help support sections.

### Product Rules Confirmed By Repository Logic

- Secondary antibody PDPs use the secondary subtype path `/antibody/secondary`.
- Secondary antibody related-antibody display is always enabled in the secondary antibody PDP view model.
- Secondary antibody related-antibody links include See all Secondary Antibodies, Epitope tag antibodies, and Loading isotype controls.
- Q&A display requires global Q&A enablement and subtype enablement.
- Secondary Antibody is configured as Q&A-enabled.
- Q&A country enablement is limited to configured countries, currently US and CA.
- Related-products display requires global related-products enablement and subtype enablement.
- Secondary Antibody is configured as related-products-enabled.
- Product specifications are included only when the corresponding product values exist.
- Secondary antibody target-specific fields include Target, Cross Adsorption, and Antibody Form when present.
- Shipping Condition is shown only when enabled and when the value exists.
- Tech Support modal display is subtype and country gated.

### Product Rules That Need Runtime Validation

- Final displayed price requires pricing API execution.
- Final Add to Cart availability requires selected package, entitlement, search status, pricing action, long-term-unavailable state, discontinued state, and runtime API response.
- Availability details require country/login context and availability API response.
- Package switching should be tested to confirm banner, price, availability, data sheet, and SKU updates for the selected package.
- Q&A widget loading should be tested in US and CA contexts and outside enabled countries.
- Related-products widget loading should be tested to confirm whether V2 widget output is visible and whether legacy links are still present.
- Product-specific banner behavior should be tested for available, temporarily unavailable, discontinued, replaced, and long-term-unavailable secondary antibody SKUs.

## Bioinformatics Validation

- The requested Bioinformatics area was reviewed in the PDP source.
- The legacy PDP Bioinformatics template can display Panther and GO function/process links when annotation data exists.
- For Secondary Antibody products, the legacy template suppresses Protein Aliases, Gene Aliases, UniProt ID, and Entrez Gene ID.
- In the shared view model, alias and ID display requires the product subtype to be Bioinformatics-enabled.
- Secondary Antibody does not enable the Bioinformatics display flag in the reviewed subtype configuration.
- The live A-11008 PDP did not show a Bioinformatics section in the static page content.
- Recommendation: keep Bioinformatics rules conditional and avoid copying primary-antibody Bioinformatics rules into secondary-antibody rule sets.

## Correctness Review Of Captured Rule Areas

### Correct To Keep

- Secondary search must be restricted to Secondary Antibody products.
- Secondary search must apply search-status and entitlement rules.
- Search result columns for secondary antibody should include product, images, host, target species, conjugate, application, price, and compare.
- Result-row references and advanced-verification links are conditional.
- Product specifications should display only populated values.
- Secondary antibody-specific specification fields should include Target, Cross Adsorption, and Antibody Form when present.
- Q&A should be documented as subtype-enabled, country-gated, and configuration-gated.
- Related antibody display should be documented as enabled for secondary PDPs.
- References and published figures should be documented as separate behaviors.

### Correct To Remove Or Reword

- Do not state that every secondary antibody PDP shows Bioinformatics.
- Do not state detailed Q&A sorting, matching, and fallback rules unless the Q&A service repository is reviewed.
- Do not state final price or availability outcomes from static page HTML alone.
- Do not state that secondary typeahead is active without verifying the current runtime path.
- Do not merge Related Products and Related Antibodies as one behavior; the reviewed secondary PDP code contains fixed related-antibody links, while the related-products widget is separately feature-flagged.

## Suggested Improvements

- Add a traceability appendix to future rule documents with one row per rule: rule, repo evidence, page evidence, and validation status.
- Run Playwright tests for search filters, sort, Load More, compare selection, package-size selection, price refresh, availability refresh, Q&A widget, related-products widget, and banner changes.
- Test anonymous and signed-in commerce states because price and availability behavior changes by login state.
- Test US, CA, CN, KR, and a country outside enabled availability lists to confirm country-specific behavior.
- Test a secondary antibody PDP with nonzero references to validate reference-card fields and sorting.
- Test a secondary antibody PDP with visible Bioinformatics data, if one exists, before adding stronger Bioinformatics rules.
- Test long-term-unavailable and discontinued secondary antibody products to validate banner and commerce-action states.
- Confirm whether the production bundle uses the legacy JSP commerce card or the newer common product-order component for all secondary antibody PDP traffic.
- Confirm the exact de-magellan team repository list through GitHub team access before labeling future extraction as complete under the strict multi-repo prompt.

## Final Recommendation

- Use the generated business-rules document as a repo-backed working rule set for Secondary Antibody Search and PDP.
- Treat it as validated for search subtype routing, visible result columns, PDP section visibility rules, Q&A enablement, related-antibody enablement, and specification display.
- Treat commerce price, availability, Add to Cart, Q&A service internals, and full related-products widget output as requiring a runtime/API validation pass before final business sign-off.
