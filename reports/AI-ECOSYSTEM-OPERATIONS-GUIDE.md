# AI Ecosystem Operations Guide
**Architecture Taxonomy, Component Directory, Invocation Runbooks & Operational Matrix**

**Date:** 2026-10-01  
**Central Home:** `/Users/subhajkar/Developer/AI-Dev-Team/`  
**System Lead:** Antigravity Global AI Engineering Dev Team / Master Orchestrator  
**Runtime:** macOS (`arm64`), Python 3.12 (`environments/mcp-env`), Node.js v22.18.0, Antigravity Host Runtime  

---

## 1. Architectural Taxonomy: The 10 Fundamental Distinctions

A critical mistake in managing an AI ecosystem is assuming that every entity is a standalone executable agent. In reality, the 77 cataloged components span **10 distinct conceptual layers**. Understanding these distinctions determines whether an entity is something you prompt, an executable you run, a persona injected into a runtime, or a background service.

```
+-----------------------------------------------------------------------------------+
|                            ORCHESTRATOR / HOST RUNTIME                            |
|       (AGT-001 Master Orchestrator, AGT-051 Autonomous Dispatcher, OpenHands)     |
+-----------------------------------------+-----------------------------------------+
                                          |
        +---------------------------------+---------------------------------+
        |                                                                   |
        v                                                                   v
+-------------------------------+                         +-------------------------------+
|         AGENT ROLES           |                         |            SKILLS             |
| (AGT-015 - AGT-028 in roles/) |                         | (100+ procedural cheatsheets  |
| Personas & Scope Constraints  |                         | loaded on-demand: 007, TDD)   |
+---------------+---------------+                         +---------------+---------------+
                |                                                         |
                +-------------------------+-------------------------------+
                                          |
                                          v
+-----------------------------------------------------------------------------------+
|                             DIRECTLY INVOKABLE AGENTS                             |
|  (Native Subagents: fast-developer, architect; External: Copilot Bridge, Strix)   |
+-----------------------------------------+-----------------------------------------+
                                          |
        +---------------------------------+---------------------------------+
        |                                                                   |
        v                                                                   v
+-------------------------------+                         +-------------------------------+
|          MCP SERVERS          |                         |         MODEL ROUTERS         |
| Background JSON-RPC Daemons   |                         | Proxies & Gateways            |
| (agent-team, browser, git)    |                         | (Copilot Bridge, OmniRoute)   |
+---------------+---------------+                         +---------------+---------------+
                |                                                         |
                v                                                         v
+-------------------------------+                         +-------------------------------+
|           MCP TOOLS           |                         |      FRAMEWORKS & UTILITIES   |
| Callable API functions        |                         | Repos, CLIs, Memory Engine    |
| (create_task, puppeteer_click)|                         | (ai-team, OpenSepia, Memory)  |
+-------------------------------+                         +-------------------------------+
```

### The 10 Entity Definitions:

| # | Entity Type | Definition | Directly Invokable? | Concrete Examples |
|---|---|---|---|---|
| 1 | **Agent** | Autonomous entity with an execution loop, reasoning model, and direct tool-execution capability. | **YES** | `Fast Developer`, `Developer Agent`, `Strix Pentester` |
| 2 | **Agent Role** | Standardized specification, personality, and behavioral contract. Defines boundaries and competencies; cannot run as a standalone process. | **NO** (Injected into Agent) | `roles/backend-developer.md`, `roles/security-engineer.md` |
| 3 | **Skill** | Dynamic procedural recipe or cheatsheet (`SKILL.md`) loaded into an agent's context when performing specialized tasks. | **NO** (Loaded by Agent) | `007` (security), `tdd-workflow`, `api-designer` |
| 4 | **MCP Server** | Background daemon providing structured tools and data resources over JSON-RPC stdio/HTTP. | **NO** (Queried via Host) | `agent-team`, `browser`, `filesystem`, `datacloud_*` |
| 5 | **MCP Tool** | A single callable function exposed by an MCP Server. | **YES** (Via Agent) | `agent-team:create_task`, `browser:puppeteer_navigate` |
| 6 | **Workflow** | Deterministic pipeline, script, or state machine orchestrating tasks across multiple stages. | **YES** (Via CLI / Runner) | `autonomous-dev-team/pipeline`, `specify implement` |
| 7 | **Orchestrator** | Meta-agent that plans, breaks down work into Work Packages, delegates to subagents, and synthesizes outputs. | **YES** (Via Chat) | `Master Orchestrator` (`AGT-001`) |
| 8 | **Model Router** | Proxy or gateway directing LLM inference requests across models, vendors, or local engines. | **YES** (Via CLI / Port) | `Copilot Bridge` (`AGT-012`), `OmniRoute` (`AGT-075`) |
| 9 | **Framework** | Full multi-agent engine containing runtime environments, event loops, and worker processes. | **YES** (Via CLI / Docker) | `OpenHands`, `OpenSepia`, `AgentTeam` |
| 10 | **Utility** | CLI helper, memory engine, or AST parser supporting the development ecosystem. | **YES** (Via Terminal) | `ai-team doctor`, `ai-team memory`, `Understand-Anything` |

---

## 2. Every Agent You Can Actually Invoke / Use

Out of the 77 cataloged entities, the following are the **directly usable / invokable agents and systems**, organized by runtime execution method:

### A. Antigravity Native Subagents (Direct Chat / `@mention`)
*Available directly within your current Antigravity IDE session. Trigger by addressing `@agent` or via orchestrator delegation.*

1. **Master Orchestrator (`AGT-001`)**:
   - **Designed for:** Global coordination, task decomposition, work package partitioning (`WP-XXX`), multi-backend routing, risk gating.
   - **Invocation:** Always active host runtime. Prompt directly in conversation.
2. **Architect Specialist (`AGT-002`)**:
   - **Designed for:** High-level system architecture, C4 component modeling, database schemas, RFCs, ADRs.
   - **Invocation:** `@architect` or subagent delegation (`Claude Sonnet / Gemini Pro`).
3. **Developer Agent (`AGT-003`)**:
   - **Designed for:** Full-stack feature implementation, complex refactoring, API construction.
   - **Invocation:** `@developer` or subagent delegation.
4. **Fast Developer (`AGT-004`)**:
   - **Designed for:** Rapid bug fixes, simple scripts, small PRs, low-latency code generation.
   - **Invocation:** `@fast-developer` (Gemini 3 Flash backend).
5. **Tester Agent (`AGT-005`)**:
   - **Designed for:** Test-driven development (TDD), writing unit tests, running test runners, asserting coverage.
   - **Invocation:** `@tester` (Pytest, Vitest, Jest).
6. **Security Reviewer (`AGT-006`)**:
   - **Designed for:** SAST audits, threat modeling, vulnerability detection (OWASP Top 10), secret scanning.
   - **Invocation:** `@security-reviewer`.
7. **Deep Reviewer (`AGT-007`)**:
   - **Designed for:** High-reasoning deep code analysis, race condition detection, edge-case analysis.
   - **Invocation:** `@deep-reviewer`.
8. **Second Opinion (`AGT-008`)**:
   - **Designed for:** Orthogonal architectural validation, adversarial reviews, second-look verification.
   - **Invocation:** `@second-opinion`.
9. **Researcher Agent (`AGT-009`)**:
   - **Designed for:** Web research, documentation lookups, technology stack comparisons, scientific literature.
   - **Invocation:** `@researcher`.
10. **Documentation Agent (`AGT-010`)**:
    - **Designed for:** System documentation, API documentation, READMEs, changelogs, Mermaid diagrams.
    - **Invocation:** `@documentation`.
11. **Git Release Agent (`AGT-011`)**:
    - **Designed for:** Git branches, release tags, semantic versioning, changelog generation, GitHub PR lifecycles.
    - **Invocation:** `@git-release`.
12. **Firestore Rules Author (`AGT-013`)**:
    - **Designed for:** Designing and hardening Google Cloud Firestore Security Rules (`firestore.rules`).
    - **Invocation:** Delegated subagent via Firebase plugin (`firestore-rules-author`).
13. **Flutter A11y Agent (`AGT-014`)**:
    - **Designed for:** Accessibility audits, screen reader semantics, tap targets for Flutter applications.
    - **Invocation:** Delegated subagent via Flutter plugin (`flutter_a11y_agent`).

---

### B. External Multi-Model Sidecar Agent

14. **GitHub Copilot Bridge (`AGT-012`)**:
    - **Designed for:** External multi-model inference via GitHub Copilot CLI across 39 available models (`gpt-5.3-codex`, `claude-sonnet-5`, `gpt-5.5`, `gpt-5.4-mini`).
    - **Invocation Method:**
      ```bash
      # Run via bridge sidecar
      node ~/.gemini/config/sidecars/copilot-bridge.mjs run "<prompt>" --model <copilot_model>
      
      # In chat:
      @github-copilot --model claude-sonnet-5 "<prompt>"
      ```
    - **Prerequisites:** GitHub Copilot CLI authenticated via ACP.

---

### C. Unified AI-Dev-Team CLI (`ai-team`) Executables
*Available globally via `/Users/subhajkar/Developer/AI-Dev-Team/scripts/ai-team`.*

15. **Spec Kit Specify CLI (`AGT-057`)**:
    - **Designed for:** Specification-driven development (`spec-driven-development`). Generates structured project specifications, plans, and implementation steps.
    - **Invocation:**
      ```bash
      ai-team specify check
      ai-team specify init
      ai-team specify plan
      ai-team specify implement
      ```
16. **OpenSepia Multi-Agent Sprint CLI (`AGT-042`–`AGT-050`)**:
    - **Designed for:** Simulating an entire agile development squad (PO, PM, Dev1, Dev2, Tester, DevOps, Sec Analyst).
    - **Invocation:**
      ```bash
      ai-team opensepia --role po --prompt "Define backlog for feature X"
      ai-team opensepia --role dev1 --prompt "Implement database models"
      ai-team opensepia --role sec_analyst --prompt "Audit authentication endpoints"
      ```
17. **Autonomous Background Dispatcher (`AGT-051`–`AGT-053`)**:
    - **Designed for:** Hands-off autonomous development loops and automated code review pipelines.
    - **Invocation:**
      ```bash
      ai-team autonomous
      ```
18. **OpenHands Agent Canvas (`AGT-054`)**:
    - **Designed for:** Autonomous coding tasks inside an isolated Docker sandbox.
    - **Invocation:**
      ```bash
      ai-team canvas
      # or server mode:
      ai-team openhands
      ```
19. **Global Project Intelligence & Memory Engine (`AGT-077`)**:
    - **Designed for:** Autonomous project context detection, architectural memory discovery, level 1–4 change classification, and self-healing token-efficient context.
    - **Invocation:**
      ```bash
      ai-team memory detect <path>
      ai-team memory discover <path>
      ai-team memory load <path>
      ai-team memory refresh <path>
      ai-team memory status <path>
      ```

---

### D. Standalone Security & Specialized Agents

20. **Strix Pentesting Agent (`AGT-055`)**:
    - **Designed for:** Autonomous application security testing, dynamic web fuzzing, exploit verification.
    - **Invocation:**
      ```bash
      cd /Users/subhajkar/Developer/AI-Dev-Team/repos/strix
      python -m strix.cli audit --target <target_url_or_repo>
      ```
21. **Understand-Anything AST Knowledge Engine (`AGT-056`)**:
    - **Designed for:** Deep codebase AST analysis, architectural knowledge graph visualization, onboarding guides.
    - **Invocation:**
      ```bash
      cd /Users/subhajkar/Developer/AI-Dev-Team/repos/Understand-Anything
      npm run start
      # Launch interactive dashboard:
      # Skills: understand-dashboard, understand-explain, understand-chat
      ```
22. **Awesome-LLM-Apps Specialized Agents (`AGT-058`–`AGT-073`)**:
    - **Designed for:** Production-ready reference implementations across diverse domains (Fraud Detection, Financial Analysis, Data Scraping, Voice Support, Mixture-of-Agents).
    - **Invocation:** Executed as standalone Python/Streamlit apps in `AI-Dev-Team/repos/awesome-llm-apps/<app_dir>/`.

---

## 3. Ecosystem Layer Breakdown

```
================================================================================
LAYER 1: ANTIGRAVITY NATIVE (14 AGENTS)
================================================================================
* Location: ~/.gemini/config/agents/ and plugin directories
* Characteristics: Directly promptable, zero startup latency, native IDE tools
* Key Agents: Master Orchestrator, Architect, Developer, Fast Developer, Tester,
  Security Reviewer, Deep Reviewer, Second Opinion, Researcher, Documentation,
  Git Release, Copilot Bridge, Firestore Author, Flutter A11y

================================================================================
LAYER 2: STANDARDIZED CENTRAL ROLES (14 ROLES)
================================================================================
* Location: ~/Developer/AI-Dev-Team/roles/ (symlinked to agents/)
* Characteristics: Authoritative role definitions and constraints. Injected into
  agents. NOT standalone executables.
* Key Roles: Product Manager, Project Manager, Specification Engineer, Software
  Architect, Frontend Dev, Backend Dev, AI/ML Dev, DevOps, QA, Security, Code
  Reviewer, Documentation Eng, Research Eng, Git/GitHub Eng

================================================================================
LAYER 3: REPOSITORY & FRAMEWORK AGENTS (42 AGENTS)
================================================================================
* Location: ~/Developer/AI-Dev-Team/repos/
* Characteristics: Dedicated Python/Node runtimes, specific test suites, internal
  agent collaboration loops.
* Repositories:
  - AgentTeam (13 roles + MCP Server)
  - OpenSepia (9 sprint roles)
  - autonomous-dev-team (Dispatcher, Dev, Review)
  - OpenHands (Autonomous agent sandbox)
  - Strix (Security pentesting)
  - awesome-llm-apps (16 reference implementations)

================================================================================
LAYER 4: MODEL ROUTERS & GATEWAYS (2 GATEWAYS)
================================================================================
* AGT-074 Qwen Antigravity Bridge (FastAPI proxy at http://127.0.0.1:8000)
* AGT-075 OmniRoute Gateway (Reverse proxy for OpenAI/Claude/Gemini)

================================================================================
LAYER 5: PROJECT-LOCAL AGENTS & SUITES (2 ENCLAVES)
================================================================================
* AGT-076 LinkedIn Profile Reader (~/Developer/LinkedIn-Audit/) [PROTECTED]
* AGT-077 Portfolio QA & Security Suite (~/Developer/subhajitportfolio-2.0/) [PROTECTED]
================================================================================
```

---

## 4. Functional Domain Directory: "Who to Call for What"

When facing a specific engineering objective, consult this directory to select the exact agent, role, skill, and tool:

### 4.1 Security & Pentesting
- **Native Agent:** `Security Reviewer` (`AGT-006`) — SAST audits, code security.
- **Framework Agent:** `Strix Pentesting Agent` (`AGT-055`) — Dynamic penetration testing.
- **Framework Role:** OpenSepia `sec_analyst` (`AGT-048`), AgentTeam `Security Engineer` (`AGT-035`).
- **Standardized Role Spec:** `roles/security-engineer.md` (`AGT-024`).
- **Specialized Skills:** `007`, `vulnerability-scanner`, `security-scanning-security-sast`, `solidity-security`, `firebase-security-rules-auditor`.

### 4.2 Web Development
- **Native Agents:** `Developer Agent` (`AGT-003`) (complex fullstack), `Fast Developer` (`AGT-004`) (rapid UI).
- **Framework Roles:** OpenSepia `dev1` (`AGT-044`), AgentTeam `Frontend Developer` (`AGT-031`) & `Full-Stack Developer` (`AGT-029`).
- **Standardized Role Specs:** `roles/frontend-developer.md` (`AGT-019`), `roles/backend-developer.md` (`AGT-020`).
- **Specialized Skills:** `modern-web-guidance`, `react-patterns`, `nextjs-best-practices`, `tailwind-patterns`, `magic-ui-generator`, `animejs-animation`.

### 4.3 Coding & Implementation
- **Native Agents:** `Developer Agent` (`AGT-003`), `Fast Developer` (`AGT-004`).
- **External Multi-Model:** `GitHub Copilot Bridge` (`AGT-012`) (delegate via `gpt-5.3-codex` or `claude-sonnet-5`).
- **Autonomous Platform:** `OpenHands Agent Canvas` (`AGT-054`).
- **Specialized Skills:** `tdd-workflow`, `api-designer`, `fp-pragmatic`, `python-patterns`, `dotnet-backend`.

### 4.4 Testing & Code Review
- **Native Agents:** `Tester Agent` (`AGT-005`), `Deep Reviewer` (`AGT-007`), `Second Opinion` (`AGT-008`).
- **Framework Agents:** `Autonomous Review Agent` (`AGT-053`), OpenSepia `tester` (`AGT-046`).
- **Standardized Role Specs:** `roles/qa-engineer.md` (`AGT-023`), `roles/code-reviewer.md` (`AGT-025`).
- **Specialized Skills:** `browser-qa`, `test-guard`, `screen-reader-testing`, `benchmark`, `systematic-debugging`.

### 4.5 Research & Intelligence
- **Native Agent:** `Researcher Agent` (`AGT-009`).
- **Framework Agent:** `Understand-Anything Engine` (`AGT-056`), `AI Deep Research Agent` (`AGT-061`).
- **Standardized Role Spec:** `roles/research-engineer.md` (`AGT-027`).
- **Specialized Skills:** `deep-research`, `search-first`, `infinite-gratitude`, `literature-search-arxiv`, `pubmed-database`.

### 4.6 Documentation & Architecture
- **Native Agents:** `Architect Specialist` (`AGT-002`), `Documentation Agent` (`AGT-010`).
- **Framework Tool:** `GitHub Spec Kit CLI` (`AGT-057`).
- **Standardized Role Specs:** `roles/software-architect.md` (`AGT-018`), `roles/documentation-engineer.md` (`AGT-026`).
- **Specialized Skills:** `mermaid-expert`, `docs-architect`, `c4-architecture-c4-architecture`, `writing-for-agents`.

### 4.7 Git & GitHub Automation
- **Native Agent:** `Git Release Agent` (`AGT-011`).
- **Framework Agent:** `Autonomous Dispatcher` (`AGT-051`).
- **Standardized Role Spec:** `roles/github-engineer.md` (`AGT-028`).
- **Specialized Skills:** `smart-git-automation`, `address-github-comments`, `git-pr-review`, `resolving-merge-conflicts`.

### 4.8 Orchestration & Multi-Agent Collaboration
- **Master Orchestrator:** `AGT-001` (Antigravity Host Runtime).
- **Multi-Agent Teams:** OpenSepia (`ai-team opensepia`), AgentTeam MCP, autonomous-dev-team (`ai-team autonomous`).
- **Memory Engine:** Global Project Intelligence & Memory Engine (`scripts/project-memory` / `ai-team memory`).

---

## 5. Model Context Protocol (MCP) Ecosystem

The Antigravity host runtime has 16 configured MCP servers providing direct tool access:

| MCP Server | Runtime | Protocol | Tools Available | Core Purpose |
|---|---|---|---|---|
| **agent-team** | Node 22 (Isolated) | stdio | 44 tools (`create_task`, `add_team_member`, `share_artifact`) | Persistent multi-agent task and discussion tracking in SQLite |
| **browser** | Node 22 (Puppeteer) | stdio | 7 tools (`puppeteer_navigate`, `puppeteer_screenshot`, etc.) | Automated web testing, visual rendering, scraping |
| **git** | Python 3.12 (`mcp-env`) | stdio | 12 tools (`git_status`, `git_diff`, `git_commit`, etc.) | Local git repository operations |
| **github** | Node 22 (GitHub SDK) | stdio | 24 tools (`create_pull_request`, `create_issue`, etc.) | GitHub remote PR, issue, and code operations |
| **filesystem** | Node 22 LTS | stdio | 14 tools (`read_file`, `write_file`, `directory_tree`) | Local file reading and manipulation |
| **context7** | Custom Node.js | stdio | 2 tools (`resolve-library-id`, `query-docs`) | Third-party library documentation queries |
| **data-agent-kit**| Node.js (IDE Proxy) | stdio | 4 tools (`get_active_gcp_connection`, etc.) | Google Cloud Data Platform integration |
| **datacloud_\*** | Google Cloud Remote | remote | Remote SQL & catalog tools across BigQuery, Cloud SQL, Spanner, Dataproc, AlloyDB | Enterprise cloud data warehouse and database queries |
| **web** | Python 3.12 (`mcp-env`) | stdio | 1 tool (`fetch`) | Fast HTTP content retrieval |
| **gemini-api-docs**| Native Plugin | native | 2 tools (`gemini_search_docs`, `gemini_get_doc`) | Official upstream Gemini API documentation search |

---

## 6. Prerequisites, Dependencies & Environments

All environments are isolated within `/Users/subhajkar/Developer/AI-Dev-Team/environments/` to prevent contamination of global system Python or Node:

| Environment | Path | Binaries | Managed Services |
|---|---|---|---|
| **Isolated Node 22** | `AI-Dev-Team/environments/node22/` | `node`, `npm`, `npx` | AgentTeam MCP, GitHub MCP, Puppeteer Browser |
| **OpenSepia Python** | `AI-Dev-Team/environments/opensepia-env/` | `python`, `pytest`, `poetry` | OpenSepia multi-agent sprint simulation |
| **OpenHands Python** | `AI-Dev-Team/environments/openhands-env/` | `python`, `agent-server` | OpenHands autonomous coding canvas |
| **Spec Kit Python** | `AI-Dev-Team/environments/speckit-env/` | `python`, `specify` | GitHub Spec Kit CLI |
| **MCP Python Env** | `AI-Dev-Team/environments/mcp-env/` | `python`, `uv pip` | Git MCP, Web MCP, openpyxl catalog scripts |

---

## 7. Master Operational Invocation Matrix

| ID | Name | Entity Classification | Invocation Method / Command | Runtime / Environment | Prerequisites | Health |
|---|---|---|---|---|---|---|
| **AGT-001** | Master Orchestrator | Orchestrator | Natural Language Prompt | Antigravity Host Runtime | None | **HEALTHY** |
| **AGT-002** | Architect Specialist | Agent | `@architect "<task>"` | Antigravity Subagent | Claude / Gemini Pro | **HEALTHY** |
| **AGT-003** | Developer Agent | Agent | `@developer "<task>"` | Antigravity Subagent | Antigravity Host | **HEALTHY** |
| **AGT-004** | Fast Developer | Agent | `@fast-developer "<task>"` | Antigravity Subagent | Gemini 3 Flash | **HEALTHY** |
| **AGT-005** | Tester Agent | Agent | `@tester "<task>"` | Antigravity Subagent | Pytest / Vitest | **HEALTHY** |
| **AGT-006** | Security Reviewer | Agent | `@security-reviewer "<task>"` | Antigravity Subagent | Claude Sonnet | **HEALTHY** |
| **AGT-007** | Deep Reviewer | Agent | `@deep-reviewer "<task>"` | Antigravity Subagent | High reasoning backend | **HEALTHY** |
| **AGT-008** | Second Opinion | Agent | `@second-opinion "<task>"` | Antigravity Subagent | Orthogonal model | **HEALTHY** |
| **AGT-009** | Researcher Agent | Agent | `@researcher "<task>"` | Antigravity Subagent | Web / Docs MCP | **HEALTHY** |
| **AGT-010** | Documentation Agent | Agent | `@documentation "<task>"` | Antigravity Subagent | Markdown tooling | **HEALTHY** |
| **AGT-011** | Git Release Agent | Agent | `@git-release "<task>"` | Antigravity Subagent | Git / GitHub CLI | **HEALTHY** |
| **AGT-012** | GitHub Copilot Bridge| External Agent | `node copilot-bridge.mjs run "<p>" --model <m>` | Node 22 Sidecar | GitHub Copilot CLI | **HEALTHY** |
| **AGT-013** | Firestore Rules Author| Plugin Agent | Delegated subagent | Firebase Plugin | `firestore.rules` | **HEALTHY** |
| **AGT-014** | Flutter A11y Agent | Plugin Agent | Delegated subagent | Flutter Plugin | Flutter SDK | **HEALTHY** |
| **AGT-015–028**| Standardized Roles (14)| Agent Roles | Injected into Agent Context | `roles/*.md` Specs | Antigravity / Framework | **HEALTHY** |
| **AGT-029–041**| AgentTeam Personas (13)| Framework Roles | `agent-team:add_team_member` | AgentTeam MCP (Node 22) | SQLite `team.db` | **HEALTHY** |
| **AGT-042–050**| OpenSepia Roles (9) | Framework Roles | `ai-team opensepia --role <role>` | OpenSepia Python Env | LiteLLM / API Key | **HEALTHY** |
| **AGT-051** | Autonomous Dispatcher| Orchestrator | `ai-team autonomous` | Bash / Git Worktrees | Git 2.30+ | **HEALTHY** |
| **AGT-052** | Autonomous Dev Agent | Workflow Agent | Dispatched by AGT-051 | autonomous-dev-team | Git Worktree | **HEALTHY** |
| **AGT-053** | Autonomous Review Agent| Workflow Agent | Dispatched by AGT-051 | autonomous-dev-team | Git Worktree | **HEALTHY** |
| **AGT-054** | OpenHands Agent Canvas| Platform | `ai-team canvas` / `ai-team openhands` | Python / Docker | Docker Daemon | **HEALTHY** |
| **AGT-055** | Strix Pentesting Agent| Agent | `python -m strix.cli --help` | Python 3.14 (strix-agent) | Target / Config | **HEALTHY** |
| **AGT-056** | Understand-Anything | System / MCP | `understand-dashboard` | Node 22 / SQLite | Node 22 LTS | **HEALTHY** |
| **AGT-057** | GitHub Spec Kit CLI | Workflow Agent | `ai-team specify <cmd>` | SpecKit Python Env | SpecKit Virtualenv | **HEALTHY** |
| **AGT-058–073**| Awesome-LLM-Apps (16)| Reference Apps | `python app.py` / `streamlit run` | Python 3.12 | App-specific deps | **HEALTHY** |
| **AGT-074** | Qwen Bridge | Model Router | `uvicorn server:app --port 8000` | FastAPI Proxy | Local LLM Engine | **HEALTHY** |
| **AGT-075** | OmniRoute Gateway | Model Router | `node gateway.js` / `ai-team omniroute`| Node.js Reverse Proxy | Node.js | **HEALTHY** |
| **AGT-076** | LinkedIn Profile Reader| Project Tool | Internal script execution | Protected Project | LinkedIn-Audit Env | **HEALTHY** |
| **AGT-077** | Portfolio QA Suite | Project Suite | `npx playwright test` | Protected Project | Portfolio Node Env | **HEALTHY** |

---

## 8. Health & Verification Summary

To verify the ecosystem at any time, execute the unified health suite:

```bash
# 1. Check all environment runtimes, symlinks, and protected projects
/Users/subhajkar/Developer/AI-Dev-Team/scripts/ai-team doctor

# 2. Run unit and integration tests across all frameworks
/Users/subhajkar/Developer/AI-Dev-Team/scripts/ai-team test

# 3. Check status of all 16 MCP servers
/Users/subhajkar/Developer/AI-Dev-Team/scripts/ai-team mcp status

# 4. Inspect current ecosystem status
ai-team status
```

**Overall Ecosystem Health:** **98 / 98 Healthy (100% operational readiness)**.  
Following the runtime health audit and repair pass:
- `AGT-055` Strix Pentesting Agent CLI entrypoint was repaired and validated (v1.6.2).
- Ponytail (`DietrichGebert/ponytail` v4.10.0) was centralized, integrated, and validated across 121 tests (core repo, 6 skills, stdio MCP server, 6 chat commands, 4 lifecycle hooks, and platform adapters).
- The ecosystem is governed by exactly ONE master Excel workbook: `/Users/subhajkar/Developer/AI-Dev-Team/Agent-Catalog.xlsx` containing 16 dedicated worksheets.
