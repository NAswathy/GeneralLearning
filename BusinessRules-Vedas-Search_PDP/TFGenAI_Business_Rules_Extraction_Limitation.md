# TFGenAI Business Rules Extraction Limitation

Normal repo-wise business-rules documents could not be produced under the provided strict prompt.

Accessible repositories and content:
- GitHub repository search metadata was accessible for the Thermo Fisher `tfgenai` repository set.
- The search returned multiple private `tfgenai` repositories, including related groups such as search UI/vector services, data pipelines, agent gateway/agent repositories, admin/entity repositories, ordering repositories, product information repositories, and evaluation/benchmarking repositories.
- The GitHub connector can fetch a known file path when the exact file path is already known. This was confirmed by fetching `README.md` from `thermofisher/tfgenai-components`.

Repositories or content not fully accessible:
- Local `git clone` access to the private repositories failed with `Repository not found`, so the repositories could not be reviewed locally.
- The GitHub connector did not expose recursive repository tree or directory-listing access for these repositories.
- Because file inventories were not available, business-rule packages, UI flows, validators, configuration files, tests, templates, jobs, integrations, and message processors could not be exhaustively identified or reviewed across the repository set.

Mandatory sweep coverage:
- Fully covered: none.
- Partially covered: repository discovery and limited known-file access.
- Not reached: actor and access context; entity lifecycle; eligibility and validation; selection, filtering, and visibility; entry points and user actions; defaults and source-of-truth rules; constants, flags, and precedence; source and variant handling; pricing and quantity behavior; state transitions and side effects; integrations and downstream behavior; file, record, and payload contracts; background and scheduled behavior; error, exception, and warning behavior; UI behavior with business impact; user-facing business messages; and test-confirmed edge cases.

Specific blocker:
- The supplied prompt requires full repository review and prohibits producing a normal business-rules document when mandatory business-rule areas cannot be fully reviewed. Since only repository metadata and isolated known files were accessible, generating repo-wise business rules would require unsupported inference.
