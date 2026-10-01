#!/usr/bin/env bash
# GitHub MCP Server Runner (Isolated Node 22 runtime)
set -eo pipefail
export PATH="/opt/homebrew/bin:$PATH"

# Auto-resolve token securely via gh CLI if not set in environment
if [ -z "${GITHUB_PERSONAL_ACCESS_TOKEN:-}" ]; then
  if command -v gh >/dev/null 2>&1; then
    _GH_TOKEN="$(gh auth token 2>/dev/null || true)"
    if [ -n "$_GH_TOKEN" ]; then
      export GITHUB_PERSONAL_ACCESS_TOKEN="$_GH_TOKEN"
    fi
  fi
fi

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MCP_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
NODE_BIN="/Users/subhajkar/Developer/AI-Dev-Team/environments/node22/bin/node"

exec "$NODE_BIN" "$MCP_ROOT/node_modules/@modelcontextprotocol/server-github/dist/index.js" "$@"
