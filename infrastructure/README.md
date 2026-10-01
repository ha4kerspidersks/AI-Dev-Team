# Global AI Infrastructure Layer

## Overview
The infrastructure layer houses supporting AI gateways, routing proxies, and multi-model traffic management runtimes that operate independently from agent skills.

## Infrastructure Directory Structure
```
~/Developer/AI-Dev-Team/infrastructure/
└── omniroute/       # Unified AI router with 359 providers, fallback logic & RTK compression
```

## AI Gateway Analysis & Operational Policy
- **Existing Gateway Runtime**: FreeLLMAPI is active locally on `127.0.0.1:31415`.
- **Primary Agent Routing**: Antigravity, Gemini CLI, and Codex use direct model APIs with granular MCP routing per `.agents/rules/mcp-routing-policy.md`.
- **OmniRoute Gateway (`infrastructure/omniroute`)**:
  - **Classification**: SUPPORTING INFRASTRUCTURE / AI GATEWAY
  - **Version**: 3.8.51 (Commit `0d089e7e`)
  - **Default Port**: `20128` (avoids any conflict with FreeLLMAPI on 31415 or web dev servers on 3000/5173).
  - **Status**: INSTALLED (Available on-demand). In accordance with Phase 8 policy, OmniRoute is NOT spawned as an unprompted competing background daemon. When multi-provider fallback or token compression is required, it can be started on-demand via `pnpm --filter omniroute dev` or Docker container without altering existing agent workflows.
