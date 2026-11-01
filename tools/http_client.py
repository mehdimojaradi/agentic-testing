import httpx

async def fetch_url(url: str) -> str:
    """Automated tool for agents to fetch JSON payloads asynchronously."""
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, timeout=10.0)
            if response.status_code == 200:
                return f"HTTP 200 - SUCCESS. Payload: {response.text}"
            else:
                return f"HTTP ERROR {response.status_code}: Server responded with code {response.status_code}."
        except Exception as e:
            return f"CRITICAL EXCEPTION during network call: {str(e)}"
