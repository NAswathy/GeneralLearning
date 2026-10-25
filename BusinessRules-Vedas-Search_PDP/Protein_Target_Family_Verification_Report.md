# Protein Target Family Rule Verification Report

## Executive Summary

The captured Protein Target Family rules are mostly correct for page routing, metadata, target data parsing, Protein Details tabs, Research Products grouping, product-category routing, Learn More, Additional Resources, and 3D Structure behavior.

Important limitations and findings:

- The GitHub private multi-repo verification could not be completed because the GitHub connector returned an expired authentication-token error.
- Verification was completed against the QA pages, embedded page state, deployed BDNA JavaScript bundle, and live QA API responses.
- Two implementation issues should be reviewed: the target header subtitle appears hardcoded to the AKT1 alias, and bDNA counts differ between the category-card endpoint and the Research Products product-count endpoint.

## Verification Sources

- Prompt file: `/Users/aswathy.n/Downloads/business-rule-extraction-prompt-v3.md`
- QA target pages:
  - https://www.qa.thermofisher.com/tools/target/AKT1
  - https://www.qa.thermofisher.com/tools/target/BRCA1
- Deployed bundle:
  - `/bdna/static/main.7ae2b2ab1da71255138c.js`
- Target XML API:
  - `/bdna/MagWebSvcs/product/v1/getTargetData/{TARGET}`
- Research Products product-count API:
  - `/order/genome-database/unifiedCardProductTypeCount`
- Embedded category-card API:
  - `/order/genome-database/embeddedUnifiedResultsTF`
- Learn More API:
  - `/api/search/keyword/learnmore`

## GitHub Repository Verification Status

The requested team repository page requires authenticated GitHub access. The available GitHub connector failed with:

`Provided authentication token is expired. Please try signing in again.`

Because of this, the generated documents should be treated as deployed-behavior verified, not as fully private-source verified. A follow-up multi-repo source sweep should be run after GitHub authentication is refreshed.

## Correctness Checks

| Area | Result | Evidence |
| --- | --- | --- |
| Route | Correct | Pages resolve at `/tools/target/AKT1` and `/tools/target/BRCA1`. |
| SEO title | Correct | AKT1 title: `AKT1 Antibodies, Proteins & Assays | Thermo Fisher Scientific`; BRCA1 follows the same pattern. |
| SEO description | Correct | Description includes antibodies, proteins, ELISA kits, qPCR assays, bDNA assays, primers, and RNA. |
| Product family state | Correct | Embedded page state maps target pages to `genomic-portfolio` and product type `EBGPO`. |
| Protein Details source | Correct | Target XML endpoint returned target data for AKT1 and BRCA1. |
| Protein Details tabs | Correct | Bundle parses Overview, Gene Details, Protein Details, and Functions. |
| Research Products grouping | Correct | Bundle groups products into Gene Expression and Analysis, Gene Editing and Silencing, Proteins and Peptides, Protein Detection Kits, and Antibodies. |
| Zero-count hiding | Correct for cards | BRCA1 ELISA count was zero in product-count data and was omitted from embedded category cards. |
| Learn More behavior | Correct | API returns up to three results; UI displays first two. |
| Additional Resources | Correct | Documents & Support links to search with `persona=DocSupport`. |
| 3D Structure gating | Correct | Bundle requires Uniprot ID, PDB ID, and positive antigen length. |

## Example Data Validation

### AKT1

Target XML returned:

- Gene symbol: AKT1
- Gene name: AKT serine/threonine kinase 1
- Gene ID: 207
- Chromosome: 14
- Uniprot ID: P31749
- Entry name: AKT1_HUMAN
- PDB ID: AF_AFP31749F1
- Antigen length: 480
- Brightcove IDs: Antibody video present, ELISA video present, Protein video value is zero and should be ignored.

Research Products product-count API returned:

- Antibodies: 174
- Recombinant proteins and peptides: 2
- ELISA kits: 4
- TaqMan assays and arrays: 1375
- Branched DNA gene expression assays: 308
- Branched DNA miRNA assays: 0
- PCR and Sanger sequencing primers: 80
- CRISPR guide RNA: 24
- siRNA: 38
- miRNA mimics and inhibitors: 0

Embedded category cards displayed:

- Antibodies: 174
- Recombinant proteins and peptides: 2
- ELISA kits: 4
- TaqMan assays and arrays: 1375
- Branched DNA gene expression assays: 322
- PCR and Sanger sequencing primers: 80
- CRISPR guide RNA: 24
- siRNA: 38

### BRCA1

Target XML returned:

- Gene symbol: BRCA1
- Gene name: BRCA1, DNA repair associated
- Gene ID: 672
- Chromosome: 17
- Uniprot ID: P38398
- Entry name: BRCA1_HUMAN
- PDB ID: AF_AFP38398F1
- Antigen length: 1863
- Brightcove IDs: Antibody video present, Protein video value is zero and should be ignored.

Research Products product-count API returned:

- Antibodies: 79
- Recombinant proteins and peptides: 1
- ELISA kits: 0
- TaqMan assays and arrays: 16670
- Branched DNA gene expression assays: 1582
- Branched DNA miRNA assays: 0
- PCR and Sanger sequencing primers: 804
- CRISPR guide RNA: 97
- siRNA: 54
- miRNA mimics and inhibitors: 0

Embedded category cards displayed:

- Antibodies: 79
- Recombinant proteins and peptides: 1
- TaqMan assays and arrays: 16670
- Branched DNA gene expression assays: 1624
- PCR and Sanger sequencing primers: 804
- CRISPR guide RNA: 97
- siRNA: 54

## Findings

**Finding 1 - Header subtitle appears hardcoded**  
The deployed bundle renders the header subtitle as `(Protein Kinase B, PKB)` for the target header component. That subtitle is valid for AKT1 but not for BRCA1. This should not be accepted as a business rule. The business rule should require target-specific synonym or descriptive-name data.

**Finding 2 - Updated date appears hardcoded**  
The deployed bundle renders `Updated: Mar 30, 2025`. If this date is intended to represent content freshness, it should be data-driven or clearly documented as a release/static-content date.

**Finding 3 - Count mismatch between endpoints**  
The embedded category-card endpoint and Research Products product-count endpoint disagree for Branched DNA gene expression assays:

- AKT1: category cards show 322; product-count API shows 308.
- BRCA1: category cards show 1624; product-count API shows 1582.

This can create inconsistent product availability counts on the same page.

**Finding 4 - Recombinant product routes differ by source**  
The product-count API returned `/antibody/protein/query/{TARGET}` for recombinant proteins and peptides, while the embedded category cards route to `/proteins/target/{TARGET}`. The preferred canonical route should be clarified.

**Finding 5 - Some taxonomy mappings are indirect**  
Research Products uses label, imageLink, siteSearchFilterLabel, product detail keys, and template matching to decide which categories to show. This makes the category behavior harder to reason about and easier to break when labels change.

**Finding 6 - Accessibility copy issue**  
The deployed bundle includes the Olink external link aria label and alt text with a trailing `qqq`. This should be removed.

**Finding 7 - Misleading fallback target in descriptions**  
Some description replacement logic uses `AKT1` as a fallback target when the current target is empty. A generic blank or guarded no-render behavior would avoid showing the wrong target.

**Finding 8 - Internal typo in state name**  
The bundle contains `porductSearchCount`. If still present in source, this typo should be corrected or isolated before it spreads into additional logic.

## Suggested Improvements

1. Refresh GitHub authentication and rerun a true multi-repo source verification against the DE Magellan repositories.
2. Make the header subtitle target-specific by sourcing it from target XML or another authoritative target profile service.
3. Make the updated date data-driven, or rename it if it reflects the page-template release date rather than target content freshness.
4. Standardize category counts so the embedded category cards and Research Products use the same count source or a clearly documented count contract.
5. Decide and document the canonical route for recombinant proteins and peptides.
6. Add automated regression checks for AKT1 and BRCA1 covering metadata, category cards, Research Products tabs, zero-count hiding, Protein Details fields, Learn More limit, and 3D Structure gating.
7. Replace label-string matching with a stable product taxonomy map using canonical product-type IDs.
8. Remove the `qqq` suffix from Olink alt and aria-label text.
9. Avoid defaulting target-specific text to AKT1 when no target is available.
10. Document the ownership and source of each target-page section: target XML, unified card HTML, product-count service, Learn More search, and AlphaFold/3D structure service.

## Overall Verdict

The generated rule set is suitable as a deployed-behavior business-rules draft. It should be finalized only after GitHub access is restored and the rules are reconciled with source code across the relevant private repositories.
