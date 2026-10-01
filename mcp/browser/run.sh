#!/usr/bin/env bash
# Browser Puppeteer MCP Server Runner (Isolated Node 22 runtime)
set -eo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MCP_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
NODE_BIN="/Users/subhajkar/Developer/AI-Dev-Team/environments/node22/bin/node"

exec "$NODE_BIN" "$MCP_ROOT/node_modules/@modelcontextprotocol/server-puppeteer/dist/index.js" "$@"
