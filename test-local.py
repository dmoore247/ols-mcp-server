"""Test the locally running OLS MCP server."""

import asyncio

from fastmcp import Client

MCP_URL = "http://localhost:8000/mcp"


async def main():
    async with Client(MCP_URL) as client:
        # List available tools
        tools = await client.list_tools()
        print(f"Available tools ({len(tools)}):")
        for tool in tools:
            print(f"  - {tool.name}: {tool.description[:80]}")

        # Search for a term
        print("\n--- search_terms('osteoporosis') ---")
        result = await client.call_tool("search_terms", {"query": "osteoporosis", "rows": 3})
        print(result.content[0].text)

        # Get ontology info
        print("\n--- get_ontology_info('efo') ---")
        result = await client.call_tool("get_ontology_info", {"ontology_id": "efo"})
        print(result.content[0].text)


if __name__ == "__main__":
    asyncio.run(main())
