#!/usr/bin/env bash
# Git MCP Server Runner (Isolated mcp-env Python runtime)
set -eo pipefail
PYTHON_BIN="/Users/subhajkar/Developer/AI-Dev-Team/environments/mcp-env/bin/mcp-server-git"

exec "$PYTHON_BIN" "$@"
