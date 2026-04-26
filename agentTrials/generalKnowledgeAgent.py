import asyncio
import datetime
import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langgraph.prebuilt import create_react_agent


load_dotenv()


def get_llm() -> ChatOllama:
    return ChatOllama(
        model=os.getenv("OLLAMA_MODEL", "llama3"),
        temperature=0.3,
    )


def get_server_config() -> dict:
    server_path = Path(__file__).with_name("gk_news_mcp_server.py").resolve()
    return {
        "gk_news": {
            "transport": "stdio",
            "command": sys.executable,
            "args": [str(server_path)],
        }
    }


async def load_mcp_tools():
    try:
        from langchain_mcp_adapters.client import MultiServerMCPClient
    except ImportError as exc:
        raise RuntimeError(
            "Missing MCP adapter dependency. Install it with:\n"
            "pip install langchain-mcp-adapters mcp"
        ) from exc

    client = MultiServerMCPClient(get_server_config())
    return await client.get_tools()


def extract_final_answer(result: dict) -> str:
    for message in reversed(result.get("messages", [])):
        if getattr(message, "type", "") == "ai":
            content = getattr(message, "content", "")
            if isinstance(content, str):
                return content
            if isinstance(content, list):
                text_parts = [
                    block.get("text", "")
                    for block in content
                    if isinstance(block, dict) and block.get("type") == "text"
                ]
                return "\n".join(part for part in text_parts if part).strip()
    return "No final AI response was produced."


async def main():
    tools = await load_mcp_tools()
    agent = create_react_agent(
        model=get_llm(),
        tools=tools,
        prompt=(
            "You are a general knowledge quiz generator. "
            "Always use the available MCP news tool to gather current topics before writing questions. "
            "Create 5 factual general knowledge questions with answers. "
            "Each question must come from a different recent topic. "
            "Keep each question and answer short and clear."
        ),
    )

    today = datetime.date.today().isoformat()
    user_request = (
        f"Today's date is {today}. "
        "Use the MCP news tool to get recent headlines, choose 5 diverse topics, "
        "and return exactly 5 numbered general knowledge questions with their answers."
    )

    result = await agent.ainvoke(
        {"messages": [{"role": "user", "content": user_request}]}
    )

    print("\nDaily GK Questions via MCP + LangGraph:\n")
    print(extract_final_answer(result))


if __name__ == "__main__":
    asyncio.run(main())
