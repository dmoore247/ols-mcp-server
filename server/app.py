"""FastAPI application configuration for the OLS MCP server.

Sets up the FastMCP server with streamable HTTP transport for Databricks Apps deployment.
Combines MCP protocol routes with standard FastAPI routes.
"""

from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastmcp import FastMCP

from .tools import load_tools
from .utils import header_store

STATIC_DIR = Path(__file__).parent / "../static"

# Create the MCP server instance
mcp_server = FastMCP(name="OLS MCP Server")

# Load and register all tools with the MCP server
load_tools(mcp_server)

# Convert the MCP server to a streamable HTTP application
mcp_app = mcp_server.http_app()

# Create a separate FastAPI instance for additional API endpoints
app = FastAPI(
    title="OLS MCP Server",
    description="MCP server for Ontology Lookup Service (OLS) API",
    version="0.1.0",
    lifespan=mcp_app.lifespan,
)


@app.get("/", include_in_schema=False)
async def serve_index():
    """Serve the landing page."""
    if STATIC_DIR.exists() and (STATIC_DIR / "index.html").exists():
        return FileResponse(STATIC_DIR / "index.html")
    return {"message": "OLS MCP Server is running", "status": "healthy"}


# Combine MCP routes with custom API routes
combined_app = FastAPI(
    title="OLS MCP Server",
    routes=[
        *mcp_app.routes,
        *app.routes,
    ],
    lifespan=mcp_app.lifespan,
)


if STATIC_DIR.exists():
    combined_app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")


@combined_app.middleware("http")
async def capture_headers(request: Request, call_next):
    """Middleware to capture request headers for authentication."""
    header_store.set(dict(request.headers))
    return await call_next(request)
