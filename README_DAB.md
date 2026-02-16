# OLS MCP Service - Databricks Asset Bundle

This directory contains a Databricks Asset Bundle (DAB) configuration for deploying the OLS MCP service as a Databricks App.

## Directory Structure

```
ols-mcp-server/
├── databricks.yml          # Main DAB configuration
├── resources/
│   └── app.yml            # App resource definition
├── app/
│   ├── app.py             # FastAPI application
│   └── requirements.txt   # Python dependencies
└── README_DAB.md          # This file
```

## Prerequisites

1. Install Databricks CLI:
   ```bash
   pip install databricks-cli
   ```

2. Authenticate with your workspace:
   ```bash
   databricks auth login --host <your-workspace-url>
   ```

## Deployment

### Deploy to Development

```bash
cd /Workspace/Users/douglas.moore@databricks.com/ols-mcp-server
databricks bundle deploy
```

This will:
- Validate the bundle configuration
- Upload app files to the workspace
- Create/update the Databricks App
- Deploy to the `dev` target (default)

### Deploy to Production

```bash
databricks bundle deploy --target prod
```

### View Deployment Status

```bash
databricks bundle run ols_mcp_service
```

### Destroy/Remove the App

```bash
databricks bundle destroy
```

## Validate Configuration

Before deploying, validate your bundle:

```bash
databricks bundle validate
```

## Local Development

To test the FastAPI app locally:

```bash
cd app
pip install -r requirements.txt
uvicorn app:app --reload
```

Access the API at: http://localhost:8000
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Configuration

### Environment Variables

Edit `resources/app.yml` to modify environment variables:
- `OLS_API_BASE_URL`: Base URL for OLS API
- `LOG_LEVEL`: Logging level (INFO, DEBUG, WARNING, ERROR)

### Targets

The bundle supports two deployment targets:
- `dev` (default): Development environment
- `prod`: Production environment

## Troubleshooting

### View App Logs

```bash
databricks apps logs ols-mcp-service
```

### Check App Status

```bash
databricks apps get ols-mcp-service
```

### Common Issues

1. **Authentication Error**: Run `databricks auth login` again
2. **Bundle Validation Failed**: Check `databricks.yml` syntax
3. **App Won't Start**: Check logs for dependency or runtime errors

## API Endpoints

Once deployed, your app will expose:

- `GET /` - Health check
- `GET /health` - Detailed health status
- `POST /mcp/search` - Search ontologies
- `GET /mcp/ontologies` - List all ontologies
- `POST /mcp/ontology` - Get ontology details
- `POST /mcp/term` - Get term details
- `GET /mcp/ontologies/{id}/terms` - Get ontology terms
- `POST /mcp/initialize` - MCP protocol initialization
- `POST /mcp/tools/list` - List available MCP tools
- `POST /mcp/tools/call` - Execute MCP tool

## Next Steps

1. Review and customize `databricks.yml` and `resources/app.yml`
2. Run `databricks bundle validate` to check configuration
3. Deploy with `databricks bundle deploy`
4. Test the deployed app endpoints
5. Monitor logs and performance
