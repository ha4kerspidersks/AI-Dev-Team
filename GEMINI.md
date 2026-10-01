# AI Development Team — Ecosystem Instructions & Rules

## Root Directory: `/Users/subhajkar/Developer/AI-Dev-Team`

### Mandatory Global MCP Routing Policy
Tool selection across all agents and operations in this ecosystem is governed by **Minimum Necessary Capability**:
- **Research documentation / fetch web content** → `web` (`mcp-server-fetch`) or `gemini-api_gemini-api-docs`
- **Check git status, commit, branch, diff** → `git` (`mcp-server-git`) / native git
- **Explain repository architecture & code graph** → `Understand-Anything`
- **Create technical specification** → Spec Kit (`ai-team specify`)
- **Coordinate multiple agents / task tracking** → `agent-team` (SQLite `~/.agent-team/team.db`)
- **Edit local files** → `filesystem` (`@modelcontextprotocol/server-filesystem`) / native tools
- **Test web UI / screenshots** → `browser` (`@modelcontextprotocol/server-puppeteer`)
- **Inspect GitHub issues, PRs, code** → `github` (`@modelcontextprotocol/server-github`)
- **Query GCP services** → `datacloud_*` Remote MCPs / IDE proxies
- **Project databases (Postgres, MySQL, SQLite)** → Project-local MCP in `<project>/.agents/mcp_config.json`

### Strict Routing Principles
1. **Dynamic Task-Driven Selection**: Do NOT force Understand Anything or repository AST analysis on every task. Select tools dynamically based on user intent.
2. **Minimum Necessary Tooling**: Invoke only the specific tool needed for the current step. Do not activate unrelated MCP servers simply because they are available.
3. **Project Isolation**: Never place project-specific database passwords, cloud tokens, or API secrets into global configs.

### Protected Workspaces Invariant
The following projects MUST NEVER be modified, moved, renamed, deleted, or overwritten:
- `/Users/subhajkar/Developer/LinkedIn-Audit/`
- `/Users/subhajkar/Developer/subhajitportfolio-2.0/`

### Global Project Intelligence Bootstrap Rule (Mandatory Invariant)
**PROJECT CONTEXT MUST EXIST BEFORE DEVELOPMENT**. Whenever Antigravity starts working on ANY software project, repository, workspace, or codebase, you MUST automatically determine whether that project already has Project Intelligence / Context Memory. This rule applies to EVERY project and EVERY future task.

#### Operating Pipeline for Every Task:
```
DETECT → IDENTIFY PROJECT → LOAD PROJECT INTELLIGENCE → (IF MISSING → DISCOVER + CREATE MEMORY) → VALIDATE MEMORY → ANALYZE USER REQUEST → INSPECT RELEVANT SOURCE → IMPLEMENT → BUILD / TEST / VERIFY → UPDATE PROJECT INTELLIGENCE → FINAL VALIDATION → REPORT
```

#### Inviolable Tenets:
1. **Mandatory First-Time Initialization**: If project intelligence does not exist, STOP NORMAL DEVELOPMENT TEMPORARILY. Perform structured discovery and initialize memory automatically. Never ask the user "Should I analyze?" or "Would you like me to create memory?". After initialization, automatically resume the user's original request.
2. **Known Project Navigation**: If intelligence exists, load `PROJECT-CONTEXT.md` first (<150 lines). Validate whether it is stale. Compare project state, refresh affected areas, and inspect ONLY source files relevant to the active task.
3. **Source Code Authority**: Project memory is an architectural navigation layer. Source code is ALWAYS the authoritative source of truth. If code contradicts memory, trust the code and update the memory.
4. **Change Classification & Refresh**: After development, classify changes (Level 1 Content, Level 2 Code, Level 3 Structural, Level 4 Architectural). Update file index, affected maps, changelog, and ADRs.
5. **Multi-Project Isolation**: Every project has a stable, unique `PROJECT_ID`. Never leak context from Project 1 into Project 2.
6. **Separation of Concerns**: Global rules govern agent methodology; project memory stores project-specific architecture. Never store project architecture in global configs.
7. **Security & Privacy**: Zero secrets stored. `.env` is recorded by existence only. All credentials, tokens, and private keys are strictly redacted.
8. **Autonomous Execution**: Perform discovery, context loading, testing, and memory updates automatically without asking routine permission.
9. **Storage & Engine**: Store under `<PROJECT_ROOT>/.agent/project-memory/` (or `.agents/project-memory/`). Powered by `ai-team memory [detect|discover|load|refresh|check|recover|status]` or `/Users/subhajkar/Developer/AI-Dev-Team/scripts/project-memory`.

