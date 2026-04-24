import random
import datetime
import feedparser
from typing import TypedDict, List

from langgraph.graph import StateGraph, START, END
from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage


# -------- STATE --------
class GKState(TypedDict, total=False):
    topics: List[str]
    selected_topics: List[str]
    questions: str


# -------- LLM --------
def get_llm():
    return ChatOllama(
        model="llama3",
        temperature=0.3
    )


# -------- STEP 1: FETCH TOPICS FROM INTERNET --------
def fetch_topics(state: GKState) -> GKState:
    feed = feedparser.parse("https://news.google.com/rss?hl=en-IN&gl=IN&ceid=IN:en")

    topics = []
    for entry in feed.entries[:20]:
        title = entry.title
        topics.append(title)

    return {"topics": topics}


# -------- STEP 2: SELECT DIVERSE TOPICS --------
def select_topics(state: GKState) -> GKState:
    topics = state["topics"]

    # Shuffle and pick 5 diverse topics
    random.shuffle(topics)
    selected = topics[:5]

    return {"selected_topics": selected}


# -------- STEP 3: GENERATE QUESTIONS --------
def generate_questions(state: GKState) -> GKState:
    llm = get_llm()
    topics = state["selected_topics"]

    today = datetime.date.today().isoformat()

    prompt = [
        SystemMessage(
            content=(
                "You are a quiz generator. Create general knowledge questions. "
                "Each question must be factual, short, and from a different topic. "
                "Do not repeat topics. Focus on current events and recent advancements. "
                "Topics to consider include: current affairs, eminent personalities, scientific discoveries, historical events, etc."
            )
        ),
        HumanMessage(
            content=(
                f"Today's date: {today}\n\n"
                f"Generate 5 general knowledge questions based on these topics:\n{topics}\n\n"
                "Return only numbered questions and the respective answers."
            )
        )
    ]

    response = llm.invoke(prompt).content
    return {"questions": response}


# -------- BUILD GRAPH --------
def build_graph():
    graph = StateGraph(GKState)

    graph.add_node("fetch_topics", fetch_topics)
    graph.add_node("select_topics", select_topics)
    graph.add_node("generate_questions", generate_questions)

    graph.add_edge(START, "fetch_topics")
    graph.add_edge("fetch_topics", "select_topics")
    graph.add_edge("select_topics", "generate_questions")
    graph.add_edge("generate_questions", END)

    return graph.compile()


# -------- RUN --------
if __name__ == "__main__":
    app = build_graph()
    result = app.invoke({})

    print("\n🧠 Daily GK Questions:\n")
    print(result["questions"])