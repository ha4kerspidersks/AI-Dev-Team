# AI-Dev-Team: Portable Multi-Agent Engineering Ecosystem

[![Security Audit](https://img.shields.io/badge/Security_Audit-PASS-brightgreen.svg)](#security--credentials)
[![Doctor Health](https://img.shields.io/badge/Doctor-100%25_Healthy-success.svg)](#ecosystem-health-check)
[![Skills](https://img.shields.io/badge/Skills-1%2C371-blue.svg)](#skills-catalog)
[![Agents](https://img.shields.io/badge/Agents-29-purple.svg)](#standardized-agent-roles)
[![FreeLLMAPI](https://img.shields.io/badge/FreeLLMAPI-19_Agents-orange.svg)](#freellmapi-multi-agent-integration)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

An enterprise-grade, reproducible, portable multi-agent software engineering organization, toolchain, and model routing foundation. Designed for seamless execution with **Google Antigravity**, **VS Code**, **Claude Code**, **Codex**, and autonomous CLI agents.

---

## Architecture Overview

```
AI-Dev-Team/
├── agents/             # 29 standardized AI agent definitions & protocols
├── roles/              # 30 specialized engineering roles
├── skills/             # 1,371 centralized development, security, & cloud skills
├── mcp/                # 18 MCP server definitions (8,866 tool signatures)
├── orchestrators/      # Multi-agent review pipelines and orchestration engines
├── workflows/          # TDD cycles, security audits, diff reviews, git releases
├── freellmapi-agents/  # FreeLLMAPI multi-agent wrappers (flm, 19 CLI agents)
├── registry/           # manifest.yaml and ecosystem schema specifications
├── scripts/            # bootstrap.sh, doctor.sh, snapshot.sh, restore.sh, ai-team
├── docs/               # Architecture, security audit, and integration specs
├── inventory/          # Comprehensive agent and capability manifests
└── Agent-Catalog.xlsx  # 19-sheet canonical ecosystem master catalog
```

---

## Key Capabilities

1. **Standardized Agent Roles (29 Agents / 30 Roles):**
   - Architectural and specialist personas spanning Master Orchestrator, Software Architect, Security Reviewer, Deep Reviewer, QA/Tester, DevOps, Documentation Engineer, and GitHub Copilot Specialist.
2. **Centralized Skills Catalog (1,371 Skills):**
   - Automated skill management covering full-stack web, cloud infrastructure (GCP/AWS/Azure), application security, performance profiling, and reverse engineering.
3. **Model Context Protocol (MCP) Foundation:**
   - 18 configured servers including `agent-team` (SQLite task tracking), `context7` (real-time documentation resolver), `browser` (Puppeteer automation), `git`, `github`, and `filesystem`.
4. **FreeLLMAPI Multi-Agent Gateway:**
   - 19 unified CLI agent wrappers (`flm-aider`, `flm-claude`, `flm-cline`, `flm-codex`, `flm-crush`, `flm-gemini`, `flm-qwen`, etc.) routing through `http://127.0.0.1:31415`.
5. **Model Routers & Gateways:**
   - Dynamic failover, quota preservation, and fallback routing across FreeLLMAPI, OmniRoute Gateway, and Qwen Antigravity Bridge.
6. **Ponytail Integration:**
   - Deterministic audit, technical debt management, rules enforcement, and automated code review lenses.

---

## Portable Quickstart & Installation

### 1. Clone the Repository
```bash
git clone https://github.com/ha4kerspidersks/AI-Dev-Team.git
cd AI-Dev-Team
```

### 2. Bootstrap the Ecosystem
Run the automated bootstrapper to detect your OS/architecture, install prerequisites, link skills, and configure runtimes:
```bash
./scripts/bootstrap.sh
```

### 3. Install CLI Wrappers (Optional)
Link `ai-team` and the `flm-*` agent wrappers into your `~/.local/bin`:
```bash
./scripts/install.sh
```

### 4. Verify System Health
Run the diagnostic doctor to confirm all components, symlinks, and runtimes are operational:
```bash
./scripts/doctor.sh
# or via CLI
ai-team doctor
```

---

## Security & Credentials

> [!IMPORTANT]
> **ZERO SECRETS ARE COMMITTED TO THIS REPOSITORY.**  
> All API keys, credentials, tokens, private keys, authentication databases, and session caches are strictly ignored by `.gitignore` and enforced via pre-commit gates.

### Configuring Local Credentials
1. Copy the safe configuration template:
   ```bash
   cp .env.example .env
   ```
2. Populate the required keys in `.env` (this file is `.gitignored`):
   ```bash
   FREELLMAPI_BASE_URL=http://127.0.0.1:31415
   FREELLMAPI_API_KEY=your_key_here
   GITHUB_TOKEN=your_github_token
   HF_TOKEN=your_huggingface_token
   OPENAI_API_KEY=your_openai_key
   ANTHROPIC_API_KEY=your_anthropic_key
   GEMINI_API_KEY=your_gemini_key
   ```
3. Audit your local repository status:
   ```bash
   git status
   # Ensure .env is never staged or committed
   ```

Detailed security verification details are available in [docs/security/GIT-SECURITY-AUDIT.md](docs/security/GIT-SECURITY-AUDIT.md).

---

## Restoration on a New Machine

To recreate this complete AI engineering environment on another computer:

```bash
git clone https://github.com/ha4kerspidersks/AI-Dev-Team.git
cd AI-Dev-Team
./scripts/restore.sh
```

`restore.sh` executes the following automated pipeline:
1. Validates `registry/manifest.yaml`.
2. Clones required upstream source repositories into `repos/`.
3. Relinks all 1,371 skills using relative and dynamically-resolved paths.
4. Restores agent protocols and MCP configurations.
5. Verifies ecosystem health with `ai-team doctor`.

---

## FreeLLMAPI Multi-Agent Integration

The ecosystem includes a complete CLI agent suite in `freellmapi-agents/bin/` backed by FreeLLMAPI:

| Agent Command | Backend Engine | Primary Focus |
| :--- | :--- | :--- |
| `flm` | Unified CLI | Master interactive agent manager & runner |
| `flm-claude` | Claude Code CLI | Deep architectural reasoning & security review |
| `flm-codex` | Codex CLI | High-speed script & tool development |
| `flm-gemini` | Gemini CLI | Large-context analysis & multimodal tasks |
| `flm-aider` | Aider | Pair programming & git-aware code edits |
| `flm-crush` | Crush / Qwen | High-efficiency local and cloud task execution |
| `flm-openclaw` | OpenClaw | Persona-based autonomous execution |
| `flm-cline` | Cline Core | VS Code and autonomous agent workflows |

Test model routing anytime:
```bash
python3 freellmapi-agents/scripts/tester.py
```

---

## Ecosystem Management CLI

The `ai-team` central command line interface controls all team functions:

```bash
ai-team status       # Check status of all AI Dev Team components & environments
ai-team doctor       # Diagnose environment health, symlinks, and runtimes
ai-team skills       # Inspect and search centralized skills (e.g. ai-team skills search api)
ai-team agents       # List standardized agent roles and ownership mapping
ai-team mcp          # Manage and inspect Global MCP Foundation (status|list|doctor|test|run)
ai-team repos        # List all installed upstream repositories and branches
ai-team memory       # Global Project Intelligence & Context Memory
ai-team qwen         # Manage Qwen Antigravity Bridge (status|start|test)
ai-team report       # Display latest audit and inventory reports
```

---

## Protected Workspaces Invariant

The following workspaces are protected development environments that remain isolated and unaffected:
- `~/Developer/LinkedIn-Audit/`
- `~/Developer/subhajitportfolio-2.0/`

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
