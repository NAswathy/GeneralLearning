# TFGenAI Product Information V2 Summary

## What It Is

`tfgenai-product-information-v2` is a private Thermo Fisher GenAI repository for a Product Information agent. Its purpose is to answer Thermo Fisher product-related questions, especially around product details, discovery, documents, pricing, availability, alternatives, accessories, comparisons, support, and troubleshooting.

## Verified Repo Details

- Repo: `thermofisher/tfgenai-product-information-v2`
- Default branch: `master`
- Status: not archived
- Main language/runtime: Python 3.12
- Package name: `product-information-v2`
- Description from `pyproject.toml`: LangGraph agent for Thermo Fisher product-related questions
- Entry point: `application.py`
- Agent configuration: `app/resources/agent_card.yaml`

## How It Works

The app starts a Starlette/A2A-compatible agent server through a shared internal library: `tfgenai_agent_config_lib`. The service loads its agent behavior from `agent_card.yaml`.

The exposed agent URL is:

`/api/store/genai/agents/product-information/v2`

It supports:

- JSON
- Plain text
- Text/event-stream
- HTML output
- Streaming responses
- No push notifications

## Main Capabilities

The agent is configured for these business and user intents:

- Product details: specifications, attributes, packaging, storage, regulatory/compliance information
- Product search and discovery: finding Thermo Fisher products by name, category, use case, or attributes
- Product documentation: SDS, certificates, manuals, brochures, and spec sheets
- Pricing and promotions
- Availability, stock, lead time, and orderability
- Alternates, substitutes, and similar products
- Accessories, consumables, add-ons, and replacement parts
- Product comparison
- Product support and escalation
- Product troubleshooting, setup, operation, maintenance, and calibration
- Product documentation and protocol content search

## Important Behavior

If a catalog, SKU, or page product is provided, the agent uses it for contextual product questions such as pricing, availability, documents, specifications, accessories, alternatives, and support.

If the user asks about a different product need, the agent should route based on the query instead of forcing the current page SKU.

It explicitly does not support unrelated non-product chatter or general commerce requests outside Thermo Fisher product and support workflows.

## Tech Stack Observed

- Python 3.12
- Poetry
- LangGraph prebuilt
- OpenAI ChatKit
- Internal `tfgenai_agent_config_lib`
- Starlette/A2A application bootstrap
- Dockerized service exposing port `80`

## Limitations

I could verify `README.md`, `pyproject.toml`, `Dockerfile`, `application.py`, and `app/resources/agent_card.yaml`. The connector did not expose a full directory tree, and repo code search returned no results, so this is a source-backed summary of the accessible files, not a full code audit.
