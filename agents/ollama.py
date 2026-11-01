from agent_framework.ollama import OllamaChatClient
from agent_framework import Agent, InMemoryHistoryProvider
from tools import fetch_url, read_feature_file

async def ollama_agent() -> Agent:
    """Assembles and returns a pre-configured QA Validation Agent."""

    agent = Agent(
        client=OllamaChatClient(),
        name="QA_Validation_Expert",
        instructions=(
            
        ),
        tools=[fetch_url, read_feature_file],
        context_providers=[InMemoryHistoryProvider("pytest_qa_suite", load_messages=True)],
    )
    return agent
