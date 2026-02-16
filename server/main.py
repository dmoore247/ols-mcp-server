"""Main entry point for the OLS MCP server application.

Starts the uvicorn ASGI server with the combined FastAPI/FastMCP application.
Configured as the entry point in pyproject.toml.
"""

import argparse

import uvicorn


def main():
    """Start the MCP server using uvicorn."""
    parser = argparse.ArgumentParser(description="OLS MCP Server")
    parser.add_argument(
        "--port", type=int, default=8000, help="Port to run the server on (default: 8000)"
    )
    args = parser.parse_args()

    uvicorn.run(
        "server.app:combined_app",
        host="0.0.0.0",
        port=args.port,
    )
