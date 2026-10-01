#!/usr/bin/env bash
# Web Fetch MCP Server Runner (Isolated mcp-env Python runtime)
set -eo pipefail
FETCH_BIN="/Users/subhajkar/Developer/AI-Dev-Team/environments/mcp-env/bin/mcp-server-fetch"

exec "$FETCH_BIN" "$@"
