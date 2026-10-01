# Database MCP Layer & Isolation Policy

## Policy: Global vs Project Isolation
Database connections frequently carry stateful data, production credentials, and schema specificities. Therefore:
- **Global Layer**: Retains cloud managed database bridges (Google Cloud BigQuery, Spanner, AlloyDB, Cloud SQL) via `mcp_config.json`.
- **Project Layer**: Project-specific local databases (e.g. SQLite, PostgreSQL, MySQL, Redis, MongoDB) MUST be configured inside `<project>/.agents/mcp_config.json`.
- **Credential Safety**: Never commit database passwords, connection strings, or service tokens into global configurations or version control.
