from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP
import os
import json

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
    

    # Join all formatted chunks from all namespaces into a single string
    context = ''.join("" + chunk for chunk in input_queries.split("\n") if chunk.strip())
    return context


if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')