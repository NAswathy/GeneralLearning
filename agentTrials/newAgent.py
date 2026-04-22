# daily_ai_health_news 
import os
import json
import calendar
from datetime import datetime, timezone
from typing import TypedDict, List, Dict, Any
from urllib.parse import quote_plus

import feedparser
from langgraph.graph import StateGraph, END
#from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv
from langchain_community.chat_models import ChatOllama
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
print(api_key)

QUERIES = [
    "AI healthcare breakthrough",
    "medical AI latest advancement",
    "healthcare AI FDA approval",
    "AI genomics healthcare",
    "AI drug discovery healthcare",
]

RSS_BASE = "https://news.google.com/rss/search?q={q}&hl=en-IN&gl=IN&ceid=IN:en"


class NewsState(TypedDict, total=False):
    candidates: List[Dict[str, Any]]
    top_items: List[Dict[str, Any]]
    report: str


def entry_ts(entry: Any) -> int:
    parsed = getattr(entry, "published_parsed", None) or getattr(entry, "updated_parsed", None)
    if parsed:
        return calendar.timegm(parsed)
    return 0


def fetch_rss(query: str, max_items: int = 10) -> List[Dict[str, Any]]:
    url = RSS_BASE.format(q=quote_plus(query))
    feed = feedparser.parse(url)

    items = []
    for entry in feed.entries[:max_items]:
        published = getattr(entry, "published", "") or getattr(entry, "updated", "")
        items.append(
            {
                "title": getattr(entry, "title", "").strip(),
                "link": getattr(entry, "link", "").strip(),
                "source": getattr(getattr(entry, "source", {}), "title", "") if hasattr(entry, "source") else "",
                "published": published,
                "ts": entry_ts(entry),
                "summary": getattr(entry, "summary", "").strip(),
                "query": query,
            }
        )
    return items


def fetch_news(state: NewsState) -> NewsState:
    all_items: List[Dict[str, Any]] = []
    for query in QUERIES:
        all_items.extend(fetch_rss(query))
    return {"candidates": all_items}


def is_relevant(item: Dict[str, Any]) -> bool:
    text = f"{item.get('title', '')} {item.get('summary', '')}".lower()
    ai_terms = ["ai", "artificial intelligence", "machine learning", "ml", "generative ai"]
    health_terms = ["health", "healthcare", "medical", "medicine", "clinical", "hospital", "drug", "patient", "radiology","genomics", "pharma", "biotech"]
    return any(t in text for t in ai_terms) and any(t in text for t in health_terms)


def dedupe_and_select(state: NewsState) -> NewsState:
    candidates = state.get("candidates", [])

    seen = set()
    unique: List[Dict[str, Any]] = []
    for item in candidates:
        if not is_relevant(item):
            continue

        key = item.get("link") or item.get("title")
        if not key or key in seen:
            continue
        seen.add(key)
        unique.append(item)

    unique.sort(key=lambda x: x.get("ts", 0), reverse=True)
    top_five = unique[:5]
    return {"top_items": top_five}


def summarize(state: NewsState) -> NewsState:
    top_items = state.get("top_items", [])
    # llm = ChatOpenAI(
    #     model=os.getenv("OPENAI_MODEL", "gpt-4.1-mini"),
    #     temperature=0.4,
    # )
    llm = ChatOllama(
    model="llama3",
    temperature=0.4
)
    

    payload = json.dumps(top_items, ensure_ascii=False, indent=2)

    messages = [
        SystemMessage(
            content=(
                "You are a news analyst. Use only the provided items. "
                "Create a concise daily briefing focused on the 5 latest AI advancements in healthcare. "
                "For each item, include: title, source, date, what happened, and why it matters and the url. "
                "Do not invent facts."
            )
        ),
        HumanMessage(
            content=(
                "Turn these news results into a polished briefing:\n\n"
                f"{payload}\n\n"
                "Return markdown with exactly 5 items if 5 are available; otherwise use all available items."
            )
        ),
    ]

    report = llm.invoke(messages).content
    return {"report": report}


def build_graph():
    graph = StateGraph(NewsState)
    graph.add_node("fetch_news", fetch_news)
    graph.add_node("dedupe_and_select", dedupe_and_select)
    graph.add_node("summarize", summarize)

    graph.set_entry_point("fetch_news")
    graph.add_edge("fetch_news", "dedupe_and_select")
    graph.add_edge("dedupe_and_select", "summarize")
    graph.add_edge("summarize", END)

    return graph.compile()


if __name__ == "__main__":
    app = build_graph()
    result = app.invoke({})
    print(result["report"])