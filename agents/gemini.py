from agent_framework_gemini import GeminiChatClient
from agent_framework import Agent, InMemoryHistoryProvider
from tools import fetch_url, read_feature_file
from pathlib import Path

async def instructions() -> str:
    instructions_file = Path(__file__).parents[1] / "prompts" / "instructions.txt"
    with open(instructions_file, "r") as f:
        return f.read()
    

async def gemini_agent() -> Agent:

    agent = Agent(
        client=GeminiChatClient(),
        name="QA_Validation_Expert",
        instructions=await instructions(),
        tools=[fetch_url, read_feature_file],
        context_providers=[InMemoryHistoryProvider("pytest_qa_suite", load_messages=True)],
    )
    
    return agent
