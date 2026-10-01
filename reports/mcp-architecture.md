# Global Model Context Protocol (MCP) Foundation Architecture

## 1. Executive Summary

This document establishes the authoritative architecture for the **Global MCP Foundation** across the local development workstation on macOS using Google Antigravity. The infrastructure provides a unified, cross-language, cross-stack tool execution layer serving web, backend, mobile, AI/ML, DevOps, and cloud workloads while guaranteeing strict project isolation and zero leakage of credentials.

The global MCP layer is decoupled from project-specific domains (such as portfolio assets or client databases). Individual projects consume the global foundation as an execution substrate while retaining their own isolated project configurations when specific databases or cloud accounts are required.

---

## 2. High-Level Architectural Topology

```text
                                  GOOGLE ANTIGRAVITY
                                          │
                                          ▼
                               GLOBAL MCP RUNTIME LAYER
                       (~/.gemini/config/mcp_config.json)
                                          │
         ┌────────────────────────────────┼────────────────────────────────┐
         │                                │                                │
         ▼                                ▼                                ▼
  CORE DEVELOPMENT               KNOWLEDGE & RESEARCH             AUTOMATION & INFRA
         │                                │                                │
  ┌──────┴──────┐                  ┌──────┴──────┐                  ┌──────┴──────┐
  │ Git (local) │                  │ Gemini Docs │                  │ Google Cloud│
  │ GitHub API  │                  │ Web Fetch   │                  │ (Remote APIs│
  │ Filesystem  │                  │ Browser DOM │                  │ BigQuery,   │
  │ Docker Host │                  │ Understand- │                  │ Spanner,    │
  │ Testing     │                  │  Anything   │                  │ AlloyDB,    │
  └──────┬──────┘                  └──────┬──────┘                  │ Cloud SQL)  │
         │                                │                         └──────┬──────┘
         └────────────────────────────────┼────────────────────────────────┘
                                          │
                                          ▼
                               AGENTTEAM COORDINATION LAYER
                           (SQLite Persistent State Engine:
                              ~/.agent-team/team.db)
```

---

## 3. Central Directory Layout

The physical implementations, runners, and adapter configurations are centralized under:
`~/Developer/AI-Dev-Team/mcp/`

```text
mcp/
├── github/                 # Official @modelcontextprotocol/server-github (Node 22)
│   ├── run.sh              # Local stdio runner
│   └── README.md           # API capabilities & security guardrails
├── git/                    # Official mcp-server-git (Python 3.14 mcp-env)
│   ├── run.sh              # Stdio runner
│   └── README.md           # Working tree, diffs, log, commit controls
├── filesystem/             # Official @modelcontextprotocol/server-filesystem
│   ├── run.sh              # Scoped runner (/Users/subhajkar/Developer)
│   └── README.md           # Strict path confinement specification
├── browser/                # Official @modelcontextprotocol/server-puppeteer
│   ├── run.sh              # Headless browser automation runner
│   └── README.md           # DOM traversal, screenshot, interaction
├── web/                    # Official mcp-server-fetch (Python 3.14 mcp-env)
│   ├── run.sh              # Clean HTML-to-Markdown HTTP fetch runner
│   └── README.md           # Web documentation & research engine
├── databases/              # Project database templates & isolation guide
│   └── README.md           # PostgreSQL, SQLite, MySQL isolation policy
├── docker/                 # Container runtime interface & security bounds
│   └── README.md           # Daemon socket access rules & safety limits
├── testing/                # Multi-framework test execution specifications
│   └── README.md           # Pytest, Vitest, Jest, Node test runner patterns
├── cloud/                  # Multi-cloud architecture documentation
│   └── README.md           # GCP remote endpoints, AWS/Azure isolation
├── devops/                 # CI/CD, Terraform, Kubernetes governance
│   └── README.md           # Destruction prevention & plan validation
├── documentation/          # Documentation aggregation layer
│   └── README.md           # Live Gemini docs + universal DevDocs fetch
├── agentteam/              # AgentTeam coordination module
│   ├── run.sh              # Stdio server runner
│   └── README.md           # 46 tools, SQLite schema, multi-agent protocol
├── understand-anything/    # Understand-Anything repository integration
│   └── README.md           # AST, Tree-sitter, code knowledge graph engine
└── custom/                 # Extensible template for custom MCP tools
    └── README.md           # Protocol onboarding instructions
```

---

## 4. Global vs Project MCP Policy

| Dimension | Global MCP Foundation | Project-Specific MCP |
| :--- | :--- | :--- |
| **Location** | `~/.gemini/config/mcp_config.json` | `<project>/.agents/mcp_config.json` |
| **Scope** | Cross-project developer capabilities | Single repository lifecycle |
| **Capabilities** | Git, GitHub, Filesystem, Browser, Web, AgentTeam, Gemini Docs | Local app database, staging APIs, project cloud keys |
| **Credentials** | Shared workstation credentials (GitHub token via env) | Dedicated service accounts, DB passwords, test secrets |
| **Persistence** | Centralized in `~/.agent-team/team.db` | Project local storage or ephemeral test databases |
| **Sandboxing** | Confined to `/Users/subhajkar/Developer` | Confined to project repository root |

### Strict Security Rule:
Project-specific credentials or sensitive production database strings MUST NEVER be committed to global configurations. When a specific repository requires custom database inspection (e.g. Supabase, local PostgreSQL, Redis), the configuration is defined locally inside `<project>/.agents/mcp_config.json`.

---

## 5. Architectural Subsystems

### 5.1 Core Development Layer
- **`github`**: Implements remote GitHub operations (issue tracking, pull requests, repository inspection, code search). All destructive write actions require explicit authorization.
- **`git`**: Provides high-speed local repository operations (status, diffs, commits, branches, log) via `mcp-server-git` in an isolated Python virtual environment.
- **`filesystem`**: Confines filesystem traversal to `/Users/subhajkar/Developer`. Blocks access to system root (`/`), SSH keys (`~/.ssh`), cloud keys (`~/.aws`), or user credentials.

### 5.2 Knowledge, Research & Code Understanding
- **`gemini-api_gemini-api-docs`**: Builtin in-process eager MCP providing instant, authoritative documentation search across Google Gemini APIs and SDKs.
- **`web` (`fetch`)**: Converts online documentation and articles into clean Markdown without executing JavaScript, providing lightweight and deterministic content retrieval.
- **`browser` (`puppeteer`)**: Headless browser automation for rendering dynamic JavaScript SPAs, capturing UI screenshots, and verifying web frontend behavior.
- **`understand-anything`**: Specialized local code comprehension engine utilizing Tree-sitter AST parsing across 14 languages to construct entity relation graphs (calls, imports, inheritance) without polluting standard MCP tool schemas.

### 5.3 Multi-Agent Coordination Backbone (`agent-team`)
AgentTeam serves as the operational state machine and persistent ledger for Antigravity:
- **Persistence**: High-performance SQLite database at `~/.agent-team/team.db` with 15 normalized tables.
- **Tool Roster**: 46 tools encompassing project lifecycle, task scheduling, work logging, team member management, discussions, decision records, and artifact sharing.
- **Reusability**: Decoupled from any single codebase; available globally across all projects.

### 5.4 Cloud & Enterprise Data Layer
- **Google Cloud Datacloud Endpoints**: Remote SSE/HTTPS integrations for BigQuery, Spanner, AlloyDB, Cloud SQL, Dataplex, and Dataproc.
- **Datacloud Extension Proxies**: In-IDE domain socket proxies (`notebooks`, `visualization`, `data-agent-kit`) activating dynamically when active Datacloud sessions are opened.
