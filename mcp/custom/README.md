# Custom MCP Server Registry

## Adding a Custom MCP Server
1. Create a subdirectory under `~/Developer/AI-Dev-Team/mcp/custom/<server-name>/`.
2. Provide a standard `run.sh` entrypoint executing the server via stdio.
3. Validate JSON-RPC 2.0 handshake via `ai-team mcp test <server-name>`.
4. Register the entry into `~/.gemini/config/mcp_config.json` under `mcpServers`.
