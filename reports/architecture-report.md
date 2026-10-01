# Centralized AI Development Team — Architecture Report

**Date:** 2026-09-16  
**Ecosystem Root:** `~/Developer/AI-Dev-Team/`  
**Host:** macOS 27.0 arm64  
**Primary Integration:** Google Antigravity  

---

## 1. Executive Architectural Overview

The **AI Development Team** ecosystem establishes a unified, multi-framework autonomous engineering organization. It merges seven distinct GitHub projects into an orchestrated hierarchy, ensuring each tool performs its native purpose without competing for primary control:

```
                                  USER & GOOGLE ANTIGRAVITY
                                              │
                                              ▼
                        ┌───────────────────────────────────────────┐
                        │   ~/Developer/AI-Dev-Team/scripts/ai-team  │
                        └─────────────────────┬─────────────────────┘
                                              │
         ┌────────────────────────────────────┼────────────────────────────────────┐
         ▼                                    ▼                                    ▼
┌──────────────────┐               ┌──────────────────────┐             ┌─────────────────────┐
│ SPECIFICATION    │               │ ORCHESTRATION & TEAM │             │ KNOWLEDGE & CODE    │
│ GitHub Spec Kit  │               │ OpenSepia            │             │ Understand Anything │
│ (`specify-cli`)  │               │ - Agile Sprint Cycles│             │ - Tree-sitter & AST │
│ - Constitutions  │               │ - PM/PO/Dev/QA/Sec   │             │ - Knowledge Graph   │
│ - Spec Plans     │               │                      │             │ - Code Exploration  │
│ - Tasks Matrix   │               │ autonomous-dev-team  │             │ - Onboarding Tours  │
│                  │               │ - Worktree Isolation │             └─────────────────────┘
└────────┬─────────┘               │ - TDD Pipeline       │                        │
         │                         │ - Multi-agent Review │                        │
         │                         └──────────┬───────────┘                        │
         │                                    │                                    │
         └────────────────────────────────────┼────────────────────────────────────┘
                                              │
                                              ▼
                                 ┌─────────────────────────┐
                                 │     AgentTeam MCP       │
                                 │     (44 Stdio Tools)    │
                                 │  - Projects & Summaries │
                                 │  - Persistent SQLite    │
                                 │  - Tasks & Work Entries │
                                 │  - Artifacts & Journal  │
                                 └────────────┬────────────┘
                                              │
         ┌────────────────────────────────────┼────────────────────────────────────┐
         ▼                                    ▼                                    ▼
┌──────────────────┐               ┌──────────────────────┐             ┌─────────────────────┐
│ 14 STANDARDIZED  │               │ CENTRAL SKILLS (1163)│             │ CONTROL CANVAS      │
│ AGENT ROLES      │               │ - global/            │             │ OpenHands / Canvas  │
│ - PM / PO        │               │ - plugins/           │             │ - agent-server      │
│ - Architect      │               │ - antigravity-skills │             │ - Web UI Dashboard  │
│ - Dev / QA       │               │ - agentic-awesome    │             │ - Local Sandboxing  │
│ - DevOps / Sec   │               │ - repository-specific│             └─────────────────────┘
│ - Spec / Research│               │ - builtin / codex    │
└──────────────────┘               └──────────────────────┘
```

---

## 2. Layer Responsibilities & Ownership

### 1. Primary Orchestrator: Google Antigravity (`agy`)
- **Role:** High-level interactive planning, contextual task assignment, tool calling, and human-in-the-loop pair programming.
- **Integration Seam:** Configured via `~/.gemini/config/skills.json` and `~/.gemini/config/mcp_config.json`.

### 2. Specification Layer: GitHub Spec Kit (`spec-kit`)
- **Role:** Contract-first development bootstrap.
- **Tools:** `specify init`, `specify check`, template library (`constitution`, `spec`, `plan`, `tasks`).
- **Runtime:** Isolated Python virtual environment (`environments/speckit-env`).

### 3. Project Management & Continuous Sprints: OpenSepia
- **Role:** Multi-cycle autonomous sprint execution, persistent Kanban boards, cross-cycle reviews, and automated backlog refinement.
- **Agents:** Product Owner (`po`), Project Manager (`pm`), Developers (`dev1`, `dev2`), Tester, DevOps, Security Analyst.
- **Runtime:** Isolated Python virtual environment (`environments/opensepia-env`).

### 4. Git Worktree & Automated TDD Pipeline: autonomous-dev-team
- **Role:** Autonomous issue scanner and branch dispatcher. Turns issues into verified, reviewed pull requests using git worktree isolation.
- **Supported CLIs:** Native adapters for Antigravity (`agy`), Codex (`codex`), and Claude Code (`claude`).
- **Configuration:** `configs/autonomous.conf`.

### 5. Persistent State & Tool Context: AgentTeam MCP Server
- **Role:** SQLite-backed Model Context Protocol server exposing 44 granular software development tools across 12 domains.
- **Runtime:** Isolated Node.js 22 LTS runtime (`environments/node22/bin/node`) guaranteeing binary stability for `better-sqlite3`.

### 6. Repository-Understanding & Static Analysis: Understand Anything
- **Role:** Codebase indexing, AST parsing via tree-sitter, interactive knowledge graphs, and codebase onboarding guides.
- **Components:** `understand-anything-plugin`, CLI scripts, 10 specialized code analyzers, and 9 interactive skills.

### 7. Skills & Capabilities Ecosystem
- **Total Unique Top-Level Skills:** 1,163 skills.
- **Categorized Symlink Collections:**
  - `skills/global/`: 59 skills
  - `skills/plugins/`: 113 skills
  - `skills/builtin/`: 5 skills
  - `skills/codex/`: 6 skills
  - `skills/antigravity-skills/`: 305 curated skills
  - `skills/agentic-awesome-skills/`: 855 curated development/AI/cloud skills
  - `skills/repository-specific/`: Skills from Understand-Anything (9), autonomous-dev-team (5), and AgentTeam (1).

---

## 3. Standardized 14-Agent Engineering Team

All agents operate under `~/Developer/AI-Dev-Team/agents/` and adhere to `_base-protocol.md`:
1. **Product Manager** (`product-manager.md`): User stories, requirements, prioritization.
2. **Project Manager** (`project-manager.md`): Task manifests, sprints, agent dispatching.
3. **Specification Engineer** (`specification-engineer.md`): Spec-Driven Development, constitutions, contracts.
4. **Software Architect** (`software-architect.md`): System topology, API schemas, ADRs.
5. **Frontend Developer** (`frontend-developer.md`): Web/mobile UI, component architecture, accessibility.
6. **Backend Developer** (`backend-developer.md`): Microservices, APIs, database integration.
7. **AI/ML Developer** (`aiml-developer.md`): LLM APIs (Gemini, Claude, OpenAI), RAG, embeddings.
8. **DevOps Engineer** (`devops-engineer.md`): Containerization, multi-stage Docker, CI/CD pipelines.
9. **QA Engineer** (`qa-engineer.md`): Automated testing, contract verification, regression tests.
10. **Security Engineer** (`security-engineer.md`): SAST, secret auditing, container hardening.
11. **Code Reviewer** (`code-reviewer.md`): Code quality gates, clean architecture, approval verdicts.
12. **Documentation Engineer** (`documentation-engineer.md`): Technical writing, READMEs, API specs.
13. **Research Engineer** (`research-engineer.md`): Algorithm research, deep investigations, literature analysis.
14. **Git/GitHub Engineer** (`github-engineer.md`): Worktrees, rebase management, GitHub Actions automation.

---

## 4. Multi-Model Support Matrix

| Framework | Google Gemini | Anthropic Claude | OpenAI / Codex | Local Models (Ollama/vLLM) |
|---|---|---|---|---|
| **Antigravity CLI (`agy`)** | Native Primary | Supported | Supported | Supported via OpenAI compatibility |
| **autonomous-dev-team** | Native (`agy` adapter) | Native (`claude`) | Native (`codex`) | Generic `-p` CLI fallback |
| **OpenSepia** | Supported via CLI | Native CLI runner | Supported via Codex | Supported via proxy |
| **AgentTeam** | Supported via MCP | Native prompt format | Supported via MCP | Supported via MCP |
| **Understand Anything** | Supported via CLI | Native plugin | Supported via CLI | Supported via LiteLLM |
| **GitHub Spec Kit** | Auto-detected (`check`)| Auto-detected | Auto-detected | Compatible |
| **OpenHands** | GenAI SDK | Anthropic SDK | OpenAI SDK | Supported via LiteLLM / Ollama |

---

## 5. Security & Isolation Strategy

1. **Rule 18 Enforcement (Offensive Tooling Filter):** 72 offensive security/pentesting tools (exploit builders, reverse shells, privilege escalators, malware analyzers) were identified and excluded from automated workflows.
2. **Zero Plaintext Secrets:** No API keys, credentials, or tokens are committed or stored in plain text.
3. **Environment Isolation:** Runtimes are partitioned into `environments/node22/`, `environments/opensepia-env/`, `environments/speckit-env/`, and `environments/openhands-env/`, preventing system-wide dependency pollution.
4. **Workspace Protection:** Existing projects (`LinkedIn-Audit`, `subhajitportfolio-2.0`) are quarantined and protected from all installer activity.
