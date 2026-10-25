# Functional PRD - TFGenAI Project

| Field | Details |
| --- | --- |
| Document name | Functional PRD - TFGenAI Project |
| Version | 1.0 |
| Date | July 24, 2026 |
| Prepared for | Thermo Fisher Scientific GenAI / Digital Engineering stakeholders |
| Source scope | GitHub search results for `tfgenai`, with repo evidence reviewed through accessible repository files |
| Prompt basis | Multi-repo extraction discipline from `business-rule-extraction-prompt-v3.1.md`; PRD structure styled after `Antibody_Product_Subtypes_PRD_NoTaqMan_Final_With_TOC.docx` |
| Constraint | Do not invent missing facts. Repos with incomplete or generic reviewed evidence are marked as validation pending. |

## Table of Contents

| Section | Page |
| --- | --- |
| 1. Product Overview | Update in Word |
| 2. Users and Stakeholders | Update in Word |
| 3. Repository Inventory and Review Boundary | Update in Word |
| 4. Functional Architecture | Update in Word |
| 5. Repo-Wise Functional Requirements | Update in Word |
| 6. API and Integration Requirements | Update in Word |
| 7. Data, Configuration, and Analytics | Update in Word |
| 8. Core Workflows and Acceptance Criteria | Update in Word |
| 9. Operations and Support | Update in Word |
| 10. Risks, Constraints, and Improvements | Update in Word |
| 11. Validation Report | Update in Word |

## 1. Product Overview

| Area | Requirement |
| --- | --- |
| Product name | TFGenAI project portfolio |
| Purpose | Provide reusable GenAI services, agent execution, search/vector retrieval, ordering workflow support, SQL agent capability, sentiment analytics, citation intelligence, administrative configuration, MCP tooling, and data ingestion pipelines for Thermo Fisher digital experiences. |
| Business goals | Improve response quality, increase reuse of agent and retrieval capabilities, centralize GenAI configuration, support commerce and content workflows, and provide operational traceability for GenAI interactions. |
| Scope in this PRD | Functional requirements derived from reviewed `tfgenai` repositories, including repo-wise modules, scripts, controllers, services, methods, endpoints, workflows, and operational needs. |
| Out of scope | Undocumented internal implementation not visible in reviewed files; production infrastructure details not present in repositories; business commitments not supported by source evidence. |
| Delivery expectation | A developer-readable Functional PRD that maps functions to repos and scripts at least two levels below the repo where evidence is available. |

## 2. Users and Stakeholders

| Persona | Needs | Repos / Capabilities Used |
| --- | --- | --- |
| Business owner | Understand what TFGenAI capabilities exist, what business functions they support, and what gaps need decisions. | All repos; inventory and validation sections |
| Product manager | Translate GenAI features into roadmap-ready requirements, acceptance criteria, and risk items. | Admin UI, agent gateway, ordering gateway, citation, sentiment, search/vector |
| Backend developer | Locate service boundaries, controllers, methods, endpoints, data dependencies, and operational behavior. | `tfgenai-ordering-gateway`, `tfgenai-search-vector-api`, `tfgenai-sqlagent-api`, `tfgenai-agent-gateway`, `tfgenai-sentiments`, `tfgenai-citation` |
| Frontend developer | Understand UI-driven functional needs, config dependencies, route permissions, and state handling. | `tfgenai-admin-ui`, `tfgenai-sentiment-analysis-ui` |
| Data engineer | Understand ingestion entry points, source file handling, content pipelines, and vector/search dependencies. | `tfgenai-data-pipeline`, search/vector repos |
| Operations / SRE | Monitor service health, request flow, failures, DB/cache dependencies, and degraded states. | Gateway, ordering, sentiment, SQL, MCP, admin |
| QA / validation analyst | Verify repo evidence, endpoint behavior, filters, input handling, and acceptance criteria. | Validation report and API matrix |

## 3. Repository Inventory and Review Boundary

The GitHub search result for `tfgenai` returned a broad portfolio. The following repositories were reviewed at method or script level where files were accessible. Repositories with only generic README content, minimal size, archived state, or no implementation evidence in reviewed files are included but marked for follow-up validation.

| Review tier | Repository | Evidence reviewed | Functional classification |
| --- | --- | --- | --- |
| Method-level reviewed | `thermofisher/tfgenai-ordering-gateway` | `README.md`, `src/request-gateway/main.py`, `src/product-discovery/main.py`, `src/checkout/main.py`, `src/ops-ui/app/main.py` | Commerce/ordering gateway, product discovery, checkout, operations UI |
| Method-level reviewed | `thermofisher/tfgenai-search-vector-api` | `README.md`, `application.py`, `VectorSearchController.py`, `IntentClassificationController.py` | Vector, hybrid, keyword search and intent classification |
| Method-level reviewed | `thermofisher/tfgenai-sqlagent-api` | `README.md`, `application.py`, `GenAISQLAgentBaseController.py` | SQL agent API and feedback |
| Method-level reviewed | `thermofisher/tfgenai-sentiments` | `README.md`, `application.py`, `sentiments_controller.py` | Sentiment detail, summary, processing, CSV download |
| Method-level reviewed | `thermofisher/tfgenai-sentiment-analysis-ui` | `package.json`, `src/App.tsx`, `src/components/Main/Main.tsx` | Sentiment analytics UI |
| Method-level reviewed | `thermofisher/tfgenai-admin-ui` | `package.json`, `src/main.jsx`, `src/App.jsx`, `src/routes/AppRoutes.jsx`, `src/services/preferencesApiService.js`, `src/store/store.js` | GenAI administration UI, prompts, preferences, agent mapping, security, ingestion and cache screens |
| Method-level reviewed | `thermofisher/tfgenai-data-pipeline` | `README.md`, `document_data_pipeline.py`, `product_content_data_pipeline.py`, `faq_data_pipeline.py` | Content, FAQ, document, product content ingestion |
| Method-level reviewed | `thermofisher/tfgenai-agent-builder` | `README.md`, `.github/workflows/create-ai-agent.yml`, `tfgenai-agent-templates/standalone_repository/copier.yml` | Agent scaffolding and templating |
| Method-level reviewed | `thermofisher/tfgenai-gateway-mcp-server` | `README.md`, `server.py` | MCP server for prompts, fallback messages, agent invocation |
| Method-level reviewed | `thermofisher/tfgenai-citation` | `README.md`, `application.py`, `app/resources/agent_card.yaml`, `pyproject.toml`, `agent_executor.py` | Citation agent with A2A protocol, streaming, sources, summary shortcut |
| Controller-level reviewed | `thermofisher/tfgenai-agent-gateway` | `application.py`; README generic | Agent gateway Flask app, search, chat, administration, metadata, A2A |
| Limited evidence | `thermofisher/tfgenai-components` | README generic; package metadata not reviewed | Shared components, validation pending |
| Limited evidence | `thermofisher/tfgenai-searchvector-v3` | README generic | Search/vector v3, validation pending |
| Limited evidence | `thermofisher/tfgenai-custom-model` | Not enough implementation evidence reviewed | Custom model capability, validation pending |
| Limited evidence | `thermofisher/tfgenai-back-ops` | Not enough implementation evidence reviewed | Back office operations, validation pending |
| Limited evidence | `thermofisher/tfgenai-benchmarking-agent` | Not enough implementation evidence reviewed | Benchmarking agent, validation pending |
| Limited evidence | `thermofisher/tfgenai-vectors-entity-benchmark` | Not enough implementation evidence reviewed | Vector/entity benchmark, validation pending |
| Limited evidence | `thermofisher/tfgenai-vector-search-mcp-server` | Minimal repo size in search metadata; implementation not reviewed | Vector search MCP, validation pending |
| Limited evidence | `thermofisher/tfgenai-models` | Search did not return model implementation evidence | Model registry/service, validation pending |
| Limited evidence | `thermofisher/tfgenai-mcp-validation` | Not enough implementation evidence reviewed | MCP validation, validation pending |
| Limited evidence | `thermofisher/tfgenai-base-images` | Not enough implementation evidence reviewed | Shared container base images, validation pending |
| Limited evidence | `thermofisher/tfgenai-cmdb-agent` | Not enough implementation evidence reviewed | CMDB agent, validation pending |
| Limited evidence | `thermofisher/tfgenai-agent-builder-templates` | Related to agent builder templates, but not separately reviewed | Agent templates, validation pending |
| Limited evidence | `thermofisher/tfgenai-customer-insights-agent` | Not enough implementation evidence reviewed | Customer insights agent, validation pending |
| Limited evidence | `thermofisher/tfgenai-agent-gateway-listener` | Not enough implementation evidence reviewed | Gateway listener, validation pending |
| Limited evidence | `thermofisher/tfgenai-vectors-entity-documents` | Not enough implementation evidence reviewed | Vector/entity documents, validation pending |
| Archived / validation only | `thermofisher/tfgenai-agent-gateway-llm` | Search metadata indicated archived | Historical gateway LLM implementation |
| Archived / validation only | `thermofisher/tfgenai-extractive-qa` | Search metadata indicated archived | Historical extractive QA implementation |

## 4. Functional Architecture

### 4.1 Portfolio-Level Functional View

| Layer | Component | Level 2 modules / functions | Functional role |
| --- | --- | --- | --- |
| User experience | Admin UI | Prompts, preferences, application messages, agent mapping, security dashboard, document ingestion, cache management | Allows business and admin users to configure and operate GenAI behavior. |
| User experience | Sentiment Analysis UI | Date filters, SKU filters, username filters, page-group filters, sentiment summary, sentiment detail | Allows operational users to review feedback sentiment trends and drill into records. |
| Application clients | Agent Gateway | Search controller, user chat message controller, agent administration controller, agents metadata controller, A2A controller | Provides the central API boundary for agent search, chat, administration, metadata, and A2A access. |
| Application clients | Search Vector API | Vector match with score, hybrid search, keyword search, intent classification, entity classification | Provides retrieval and classification services for GenAI use cases. |
| Application clients | Agent services | Citation agent, SQL agent API, MCP prompt/fallback/invocation server | Executes specialized GenAI agents and shared MCP tools. |
| Commerce clients | Ordering Gateway | Request gateway, product discovery, checkout service, operations UI | Supports agent-assisted product discovery, checkout, request logging, and operational visibility. |
| Data and configuration | Spring Cloud Config | Endpoints, model keys, Redis settings, prompt/config values | Centralizes runtime configuration used by multiple services. |
| Data and configuration | PostgreSQL | Request logging, checkout sessions, order records, sentiments, audit | Stores transactional, operational, and analytical records where implemented. |
| Data and configuration | SQLite/static JSON | Product discovery mock/catalog data | Supports local or mock product discovery flows where configured. |
| Data and configuration | S3 | FAQ files, product content, document pipeline inputs | Provides source files and metadata for ingestion pipelines. |
| Data and configuration | PGVector / embeddings | Vector collections and embedded product/content data | Supports semantic search and retrieval scoring. |
| Data and configuration | Redis | MCP response cache when enabled | Improves repeated MCP response performance when cache middleware is enabled. |

### 4.2 Ordering Gateway Functional View

| Flow stage | Repo script / module | Level 2 module or method | Functional role |
| --- | --- | --- | --- |
| Client / agent commerce request | `src/request-gateway/main.py` | `Settings` | Loads product discovery, checkout, and MCP endpoints from config and environment values. |
| Client / agent commerce request | `src/request-gateway/main.py` | `RequestLoggingMiddleware` | Stores request and response traces for audit and troubleshooting. |
| Client / agent commerce request | `src/request-gateway/main.py` | `UCPService` | Handles UCP checkout operations. |
| Client / agent commerce request | `src/request-gateway/main.py` | `ACPService` | Handles ACP checkout operations. |
| Client / agent commerce request | `src/request-gateway/main.py` | `ProductService` / `ProductDiscoveryClient` | Routes product-related requests to product discovery. |
| Client / agent commerce request | `src/request-gateway/main.py` | ACP and UCP MCP mounts | Exposes ACP and UCP tool access through MCP. |
| Product discovery | `src/product-discovery/main.py` | List, search, get product endpoints | Provides product browsing, retrieval, pagination, and filtering. |
| Product discovery | `src/product-discovery/main.py` | UCP, ACP, merchant, and vendor mapping helpers | Converts internal product data into required external commerce formats. |
| Product discovery | `src/product-discovery/main.py` | XML, TSV, JSON download endpoints | Provides downloadable product feeds in supported formats. |
| Checkout | `src/checkout/main.py` | Fisher Scientific UI/API routers | Serves checkout UI/API routes. |
| Checkout | `src/checkout/main.py` | Legacy API router | Supports legacy API access under the existing route pattern. |
| Checkout | `src/checkout/main.py` | `health_check()` | Reports checkout service status, version, and timestamp. |
| Operations | `src/ops-ui/app/main.py` | Dashboard, orders, sessions, requests, errors, simulator routes | Gives operations users visibility into ordering gateway behavior. |
| Operations | `src/ops-ui/app/main.py` | `health_check()` DB validation | Reports healthy or degraded DB status. |

### 4.3 Search, Retrieval, and Classification View

| Flow stage | Repo script / module | Level 2 method / service | Functional role |
| --- | --- | --- | --- |
| Search request intake | `tfgenai-search-vector-api/application.py` | Blueprint registration | Registers vector, metadata, health, API integration, intent, base search, and feedback routes. |
| Vector scoring | `VectorSearchController.py` | `display_vector_match_with_score()` | Reads `searchQuery`, creates Azure OpenAI embeddings, searches PGVector, and returns catalog number, score, metadata, and page content. |
| Hybrid retrieval | `VectorSearchController.py` | `vector_search_hybrid()` | Uses default or configured collection and calls `VectorHybridSearchService.hybrid_search`. |
| Keyword retrieval | `VectorSearchController.py` | `vector_search_keyword()` | Uses default or configured collection and calls `VectorHybridSearchService.keyword_search`. |
| Intent classification | `IntentClassificationController.py` | `classification()` | Builds `SearchResultChain` and calls `IntentClassificationService.perform_intent_classification`. |
| Intent/entity classification | `IntentClassificationController.py` | `classification_v2()` | Uses `GPT_4_TURBO_MODEL` and calls `IntentEntityClassificationService.classify_intent_entity`. |

### 4.4 Data Pipeline Functional View

| Flow stage | Repo script / module | Level 2 method / configuration | Functional role |
| --- | --- | --- | --- |
| Scheduled or manual ingest trigger | `document_data_pipeline.py` | `document_type` and `s3_file_path` environment values | Selects document ingestion behavior based on runtime inputs. |
| Document ingestion | `document_data_pipeline.py` | `process_brochures_data`, `process_manuals_data`, `process_gallery_data`, `process_posters_data`, `process_sds_data`, `process_coa_data`, `process_support_files_data` | Routes supported document types to the matching processor. |
| Product content ingestion | `product_content_data_pipeline.py` | `s3_file_path` argument | Reads the source S3 product content path from command-line input. |
| Product content ingestion | `product_content_data_pipeline.py` | `Entitlements/product_entitlements_v3.csv` | Includes entitlement data as part of product content processing. |
| Product content ingestion | `product_content_data_pipeline.py` | `ProductContentProcessorV2.process_product_content_data_v2` | Executes product content processing with product content and entitlement inputs. |
| FAQ ingestion | `faq_data_pipeline.py` | `FAQ/genai-faq-dataload-metadata.json` | Reads FAQ ingestion metadata from S3. |
| FAQ ingestion | `faq_data_pipeline.py` | `will_process` flag | Processes only configured FAQ files marked for processing. |
| FAQ ingestion | `faq_data_pipeline.py` | `process_faq_excel(...)` | Passes collection definitions, file details, page URL, entity type, column mappings, header row, and dtype configuration to the Excel processor. |

### 4.5 Agent and MCP Functional View

| Flow stage | Component / repo | Level 2 method / capability | Functional role |
| --- | --- | --- | --- |
| Agent client request | Agent Gateway | Search, chat, administration, metadata, A2A routes | Routes agent-related requests to the appropriate gateway capability. |
| Prompt and fallback support | MCP Server | `fallback_messages_prompt` | Retrieves fallback/application messages by agent, message key, tenant, and language. |
| Prompt and fallback support | MCP Server | `language_detection_and_style` | Retrieves language and style prompt content by agent. |
| Prompt and fallback support | MCP Server | `compliance_and_behavior` | Retrieves compliance and behavior prompt content by agent. |
| MCP operations | MCP Server | Audit middleware | Records request/response audit events when enabled. |
| MCP operations | MCP Server | Redis cache middleware | Caches MCP responses when explicitly enabled. |
| Citation execution | Citation Agent | A2A server bootstrap | Runs the citation agent through the shared A2A server helper. |
| Citation execution | Citation Agent | `CitationQueryExecutor._run_agent` | Handles non-streaming summary shortcuts or invokes `CitationQueryAgent`. |
| Citation execution | Citation Agent | `CitationQueryExecutor._run_agent_sse` | Streams intermediate content and final response events. |
| Citation execution | Citation Agent | `CitationQueryAgent.ainvoke` / `CitationQueryAgent.astream` | Executes citation answer generation. |
| Citation execution | Citation Agent | `CitationService.get_summary` | Retrieves stored citation summaries for `summaryId` or `suggestionId` shortcuts. |

## 5. Repo-Wise Functional Requirements

### 5.1 Ordering Gateway

| Repo | Script / module | Method / function / endpoint | Functional requirement |
| --- | --- | --- | --- |
| `tfgenai-ordering-gateway` | `src/request-gateway/main.py` | `Settings(BaseSettings)` | The gateway shall load product discovery and checkout service URLs from Spring Cloud Config or environment variables. Startup shall fail if required endpoints are missing. |
| `tfgenai-ordering-gateway` | `src/request-gateway/main.py` | `Settings(BaseSettings)` | The gateway shall load an MCP server endpoint from Spring Cloud Config or environment variables, with localhost fallback. |
| `tfgenai-ordering-gateway` | `src/request-gateway/main.py` | `EncryptionConfig` / `EncryptionService` startup validation | The gateway shall validate encryption configuration at startup because checkout token/card-related data requires secure handling. |
| `tfgenai-ordering-gateway` | `src/request-gateway/main.py` | `load_discovery_profile(base_url)` | The gateway shall load `data/discovery_profile.json`, replace endpoint and merchant placeholders, and return a minimal fallback UCP profile only when the file is missing. |
| `tfgenai-ordering-gateway` | `src/request-gateway/main.py` | `lifespan(app)` | The gateway shall enter and exit ACP and UCP MCP lifespans when MCP apps are available. |
| `tfgenai-ordering-gateway` | `src/request-gateway/main.py` | `RequestLoggingMiddleware` | The gateway shall log requests and responses through the configured request repository. |
| `tfgenai-ordering-gateway` | `src/request-gateway/main.py` | `mcp_test_execute(request)` | The MCP test endpoint shall dispatch ACP and UCP tool methods and return JSON-RPC-style success or error payloads. |
| `tfgenai-ordering-gateway` | `src/request-gateway/main.py` | `mcp_test_execute(request)` | Missing ACP/UCP method parameters shall return invalid-params error code `-32602`; unknown methods shall return method-not-found error code `-32601`. |
| `tfgenai-ordering-gateway` | `src/product-discovery/main.py` | `_load_products_from_json()` | The product discovery service shall load static product data from the configured JSON path and reject missing or non-list payloads. |
| `tfgenai-ordering-gateway` | `src/product-discovery/main.py` | `_get_all_products_source(category, in_stock_only)` | Product listing shall support category filtering, in-stock filtering, and name sorting. |
| `tfgenai-ordering-gateway` | `src/product-discovery/main.py` | `_search_products_source(query, limit)` | Product search shall match lowercased query text across name, description, and catalog number; results shall be limited to the requested count. |
| `tfgenai-ordering-gateway` | `src/product-discovery/main.py` | `_get_product_source(catalog_number)` | Product lookup shall match catalog numbers case-insensitively. |
| `tfgenai-ordering-gateway` | `src/product-discovery/main.py` | `_map_db_product_to_merchant_item(product_data)` | Product data shall be mapped to merchant-center-compatible fields including id, title, description, link, image link, availability, price, brand, condition, product category, MPN, and identifier flag. |
| `tfgenai-ordering-gateway` | `src/product-discovery/main.py` | `_map_db_product_to_acp_item(product_data)` | Product data shall be mapped to ACP product discovery fields, with search eligibility true and checkout eligibility based on stock status. |
| `tfgenai-ordering-gateway` | `src/product-discovery/main.py` | `list_products` | The service shall return paginated product results with page and page-size validation. |
| `tfgenai-ordering-gateway` | `src/product-discovery/main.py` | `search_products_endpoint` | The service shall expose a required `q` search parameter and return paginated matching products. |
| `tfgenai-ordering-gateway` | `src/product-discovery/main.py` | `download_ucp_products(format)` | The service shall support `xml`, `tsv`, `json`, `merchant_center`, and `ucp` output formats and reject unsupported formats with HTTP 400. |
| `tfgenai-ordering-gateway` | `src/checkout/main.py` | `health_check()` | The checkout service shall expose a health endpoint returning service status, version, and timestamp. |
| `tfgenai-ordering-gateway` | `src/ops-ui/app/main.py` | `health_check()` | Ops UI health shall verify DB connectivity with `SELECT 1` and return healthy or degraded status. |

### 5.2 Search Vector API

| Repo | Script / module | Method / endpoint | Functional requirement |
| --- | --- | --- | --- |
| `tfgenai-search-vector-api` | `application.py` | Blueprint registration | The Flask service shall register vector, metadata, health, API integration, intent classification, base search, and feedback blueprints. |
| `tfgenai-search-vector-api` | `VectorSearchController.py` | `POST /resultswithscore` / `display_vector_match_with_score()` | The API shall accept `searchQuery`, create Azure OpenAI embeddings from Spring Cloud Config, search PGVector, and return catalog number, score, metadata, and page content. |
| `tfgenai-search-vector-api` | `VectorSearchController.py` | `POST /hybrid` / `vector_search_hybrid()` | The API shall run hybrid search against the configured or default collection using `VectorHybridSearchService.hybrid_search`. |
| `tfgenai-search-vector-api` | `VectorSearchController.py` | `POST /keyword` / `vector_search_keyword()` | The API shall run keyword search using `VectorHybridSearchService.keyword_search`. |
| `tfgenai-search-vector-api` | `IntentClassificationController.py` | `POST /classification` | The API shall classify intent from `searchQuery`, using request headers for country code and user id when present. |
| `tfgenai-search-vector-api` | `IntentClassificationController.py` | `POST /classification/v2` | The API shall classify intent and entities using `GPT_4_TURBO_MODEL` and `IntentEntityClassificationService.classify_intent_entity`. |

### 5.3 SQL Agent API

| Repo | Script / module | Method / endpoint | Functional requirement |
| --- | --- | --- | --- |
| `tfgenai-sqlagent-api` | `application.py` | `before_request()` | The API shall capture `X-Request-ID` from inbound headers into thread-local request context. |
| `tfgenai-sqlagent-api` | `application.py` | Blueprint registration | The Flask app shall register base SQL agent, feedback, and health check blueprints. |
| `tfgenai-sqlagent-api` | `GenAISQLAgentBaseController.py` | `POST /basic` / `perform_basic_search()` | The API shall read request JSON plus country, language, user id, and user name headers, instantiate `GenAISQExecutionService`, and call `perform_sql_gen_search()`. |
| `tfgenai-sqlagent-api` | `GenAISQLAgentBaseController.py` | Error handler path | Unhandled execution errors shall return JSON error payload with HTTP 500. |

### 5.4 Sentiment Service and UI

| Repo | Script / module | Method / function / endpoint | Functional requirement |
| --- | --- | --- | --- |
| `tfgenai-sentiments` | `application.py` | Swagger configuration | The sentiment service shall expose Swagger under `/api/store/genai/sentiments/apidocs` using dynamic host detection from `x-host-header`. |
| `tfgenai-sentiments` | `sentiments_controller.py` | `POST /details` / `find_sentiments_details()` | The API shall sanitize payloads, require `from_date` and `to_date`, parse dates, apply optional sentiment/username/SKU/pagegroup/timestamp filters, and return matching sentiment records. |
| `tfgenai-sentiments` | `sentiments_controller.py` | `POST /summary` / `find_sentiments_summary()` | The API shall sanitize payloads, require date range, apply optional username/SKU/pagegroup filters, and return sentiment label counts. |
| `tfgenai-sentiments` | `sentiments_controller.py` | `GET /process` / `process_sentiments()` | The API shall trigger `SentimentsProcessSerivice.sentiment_anlaysis()` and return the serialized result. |
| `tfgenai-sentiments` | `sentiments_controller.py` | `POST /download` / `download_records()` | The API shall fetch records by filters, flatten chat history into question and answer rows, format timestamps, and return a CSV file. |
| `tfgenai-sentiment-analysis-ui` | `src/components/Main/Main.tsx` | `useGetSummaryQuery` | The UI shall request summary data only when the date range or SKU/username filter is populated. |
| `tfgenai-sentiment-analysis-ui` | `src/components/Main/Main.tsx` | Filter handlers | The UI shall support date range, username, SKU, and page-group filters and reset selected sentiment when filters change. |
| `tfgenai-sentiment-analysis-ui` | `src/components/Main/Main.tsx` | `resetState()` | The UI shall reset date range, SKU, username, tenant, page group, and filter input values. |

### 5.5 Admin UI

| Repo | Script / module | Method / component | Functional requirement |
| --- | --- | --- | --- |
| `tfgenai-admin-ui` | `src/main.jsx` | `BrowserRouter` basename | The admin app shall use `/` as basename in development and `VITE_ADMIN_API_BASE` in other environments. |
| `tfgenai-admin-ui` | `src/App.jsx` | `getUiConfigOptions.initiate()` | After login, the app shall preload UI configuration options without polling. |
| `tfgenai-admin-ui` | `src/routes/AppRoutes.jsx` | Protected routes | Routes for prompts, application messages, agent mapping, preferences, security dashboard, document ingestion, cache management, and agent cards shall enforce permission checks. |
| `tfgenai-admin-ui` | `src/services/preferencesApiService.js` | `normalizeError()` | Preference API errors shall be translated into user-friendly messages for duplicates, validation errors, permission errors, missing resources, large requests, rate limits, server errors, network errors, and timeouts. |
| `tfgenai-admin-ui` | `src/services/preferencesApiService.js` | `getUiConfigOptions` | UI configuration options shall be fetched for `gateway-admin-ui-config` and transformed into tenants, page groups, languages, types, blue/green values, and default agent. |
| `tfgenai-admin-ui` | `src/services/preferencesApiService.js` | `getPreferences` | Preference search shall support agent, tenant, and trimmed text search parameters and tolerate known missing-table responses by returning an empty list. |
| `tfgenai-admin-ui` | `src/store/store.js` | `configureStore()` | Redux store shall register permissions/session state and API slices for prompts, agents, preferences, messages, mapping, security, ingestion, and back-office config. |

### 5.6 Data Pipeline

| Repo | Script / module | Method / process | Functional requirement |
| --- | --- | --- | --- |
| `tfgenai-data-pipeline` | `document_data_pipeline.py` | `document_type` dispatcher | The pipeline shall route document ingestion based on `document_type` environment value. |
| `tfgenai-data-pipeline` | `document_data_pipeline.py` | `process_brochures_data`, `process_manuals_data`, `process_gallery_data`, `process_posters_data`, `process_sds_data`, `process_coa_data`, `process_support_files_data` | Each supported document type shall call the corresponding processor with `s3_file_path`. |
| `tfgenai-data-pipeline` | `product_content_data_pipeline.py` | `ProductContentProcessorV2.process_product_content_data_v2()` | Product content ingestion shall process the provided S3 product content path together with `Entitlements/product_entitlements_v3.csv`. |
| `tfgenai-data-pipeline` | `faq_data_pipeline.py` | Metadata read | FAQ ingestion shall read `FAQ/genai-faq-dataload-metadata.json` from S3 and process only configured files where `will_process` is true. |
| `tfgenai-data-pipeline` | `faq_data_pipeline.py` | `process_faq_excel(...)` | FAQ ingestion shall pass collection definition, file name, page URL, entity type, custom id column, use columns, rename columns, header row, and dtype config to the Excel processor. |

### 5.7 Agent Builder

| Repo | Script / module | Method / process | Functional requirement |
| --- | --- | --- | --- |
| `tfgenai-agent-builder` | `README.md` | Generated agent contents | The builder shall scaffold LangGraph agents with Docker, Poetry, Kubernetes, CI/CD, optional Tavily, optional MCP tools, optional PostgreSQL memory, tests, pre-commit, YAML config, agent card, prompts, executor, and graph modules. |
| `tfgenai-agent-builder` | `.github/workflows/create-ai-agent.yml` | `workflow_dispatch` | The GitHub Action shall allow manual agent creation with project, repository, API path, Python, image, dependency, Tavily, and MCP inputs. |
| `tfgenai-agent-builder` | `.github/workflows/create-ai-agent.yml` | `issues` trigger | The workflow shall support issue-triggered generation when an issue is labeled `create-ai-agent` and contains parseable YAML input. |
| `tfgenai-agent-builder` | `.github/workflows/create-ai-agent.yml` | Target repository validation | Repository URL inputs shall be normalized and invalid target repository values shall be rejected. |
| `tfgenai-agent-builder` | `tfgenai-agent-templates/standalone_repository/copier.yml` | Template variables | Generated agents shall derive defaults for project slug, agent module name, deployment name, container image, repository URL, API context path, Python version, Docker base image, config library version, Poetry version, and optional MCP settings. |

### 5.8 MCP Server

| Repo | Script / module | Method / function | Functional requirement |
| --- | --- | --- | --- |
| `tfgenai-gateway-mcp-server` | `README.md` | `fallback_messages_prompt` | MCP tools shall retrieve fallback/application messages by agent and message key, with tenant and language defaults. |
| `tfgenai-gateway-mcp-server` | `README.md` | `language_detection_and_style` | MCP tools shall retrieve language/style prompt content by agent. |
| `tfgenai-gateway-mcp-server` | `README.md` | `compliance_and_behavior` | MCP tools shall retrieve compliance and behavior prompt content by agent. |
| `tfgenai-gateway-mcp-server` | `server.py` | `_env_enabled(name, default)` | Boolean feature flags shall treat unset values as defaults and treat `0`, `false`, `no`, and `off` as disabled. |
| `tfgenai-gateway-mcp-server` | `server.py` | `_build_audit_middleware()` | Audit middleware shall be enabled by default unless disabled with `MCP_ENABLE_AUDIT_MIDDLEWARE`; startup failures shall log a warning rather than stopping server creation. |
| `tfgenai-gateway-mcp-server` | `server.py` | `_build_cache_middleware()` | Redis response cache middleware shall be disabled by default and enabled only when `MCP_ENABLE_CACHE_MIDDLEWARE` is true. |
| `tfgenai-gateway-mcp-server` | `server.py` | `create_app()` | MCP app creation shall include auth provider, error middleware, rate limit middleware, concurrency limit middleware, audit middleware, cache middleware, and request/response logging. |

### 5.9 Citation Agent

| Repo | Script / module | Method / function | Functional requirement |
| --- | --- | --- | --- |
| `tfgenai-citation` | `README.md` | A2A endpoint | The citation agent shall expose an Agent-to-Agent interface under the configured context path. |
| `tfgenai-citation` | `app/resources/agent_card.yaml` | `citation-insights` skill | The agent shall answer publication/literature-based questions about Thermo Fisher products and shall not be used for pricing, availability, general product usage, compatibility, workflow guidance, or technique suitability. |
| `tfgenai-citation` | `application.py` | `main(host, port, agent_card_path)` | The app shall start through the shared `run_server_main` helper and accept host, port, and agent card path CLI options. |
| `tfgenai-citation` | `agent_executor.py` | `_run_agent(agent_request)` | The executor shall detect `summaryId` or `suggestionId` in agent context and return a saved citation summary without invoking the agent graph. |
| `tfgenai-citation` | `agent_executor.py` | `_run_agent(agent_request)` | When no summary shortcut is present, the executor shall emit reasoning start/completion events, initialize `CitationQueryAgent`, invoke it, and return answer HTML with sources. |
| `tfgenai-citation` | `agent_executor.py` | `_run_agent_sse(agent_request)` | Streaming execution shall yield intermediate content events and a final completed `AgentResponse`; source events shall be collected separately. |
| `tfgenai-citation` | `agent_executor.py` | Exception handling | Execution errors shall return an `AgentError`; streaming errors shall yield a completed error event with a generic retry message. |

### 5.10 Agent Gateway

| Repo | Script / module | Method / blueprint | Functional requirement |
| --- | --- | --- | --- |
| `tfgenai-agent-gateway` | `application.py` | Swagger configuration | The gateway shall expose Swagger under `/api/store/genai/agent/gateway/search/apidocs` with dynamic host detection from `x-host-header`. |
| `tfgenai-agent-gateway` | `application.py` | `genai_agent_gateway_search_controller` | The gateway shall register search functionality under `/api/store/genai/agent/gateway/search`. |
| `tfgenai-agent-gateway` | `application.py` | `health_check_controller` | The gateway shall register health checks under `/api/store/genai/agent/gateway`. |
| `tfgenai-agent-gateway` | `application.py` | `user_chat_message_controller` | The gateway shall register user chat message functionality under `/api/store/genai/agent/gateway/chat`. |
| `tfgenai-agent-gateway` | `application.py` | `agent_administration_controller` | The gateway shall register agent administration under `/api/store/genai/agent/gateway/administration`. |
| `tfgenai-agent-gateway` | `application.py` | `agents_controller` | The gateway shall register agent metadata under `/api/store/genai/agent/gateway/`. |
| `tfgenai-agent-gateway` | `application.py` | `genai_agent_gateway_search_a2a_controller` | The gateway shall register A2A search functionality under `/api/store/genai/agent/gateway/search/a2a`. |

## 6. API and Integration Requirements

| Domain | API / endpoint pattern | Required behavior |
| --- | --- | --- |
| Ordering gateway | `/api/store/genai/ordering/gateway/v1/*` | Route UCP, ACP, REST, product, order, identity-linking, MCP, and health requests through the gateway service. |
| Product discovery | `/api/store/genai/ordering/products/v1/*` | List, search, retrieve, paginate, map, and download products in supported commerce/vendor formats. |
| Checkout | `/api/store/genai/ordering/checkout/v1/*` | Serve checkout API/UI routes and expose service health. |
| Ops UI | `/api/store/genai/ordering/ops/v1/*` | Show dashboard, orders, sessions, requests, errors, product discovery, simulator, and DB health. |
| Search vector | `/api/store/genai/search/vector/*` | Support vector scoring, hybrid search, keyword search, and related search-vector operations. |
| Intent classification | `/api/store/genai/search/intent/*` | Classify intent and intent/entity combinations using configured model services. |
| SQL agent | `/api/store/genai/sql/agent/basic` | Convert inbound request JSON and headers into a SQL agent execution request. |
| Sentiments | `/api/store/genai/sentiments/details`, `/summary`, `/process`, `/download` | Support detail filtering, summary counts, processing trigger, and CSV export. |
| Agent gateway | `/api/store/genai/agent/gateway/*` | Serve agent search, chat, administration, metadata, health, and A2A integration. |
| MCP gateway | MCP server tools | Expose prompts, fallback messages, and agent invocation tools with rate limiting, concurrency controls, audit, and optional cache. |
| Citation agent | `/api/store/genai/agents/citations/v1`, A2A endpoint | Serve citation-specific agent capability with non-streaming and streaming execution. |

## 7. Data, Configuration, and Analytics

| Data / config object | Source evidence | Functional requirement |
| --- | --- | --- |
| Spring Cloud Config endpoint values | Ordering gateway, vector search, MCP server | Runtime endpoints, model keys, Redis config, and service URLs shall be loaded from Spring Cloud Config where supported. |
| Environment variables | Ordering gateway, product discovery, MCP, Flask/FastAPI services | Services shall support environment-based overrides for endpoints, file paths, debug mode, middleware flags, and runtime options. |
| PostgreSQL | Ordering gateway repositories, ops UI DB check, vector APIs, sentiment repository evidence | Request logs, checkout/order/session records, sentiment data, and vector data dependencies shall be treated as critical backend dependencies where used. |
| PGVector collection | Search vector controller | Vector search shall use a configured collection and return score-bearing results. |
| Static JSON product catalog | Product discovery service | Product data may be loaded from local/static JSON when configured, especially for mock/product discovery flows. |
| S3 ingestion metadata | FAQ and document pipeline scripts | Ingestion scripts shall read configured S3 paths and metadata before processing FAQ, document, and product content data. |
| Application messages and prompts | MCP README, admin UI preference services, citation executor | Prompt and fallback message content shall be managed centrally and retrieved per agent, tenant, language, and message key where supported. |
| Sentiment filters | Sentiment service and UI | Sentiment analytics shall support date, username, SKU, page group, sentiment label, score, and conversation timestamp filters where present in service logic. |

### 7.1 Metrics and Reporting Events

| Metric / event | Source | Recommended use |
| --- | --- | --- |
| Request id | SQL agent `X-Request-ID`; gateway logging | Correlate user request, service logs, generated answer, and backend actions. |
| Request/response log | Ordering gateway middleware | Audit commerce/checkout interactions and troubleshoot failed flows. |
| Health status | Ordering, checkout, ops UI, agent gateway, SQL, sentiments | Monitor service availability and degraded database states. |
| Sentiment counts by label | Sentiments summary endpoint | Track user experience patterns across page groups, SKUs, and time windows. |
| Sentiment detail export | Sentiments download endpoint | Support operational review and offline analysis. |
| Reasoning start/completion | Citation executor | Trace agent progress and answer generation lifecycle. |
| Vector result score | Search vector score endpoint | Evaluate retrieval quality and ranking confidence. |
| MCP rate/concurrency events | MCP server middleware | Detect overload, abusive traffic, and capacity constraints. |

## 8. Core Workflows and Acceptance Criteria

### 8.1 Search and Retrieval Workflow

| Step | Functional flow | Acceptance criteria |
| --- | --- | --- |
| 1 | Client submits search query to vector or hybrid endpoint. | API accepts `searchQuery` and returns structured JSON. |
| 2 | Controller loads embedding/model/vector DB configuration. | Missing critical configuration fails visibly rather than producing silent empty results. |
| 3 | Service executes vector, hybrid, or keyword retrieval. | Results include relevant data fields supported by the endpoint, such as score, metadata, page content, and catalog number where implemented. |
| 4 | Intent classification can be called separately. | Country code and user id headers are handled with defaults. |

### 8.2 Agent Execution Workflow

| Step | Functional flow | Acceptance criteria |
| --- | --- | --- |
| 1 | Client routes request to agent gateway or A2A endpoint. | Gateway exposes search, chat, administration, metadata, and A2A routes. |
| 2 | Agent or MCP service retrieves prompts and fallback messages. | Prompt retrieval supports agent-specific and tenant/language-aware defaults where implemented. |
| 3 | Agent executor runs graph or shortcut logic. | Citation agent returns saved summaries when `summaryId` or `suggestionId` exists and invokes graph only otherwise. |
| 4 | Response is returned or streamed. | Non-streaming response includes answer and sources where available; streaming sends intermediate chunks and final completion. |

### 8.3 Commerce Ordering Workflow

| Step | Functional flow | Acceptance criteria |
| --- | --- | --- |
| 1 | Client sends commerce request to ordering gateway. | Request reaches standard `/api/store/genai/ordering/{service}/v1/{endpoint}` path. |
| 2 | Gateway validates config and routes to UCP, ACP, product, checkout, or order services. | Missing required endpoints are caught at startup. |
| 3 | Product discovery returns product list/search/get/download output. | Results support pagination, filtering, mapping, and supported output formats. |
| 4 | Checkout and order services process session/order requests. | Health and operation traces are visible through service health and ops UI. |

### 8.4 Sentiment Analytics Workflow

| Step | Functional flow | Acceptance criteria |
| --- | --- | --- |
| 1 | UI collects date, username, SKU, and page group filters. | UI resets selected sentiment when filters change. |
| 2 | UI calls summary API when required filters are available. | Empty or error states are visible to the user. |
| 3 | Service sanitizes payload and applies filters. | Missing date fields produce validation behavior; optional filters are applied only when provided. |
| 4 | Detail or CSV download returns records. | CSV export flattens chat history into question and answer rows. |

### 8.5 Data Ingestion Workflow

| Step | Functional flow | Acceptance criteria |
| --- | --- | --- |
| 1 | Pipeline receives document type or configured metadata. | Unsupported or missing source inputs are not treated as successful processing. |
| 2 | Pipeline chooses processor based on document type or metadata entry. | Only `will_process` FAQ files are processed. |
| 3 | Pipeline sends content, entitlements, or FAQ metadata to processor. | Processor receives S3 paths and column/dtype configuration from metadata. |
| 4 | Downstream search/agent systems consume processed content. | Downstream dependency is documented as a validation item unless exact handoff code is reviewed. |

## 9. Operations and Support

| Area | Requirement |
| --- | --- |
| Health checks | Each service shall expose health endpoints or startup logs sufficient for platform monitoring. |
| Configuration validation | Services that require endpoints, encryption, DB connections, model keys, or S3 paths shall fail early or return degraded states instead of silently continuing. |
| Logging | Request IDs, request/response traces, errors, reasoning events, and pipeline inputs shall be logged in a way that supports incident analysis. |
| Error handling | APIs shall return structured error responses for validation errors, unknown MCP methods, missing products/files, and internal exceptions. |
| Swagger/API docs | Flask/FastAPI APIs that already expose Swagger shall keep routes aligned with deployed base paths. |
| Security | Admin UI protected routes shall enforce permissions. MCP and ordering gateway encryption/audit/cache controls shall be validated in deployment configuration. |
| Data retention | Retention requirements for request logs, sentiments, audit middleware records, downloaded CSV files, and vector collections need product/security confirmation. |
| Support playbooks | Support teams need runbooks for Spring Cloud Config failures, PGVector availability, S3 ingestion failures, Redis cache issues, and checkout/order failures. |

## 10. Risks, Constraints, and Improvements

| Type | Observation | Impact | Suggested improvement |
| --- | --- | --- | --- |
| Evidence constraint | Several repos returned generic README content or were not deeply reviewable from accessible files. | Functional coverage may be incomplete for those repos. | Run a repo-owner review and fill validation gaps before using this PRD as final implementation scope. |
| Architecture clarity | Gateway, agent, MCP, data pipeline, search, and UI capabilities span many repos. | New developers may struggle to locate the correct service boundary. | Maintain a central architecture index with owner, runtime, endpoint base path, data store, and escalation contact per repo. |
| Config dependency | Several services rely on Spring Cloud Config and environment variables. | Missing config may cause startup failure or runtime outages. | Add explicit config reference tables per environment and automated config validation. |
| Search quality | Vector and hybrid search depend on embedding model, collection name, and data freshness. | Retrieval quality can degrade without visible release change. | Track collection version, ingest timestamp, embedding model, and retrieval metrics per response. |
| Sentiment export | Sentiment download writes a timestamped CSV in the working directory before sending. | Local file buildup or storage permissions can become operational issues. | Stream CSV directly or write to a managed temporary location with cleanup. |
| Agent generation | Agent builder derives repository URL and other defaults from template variables. | Incorrect defaults can generate confusing project paths. | Validate generated repository URL and API context path in workflow output before committing generated code. |
| Archived repos | Archived repos may still appear in search results. | Teams may accidentally treat old implementations as current. | Mark archived repos in the portfolio registry and exclude them from current architecture diagrams unless used for reference. |
| Table ownership | Admin UI route permissions reference many domains. | Missing permission mapping can block users or overexpose features. | Add a role-to-route permission matrix to product documentation. |

## 11. Validation Report

| Validation item | Status | Evidence / note |
| --- | --- | --- |
| Multi-repo search used | Completed with limitations | Repositories matching `tfgenai` were inventoried and grouped by evidence depth. |
| Method-level details captured | Completed for reviewed repos | Ordering, search vector, SQL agent, sentiments, sentiment UI, admin UI, data pipeline, agent builder, MCP server, citation, and agent gateway include script/method-level rows. |
| Business facts avoided where unsupported | Completed | Ownership, SLAs, deployment cadence, and unreviewed implementation behavior are not invented. |
| Tables used where applicable | Completed | Inventory, requirements, APIs, data, metrics, workflows, risks, and validation are table-based. |
| Architecture diagrams included | Completed | Portfolio, ordering, search/vector, data pipeline, and agent/MCP diagrams are included. |
| Two-level functional detail | Completed where evidence exists | Repo -> script/module -> method/endpoint mapping is provided for reviewed repos. |
| Limited-evidence repos marked | Completed | Generic/minimal/archived repos are identified as validation pending or archived. |
| Template styling followed | Completed within local generation limits | The document uses title, metadata table, TOC placeholder, major PRD sections, native Word tables, and validation note consistent with the referenced PRD structure. |

## 12. Open Questions

| Question | Owner needed |
| --- | --- |
| Which `tfgenai` repositories are officially in current production scope versus experimental, archived, or template-only? | Product / engineering leadership |
| What is the authoritative owner for each repo and service? | Engineering leadership |
| Which environments and base paths are considered active for each API? | Platform / DevOps |
| What are the SLAs for agent gateway, search vector, ordering gateway, SQL agent, and sentiment APIs? | Product / operations |
| What retention policy applies to request logs, reasoning events, sentiment exports, audit middleware records, and generated CSV files? | Security / compliance |
| Which vector collections, embedding models, and data freshness windows are approved for production? | Search / data engineering |
| Are the limited-evidence repos still maintained and required for the GenAI program? | Repo owners |

## 13. Source Evidence

| Source | Reviewed artifacts |
| --- | --- |
| `thermofisher/tfgenai-ordering-gateway` | `README.md`, `src/request-gateway/main.py`, `src/product-discovery/main.py`, `src/checkout/main.py`, `src/ops-ui/app/main.py` |
| `thermofisher/tfgenai-search-vector-api` | `README.md`, `application.py`, `VectorSearchController.py`, `IntentClassificationController.py` |
| `thermofisher/tfgenai-sqlagent-api` | `README.md`, `application.py`, `GenAISQLAgentBaseController.py` |
| `thermofisher/tfgenai-sentiments` | `README.md`, `application.py`, `sentiments_controller.py` |
| `thermofisher/tfgenai-sentiment-analysis-ui` | `package.json`, `src/App.tsx`, `src/components/Main/Main.tsx` |
| `thermofisher/tfgenai-admin-ui` | `package.json`, `src/main.jsx`, `src/App.jsx`, `src/routes/AppRoutes.jsx`, `src/services/preferencesApiService.js`, `src/store/store.js` |
| `thermofisher/tfgenai-data-pipeline` | `README.md`, `document_data_pipeline.py`, `product_content_data_pipeline.py`, `faq_data_pipeline.py` |
| `thermofisher/tfgenai-agent-builder` | `README.md`, `.github/workflows/create-ai-agent.yml`, `tfgenai-agent-templates/standalone_repository/copier.yml` |
| `thermofisher/tfgenai-gateway-mcp-server` | `README.md`, `server.py` |
| `thermofisher/tfgenai-citation` | `README.md`, `application.py`, `app/resources/agent_card.yaml`, `pyproject.toml`, `app/thermofisher/citation_agent/executor/agent_executor.py` |
| `thermofisher/tfgenai-agent-gateway` | `application.py` |
