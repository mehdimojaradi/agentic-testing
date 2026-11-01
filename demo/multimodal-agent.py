import asyncio
from agent_framework import Agent, Content
from agent_framework_gemini import GeminiChatClient
from dotenv import load_dotenv

load_dotenv()

async def non_streaming_example() -> None:
    
    agent = Agent(
        client=GeminiChatClient(),
        name="ImageAnalysisAgent",
        instructions="You can analyze the image and say what is the content of it.",
    )
    
    with(open("screenshot.jpg", "rb") as f):
        img_data = f.read()

    multimodal_input = [
        Content.from_text("Analyze the image and just show the content without any additional description."),
        Content.from_data(img_data, media_type="image/jpg")
    ]

    result = await agent.run(multimodal_input)
    print(result.text)


async def main() -> None:
    await non_streaming_example()


if __name__ == "__main__":
    asyncio.run(main())
