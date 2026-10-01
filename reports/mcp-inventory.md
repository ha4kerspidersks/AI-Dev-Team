# Comprehensive MCP Foundation Inventory & Classification

## 1. Master Server Inventory

| Server Name | Transport | Scope | Runtime | Tools | Purpose | Authentication | Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **`agent-team`** | stdio | Global / Ecosystem | Node.js 22 LTS | 46 | Multi-agent state, tasks, discussions, journal | None (Local SQLite) | **HEALTHY** |
| **`github`** | stdio | Global / Core | Node.js 22 LTS | 26 | Repo inspection, issues, PRs, code search | `GITHUB_PERSONAL_ACCESS_TOKEN` | **HEALTHY** |
| **`git`** | stdio | Global / Core | Python 3.14 (`mcp-env`) | 12 | Local Git status, diffs, branches, commits | Local Git Identity | **HEALTHY** |
| **`filesystem`** | stdio | Global / Core (Confined) | Node.js 22 LTS | 14 | Scoped file read/write/edit/list | Confinement (`~/Developer`) | **HEALTHY** |
| **`browser`** | stdio | Global / Core | Node.js 22 LTS | 7 | Headless Chromium navigation & inspection | None (Local Sandbox) | **HEALTHY** |
| **`web`** | stdio | Global / Core | Python 3.14 (`mcp-env`) | 1 | Fast HTML-to-Markdown HTTP fetch | None (Direct HTTP) | **HEALTHY** |
| **`gemini-api_gemini-api-docs`** | builtin | Builtin / Eager | In-Process | 2 | Gemini API & SDK documentation search | In-Process IDE Context | **HEALTHY** |
| **`notebooks`** | stdio | Preinstalled / GCP | Node.js (Datacloud Proxy) | 11 | Datacloud notebook cell management | IDE Datacloud Socket | **READY (Dormant Proxy)** |
| **`visualization`** | stdio | Preinstalled / GCP | Node.js (Datacloud Proxy) | 1 | Datacloud chart and visualization render | IDE Datacloud Socket | **READY (Dormant Proxy)** |
| **`data-agent-kit`** | stdio | Preinstalled / GCP | Node.js (Datacloud Proxy) | 4 | Active editor context & GCP bridge | IDE Datacloud Socket | **READY (Dormant Proxy)** |
| **`datacloud_bigquery_remote`** | remote | Global / GCP | Remote HTTPS | Remote | BigQuery data warehouse queries | Google OAuth (`bigquery`) | **CONFIGURED** |
| **`datacloud_spanner_remote`** | remote | Global / GCP | Remote HTTPS | Remote | Cloud Spanner database administration | Google OAuth (`spanner`) | **CONFIGURED** |
| **`datacloud_alloydb_remote`** | remote | Global / GCP | Remote HTTPS | Remote | Cloud AlloyDB PostgreSQL queries | Google OAuth (`cloud-platform`) | **CONFIGURED** |
| **`datacloud_cloud-sql_remote`** | remote | Global / GCP | Remote HTTPS | Remote | Cloud SQL instance administration | Google OAuth (`cloud-platform`) | **CONFIGURED** |
| **`datacloud_knowledge_catalog_remote`**| remote | Global / GCP | Remote HTTPS | Remote | Dataplex governance & catalog | Google OAuth (`cloud-platform`) | **CONFIGURED** |
| **`datacloud_dataproc_remote`** | remote | Global / GCP | Remote HTTPS | Remote | Dataproc Spark/Hadoop cluster ops | Google OAuth (`dataproc`) | **CONFIGURED** |

---

## 2. Categorized Inventory Groupings

### 2.1 Global MCP Servers (Active in Authoritative Config)
- `agent-team`: Multi-agent orchestration
- `github`: Remote GitHub API operations
- `git`: Local Git repository management
- `filesystem`: Scoped filesystem management within `/Users/subhajkar/Developer`
- `browser`: Headless Puppeteer automation
- `web`: Deterministic markdown content retrieval
- `gemini-api_gemini-api-docs`: Official Gemini reference documentation

### 2.2 Workspace MCP Servers
- Currently **0** workspace-level config overrides active. Projects consume the Global MCP layer, creating local overrides in `<project>/.agents/mcp_config.json` only when dedicated databases or custom APIs are needed.

### 2.3 AgentTeam MCP
- Location: `/Users/subhajkar/Developer/AI-Dev-Team/repos/AgentTeam/mcp-server`
- Database: `/Users/subhajkar/.agent-team/team.db` (SQLite3, 15 tables)
- Runtime: Isolated Node 22 (`/Users/subhajkar/Developer/AI-Dev-Team/environments/node22/bin/node`)
- Role: Persistent state machine and agent coordination ledger across all projects.

### 2.4 Google Cloud MCP
- Local Proxies: `notebooks`, `visualization`, `data-agent-kit` (interfacing via `mcp_proxy_bundle.js` with Antigravity IDE Datacloud extension).
- Remote SSE/HTTPS Endpoints: BigQuery, Spanner, AlloyDB, Cloud SQL, Dataplex Knowledge Catalog, Dataproc.

### 2.5 Other & Auxiliary MCP Components
- `Understand-Anything`: Local repository static analysis and visual AST knowledge graph engine (`~/Developer/AI-Dev-Team/repos/Understand-Anything`). Operates as a local analysis engine without requiring a separate MCP daemon.

### 2.6 Disabled MCP Servers
- **None**. All 15 configured servers in `mcp_config.json` are enabled and verified.

### 2.7 Broken MCP Servers
- **None**. 0 missing binaries, 0 missing runtimes, 0 broken paths.

### 2.8 Duplicate Analysis
- **GitHub**: Only 1 GitHub server configured (`@modelcontextprotocol/server-github`). Antigravity's native tools provide shell git access, while Git MCP handles structured local git, and GitHub MCP handles remote API. No duplicate servers exist.
- **Filesystem**: Only 1 Filesystem MCP server configured (`@modelcontextprotocol/server-filesystem`). Antigravity built-in tools (`view_file`, `write_to_file`) are complementary; no duplicate MCP server.
- **Browser/Web**: Distinct separation of concerns: `browser` (`puppeteer`) handles interactive JavaScript DOM and screenshots; `web` (`fetch`) handles static text extraction and documentation parsing.
- **Databases**: Global configuration retains only Google Cloud managed database bridges. Project databases (PostgreSQL, SQLite, MySQL) remain strictly project-scoped.

---

## 3. Required MCP Categories Classification

| Category | Capability | Classification | Rationale |
| :--- | :--- | :--- | :--- |
| **Core** | Filesystem, Git, GitHub, Browser, Web, Docs, AgentTeam | **REQUIRED NOW** | Fundamental development, navigation, research, and coordination substrate. Already installed and operational. |
| **Code Understanding**| Understand-Anything / AST Analysis | **REQUIRED NOW** | Deep codebase relationship and topology mapping. Integrated via local repository. |
| **DevOps** | Docker inspect, Test Runners, CI/CD status | **USEFUL LATER** | Useful for containerized workflows; local CLI tooling already fulfills current requirements. |
| **Databases** | Project PostgreSQL / MySQL / SQLite | **OPTIONAL (Project-level)**| Must not be installed globally to avoid credential leakage and cross-contamination. |
| **Cloud** | AWS / Azure / GCP custom integrations | **OPTIONAL (Project-level)**| Handled via project configurations when dedicated accounts are targeted. |
| **Productivity** | Google Drive, Calendar, Slack, Notion, Jira | **UNNECESSARY** | Adds latency, excessive tool token footprint, and broad credential risk without direct developer value. |
| **Offensive Security**| Fuzzers, exploit payloads, automated vulnerability attack tools | **DANGEROUS** | Violates safety policy; must never be globally configured into agent toolsets. |
