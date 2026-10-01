# Global Model Context Protocol (MCP) Routing Policy

## 1. Mandatory Routing Principle

This policy is a **DYNAMIC CAPABILITY ROUTING POLICY**, not a rigid sequential workflow.

Tool selection across Antigravity and the AI-Dev-Team ecosystem MUST adhere to the principle of **Minimum Necessary Capability**:
1. **Identify the user's actual task**: Discern the exact scope, intent, and domain of the user request.
2. **Determine the required capability**: Map the request directly to the specific capability needed.
3. **Select the minimum MCP/tool necessary**: Invoke only the single tool or server required to fulfill that step.
4. **On-demand invocation**: Invoke additional MCP tools ONLY when the task genuinely branches into their domain.
5. **No unnecessary activation**: Never activate, query, or enumerate unrelated MCP servers simply because they are available in the environment.
6. **No rigid waterfalls**: The tool selection guidelines do NOT mean that every task must begin with Understand Anything or full repository discovery.

---

## 2. Capability-to-Tool Routing Matrix

| User Objective / Intent | Target MCP Server / Engine | Tool / CLI Invocations | Selection Rationale |
| :--- | :--- | :--- | :--- |
| **"Research the latest documentation"** | `web` (`mcp-server-fetch`) or `gemini-api-docs` | `fetch`, `gemini_search_docs`, `gemini_get_doc` | Fast, deterministic HTML-to-Markdown extraction without headless browser overhead. |
| **"Lookup external library/framework docs"** | `context7` (`@upstash/context7-mcp`) / `ctx7` CLI | `resolve-library-id`, `query-docs`, `ctx7 docs` | Up-to-date documentation and code examples for React, Vite, Next.js, Three.js, Playwright, Node.js, and popular SDKs. |
| **"Check git status"** | `git` (`mcp-server-git`) / Native git | `git_status`, `git_diff`, `git_commit`, `git_log` | High-speed, structured local Git tree management without remote calls. |
| **"Explain this repository architecture"** | `Understand-Anything` | `~/Developer/AI-Dev-Team/repos/Understand-Anything` | Deep AST analysis, entity relationships, dependency discovery. Only invoke when codebase comprehension is requested. |
| **"Create a technical specification"** | GitHub Spec Kit | `ai-team specify` (`specify-cli`) | Structured specification, checklist, and prompt engineering workflow. |
| **"Coordinate multiple agents"** | `agent-team` | `create_task`, `log_work`, `update_task`, `list_tasks` | Persistent multi-agent coordination backed by SQLite (`~/.agent-team/team.db`). |
| **"Edit local files"** | `filesystem` (`@modelcontextprotocol/server-filesystem`) / Native tools | `read_file`, `write_file`, `edit_file`, `list_directory` | Confined strictly to `/Users/subhajkar/Developer`. |
| **"Test the web UI"** | `browser` (`@modelcontextprotocol/server-puppeteer`) | `puppeteer_navigate`, `puppeteer_screenshot`, `puppeteer_click` | Headless Chromium automation. Use ONLY when interactive JavaScript or visual rendering is required. |
| **"Get GitHub issue information"** | `github` (`@modelcontextprotocol/server-github`) | `get_issue`, `list_pull_requests`, `search_code` | Remote GitHub API integration. Requires `GITHUB_PERSONAL_ACCESS_TOKEN`. Read-only by default. |
| **"Query GCP"** | `datacloud_*` Remote MCPs / Datacloud IDE Proxies | `datacloud_bigquery_remote`, `datacloud_spanner_remote`, etc. | Managed Google Cloud data services. Use only when cloud data queries or Datacloud sessions are targeted. |
| **"Use this project's PostgreSQL database"** | Project-local MCP | Configured in `<project>/.agents/mcp_config.json` | Project-scoped database credentials and queries. Never configured globally. |

---

## 3. Strict Operational Anti-Patterns (Prohibited Behaviors)

1. **NO Universal Understand-Anything Requirement**: Do NOT run repository AST analysis or knowledge graph generation for simple bugfixes, single-file edits, git status checks, or documentation questions.
2. **NO Redundant Server Execution**: Do NOT launch Puppeteer when a simple HTTP `fetch` satisfies the documentation lookup.
3. **NO Premature Multi-Agent Overhead**: Do NOT log tasks into AgentTeam for simple single-step user questions or quick terminal lookups. Reserve AgentTeam for multi-step team projects.
4. **NO Global Credential Leakage**: Never place database passwords, private cloud keys, or project secrets in global configuration files (`~/.gemini/config/mcp_config.json`).
5. **NO Unprompted Remote Publishing**: Never automatically run `git push`, create remote PRs, or publish releases without explicit authorization.

---

## 4. Protected Workspaces Invariant

The following directories are permanently protected:
- `/Users/subhajkar/Developer/LinkedIn-Audit/`
- `/Users/subhajkar/Developer/subhajitportfolio-2.0/`

Under no circumstances should any MCP tool, script, or agent modify, move, rename, delete, reinstall, or overwrite files within these repositories.
