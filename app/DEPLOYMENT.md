# Deploying MCP OLS Service to Databricks Apps

## Prerequisites
1. Databricks workspace with Apps enabled
2. Databricks CLI installed and configured
3. Appropriate permissions to create and manage apps

## Deployment Steps

### Using Databricks CLI
```bash
databricks apps create mcp-ols-service
databricks apps deploy mcp-ols-service /Workspace/Users/douglas.moore@databricks.com/mcp-ols-server
databricks apps start mcp-ols-service
databricks apps get mcp-ols-service
```

## Testing
```bash
curl https://<your-app-url>/health
curl https://<your-app-url>/mcp/ontologies
```

## API Documentation
- Swagger UI: https://<your-app-url>/docs
- ReDoc: https://<your-app-url>/redoc
