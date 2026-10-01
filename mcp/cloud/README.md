# Cloud MCP Layer

## Multi-Cloud Architecture
- **Google Cloud Platform (GCP)**: Preconfigured remote endpoints for BigQuery, Spanner, AlloyDB, Cloud SQL, Dataplex, and Dataproc using Google OAuth tokens.
- **AWS / Azure**: Configured on demand per project in `<project>/.agents/mcp_config.json` to prevent cross-account credential leakage.
