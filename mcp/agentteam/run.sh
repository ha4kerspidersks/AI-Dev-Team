#!/usr/bin/env bash
# AgentTeam MCP Server Runner (Isolated Node 22 runtime)
set -eo pipefail
NODE_BIN="/Users/subhajkar/Developer/AI-Dev-Team/environments/node22/bin/node"
SERVER_JS="/Users/subhajkar/Developer/AI-Dev-Team/repos/AgentTeam/mcp-server/dist/index.js"

exec "$NODE_BIN" "$SERVER_JS" "$@"
