from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP
import os
import requests
import sys
sys.stdout.reconfigure(encoding='utf-8')
# Initialize FastMCP server
mcp = FastMCP("askcpg")


from dotenv import load_dotenv
load_dotenv()
ASKCPG_API_KEY = os.getenv("ASKCPG_API_KEY")
ASKCPG_BACKEND = os.getenv("ASKCPG_BACKEND")


@mcp.tool()
async def get_cpg_context(input_queries: str) -> str:
    """Get context from medical clinical practice guideline books based on user query.

    Args:
        input_queries: user query to get the context from the medical books.
    """
    print("Input Queries:", input_queries)

    url = f"{ASKCPG_BACKEND}/v4/cpg/mcp_context_reply"
    
    # Build the payload and headers with the required API key.
    payload = {"query": input_queries}
    headers = {"x-api-key": ASKCPG_API_KEY}
    
    response = requests.post(
        url,
        headers=headers,
        json=payload,
    )
    # Check for a successful response.
    if response.status_code != 200:
        raise Exception(f"Request failed: {response.status_code} - {response.text}")

    
    data = response.json()
    # Return the context as a string.
    return {
        "context": response.json(),
        "query": input_queries,
        "status": "success",
    }


if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')