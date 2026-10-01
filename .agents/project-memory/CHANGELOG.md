# Project Memory Changelog: AI-Dev-Team

## [2026-09-17 13:27:34Z] Initial Project Discovery
- **Action**: Initial structured discovery and memory index generation.
- **Change Level**: Level 3 (Structural Baseline)
- **Indexed Files**: 18653
- **Git Commit**: `none`
- **Result**: Complete persistent context created.

## [2026-09-25] ScrapeGraphAI Global Skill Installation
- **Action**: Installed official ScrapeGraphAI (`scrapegraphai` 2.2.4) open-source library globally, isolated in a new uv-managed venv `environments/scrapegraphai-env` (Python 3.12). Installed Playwright 1.63.0 + Chromium browser binary. Added global skill `skills/scrapegraphai-web-extraction/SKILL.md` (source: official upstream README/AGENTS.md, no unofficial duplicate skill existed). Evaluated the official managed `scrapegraph-mcp` MCP server per the global MCP routing policy and intentionally did NOT add it (requires paid `SGAI_API_KEY`, would duplicate existing `web`/`browser` MCP servers).
- **Change Level**: Level 2 (Code/Tooling addition, additive only)
- **Verification**: Python import OK, Playwright Chromium fetch of `https://example.com` OK. LLM-based structured extraction step verified as functional in code but not run live (no LLM API key present in this environment; user must export one, e.g. `OPENAI_API_KEY`).
- **Result**: No existing skills, MCP servers, or configs modified or removed.
