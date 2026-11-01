from agent_framework_gemini import GeminiChatClient
from agent_framework import Agent, InMemoryHistoryProvider
from tools import fetch_url, read_feature_file

async def gemini_agent() -> Agent:
    """Assembles and returns a pre-configured QA Validation Agent."""

    agent = Agent(
        client=GeminiChatClient(),
        name="QA_Validation_Expert",
        instructions=(
            "You are a strict QA automation engineer. Your goal is to run API validations based on feature specifications. "
            "Analyze data payloads carefully and determine if expected keys/values match criteria."
        ),
        tools=[fetch_url, read_feature_file],
        context_providers=[InMemoryHistoryProvider("pytest_qa_suite", load_messages=True)],
    )
    return agent
