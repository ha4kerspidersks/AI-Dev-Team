# Global AI Skill & Tooling Registry

**Central Environment:** `/Users/subhajkar/Developer/AI-Dev-Team`  
**Registry Version:** 3.0.0  
**Last Updated:** 2026-09-17  
**Architecture:** Centralized Reusable Ecosystem (Zero Local Project Duplication)  

---

## 1. Global Skills Registry

| Name | Type | Source | URL | Local Path | Commit / Version | Install Method | Supported Agents | Dependencies | Status | Primary Use | Conflicts / Resolution |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **spec-driven-development** | Global Skill | `addyosmani/agent-skills` | `https://github.com/addyosmani/agent-skills.git` | `skills/addyosmani/skills/spec-driven-development` | `be4e44a9` (v0.6.9) | Central Namespace + Flat Link | Universal, Antigravity, Claude, Codex | Spec Kit / Markdown | Verified Active | Specification engineering | None |
| **idea-refine** | Global Skill | `addyosmani/agent-skills` | `https://github.com/addyosmani/agent-skills.git` | `skills/addyosmani/skills/idea-refine` | `be4e44a9` (v0.6.9) | Central Namespace + Flat Link | Universal, Antigravity, Claude, Codex | None | Verified Active | Requirement elicitation | None |
| **using-agent-skills** | Global Skill | `addyosmani/agent-skills` | `https://github.com/addyosmani/agent-skills.git` | `skills/addyosmani/skills/using-agent-skills` | `be4e44a9` (v0.6.9) | Central Namespace + Flat Link | Universal, Antigravity, Claude, Codex | References sidecar | Verified Active | Meta-skill for agent skill execution | None |
| **planning-and-task-breakdown** | Global Skill | `addyosmani/agent-skills` | `https://github.com/addyosmani/agent-skills.git` | `skills/addyosmani/skills/planning-and-task-breakdown` | `be4e44a9` (v0.6.9) | Central Namespace + Flat Link | Universal, Antigravity, Claude, Codex | References sidecar | Verified Active | Phased task planning & decomposition | None |
| **incremental-implementation** | Global Skill | `addyosmani/agent-skills` | `https://github.com/addyosmani/agent-skills.git` | `skills/addyosmani/skills/incremental-implementation` | `be4e44a9` (v0.6.9) | Central Namespace + Flat Link | Universal, Antigravity, Claude, Codex | References sidecar | Verified Active | Step-by-step TDD delivery | None |
| **ci-cd-and-automation** | Global Skill | `addyosmani/agent-skills` | `https://github.com/addyosmani/agent-skills.git` | `skills/addyosmani/skills/ci-cd-and-automation` | `be4e44a9` (v0.6.9) | Central Namespace + Flat Link | Universal, Antigravity, Claude, Codex | None | Verified Active | CI/CD pipeline automation | None |
| **constraint-driven-development** | Global Skill | `addyosmani/agent-skills` | `https://github.com/addyosmani/agent-skills.git` | `skills/addyosmani/skills/constraint-driven-development` | `be4e44a9` (v0.6.9) | Central Namespace + Flat Link | Universal, Antigravity, Claude, Codex | Floor guard ref | Verified Active | Invariant-first software development | None |
| **deprecation-and-migration** | Global Skill | `addyosmani/agent-skills` | `https://github.com/addyosmani/agent-skills.git` | `skills/addyosmani/skills/deprecation-and-migration` | `be4e44a9` (v0.6.9) | Central Namespace + Flat Link | Universal, Antigravity, Claude, Codex | None | Verified Active | Safe code deprecation & refactoring | None |
| **interview-me** | Global Skill | `addyosmani/agent-skills` | `https://github.com/addyosmani/agent-skills.git` | `skills/addyosmani/skills/interview-me` | `be4e44a9` (v0.6.9) | Central Namespace + Flat Link | Universal, Antigravity, Claude, Codex | None | Verified Active | Design alignment interview | None |
| **doubt-driven-development** | Global Skill | `addyosmani/agent-skills` | `https://github.com/addyosmani/agent-skills.git` | `skills/addyosmani/skills/doubt-driven-development` | `be4e44a9` (v0.6.9) | Central Namespace + Flat Link | Universal, Antigravity, Claude, Codex | None | Verified Active | Rigorous requirement challenge | None |
| **source-driven-development** | Global Skill | `addyosmani/agent-skills` | `https://github.com/addyosmani/agent-skills.git` | `skills/addyosmani/skills/source-driven-development` | `be4e44a9` (v0.6.9) | Central Namespace + Flat Link | Universal, Antigravity, Claude, Codex | Git CLI | Verified Active | Git history driven engineering | None |
| **documentation-and-adrs** | Global Skill | `addyosmani/agent-skills` | `https://github.com/addyosmani/agent-skills.git` | `skills/addyosmani/skills/documentation-and-adrs` | `be4e44a9` (v0.6.9) | Central Namespace + Flat Link | Universal, Antigravity, Claude, Codex | None | Verified Active | Architecture decision records | None |
| **addyosmani-test-driven-development** | Global Skill | `addyosmani/agent-skills` | `https://github.com/addyosmani/agent-skills.git` | `skills/addyosmani/skills/test-driven-development` | `be4e44a9` (v0.6.9) | Namespaced Symlink | Universal, Antigravity, Claude, Codex | `testing-patterns.md` | Verified Active | Authoritative TDD with JS/TS patterns | Namespaced to prevent collision with Superpowers TDD |
| **addyosmani-code-review-and-quality** | Global Skill | `addyosmani/agent-skills` | `https://github.com/addyosmani/agent-skills.git` | `skills/addyosmani/skills/code-review-and-quality` | `be4e44a9` (v0.6.9) | Namespaced Symlink | Universal, Antigravity, Claude, Codex | `definition-of-done.md` | Verified Active | Authoritative code review bar | Namespaced to preserve legacy review link |
| **graphify** | Global Skill | `Graphify-Labs/graphify` | `https://github.com/Graphify-Labs/graphify.git` | `skills/graphify` | `26b02b5e` (v0.9.63) | Root Dir + References | Universal, Antigravity, Claude, Codex | `graphify` CLI, NetworkX | Verified Active | AST extraction & knowledge graph | None |
| **ponytail** | Global Skill | `DietrichGebert/ponytail` | `https://github.com/DietrichGebert/ponytail.git` | `skills/ponytail` | `e3ba2aa6` (v4.10.0) | Root Dir + Flat Links | Universal, Antigravity, Claude, Codex | None | Verified Active | Lazy senior dev / YAGNI | None |
| **ponytail-audit** | Global Skill | `DietrichGebert/ponytail` | `https://github.com/DietrichGebert/ponytail.git` | `skills/ponytail/skills/ponytail-audit` | `e3ba2aa6` (v4.10.0) | Flat Symlink | Universal, Antigravity, Claude, Codex | None | Verified Active | Whole-repo complexity audit | None |
| **ponytail-debt** | Global Skill | `DietrichGebert/ponytail` | `https://github.com/DietrichGebert/ponytail.git` | `skills/ponytail/skills/ponytail-debt` | `e3ba2aa6` (v4.10.0) | Flat Symlink | Universal, Antigravity, Claude, Codex | None | Verified Active | Debt ledger tracking | None |
| **ponytail-gain** | Global Skill | `DietrichGebert/ponytail` | `https://github.com/DietrichGebert/ponytail.git` | `skills/ponytail/skills/ponytail-gain` | `e3ba2aa6` (v4.10.0) | Flat Symlink | Universal, Antigravity, Claude, Codex | None | Verified Active | Ponytail scoreboard | None |
| **ponytail-help** | Global Skill | `DietrichGebert/ponytail` | `https://github.com/DietrichGebert/ponytail.git` | `skills/ponytail/skills/ponytail-help` | `e3ba2aa6` (v4.10.0) | Flat Symlink | Universal, Antigravity, Claude, Codex | None | Verified Active | Ponytail command reference | None |
| **ponytail-review** | Global Skill | `DietrichGebert/ponytail` | `https://github.com/DietrichGebert/ponytail.git` | `skills/ponytail/skills/ponytail-review` | `e3ba2aa6` (v4.10.0) | Flat Symlink | Universal, Antigravity, Claude, Codex | None | Verified Active | Overengineering code review | None |
| **strix** (suite: 9 skills) | Security Skills | `usestrix/strix` | `https://github.com/usestrix/strix.git` | `skills/strix/skills/*` | `910c1ea4` (v1.6.2) | Root Dir + Flat Links | Universal, Antigravity, Claude, Codex | Strix CLI | Verified Active | Autonomous AI penetration testing | None |
| **context7-cli** | Doc Skill | `upstash/context7` | `https://github.com/upstash/context7.git` | `skills/context7/skills/context7-cli` | `dedb03d5` (v0.5.11) | Root Dir + Flat Link | Universal, Antigravity, Claude, Codex | `ctx7` CLI | Verified Active | Documentation CLI search | None |
| **context7-mcp** | Doc Skill | `upstash/context7` | `https://github.com/upstash/context7.git` | `skills/context7/skills/context7-mcp` | `dedb03d5` (v4.1.1) | Root Dir + Flat Link | Universal, Antigravity, Claude, Codex | `@upstash/context7-mcp` | Verified Active | Documentation MCP queries | None |
| **find-docs** | Doc Skill | `upstash/context7` | `https://github.com/upstash/context7.git` | `skills/context7/skills/find-docs` | `dedb03d5` (v1.0.0) | Root Dir + Flat Link | Universal, Antigravity, Claude, Codex | Context7 API | Verified Active | Up-to-date library search | None |
| **brainstorming** | Methodology Skill | `obra/superpowers` | `https://github.com/obra/superpowers.git` | `.gemini/config/plugins/superpowers/skills/brainstorming` | `b36e0829` (v6.3.0) | Official `agy plugin` + Flat Link | Universal, Antigravity, Claude, Codex | None | Verified Active | Socratic design & brainstorming | None |
| **writing-plans** | Methodology Skill | `obra/superpowers` | `https://github.com/obra/superpowers.git` | `.gemini/config/plugins/superpowers/skills/writing-plans` | `b36e0829` (v6.3.0) | Official `agy plugin` + Flat Link | Universal, Antigravity, Claude, Codex | None | Verified Active | Implementation plan synthesis | None |
| **dispatching-parallel-agents** | Methodology Skill | `obra/superpowers` | `https://github.com/obra/superpowers.git` | `.gemini/config/plugins/superpowers/skills/dispatching-parallel-agents` | `b36e0829` (v6.3.0) | Official `agy plugin` + Flat Link | Universal, Antigravity, Claude, Codex | AgentTeam / subagents | Verified Active | Parallel agent fan-out | None |
| **systematic-debugging** | Methodology Skill | `obra/superpowers` | `https://github.com/obra/superpowers.git` | `.gemini/config/plugins/superpowers/skills/systematic-debugging` | `b36e0829` (v6.3.0) | Official `agy plugin` + Flat Link | Universal, Antigravity, Claude, Codex | None | Verified Active | 4-phase root cause debugging | None |
| **using-superpowers** | Methodology Skill | `obra/superpowers` | `https://github.com/obra/superpowers.git` | `.gemini/config/plugins/superpowers/skills/using-superpowers` | `b36e0829` (v6.3.0) | Official `agy plugin` + Flat Link | Universal, Antigravity, Claude, Codex | SessionStart Hook | Verified Active | Superpowers framework bootstrap | None |
| **writing-skills** | Methodology Skill | `obra/superpowers` | `https://github.com/obra/superpowers.git` | `.gemini/config/plugins/superpowers/skills/writing-skills` | `b36e0829` (v6.3.0) | Official `agy plugin` + Flat Link | Universal, Antigravity, Claude, Codex | None | Verified Active | TDD-style skill authoring | None |
| **superpowers-subagent-driven-development** | Methodology Skill | `obra/superpowers` | `https://github.com/obra/superpowers.git` | `.gemini/config/plugins/superpowers/skills/subagent-driven-development` | `b36e0829` (v6.3.0) | Namespaced Symlink | Universal, Antigravity, Claude, Codex | Subagents | Verified Active | Subagent per task methodology | Namespaced to preserve legacy symlink |
| **grill-me** | Developer Skill | `mattpocock/skills` | `https://github.com/mattpocock/skills.git` | `skills/mattpocock/productivity/grill-me` | `74ca5fe0` | Categorized Dir + Flat Link | Universal, Antigravity, Claude, Codex | None | Verified Active | Interactive design grill | None |
| **grill-with-docs** | Developer Skill | `mattpocock/skills` | `https://github.com/mattpocock/skills.git` | `skills/mattpocock/engineering/grill-with-docs` | `74ca5fe0` | Categorized Dir + Flat Link | Universal, Antigravity, Claude, Codex | None | Verified Active | Documentation-based design grill | None |
| **domain-modeling** | Developer Skill | `mattpocock/skills` | `https://github.com/mattpocock/skills.git` | `skills/mattpocock/engineering/domain-modeling` | `74ca5fe0` | Categorized Dir + Flat Link | Universal, Antigravity, Claude, Codex | None | Verified Active | Domain entity modeling | None |
| **codebase-design** | Developer Skill | `mattpocock/skills` | `https://github.com/mattpocock/skills.git` | `skills/mattpocock/engineering/codebase-design` | `74ca5fe0` | Categorized Dir + Flat Link | Universal, Antigravity, Claude, Codex | None | Verified Active | Architecture & module design | None |
| **wayfinder** | Developer Skill | `mattpocock/skills` | `https://github.com/mattpocock/skills.git` | `skills/mattpocock/engineering/wayfinder` | `74ca5fe0` | Categorized Dir + Flat Link | Universal, Antigravity, Claude, Codex | None | Verified Active | Navigation & codebase mapping | None |
| **wizard** | Developer Skill | `mattpocock/skills` | `https://github.com/mattpocock/skills.git` | `skills/mattpocock/engineering/wizard` | `74ca5fe0` | Categorized Dir + Flat Link | Universal, Antigravity, Claude, Codex | None | Verified Active | Step-by-step guidance wizard | None |
| **to-spec** | Developer Skill | `mattpocock/skills` | `https://github.com/mattpocock/skills.git` | `skills/mattpocock/engineering/to-spec` | `74ca5fe0` | Categorized Dir + Flat Link | Universal, Antigravity, Claude, Codex | None | Verified Active | Fast spec writing | None |
| **to-tickets** | Developer Skill | `mattpocock/skills` | `https://github.com/mattpocock/skills.git` | `skills/mattpocock/engineering/to-tickets` | `74ca5fe0` | Categorized Dir + Flat Link | Universal, Antigravity, Claude, Codex | None | Verified Active | Spec to ticket breakdown | None |
| **wait-what** | Developer Skill | `mattpocock/skills` | `https://github.com/mattpocock/skills.git` | `skills/mattpocock/productivity/wait-what` | `74ca5fe0` | Categorized Dir + Flat Link | Universal, Antigravity, Claude, Codex | None | Verified Active | Sanity checking & doubt analysis | None |
| **mattpocock-tdd** | Developer Skill | `mattpocock/skills` | `https://github.com/mattpocock/skills.git` | `skills/mattpocock/engineering/tdd` | `74ca5fe0` | Namespaced Symlink | Universal, Antigravity, Claude, Codex | None | Verified Active | Red-Green-Refactor TDD | Namespaced to preserve legacy TDD |
| **agentic-engineering** | Agent Platform Skill | `affaan-m/ECC` | `https://github.com/affaan-m/ECC.git` | `plugins/ecc/skills/agentic-engineering` | `8321021c` (v2.2.1) | Plugins Dir + Flat Link | Universal, Antigravity, Claude, Codex | None | Verified Active | Agentic engineering methodology | None |
| **agent-architecture-audit** | Agent Platform Skill | `affaan-m/ECC` | `https://github.com/affaan-m/ECC.git` | `plugins/ecc/skills/agent-architecture-audit` | `8321021c` (v2.2.1) | Plugins Dir + Flat Link | Universal, Antigravity, Claude, Codex | None | Verified Active | Multi-agent architecture audit | None |
| **agent-eval** | Agent Platform Skill | `affaan-m/ECC` | `https://github.com/affaan-m/ECC.git` | `plugins/ecc/skills/agent-eval` | `8321021c` (v2.2.1) | Plugins Dir + Flat Link | Universal, Antigravity, Claude, Codex | None | Verified Active | Agent benchmark evaluation | None |
| **browser-qa** | QA Skill | `affaan-m/ECC` | `https://github.com/affaan-m/ECC.git` | `plugins/ecc/skills/browser-qa` | `8321021c` (v2.2.1) | Plugins Dir + Flat Link | Universal, Antigravity, Claude, Codex | Playwright | Verified Active | Browser QA validation loop | None |
| **verification-loop** | QA Skill | `affaan-m/ECC` | `https://github.com/affaan-m/ECC.git` | `plugins/ecc/skills/verification-loop` | `8321021c` (v2.2.1) | Plugins Dir + Flat Link | Universal, Antigravity, Claude, Codex | None | Verified Active | Closed-loop verification | None |
| **strategic-compact** | Context Skill | `affaan-m/ECC` | `https://github.com/affaan-m/ECC.git` | `plugins/ecc/skills/strategic-compact` | `8321021c` (v2.2.1) | Plugins Dir + Flat Link | Universal, Antigravity, Claude, Codex | None | Verified Active | Strategic context compaction | None |
| **unified-memory** | Memory Skill | `affaan-m/ECC` | `https://github.com/affaan-m/ECC.git` | `plugins/ecc/skills/unified-memory` | `8321021c` (v2.2.1) | Plugins Dir + Flat Link | Universal, Antigravity, Claude, Codex | None | Verified Active | Cross-session memory coordination | None |
| **ecc-tdd-workflow** | Agent Platform Skill | `affaan-m/ECC` | `https://github.com/affaan-m/ECC.git` | `plugins/ecc/skills/tdd-workflow` | `8321021c` (v2.2.1) | Namespaced Symlink | Universal, Antigravity, Claude, Codex | None | Verified Active | ECC TDD implementation | Namespaced to prevent collision |
| **commit-archaeologist** | Selective Skill | `Shubhamsaboo/awesome-llm-apps` | `https://github.com/Shubhamsaboo/awesome-llm-apps.git` | `skills/awesome-llm-apps/commit-archaeologist` | `f163bb5a` | Selective Dir + Flat Link | Universal, Antigravity, Claude, Codex | Git CLI | Verified Active | Reconstruct why code exists via git | None |
| **dependency-doctor** | Selective Skill | `Shubhamsaboo/awesome-llm-apps` | `https://github.com/Shubhamsaboo/awesome-llm-apps.git` | `skills/awesome-llm-apps/dependency-doctor` | `f163bb5a` | Selective Dir + Flat Link | Universal, Antigravity, Claude, Codex | Python/Node manifests | Verified Active | Manifest footgun & dependency rot audit | None |
| **scope-creep-detector** | Selective Skill | `Shubhamsaboo/awesome-llm-apps` | `https://github.com/Shubhamsaboo/awesome-llm-apps.git` | `skills/awesome-llm-apps/scope-creep-detector` | `f163bb5a` | Selective Dir + Flat Link | Universal, Antigravity, Claude, Codex | Git diff | Verified Active | Prevent pull request scope creep | None |
| **first-reader** | Selective Skill | `Shubhamsaboo/awesome-llm-apps` | `https://github.com/Shubhamsaboo/awesome-llm-apps.git` | `skills/awesome-llm-apps/first-reader` | `f163bb5a` | Selective Dir + Flat Link | Universal, Antigravity, Claude, Codex | Python stdlib | Verified Active | Simulate real human reader/skimmer | None |
| **project-graveyard** | Selective Skill | `Shubhamsaboo/awesome-llm-apps` | `https://github.com/Shubhamsaboo/awesome-llm-apps.git` | `skills/awesome-llm-apps/project-graveyard` | `f163bb5a` | Selective Dir + Flat Link | Universal, Antigravity, Claude, Codex | Git history | Verified Active | Autopsy & resurrect dead side projects | None |
| **advisor-orchestrator-worker** | Selective Skill | `Shubhamsaboo/awesome-llm-apps` | `https://github.com/Shubhamsaboo/awesome-llm-apps.git` | `skills/awesome-llm-apps/advisor-orchestrator-worker` | `f163bb5a` | Selective Dir + Flat Link | Universal, Antigravity, Claude, Codex | None | Verified Active | Multi-model advisor-worker fan-out | None |
| **thinking-out-loud** | Selective Skill | `Shubhamsaboo/awesome-llm-apps` | `https://github.com/Shubhamsaboo/awesome-llm-apps.git` | `skills/awesome-llm-apps/thinking-out-loud` | `f163bb5a` | Selective Dir + Flat Link | Universal, Antigravity, Claude, Codex | None | Verified Active | Echo brief contract for voice dictation | None |

*(Total indexed skills in repository: 1,361 entries across all namespaces).*

---

## 2. Global Plugins Registry

| Name | Source URL | Commit / Version | Global Location | Runtime Location | Manifest Type | Components Provided | Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **superpowers** | `https://github.com/obra/superpowers.git` | `b36e0829` (v6.3.0) | `plugins/superpowers` | `/Users/subhajkar/.gemini/config/plugins/superpowers` | `plugin.json` / `gemini-extension.json` | 14 Skills, SessionStart Hook, Subagent Workflows | Verified Active (`agy plugin list`) |
| **ecc-universal** | `https://github.com/affaan-m/ECC.git` | `8321021c` (v2.2.1) | `plugins/ecc` | `plugins/ecc/` | `package.json` / `.gemini/GEMINI.md` | 292 Skills, 68 Agents, 23 Rules, 94 Commands | Verified Active |

---

## 3. Global CLI & Runtimes

| Name | Binary Location | Install Mechanism | Version | Verification Command | Primary Purpose | Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **graphify** | `/Users/subhajkar/.local/bin/graphify` | `uv tool install graphifyy` | `0.9.63` | `graphify install --help` | AST extraction, community clustering, knowledge graph query engine | Verified Active |
| **strix** | `/Users/subhajkar/.local/bin/strix` | `uv tool install strix-agent` | `1.6.2` | `strix --version` | Autonomous AI penetration tester & application security auditor | Verified Active |
| **ctx7** | `/opt/homebrew/bin/ctx7` | `npm install -g ctx7` | `0.5.11` | `ctx7 --version` | Up-to-date documentation search and library resolver CLI | Verified Active |
| **agy** | `/Users/subhajkar/.local/bin/agy` | System Antigravity CLI | System | `agy plugin list` | Native agent CLI and plugin manager | Verified Active |

---

## 4. Global MCP Services

| Server Name | Module / Entry Point | Runtime Engine | Transport | Config Path | Exposed Tools | Routing Scope | Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **context7** | `mcp/node_modules/@upstash/context7-mcp/dist/index.js` | `node22` (v22.8.2) | Stdio JSON-RPC | `configs/mcp_config.json` | `resolve-library-id`, `query-docs` | External documentation for modern libraries (React, Vite, Three.js, Playwright, etc.) | Verified Active |
| **graphify-mcp** | `/Users/subhajkar/.local/bin/graphify-mcp` | Python 3.14 (`uv tool` env) | Stdio / Streamable HTTP | On-demand / CLI | `query`, `path`, `explain` | GraphRAG queries over generated codebase knowledge graphs | Verified Ready |

---

## 5. Global Infrastructure

| System | Directory Location | Upstream Git Repo | Version / Commit | Default Port | Routing & Gateway Role | Operational Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **OmniRoute** | `infrastructure/omniroute/` | `diegosouzapw/OmniRoute` | `3.8.51` (`0d089e7e`) | `20128` | Multi-model router with 359 providers, RTK compression, and fallback routing | Installed (On-Demand / Non-Conflicting) |
| **FreeLLMAPI** | `/Applications/FreeLLMAPI.app` | System Application | Live Local | `31415` | Local LLM proxy engine (Active) | Active System Service |

---

## 6. Reference-Only / Not Global

To prevent future agents from re-cloning or polluting the global skills directory with demo applications, the following components are explicitly designated as **REFERENCE LIBRARIES / RUNNABLE APPS ONLY**:

| Component / Subdirectory | Source Repository | Purpose | Why Excluded from Global Skills |
| :--- | :--- | :--- | :--- |
| `starter_ai_agents/` | `awesome-llm-apps` | 20+ beginner AI agent demos (financial, research, routing) | Runnable tutorial apps requiring standalone API keys; not modular agent skills. |
| `voice_ai_agents/` | `awesome-llm-apps` | Real-time speech & conversational agent examples | Full application code with frontend/audio drivers; not reusable prompt skills. |
| `rag_tutorials/` | `awesome-llm-apps` | RAG implementations with various vector DBs | Standalone tutorial scripts; knowledge graph RAG is covered globally by Graphify. |
| `mcp_ai_agents/` | `awesome-llm-apps` | Example applications connecting to MCP servers | Runnable sample apps; MCP infrastructure is managed in `configs/mcp_config.json`. |
| `self-improving-agent-skills/` | `awesome-llm-apps` | Full-stack web application (FastAPI + React) | Multi-container application requiring local database; reference implementation. |
| `evals/` | `awesome-llm-apps` | Test harness for evaluating agent skills | Offline evaluation benchmark; available in `repos/awesome-llm-apps/agent_skills/evals/`. |
| `electron/` / `desktop/` | `OmniRoute` | Desktop Electron application wrapper | Infrastructure client; not an agent capability. |
