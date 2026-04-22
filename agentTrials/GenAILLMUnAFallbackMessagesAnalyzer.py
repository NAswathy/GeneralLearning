#Fallback messages analyzer

# llm_unable_agent.py
import argparse
import csv
import json
import os
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Dict, List, TypedDict

from langchain_core.messages import HumanMessage, SystemMessage
from langchain_ollama import ChatOllama
from langgraph.graph import START, END, StateGraph


TARGET_FALLBACK= "llm.unable.to.answer"
REQUIRED_COLUMNS = {
    "chat_id",
    "username",
    "sku",
    "fallback_type",
    "intents",
    "pagegroup",
    "created_ts",
    "response_status",
    "Q&A",
}


class AgentState(TypedDict, total=False):
    csv_path: str
    top_n: int
    model: str
    summary: Dict[str, Any]
    report: str


def extract_question(qa_text: str) -> str:
    if not qa_text:
        return ""
    match = re.search(r"Question:\s*(.*?)\s*\|\s*Answer:", qa_text, flags=re.I | re.S)
    if match:
        return re.sub(r"\s+", " ", match.group(1)).strip()
    return re.sub(r"\s+", " ", qa_text).strip()[:220]


def analyze_csv(csv_path: str, top_n: int = 5) -> Dict[str, Any]:
    path = Path(csv_path)
    if not path.exists():
        raise FileNotFoundError(f"CSV not found: {csv_path}")

    total_rows = 0
    fallback_rows = 0

    sku_counts = Counter()
    intent_counts = Counter()
    pagegroup_counts = Counter()
    status_counts = Counter()
    examples_by_sku = defaultdict(list)

    with path.open("r", newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        missing = REQUIRED_COLUMNS - set(reader.fieldnames or [])
        if missing:
            raise ValueError(f"Missing required columns: {sorted(missing)}")

        for row in reader:
            total_rows += 1
            if (row.get("fallback_type") or "").strip() != TARGET_FALLBACK:
                continue

            fallback_rows += 1

            sku = (row.get("sku") or "").strip() or "<blank>"
            intent = (row.get("intents") or "").strip() or "<blank>"
            pagegroup = (row.get("pagegroup") or "").strip() or "<blank>"
            status = (row.get("response_status") or "").strip() or "<blank>"

            sku_counts[sku] += 1
            intent_counts[intent] += 1
            pagegroup_counts[pagegroup] += 1
            status_counts[status] += 1

            if len(examples_by_sku[sku]) < 2:
                examples_by_sku[sku].append(extract_question(row.get("Q&A", "")))

    top_skus = []
    for sku, count in sku_counts.most_common(top_n):
        top_skus.append(
            {
                "sku": sku,
                "count": count,
                "share_of_fallbacks": round(count / fallback_rows, 4) if fallback_rows else 0.0,
                "example_questions": [q for q in examples_by_sku.get(sku, []) if q],
            }
        )

    summary = {
        "file": str(path.name),
        "total_rows": total_rows,
        "fallback_rows": fallback_rows,
        "fallback_rate": round(fallback_rows / total_rows, 4) if total_rows else 0.0,
        "target_fallback": TARGET_FALLBACK,
        "top_skus": top_skus,
        "top_intents": [
            {"intent": intent, "count": count, "share": round(count / fallback_rows, 4) if fallback_rows else 0.0}
            for intent, count in intent_counts.most_common(10)
        ],
        "top_pagegroups": [
            {"pagegroup": pg, "count": count, "share": round(count / fallback_rows, 4) if fallback_rows else 0.0}
            for pg, count in pagegroup_counts.most_common(10)
        ],
        "response_status_breakdown": dict(status_counts),
    }
    return summary


def build_llm(model: str) -> ChatOllama:
    return ChatOllama(
        model=model,
        temperature=0,
    )


def load_and_analyze_node(state: AgentState) -> Dict[str, Any]:
    summary = analyze_csv(state["csv_path"], state.get("top_n", 5))
    return {"summary": summary}


def synthesize_insights_node(state: AgentState) -> Dict[str, Any]:
    summary = state["summary"]
    llm = build_llm(state.get("model", os.getenv("OLLAMA_MODEL", "llama3.1")))

    prompt = [
        SystemMessage(
            content=(
                "You are a senior product analytics assistant. "
                "Use only the supplied JSON summary. "
                "Do not invent metrics, counts, or causes. "
                "Write a concise but useful analysis for product and content owners."
            )
        ),
        HumanMessage(
            content=(
                "Analyze the following CSV summary for llm.unable.to.answer fallback messages.\n\n"
                "Return markdown with these sections:\n"
                "1. Executive summary\n"
                "2. Worst performing SKUs (use the exact top_skus data)\n"
                "3. Intent patterns\n"
                "4. Pagegroup patterns\n"
                "5. Recommended actions\n\n"
                "Be specific. Mention the top 5 SKUs and explain what the concentration suggests.\n\n"
                f"JSON SUMMARY:\n{json.dumps(summary, indent=2, ensure_ascii=False)}"
            )
        ),
    ]

    report = llm.invoke(prompt).content
    return {"report": report}


def build_graph():
    graph = StateGraph(AgentState)
    graph.add_node("load_and_analyze", load_and_analyze_node)
    graph.add_node("synthesize_insights", synthesize_insights_node)

    graph.add_edge(START, "load_and_analyze")
    graph.add_edge("load_and_analyze", "synthesize_insights")
    graph.add_edge("synthesize_insights", END)

    return graph.compile()


def main():
    parser = argparse.ArgumentParser(description="Analyze llm.unable.to.answer fallbacks with LangGraph + Ollama")
    parser.add_argument("--csv", required=True, help="Path to the input CSV")
    parser.add_argument("--top_n", type=int, default=5, help="How many worst SKUs to return")
    parser.add_argument("--model", default=os.getenv("OLLAMA_MODEL", "llama3.1"), help="Ollama model name")
    parser.add_argument("--fallback_type", type=str, default="llm.unable.to.answer", help="any one fallback type to be anaylzed, default is llm.unable.to.answer") 
    parser.add_argument("--out", default="", help="Optional output markdown file")
    args = parser.parse_args()

    app = build_graph()
    result = app.invoke(
        {
            "csv_path": args.csv,
            "top_n": args.top_n,
            "model": args.model,
            "fallback_type": args.fallback_type
        }
    )

    print(result["report"])

    if args.out:
        Path(args.out).write_text(result["report"], encoding="utf-8")


if __name__ == "__main__":
    main()