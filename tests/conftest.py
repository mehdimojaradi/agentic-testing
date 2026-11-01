# Copyright (c) Microsoft. All rights reserved.
import asyncio
import pytest
import pytest_asyncio
from agents import gemini_agent, ollama_agent

from dotenv import load_dotenv

load_dotenv()

# Parameterize the fixture so tests injecting 'run_agent' can run against multiple backends,
# or you can select a specific one via command line arguments.
@pytest_asyncio.fixture(scope="session", params=["ollama", "gemini"])
async def run_agent(request):
    """Factory fixture that provisions the correct agent client based on parameterization."""
    model_type = request.param
    
    if model_type == "gemini":
        agent = await gemini_agent()
    elif model_type == "ollama":
        agent = await ollama_agent()
    else:
        raise ValueError(f"Unsupported agent model type: {model_type}")
        
    return agent