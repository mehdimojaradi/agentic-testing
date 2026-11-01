import pytest
from agents import gemini_agent, ollama_agent
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture(scope="session", params=["ollama", "gemini"])
async def run_agent(request):
    model_type = request.param
    
    if model_type == "gemini":
        agent = await gemini_agent()
    elif model_type == "ollama":
        agent = await ollama_agent()
    else:
        raise ValueError(f"Unsupported agent model type: {model_type}")
        
    return agent

@pytest.fixture(scope="session")
def prompts():
    def _prompts(filename: str) -> str:
        current_dir = Path(__file__).parent
        prompts_file = current_dir / "prompts" / filename
        print(prompts_file)
        with open(prompts_file) as f:
            prompt_content = f.read()   
            
        return prompt_content
    return _prompts