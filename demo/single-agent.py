# Copyright (c) Microsoft. All rights reserved.
import asyncio
from agent_framework import AgentSession, InMemoryHistoryProvider
from agent_framework.ollama import OllamaChatClient
from dotenv import load_dotenv
import json

load_dotenv()


async def main() -> None:

    client = OllamaChatClient()
    message = "generate two names of famous movies, just the names, no description, no explanation, no additional text, no punctuation, no quotes, no brackets, no parentheses, no numbers, no letters, just the names of the movies."
    message2 = "list the names you generated"
    
    agent = client.as_agent(
        name="MovieNameGenerator1",
        instructions="You are a movie name generator.",
        context_providers=[InMemoryHistoryProvider("memory", load_messages=True)]
    )
    # session = agent.create_session()
    
    # response1 = await agent.run(message, session=session)
    
    # exported_state = session.to_dict()
    
    # with open("session_state.json", "w") as states:
    #     json.dump(exported_state, states, indent=4)
        
    with open("session_state.json", "r") as states:
        loaded_state = json.load(states)
    
    session2 = AgentSession.from_dict(loaded_state)
    # session.state.update(exported_state)
    response2 = await agent.run(message2, session=session2)
    print(response2)
            

if __name__ == "__main__":
    asyncio.run(main())
    print()
