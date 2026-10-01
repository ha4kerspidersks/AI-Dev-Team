#!/usr/bin/env bash
# Filesystem MCP Server Runner (Scoped to /Users/subhajkar/Developer)
set -eo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MCP_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
NODE_BIN="/Users/subhajkar/Developer/AI-Dev-Team/environments/node22/bin/node"

ALLOWED_DIR="${1:-/Users/subhajkar/Developer}"
exec "$NODE_BIN" "$MCP_ROOT/node_modules/@modelcontextprotocol/server-filesystem/dist/index.js" "$ALLOWED_DIR"
